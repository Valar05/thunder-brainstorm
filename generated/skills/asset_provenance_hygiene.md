# asset-provenance-hygiene Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/asset-provenance-hygiene/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: asset-provenance-hygiene
description: Use when adding, cataloging, moving, generating, importing, archiving, or licensing assets such as Godot .import/.uid sidecars, GLB/FBX/Blend files, generated images, Freesound/Creative Commons audio, TTS clips, source art libraries, or archive folders.
---

# Asset Provenance Hygiene

Use this skill when asset origin or ownership matters.

## Workflow

1. Identify asset class: generated, downloaded, imported, source-authored, archived, placeholder, canonical.
2. Preserve sidecars with Godot assets.
3. Record source, license, generator/tool, processing step, and target use.
4. Keep source libraries separate from project-owned runtime assets.
5. Update project source manifests or Thunder Brainstorm observations when asset policy changes.

## Typical Sources

- `Artsources/`
- `audio/`
- `sprites/`
- Godot `.import` and `.uid`
- `generated/`
- `revelation_tts_archive/`
- `audio/freesound_cc_manifest.json`

## Guardrails

- Do not delete or regenerate archives unless explicitly asked.
- Do not treat imported sidecars as independent source truth.
- For CC-BY audio, attribution must travel with the asset.

## Generated Image / Music / SFX Assets

For AI-generated or locally synthesized assets, record the asset after it becomes project-bound, not while it is still a preview in a tool cache.

Checklist:

1. Move/copy the final selected image/audio into the project or release asset folder.
2. Preserve prompt/source/tool notes, generator name, date when known, target use, and any ownership/license certificate.
3. Update the owning manifest, for example `assets/asset_manifest.json`, `assets/sfx/sfx_manifest.json`, or `release/page_assets/page_asset_manifest.json`.
4. For transparent/cutout assets, validate alpha corners, subject coverage, and edge fringing before wiring the asset.
5. For Android-visible exports under `/storage/emulated/0/Pictures`, `/storage/emulated/0/Download`, or `/storage/emulated/0/Documents`, refresh media/file indexing before reporting completion:
   ```sh
   am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d "file:///storage/emulated/0/Pictures/path/to/file.png"
   ```
6. Save sibling/versioned files unless the user explicitly asked to overwrite.

