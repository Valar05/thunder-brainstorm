# Three.js Phone Game Port Agent

Thunder Brainstorm corpus skill note for porting local Godot or canvas prototypes into phone-first Three.js web games. This is a doc-viewer/corpus skill note, not an installed Codex skill.

## Trigger

Use when a project in `/storage/emulated/0/Documents/GodotProjects` needs a faithful mobile web port, especially from Godot 3D combat into Three.js.

## Workflow

1. Identify the exact source project root. If duplicate mirrors or archives exist, confirm the active writable root before copying behavior or assets.
2. Read source orientation docs, local `AGENTS.md`, and engine entry points. For Godot, inspect `project.godot`, main scene scripts, autoloads, data JSON, and available GLB/audio/image assets.
3. Build a parity map before coding: live playable systems, dead or unreachable systems to exclude, source data files to preserve as runtime JSON, assets to copy with provenance, and mechanics requiring browser-specific approximation.
4. Create a phone-first Three.js project: fullscreen canvas, fixed-step simulation, DOM HUD and menus, WebAudio unlock, deterministic zip builder, and asset manifest.
5. Preserve mechanics before visual polish. Use source GLB assets when usable, but include procedural fallbacks so validation can continue when imports fail.
6. Keep mobile controls native-feeling: full-surface pointer events, large HUD buttons, no in-game control clutter, and desktop keys/mouse as secondary support.
7. Validate with JS syntax check, JSON checks, release zip `testzip()`, local server, mobile viewport smoke, and manual feel checks.
8. Refresh Android file indexing for generated/copied project assets and release files under shared storage.

## Porting Heuristics

- Treat Godot `Engine.time_scale` as a browser clock multiplier with unscaled timers for hit pause.
- Replace `CharacterBody3D` with simple capsule/circle collision on the X/Z plane unless exact physics is central to the game.
- Replace `NavigationAgent3D` with direct steering, radial slots, and simple collision/yield logic for vertical slices.
- Preserve attack windows from JSON: startup, active duration, dash start, dash distance, cooldown, recovery, hit reaction, and knockback.
- Keep dead systems out of parity. Mention them in orientation docs instead of silently deleting source context.

## Gravity Fist Evidence

- Source root: `/storage/emulated/0/Documents/GodotProjects/gravity-fist`
- Port root: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs`
- Live slice files: `scripts/player.gd`, `scenes/ai_controller.gd`, `scenes/ai_conductor.gd`, `scenes/world.gd`, `player_attacks.json`, `security_titan.json`
- Excluded dead systems: move shop, move currency, level-up offer overlay, combo-row UI, drag/drop move slots, reroll, progression menus.

## Reusable Thunder Patterns

- From Armor Command: phone-first full-surface input, sparse live HUD, manifest-backed assets, WebAudio SFX bus, cache-busted JS, deterministic release zip.
- From Marrow Runner: DOM overlays for phone/itch iframe play, local validation scripts, release handoff docs, and Android media refresh after exports.
