#!/usr/bin/env python3
"""Build a provenance-bound Thunder progression gallery from a named source project."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "data" / "fleshpunk_gallery_sources.json"
DEFAULT_OUT = ROOT / "generated" / "galleries" / "fleshpunk-maze"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def png_dimensions(path: Path) -> list[int]:
    header = path.read_bytes()[:24]
    if not header.startswith(b"\x89PNG\r\n\x1a\n") or len(header) < 24:
        raise ValueError(f"not a valid PNG: {path}")
    return [int.from_bytes(header[16:20], "big"), int.from_bytes(header[20:24], "big")]


def write_if_changed(path: Path, data: bytes) -> bool:
    if path.exists() and path.read_bytes() == data:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    tmp.replace(path)
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    if config.get("schema") != "THUNDER VISUAL GALLERY SOURCES 1":
        raise SystemExit("REJECT: unknown gallery source schema")
    stages = config.get("stages", [])
    if [stage.get("stage") for stage in stages] != list(range(1, len(stages) + 1)):
        raise SystemExit("REJECT: gallery stages must be consecutive and ordered")
    if len(stages) < 2:
        raise SystemExit("REJECT: progression requires at least two stages")

    assets = args.out / "assets"
    receipts = []
    changed = 0
    for stage in stages:
        source = (source_root / stage["source_rel"]).resolve()
        if not source.is_relative_to(source_root):
            raise SystemExit("REJECT: source escapes source root")
        if not source.is_file():
            raise SystemExit(f"REJECT: missing stage source: {stage['source_rel']}")
        destination = assets / stage["file"]
        payload = source.read_bytes()
        changed += int(write_if_changed(destination, payload))
        receipts.append({
            **stage,
            "source_path": str(source),
            "source_sha256": hashlib.sha256(payload).hexdigest(),
            "gallery_path": destination.relative_to(ROOT).as_posix(),
            "raw_url": "/raw/" + destination.relative_to(ROOT).as_posix(),
            "gallery_sha256": sha256(destination),
            "dimensions": png_dimensions(destination),
            "bytes": destination.stat().st_size,
        })

    manifest = {
        "schema": "THUNDER VISUAL GALLERY 1",
        "marker": "THUNDER_FLESHPUNK_GALLERY_V2",
        "slug": config["slug"],
        "title": config["title"],
        "source_project": config["source_project"],
        "stage_count": len(receipts),
        "build_fingerprint": hashlib.sha256(json.dumps(receipts, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        "stages": receipts,
    }
    manifest_bytes = (json.dumps(manifest, indent=2) + "\n").encode()
    changed += int(write_if_changed(args.out / "gallery.json", manifest_bytes))
    print(json.dumps({"status": "PROCEED", "stages": len(receipts), "changed": changed, "fingerprint": manifest["build_fingerprint"], "out": str(args.out)}, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
