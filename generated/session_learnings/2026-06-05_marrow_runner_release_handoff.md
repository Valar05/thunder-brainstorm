# Marrow Runner Release Handoff - Session Learnings

## Durable Project State

Marrow Runner is now a standalone sibling project:

```text
/storage/emulated/0/Documents/GodotProjects/marrow-runner
```

The old Thunder prototype remains as historical context:

```text
/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/prototypes/immune-maze-canvas
```

Standalone repo facts:

- Branch: `main`
- Initial standalone commit: `f951a0f Initial standalone Marrow Runner project`
- Git LFS observed file count: `44`
- Release zip is generated and ignored: `release/marrow-runner-v0.9.0-rc3-web.zip`
- Android shared storage does not reliably preserve executable git hook bits; use a local `core.hooksPath` in executable Termux storage for LFS hooks when needed.

## Runtime / Design Learnings

- The strongest feel came from free radial movement with strong grid/gap assist rather than strict gridlock.
- Pseudopod Ram should launch enemies, not directly kill them. Kills happen when launched enemies hit walls or other enemies.
- Chain reactions need generous acquisition and slight target bias or near misses feel unfair.
- Complement is separate from ram: complement sucks/ingests; ram launches; both need distinct sounds and visual feedback.
- Mobile fullscreen/itch iframe play needs DOM overlay controls in addition to canvas controls.
- Tutorial should demonstrate the chain reaction with a prepared setup, not just explain textually.
- Organic maze growth and cellular/noisy boundaries read better for the flesh theme than regular corridors or flat wall blocks.
- The infection nest/ghost-cage equivalent gives enemy spawning a readable high-risk zone.

## Release / Validation Commands

From the standalone Marrow Runner repo:

```sh
node --check src/main.js
python3 -m json.tool assets/asset_manifest.json >/dev/null
python3 -m json.tool assets/sfx/sfx_manifest.json >/dev/null
python3 -m json.tool release/page_assets/page_asset_manifest.json >/dev/null
python tools/build_itch_release.py
```

## Itch Facts

Known itch project:

```text
https://grailawakeninggames.itch.io/marrow-runner
```

Social/public URL used by the user:

```text
https://valarsbeard.itch.io/marrow-runner
```

Butler target:

```text
grailawakeninggames/marrow-runner:html
```

Latest known pushed build:

```text
version: v0.9.0-rc3
channel: html
upload: #17807876
build: #1707945
```

## Club Crucible Publication

Club Crucible live site:

```text
https://clubcrucible.web.app
```

Marrow Runner announcement post:

```text
https://clubcrucible.web.app/valarsbeard-development/marrow-runner-ai-first-phone-workflow
```

Remote repo/workspace:

```text
git@github.com:Valar05/club-crucible.git
ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/ClubCrucible
```

Published commit:

```text
f75ca8d Add Marrow Runner announcement post
```

## Android External File Rule

When moving, copying, exporting, or resizing files into Android-visible folders such as `Pictures`, `Download`, or `Documents`, refresh Android media/file indexing before reporting completion. This makes Google Files, gallery apps, upload pickers, and share sheets see the new files immediately.

Scoped refresh pattern:

```sh
am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d "file:///storage/emulated/0/Pictures/path/to/file.png"
```

## AI / Asset Workflow

- Use built-in image generation for project-bound raster assets, then move/copy outputs into the project; do not leave runtime assets in tool cache locations.
- Record generated art, generated music, and synthesized SFX in manifests.
- For transparent/cutout assets, validate alpha/fringing after chroma removal or other post-processing.
- For screenshots or external upload assets, save sibling copies rather than overwriting originals unless the user explicitly asks for replacement.
