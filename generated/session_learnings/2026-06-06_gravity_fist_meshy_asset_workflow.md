# Gravity Fist Meshy Asset Workflow - Session Learnings

Date: 2026-06-06

## Durable Paths

- Workspace CLI: `/storage/emulated/0/Documents/GodotProjects/tools/meshy_asset_workflow.py`
- Workflow note: `/storage/emulated/0/Documents/GodotProjects/docs/meshy_asset_workflow.md`
- Active Godot source project: `/storage/emulated/0/Documents/GodotProjects/gravity-fist`
- Active browser port: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs`
- Thunder project links: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/project_links/gravity_fist_project_links.md`

Generated Meshy assets should land under:

```text
PROJECT/assets/generated/meshy/ASSET_SLUG/
```

Each asset folder should include `manifest.json` with prompt, provider, task ids, request settings, downloaded files, target project, and timestamps. API keys must never be written to manifests.

## Workflow Shape

The intended prototype asset loop is:

1. Generate or select a 2D concept image.
2. Submit that image to Meshy image-to-3D.
3. Poll the asynchronous Meshy task.
4. Download GLB/FBX outputs before Meshy asset retention expires.
5. Optionally run Meshy rigging for standard humanoid bipeds.
6. Import or test in the target project.
7. Preserve provenance and import assumptions beside the asset.

For Gravity Fist humanoids, prefer clear front-facing or A-pose/T-pose biped silhouettes. Meshy rigging is viable for fast prototype characters, but treat results as prototype-ready until verified for:

- Godot/Three.js scale;
- skeleton and bone naming;
- forward axis and pose orientation;
- animation retargeting compatibility;
- hitbox and attachment-point placement.

## Three.js Port Context

`gravity-fist-threejs` is the active itch HTML5 target. Meshy outputs should be evaluated there with the existing pose lab and runtime asset import behavior before they are treated as production replacements.

Recommended evaluation path:

1. Generate/download the Meshy model into the Godot source project or a named project asset folder.
2. Mirror/copy only selected runtime-ready assets into `gravity-fist-threejs/assets/`.
3. Update `gravity-fist-threejs/assets/asset_manifest.json` with source and processing notes.
4. Use `pose-lab.html` to inspect orientation, scale, and animations.
5. Wire the model into `src/main.js` only after transform values are known.
6. Validate with the normal Three.js checks.

Validation commands from `gravity-fist-threejs`:

```sh
node --check src/main.js
python3 -m json.tool data/player_attacks.json >/dev/null
python3 -m json.tool data/security_titan.json >/dev/null
python3 -m json.tool assets/asset_manifest.json >/dev/null
python3 tools/build_web_release.py
```

## CLI Commands

Check environment and Meshy balance:

```sh
python3 tools/meshy_asset_workflow.py check --project gravity-fist --balance
```

Use Meshy's no-credit dummy key for API-shape tests:

```sh
python3 tools/meshy_asset_workflow.py check --project gravity-fist --balance --test-mode
```

Generate an OpenAI concept image:

```sh
python3 tools/meshy_asset_workflow.py openai-image \
  --project gravity-fist \
  --name alley_brute_01 \
  --prompt "stylized hulking biped street fighter, clear limbs, A-pose, game-ready concept art"
```

Submit image-to-3D with Meshy:

```sh
python3 tools/meshy_asset_workflow.py image-to-3d \
  --project gravity-fist \
  --name alley_brute_01 \
  --image-file gravity-fist/assets/generated/meshy/alley_brute_01/alley_brute_01_concept.png \
  --pose-mode a-pose \
  --pbr \
  --remesh \
  --polycount 50000 \
  --formats glb fbx
```

Submit and auto-rig:

```sh
python3 tools/meshy_asset_workflow.py image-to-3d \
  --project gravity-fist \
  --name alley_brute_01 \
  --image-file gravity-fist/assets/generated/meshy/alley_brute_01/alley_brute_01_concept.png \
  --pose-mode a-pose \
  --pbr \
  --remesh \
  --polycount 50000 \
  --formats glb fbx \
  --rig \
  --height 1.8
```

## Current Test State

Local validation passed:

```sh
python3 -m py_compile tools/meshy_asset_workflow.py
python3 tools/meshy_asset_workflow.py --help
python3 tools/meshy_asset_workflow.py check --project gravity-fist
python3 tools/meshy_asset_workflow.py image-to-3d --project gravity-fist --name cli_smoke_test --image-file gravity-fist/models/Ares_texture_0.png --pose-mode a-pose --pbr --remesh --polycount 50000 --formats glb fbx --dry-run --test-mode
```

The dry-run manifest exists at:

```text
/storage/emulated/0/Documents/GodotProjects/gravity-fist/assets/generated/meshy/cli_smoke_test/manifest.json
```

At the time this note was written, the plain shell saw `OPENAI_API_KEY` but did not see `MESHY_API_KEY`. The user's `~/.bashrc` exports Meshy as `MESHY_API_KRY`, so the CLI accepts `MESHY_API_KEY`, `MESHY_APIKEY`, and the existing typo `MESHY_API_KRY` from the environment, `~/.env`, workspace `.env`, or target project `.env`.

## Verified End-To-End Test

Real API validation succeeded on 2026-06-06 after sourcing `~/.bashrc`.

Test asset:

```text
/storage/emulated/0/Documents/GodotProjects/gravity-fist/assets/generated/meshy/cli_meshy_brawler_test/
```

Concept image:

```text
/storage/emulated/0/Documents/GodotProjects/gravity-fist/assets/generated/meshy/cli_meshy_brawler_test/cli_meshy_brawler_test_concept.png
```

Meshy image-to-3D:

```text
task: 019e9d9e-083e-772d-affd-c254dbc1fb02
status: SUCCEEDED
credits: 30
outputs:
- glb.glb
- fbx.fbx
```

Meshy rigging:

```text
task: 019e9da3-bb85-75c0-8bfd-bdf7858d7531
status: SUCCEEDED
credits: 5
outputs:
- rigged/rigged_character_glb_url.glb
- rigged/rigged_character_fbx_url.fbx
- rigged/basic_animations_walking_glb_url.glb
- rigged/basic_animations_walking_fbx_url.fbx
- rigged/basic_animations_walking_armature_glb_url.glb
- rigged/basic_animations_running_glb_url.glb
- rigged/basic_animations_running_fbx_url.fbx
- rigged/basic_animations_running_armature_glb_url.glb
```

Meshy balance moved from `1960` before the real image-to-3D test to `1925` after image-to-3D plus rigging. The manifest was refreshed after downloads and validates as JSON with signed Meshy URLs redacted:

```text
/storage/emulated/0/Documents/GodotProjects/gravity-fist/assets/generated/meshy/cli_meshy_brawler_test/manifest.json
```

The generated concept image is cropped near the head/feet and is a pipeline test, not a production-quality character brief. Use it for CLI/API validation and initial import experiments only.

## Guardrails

- Do not target `gothic-throne/assets/legacy/gravity-fist` for active Gravity Fist work.
- Do not rely on Meshy-hosted asset URLs for long-term storage; download selected outputs promptly.
- Do not commit or write API keys into manifests or docs.
- Keep generated source images, model outputs, and runtime-ready mirrored copies distinguishable in provenance.
- Refresh Android media/file indexing after creating or moving externally visible generated files under shared storage.
