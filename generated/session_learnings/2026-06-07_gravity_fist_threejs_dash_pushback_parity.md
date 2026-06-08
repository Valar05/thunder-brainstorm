# Gravity Fist Three.js Dash And Pushback Parity - Session Learnings

Date: 2026-06-07
Project: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs`
Source of truth: `/storage/emulated/0/Documents/GodotProjects/gravity-fist`

## Problem Signal

User playtest feedback said attack dash and pushback felt delayed or nonexistent. The important correction was to inspect source movement math rather than only tune visible distances.

## Source Findings

- Godot player attack dash is scheduled by `dash_start`, then clamped to the target gap before activating.
- Godot dash displacement uses a quadratic ease-out over `DASH_TIME = 0.25` and stops at `_dash_stop_progress = 0.3`, so the visible movement is a short microdash rather than a linear dash across the whole attack.
- Godot knockback distance is `max(dash * 0.75, MIN_ATTACK_KNOCKBACK_DISTANCE) * knockback_multi`, with a `0.12s` impulse. Formula order matters: light Jab remains subtle, but larger dash moves such as Backfist must not be flattened to a small constant.

## Runtime Fix

Three.js now mirrors the Godot shape:

- `PLAYER_ATTACK_DASH_TIME = 0.25`
- `PLAYER_ATTACK_DASH_STOP_PROGRESS = 0.3`
- target-gap clamping in `getPlayerAttackDashGap()` and `clampPlayerAttackDashDistance()`
- ease-out displacement in `updatePlayerAttackDash()`
- source-parity knockback in `getPlayerKnockbackDistance()`

## Validation Learning

Add displacement-based regression probes for combat feel. The useful proof was not just damage landing; it measured actual movement:

- player Jab dash: `0.183m`
- enemy pushback from Jab: `0.125m`
- computed Jab knockback: `0.113m`
- computed Backfist knockback: `0.675m`

Validated with `node --check src/main.js`, JSON checks, Android browser `video-regression-suite` at `v=0.4.23`, and `python3 tools/build_web_release.py`.

## Reusable Rule

When a ported melee move feels late or weak, compare source scheduling, hitbox arming, dash easing, gap clamp, and knockback formula order before changing constants. Add an in-runtime probe that records displacement for both actor and target.

## Source References

- Godot dash gap and clamp: `gravity-fist/scripts/player.gd:785`
- Godot knockback formula: `gravity-fist/scripts/player.gd:1291`
- Godot ease-out dash: `gravity-fist/scripts/player.gd:1738`
- Godot hit knockback impulse: `gravity-fist/scripts/player.gd:1812`
- Three.js constants/state: `gravity-fist-threejs/src/main.js:41`, `gravity-fist-threejs/src/main.js:820`
- Three.js dash gap/ease/knockback: `gravity-fist-threejs/src/main.js:2450`, `gravity-fist-threejs/src/main.js:2478`, `gravity-fist-threejs/src/main.js:2500`
- Three.js hit application: `gravity-fist-threejs/src/main.js:2571`
- Three.js regression probe: `gravity-fist-threejs/src/main.js:3646`, `gravity-fist-threejs/src/main.js:3939`
