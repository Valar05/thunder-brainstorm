#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import mimetypes
import os
import re
import socket
import socketserver
from datetime import datetime
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, quote, unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
DOC_EXTS = {".md", ".json", ".jsonl", ".txt", ".stdout", ".html"} | IMAGE_EXTS
MAX_TEXT_CHARS = 250_000
JSONL_PAGE_SIZE = 150

LABELS = {
    "candidate_id": "Candidate",
    "theme_pitch": "Theme Pitch",
    "core_loop": "Core Loop",
    "movement_model": "Movement Model",
    "maze_generation": "Maze Generation",
    "pursuers": "Pursuers",
    "floor_modifiers": "Floor Modifiers",
    "player_upgrades": "Player Upgrades",
    "scoring_and_pressure": "Scoring And Pressure",
    "first_playable_scope": "First Playable Scope",
    "debug_and_validation": "Debug And Validation",
    "risks": "Risks",
    "implementation_recommendation": "Implementation Recommendation",
}


class ReuseTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

    def get_request(self):
        request, client_address = super().get_request()
        request.settimeout(15)
        return request, client_address


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def label_for(key: str) -> str:
    return LABELS.get(key, key.replace("_", " " ).replace("-", " " ).title())


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "section"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def safe_path(raw: str) -> Path:
    raw = unquote(raw).lstrip("/")
    path = (ROOT / raw).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError("path escapes Thunder Brainstorm root")
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(raw)
    return path


def file_kind(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".json":
        return "json"
    if suffix == ".jsonl":
        return "jsonl"
    if suffix == ".md":
        return "markdown"
    if suffix == ".html":
        return "html"
    if suffix in IMAGE_EXTS:
        return "image"
    return "text"


def image_dimensions(path: Path) -> tuple[int, int] | None:
    try:
        with path.open("rb") as handle:
            header = handle.read(32)
        if path.suffix.lower() == ".png" and header.startswith(b"\x89PNG\r\n\x1a\n"):
            return int.from_bytes(header[16:20], "big"), int.from_bytes(header[20:24], "big")
    except OSError:
        return None
    return None


def iter_docs() -> list[Path]:
    roots = [ROOT / "README.md", ROOT / "data", GENERATED]
    docs: list[Path] = []
    for start in roots:
        if not start.exists():
            continue
        if start.is_file():
            docs.append(start)
            continue
        for path in start.rglob("*"):
            if path.is_file() and (path.suffix.lower() in DOC_EXTS or path.name.endswith(".stdout")):
                docs.append(path)

    def sort_key(path: Path) -> tuple[float, str]:
        try:
            modified = path.stat().st_mtime
        except OSError:
            modified = 0.0
        return (-modified, rel(path).lower())

    return sorted(set(docs), key=sort_key)


def category_for(path: Path) -> str:
    value = rel(path)
    if value == "README.md":
        return "Orientation"
    if value.startswith("generated/page_assets/"):
        return "Page Assets"
    if value.startswith("generated/project_links/"):
        return "Project Links"
    if value.startswith("generated/session_learnings/"):
        return "Session Learnings"
    if value.startswith("generated/source_refs_manual/"):
        return "Manual Source Refs"
    if value.startswith("generated/game_stubs/"):
        return "Game Stubs"
    if value.startswith("generated/source_packets/"):
        return "Source Packets"
    if value.startswith("generated/release_packets/"):
        return "Release Packets"
    if value.startswith("generated/skills/"):
        return "Skills"
    if value.startswith("generated/assets/"):
        return "Assets"
    if "mechanic_index" in value or value.endswith("mechanic_code_source_examples.md"):
        return "Corpus Indexes"
    if value.startswith("generated/index_"):
        return "Corpus Indexes"
    if value.startswith("generated/cauldron"):
        return "Cauldron"
    if value.startswith("data/"):
        return "Pattern Data"
    return "Generated"


def file_summary(path: Path) -> str:
    size = path.stat().st_size
    kind = file_kind(path)
    if kind == "json":
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                keys = ", ".join(list(data.keys())[:6])
                return f"JSON object: {keys}" if keys else "JSON object"
            if isinstance(data, list):
                return f"JSON list with {len(data)} entries"
        except Exception:
            pass
    if kind == "jsonl":
        return "JSONL source-reference stream"
    if kind == "image":
        dims = image_dimensions(path)
        dim_text = f", {dims[0]} x {dims[1]}" if dims else ""
        return f"Image asset{dim_text}, {size:,} bytes"
    if kind == "markdown":
        return "Markdown document"
    return f"{kind.upper()} file, {size:,} bytes"


def group_docs() -> dict[str, list[Path]]:
    groups: dict[str, list[Path]] = {}
    for path in iter_docs():
        groups.setdefault(category_for(path), []).append(path)
    return groups


def default_sidebar() -> str:
    return '<div class="brand">Thunder Brainstorm</div><p class="side-note">Local document server</p><a class="side-link" href="/">Index</a>'


def layout(title: str, body: str, sidebar: str = "") -> bytes:
    full_sidebar = sidebar or default_sidebar()
    html_doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} - Thunder Brainstorm Docs</title>
<style>
:root {{ color-scheme: light; --ink:#17212b; --muted:#5e6a76; --paper:#f6f2e9; --panel:#fffdf7; --line:#d6cdbf; --line2:#eee3d5; --accent:#0b6b78; --red:#9a3f2f; --green:#536f2b; font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
* {{ box-sizing:border-box; }} html {{ scroll-behavior:smooth; }} body {{ margin:0; background:var(--paper); color:var(--ink); line-height:1.5; }}
a {{ color:var(--accent); text-decoration:none; }} a:hover {{ text-decoration:underline; }}
.shell {{ min-height:100vh; display:grid; grid-template-columns:300px minmax(0,1fr); }}
aside {{ position:sticky; top:0; height:100vh; overflow:auto; background:#ece2d4; border-right:1px solid var(--line); padding:20px 16px; }}
.brand {{ font-weight:850; color:var(--red); text-transform:uppercase; font-size:.78rem; letter-spacing:0; margin-bottom:10px; }}
.side-note {{ color:var(--muted); font-size:.84rem; margin:0 0 14px; overflow-wrap:anywhere; }}
.side-link {{ display:block; padding:7px 8px; border-left:3px solid transparent; color:#27323d; }}
.side-link:hover {{ background:rgba(11,107,120,.08); border-left-color:var(--accent); text-decoration:none; }}
main {{ min-width:0; padding:30px clamp(16px,4vw,56px) 70px; }}
header.page {{ border-bottom:1px solid var(--line); padding-bottom:20px; margin-bottom:24px; }}
h1 {{ margin:0; font-size:clamp(2rem,4vw,3.6rem); line-height:1.04; letter-spacing:0; }}
h2 {{ margin:28px 0 12px; font-size:1.36rem; letter-spacing:0; }} h3 {{ margin:0 0 10px; font-size:1rem; letter-spacing:0; }}
.subtle {{ color:var(--muted); }} .path {{ overflow-wrap:anywhere; font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.85rem; }}
.toolbar {{ display:flex; flex-wrap:wrap; gap:8px; margin:16px 0 0; }}
.button, button {{ display:inline-flex; align-items:center; justify-content:center; border:1px solid #aaa093; background:var(--panel); color:var(--ink); border-radius:6px; padding:8px 10px; font:inherit; min-height:36px; cursor:pointer; }}
.button:hover, button:hover {{ border-color:var(--accent); color:var(--accent); text-decoration:none; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:14px; align-items:start; }}
.card {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:16px; box-shadow:0 16px 36px rgba(33,31,26,.10); }}
.card h3 {{ overflow-wrap:anywhere; }} .card p {{ margin:8px 0; }}
.badge {{ display:inline-block; border:1px solid var(--line); background:#f4eadf; color:#4c5560; border-radius:6px; padding:2px 7px; font-size:.76rem; margin-right:6px; }}
.fields {{ display:grid; gap:9px; max-width:1100px; }} .field {{ display:grid; grid-template-columns:minmax(150px,220px) minmax(0,1fr); gap:16px; padding:8px 0; border-bottom:1px solid var(--line2); }} .field-key {{ color:var(--red); font-weight:800; font-size:.8rem; text-transform:uppercase; }} .field-value {{ overflow-wrap:anywhere; }}
.item-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:14px; align-items:start; }} .item {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:15px; box-shadow:0 16px 36px rgba(33,31,26,.10); }} .item .field {{ grid-template-columns:120px minmax(0,1fr); gap:12px; }}
.nested {{ border-left:3px solid var(--green); padding-left:14px; margin:8px 0; }} ol {{ padding-left:1.35rem; max-width:980px; }} li {{ margin:7px 0; }}
pre {{ white-space:pre-wrap; overflow-wrap:anywhere; background:#202a30; color:#f2efe5; border-radius:8px; padding:16px; overflow:auto; }}
.asset-preview {{ background:#111820; border:1px solid var(--line); border-radius:8px; padding:16px; overflow:auto; }}
.asset-preview img {{ display:block; max-width:100%; height:auto; margin:0 auto; image-rendering:auto; }}
.search-row {{ display:flex; flex-wrap:wrap; gap:8px; margin:14px 0 18px; }} input[type="search"] {{ flex:1 1 260px; border:1px solid #bdb3a6; background:var(--panel); color:var(--ink); border-radius:6px; padding:9px 10px; font:inherit; }}
.table {{ width:100%; border-collapse:collapse; background:var(--panel); border:1px solid var(--line); }} .table th,.table td {{ text-align:left; vertical-align:top; border-bottom:1px solid var(--line2); padding:8px; }} .table th {{ color:var(--red); font-size:.78rem; text-transform:uppercase; }}
.hidden {{ display:none; }}
@media (max-width:860px) {{ .shell {{ display:block; }} aside {{ position:static; height:auto; border-right:0; border-bottom:1px solid var(--line); }} main {{ padding:24px 14px 50px; }} .field,.item .field {{ grid-template-columns:1fr; gap:4px; }} }}
@media print {{ aside,.toolbar,.search-row {{ display:none; }} .shell {{ display:block; }} main {{ padding:0; }} .card,.item {{ box-shadow:none; break-inside:avoid; }} }}
</style>
</head>
<body><div class="shell"><aside>{full_sidebar}</aside><main>{body}</main></div></body></html>'''
    return html_doc.encode("utf-8")


def render_index() -> bytes:
    groups = group_docs()
    cards = []
    order = ["Page Assets", "Project Links", "Session Learnings", "Manual Source Refs", "Game Stubs", "Assets", "Source Packets", "Release Packets", "Skills", "Corpus Indexes", "Cauldron", "Pattern Data", "Orientation", "Generated"]
    for group in order:
        docs = groups.get(group, [])
        if not docs:
            continue
        entries = []
        for path in docs:
            r = rel(path)
            entries.append(f'''<article class="card" data-filter="{esc((r + ' ' + file_summary(path)).lower())}">
<h3>{esc(path.name)}</h3>
<p class="path">{esc(r)}</p>
<p class="subtle">{esc(file_summary(path))}</p>
<span class="badge">{esc(file_kind(path))}</span>
<div class="toolbar"><a class="button" href="/doc/{quote(r)}">View</a><a class="button" href="/raw/{quote(r)}">Raw</a></div>
</article>''')
        cards.append(f'<section><h2>{esc(group)}</h2><div class="grid">{"".join(entries)}</div></section>')
    body = f'''<header class="page"><h1>Thunder Brainstorm Docs</h1>
<p class="subtle">Browse generated game stubs, source packets, corpus reports, and index artifacts.</p>
<div class="search-row"><input id="filter" type="search" placeholder="Filter docs" aria-label="Filter docs"></div>
</header>{''.join(cards)}
<script>
const filter=document.getElementById('filter');
filter.addEventListener('input',()=>{{ const q=filter.value.trim().toLowerCase(); document.querySelectorAll('[data-filter]').forEach(card=>card.classList.toggle('hidden', !!q && !card.dataset.filter.includes(q))); }});
</script>'''
    return layout("Index", body)


def render_scalar(key: str, value: Any) -> str:
    return f'<div class="field"><div class="field-key">{esc(label_for(key))}</div><div class="field-value">{esc(value)}</div></div>'


def render_value(value: Any) -> str:
    if isinstance(value, dict):
        rows = []
        for key, child in value.items():
            if isinstance(child, (dict, list)):
                rows.append(f'<div class="nested"><h3>{esc(label_for(str(key)))}</h3>{render_value(child)}</div>')
            else:
                rows.append(render_scalar(str(key), child))
        return '<div class="fields">' + ''.join(rows) + '</div>'
    if isinstance(value, list):
        if all(not isinstance(item, dict) for item in value):
            return '<ol>' + ''.join(f'<li>{esc(item)}</li>' for item in value) + '</ol>'
        cards = []
        for item in value:
            if isinstance(item, dict):
                title = item.get("id") or item.get("label") or item.get("name") or item.get("personality") or "Entry"
                cards.append(f'<article class="item"><h3>{esc(title)}</h3>{render_value(item)}</article>')
            else:
                cards.append(f'<article class="item"><p>{esc(item)}</p></article>')
        return '<div class="item-grid">' + ''.join(cards) + '</div>'
    return f'<p>{esc(value)}</p>'


def render_json_doc(path: Path, data: Any) -> tuple[str, str]:
    if isinstance(data, dict):
        sections = []
        nav = []
        for key, value in data.items():
            section_id = slug(str(key))
            nav.append(f'<a class="side-link" href="#{section_id}">{esc(label_for(str(key)))}</a>')
            body = f'<p class="path">{esc(value)}</p>' if key == "candidate_id" else render_value(value)
            sections.append(f'<section id="{section_id}"><h2>{esc(label_for(str(key)))}</h2>{body}</section>')
        return ''.join(sections), ''.join(nav)
    return f'<pre>{esc(json.dumps(data, indent=2, ensure_ascii=False))}</pre>', ""


def render_markdown(text: str) -> str:
    blocks: list[str] = []
    in_code = False
    code_lines: list[str] = []
    list_lines: list[str] = []

    def flush_list() -> None:
        nonlocal list_lines
        if list_lines:
            blocks.append('<ul>' + ''.join(f'<li>{esc(item)}</li>' for item in list_lines) + '</ul>')
            list_lines = []

    for raw in text.splitlines():
        line = raw.rstrip("\n")
        if line.strip().startswith("```"):
            if in_code:
                blocks.append(f'<pre>{esc(chr(10).join(code_lines))}</pre>')
                code_lines = []
                in_code = False
            else:
                flush_list()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            flush_list()
            continue
        if line.startswith("### " ):
            flush_list(); blocks.append(f'<h3>{esc(line[4:])}</h3>'); continue
        if line.startswith("## " ):
            flush_list(); blocks.append(f'<h2>{esc(line[3:])}</h2>'); continue
        if line.startswith("# " ):
            flush_list(); blocks.append(f'<h2>{esc(line[2:])}</h2>'); continue
        if line.startswith("- " ):
            list_lines.append(line[2:]); continue
        blocks.append(f'<p>{esc(line)}</p>')
    flush_list()
    if code_lines:
        blocks.append(f'<pre>{esc(chr(10).join(code_lines))}</pre>')
    return ''.join(blocks)


def render_text_doc(path: Path, text_value: str) -> str:
    truncated = len(text_value) > MAX_TEXT_CHARS
    if truncated:
        text_value = text_value[:MAX_TEXT_CHARS] + "\n\n[truncated in viewer; use Raw for the full file]"
    if path.suffix.lower() == ".md":
        return render_markdown(text_value)
    return f'<pre>{esc(text_value)}</pre>'


def render_image_doc(path: Path) -> str:
    r = rel(path)
    dims = image_dimensions(path)
    dim_text = f"{dims[0]} x {dims[1]}" if dims else "unknown dimensions"
    provenance_path = ROOT / "generated" / "assets" / "asset_provenance.json"
    provenance_link = ""
    if provenance_path.exists():
        provenance_link = f'<p><a class="button" href="/doc/{quote(rel(provenance_path))}">Asset Provenance</a></p>'
    return (
        f'<div class="asset-preview"><img src="/raw/{quote(r)}" alt="{esc(path.name)}"></div>'
        f'<section><h2>Asset Details</h2><div class="fields">'
        f'{render_scalar("path", r)}'
        f'{render_scalar("dimensions", dim_text)}'
        f'{render_scalar("bytes", path.stat().st_size)}'
        f'</div>{provenance_link}</section>'
    )


def render_jsonl_doc(path: Path, query: str) -> str:
    rows = []
    total = 0
    matched = 0
    q = query.lower().strip()
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            total += 1
            if q and q not in line.lower():
                continue
            matched += 1
            if len(rows) >= JSONL_PAGE_SIZE:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                rows.append((str(total), "", "", "", line.strip()))
                continue
            mechanics = record.get("mechanics", [])
            mechanics_text = ", ".join(str(v) for v in mechanics[:4]) if isinstance(mechanics, list) else str(mechanics)
            rows.append((str(record.get("line", total)), str(record.get("project", "")), str(record.get("path", "")), mechanics_text, str(record.get("evidence", ""))))
    table_rows = ''.join(f'<tr><td>{esc(line)}</td><td>{esc(project)}</td><td class="path">{esc(path_value)}</td><td>{esc(mechanics)}</td><td>{esc(evidence)}</td></tr>' for line, project, path_value, mechanics, evidence in rows)
    return f'''<form class="search-row" method="get"><input type="search" name="q" value="{esc(query)}" placeholder="Search this JSONL index"><button type="submit">Search</button></form>
<p class="subtle">Showing {len(rows):,} rows. Matched {matched:,} of {total:,} records.</p>
<table class="table"><thead><tr><th>Line</th><th>Project</th><th>Path</th><th>Mechanics</th><th>Evidence</th></tr></thead><tbody>{table_rows}</tbody></table>'''


def render_doc(raw_path: str, query: str = "") -> bytes:
    path = safe_path(raw_path)
    r = rel(path)
    title = path.name
    kind = file_kind(path)
    nav_extra = ""
    if kind == "json":
        data = json.loads(path.read_text(encoding="utf-8"))
        content, nav_extra = render_json_doc(path, data)
    elif kind == "jsonl":
        content = render_jsonl_doc(path, query)
    elif kind == "image":
        content = render_image_doc(path)
    else:
        content = render_text_doc(path, path.read_text(encoding="utf-8", errors="replace"))
    sidebar = default_sidebar() + nav_extra
    body = f'''<header class="page"><h1>{esc(title)}</h1><p class="path">{esc(r)}</p><p class="subtle">{esc(file_summary(path))}</p><div class="toolbar"><a class="button" href="/">Index</a><a class="button" href="/raw/{quote(r)}">Raw</a><button onclick="window.print()">Print</button></div></header>{content}'''
    return layout(title, body, sidebar)


def render_raw(raw_path: str) -> tuple[bytes, str]:
    path = safe_path(raw_path)
    guessed = mimetypes.guess_type(path.name)[0]
    content_type = guessed or "text/plain; charset=utf-8"
    return path.read_bytes(), content_type


class Handler(BaseHTTPRequestHandler):
    server_version = "ThunderBrainstormDocServer/0.1"

    def log_message(self, fmt: str, *args: Any) -> None:
        stamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{stamp}] {self.client_address[0]} {fmt % args}")

    def send_bytes(self, payload: bytes, content_type: str = "text/html; charset=utf-8", status: int = 200) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def send_head_only(self, content_type: str = "text/html; charset=utf-8", status: int = 200, length: int = 0) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(length))
        self.end_headers()

    def do_HEAD(self) -> None:
        parsed = urlparse(self.path)
        try:
            if parsed.path == "/" or parsed.path == "/index.html" or parsed.path.startswith("/doc/"):
                self.send_head_only()
                return
            if parsed.path.startswith("/raw/"):
                path = safe_path(parsed.path[len("/raw/"):])
                guessed = mimetypes.guess_type(path.name)[0]
                self.send_head_only(content_type=guessed or "text/plain; charset=utf-8", length=path.stat().st_size)
                return
            if parsed.path == "/api/files":
                self.send_head_only(content_type="application/json; charset=utf-8")
                return
        except FileNotFoundError:
            self.send_head_only(status=404)
            return
        except Exception:
            self.send_head_only(status=500)
            return
        self.send_head_only(status=404)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        try:
            if parsed.path == "/" or parsed.path == "/index.html":
                self.send_bytes(render_index())
                return
            if parsed.path.startswith("/doc/"):
                query = parse_qs(parsed.query).get("q", [""])[0]
                self.send_bytes(render_doc(parsed.path[len("/doc/"):], query=query))
                return
            if parsed.path.startswith("/raw/"):
                payload, content_type = render_raw(parsed.path[len("/raw/"):])
                self.send_bytes(payload, content_type=content_type)
                return
            if parsed.path == "/api/files":
                files = [{"path": rel(path), "kind": file_kind(path), "category": category_for(path), "summary": file_summary(path)} for path in iter_docs()]
                self.send_bytes(json.dumps({"files": files}, indent=2).encode("utf-8"), "application/json; charset=utf-8")
                return
        except FileNotFoundError as exc:
            self.send_bytes(layout("Not Found", f"<h1>Not Found</h1><p>{esc(exc)}</p>"), status=404)
            return
        except (TimeoutError, socket.timeout):
            return
        except Exception as exc:
            self.send_bytes(layout("Server Error", f"<h1>Server Error</h1><pre>{esc(type(exc).__name__ + ': ' + str(exc))}</pre>"), status=500)
            return
        self.send_bytes(layout("Not Found", "<h1>Not Found</h1>"), status=404)


def main() -> int:
    parser = argparse.ArgumentParser(description="Serve Thunder Brainstorm generated documents.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=int(os.environ.get("THUNDER_DOC_PORT", "8765")))
    args = parser.parse_args()
    with ReuseTCPServer((args.host, args.port), Handler) as httpd:
        print(f"Thunder Brainstorm docs: http://{args.host}:{args.port}/")
        print(f"Root: {ROOT}")
        httpd.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
