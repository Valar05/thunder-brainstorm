#!/usr/bin/env python3
"""Thunder Brainstorm: generalized game-pattern extraction and idea generation."""
from __future__ import annotations

import argparse
import json
import os
import random
import hashlib
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent


def utc_now() -> datetime:
    return datetime.now(timezone.utc)
CARDS_PATH = ROOT / "data" / "pattern_cards.json"
OBSERVATIONS_PATH = ROOT / "data" / "source_observations.json"

STOP_DIRS = {".git", ".godot", "generated", "audio", "assets", "models", "music", "node_modules", "__pycache__"}
CODE_EXTS = {".gd", ".py", ".js", ".ts", ".tsx", ".jsx", ".vue", ".cs", ".cpp", ".h"}
DOC_NAMES = {"README.md", "PROJECT_ORIENTATION.md", "AGENTS.md"}

MECHANIC_RULES = {
    "event_clouds": ["event_cloud", "event_line", "event_seed", "domain", "reaction", "cascade", "cross_domain"],
    "deck_pressure": ["deck", "bpm", "threshold", "cadence", "draw", "outcome_attractor", "state_axis"],
    "delayed_consequences": ["followup", "follow_up", "payoff", "hook", "delayed", "echo", "memory"],
    "source_packet_generation": ["source_packet", "claude", "corpus", "packet", "transform", "motif"],
    "validation_pipeline": ["validate", "audit", "smoke", "bootstrap", "strict", "lint", "repair"],
    "text_console_runtime": ["dashboard", "console", "command", "parser", "choice", "button", "room"],
    "tts_audio_pipeline": ["tts", "audio", "manifest", "speaker", "clip", "mp3", "wav"],
    "touch_lane_combat": ["swipe", "lane", "attack", "dash", "block", "parry", "hitbox", "combo", "stomp"],
    "ai_pressure": ["ai", "conductor", "enemy", "flee", "chase", "raider", "zombie", "spawn"],
    "vehicle_survival": ["vehicle", "road", "lane", "mph", "rpm", "tire", "slip", "skid", "fuel", "chaser"],
    "asset_import_pipeline": ["import", "glb", "blend", "asset", "manifest", "attribution", "license", "source"],
    "pose_animation_tools": ["pose", "rig", "bone", "skeleton", "keyframe", "ik", "onion", "clip"],
    "resource_upgrade_loop": ["mine", "shop", "upgrade", "crystal", "resource", "harvest", "offer"],
    "web_choice_player": ["render", "localstorage", "save", "load", "choice", "html", "web", "server"],
    "writing_corpus_review": ["draft", "report", "drift", "repetition", "chunk", "critique", "original"],
}

INDEX_TEXT_EXTS = CODE_EXTS | {".md", ".json", ".godot"}
INDEX_SKIP_PARTS = {".git", ".godot", "__pycache__", "node_modules", "generated", "thunder-brainstorm", "revelation_tts_archive"}
INDEX_SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".mp3", ".ogg", ".wav", ".fbx", ".glb", ".import", ".uid", ".pyc", ".tmp"}

FOCUS_ALIASES = {
    "mobile": ["touch_lane_combat", "text_console_choice_runtime", "audio_manifest_sync"],
    "action": ["touch_lane_combat", "contact_to_duel_handoff", "survivorlike_offer_loop"],
    "combat": ["touch_lane_combat", "contact_to_duel_handoff", "multi_use_power_mutation"],
    "narrative": ["pressure_arena_event_cloud", "delayed_consequence_stack", "source_packet_pipeline"],
    "roguelike": ["pressure_arena_event_cloud", "deck_pressure_run_manager", "artifact_recipe_unlocks"],
    "corpus": ["corpus_to_mechanic_transform", "source_packet_pipeline", "validation_first_content"],
    "web": ["web_choice_player", "review_surface_browser", "validation_first_content"],
    "writing": ["nondestructive_writing_lab", "corpus_to_mechanic_transform", "source_packet_pipeline"],
    "tts": ["audio_manifest_sync", "layered_vehicle_audio_model", "text_console_choice_runtime", "validation_first_content"],
    "board": ["board_creature_ecosystem", "deck_pressure_run_manager", "artifact_recipe_unlocks"],
    "vehicle": ["highway_vehicle_survivorlike", "layered_vehicle_audio_model", "cockpit_hud_gesture_zones", "pursuer_rearm_gap", "vehicle_body_as_dungeon"],
    "driving": ["highway_vehicle_survivorlike", "cockpit_hud_gesture_zones", "pursuer_rearm_gap", "layered_vehicle_audio_model"],
    "road": ["highway_vehicle_survivorlike", "pursuer_rearm_gap", "asset_sourcing_manifest_pipeline"],
    "long-haul": ["highway_vehicle_survivorlike", "layered_vehicle_audio_model", "cockpit_hud_gesture_zones", "pursuer_rearm_gap"],
    "pose": ["pose_lab_animation_retargeting", "contact_to_duel_handoff", "touch_lane_combat"],
    "animation": ["pose_lab_animation_retargeting", "touch_lane_combat", "asset_sourcing_manifest_pipeline"],
    "mining": ["mining_shop_upgrade_microloop", "deck_pressure_run_manager", "survivorlike_offer_loop"],
}

TITLE_BITS = [
    "Pressure", "Relic", "Signal", "Ash", "Glass", "Iron", "Morrow", "Pulse", "Threshold", "Circuit",
    "Wake", "Cinder", "Vow", "Drift", "Engine", "Hollow", "Echo", "Rift", "Beacon", "Debt",
]
TITLE_NOUNS = [
    "Acolytes", "Convoy", "Citadel", "Harbor", "Pilgrims", "Circuit", "Archive", "Reactor", "Garden", "March",
    "Wardens", "Procession", "Engine", "Witnesses", "Deck", "Vault", "Frontier", "Choir", "Garrison", "Exile",
]
TONES = [
    "practical and tense", "ritualized but concrete", "systems-forward", "bleakly funny", "mythic without being vague",
    "tactile and violent", "procedural and readable", "intimate but replayable", "strange with hard rules",
]

MOTION_DUNGEON_EXPORT_ENGINES = ("threejs", "godot", "unity", "unreal")
MOTION_DUNGEON_EXPORTER_VERSION = 1


def load_cards() -> list[dict[str, Any]]:
    data = json.loads(CARDS_PATH.read_text(encoding="utf-8"))
    return data["cards"]


def save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def stable_json_text(payload: Any) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def normalize_for_hash(payload: Any) -> Any:
    if isinstance(payload, dict):
        return {key: normalize_for_hash(value) for key, value in payload.items() if key not in {"created_at", "generated_at", "updated_at"}}
    if isinstance(payload, list):
        return [normalize_for_hash(item) for item in payload]
    return payload


def stable_hash(payload: Any) -> str:
    normalized = normalize_for_hash(payload)
    canonical = json.dumps(normalized, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def write_text_atomic(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=path.parent, prefix=path.name + ".", suffix=".tmp") as handle:
        handle.write(content)
        temp_name = Path(handle.name)
    temp_name.replace(path)
    return True


def write_json_atomic(path: Path, payload: Any) -> bool:
    return write_text_atomic(path, stable_json_text(payload))


def token_set(text: str) -> set[str]:
    return {t for t in re.split(r"[^a-z0-9]+", text.lower()) if len(t) > 2}


def choose_cards(cards: list[dict[str, Any]], focus: str, rng: random.Random) -> list[dict[str, Any]]:
    by_id = {card["id"]: card for card in cards}
    focus_tokens = token_set(focus)
    pinned: list[str] = []
    for token, ids in FOCUS_ALIASES.items():
        if token in focus_tokens:
            pinned.extend(ids)

    scored: list[tuple[int, dict[str, Any]]] = []
    for card in cards:
        haystack = " ".join([
            card["id"], card["kind"], card["name"], card["summary"],
            " ".join(card.get("usable_when", [])), " ".join(card.get("ingredients", [])),
        ])
        score = len(focus_tokens & token_set(haystack))
        if card["id"] in pinned:
            score += 4
        scored.append((score, card))

    selected = [by_id[i] for i in dict.fromkeys(pinned) if i in by_id]
    candidates = [card for score, card in sorted(scored, key=lambda x: x[0], reverse=True) if score > 0 and card not in selected]
    rng.shuffle(candidates)
    selected.extend(candidates[: max(0, 5 - len(selected))])

    if len(selected) < 5:
        kinds = {card["kind"] for card in selected}
        remaining = [card for card in cards if card not in selected]
        rng.shuffle(remaining)
        for card in remaining:
            if len(selected) >= 5:
                break
            if card["kind"] not in kinds or rng.random() < 0.35:
                selected.append(card)
                kinds.add(card["kind"])

    return selected[:5]


def idea_title(rng: random.Random) -> str:
    style = rng.choice([0, 1, 2])
    if style == 0:
        return f"{rng.choice(TITLE_BITS)} {rng.choice(TITLE_NOUNS)}"
    if style == 1:
        return f"{rng.choice(TITLE_NOUNS)} of the {rng.choice(TITLE_BITS)}"
    return f"{rng.choice(TITLE_BITS)}-{rng.choice(TITLE_NOUNS)}"


def build_pitch(cards: list[dict[str, Any]], focus: str, rng: random.Random) -> dict[str, Any]:
    structures = [c for c in cards if c["kind"] in {"structure", "system", "premise"}]
    workflows = [c for c in cards if c["kind"] in {"workflow", "tooling"}]
    interfaces = [c for c in cards if c["kind"] in {"interface", "control", "presentation"}]
    lead = rng.choice(structures or cards)
    interface = rng.choice(interfaces or cards)
    workflow = rng.choice(workflows or cards)

    verbs = ["authorize", "survive", "interpret", "route", "interrupt", "repair", "commit", "trade", "extract", "withstand"]
    nouns = ["pressure", "debt", "signals", "bodies", "routes", "relics", "reports", "storms", "offers", "thresholds"]
    loop_steps = [
        f"Read a concrete situation shaped by {lead['name'].lower()}.",
        f"Choose how to {rng.choice(verbs)} the {rng.choice(nouns)} through {interface['name'].lower()}.",
        "Spend, gain, or contaminate one visible state axis.",
        f"Let {rng.choice(cards)['name'].lower()} alter the next draw or route.",
        "Resolve a later echo that proves the previous choice mattered."
    ]

    systems = []
    for card in cards[:4]:
        ingredient = rng.choice(card.get("ingredients", [card["name"]]))
        if card["kind"] in {"workflow", "tooling"}:
            systems.append(f"{card['name']}: make {ingredient} a production constraint with a visible review or validation step.")
        else:
            systems.append(f"{card['name']}: make {ingredient} a player-facing rule, not just lore.")

    validation = [
        "Create a tiny schema for rooms/events/actions before writing content.",
        "Generate 6-10 sample records and run an action-ID/dangling-reference audit.",
        "Build one review surface or CLI output that shows state before and after each choice.",
        f"Prototype the riskiest piece first: {rng.choice(sum([c.get('risks', []) for c in cards], []))}."
    ]

    return {
        "title": idea_title(rng),
        "focus": focus or "open",
        "tone": rng.choice(TONES),
        "core_fantasy": f"The player inhabits this premise: {lead['summary'][0].lower() + lead['summary'][1:]}",
        "pattern_stack": [c["id"] for c in cards],
        "player_loop": loop_steps,
        "signature_systems": systems,
        "content_pipeline": [
            f"Start from {workflow['name'].lower()}.",
            "Keep prose, mechanics, and validation as separate artifacts.",
            "Accept content only when choices produce readable state changes and later consequences."
        ],
        "prototype_scope": [
            "One arena or board state.",
            "Three repeatable event templates.",
            "Two resource axes and one delayed consequence queue.",
            "One review command that prints why each event was selected."
        ],
        "validation_plan": validation,
        "design_questions": rng.sample(sum([c.get("questions", []) for c in cards], []), k=min(5, sum(len(c.get("questions", [])) for c in cards))),
        "early_risks": rng.sample(sum([c.get("risks", []) for c in cards], []), k=min(4, sum(len(c.get("risks", [])) for c in cards)))
    }


def cmd_list(args: argparse.Namespace) -> int:
    cards = load_cards()
    for card in cards:
        if args.kind and card["kind"] != args.kind:
            continue
        print(f"{card['id']} [{card['kind']}] {card['name']}")
        if args.verbose:
            print(f"  {card['summary']}")
            print(f"  ingredients: {', '.join(card.get('ingredients', []))}")
    return 0


def cmd_generate(args: argparse.Namespace) -> int:
    cards = load_cards()
    rng = random.Random(args.seed)
    ideas = []
    for _ in range(args.count):
        chosen = choose_cards(cards, args.focus or "", rng)
        ideas.append(build_pitch(chosen, args.focus or "open", rng))
    if args.out:
        save_json(Path(args.out), {"ideas": ideas})
    print(json.dumps({"ideas": ideas}, indent=2, ensure_ascii=False))
    return 0


def inspect_local(root: Path) -> dict[str, Any]:
    file_counts: Counter[str] = Counter()
    docs: list[str] = []
    schema_keys: Counter[str] = Counter()
    identifiers: Counter[str] = Counter()
    project_dirs: set[str] = set()

    for current, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in STOP_DIRS]
        rel_current = Path(current).relative_to(root)
        if len(rel_current.parts) > 4:
            dirs[:] = []
            continue
        for name in files:
            path = Path(current) / name
            suffix = path.suffix.lower()
            file_counts[suffix or "<none>"] += 1
            rel = str(path.relative_to(root))
            if name in DOC_NAMES or "/docs/" in rel or "/.agent-memory/" in rel:
                docs.append(rel)
            if name == "project.godot" and rel_current.parts:
                project_dirs.add(rel_current.parts[0])
            if suffix == ".json":
                try:
                    data = json.loads(path.read_text(encoding="utf-8"))
                except Exception:
                    continue
                for key in top_keys(data):
                    schema_keys[key] += 1
            if suffix in CODE_EXTS:
                try:
                    text = path.read_text(encoding="utf-8", errors="ignore")[:20000]
                except Exception:
                    continue
                for ident in re.findall(r"(?:func|def|function)\s+([A-Za-z_][A-Za-z0-9_]*)", text):
                    identifiers[ident] += 1

    tags = infer_tags(schema_keys, identifiers, docs)
    return {
        "root": str(root),
        "project_dirs_with_project_godot": sorted(project_dirs),
        "file_counts_by_extension": dict(file_counts.most_common(30)),
        "doc_count": len(docs),
        "representative_docs": docs[:80],
        "top_schema_keys": dict(schema_keys.most_common(80)),
        "top_identifiers": dict(identifiers.most_common(80)),
        "inferred_pattern_tags": tags,
    }


def top_keys(data: Any) -> list[str]:
    if isinstance(data, dict):
        keys = list(data.keys())
        nested = []
        for value in data.values():
            if isinstance(value, list) and value and isinstance(value[0], dict):
                nested.extend(value[0].keys())
        return keys[:40] + nested[:30]
    if isinstance(data, list) and data and isinstance(data[0], dict):
        return list(data[0].keys())[:40]
    return []


def infer_tags(schema_keys: Counter[str], identifiers: Counter[str], docs: list[str]) -> list[str]:
    haystack = " ".join(list(schema_keys) + list(identifiers) + docs).lower()
    rules = {
        "event-cloud": ["event_lines", "event_seeds", "domain"],
        "deck-pressure": ["deck", "threshold", "bpm"],
        "delayed-consequence": ["followup", "payoff", "hook"],
        "touch-combat": ["swipe", "attack", "dash", "block"],
        "source-packet": ["source_packet", "corpus", "packet"],
        "tts": ["tts", "audio", "manifest"],
        "web-choice": ["localstorage", "choice", "render"],
        "validation": ["validate", "audit", "smoke"],
    }
    tags = []
    for tag, needles in rules.items():
        if any(n in haystack for n in needles):
            tags.append(tag)
    return tags


def cmd_inspect_local(args: argparse.Namespace) -> int:
    payload = inspect_local(Path(args.root).resolve())
    if args.out:
        save_json(Path(args.out), payload)
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


def cmd_inspect_gh(args: argparse.Namespace) -> int:
    command = ["gh", "repo", "list", args.owner, "--limit", str(args.limit), "--json", "name,description,primaryLanguage,isPrivate,updatedAt,url"]
    repos = json.loads(subprocess.check_output(command).decode())
    observed = []
    for repo in repos:
        name = repo["name"]
        top_level: list[str] = []
        if not args.no_contents:
            try:
                raw = subprocess.check_output(["gh", "api", f"/repos/{args.owner}/{name}/contents", "--jq", ".[ ].name"], stderr=subprocess.DEVNULL, timeout=10).decode()
                top_level = raw.splitlines()
            except Exception:
                top_level = []
        observed.append({
            "name": name,
            "description": repo.get("description") or "",
            "primary_language": (repo.get("primaryLanguage") or {}).get("name"),
            "is_private": repo.get("isPrivate"),
            "updated_at": repo.get("updatedAt"),
            "url": repo.get("url"),
            "top_level_signals": [x for x in top_level if x in {"README.md", "project.godot", "package.json", "docs", "tools", "scripts", "scenes", "src", "assets"} or x.endswith((".gd", ".js", ".py", ".cs", ".cpp", ".vue"))][:30]
        })
    payload = {"owner": args.owner, "policy": "metadata and top-level file names only; no source bodies copied", "repos": observed}
    if args.out:
        save_json(Path(args.out), payload)
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


def surface_path_score(path: str) -> tuple[int, list[str]]:
    lowered = path.lower()
    name = Path(path).name
    score = 0
    reasons: list[str] = []

    if name == "README.md":
        score += 100
        reasons.append("root readme")
    if name == "PROJECT_ORIENTATION.md":
        score += 96
        reasons.append("project orientation")
    if name == "state.md":
        score += 94
        reasons.append("authoritative state")
    if name == "package.json":
        score += 92
        reasons.append("package contract")
    if lowered.endswith(".openai/hosting.json") or lowered.endswith("hosting.json") and "/.openai/" in f"/{lowered}":
        score += 90
        reasons.append("hosting contract")
    if name == "project.godot":
        score += 88
        reasons.append("godot project contract")
    if lowered == "app/page.tsx":
        score += 120
        reasons.append("core runtime")
    if lowered == "app/layout.tsx":
        score += 112
        reasons.append("app shell")
    if lowered.startswith("app/api/"):
        score += 22
        reasons.append("api route")
    if lowered.startswith("app/"):
        score += 84
        reasons.append("runtime surface")
    if lowered.startswith("projects/"):
        score += 82
        reasons.append("child manifest surface")
    if "/docs/" in f"/{lowered}":
        score += 76
        reasons.append("documentation surface")
    if lowered.startswith("scripts/"):
        score += 72
        reasons.append("tooling surface")
    if lowered.startswith("tests/"):
        score += 70
        reasons.append("test surface")
    if lowered.startswith("tools/"):
        score += 68
        reasons.append("helper tooling")
    if "/scenes/" in f"/{lowered}" or lowered.endswith("-scene.tsx") or lowered.endswith("-room.tsx") or lowered.endswith("-lab.tsx"):
        score += 64
        reasons.append("scene carrier")
    if any(bit in lowered for bit in ["timeline", "export", "voice", "audio", "shader", "glsl", "tween", "share", "manifest"]):
        score += 12
        reasons.append("motion surface")
    if any(bit in lowered for bit in ["readme", "state", "orientation", "manifest", "config", "page", "server", "worker"]):
        score += 8
        reasons.append("contract surface")
    if Path(path).suffix.lower() in INDEX_TEXT_EXTS or name in DOC_NAMES or name == "project.godot":
        score += 4
        reasons.append("indexable text")
    return score, reasons


def mine_gh_repo_surface(
    *,
    owner: str,
    repo: str,
    ref: str,
    max_files: int,
    include_generated: bool,
    out_dir: Path,
) -> tuple[dict[str, Any], Path]:
    metadata = json.loads(subprocess.check_output([
        "gh", "repo", "view", f"{owner}/{repo}",
        "--json", "name,description,updatedAt,visibility,isPrivate,url,defaultBranchRef,homepageUrl",
    ]).decode())
    branch = ((metadata.get("defaultBranchRef") or {}).get("name")) or ref or "HEAD"
    tree = github_api_json(f"/repos/{owner}/{repo}/git/trees/{branch}?recursive=1")
    candidates: list[dict[str, Any]] = []
    for item in tree.get("tree", []):
        if item.get("type") != "blob":
            continue
        path = item.get("path", "")
        score, reasons = surface_path_score(path)
        if not score:
            continue
        if not should_index_path(path, include_generated=include_generated) and score < 64:
            continue
        candidates.append({
            "path": path,
            "mode": item.get("mode", ""),
            "sha": item.get("sha", ""),
            "size": item.get("size", 0),
            "score": score,
            "reasons": reasons,
        })

    candidates.sort(key=lambda item: (-item["score"], item["path"]))
    selected = candidates[:max_files]
    records: list[dict[str, Any]] = []
    file_rows: list[dict[str, Any]] = []
    for entry in selected:
        path = entry["path"]
        try:
            text = github_fetch_file(owner, repo, path)
        except Exception:
            entry["status"] = "fetch-failed"
            file_rows.append(entry)
            continue
        entry["status"] = "fetched"
        entry["line_count"] = len(text.splitlines())
        entry["byte_count"] = len(text.encode("utf-8", errors="ignore"))
        entry["mechanics"] = []
        if Path(path).suffix.lower() in INDEX_TEXT_EXTS or Path(path).name in DOC_NAMES or Path(path).name == "project.godot":
            file_records = index_text_content(
                origin="github",
                project=repo,
                repo=f"{owner}/{repo}",
                path=path,
                text=text,
                source_url_base=f"https://github.com/{owner}/{repo}/blob/{branch}/{path}",
            )
            records.extend(file_records)
            entry["mechanics"] = sorted({mechanic for record in file_records for mechanic in record.get("mechanics", [])})
            entry["source_line_refs"] = [record.get("source_url") for record in file_records[:8]]
        file_rows.append(entry)

    summary = summarize_index(records)
    payload = {
        "repo": f"{owner}/{repo}",
        "branch": branch,
        "metadata": metadata,
        "policy": "read-only GitHub repo surface mining; no body cloning beyond selected surface files",
        "selected_file_count": len(file_rows),
        "selected_files": file_rows,
        "mechanic_summary": summary,
    }
    repo_dir = out_dir / repo
    save_json(repo_dir / "repo_surface.json", payload)
    write_jsonl(repo_dir / "mechanic_source_refs.jsonl", records)
    report_lines = [
        f"# Repo Surface Mining: {owner}/{repo}",
        "",
        f"- Branch: {branch}",
        f"- Visibility: {(metadata.get('visibility') or 'unknown').lower()}",
        f"- Updated: {metadata.get('updatedAt') or 'unknown'}",
        f"- Homepage: {metadata.get('homepageUrl') or 'none'}",
        f"- Description: {metadata.get('description') or 'none'}",
        f"- Selected surface files: {len(file_rows)}",
        f"- Indexed evidence records: {summary['record_count']}",
        "",
        "## Ranked Surface Files",
        "",
    ]
    for entry in file_rows:
        mechanics = ", ".join(entry.get("mechanics", [])) or "none"
        reasons = ", ".join(entry.get("reasons", [])) or "surface match"
        report_lines.append(f"- {entry['path']} | score={entry['score']} | {reasons} | mechanics={mechanics}")
    report_lines.extend([
        "",
        "## Mechanic Counts",
        "",
    ])
    for mechanic, count in summary["by_mechanic"].items():
        report_lines.append(f"- {mechanic}: {count}")
    report_lines.extend([
        "",
        "## Next Excavation Targets",
        "",
    ])
    for entry in file_rows[:8]:
        report_lines.append(f"- {entry['path']}")
    repo_dir.mkdir(parents=True, exist_ok=True)
    (repo_dir / "repo_surface_report.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    save_json(repo_dir / "repo_surface.done.json", {
        "repo": payload["repo"],
        "branch": payload["branch"],
        "selected_file_count": payload["selected_file_count"],
        "indexed_records": summary["record_count"],
        "status": "ok",
    })
    return payload, repo_dir


def cmd_mine_gh_repo(args: argparse.Namespace) -> int:
    payload, _ = mine_gh_repo_surface(
        owner=args.owner,
        repo=args.repo,
        ref=args.ref,
        max_files=args.max_files,
        include_generated=args.include_generated,
        out_dir=Path(args.out_dir),
    )
    if args.quiet:
        top = ", ".join(f"{k}={v}" for k, v in list(payload["mechanic_summary"]["by_mechanic"].items())[:5]) or "no mechanics"
        print(f"{payload['repo']} :: {payload['selected_file_count']} files :: {payload['mechanic_summary']['record_count']} records :: {top}")
    else:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


def cmd_mine_gh_owner(args: argparse.Namespace) -> int:
    repos = json.loads(subprocess.check_output([
        "gh", "repo", "list", args.owner, "--limit", str(args.limit),
        "--json", "name,updatedAt,visibility,isPrivate,url,description,defaultBranchRef,homepageUrl",
    ]).decode())
    out_root = Path(args.out_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    summary_path = out_root / f"{args.owner}_overnight_summary.jsonl"
    allow = set(args.allow_repo or [])
    deny = set(args.deny_repo or [])
    aggregate = {
        "owner": args.owner,
        "limit": args.limit,
        "repo_count": 0,
        "selected_file_count": 0,
        "indexed_records": 0,
        "mechanic_counts": Counter(),
        "repos": [],
        "skipped": [],
    }
    mode = "a" if args.resume and summary_path.exists() else "w"
    with summary_path.open(mode, encoding="utf-8") as summary_handle:
        for index, repo_info in enumerate(repos, start=1):
            repo = repo_info["name"]
            if allow and repo not in allow:
                aggregate["skipped"].append({"repo": repo, "reason": "not-allowed"})
                continue
            if repo in deny:
                aggregate["skipped"].append({"repo": repo, "reason": "denied"})
                continue
            repo_dir = out_root / repo
            if args.skip_existing and (repo_dir / "repo_surface.done.json").exists():
                if not args.quiet:
                    print(f"[{index}/{len(repos)}] {repo} skipped")
                aggregate["skipped"].append({"repo": repo, "reason": "checkpoint-exists"})
                continue
            try:
                command = [
                    sys.executable,
                    str(Path(__file__).resolve()),
                    "mine-gh-repo",
                    "--owner",
                    args.owner,
                    "--repo",
                    repo,
                    "--ref",
                    args.ref,
                    "--out-dir",
                    args.out_dir,
                    "--max-files",
                    str(args.max_files),
                    "--quiet",
                ]
                if args.include_generated:
                    command.append("--include-generated")
                subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    timeout=args.per_repo_timeout,
                    check=True,
                )
                payload = json.loads((repo_dir / "repo_surface.json").read_text(encoding="utf-8"))
            except Exception as exc:
                record = {
                    "repo": f"{args.owner}/{repo}",
                    "status": "failed",
                    "error": str(exc),
                }
                summary_handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                summary_handle.flush()
                aggregate["skipped"].append({"repo": repo, "reason": "failed", "error": str(exc)})
                if not args.quiet:
                    print(f"[{index}/{len(repos)}] {repo} failed: {exc}")
                continue

            record = {
                "repo": payload["repo"],
                "branch": payload["branch"],
                "selected_file_count": payload["selected_file_count"],
                "indexed_records": payload["mechanic_summary"]["record_count"],
                "top_mechanics": list(payload["mechanic_summary"]["by_mechanic"].items())[:10],
                "status": "ok",
            }
            summary_handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            summary_handle.flush()
            aggregate["repo_count"] += 1
            aggregate["selected_file_count"] += payload["selected_file_count"]
            aggregate["indexed_records"] += payload["mechanic_summary"]["record_count"]
            aggregate["repos"].append(record)
            aggregate["mechanic_counts"].update(payload["mechanic_summary"]["by_mechanic"])
            if not args.quiet:
                top = ", ".join(f"{k}={v}" for k, v in list(payload["mechanic_summary"]["by_mechanic"].items())[:5]) or "no mechanics"
                print(f"[{index}/{len(repos)}] {repo}: {payload['selected_file_count']} files, {payload['mechanic_summary']['record_count']} records :: {top}")

    aggregate_payload = {
        "owner": args.owner,
        "limit": args.limit,
        "repo_count": aggregate["repo_count"],
        "selected_file_count": aggregate["selected_file_count"],
        "indexed_records": aggregate["indexed_records"],
        "mechanic_counts": dict(aggregate["mechanic_counts"].most_common()),
        "skipped": aggregate["skipped"],
        "summary_path": str(summary_path),
    }
    save_json(out_root / f"{args.owner}_overnight_summary.json", aggregate_payload)
    if args.quiet:
        print(f"{args.owner} overnight summary: {aggregate_payload['repo_count']} repos, {aggregate_payload['selected_file_count']} files, {aggregate_payload['indexed_records']} records")
    else:
        print(json.dumps(aggregate_payload, indent=2, ensure_ascii=False))
    return 0


def build_critical_manifest(
    *,
    summary: dict[str, Any],
    summary_path: Path,
    summary_jsonl_path: Path,
    signals: list[str],
) -> dict[str, Any]:
    rows = read_jsonl(summary_jsonl_path)
    ok_rows = [row for row in rows if row.get("status") == "ok"]

    mechanic_stats: dict[str, dict[str, Any]] = defaultdict(lambda: {
        "record_count": 0,
        "repos": set(),
        "repo_hits": Counter(),
    })
    for row in ok_rows:
        repo = row.get("repo", "")
        for mechanic, count in row.get("top_mechanics", []):
            stats = mechanic_stats[mechanic]
            stats["record_count"] += int(count)
            stats["repos"].add(repo)
            stats["repo_hits"][repo] += int(count)

    ranked_mechanics: list[dict[str, Any]] = []
    for mechanic, stats in sorted(
        mechanic_stats.items(),
        key=lambda item: (-len(item[1]["repos"]), -item[1]["record_count"], item[0]),
    ):
        breadth = len(stats["repos"])
        if breadth >= 60:
            tier = "core"
        elif breadth >= 35:
            tier = "shared"
        elif breadth >= 15:
            tier = "specialized"
        else:
            tier = "edge"
        ranked_mechanics.append({
            "mechanic": mechanic,
            "tier": tier,
            "repo_breadth": breadth,
            "record_count": stats["record_count"],
            "top_repos": [
                {"repo": repo, "records": count}
                for repo, count in stats["repo_hits"].most_common(5)
            ],
        })

    top_repos = sorted(
        ok_rows,
        key=lambda row: (-row.get("indexed_records", 0), -len(row.get("top_mechanics", [])), row.get("repo", "")),
    )
    critical_repos = []
    for row in top_repos[:12]:
        critical_repos.append({
            "repo": row.get("repo", ""),
            "selected_file_count": row.get("selected_file_count", 0),
            "indexed_records": row.get("indexed_records", 0),
            "top_mechanics": row.get("top_mechanics", [])[:5],
        })

    failed_repos = [
        {
            "repo": item.get("repo", ""),
            "error": item.get("error", ""),
        }
        for item in summary.get("skipped", [])
        if item.get("reason") == "failed"
    ]

    knowledge_capture = {
        "rules": [
            "Rank breadth across repos ahead of raw record count when the goal is corpus-wide leverage.",
            "Use existing summary artifacts as the source of truth; do not reread the source corpus by hand.",
            "Keep failed repos visible as a retry queue instead of folding them into the success counts.",
        ],
        "patterns": [
            "ai_pressure, asset_import_pipeline, tts_audio_pipeline, web_choice_player, and pose_animation_tools form the cross-corpus core.",
            "source_packet_generation and validation_pipeline are the ingestion and correctness spine.",
            "text_console_runtime, touch_lane_combat, and writing_corpus_review sit in the gameplay/content adaptation layer.",
        ],
        "design_decisions": [
            "A blender command is more useful than a static note because it can be rerun against updated summary files.",
            "Markdown plus JSON gives both human triage and machine reuse without duplicating the source corpus.",
        ],
        "discoveries": [
            f"{summary.get('repo_count', 0)} repos mined with {summary.get('selected_file_count', 0)} files and {summary.get('indexed_records', 0)} records.",
            f"{len(failed_repos)} repos still need retry or inspection.",
        ],
    }
    friction_audit = {
        "missing_scripts": [
            "No dedicated critical-manifest blender existed before this pass.",
        ],
        "missing_tools": [
            "No single artifact was blending repo mining with the live external pipelines the user named.",
        ],
        "missing_tests": [
            "No regression had been proving that the leverage ranking stayed stable as new summary files arrived.",
        ],
        "missing_documentation": [
            "No manifest documented why breadth-first mechanics outrank raw record counts for triage.",
        ],
        "missing_automation": [
            "The four failed repos needed an explicit retry queue instead of disappearing into the aggregate summary.",
        ],
    }

    return {
        "title": "Critical Thunder Manifest",
        "owner": summary.get("owner", ""),
        "created_at": utc_now().isoformat(timespec="seconds") + "Z",
        "inputs": {
            "summary_path": str(summary_path),
            "summary_jsonl_path": str(summary_jsonl_path),
            "signals": signals,
        },
        "coverage": {
            "repo_limit": summary.get("limit", 0),
            "repos_mined": summary.get("repo_count", 0),
            "selected_files": summary.get("selected_file_count", 0),
            "indexed_records": summary.get("indexed_records", 0),
            "failed_repos": len(failed_repos),
        },
        "critical_mechanics": ranked_mechanics[:15],
        "critical_repos": critical_repos,
        "failed_repos": failed_repos,
        "knowledge_capture": knowledge_capture,
        "friction_audit": friction_audit,
        "next_build": [
            "Turn the top breadth mechanics into canonical pattern cards and process notes.",
            "Re-run the owner miner only for the failed repos, then regenerate the manifest.",
            "Blend in the other already-running pipelines once their artifact paths are known.",
        ],
    }


def render_critical_manifest(manifest: dict[str, Any]) -> str:
    lines = [
        "# Critical Thunder Manifest",
        "",
        f"- Owner: {manifest.get('owner') or 'unknown'}",
        f"- Created: {manifest.get('created_at') or 'unknown'}",
        f"- Source fingerprint: {manifest.get('source_fingerprint') or 'unknown'}",
        f"- Repos mined: {manifest.get('coverage', {}).get('repos_mined', 0)} / {manifest.get('coverage', {}).get('repo_limit', 0)}",
        f"- Files selected: {manifest.get('coverage', {}).get('selected_files', 0)}",
        f"- Records indexed: {manifest.get('coverage', {}).get('indexed_records', 0)}",
        f"- Failed repos: {manifest.get('coverage', {}).get('failed_repos', 0)}",
        "",
        "## Blender Inputs",
        "",
    ]
    for signal in manifest.get("inputs", {}).get("signals", []):
        lines.append(f"- {signal}")
    if not manifest.get("inputs", {}).get("signals"):
        lines.append("- none recorded")

    lines.extend([
        "",
        "## Critical Mechanics",
        "",
        "| Rank | Mechanic | Tier | Repo breadth | Records | Anchor repos |",
        "| --- | --- | --- | --- | --- | --- |",
    ])
    for index, item in enumerate(manifest.get("critical_mechanics", []), start=1):
        anchors = ", ".join(
            f"{repo_hit['repo']}={repo_hit['records']}"
            for repo_hit in item.get("top_repos", [])[:3]
        ) or "none"
        lines.append(
            f"| {index} | {item.get('mechanic', '')} | {item.get('tier', '')} | {item.get('repo_breadth', 0)} | {item.get('record_count', 0)} | {anchors} |"
        )

    lines.extend([
        "",
        "## Critical Repos",
        "",
        "| Repo | Files | Records | Leading mechanics |",
        "| --- | --- | --- | --- |",
    ])
    for item in manifest.get("critical_repos", []):
        mechanics = ", ".join(
            f"{mech[0]}={mech[1]}"
            for mech in item.get("top_mechanics", [])
        ) or "none"
        lines.append(
            f"| {item.get('repo', '')} | {item.get('selected_file_count', 0)} | {item.get('indexed_records', 0)} | {mechanics} |"
        )

    lines.extend([
        "",
        "## Failed Repos / Retry Queue",
        "",
    ])
    failed_repos = manifest.get("failed_repos", [])
    if failed_repos:
        for item in failed_repos:
            lines.append(f"- {item.get('repo', '')}: {item.get('error', '')}")
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Knowledge Capture",
        "",
    ])
    knowledge = manifest.get("knowledge_capture", {})
    for section in ("rules", "patterns", "design_decisions", "discoveries"):
        lines.append(f"### {section.replace('_', ' ').title()}")
        for entry in knowledge.get(section, []):
            lines.append(f"- {entry}")
        lines.append("")

    lines.extend([
        "## Friction Audit",
        "",
    ])
    friction = manifest.get("friction_audit", {})
    for section in ("missing_scripts", "missing_tools", "missing_tests", "missing_documentation", "missing_automation"):
        lines.append(f"### {section.replace('_', ' ').title()}")
        for entry in friction.get(section, []):
            lines.append(f"- {entry}")
        lines.append("")

    lines.extend([
        "## Next Build",
        "",
    ])
    for item in manifest.get("next_build", []):
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def cmd_critical_manifest(args: argparse.Namespace) -> int:
    out_root = Path(args.out_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    summary_path = Path(args.summary) if args.summary else None
    if summary_path is None:
        candidates = sorted(Path(args.source_root).glob("*_overnight_summary.json"))
        if not candidates:
            raise SystemExit(f"No overnight summary found under {args.source_root}")
        summary_path = candidates[-1]
    summary_jsonl_path = Path(args.summary_jsonl) if args.summary_jsonl else summary_path.with_suffix(".jsonl")
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    manifest = build_critical_manifest(
        summary=summary,
        summary_path=summary_path,
        summary_jsonl_path=summary_jsonl_path,
        signals=args.signal or [],
    )
    save_json(out_root / "critical_thunder_manifest.json", manifest)
    (out_root / "critical_thunder_manifest.md").write_text(render_critical_manifest(manifest), encoding="utf-8")
    if args.quiet:
        top = ", ".join(item["mechanic"] for item in manifest["critical_mechanics"][:5]) or "no mechanics"
        print(f"{manifest['owner']} critical manifest: {manifest['coverage']['repos_mined']} repos, {manifest['coverage']['indexed_records']} records :: {top}")
    else:
        print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0


def motion_dungeon_unit_role(path: str) -> str:
    lowered = path.lower()
    if path == "app/page.tsx":
        return "composition_core"
    if path == "state.md":
        return "composition_bible"
    if path == "README.md":
        return "source_contract"
    if lowered.startswith("app/scenes/"):
        return "source_locked_scene"
    if lowered.startswith("app/api/"):
        return "service_lane"
    if lowered.startswith("projects/"):
        return "performance_record"
    if lowered.endswith(".css"):
        return "presentation_skin"
    if lowered.endswith(".json"):
        return "structured_record"
    return "supporting_surface"


def motion_dungeon_evidence(
    records: list[dict[str, Any]],
    needles: list[str],
    *,
    limit: int = 3,
    path_prefixes: list[str] | None = None,
) -> list[dict[str, Any]]:
    wanted = [needle.lower() for needle in needles]
    prefixes = [prefix.lower() for prefix in (path_prefixes or [])]
    hits: list[dict[str, Any]] = []
    seen: set[tuple[str, int, str]] = set()
    for record in records:
        path = str(record.get("path", ""))
        if prefixes and not any(path.lower().startswith(prefix) for prefix in prefixes):
            continue
        haystack = " ".join([
            path,
            str(record.get("symbol", "")),
            str(record.get("evidence", "")),
            str(record.get("source_url", "")),
        ]).lower()
        if wanted and not any(needle in haystack for needle in wanted):
            continue
        key = (path, int(record.get("line", 0) or 0), str(record.get("source_url", "")))
        if key in seen:
            continue
        seen.add(key)
        hits.append({
            "path": path,
            "line": record.get("line", 0),
            "source_url": record.get("source_url", ""),
            "mechanics": record.get("mechanics", []),
            "evidence": record.get("evidence", ""),
        })
        if len(hits) >= limit:
            break
    return hits


def build_motion_dungeon_composition_manifest(
    *,
    repo_surface: dict[str, Any],
    critical_manifest: dict[str, Any],
    source_refs: list[dict[str, Any]],
    summary_path: Path,
    critical_manifest_path: Path,
    repo_surface_path: Path,
    source_refs_path: Path,
    engines: list[str],
) -> dict[str, Any]:
    breadth_by_mechanic = {
        item.get("mechanic", ""): int(item.get("repo_breadth", 0))
        for item in critical_manifest.get("critical_mechanics", [])
    }
    record_count_by_mechanic = {
        item.get("mechanic", ""): int(item.get("record_count", 0))
        for item in critical_manifest.get("critical_mechanics", [])
    }
    selected_files = repo_surface.get("selected_files", [])
    file_roles = []
    for entry in selected_files:
        path = str(entry.get("path", ""))
        file_roles.append({
            "path": path,
            "role": motion_dungeon_unit_role(path),
            "score": entry.get("score", 0),
            "mechanics": entry.get("mechanics", []),
            "source_line_refs": entry.get("source_line_refs", []),
        })

    performance_key_specs = [
        {
            "key": "time",
            "category": "timeline",
            "needles": ["timeRef", "setTime", "renderAt", "seek", "animate", "togglePlayback"],
            "paths": ["app/page.tsx", "state.md"],
        },
        {
            "key": "preset",
            "category": "composition selection",
            "needles": ["preset", "adam", "courtship", "beardslap"],
            "paths": ["app/page.tsx", "state.md", "README.md"],
        },
        {
            "key": "rendererMode",
            "category": "render backend",
            "needles": ["rendererMode", "webgl", "fallback"],
            "paths": ["app/page.tsx", "app/sherman/sherman-lab.tsx"],
        },
        {
            "key": "exporting",
            "category": "export gate",
            "needles": ["exporting", "MP4 export", "Rendering on this device", "video/mp4"],
            "paths": ["app/page.tsx", "state.md", "README.md"],
        },
        {
            "key": "outputSizeRef",
            "category": "capture sizing",
            "needles": ["outputSizeRef", "setPixelRatio", "setSize", "1280", "720"],
            "paths": ["app/page.tsx", "README.md"],
        },
        {
            "key": "voice",
            "category": "audio lane",
            "needles": ["voice", "renderAdamAudio", "renderCourtshipAudio", "renderBeardSlapAudio"],
            "paths": ["app/page.tsx", "app/api/venice/voice/route.ts", "app/venice/venice-room.tsx"],
        },
        {
            "key": "foley",
            "category": "audio lane",
            "needles": ["foley"],
            "paths": ["app/page.tsx", "state.md"],
        },
        {
            "key": "sourceName",
            "category": "performance provenance",
            "needles": ["sourceName", "source-locked", "accepted performance", "take"],
            "paths": ["projects/", "app/scenes/", "state.md"],
        },
    ]
    performance_keys = []
    for spec in performance_key_specs:
        evidence = motion_dungeon_evidence(source_refs, spec["needles"], limit=3, path_prefixes=spec["paths"])
        if not evidence:
            continue
        performance_keys.append({
            "key": spec["key"],
            "category": spec["category"],
            "evidence": evidence,
        })

    pattern_specs = [
        {
            "id": "source_locked_composition_canon",
            "name": "Source-locked composition canon",
            "mechanics": ["asset_import_pipeline", "validation_pipeline", "web_choice_player"],
            "needles": ["source-locked", "source of truth", "accepted performance", "state.md"],
            "paths": ["state.md", "app/scenes/", "projects/", "README.md"],
            "problem": "Keep the editable composition authoritative while binaries stay downstream.",
        },
        {
            "id": "key_driven_timeline_transport",
            "name": "Key-driven timeline transport",
            "mechanics": ["web_choice_player", "text_console_runtime", "delayed_consequences"],
            "needles": ["timeRef", "renderAt", "seek", "togglePlayback", "rendererMode", "playingRef"],
            "paths": ["app/page.tsx", "app/sherman/", "app/venice/"],
            "problem": "Keep motion composition deterministic and scrub-friendly from source keys.",
        },
        {
            "id": "browser_preview_heavy_mp4_export",
            "name": "Browser preview, heavy MP4 export",
            "mechanics": ["web_choice_player", "tts_audio_pipeline", "asset_import_pipeline"],
            "needles": ["WebCodecs", "VideoFrame", "video/mp4", "MP4 export", "rendering on this device"],
            "paths": ["app/page.tsx", "README.md", "state.md"],
            "problem": "Let preview stay light while the exported movie carries the heavy output.",
        },
        {
            "id": "child_manifest_composition_chain",
            "name": "Child manifest composition chain",
            "mechanics": ["asset_import_pipeline", "source_packet_generation", "validation_pipeline"],
            "needles": ["child scene manifests", "source-locked scene", "performance", "project records"],
            "paths": ["app/scenes/", "projects/", "state.md"],
            "problem": "Let scenes and performance records inherit the engine without losing their own source names.",
        },
        {
            "id": "audio_tracks_as_composition_lanes",
            "name": "Audio tracks as composition lanes",
            "mechanics": ["tts_audio_pipeline", "ai_pressure", "web_choice_player"],
            "needles": ["renderAdamAudio", "renderCourtshipAudio", "renderBeardSlapAudio", "voice", "foley"],
            "paths": ["app/page.tsx", "app/api/venice/voice/", "app/venice/"],
            "problem": "Treat voice and foley as first-class compositional tracks, not post-process noise.",
        },
    ]

    portable_patterns = []
    for spec in pattern_specs:
        mechanics = spec["mechanics"]
        supporting_breadth = max((breadth_by_mechanic.get(mechanic, 0) for mechanic in mechanics), default=0)
        supporting_records = sum(record_count_by_mechanic.get(mechanic, 0) for mechanic in mechanics)
        evidence = motion_dungeon_evidence(source_refs, spec["needles"], limit=3, path_prefixes=spec["paths"])
        engine_notes = {
            "threejs": "Keep the source manifest textual; render the preview with a scene graph and export MP4 only at the end.",
            "godot": "Map the manifest to scenes/resources; keep source as text and let export generate the binary build later.",
            "unity": "Translate the same manifest to data assets and timeline-like transport; compile only during export.",
            "unreal": "Treat the manifest as Sequencer/DataAsset input; package binaries only when exporting.",
        }
        portable_patterns.append({
            "id": spec["id"],
            "name": spec["name"],
            "problem": spec["problem"],
            "mechanics": mechanics,
            "supporting_breadth": supporting_breadth,
            "supporting_records": supporting_records,
            "source_evidence": evidence,
            "engine_notes": engine_notes,
        })

    portable_patterns.sort(key=lambda item: (-item["supporting_breadth"], -item["supporting_records"], item["id"]))

    engine_defaults = {
        "threejs": {
            "source_adapter": "scene graph + browser composition",
            "binary_on_export": True,
            "export_lane": "MP4 via browser media capture or WebCodecs",
        },
        "godot": {
            "source_adapter": "scene tree + resource manifests",
            "binary_on_export": True,
            "export_lane": "project export only",
        },
        "unity": {
            "source_adapter": "data assets + timeline transport",
            "binary_on_export": True,
            "export_lane": "package only on export",
        },
        "unreal": {
            "source_adapter": "sequencer + data assets",
            "binary_on_export": True,
            "export_lane": "packaged build only",
        },
    }
    engine_matrix = []
    for engine in engines:
        base = engine_defaults.get(engine, {
            "source_adapter": "source manifest adapter",
            "binary_on_export": True,
            "export_lane": "export-time materialization only",
        })
        engine_matrix.append({"engine": engine, **base})

    retry_queue = [
        {"repo": item.get("repo", ""), "reason": item.get("reason", ""), "error": item.get("error", "")}
        for item in critical_manifest.get("failed_repos", [])
    ]

    composition_units = file_roles[:12]
    source_inputs = [
        str(repo_surface_path),
        str(source_refs_path),
        str(critical_manifest_path),
        str(summary_path),
    ]

    export_profile = {
        "primary_output": "mp4",
        "format": "H.264 MP4",
        "role": "heavy output archive",
        "source_truth": "Motion Dungeon composition keys and source-locked manifests",
        "binary_policy": "binaries are export artifacts, not source",
    }

    manifest = {
        "title": "Motion Dungeon Composition Compiler",
        "owner": repo_surface.get("repo", "").split("/")[0] if repo_surface.get("repo") else "",
        "source_repo": repo_surface.get("repo", ""),
        "created_at": utc_now().isoformat(timespec="seconds") + "Z",
        "policy": {
            "source_first": True,
            "binary_source_boundary": "binary artifacts are only produced on export",
            "big_4": ["threejs", "godot", "unity", "unreal"],
        },
        "source_inputs": source_inputs,
        "composition_units": composition_units,
        "performance_keys": performance_keys,
        "portable_patterns": portable_patterns,
        "engine_matrix": engine_matrix,
        "export_profile": export_profile,
        "retry_queue": retry_queue,
    }
    manifest["source_fingerprint"] = stable_hash(manifest)
    return manifest


def render_motion_dungeon_composition_manifest(manifest: dict[str, Any]) -> str:
    lines = [
        "# Motion Dungeon Composition Compiler",
        "",
        f"- Source repo: {manifest.get('source_repo') or 'unknown'}",
        f"- Created: {manifest.get('created_at') or 'unknown'}",
        f"- Source-first: {manifest.get('policy', {}).get('source_first', False)}",
        f"- Binary boundary: {manifest.get('policy', {}).get('binary_source_boundary', '')}",
        f"- Primary output: {manifest.get('export_profile', {}).get('primary_output', 'unknown')} ({manifest.get('export_profile', {}).get('format', 'unknown')})",
        "",
        "## Source Inputs",
        "",
    ]
    for item in manifest.get("source_inputs", []):
        lines.append(f"- {item}")

    lines.extend([
        "",
        "## Composition Units",
        "",
        "| Path | Role | Score | Mechanics |",
        "| --- | --- | --- | --- |",
    ])
    for item in manifest.get("composition_units", []):
        mechanics = ", ".join(item.get("mechanics", [])) or "none"
        lines.append(f"| {item.get('path', '')} | {item.get('role', '')} | {item.get('score', 0)} | {mechanics} |")

    lines.extend([
        "",
        "## Performance Keys",
        "",
    ])
    for item in manifest.get("performance_keys", []):
        lines.append(f"### {item.get('key', '')} ({item.get('category', '')})")
        for evidence in item.get("evidence", []):
            source = evidence.get("source_url") or f"{evidence.get('path', '')}:{evidence.get('line', '')}"
            lines.append(f"- [{source}] {evidence.get('evidence', '')}")
        lines.append("")

    lines.extend([
        "## Portable Patterns",
        "",
    ])
    for item in manifest.get("portable_patterns", []):
        lines.append(f"### {item.get('name', '')}")
        lines.append(f"- Problem: {item.get('problem', '')}")
        lines.append(f"- Supporting breadth: {item.get('supporting_breadth', 0)}")
        lines.append(f"- Supporting records: {item.get('supporting_records', 0)}")
        lines.append(f"- Mechanics: {', '.join(item.get('mechanics', [])) or 'none'}")
        lines.append("- Engine notes:")
        for engine, note in item.get("engine_notes", {}).items():
            lines.append(f"  - {engine}: {note}")
        if item.get("source_evidence"):
            lines.append("- Evidence:")
            for evidence in item.get("source_evidence", []):
                source = evidence.get("source_url") or f"{evidence.get('path', '')}:{evidence.get('line', '')}"
                lines.append(f"  - [{source}] {evidence.get('evidence', '')}")
        lines.append("")

    lines.extend([
        "## Engine Matrix",
        "",
        "| Engine | Source adapter | Binary on export | Export lane |",
        "| --- | --- | --- | --- |",
    ])
    for item in manifest.get("engine_matrix", []):
        lines.append(f"| {item.get('engine', '')} | {item.get('source_adapter', '')} | {item.get('binary_on_export', False)} | {item.get('export_lane', '')} |")

    lines.extend([
        "",
        "## Export Profile",
        "",
    ])
    export = manifest.get("export_profile", {})
    lines.append(f"- Primary output: {export.get('primary_output', '')}")
    lines.append(f"- Format: {export.get('format', '')}")
    lines.append(f"- Role: {export.get('role', '')}")
    lines.append(f"- Source truth: {export.get('source_truth', '')}")
    lines.append(f"- Binary policy: {export.get('binary_policy', '')}")

    lines.extend([
        "",
        "## Retry Queue",
        "",
    ])
    if manifest.get("retry_queue"):
        for item in manifest.get("retry_queue", []):
            lines.append(f"- {item.get('repo', '')}: {item.get('reason', '')} {item.get('error', '')}".strip())
    else:
        lines.append("- none")
    lines.append("")
    return "\n".join(lines)


def cmd_compose_motion_dungeon(args: argparse.Namespace) -> int:
    repo_surface_path = Path(args.repo_surface)
    critical_manifest_path = Path(args.critical_manifest)
    source_refs_path = Path(args.source_refs)
    summary_path = Path(args.summary)
    out_root = Path(args.out_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    repo_surface = json.loads(repo_surface_path.read_text(encoding="utf-8"))
    critical_manifest = json.loads(critical_manifest_path.read_text(encoding="utf-8"))
    source_refs = read_jsonl(source_refs_path)
    engines = args.engine or ["threejs", "godot", "unity", "unreal"]
    manifest = build_motion_dungeon_composition_manifest(
        repo_surface=repo_surface,
        critical_manifest=critical_manifest,
        source_refs=source_refs,
        summary_path=summary_path,
        critical_manifest_path=critical_manifest_path,
        repo_surface_path=repo_surface_path,
        source_refs_path=source_refs_path,
        engines=engines,
    )
    save_json(out_root / "motion_dungeon_composition_manifest.json", manifest)
    (out_root / "motion_dungeon_composition_manifest.md").write_text(render_motion_dungeon_composition_manifest(manifest), encoding="utf-8")
    if args.quiet:
        top = ", ".join(item["id"] for item in manifest["portable_patterns"][:5]) or "no patterns"
        print(f"{manifest['source_repo']} composition: {len(manifest['portable_patterns'])} patterns, {len(manifest['performance_keys'])} keys, output={manifest['export_profile']['primary_output']} :: {top}")
    else:
        print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0


def motion_dungeon_export_engines(requested: list[str]) -> list[str]:
    if not requested:
        return list(MOTION_DUNGEON_EXPORT_ENGINES)
    wanted = {engine.lower() for engine in requested}
    unknown = sorted(wanted - set(MOTION_DUNGEON_EXPORT_ENGINES))
    if unknown:
        raise SystemExit(f"Unknown export engine(s): {', '.join(unknown)}")
    return [engine for engine in MOTION_DUNGEON_EXPORT_ENGINES if engine in wanted]


def motion_dungeon_source_fingerprint(manifest: dict[str, Any]) -> str:
    return str(manifest.get("source_fingerprint") or stable_hash(manifest))


def motion_dungeon_export_engine_info(composition: dict[str, Any], engine: str) -> dict[str, Any]:
    defaults = {
        "threejs": {
            "source_adapter": "scene graph + browser composition",
            "binary_on_export": True,
            "export_lane": "MP4 via browser media capture or WebCodecs",
        },
        "godot": {
            "source_adapter": "scene tree + resource manifests",
            "binary_on_export": True,
            "export_lane": "project export only",
        },
        "unity": {
            "source_adapter": "data assets + timeline transport",
            "binary_on_export": True,
            "export_lane": "package only on export",
        },
        "unreal": {
            "source_adapter": "sequencer + data assets",
            "binary_on_export": True,
            "export_lane": "packaged build only",
        },
    }
    info_by_engine = {item.get("engine", ""): item for item in composition.get("engine_matrix", [])}
    info = dict(defaults.get(engine, {
        "source_adapter": "source manifest adapter",
        "binary_on_export": True,
        "export_lane": "export-time materialization only",
    }))
    info.update(info_by_engine.get(engine, {}))
    return info


def motion_dungeon_export_composition_units(composition: dict[str, Any]) -> list[dict[str, Any]]:
    units: list[dict[str, Any]] = []
    for item in composition.get("composition_units", []):
        units.append({
            "path": item.get("path", ""),
            "role": item.get("role", ""),
            "score": item.get("score", 0),
            "mechanics": item.get("mechanics", []),
            "source_line_refs": item.get("source_line_refs", []),
        })
    return units


def motion_dungeon_export_performance_axes(composition: dict[str, Any]) -> list[dict[str, Any]]:
    axes: list[dict[str, Any]] = []
    for item in sorted(composition.get("performance_keys", []), key=lambda row: row.get("key", "")):
        axes.append({
            "key": item.get("key", ""),
            "category": item.get("category", ""),
            "evidence": item.get("evidence", [])[:1],
        })
    return axes


def motion_dungeon_export_patterns(composition: dict[str, Any], engine: str) -> list[dict[str, Any]]:
    patterns: list[dict[str, Any]] = []
    for item in composition.get("portable_patterns", []):
        patterns.append({
            "id": item.get("id", ""),
            "name": item.get("name", ""),
            "problem": item.get("problem", ""),
            "mechanics": item.get("mechanics", []),
            "supporting_breadth": item.get("supporting_breadth", 0),
            "supporting_records": item.get("supporting_records", 0),
            "engine_note": item.get("engine_notes", {}).get(engine, ""),
            "source_evidence": item.get("source_evidence", [])[:2],
        })
    return patterns


def motion_dungeon_export_stamp_core(*, engine: str, input_manifest_hash: str, exporter_version: int) -> dict[str, Any]:
    target_fingerprint = stable_hash({
        "engine": engine,
        "input_manifest_hash": input_manifest_hash,
        "exporter_version": exporter_version,
    })
    return {
        "engine": engine,
        "exporter_version": exporter_version,
        "input_manifest_hash": input_manifest_hash,
        "target_fingerprint": target_fingerprint,
    }


def motion_dungeon_export_target_contract(
    *,
    composition: dict[str, Any],
    composition_path: Path,
    engine: str,
) -> dict[str, Any]:
    input_manifest_hash = motion_dungeon_source_fingerprint(composition)
    engine_info = motion_dungeon_export_engine_info(composition, engine)
    target_fingerprint = motion_dungeon_export_stamp_core(
        engine=engine,
        input_manifest_hash=input_manifest_hash,
        exporter_version=MOTION_DUNGEON_EXPORTER_VERSION,
    )["target_fingerprint"]
    artifact_map = {
        "export_spec": "export_spec.json",
        "export_stamp": "export_stamp.json",
        "export_report": "export_report.md",
        "matrix": "../export_matrix.json",
    }
    composition_units = motion_dungeon_export_composition_units(composition)
    performance_axes = motion_dungeon_export_performance_axes(composition)
    patterns = motion_dungeon_export_patterns(composition, engine)
    export_lane = engine_info.get("export_lane", "")
    target_dir = Path(engine)
    contract = {
        "engine": engine,
        "export_target_id": f"motion-dungeon:{engine}",
        "exporter": "motion_dungeon_export_target",
        "exporter_version": MOTION_DUNGEON_EXPORTER_VERSION,
        "monolithic": True,
        "idempotent": True,
        "deterministic": True,
        "source_repo": composition.get("source_repo", ""),
        "source_manifest_path": str(composition_path),
        "source_fingerprint": input_manifest_hash,
        "input_manifest_hash": input_manifest_hash,
        "source_adapter": engine_info.get("source_adapter", ""),
        "binary_on_export": engine_info.get("binary_on_export", True),
        "export_lane": export_lane,
        "artifact_map": artifact_map,
        "policy": {
            "source_first": True,
            "binary_source_boundary": "binary artifacts are export outputs only",
            "export_only_on_hash_change": True,
        },
        "engine_projection": {
            "composition_units": composition_units,
            "performance_axes": performance_axes,
            "portable_patterns": patterns,
            "retry_queue": composition.get("retry_queue", []),
        },
        "target_fingerprint": target_fingerprint,
        "target_dir": str(target_dir),
    }
    return contract


def motion_dungeon_export_report(contract: dict[str, Any]) -> str:
    lines = [
        f"# Motion Dungeon {contract.get('engine', '')} Export Target",
        "",
        f"- Export target: {contract.get('export_target_id', '')}",
        f"- Source manifest: {contract.get('source_manifest_path', '')}",
        f"- Source fingerprint: {contract.get('source_fingerprint', '')}",
        f"- Input hash: {contract.get('input_manifest_hash', '')}",
        f"- Target fingerprint: {contract.get('target_fingerprint', '')}",
        f"- Source adapter: {contract.get('source_adapter', '')}",
        f"- Export lane: {contract.get('export_lane', '')}",
        f"- Binary on export: {contract.get('binary_on_export', False)}",
        "",
        "## Artifact Map",
        "",
    ]
    for key in sorted(contract.get("artifact_map", {}).keys()):
        lines.append(f"- {key}: {contract['artifact_map'][key]}")
    lines.extend([
        "",
        "## Composition Units",
        "",
        "| Path | Role | Score | Mechanics |",
        "| --- | --- | --- | --- |",
    ])
    for item in contract.get("engine_projection", {}).get("composition_units", []):
        mechanics = ", ".join(item.get("mechanics", [])) or "none"
        lines.append(f"| {item.get('path', '')} | {item.get('role', '')} | {item.get('score', 0)} | {mechanics} |")
    lines.extend([
        "",
        "## Performance Axes",
        "",
    ])
    for item in contract.get("engine_projection", {}).get("performance_axes", []):
        lines.append(f"### {item.get('key', '')} ({item.get('category', '')})")
        for evidence in item.get("evidence", []):
            source = evidence.get("source_url") or f"{evidence.get('path', '')}:{evidence.get('line', '')}"
            lines.append(f"- [{source}] {evidence.get('evidence', '')}")
        lines.append("")
    lines.extend([
        "## Portable Patterns",
        "",
    ])
    for item in contract.get("engine_projection", {}).get("portable_patterns", []):
        lines.append(f"### {item.get('name', '')}")
        lines.append(f"- Problem: {item.get('problem', '')}")
        lines.append(f"- Mechanics: {', '.join(item.get('mechanics', [])) or 'none'}")
        lines.append(f"- Supporting breadth: {item.get('supporting_breadth', 0)}")
        lines.append(f"- Supporting records: {item.get('supporting_records', 0)}")
        lines.append(f"- Engine note: {item.get('engine_note', '')}")
        if item.get("source_evidence"):
            lines.append("- Evidence:")
            for evidence in item.get("source_evidence", []):
                source = evidence.get("source_url") or f"{evidence.get('path', '')}:{evidence.get('line', '')}"
                lines.append(f"  - [{source}] {evidence.get('evidence', '')}")
        lines.append("")
    lines.extend([
        "## Retry Queue",
        "",
    ])
    retry_queue = contract.get("engine_projection", {}).get("retry_queue", [])
    if retry_queue:
        for item in retry_queue:
            lines.append(f"- {item.get('repo', '')}: {item.get('reason', '')} {item.get('error', '')}".strip())
    else:
        lines.append("- none")
    lines.append("")
    return "\n".join(lines)


def motion_dungeon_export_matrix_report(entries: list[dict[str, Any]], composition: dict[str, Any]) -> str:
    lines = [
        "# Motion Dungeon Export Matrix",
        "",
        f"- Source repo: {composition.get('source_repo', '')}",
        f"- Source fingerprint: {motion_dungeon_source_fingerprint(composition)}",
        f"- Exporter version: {MOTION_DUNGEON_EXPORTER_VERSION}",
        "",
        "| Engine | Status | Input hash | Target fingerprint | Export lane |",
        "| --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        lines.append(
            f"| {entry.get('engine', '')} | {entry.get('status', '')} | {entry.get('input_manifest_hash', '')} | {entry.get('target_fingerprint', '')} | {entry.get('export_lane', '')} |"
        )
    lines.append("")
    return "\n".join(lines)


def cmd_export_motion_dungeon_targets(args: argparse.Namespace) -> int:
    composition_path = Path(args.composition_manifest)
    composition = json.loads(composition_path.read_text(encoding="utf-8"))
    out_root = Path(args.out_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    engines = motion_dungeon_export_engines(args.engine or [])
    matrix_entries: list[dict[str, Any]] = []
    for engine in engines:
        contract = motion_dungeon_export_target_contract(
            composition=composition,
            composition_path=composition_path,
            engine=engine,
        )
        engine_dir = out_root / engine
        engine_dir.mkdir(parents=True, exist_ok=True)
        spec_path = engine_dir / "export_spec.json"
        stamp_path = engine_dir / "export_stamp.json"
        report_path = engine_dir / "export_report.md"
        desired_stamp = motion_dungeon_export_stamp_core(
            engine=engine,
            input_manifest_hash=contract["input_manifest_hash"],
            exporter_version=contract["exporter_version"],
        )
        current_stamp = None
        if stamp_path.exists():
            try:
                current_stamp = json.loads(stamp_path.read_text(encoding="utf-8"))
            except Exception:
                current_stamp = None
        stamp_matches = bool(current_stamp) and all(current_stamp.get(key) == value for key, value in desired_stamp.items())
        all_outputs_exist = spec_path.exists() and report_path.exists() and stamp_path.exists()
        if args.force or not (stamp_matches and all_outputs_exist):
            write_json_atomic(spec_path, contract)
            stamp_payload = dict(desired_stamp)
            stamp_payload["status"] = "written"
            write_json_atomic(stamp_path, stamp_payload)
            write_text_atomic(report_path, motion_dungeon_export_report(contract))
            status = "written"
        else:
            status = "skipped"
        matrix_entries.append({
            "engine": engine,
            "status": status,
            "input_manifest_hash": contract["input_manifest_hash"],
            "target_fingerprint": contract["target_fingerprint"],
            "export_lane": contract["export_lane"],
            "artifact_map": contract["artifact_map"],
            "export_spec": str(spec_path),
            "export_stamp": str(stamp_path),
            "export_report": str(report_path),
        })
    matrix_payload = {
        "title": "Motion Dungeon Export Matrix",
        "source_repo": composition.get("source_repo", ""),
        "source_manifest_path": str(composition_path),
        "source_fingerprint": motion_dungeon_source_fingerprint(composition),
        "exporter_version": MOTION_DUNGEON_EXPORTER_VERSION,
        "targets": matrix_entries,
    }
    write_json_atomic(out_root / "export_matrix.json", matrix_payload)
    write_text_atomic(out_root / "export_matrix.md", motion_dungeon_export_matrix_report(matrix_entries, composition))
    if args.quiet:
        joined = ", ".join(f"{item['engine']}={item['status']}" for item in matrix_entries)
        print(f"{composition.get('source_repo', '')} export matrix: {joined}")
    else:
        print(json.dumps(matrix_payload, indent=2, ensure_ascii=False))
    return 0


def classify_mechanics(text: str) -> list[str]:
    haystack = text.lower()
    tags = []
    for mechanic, needles in MECHANIC_RULES.items():
        if any(needle in haystack for needle in needles):
            tags.append(mechanic)
    return tags


def detect_project_name(root: Path, path: Path) -> str:
    rel = path.relative_to(root)
    if rel.parts:
        return rel.parts[0]
    return root.name


def compact_snippet(line: str, limit: int = 180) -> str:
    snippet = re.sub(r"\s+", " ", line).strip()
    if len(snippet) > limit:
        return snippet[: limit - 3] + "..."
    return snippet


def index_source_line(
    records: list[dict[str, Any]],
    *,
    origin: str,
    project: str,
    path: str,
    line_no: int,
    line: str,
    symbol: str = "",
    source_url: str = "",
    repo: str = "",
) -> None:
    mechanics = classify_mechanics(" ".join([path, symbol, line]))
    if not mechanics:
        return
    records.append({
        "record_type": "source_ref",
        "origin": origin,
        "project": project,
        "repo": repo,
        "path": path,
        "line": line_no,
        "symbol": symbol,
        "mechanics": mechanics,
        "evidence": compact_snippet(line),
        "source_url": source_url,
    })


def index_text_content(
    *,
    origin: str,
    project: str,
    path: str,
    text: str,
    repo: str = "",
    source_url_base: str = "",
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    suffix = Path(path).suffix.lower()
    lines = text.splitlines()

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped:
            continue
        symbol = ""
        match = re.match(r"(?:func|def|function)\s+([A-Za-z_][A-Za-z0-9_]*)", stripped)
        if match:
            symbol = match.group(1)
        elif suffix == ".md" and stripped.startswith("#"):
            symbol = stripped.lstrip("#").strip()
        elif suffix == ".json":
            key_match = re.match(r'"([^"]+)"\s*:', stripped)
            if key_match:
                symbol = key_match.group(1)
        elif suffix == ".godot" and ("config/name" in stripped or "run/main_scene" in stripped):
            symbol = stripped.split("=", 1)[0].strip()

        should_index = bool(symbol)
        if not should_index:
            mechanics = classify_mechanics(" ".join([path, stripped]))
            should_index = bool(mechanics) and (
                suffix == ".md"
                or len(stripped) <= 220
                or any(marker in stripped for marker in ["=", ":", "(", ")"])
            )
        if not should_index:
            continue

        source_url = f"{source_url_base}#L{idx}" if source_url_base else ""
        index_source_line(
            records,
            origin=origin,
            project=project,
            repo=repo,
            path=path,
            line_no=idx,
            line=stripped,
            symbol=symbol,
            source_url=source_url,
        )
    return records


def should_index_path(path: Path | str, include_generated: bool = False) -> bool:
    p = Path(path)
    parts = set(p.parts)
    skip_parts = set(INDEX_SKIP_PARTS)
    if include_generated:
        skip_parts.discard("generated")
    if parts & skip_parts:
        return False
    suffix = p.suffix.lower()
    if suffix in INDEX_SKIP_SUFFIXES:
        return False
    if "generated" in parts and not include_generated:
        return False
    return suffix in INDEX_TEXT_EXTS or p.name in DOC_NAMES or p.name == "project.godot"


def index_local_corpus(root: Path, max_files: int = 5000, include_generated: bool = False) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    count = 0
    for current, dirs, files in os.walk(root):
        skip_parts = set(INDEX_SKIP_PARTS)
        if include_generated:
            skip_parts.discard("generated")
        dirs[:] = [d for d in dirs if d not in skip_parts]
        current_path = Path(current)
        rel_current = current_path.relative_to(root)
        if len(rel_current.parts) > 5:
            dirs[:] = []
            continue
        for name in files:
            path = current_path / name
            if not should_index_path(path.relative_to(root), include_generated=include_generated):
                continue
            if path.stat().st_size > 750_000:
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            project = detect_project_name(root, path)
            rel = str(path.relative_to(root))
            records.extend(index_text_content(origin="local", project=project, path=rel, text=text))
            count += 1
            if count >= max_files:
                return records
    return records


def github_api_json(path: str, timeout: int = 20) -> Any:
    return json.loads(subprocess.check_output(["gh", "api", path], timeout=timeout).decode())


def github_fetch_file(owner: str, repo: str, path: str, timeout: int = 20) -> str:
    raw = subprocess.check_output(
        ["gh", "api", f"/repos/{owner}/{repo}/contents/{path}", "--jq", ".content"],
        stderr=subprocess.DEVNULL,
        timeout=timeout,
    ).decode()
    import base64
    return base64.b64decode(raw).decode("utf-8", errors="ignore")


def index_github_corpus(
    owner: str,
    limit: int = 20,
    max_files_per_repo: int = 80,
    include_generated: bool = False,
    repo_names: list[str] | None = None,
) -> list[dict[str, Any]]:
    if repo_names:
        repos = [{"name": name} for name in repo_names]
    else:
        repos = json.loads(subprocess.check_output([
            "gh", "repo", "list", owner, "--limit", str(limit),
            "--json", "name,description,primaryLanguage,updatedAt,url",
        ]).decode())
    records: list[dict[str, Any]] = []
    for repo_info in repos:
        repo = repo_info["name"]
        repo_full = f"{owner}/{repo}"
        try:
            tree = github_api_json(f"/repos/{owner}/{repo}/git/trees/HEAD?recursive=1")
        except Exception:
            continue
        paths = [
            item["path"] for item in tree.get("tree", [])
            if item.get("type") == "blob" and should_index_path(item.get("path", ""), include_generated=include_generated)
        ]
        priority = sorted(paths, key=lambda p: (
            0 if Path(p).name in DOC_NAMES or Path(p).name == "project.godot" else 1,
            0 if "/docs/" in f"/{p}" or "/tools/" in f"/{p}" or "/scripts/" in f"/{p}" else 1,
            p,
        ))
        for path in priority[:max_files_per_repo]:
            try:
                text = github_fetch_file(owner, repo, path)
            except Exception:
                continue
            if len(text) > 750_000:
                continue
            source_url = f"https://github.com/{owner}/{repo}/blob/HEAD/{path}"
            records.extend(index_text_content(
                origin="github",
                project=repo,
                repo=repo_full,
                path=path,
                text=text,
                source_url_base=source_url,
            ))
    return records


def summarize_index(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_mechanic: Counter[str] = Counter()
    by_project: Counter[str] = Counter()
    by_origin: Counter[str] = Counter()
    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_project[record.get("project", "")] += 1
        by_origin[record.get("origin", "")] += 1
        for mechanic in record.get("mechanics", []):
            by_mechanic[mechanic] += 1
            if len(examples[mechanic]) < 8:
                examples[mechanic].append({
                    "origin": record.get("origin"),
                    "project": record.get("project"),
                    "repo": record.get("repo"),
                    "path": record.get("path"),
                    "line": record.get("line"),
                    "symbol": record.get("symbol"),
                    "evidence": record.get("evidence"),
                    "source_url": record.get("source_url"),
                })
    return {
        "record_count": len(records),
        "by_origin": dict(by_origin.most_common()),
        "by_project": dict(by_project.most_common(40)),
        "by_mechanic": dict(by_mechanic.most_common()),
        "examples": dict(examples),
    }


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if not path.exists():
        return records
    with path.open(encoding="utf-8") as handle:
        for raw in handle:
            raw = raw.strip()
            if raw:
                records.append(json.loads(raw))
    return records


def write_index_report(path: Path, summary: dict[str, Any]) -> None:
    lines = [
        "# Thunder Brainstorm Mechanics Index",
        "",
        f"- Records: {summary['record_count']}",
        f"- Origins: {', '.join(f'{k}={v}' for k, v in summary['by_origin'].items())}",
        "",
        "## Mechanics",
        "",
    ]
    for mechanic, count in summary["by_mechanic"].items():
        lines.append(f"### {mechanic} ({count})")
        for example in summary["examples"].get(mechanic, [])[:5]:
            source = example.get("source_url") or f"{example.get('path')}:{example.get('line')}"
            symbol = f" `{example['symbol']}`" if example.get("symbol") else ""
            repo = f" {example['repo']}" if example.get("repo") else ""
            lines.append(f"- {example['origin']} {example['project']}{repo} [{source}]{symbol}: {example.get('evidence', '')}")
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def cmd_index_corpus(args: argparse.Namespace) -> int:
    records: list[dict[str, Any]] = []
    if not args.skip_local:
        records.extend(index_local_corpus(Path(args.root).resolve(), max_files=args.max_local_files, include_generated=args.include_generated))
    if args.include_gh:
        records.extend(index_github_corpus(
            args.owner,
            limit=args.gh_limit,
            max_files_per_repo=args.max_gh_files_per_repo,
            include_generated=args.include_generated,
            repo_names=args.repo,
        ))
    summary = summarize_index(records)
    out_dir = Path(args.out_dir)
    write_jsonl(out_dir / "mechanic_source_refs.jsonl", records)
    save_json(out_dir / "mechanic_index_summary.json", summary)
    write_index_report(out_dir / "mechanic_index_report.md", summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


def cmd_search_index(args: argparse.Namespace) -> int:
    path = Path(args.index)
    terms = token_set(args.query)
    shown = 0
    with path.open(encoding="utf-8") as handle:
        for raw in handle:
            record = json.loads(raw)
            if args.mechanic and args.mechanic not in record.get("mechanics", []):
                continue
            if args.project and args.project.lower() not in record.get("project", "").lower():
                continue
            haystack = " ".join([
                record.get("project", ""),
                record.get("repo", ""),
                record.get("path", ""),
                record.get("symbol", ""),
                record.get("evidence", ""),
                " ".join(record.get("mechanics", [])),
            ]).lower()
            if terms and not all(term in haystack for term in terms):
                continue
            source = record.get("source_url") or f"{record.get('path')}:{record.get('line')}"
            mechanics = ",".join(record.get("mechanics", []))
            symbol = f" {record['symbol']}" if record.get("symbol") else ""
            print(f"{record.get('origin')} {record.get('project')} {source}{symbol} [{mechanics}]")
            print(f"  {record.get('evidence', '')}")
            shown += 1
            if shown >= args.limit:
                break
    return 0


def cmd_observations(args: argparse.Namespace) -> int:
    print(OBSERVATIONS_PATH.read_text(encoding="utf-8"))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Generalized game brainstorming from observed codebase patterns.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List pattern cards.")
    p_list.add_argument("--kind", choices=["structure", "workflow", "interface", "system", "control", "presentation", "tooling", "premise"])
    p_list.add_argument("--verbose", action="store_true")
    p_list.set_defaults(func=cmd_list)

    p_gen = sub.add_parser("generate", help="Generate game concept pitches.")
    p_gen.add_argument("--focus", default="", help="Optional focus such as mobile action, narrative roguelike, web, corpus, board, vehicle.")
    p_gen.add_argument("--count", type=int, default=3)
    p_gen.add_argument("--seed", type=int, default=None)
    p_gen.add_argument("--out", default="")
    p_gen.set_defaults(func=cmd_generate)

    p_local = sub.add_parser("inspect-local", help="Scan a local workspace and keep only abstract structural signals.")
    p_local.add_argument("--root", default="..")
    p_local.add_argument("--out", default="")
    p_local.set_defaults(func=cmd_inspect_local)

    p_gh = sub.add_parser("inspect-gh", help="Use gh to inspect repository metadata and top-level names without cloning.")
    p_gh.add_argument("--owner", default="Valar05")
    p_gh.add_argument("--limit", type=int, default=100)
    p_gh.add_argument("--no-contents", action="store_true")
    p_gh.add_argument("--out", default="")
    p_gh.set_defaults(func=cmd_inspect_gh)

    p_mine = sub.add_parser("mine-gh-repo", help="Mine one GitHub repo's surface contract from metadata and selected files.")
    p_mine.add_argument("--owner", default="Valar05")
    p_mine.add_argument("--repo", required=True)
    p_mine.add_argument("--ref", default="HEAD")
    p_mine.add_argument("--out-dir", default="generated/repo_mining")
    p_mine.add_argument("--max-files", type=int, default=60)
    p_mine.add_argument("--include-generated", action="store_true")
    p_mine.add_argument("--quiet", action="store_true")
    p_mine.set_defaults(func=cmd_mine_gh_repo)

    p_owner = sub.add_parser("mine-gh-owner", help="Mine all GitHub repos for one owner with low-noise overnight output.")
    p_owner.add_argument("--owner", default="Valar05")
    p_owner.add_argument("--limit", type=int, default=200)
    p_owner.add_argument("--ref", default="HEAD")
    p_owner.add_argument("--out-dir", default="generated/repo_mining")
    p_owner.add_argument("--max-files", type=int, default=24)
    p_owner.add_argument("--include-generated", action="store_true")
    p_owner.add_argument("--allow-repo", action="append", default=[], help="Only mine repos with this exact name. Repeatable.")
    p_owner.add_argument("--deny-repo", action="append", default=[], help="Skip repos with this exact name. Repeatable.")
    p_owner.add_argument("--per-repo-timeout", type=int, default=1800, help="Seconds to allow each repo mine before marking it failed.")
    p_owner.add_argument("--skip-existing", action="store_true", default=True)
    p_owner.add_argument("--resume", action="store_true")
    p_owner.add_argument("--quiet", action="store_true", default=True)
    p_owner.set_defaults(func=cmd_mine_gh_owner)

    p_crit = sub.add_parser("critical-manifest", help="Blend repo mining summaries into a critical Thunder manifest.")
    p_crit.add_argument("--summary", default="", help="Path to an overnight summary JSON. Defaults to the newest one under the source root.")
    p_crit.add_argument("--summary-jsonl", default="", help="Path to the overnight summary JSONL. Defaults to the sibling JSONL file.")
    p_crit.add_argument("--source-root", default="generated/repo_mining", help="Folder to search for the newest overnight summary.")
    p_crit.add_argument("--out-dir", default="generated/critical_thunder_manifest")
    p_crit.add_argument("--signal", action="append", default=[], help="Record a live upstream process or artifact stream being blended.")
    p_crit.add_argument("--quiet", action="store_true", default=True)
    p_crit.set_defaults(func=cmd_critical_manifest)

    p_compose = sub.add_parser("compose-motion-dungeon", help="Compile Motion Dungeon source composition into a portable, source-first manifest.")
    p_compose.add_argument("--repo-surface", default="generated/repo_mining/motion-dungeon/repo_surface.json")
    p_compose.add_argument("--critical-manifest", default="generated/critical_thunder_manifest/critical_thunder_manifest.json")
    p_compose.add_argument("--source-refs", default="generated/repo_mining/motion-dungeon/mechanic_source_refs.jsonl")
    p_compose.add_argument("--summary", default="generated/repo_mining/Valar05_overnight_summary.json")
    p_compose.add_argument("--out-dir", default="generated/motion_dungeon_composition")
    p_compose.add_argument("--engine", action="append", default=[], help="Engine target to describe; repeatable. Defaults to the big four.")
    p_compose.add_argument("--quiet", action="store_true", default=True)
    p_compose.set_defaults(func=cmd_compose_motion_dungeon)

    p_export = sub.add_parser("export-motion-dungeon-targets", help="Export deterministic Motion Dungeon target contracts for the big four engines.")
    p_export.add_argument("--composition-manifest", default="generated/motion_dungeon_composition/motion_dungeon_composition_manifest.json")
    p_export.add_argument("--out-dir", default="generated/motion_dungeon_exports")
    p_export.add_argument("--engine", action="append", default=[], help="Engine target to export. Repeatable. Defaults to the big four.")
    p_export.add_argument("--force", action="store_true", help="Rewrite targets even when the stamp matches.")
    p_export.add_argument("--quiet", action="store_true", default=True)
    p_export.set_defaults(func=cmd_export_motion_dungeon_targets)

    p_index = sub.add_parser("index-corpus", help="Build a mechanics corpus index with concrete source references.")
    p_index.add_argument("--root", default="..", help="Local corpus root to scan.")
    p_index.add_argument("--out-dir", default="generated/index", help="Directory for JSONL index and summary outputs.")
    p_index.add_argument("--max-local-files", type=int, default=5000)
    p_index.add_argument("--skip-local", action="store_true", help="Skip local disk indexing and only use requested remote sources.")
    p_index.add_argument("--include-generated", action="store_true", help="Include generated folders in the corpus index.")
    p_index.add_argument("--include-gh", action="store_true", help="Also scan GitHub repositories through gh without cloning.")
    p_index.add_argument("--owner", default="Valar05")
    p_index.add_argument("--repo", action="append", default=[], help="Specific GitHub repo name to index. Repeatable.")
    p_index.add_argument("--gh-limit", type=int, default=20)
    p_index.add_argument("--max-gh-files-per-repo", type=int, default=80)
    p_index.set_defaults(func=cmd_index_corpus)

    p_search = sub.add_parser("search-index", help="Search a mechanic source-reference JSONL index.")
    p_search.add_argument("query", nargs="?", default="", help="Terms to require in the source record.")
    p_search.add_argument("--index", default="generated/index/mechanic_source_refs.jsonl")
    p_search.add_argument("--mechanic", default="")
    p_search.add_argument("--project", default="")
    p_search.add_argument("--limit", type=int, default=20)
    p_search.set_defaults(func=cmd_search_index)

    p_obs = sub.add_parser("observations", help="Print the initial source observations used to seed this engine.")
    p_obs.set_defaults(func=cmd_observations)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
