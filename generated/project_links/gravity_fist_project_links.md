# Gravity Fist Project Links

Date: 2026-06-06

## Active Project

- Active Godot project: `/storage/emulated/0/Documents/GodotProjects/gravity-fist`
- Project name: `Gravity Fist`
- Main scene: `res://scenes/world.tscn`
- Player script: `/storage/emulated/0/Documents/GodotProjects/gravity-fist/scripts/player.gd`
- World script: `/storage/emulated/0/Documents/GodotProjects/gravity-fist/scenes/world.gd`
- AI conductor: `/storage/emulated/0/Documents/GodotProjects/gravity-fist/scenes/ai_conductor.gd`
- Enemy controller: `/storage/emulated/0/Documents/GodotProjects/gravity-fist/scenes/ai_controller.gd`
- Player attack data: `/storage/emulated/0/Documents/GodotProjects/gravity-fist/player_attacks.json`
- Enemy attack data: `/storage/emulated/0/Documents/GodotProjects/gravity-fist/security_titan.json`
- Vertical slice plan: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/design_packets/gravity_fist_vertical_slice_plan_2026-06-06.md`

## Target Warning

Do not edit `gothic-throne/assets/legacy/gravity-fist` when the user asks for Gravity Fist unless they explicitly name that archive mirror. The intended active target is the standalone `GodotProjects/gravity-fist` folder.

## Current Platform Notes

- Current project config is Godot 4.5 Mobile with mobile renderer.
- Current export preset is Android only.
- Target planning direction is web first.
- Local Godot wrapper exists but failed on 2026-06-06 before launch because `proot-distro login` rejected `--no-arch-warning`.

## Planning Direction

Bring the project toward a Gravity Fist-specific SOR4-inspired vertical slice:

- no normal jump button;
- Superman punch, block, and parry as signature loop;
- Gravity Fist jump slam as meter special;
- kicks/backfist/stomp repurposed as contextual specials;
- hit/parry-driven meter with damage/inactivity decay;
- radial AI pressure with varied archetypes;
- segment-based scrolling roguelike level generation;
- web export and later server-authoritative co-op.

## Three.js Target Correction

Correction added 2026-06-06: the final shipping target is `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs`, not a Godot Web export. The Godot project remains source of truth for combat behavior and assets. The Three.js port is the active implementation target for itch.io HTML5 hosting.

- Three.js target project: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs`
- Three.js orientation: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/PROJECT_ORIENTATION.md`
- Three.js instructions: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/AGENTS.md`
- Three.js entry point: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/index.html`
- Three.js runtime: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/src/main.js`
- Three.js release builder: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/tools/build_web_release.py`
- Current release zip: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/release/gravity-fist-threejs-web.zip`
- Thunder correction packet: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/design_packets/gravity_fist_threejs_itch_correction_2026-06-06.md`

## Meshy Asset Workflow

Durable Meshy/DALL-E-to-3D workflow notes added 2026-06-06:

- Thunder workflow note: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/session_learnings/2026-06-06_gravity_fist_meshy_asset_workflow.md`
- Workspace CLI: `/storage/emulated/0/Documents/GodotProjects/tools/meshy_asset_workflow.py`
- CLI usage note: `/storage/emulated/0/Documents/GodotProjects/docs/meshy_asset_workflow.md`
- Dry-run test manifest: `/storage/emulated/0/Documents/GodotProjects/gravity-fist/assets/generated/meshy/cli_smoke_test/manifest.json`
- Verified generated asset folder: `/storage/emulated/0/Documents/GodotProjects/gravity-fist/assets/generated/meshy/cli_meshy_brawler_test`
- Verified raw outputs: `/storage/emulated/0/Documents/GodotProjects/gravity-fist/assets/generated/meshy/cli_meshy_brawler_test/glb.glb`, `/storage/emulated/0/Documents/GodotProjects/gravity-fist/assets/generated/meshy/cli_meshy_brawler_test/fbx.fbx`
- Verified rigged outputs folder: `/storage/emulated/0/Documents/GodotProjects/gravity-fist/assets/generated/meshy/cli_meshy_brawler_test/rigged`

Use this workflow for generated humanoid or prop elements before importing them into the Three.js port. For `gravity-fist-threejs`, inspect Meshy GLB/FBX outputs in `pose-lab.html`, update `assets/asset_manifest.json`, then validate with the normal build commands before wiring replacements into `src/main.js`.

## Retarget Pose Lab

Retarget pose-lab notes added 2026-06-06:

- Thunder workflow note: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/session_learnings/2026-06-06_gravity_fist_threejs_retarget_pose_lab.md`
- Browser pose lab: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/pose-lab.html`
- Runtime code: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/src/pose-lab.js`

The pose lab now has source/target retarget controls, a real Bones panel populated from loaded skeletons, visible selectable bone handles, local bone Translate/Rotate/Scale editing, and separate retarget channel toggles. Use it as the first browser-side bridge between Gravity Fist Three.js GLB inspection and Phalanx-style rig/clip diagnosis.
