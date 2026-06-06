# Immune Maze Canvas Prototype

Dependency-free HTML canvas roguelike prototype for the immune-cell maze-chase game stub.

## Run

From this folder:

```sh
python -m http.server 8787
```

Open:

```text
http://127.0.0.1:8787/
```


## Itch Release Candidate

Build the private web-upload zip from this folder:

```sh
python tools/build_itch_release.py
```

The generated file lands under `release/` and includes the runtime web files, generated assets, and asset/SFX manifests. It intentionally excludes screenshots, harness pages, generation tools, and ownership-certificate PDFs.

Before uploading, source the local shell config only in the terminal session that will run the upload tool:

```sh
. ~/.bashrc
```

`ITCH_API_KEY` is for upload tooling only. Do not add it to source files, manifests, release zips, or logs. Upload the release as a private/unlisted itch build first, then smoke-test mobile fullscreen, audio unlock/background pause, tutorial flow, death restart, clear-data, seed replay, and level advance from the hosted page.

## Canvas Harness

With the local server running, open:

```text
http://127.0.0.1:8787/harness.html
```

The harness embeds phone/tablet/desktop viewport fixtures and checks canvas dimensions, grid dimensions, zone count, pickup counts, complement nodes, nonblank pixels, and pixel variation. It is browser-based so it can later be driven by Playwright or another real browser runner.

## Current Scope

- Roguelike start screen with generated seed creation, localStorage seed history, replayable old seeds, active-run resume, and deterministic seed+level room layouts.
- Main menu includes a standalone Tutorial button for movement, Pseudopod Ram, knockback, and chain reactions; the first New Run shows a one-time tutorial prompt only until the tutorial is completed or dismissed.
- Persistent shuffled background music begins from the first user input/start/tutorial action, continues across menu, death, restart, and seed transitions, can be disabled with the HUD/canvas music control or `M`, and pauses while the browser tab/app is backgrounded.
- Responsive organically grown tissue maze with looped routes, blob zones, and wavy vessel corridors.
- Faster free radial keyboard movement with wall sliding and strong grid-based gap assist.
- Faster free radial touch joystick with full-surface activation, directional max-speed response, D-pad base, pip overlay, and strong grid-based gap assist.
- Pseudopod Ram: rearmed below 0.25 input, initial movement from rest bursts into frame 4, launches enemies as recursive knockback projectiles, slightly biases chains toward nearby targets, and kills knocked enemies only when they hit a wall or another enemy.
- Complement nodes are suction pickups; complement also vacuum-ingests Germ Runners, which then respawn Pac-Man-style.
- Infection enemies pathfind through the tissue, kill on contact, emerge from a marked Infection Nest, avoid lymph-gate spawning, separate while chasing, respawn until the nest is cleansed, and use a spin/expand/fade death animation.
- Four ghost-style enemy archetypes are represented: pursuer, ambusher, flanker, and wanderer, with generated sprite-sheet art and procedural fallback.
- Responsive maze dimensions selected from viewport aspect ratio, with tall phone portrait grids around 18x32-34.
- Compact optional room/zone pockets embedded as organic tissue chambers.
- Mobile and fullscreen play hide the HTML HUD, draw a compact canvas HUD, and give the whole viewport to touch input.
- Forgiving circle-based wall collision against the tile-authored maze; topology widening is currently disabled after playtest.
- Generated red/pink tissue texture cropped to the board, masked separately for dark floors and brighter wall masses with cellular-noise wall boundaries.
- Sparse route-textured antibody placement with denser zone pockets.
- Antibody pickup has a short locally synthesized wet-glint sound effect played through low-latency decoded Web Audio with an overlapping HTMLAudio fallback pool.
- Antibody vacuum upgrade hook pulls nearby antibodies into the player.
- Complement nodes.
- Complement overdrive chain-collects adjacent antibodies.
- Full antibody collection triggers a visible cleanse wave that neutralizes the Infection Nest before the lymph gate finish.
- Canvas result banner includes a restart button for mobile/fullscreen play, with canvas-coordinate touch hit testing.
- Pause is available from the HUD, the top-right canvas control, and keyboard `P`/`Esc`.
- Lymph gate level-complete state with Advance action; each deeper level increases enemy count and expands the available archetype pool.
- Fever meter.
- Debug overlay.
- Player sprite sheet loaded from `assets/player/phagocyte_4frame_sprite_sheet.png`.

Current enemy pass is prototype art and tuning: infection blobs use procedural canvas rendering until dedicated enemy sprites are generated.

## Asset Plan

Generated assets should land inside `assets/` and be recorded in `assets/asset_manifest.json`.

Prototype SFX are planned in `assets/sfx/sfx_manifest.json` and can be generated one at a time. Local synthesized presets live in `tools/sfx_synth.py`, for example:

```sh
python tools/sfx_synth.py eat_antibody assets/sfx/eat_antibody_01.wav
python tools/sfx_synth.py --all
```

Needed next:

- optional refined player sheet with transparent background and exact frame bounds
- optional dedicated enemy sprites after the procedural infection-blob pass settles

## Generated Asset Notes

The first tile sheet, backdrop, and board tissue texture have been generated and recorded:

- `assets/tiles/immune_tile_sheet.png` (`1774x887`, sliced dynamically as 4x2)
- `assets/backgrounds/tissue_board_backdrop.png` (`1254x1254`)
- `assets/backgrounds/flesh_tissue_texture.png` (`1536x1024`, cropped to board aspect and masked for floor/walls)
- `assets/backgrounds/roguelike_tissue_menu_bg.png` (`1536x1024`, start/menu and atmosphere background)
- `assets/enemies/infection_archetype_sheet_chromakey.png` (`2172x724`, four enemy archetypes, runtime chroma-key cleanup)

The renderer keeps a dark procedural fallback if the tissue texture fails to load.
