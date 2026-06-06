#!/usr/bin/env python3
"""Build a clean itch.io web zip for Marrow Runner."""
from __future__ import annotations

import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN_JS = ROOT / "src" / "main.js"
RELEASE_DIR = ROOT / "release"
INCLUDE_FILES = [
    "index.html",
    "styles.css",
    "README.md",
    "assets/asset_manifest.json",
    "assets/sfx/sfx_manifest.json",
]
INCLUDE_DIRS = ["src", "data"]
ASSET_EXTENSIONS = {".png", ".mp3", ".wav", ".json"}
EXCLUDE_NAMES = {".DS_Store"}


def app_version() -> str:
    match = re.search(r"const APP_VERSION = '([^']+)'", MAIN_JS.read_text())
    if not match:
        raise SystemExit("APP_VERSION not found in src/main.js")
    return match.group(1)


def add_file(zipf: zipfile.ZipFile, path: Path) -> None:
    if path.name in EXCLUDE_NAMES:
        return
    zipf.write(path, path.relative_to(ROOT).as_posix())


def iter_release_files():
    for name in INCLUDE_FILES:
        path = ROOT / name
        if not path.exists():
            raise SystemExit(f"Missing release file: {name}")
        yield path

    for dirname in INCLUDE_DIRS:
        root = ROOT / dirname
        if not root.exists():
            raise SystemExit(f"Missing release dir: {dirname}")
        for path in sorted(root.rglob("*")):
            if path.is_file():
                yield path

    assets = ROOT / "assets"
    if not assets.exists():
        raise SystemExit("Missing assets dir")
    for path in sorted(assets.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() in ASSET_EXTENSIONS:
            yield path


def main() -> None:
    version = app_version()
    RELEASE_DIR.mkdir(exist_ok=True)
    out = RELEASE_DIR / f"marrow-runner-{version}-web.zip"
    files = []
    seen = set()
    for path in iter_release_files():
        rel = path.relative_to(ROOT).as_posix()
        if rel in seen:
            continue
        seen.add(rel)
        files.append(path)

    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        for path in files:
            add_file(zipf, path)

    size_mb = out.stat().st_size / (1024 * 1024)
    print(f"built {out.relative_to(ROOT)}")
    print(f"files {len(files)}")
    print(f"size {size_mb:.2f} MB")


if __name__ == "__main__":
    main()
