#!/usr/bin/env python3
"""Thunder Brainstorm: generalized game-pattern extraction and idea generation."""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
CARDS_PATH = ROOT / "data" / "pattern_cards.json"
OBSERVATIONS_PATH = ROOT / "data" / "source_observations.json"

STOP_DIRS = {".git", ".godot", "generated", "audio", "assets", "models", "music", "node_modules", "__pycache__"}
CODE_EXTS = {".gd", ".py", ".js", ".ts", ".vue", ".cs", ".cpp", ".h"}
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


def load_cards() -> list[dict[str, Any]]:
    data = json.loads(CARDS_PATH.read_text(encoding="utf-8"))
    return data["cards"]


def save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


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
