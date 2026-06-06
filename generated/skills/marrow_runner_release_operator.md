# marrow-runner-release-operator Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/marrow-runner-release-operator/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: marrow-runner-release-operator
description: "Use when working on Marrow Runner release, deployment, itch upload, standalone repo state, release docs, screenshots, generated assets, SFX manifests, or Club Crucible announcement/publication followups."
---

# Marrow Runner Release Operator

Use this for Marrow Runner release and publication work.

## Project Paths

```text
Standalone project: /storage/emulated/0/Documents/GodotProjects/marrow-runner
Historical prototype: /storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/prototypes/immune-maze-canvas
Thunder release packet: /storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/release_packets/marrow_runner_itch
```

## Known URLs

```text
Itch: https://grailawakeninggames.itch.io/marrow-runner
Social itch URL: https://valarsbeard.itch.io/marrow-runner
Club Crucible post: https://clubcrucible.web.app/valarsbeard-development/marrow-runner-ai-first-phone-workflow
```

## Validation

From the standalone project:

```sh
node --check src/main.js
python3 -m json.tool assets/asset_manifest.json >/dev/null
python3 -m json.tool assets/sfx/sfx_manifest.json >/dev/null
python3 -m json.tool release/page_assets/page_asset_manifest.json >/dev/null
python tools/build_itch_release.py
```

## Release Notes

- Release zips are generated and ignored.
- Large binary assets are tracked with Git LFS.
- Android shared storage may require executable Termux hook copies via repo-local `core.hooksPath`.
- Itch build target is `grailawakeninggames/marrow-runner:html`.
- Refresh Android media indexing for screenshots or page images copied into Pictures/Download before telling the user they are ready.

