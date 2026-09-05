# Infinite Brutality Project Links

Date: 2026-06-08

## Local Project

- Project root: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality`
- Browser entry: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/index.html`
- Runtime: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/src/main.js`
- Styles: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/src/styles.css`
- Orientation: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/PROJECT_ORIENTATION.md`
- Local Thunder pointer: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/THUNDER_LINKS.md`
- Local level-design workflow: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/docs/LEVEL_DESIGN_WORKFLOW.md`
- Rock shape grammar: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/docs/ROCK_SHAPE_GRAMMAR.md`
- Vertical district realization plan: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/docs/VERTICAL_DISTRICT_REALIZATION_PLAN.md`

## Local URLs

- Play URL: `http://127.0.0.1:8798/infinite-brutality/index.html`
- Thunder docs URL: `http://127.0.0.1:8765/`

## Thunder Records

- Main prototype lessons: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/session_learnings/2026-06-08_infinite_brutality_prototype_lessons.md`
- General level-design workflow: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/skills/level_design_environment_grammar.md`
- Project links: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/project_links/infinite_brutality_project_links.md`
- Project links JSON: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/project_links/infinite_brutality_project_links.json`
- Manual source refs: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/source_refs_manual/infinite_brutality_source_refs.jsonl`
- Meshy/PBR rendering handoff: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/session_learnings/2026-06-15_infinite_brutality_meshy_pbr_rendering_handoff.md`
- Meshy/PBR rendering source refs: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/source_refs_manual/infinite_brutality_meshy_pbr_rendering_source_refs.jsonl`
- Rock shape grammar handoff: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/session_learnings/2026-06-15_infinite_brutality_rock_shape_grammar.md`
- Rock shape grammar source refs: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/source_refs_manual/infinite_brutality_rock_shape_grammar_source_refs.jsonl`
- Precursor Arcane/FPS platformer brainstorm: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/session_learnings/2026-06-07_fps_platformer_arcane_ik_brainstorm.md`
- Quake/touch movement brainstorm: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/session_learnings/2026-06-08_quake_movement_touch_speedrun_brainstorm.md`
- Quake route grammar curriculum: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/quake_route_grammar/quake_route_grammar_curriculum.md`
- Quake route grammar extractor: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/tools/quake_route_grammar.py`
- Infinite Brutality level contract: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/LEVEL_GENERATION_CONTRACT.md`
- Infinite Brutality route template data: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/data/level_route_templates.json`
- Room junction batch list: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/docs/ROOM_JUNCTION_BATCH_LIST.md`
- Room junction batch data: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/data/room_junction_batch.json`
- Generated room batch module: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/src/generated_room_batch.js`
- Room batch implementation doc: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/docs/ROOM_BATCH_IMPLEMENTATION.md`
- Quake legal source manifest: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/external_sources/quake_map_sources/source_manifest.json`
- Quake source archive: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/external_sources/quake_map_sources/quake-maps-master.zip`

## Build Context

Current documented runtime build: `0.8.175`. The page cache-buster should point at `src/main.js?v=0.8.175`.

Serve from the GodotProjects root:

```sh
cd /storage/emulated/0/Documents/GodotProjects
python3 -m http.server 8798
```

## Design Direction

Infinite Brutality is the active phone-landscape Three.js first-person melee/platformer prototype. Use FPSPlayer arms for first-person combat readability, low-poly primitive architecture for world identity, Quake-inspired but touch-forgiving movement where bunny-hop feel is merged into running jump rather than crouch, triple-bridge/route-grammar room generation instead of junk-box prop scatter, diegetic light sources, a flat vector Limbo sky dome, and SVG-authored stone/bronze/bone material textures that match the low-poly geometry without bitmap grain or gradients.

## Quake Training Status

Legal Quake map-source ingest is complete: 63 total `.map` sources scanned, 41 playable maps trained, 22 item/prefab sources retained as metadata only. The game project receives abstract ML level-design lessons and route templates only.

## Build 0.7.3 Measured Room

The active authored room is now a compact Quake-style route space: short entry read, runway lip, offset bridge commitments over a central void, west recovery/gallery stair, upper crossing, and visible skull exit gate. It replaces the earlier oversized `38 x 60` gold hall with a tighter `24 x 36` room where movement line readability matters before decoration.

## Room Junction Batch List

A generous overnight room batch list now exists with 48 room specs by connector topology: 14 one-connector terminals, 20 two-connector workhorses, 10 three-connector junctions, and 4 four-connector hubs. Runtime frequency should favor two-connector workhorses, while one-connector rooms get many semantic flavors.

## Build 0.7.4 Panorama Skybox

The skybox now uses `assets/textures/ib-vector-limbo-panorama-20260609.svg`, a locally authored flat-vector panorama with distant Limbo walls, bridge silhouettes, spires, and non-black horizon bands. Runtime sky material color is set to white after texture load so the SVG is not crushed toward black. This should replace the pure-black void visible through gates without turning the game into a starscape.

## Build 0.8.0 Generated Room Batch

The full 48-room junction batch is now generated into `../infinite-brutality/src/generated_room_batch.js` and wired into runtime. `src/main.js` imports `GENERATED_ROOM_BATCH`, builds compact blockouts from connector signatures, semantic roles, route sentences, and vertical overlays, then advances room-by-room when the player reaches the exit marker. The sequence wraps after all 48 rooms and increments the level index.

## Build 0.8.1 Real Bitmap Skybox

A real generated bitmap skybox now lives at `../infinite-brutality/assets/textures/ib-real-limbo-skybox-20260609.png`. It was generated with the built-in image tool, copied into the project, center-cropped/resized to `2048x1024`, recorded in `assets/asset_manifest.json`, and wired into the sky dome in `src/main.js`. The page cache-buster is `src/main.js?v=0.8.1`.

## Build 0.8.3 Physical Gauntlet Fix

A screenshot of build `0.8.1` exposed two generator failures: every room collapsed into a one-bridge room and surfaces depth-fought because pads/bridges shared planes with the base floor. Build `0.8.3` changes generated rooms to floor-first compact chambers, removes the default global side void, raises overlays off the base plane, and builds all 48 rooms into one physical gauntlet connected by walkable spans. Ordinary room exits no longer teleport/rebuild the next room.

## Build 0.8.174 Sandstone Mesh Harness

Active sandstone terrain now uses manifold exposed voxel faces generated from the same collision voxel field. The fix removes diagonal-only voxel contacts before meshing and extends `tools/test_island_mesh_integrity_contract.mjs` to check the active sedimentary island and bridge mesh paths, not just the legacy surface-net path.

## Build 0.8.175 Visual Weathering

The sandstone mesh remains collision-backed and manifold, but its visible vertices now receive deterministic sediment shear and erosion offsets so it does not read as exact kitbashed cubes. The rock grammar contract records this as an off-grid visual vertex ratio check.
