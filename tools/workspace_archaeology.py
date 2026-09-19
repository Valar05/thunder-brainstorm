#!/usr/bin/env python3
"""Thunder workspace archaeology: recover local repos, worktrees, tmux sessions, and at-risk work."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

try:
    from tools.turbo_survey import discover_repos, environment, survey_repo, utcnow
except ModuleNotFoundError:
    from turbo_survey import discover_repos, environment, survey_repo, utcnow

SCHEMA = "thunder.workspace-index.v1"
RECEIPT_KIND = "thunder-workspace-index"
DEFAULT_ANDROID_ROOT = Path("/storage/emulated/0/Documents/GodotProjects")
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX_RELATIVE = Path("generated/workspace/workspace_index.json")


def default_index_path() -> str:
    configured = os.environ.get("THUNDER_WORKSPACE_INDEX", "").strip()
    if configured:
        return str(Path(configured).expanduser())
    candidates = [PROJECT_ROOT / DEFAULT_INDEX_RELATIVE]
    code, out, _err = run(
        ["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
        cwd=PROJECT_ROOT,
        timeout=5,
    )
    if code == 0 and out:
        common_dir = Path(out).expanduser().resolve()
        canonical_root = common_dir.parent if common_dir.name == ".git" else PROJECT_ROOT
        canonical_index = canonical_root / DEFAULT_INDEX_RELATIVE
        if canonical_index not in candidates:
            candidates.insert(0, canonical_index)
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return str(candidates[0])
HANDOFF_RE = re.compile(r"(handoff|recovery|campaign|continuation|restore|state|receipt|commission)", re.I)
HANDOFF_EXACT = {"README.md", "AGENTS.md", "SKILL.md", "MEMORY.md", "MEMORIES.md", "PROJECT_ORIENTATION.md"}
MAX_HANDOFFS = 80


def run(cmd: list[str], cwd: Path | None = None, timeout: float = 8.0) -> tuple[int, str, str]:
    try:
        p = subprocess.run(
            cmd,
            cwd=str(cwd) if cwd else None,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            errors="replace",
            timeout=timeout,
        )
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except (OSError, subprocess.SubprocessError) as exc:
        return 127, "", repr(exc)


def git(repo: Path, *args: str, timeout: float = 8.0) -> str:
    code, out, _err = run(["git", *args], cwd=repo, timeout=timeout)
    return out if code == 0 else ""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def default_workspace_root() -> str:
    configured = os.environ.get("THUNDER_WORKSPACE_ROOT", "").strip()
    if configured:
        return configured
    if DEFAULT_ANDROID_ROOT.exists():
        return str(DEFAULT_ANDROID_ROOT)
    return str(Path.cwd().parent)


def parse_worktrees(raw: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    current: dict[str, Any] = {}
    for line in raw.splitlines() + [""]:
        if not line.strip():
            if current:
                rows.append(current)
                current = {}
            continue
        key, _, value = line.partition(" ")
        if key in {"bare", "detached", "prunable", "locked"}:
            current[key] = value or True
        else:
            current[key] = value
    return rows


def parse_branches(raw: str) -> list[dict[str, Any]]:
    out = []
    for line in raw.splitlines():
        parts = line.split("\t")
        if len(parts) < 5:
            continue
        name, upstream, track, head, committed_at = parts[:5]
        ahead = behind = 0
        ma = re.search(r"ahead (\d+)", track)
        mb = re.search(r"behind (\d+)", track)
        if ma:
            ahead = int(ma.group(1))
        if mb:
            behind = int(mb.group(1))
        out.append(
            {
                "name": name,
                "upstream": upstream,
                "track": track,
                "ahead": ahead,
                "behind": behind,
                "head": head,
                "committed_at": committed_at,
            }
        )
    return out


def collect_branch_state(repo: Path) -> list[dict[str, Any]]:
    fmt = "%(refname:short)%09%(upstream:short)%09%(upstream:track)%09%(objectname)%09%(committerdate:iso8601)"
    branches = parse_branches(git(repo, "for-each-ref", f"--format={fmt}", "refs/heads", timeout=12))
    unique_commits = set(git(repo, "rev-list", "--branches", "--not", "--remotes", timeout=20).splitlines())
    for branch in branches:
        branch["local_only"] = bool(branch.get("head") and branch["head"] in unique_commits)
    return branches


def handoff_heading(path: Path) -> str:
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            for _ in range(80):
                line = handle.readline()
                if not line:
                    break
                stripped = line.strip()
                if stripped.startswith("#"):
                    return stripped.lstrip("#").strip()[:180]
    except OSError:
        pass
    return ""


def discover_handoffs(repo: Path, max_depth: int = 5) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    skip = {".git", ".godot", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}
    for current, dirs, files in os.walk(repo):
        p = Path(current)
        try:
            depth = len(p.relative_to(repo).parts)
        except ValueError:
            depth = 0
        if depth > max_depth:
            dirs[:] = []
            continue
        dirs[:] = [d for d in dirs if d not in skip]
        for name in files:
            if name not in HANDOFF_EXACT and not HANDOFF_RE.search(name):
                continue
            path = p / name
            try:
                st = path.stat()
                rel = str(path.relative_to(repo))
            except OSError:
                continue
            out.append(
                {
                    "path": rel,
                    "bytes": st.st_size,
                    "modified_at": datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat(),
                    "heading": handoff_heading(path) if path.suffix.lower() in {".md", ".txt"} else "",
                }
            )
            if len(out) >= MAX_HANDOFFS:
                break
        if len(out) >= MAX_HANDOFFS:
            break
    out.sort(key=lambda x: x.get("modified_at", ""), reverse=True)
    return out


def collect_processes() -> dict[int, dict[str, Any]]:
    candidates = [
        ["ps", "-A", "-o", "pid=,ppid=,args="],
        ["ps", "-eo", "pid=,ppid=,args="],
    ]
    raw = ""
    for cmd in candidates:
        code, out, _err = run(cmd, timeout=5)
        if code == 0 and out:
            raw = out
            break
    result: dict[int, dict[str, Any]] = {}
    for line in raw.splitlines():
        m = re.match(r"\s*(\d+)\s+(\d+)\s+(.*)$", line)
        if not m:
            continue
        pid, ppid, args = int(m.group(1)), int(m.group(2)), m.group(3)
        result[pid] = {"pid": pid, "ppid": ppid, "args": args}
    return result


def descendants(root_pid: int, processes: dict[int, dict[str, Any]]) -> set[int]:
    children: dict[int, list[int]] = {}
    for row in processes.values():
        children.setdefault(int(row["ppid"]), []).append(int(row["pid"]))
    seen: set[int] = set()
    stack = [root_pid]
    while stack:
        pid = stack.pop()
        if pid in seen:
            continue
        seen.add(pid)
        stack.extend(children.get(pid, []))
    return seen


def collect_tmux() -> dict[str, Any]:
    exe = shutil.which("tmux")
    if not exe:
        return {"available": False, "panes": [], "sessions": []}
    fmt = "#{session_name}\t#{window_index}\t#{pane_index}\t#{pane_id}\t#{pane_pid}\t#{pane_current_path}\t#{pane_current_command}\t#{pane_title}"
    code, out, err = run([exe, "list-panes", "-a", "-F", fmt], timeout=5)
    if code != 0:
        return {"available": True, "panes": [], "sessions": [], "error": err or out}
    panes = []
    sessions: set[str] = set()
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) < 8:
            continue
        session, window, pane, pane_id, pane_pid, cwd, command, title = parts[:8]
        sessions.add(session)
        panes.append(
            {
                "session": session,
                "window": window,
                "pane": pane,
                "pane_id": pane_id,
                "pane_pid": int(pane_pid) if pane_pid.isdigit() else None,
                "cwd": cwd,
                "command": command,
                "title": title,
            }
        )
    return {"available": True, "panes": panes, "sessions": sorted(sessions)}


def parse_listener_line(line: str) -> dict[str, Any] | None:
    port_match = re.search(r"(?:^|\s)(?:\[?[0-9a-fA-F:.]*\]?):(\d+)(?:\s|$)", line)
    if not port_match:
        return None
    pids = [int(x) for x in re.findall(r"pid=(\d+)", line)]
    return {"port": int(port_match.group(1)), "pids": sorted(set(pids)), "raw": line[:500]}


def collect_listeners() -> list[dict[str, Any]]:
    commands = []
    if shutil.which("ss"):
        commands.append(["ss", "-ltnpH"])
    if shutil.which("netstat"):
        commands.append(["netstat", "-ltnp"])
    for cmd in commands:
        code, out, _err = run(cmd, timeout=5)
        if code != 0 or not out:
            continue
        rows = [x for x in (parse_listener_line(line) for line in out.splitlines()) if x]
        if rows:
            return rows
    return []


def is_inside(path: str, root: str) -> bool:
    if not path or not root:
        return False
    try:
        Path(path).resolve().relative_to(Path(root).resolve())
        return True
    except (OSError, ValueError):
        return False


def infer_ports_from_processes(pids: Iterable[int], processes: dict[int, dict[str, Any]]) -> set[int]:
    ports: set[int] = set()
    patterns = [
        r"(?:--port|-p)\s*[= ]\s*(\d{2,5})",
        r"\bPORT[=:](\d{2,5})\b",
        r"https?://[^:\s]+:(\d{2,5})",
        r"\b(?:localhost|127\.0\.0\.1):(\d{2,5})",
    ]
    for pid in pids:
        args = processes.get(pid, {}).get("args", "")
        for pat in patterns:
            for value in re.findall(pat, args, flags=re.I):
                port = int(value)
                if 1 <= port <= 65535:
                    ports.add(port)
    return ports


def runtime_for_repo(
    repo: Path,
    tmux: dict[str, Any],
    processes: dict[int, dict[str, Any]],
    listeners: list[dict[str, Any]],
) -> dict[str, Any]:
    panes = [p for p in tmux.get("panes", []) if is_inside(p.get("cwd", ""), str(repo))]
    pane_pids = {p["pane_pid"] for p in panes if p.get("pane_pid")}
    runtime_pids: set[int] = set()
    for pid in pane_pids:
        runtime_pids.update(descendants(pid, processes))
    ports = infer_ports_from_processes(runtime_pids, processes)
    for listener in listeners:
        if runtime_pids.intersection(listener.get("pids", [])):
            ports.add(int(listener["port"]))
    sessions = sorted({p["session"] for p in panes})
    return {
        "active": bool(panes),
        "tmux_sessions": sessions,
        "tmux_panes": panes,
        "process_pids": sorted(runtime_pids),
        "ports": sorted(ports),
    }


def safe_iso_max(values: Iterable[str]) -> str:
    parsed = []
    for value in values:
        if not value:
            continue
        try:
            parsed.append(datetime.fromisoformat(value.replace("Z", "+00:00")))
        except ValueError:
            continue
    return max(parsed).astimezone(timezone.utc).isoformat() if parsed else ""


def recovery_state(repo: dict[str, Any]) -> dict[str, Any]:
    status = repo.get("status") or {}
    branches = repo.get("branch_state") or []
    reasons: list[str] = []
    if status.get("conflicted"):
        reasons.append(f"conflicts:{status['conflicted']}")
    if status.get("staged"):
        reasons.append(f"staged:{status['staged']}")
    if status.get("modified"):
        reasons.append(f"modified:{status['modified']}")
    if status.get("untracked"):
        reasons.append(f"untracked:{status['untracked']}")
    if status.get("ahead"):
        reasons.append(f"unpushed:{status['ahead']}")
    if repo.get("stash_count"):
        reasons.append(f"stashes:{repo['stash_count']}")
    if not repo.get("remote"):
        reasons.append("no-remote")
    if status.get("branch") in {"", "(detached)"}:
        reasons.append("detached-head")
    local_only = [b["name"] for b in branches if b.get("local_only")]
    if local_only:
        reasons.append("local-only-branches:" + ",".join(local_only[:8]))
    lost = bool(reasons)
    if status.get("conflicted"):
        label = "AT_RISK"
    elif status.get("dirty"):
        label = "DIRTY_LOCAL_WORK"
    elif status.get("ahead") or repo.get("stash_count") or local_only:
        label = "LOCAL_ONLY_WORK"
    elif repo.get("runtime", {}).get("active"):
        label = "ACTIVE"
    else:
        label = "SYNCED_OR_UNVERIFIED"
    return {"label": label, "lost_candidate": lost, "reasons": reasons}


def enrich_repo(base: dict[str, Any], tmux: dict[str, Any], processes: dict[int, dict[str, Any]], listeners: list[dict[str, Any]]) -> dict[str, Any]:
    path = Path(base["path"])
    base["branch_state"] = collect_branch_state(path)
    base["worktree_records"] = parse_worktrees(git(path, "worktree", "list", "--porcelain"))
    base["handoffs"] = discover_handoffs(path)
    base["runtime"] = runtime_for_repo(path, tmux, processes, listeners)
    last_commit_at = (base.get("last_commit") or "").split("\t", 1)[0]
    newest_file_at = ((base.get("tree") or {}).get("newest_files") or [{}])[0].get("mtime", "")
    newest_handoff_at = (base.get("handoffs") or [{}])[0].get("modified_at", "")
    base["activity_at"] = safe_iso_max([last_commit_at, newest_file_at, newest_handoff_at])
    base["recovery"] = recovery_state(base)
    base["display_name"] = path.name
    return base


def build_index(
    roots: list[Path],
    *,
    max_depth: int,
    max_files_per_repo: int,
    workers: int,
    fetch_remotes: bool,
    include_runtime: bool,
    machine: str = "",
) -> dict[str, Any]:
    from concurrent.futures import ThreadPoolExecutor, as_completed

    env = environment()
    machine_label = machine or env.get("machine") or "unknown"
    repos = sorted({p for root in roots for p in discover_repos(root, max_depth)}, key=lambda p: str(p).lower())
    tmux = collect_tmux() if include_runtime else {"available": False, "panes": [], "sessions": []}
    processes = collect_processes() if include_runtime else {}
    listeners = collect_listeners() if include_runtime else []

    count_workers = workers or min(24, max(4, (os.cpu_count() or 4) * 2))
    surveyed: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=count_workers) as pool:
        future_map = {
            pool.submit(survey_repo, repo, max_files_per_repo, fetch_remotes): repo
            for repo in repos
        }
        for future in as_completed(future_map):
            repo = future_map[future]
            try:
                row = future.result()
                row["machine"] = machine_label
                surveyed.append(enrich_repo(row, tmux, processes, listeners))
            except Exception as exc:
                surveyed.append(
                    {
                        "machine": machine_label,
                        "path": str(repo),
                        "display_name": repo.name,
                        "error": repr(exc),
                        "recovery": {"label": "SCAN_ERROR", "lost_candidate": True, "reasons": ["scan-error"]},
                    }
                )
    surveyed.sort(key=lambda r: (not r.get("recovery", {}).get("lost_candidate", False), -(r.get("priority_score") or 0), r.get("path", "")))
    session_map = []
    for pane in tmux.get("panes", []):
        matched = [r.get("path") for r in surveyed if is_inside(pane.get("cwd", ""), r.get("path", ""))]
        session_map.append({**pane, "repo_paths": matched})
    summary = {
        "repo_count": len(surveyed),
        "lost_candidates": sum(bool(r.get("recovery", {}).get("lost_candidate")) for r in surveyed),
        "dirty": sum(bool((r.get("status") or {}).get("dirty")) for r in surveyed),
        "unpushed": sum(int((r.get("status") or {}).get("ahead", 0)) > 0 for r in surveyed),
        "with_stashes": sum(int(r.get("stash_count", 0)) > 0 for r in surveyed),
        "active_runtime": sum(bool((r.get("runtime") or {}).get("active")) for r in surveyed),
        "tmux_sessions": len(tmux.get("sessions", [])),
    }
    return {
        "schema": SCHEMA,
        "created_at": utcnow(),
        "machine": machine_label,
        "roots": [str(p.expanduser().resolve()) for p in roots],
        "fetch_remotes": fetch_remotes,
        "runtime_capture": {
            "enabled": include_runtime,
            "tmux_available": tmux.get("available", False),
            "tmux_sessions": tmux.get("sessions", []),
            "panes": session_map,
            "listener_count": len(listeners),
        },
        "summary": summary,
        "repos": surveyed,
    }


def write_index(out_dir: Path, payload: dict[str, Any]) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    index_path = out_dir / "workspace_index.json"
    jsonl_path = out_dir / "workspace_repos.jsonl"
    report_path = out_dir / "workspace_report.md"
    index_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    with jsonl_path.open("w", encoding="utf-8") as handle:
        for repo in payload["repos"]:
            handle.write(json.dumps(repo, ensure_ascii=False) + "\n")
    report_path.write_text(render_report(payload), encoding="utf-8")
    receipt = {
        "kind": RECEIPT_KIND,
        "schema": payload["schema"],
        "created_at": payload["created_at"],
        "machine": payload["machine"],
        "repo_count": len(payload["repos"]),
        "index_sha256": sha256(index_path),
        "jsonl_sha256": sha256(jsonl_path),
        "report_sha256": sha256(report_path),
    }
    (out_dir / "workspace_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    return receipt


def render_report(payload: dict[str, Any]) -> str:
    s = payload["summary"]
    lines = [
        "# Thunder Workspace Archaeology",
        "",
        f"- Created: {payload['created_at']}",
        f"- Machine: {payload['machine']}",
        f"- Repositories: {s['repo_count']}",
        f"- Lost/local-risk candidates: {s['lost_candidates']}",
        f"- Dirty: {s['dirty']}",
        f"- Unpushed: {s['unpushed']}",
        f"- Active runtimes: {s['active_runtime']}",
        "",
        "## Recovery queue",
        "",
    ]
    for repo in payload["repos"]:
        rec = repo.get("recovery", {})
        if not rec.get("lost_candidate"):
            continue
        status = repo.get("status") or {}
        lines.append(
            f"- **{repo.get('display_name')}** {repo.get('path')} "
            f"[{rec.get('label')}] branch={status.get('branch') or '?'} "
            f"+{status.get('ahead',0)}/-{status.get('behind',0)} "
            f"reasons={'; '.join(rec.get('reasons', []))}"
        )
    lines += ["", "## Active tmux", ""]
    for pane in payload.get("runtime_capture", {}).get("panes", []):
        lines.append(
            f"- {pane.get('session')}:{pane.get('window')}.{pane.get('pane')} "
            f"cwd={pane.get('cwd')} command={pane.get('command')}"
        )
    return "\n".join(lines) + "\n"


def validate_index(index_path: Path) -> dict[str, Any]:
    payload = json.loads(index_path.read_text(encoding="utf-8"))
    if payload.get("schema") != SCHEMA:
        raise SystemExit(f"Unsupported workspace index schema: {payload.get('schema')!r}")
    receipt_path = index_path.with_name("workspace_receipt.json")
    if receipt_path.exists():
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        actual = sha256(index_path)
        if receipt.get("kind") != RECEIPT_KIND or receipt.get("index_sha256") != actual:
            raise SystemExit("Workspace receipt does not match workspace_index.json")
    return payload


def match_text(repo: dict[str, Any]) -> str:
    parts = [
        repo.get("display_name", ""),
        repo.get("path", ""),
        repo.get("remote", ""),
        (repo.get("status") or {}).get("branch", ""),
        " ".join((repo.get("runtime") or {}).get("tmux_sessions", [])),
    ]
    parts.extend(h.get("path", "") for h in repo.get("handoffs", []))
    parts.extend(h.get("heading", "") for h in repo.get("handoffs", []))
    return " ".join(parts).lower()


def filter_query(repos: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    terms = [x for x in re.split(r"[^a-z0-9_.-]+", query.lower()) if x]
    return [r for r in repos if all(term in match_text(r) for term in terms)]


def target_score(repo: dict[str, Any], target: str) -> int:
    q = target.lower().strip()
    if not q:
        return 0
    name = repo.get("display_name", "").lower()
    path = repo.get("path", "").lower()
    remote = repo.get("remote", "").lower()
    branch = (repo.get("status") or {}).get("branch", "").lower()
    sessions = [x.lower() for x in (repo.get("runtime") or {}).get("tmux_sessions", [])]
    score = 0
    if q == name:
        score += 100
    if path.endswith("/" + q) or path.endswith("\\" + q):
        score += 80
    if q in name:
        score += 50
    if q in remote:
        score += 40
    if q == branch:
        score += 30
    if q in sessions:
        score += 60
    if q in match_text(repo):
        score += 10
    return score


def resolve_repo(payload: dict[str, Any], target: str) -> dict[str, Any]:
    scored = sorted(((target_score(r, target), r) for r in payload["repos"]), key=lambda x: (-x[0], x[1].get("path", "")))
    if not scored or scored[0][0] <= 0:
        raise SystemExit(f"No workspace project matched {target!r}")
    if len(scored) > 1 and scored[0][0] == scored[1][0]:
        candidates = "\n".join(f"  {r.get('display_name')}: {r.get('path')}" for score, r in scored[:8] if score == scored[0][0])
        raise SystemExit(f"Ambiguous workspace target {target!r}:\n{candidates}")
    return scored[0][1]


def repo_line(repo: dict[str, Any]) -> str:
    status = repo.get("status") or {}
    recovery = repo.get("recovery") or {}
    runtime = repo.get("runtime") or {}
    tmux = ",".join(runtime.get("tmux_sessions", [])) or "-"
    return (
        f"{repo.get('display_name','?'):<30} {recovery.get('label','?'):<18} "
        f"{status.get('branch') or '?':<28} +{status.get('ahead',0)}/-{status.get('behind',0)} "
        f"dirty={bool(status.get('dirty'))!s:<5} tmux={tmux}"
    )


def print_repos(repos: list[dict[str, Any]], as_json: bool = False) -> None:
    if as_json:
        print(json.dumps(repos, indent=2, ensure_ascii=False))
        return
    for repo in repos:
        print(repo_line(repo))
        print(f"  {repo.get('path')}")


def cmd_scan(args: argparse.Namespace) -> int:
    roots = [Path(r) for r in args.root]
    payload = build_index(
        roots,
        max_depth=args.max_depth,
        max_files_per_repo=args.max_files_per_repo,
        workers=args.workers,
        fetch_remotes=args.fetch_remotes,
        include_runtime=not args.no_runtime,
        machine=args.machine,
    )
    receipt = write_index(Path(args.out_dir), payload)
    print(json.dumps({"summary": payload["summary"], "out_dir": args.out_dir, "receipt": receipt}, indent=2))
    return 0


def load_for_args(args: argparse.Namespace) -> dict[str, Any]:
    return validate_index(Path(args.index))


def cmd_list(args: argparse.Namespace) -> int:
    payload = load_for_args(args)
    print_repos(payload["repos"], args.json)
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    repo = resolve_repo(load_for_args(args), args.target)
    print(json.dumps(repo, indent=2, ensure_ascii=False) if args.json else render_recovery(repo))
    return 0


def cmd_sessions(args: argparse.Namespace) -> int:
    payload = load_for_args(args)
    panes = payload.get("runtime_capture", {}).get("panes", [])
    if args.json:
        print(json.dumps(panes, indent=2, ensure_ascii=False))
        return 0
    for pane in panes:
        repos = ",".join(Path(x).name for x in pane.get("repo_paths", [])) or "-"
        print(f"{pane.get('session')}:{pane.get('window')}.{pane.get('pane')} {pane.get('command')} repos={repos}")
        print(f"  {pane.get('cwd')}")
    return 0


def cmd_dirty(args: argparse.Namespace) -> int:
    payload = load_for_args(args)
    print_repos([r for r in payload["repos"] if (r.get("status") or {}).get("dirty")], args.json)
    return 0


def cmd_unpushed(args: argparse.Namespace) -> int:
    payload = load_for_args(args)
    repos = []
    for r in payload["repos"]:
        status = r.get("status") or {}
        branches = r.get("branch_state") or []
        if status.get("ahead", 0) > 0 or any((b.get("ahead", 0) > 0 or b.get("local_only")) for b in branches):
            repos.append(r)
    print_repos(repos, args.json)
    return 0


def cmd_lost(args: argparse.Namespace) -> int:
    payload = load_for_args(args)
    print_repos([r for r in payload["repos"] if (r.get("recovery") or {}).get("lost_candidate")], args.json)
    return 0


def cmd_recent(args: argparse.Namespace) -> int:
    payload = load_for_args(args)
    repos = sorted(payload["repos"], key=lambda r: r.get("activity_at", ""), reverse=True)[: args.limit]
    print_repos(repos, args.json)
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    payload = load_for_args(args)
    print_repos(filter_query(payload["repos"], args.query)[: args.limit], args.json)
    return 0


def render_recovery(repo: dict[str, Any]) -> str:
    status = repo.get("status") or {}
    rec = repo.get("recovery") or {}
    runtime = repo.get("runtime") or {}
    lines = [
        f"{repo.get('display_name')}",
        f"  path       {repo.get('path')}",
        f"  remote     {repo.get('remote') or '-'}",
        f"  branch     {status.get('branch') or '-'}",
        f"  head       {repo.get('head') or '-'}",
        f"  upstream   {status.get('upstream') or '-'}",
        f"  sync       +{status.get('ahead',0)}/-{status.get('behind',0)}",
        f"  recovery   {rec.get('label')}",
        f"  reasons    {', '.join(rec.get('reasons', [])) or '-'}",
        f"  tmux       {', '.join(runtime.get('tmux_sessions', [])) or '-'}",
        f"  ports      {', '.join(str(x) for x in runtime.get('ports', [])) or '-'}",
    ]
    handoffs = repo.get("handoffs", [])[:8]
    if handoffs:
        lines.append("  handoffs")
        for item in handoffs:
            title = f" - {item['heading']}" if item.get("heading") else ""
            lines.append(f"    {item['path']}{title}")
    lines.append("  access")
    for session in runtime.get("tmux_sessions", []):
        lines.append(f"    tmux attach -t {session}")
    lines.append(f"    cd {repo.get('path')}")
    return "\n".join(lines)


def cmd_recover(args: argparse.Namespace) -> int:
    repo = resolve_repo(load_for_args(args), args.target)
    print(json.dumps(repo, indent=2, ensure_ascii=False) if args.json else render_recovery(repo))
    return 0


def add_index_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--index", default=default_index_path())
    parser.add_argument("--json", action="store_true")


def configure_parser(parent: argparse.ArgumentParser) -> None:
    sub = parent.add_subparsers(dest="workspace_command", required=True)

    scan = sub.add_parser("scan", help="Scan repos + worktrees + tmux/runtime evidence into a receipt-backed index.")
    scan.add_argument("--root", action="append", default=None, help="Workspace root. Repeatable.")
    scan.add_argument("--out-dir", default="generated/workspace")
    scan.add_argument("--machine", default="")
    scan.add_argument("--max-depth", type=int, default=8)
    scan.add_argument("--max-files-per-repo", type=int, default=25000)
    scan.add_argument("--workers", type=int, default=0)
    scan.add_argument("--fetch-remotes", action="store_true", help="Opt-in network fetch before ahead/behind evaluation.")
    scan.add_argument("--no-runtime", action="store_true", help="Skip tmux/process/listener capture.")
    scan.set_defaults(func=cmd_scan)

    listing = sub.add_parser("list", help="List indexed repositories and recovery state.")
    add_index_arg(listing)
    listing.set_defaults(func=cmd_list)

    show = sub.add_parser("show", help="Show full indexed evidence for one project.")
    show.add_argument("target")
    add_index_arg(show)
    show.set_defaults(func=cmd_show)

    sessions = sub.add_parser("sessions", help="Show tmux panes and the repos they point into.")
    add_index_arg(sessions)
    sessions.set_defaults(func=cmd_sessions)

    dirty = sub.add_parser("dirty", help="Show repos with staged, modified, untracked, or conflicted work.")
    add_index_arg(dirty)
    dirty.set_defaults(func=cmd_dirty)

    unpushed = sub.add_parser("unpushed", help="Show ahead branches or branches with commits absent from all remotes.")
    add_index_arg(unpushed)
    unpushed.set_defaults(func=cmd_unpushed)

    lost = sub.add_parser("lost", help="Show local-only/at-risk treasure that deserves recovery attention.")
    add_index_arg(lost)
    lost.set_defaults(func=cmd_lost)

    recent = sub.add_parser("recent", help="Show recently active repos by commit/file/handoff evidence.")
    recent.add_argument("--limit", type=int, default=20)
    add_index_arg(recent)
    recent.set_defaults(func=cmd_recent)

    search = sub.add_parser("search", help="Search repo/path/branch/tmux/handoff evidence.")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=20)
    add_index_arg(search)
    search.set_defaults(func=cmd_search)

    recover = sub.add_parser("recover", help="Print the evidence and exact access routes for one project.")
    recover.add_argument("target")
    add_index_arg(recover)
    recover.set_defaults(func=cmd_recover)


def normalize_scan_defaults(args: argparse.Namespace) -> None:
    if getattr(args, "workspace_command", "") == "scan" and not args.root:
        args.root = [default_workspace_root()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Thunder workspace archaeology")
    configure_parser(parser)
    args = parser.parse_args(argv)
    normalize_scan_defaults(args)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
