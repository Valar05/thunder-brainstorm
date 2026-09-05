#!/usr/bin/env python3
"""Extract abstract Quake-style route grammar without copying map geometry."""

from __future__ import annotations

import argparse
import json
import re
import struct
import zipfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

LEVEL_NAME_RE = re.compile(r"(?i)(?:^|[/\\])(?:e(?P<ep>\d)m(?P<map>\d+)|(?:dm|map)(?P<num>\d+)|(?P<start>start))")
PLAYABLE_LEVEL_RE = re.compile(r"(?i)(?:^|[/\\])(?:start|end|e\d+m\d+|dm\d+)\.map$")
ENTITY_RE = re.compile(r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", re.S)
KEY_RE = re.compile(r'"([^"]+)"\s+"([^"]*)"')


@dataclass
class SourceFile:
    path: Path
    virtual_name: str
    bytes_data: bytes


def sequence_key(name: str) -> tuple[int, int, int, str]:
    lowered = name.lower()
    if "start" in lowered:
        return (0, 0, 0, lowered)
    match = LEVEL_NAME_RE.search(lowered)
    if match and match.group("ep") and match.group("map"):
        return (1, int(match.group("ep")), int(match.group("map")), lowered)
    if match and match.group("num"):
        return (2, int(match.group("num")), 0, lowered)
    return (9, 999, 999, lowered)


def is_playable_level(name: str) -> bool:
    return bool(PLAYABLE_LEVEL_RE.search(name))


def discover_sources(inputs: list[Path]) -> list[SourceFile]:
    sources: list[SourceFile] = []
    for raw in inputs:
        path = raw.expanduser().resolve()
        if not path.exists():
            continue
        candidates = [p for p in path.rglob("*") if p.is_file()] if path.is_dir() else [path]
        for candidate in candidates:
            suffix = candidate.suffix.lower()
            if suffix in {".pk3", ".zip"}:
                try:
                    with zipfile.ZipFile(candidate) as archive:
                        for info in archive.infolist():
                            inner = Path(info.filename)
                            if inner.suffix.lower() in {".map", ".bsp"}:
                                sources.append(SourceFile(candidate, info.filename, archive.read(info)))
                except zipfile.BadZipFile:
                    continue
            elif suffix in {".map", ".bsp"}:
                sources.append(SourceFile(candidate, str(candidate), candidate.read_bytes()))
            elif suffix == ".pak":
                try:
                    sources.extend(read_pak_sources(candidate))
                except ValueError:
                    continue
    return sorted(sources, key=lambda source: sequence_key(source.virtual_name))


def parse_entities(text: str) -> list[dict[str, str]]:
    entities: list[dict[str, str]] = []
    for block in ENTITY_RE.findall(text):
        pairs = dict(KEY_RE.findall(block))
        if pairs:
            entities.append(pairs)
    return entities


def read_pak_sources(path: Path) -> list[SourceFile]:
    data = path.read_bytes()
    if len(data) < 12 or data[:4] != b"PACK":
        raise ValueError("not a Quake PAK")
    dir_offset, dir_size = struct.unpack_from("<ii", data, 4)
    if dir_offset < 0 or dir_size < 0 or dir_offset + dir_size > len(data) or dir_size % 64 != 0:
        raise ValueError("invalid PAK directory")
    sources: list[SourceFile] = []
    for pos in range(dir_offset, dir_offset + dir_size, 64):
        raw_name = data[pos:pos + 56].split(bytes([0]), 1)[0].decode("latin-1", errors="ignore")
        file_offset, file_size = struct.unpack_from("<ii", data, pos + 56)
        suffix = Path(raw_name).suffix.lower()
        if suffix not in {".map", ".bsp"}:
            continue
        if file_offset < 0 or file_size <= 0 or file_offset + file_size > len(data):
            continue
        sources.append(SourceFile(path, raw_name, data[file_offset:file_offset + file_size]))
    return sources


def vector_from_origin(value: str) -> tuple[float, float, float] | None:
    try:
        parts = [float(part) for part in value.split()]
    except ValueError:
        return None
    if len(parts) != 3:
        return None
    return (parts[0], parts[1], parts[2])


def bbox_from_points(points: list[tuple[float, float, float]]) -> dict[str, float] | None:
    if not points:
        return None
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    zs = [p[2] for p in points]
    return {
        "min_x": min(xs), "max_x": max(xs),
        "min_y": min(ys), "max_y": max(ys),
        "min_z": min(zs), "max_z": max(zs),
        "span_x": max(xs) - min(xs),
        "span_y": max(ys) - min(ys),
        "span_z": max(zs) - min(zs),
    }


def parse_bsp_vertices(data: bytes) -> list[tuple[float, float, float]]:
    if len(data) < 124:
        return []
    version = struct.unpack_from("<i", data, 0)[0]
    if version not in {29, 38, 46}:
        return []
    lump_count = 15 if version == 29 else 17
    header_len = 4 + lump_count * 8
    if len(data) < header_len:
        return []
    offset, length = struct.unpack_from("<ii", data, 4 + 3 * 8)
    if offset < 0 or length <= 0 or offset + length > len(data):
        return []
    return [struct.unpack_from("<fff", data, pos) for pos in range(offset, offset + length - 11, 12)]


def parse_bsp_entities(data: bytes) -> list[dict[str, str]]:
    if len(data) < 12:
        return []
    version = struct.unpack_from("<i", data, 0)[0]
    if version not in {29, 38, 46}:
        return []
    offset, length = struct.unpack_from("<ii", data, 4)
    if offset < 0 or length <= 0 or offset + length > len(data):
        return []
    return parse_entities(data[offset:offset + length].decode("latin-1", errors="ignore"))


def parse_map_brush_points(text: str) -> list[tuple[float, float, float]]:
    points = []
    for match in re.finditer(r"\(\s*(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s*\)", text):
        try:
            points.append(tuple(float(match.group(i)) for i in range(1, 4)))
        except ValueError:
            continue
    return points


def classify_entity(classname: str) -> str:
    c = classname.lower()
    if c.startswith("monster_"):
        return "monster"
    if c.startswith("item_") or c.startswith("weapon_") or c.startswith("ammo_"):
        return "pickup"
    if c.startswith("trigger_"):
        return "trigger"
    if c.startswith("func_door"):
        return "door"
    if c.startswith("func_button") or c.startswith("trigger_multiple"):
        return "switch"
    if "teleport" in c:
        return "teleport"
    if c in {"info_player_start", "info_player_deathmatch", "info_player_coop"}:
        return "spawn"
    if c.startswith("light"):
        return "light"
    return "other"


def infer_route_features(entity_counts: Counter[str], class_counts: Counter[str], bbox: dict[str, float] | None, origin_bbox: dict[str, float] | None) -> list[str]:
    features: list[str] = []
    span_x = (bbox or {}).get("span_x", 0)
    span_y = (bbox or {}).get("span_y", 0)
    span_z = (bbox or {}).get("span_z", 0)
    horizontal = max(span_x, span_y)
    if horizontal > 1800:
        features.append("long_acceleration_lanes")
    if span_z > 320:
        features.append("vertical_layering")
    if entity_counts["door"] or "item_key1" in class_counts or "item_key2" in class_counts:
        features.append("lock_or_gate_pacing")
    if entity_counts["teleport"]:
        features.append("teleport_recontextualization")
    if entity_counts["monster"] >= 20:
        features.append("dense_combat_pressure")
    if entity_counts["switch"]:
        features.append("switch_route_change")
    if entity_counts["pickup"] >= 12:
        features.append("reward_breadcrumbing")
    if origin_bbox and origin_bbox.get("span_z", 0) > 220:
        features.append("entity_vertical_pressure")
    return features or ["unknown_route_shape"]


def analyze_source(source: SourceFile) -> dict[str, Any]:
    suffix = Path(source.virtual_name).suffix.lower()
    entities: list[dict[str, str]] = []
    points: list[tuple[float, float, float]] = []
    if suffix == ".bsp":
        entities = parse_bsp_entities(source.bytes_data)
        points = parse_bsp_vertices(source.bytes_data)
    elif suffix == ".map":
        text = source.bytes_data.decode("latin-1", errors="ignore")
        entities = parse_entities(text)
        points = parse_map_brush_points(text)

    entity_counts: Counter[str] = Counter()
    class_counts: Counter[str] = Counter()
    origins: list[tuple[float, float, float]] = []
    for entity in entities:
        classname = entity.get("classname", "unknown")
        class_counts[classname] += 1
        entity_counts[classify_entity(classname)] += 1
        origin = vector_from_origin(entity.get("origin", ""))
        if origin:
            origins.append(origin)
    bbox = bbox_from_points(points) or bbox_from_points(origins)
    origin_bbox = bbox_from_points(origins)
    return {
        "source_path": str(source.path),
        "virtual_name": source.virtual_name,
        "playable_level": is_playable_level(source.virtual_name),
        "sequence_key": sequence_key(source.virtual_name),
        "format": suffix.lstrip("."),
        "entity_count": len(entities),
        "entity_categories": dict(entity_counts.most_common()),
        "top_classnames": dict(class_counts.most_common(16)),
        "geometry_bbox": bbox,
        "origin_bbox": origin_bbox,
        "route_features": infer_route_features(entity_counts, class_counts, bbox, origin_bbox),
    }


def template_from_features(features: list[str], index: int) -> dict[str, Any]:
    feature_set = set(features)
    if "lock_or_gate_pacing" in feature_set and "switch_route_change" in feature_set:
        return {
            "id": f"quake_seq_{index:02d}_gate_loop_return",
            "route_sentence": ["visible_locked_goal", "side_loop_drop", "switch_or_key_pressure", "changed_route_read", "return_shortcut", "committed_exit_crossing"],
            "infinite_brutality_use": "Use when the player should understand a destination early, earn it through a side route, then move faster on the return.",
            "movement_lesson": "route memory turns the second crossing into skill expression",
        }
    if "vertical_layering" in feature_set and "dense_combat_pressure" in feature_set:
        return {
            "id": f"quake_seq_{index:02d}_vertical_bridge_line",
            "route_sentence": ["approach_lane", "stair_or_ramp_lip", "air_steer_gap", "upper_bridge_landing", "side_recovery_gallery", "visible_exit"],
            "infinite_brutality_use": "Use for triple-bridge rooms with upper crossings and recoverable side galleries.",
            "movement_lesson": "running-jump bunny-hop line across vertical bridge targets",
        }
    if "vertical_layering" in feature_set or "entity_vertical_pressure" in feature_set:
        return {
            "id": f"quake_seq_{index:02d}_layered_read",
            "route_sentence": ["entry_floor_read", "visible_upper_goal", "ramp_or_stair_lip", "mid_height_recovery", "upper_exit"],
            "infinite_brutality_use": "Use for readable stacked rooms where upper routes are visible before they are reached.",
            "movement_lesson": "height changes should teach the next jump line before the player commits",
        }
    if "long_acceleration_lanes" in feature_set:
        return {
            "id": f"quake_seq_{index:02d}_runway_jump_line",
            "route_sentence": ["long_readable_runway", "timing_lip", "bridge_or_gap_target", "overshoot_recovery", "reward_marker"],
            "infinite_brutality_use": "Use for bunny-hop training without cluttering the lane.",
            "movement_lesson": "run build-up and jump timing produce speed, not sprint toggles",
        }
    return {
        "id": f"quake_seq_{index:02d}_combat_sentence",
        "route_sentence": ["readable_entry", "central_commitment", "side_recovery", "landmark_pressure", "exit_read"],
        "infinite_brutality_use": "Use as a fallback room skeleton before dressing with props.",
        "movement_lesson": "room structure comes before decoration",
    }


def bootstrap_templates() -> list[dict[str, Any]]:
    return [
        {
            "id": "ib_triple_bridge_reference",
            "source": "recovered Infinite Brutality session note, not copied Quake geometry",
            "route_sentence": ["entry_read", "central_bridge_commitment", "side_gallery_recovery", "upper_crossing", "focal_threat", "exit_landing"],
            "generator_rules": [
                "Build the movement line first; dress it after it plays.",
                "Keep central bridge readable from spawn.",
                "Add side galleries as recovery and alternate speed lines.",
                "Use upper crossing as visible desire and route memory.",
                "Do not fill a box with random rubble to fake design.",
            ],
            "movement_lesson": "running jump / bunny-hop timing replaces crouch-slide",
        },
        {
            "id": "ib_bunnyhop_runway_lip",
            "source": "Quake movement abstraction from Thunder notes",
            "route_sentence": ["acceleration_runway", "bridge_or_stair_lip", "air_steer_window", "forgiving_landing", "optional_faster_landing"],
            "generator_rules": [
                "No crouch button.",
                "Expose speed via forward run build-up, jump buffer, and air steering.",
                "Make the faster line visible but not mandatory.",
                "Place recovery floor below or beside risky jump targets.",
            ],
            "movement_lesson": "bunny-hop feel is a route-design problem as much as a controller problem",
        },
        {
            "id": "ib_gate_loop_memory",
            "source": "Quake level pacing abstraction",
            "route_sentence": ["visible_goal", "blocked_direct_path", "side_loop", "route_change_trigger", "return_shortcut", "goal_crossing"],
            "generator_rules": [
                "The player should see a destination before earning it.",
                "Loop links must be physical and readable, not teleport-only.",
                "Lighting should distinguish critical path from optional loop.",
            ],
            "movement_lesson": "route knowledge turns traversal into skill expression",
        },
    ]


def build_outputs(records: list[dict[str, Any]]) -> dict[str, Any]:
    templates = []
    cumulative_features: Counter[str] = Counter()
    playable_records = [record for record in records if record.get("playable_level")]
    curriculum_records = playable_records or records
    for idx, record in enumerate(curriculum_records, 1):
        for feature in record["route_features"]:
            cumulative_features[feature] += 1
        template = template_from_features(record["route_features"], idx)
        template["source_level"] = record["virtual_name"]
        template["features"] = record["route_features"]
        template["cumulative_feature_counts"] = dict(cumulative_features)
        templates.append(template)
    if not templates:
        templates = bootstrap_templates()
    archetype_counts = Counter(re.sub(r"^quake_seq_\d+_", "", template["id"]) for template in templates)
    feature_counts = Counter(feature for record in curriculum_records for feature in record["route_features"])
    return {
        "license_boundary": {
            "rule": "Do not redistribute Quake map data or copied layouts. Store abstract route grammar only.",
            "accepted_inputs": [".map", ".bsp", ".pk3/.zip containing map or bsp"],
            "pak_note": "Extract BSP files from PAK externally before ingestion.",
        },
        "levels_processed": len(records),
        "playable_levels_processed": len(playable_records),
        "prefab_or_item_sources_processed": len(records) - len(playable_records),
        "levels": records,
        "templates": templates,
        "ml_level_design_lessons": {
            "training_scope": "playable Quake maps only when present; item prefab maps are retained as source metadata but excluded from route-template training",
            "feature_counts": dict(feature_counts.most_common()),
            "archetype_counts": dict(archetype_counts.most_common()),
            "generator_biases": [
                "Prefer readable vertical layering with side recovery over flat box rooms.",
                "Place long acceleration lanes before lips, bridges, stairs, or upper landings.",
                "Show goals before blocking them, then create a physical return shortcut after the route change.",
                "Use pickups and monsters as breadcrumbs along an already-valid movement sentence, not as random filler.",
                "Keep teleport use as recontextualization or shortcut punctuation; do not rely on it as the only loop connector.",
                "Exclude crouch vocabulary; bunny-hop feel comes from running jump timing, buffered jumps, air steering, and recoverable landings.",
            ],
        },
        "infinite_brutality_generator_contract": {
            "primary_reference": "authored triple-bridge skull guillotine hall",
            "forbidden_pattern": "generic boxes with scattered junk",
            "movement_vocab": ["running_jump", "jump_buffer", "air_steering", "bridge_lip", "ramp_lip", "stair_lip"],
            "not_movement_vocab": ["crouch_button", "crouch_slide", "duck_jump"],
        },
    }


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# Quake Route Grammar Curriculum",
        "",
        "This file stores abstract route grammar only. It must not contain copied Quake geometry, textures, entity dumps, or layouts.",
        "",
        f"- Levels processed: {payload['levels_processed']}",
        f"- Playable levels trained: {payload.get('playable_levels_processed', payload['levels_processed'])}",
        f"- Prefab/item sources retained as metadata: {payload.get('prefab_or_item_sources_processed', 0)}",
        f"- Infinite Brutality reference: {payload['infinite_brutality_generator_contract']['primary_reference']}",
        f"- Forbidden pattern: {payload['infinite_brutality_generator_contract']['forbidden_pattern']}",
        "",
        "## ML Level Design Lessons",
        "",
    ]
    lessons = payload.get("ml_level_design_lessons", {})
    if lessons:
        lines.append(f"- Training scope: {lessons['training_scope']}")
        lines.append("- Generator biases:")
        for bias in lessons["generator_biases"]:
            lines.append(f"  - {bias}")
        lines.append("- Feature counts:")
        for feature, count in lessons["feature_counts"].items():
            lines.append(f"  - {feature}: {count}")
        lines.append("")
    lines.extend([
        "## Templates",
        "",
    ])
    for template in payload["templates"]:
        lines.append(f"### {template['id']}")
        if template.get("source_level"):
            lines.append(f"- Source level: `{template['source_level']}`")
        if template.get("source"):
            lines.append(f"- Source: {template['source']}")
        lines.append(f"- Route sentence: {' -> '.join(template['route_sentence'])}")
        lines.append(f"- Movement lesson: {template['movement_lesson']}")
        if template.get("infinite_brutality_use"):
            lines.append(f"- Infinite Brutality use: {template['infinite_brutality_use']}")
        if template.get("generator_rules"):
            lines.append("- Generator rules:")
            for rule in template["generator_rules"]:
                lines.append(f"  - {rule}")
        if template.get("features"):
            lines.append(f"- Extracted features: {', '.join(template['features'])}")
        lines.append("")
    if payload["levels"]:
        lines.extend(["## Sequential Source Summary", ""])
        for idx, level in enumerate(payload["levels"], 1):
            trained = "trained" if level.get("playable_level") else "metadata-only"
            lines.append(f"{idx}. `{level['virtual_name']}` ({trained}): {', '.join(level['route_features'])}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract abstract route grammar from local Quake map/BSP sources.")
    parser.add_argument("--input", action="append", default=[], help="File or directory containing .map, .bsp, .pk3, or .zip inputs. Repeatable.")
    parser.add_argument("--out-dir", default="thunder-brainstorm/generated/quake_route_grammar")
    parser.add_argument("--allow-empty", action="store_true", help="Write bootstrap Infinite Brutality templates if no Quake sources are found.")
    args = parser.parse_args()

    sources = discover_sources([Path(p) for p in args.input])
    records = [analyze_source(source) for source in sources]
    if not records and not args.allow_empty:
        raise SystemExit("No Quake map/BSP sources found. Pass --allow-empty to emit bootstrap route templates.")

    payload = build_outputs(records)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "quake_route_grammar_curriculum.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    write_markdown(out_dir / "quake_route_grammar_curriculum.md", payload)
    print(json.dumps({"levels_processed": payload["levels_processed"], "out_dir": str(out_dir), "templates": len(payload["templates"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
