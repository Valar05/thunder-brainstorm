# Infinite Brutality Enemy Sweep And Player Hurt Lessons

Date: 2026-06-11

## Project

Infinite Brutality combat iteration moved from vague "enemy probably hit me" feedback toward an inspectable runtime with explicit enemy hand-sweep contact, player health UI, and player-arm hurt/recover clips.

Local project: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality`
Pose tooling: `/storage/emulated/0/Documents/GodotProjects/pose-lab`

## Core Lessons

### 1. Separate query math from body collision

A visible melee debug volume can trick debugging if the real gameplay separation is happening elsewhere. In this pass, the attack sweep itself was only a closest-distance query between the enemy hand segment and the player capsule. The physical shove came from player/enemy non-overlap resolution, not from the attack sweep.

General lesson: when debugging melee, keep these ownership surfaces separate:

- animation sample source
- contact query math
- body-overlap resolution
- debug rendering

### 2. Deterministic attack labs are worth the extra plumbing

Normal engagement logic can hide combat bugs behind orbiting, retreat spacing, and room noise. A dedicated `attacklab` mode that stages the enemy in repeatable range and a large readable debug HUD cut through that ambiguity quickly.

General lesson: if the same combat bug survives multiple tuning passes, stop changing constants and build a deterministic lab mode.

### 3. Match the debug visual to the actual tested geometry

The useful breakthrough was drawing the actual player damage capsule and comparing pre-dash versus post-dash sweep traces. That stopped the team from treating a decorative box visual as if it were the real collision model.

General lesson: if the runtime uses a segment-to-capsule or capsule-to-capsule query, draw that, not a simpler proxy.

### 4. FPS-arms reaction choice should come from real GLB action inventory

The player hurt/restart choice was not guessed from aliases. The `FPSPlayer.glb` action list was enumerated first, then concrete candidates were selected by real clip name and duration:

- hurt: `FistInjuredRight`
- fallback impacts: `FistBlockHitLeft`, `FistBlockHitParry`
- restart: `FistReadied`
- steady ready: `FistReady`

General lesson: for embedded GLB rigs, enumerate `animations[].name` before selecting runtime reactions.

### 5. Visible player damage matters more than hidden counters

Enemy damage had already been landing, but without a strong player-facing reaction it looked like failure. The health bar, damage flash, and now hurt/recover arms clips made the same contact path readable.

General lesson: a combat system can be technically working and still appear broken if the defender has no visible damage response.

## Source Anchors

- Infinite Brutality runtime: `../infinite-brutality/src/main.js`
- FPSPlayer clip wiring in Pose Lab: `../pose-lab/src/rig-profiles.js`
- Project-local combat note: `../infinite-brutality/docs/PLAYER_HURT_AND_ENEMY_SWEEP_NOTES.md`

## Reusable Pattern Names

Candidate generalized patterns from this pass:

- `segment_capsule_melee_query`
- `deterministic_attack_lab_mode`
- `debug_geometry_matches_runtime_query`
- `embedded_glb_action_inventory_first`
- `visible_defender_damage_response`
