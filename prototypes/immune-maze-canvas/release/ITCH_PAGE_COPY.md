# Marrow Runner Itch Page Copy - v0.9.0-rc2

## Upload Assets

- Cover image / app picture: `release/page_assets/marrow-runner-itch-cover-630x500.png`
- Raw phagocyte frame 4 cutout: `release/page_assets/marrow-runner-phagocyte-frame4-transparent.png`
- Playable web build: `release/marrow-runner-v0.9.0-rc2-web.zip`

## Project Settings

- Title: `Marrow Runner`
- Project type: HTML / Playable in browser
- Visibility for first upload: Private or Restricted/Unlisted
- Pricing: Free / Name your own price, depending on how public you want the RC to feel
- Channel: `html`
- Version: `v0.9.0-rc2`
- Embed: Enable fullscreen button if itch offers it; the game also has an in-game fullscreen control.

## Short Description

A seeded immune-cell maze chase about cleansing infection nests and ramming germs into chain reactions.

## Page Description

Marrow Runner is a browser-playable immune-cell maze chase. You guide a phagocyte through living tissue, collect antibodies, cleanse an infection nest, and escape through the lymph gate before the infection overwhelms you.

Each run generates a seeded maze with organic rooms, enemy nests, antibody routes, complement pickups, and deeper levels that add pressure. Movement is fast and radial rather than locked to the grid, but the maze still has that classic chase-game rhythm: read the paths, bait the germs, grab the power, and survive one more descent.

The signature move is Pseudopod Ram. Release input to rearm, then move from rest to burst forward. A rammed germ becomes a projectile. If it hits a wall or another germ, it dies, and a clean hit can launch a whole chain reaction through the infection line.

This is a private release-candidate build for mobile and desktop testing before v1.0.

## Controls

- Touch: press anywhere on the game surface and drag to move
- Keyboard: WASD or arrow keys
- Pseudopod Ram: release input, then move from rest to dash
- Pause: P, Esc, or the pause button
- Music: M or the music button
- Fullscreen: in-game fullscreen button

## Features

- Seeded roguelike runs with replayable seed history
- Organic tissue maze layouts with rooms, zones, and infection nests
- Four germ archetypes inspired by classic chase enemies
- Pseudopod Ram knockback chains
- Complement pickup that vacuums and ingests enemies
- Tutorial scene for movement, ram timing, and chain reactions
- Mobile-first fullscreen canvas controls
- Generated tissue art, phagocyte sprite art, music, and locally synthesized SFX

## Suggested Tags

`html5`, `browser`, `arcade`, `maze`, `roguelike`, `mobile`, `touch-friendly`, `procedural`, `singleplayer`, `2d`, `survival`, `prototype`

## AI / Asset Disclosure

Marrow Runner uses project-owned generated visual/music assets and locally synthesized sound effects. Runtime asset provenance is recorded in `assets/asset_manifest.json` and `assets/sfx/sfx_manifest.json`; release page image provenance is recorded in `release/page_assets/page_asset_manifest.json`.

## Release Notes

v0.9.0-rc2 is the first itch release candidate. It includes seeded runs, tutorial flow, mobile fullscreen play, generated tissue art, four enemy archetypes, Pseudopod Ram chains, complement ingestion, music, SFX, pause/restart/clear-data controls, and a browser-playable web package.

## Claude Prompt For Alternate Wording

Use this if you want Claude to rewrite the page copy without changing the facts:

```text
Write concise itch.io page copy for a browser-playable game called Marrow Runner. It is an immune-cell maze chase: guide a phagocyte through organic tissue mazes, collect antibodies, cleanse an infection nest, and reach a lymph gate. The game has seeded roguelike runs, mobile touch controls, a tutorial, four ghost-style germ archetypes, complement power pickups, and a signature Pseudopod Ram move where releasing input rearms a dash that knocks germs into walls or each other for chain reactions. Tone: vivid, arcade, biological, not overly gross, not marketing-hype heavy. This is v0.9.0-rc2, a private release candidate before v1.0. Include a short description, main description, controls, feature list, suggested tags, and a brief AI/generated-asset disclosure.
```


## Hotfix Notes

v0.9.0-rc2 hotfix: larger canvas pause/music controls, a pause menu with Resume/Music/Main Menu, and a desktop HUD Menu button for exiting the run.
