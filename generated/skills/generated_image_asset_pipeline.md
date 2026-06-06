# generated-image-asset-pipeline Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/generated-image-asset-pipeline/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: generated-image-asset-pipeline
description: "Use when AI-generated bitmap art, texture, sprite, icon, cover image, screenshot derivative, transparent cutout, or page asset needs to become a durable project/release asset with provenance, manifest entries, validation, and Android-visible file refresh."
---

# Generated Image Asset Pipeline

Use this after image generation or local image processing when the result is meant to be consumed by a project, website, itch page, or external upload.

## Workflow

1. Decide whether the image is preview-only or project-bound. Project-bound assets must be copied into the project/release folder.
2. Save non-destructively unless replacement was requested.
3. Record prompt/source/tool, target use, processing step, and ownership/license facts in the relevant manifest.
4. For transparent assets, validate alpha channel, transparent corners, subject coverage, and edge fringing.
5. For screenshots or upload images in Android shared storage, refresh media indexing:
   ```sh
   am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d "file:///storage/emulated/0/Pictures/path/to/file.png"
   ```
6. Report final saved paths and validation.

## Marrow Runner Manifest Examples

```text
assets/asset_manifest.json
assets/sfx/sfx_manifest.json
release/page_assets/page_asset_manifest.json
```

## Guardrails

- Do not leave runtime assets only under `$CODEX_HOME/generated_images` or temp folders.
- Do not overwrite source screenshots or originals without explicit request.
- Do not claim an asset is licensed/owned without a manifest, certificate, or source note.

