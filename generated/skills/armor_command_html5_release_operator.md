# Armor Command HTML5 Release Operator Skill

Thunder Brainstorm corpus skill note distilled from the Armor Command 1.0 release workflow. This is a doc-viewer/corpus skill note, not an installed Codex skill.

## Trigger

Use when an HTML5/canvas prototype in `/storage/emulated/0/Documents/GodotProjects` needs mobile-first iteration, generated assets, WebAudio SFX, itch packaging, or Android/Termux release handling.

## Workflow

1. Read the project `PROJECT_ORIENTATION.md` and local `AGENTS.md` before editing.
2. Keep controls phone-first: full-surface touch input, minimal HUD buttons, settings in title/pause menus.
3. For generated images, copy final assets into project-owned `assets/`, preserve source/prompt/cache path in `assets/asset_manifest.json`, and validate alpha/crop before wiring.
4. For SFX, use `assets/sfx/sfx_manifest.json`, decoded WebAudio buffers, pitch/gain variation, procedural fallback, and a separate persistent SFX toggle.
5. For music/SFX balance, tune both source gain and post-compressor output gain; cache-bust hosted JS after mix changes.
6. Package with a deterministic zip script that includes HTML/CSS/JS plus `assets/**/*.json`, images, WAV, and MP3 files.
7. Validate with `node --check`, JSON parsing, atlas parsing, and zip `testzip()`.
8. Upload with the locally compiled Termux butler binary and record upload/build/version in Thunder project links.
9. Refresh Android media/file indexing for release zips, manifests, page assets, screenshots, and Thunder docs that the user may open externally.

## Armor Command Evidence

- Runtime: `/storage/emulated/0/Documents/GodotProjects/mecha-command/src/main.js`
- Build script: `/storage/emulated/0/Documents/GodotProjects/mecha-command/tools/build_web_release.py`
- Project manifest: `/storage/emulated/0/Documents/GodotProjects/mecha-command/assets/asset_manifest.json`
- SFX manifest: `/storage/emulated/0/Documents/GodotProjects/mecha-command/assets/sfx/sfx_manifest.json`
- Thunder source refs: `generated/source_refs_manual/armor_command_prototype_source_refs.jsonl`

## Reusable Lessons

- A compressor can hide perceived SFX volume changes; add and document a post-compressor output gain.
- Itch/mobile browsers can serve stale JS; version the script URL for release builds.
- Generated backgrounds should improve composition but still need gameplay readability overlays.
- Separate hostile arrays need a shared snapshot or collision path so targeting, explosions, and wave-clear checks do not miss new enemy families.
- For 1.0 mobile HUDs, keep live gameplay buttons sparse and move preferences to menus.
