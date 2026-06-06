# Immune Maze Canvas Prototype

A dependency-free HTML canvas prototype has been bootstrapped at:

```text
prototypes/immune-maze-canvas/
```

Local prototype URL:

```text
http://127.0.0.1:8787/
```

## Current Scope

- 21x21 interconnected tissue maze with looped routes.
- Compact optional room/zone pockets embedded in maze-first tissue corridors.
- Keyboard movement with buffered turns.
- Touch joystick with D-pad base and pip overlay, ported from the `gravity-fist/scripts/joystick.gd` behavior.
- Wall collision.
- Contiguous flesh wall masses with edge-only boundaries and dark procedural floor texture.
- Antibody pickup collection.
- Complement nodes.
- Complement overdrive chain-collects adjacent antibodies.
- Lymph gate win condition.
- Fever meter and HUD.
- Debug toggle.
- Project-local phagocyte sprite sheet copied into `assets/player/`.

## Project Files

- `prototypes/immune-maze-canvas/index.html`
- `prototypes/immune-maze-canvas/styles.css`
- `prototypes/immune-maze-canvas/src/main.js`
- `prototypes/immune-maze-canvas/data/level_01.json`
- `prototypes/immune-maze-canvas/assets/asset_manifest.json`
- `prototypes/immune-maze-canvas/assets/player/phagocyte_4frame_sprite_sheet.png`

## Next Assets To Generate Inside The Project

- `assets/tiles/immune_tile_sheet.png`
- `assets/backgrounds/tissue_board_backdrop.png`
- optional refined player sheet with transparent background and exact 4-frame bounds

## Run Command

```sh
cd /storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/prototypes/immune-maze-canvas
python -m http.server 8787
```

## Generated Assets Added

The project now includes generated prototype visuals:

- `prototypes/immune-maze-canvas/assets/tiles/immune_tile_sheet.png` (`1774x887`, 4x2 dynamic slicing)
- `prototypes/immune-maze-canvas/assets/backgrounds/tissue_board_backdrop.png` (`1254x1254`)

Both are recorded in `prototypes/immune-maze-canvas/assets/asset_manifest.json`. The canvas renderer uses them when loaded and keeps procedural fallback drawing available.

