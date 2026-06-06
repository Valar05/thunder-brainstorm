# Gravity Fist Vertical Slice Plan

Date: 2026-06-06
Target project: `/storage/emulated/0/Documents/GodotProjects/gravity-fist`
Thunder role: durable planning packet for bringing the current Godot project toward a Gravity Fist-specific Streets of Rage 4 quality target, with web as the main platform.

## Orientation

Gravity Fist is currently a Godot 4.5 Mobile project using `res://scenes/world.tscn` as the main scene. The project is not a git repo in this workspace. Do not confuse this standalone project with the archived mirror under `gothic-throne/assets/legacy/gravity-fist`.

Current foundations:

- `project.godot`: `config/name="Gravity Fist"`, `run/main_scene="res://scenes/world.tscn"`, `renderer/rendering_method="mobile"`.
- Main scene: `scenes/world.tscn`, a `WorldEnvironment` with camera, static walkway/container dressing, player, `AIConductor`, music holder, and CanvasLayer UI.
- Core scripts: `scripts/player.gd`, `scenes/world.gd`, `scenes/ai_controller.gd`, `scenes/ai_conductor.gd`.
- Data: `player_attacks.json`, `security_titan.json`.
- Assets: `models/Ares.glb`, `models/SecurityTitan.glb`, Meshy-style textures, container/walkway meshes, outline shader, nova sprite/normal, music and punch SFX.

Validation status from this pass:

- `godot` exists at `/data/data/com.termux/files/home/bin/godot`, but the wrapper failed before launching because `proot-distro login` rejected `--no-arch-warning`.
- Treat that as a local validation environment issue, not a confirmed project parse/runtime failure.
- No project-local smoke tests or bootstrap scripts were found.
- `export_presets.cfg` currently has Android only. Web export preset is not present yet.

## Current Combat Surface

Already useful:

- Five-slot standard combo loadout with purchasable/reorderable moves.
- Special catalog: `Headbutt`, `SupermanPunch`, `LowBackKick`, `FrontKick`, `Backfist`, `SpinningHighKick`, `AxeKick`, `AxleKick`.
- Combo finisher rows from zero hit to five hit with default fallback behavior.
- Hold input can trigger stomp on prone/stompable targets, otherwise buffers the configured held special.
- Right-side swipe combat input drives block, Superman punch, sidestep, and attacks.
- Block/parry has facing check, counter window, heal-on-parry hook, and AI attack lockout.
- Attack aim already auto-targets lane enemies and gives Superman punch wider targeting.
- Enemy hit flow supports knockdown, prone, stomp damage, bleed, bonus hit counts, impact damage, blood spray, hit reactions, and camera shake.
- World has item affixes, rarity rolls, XP/level progression, move shop, move upgrades, and move currency plumbing.
- AI has radial support slots, one active attacker permission, wounded flee/replacement, respawn pressure, camera-edge spawning, and enemy combo data.

Mismatches with the requested target:

- Requested special bar is hit-driven and decays on damage or inactivity. Current progression is XP/level/shop-driven and does not yet model combat momentum.
- Normal jump input still exists in `scripts/player.gd`; target slice should remove normal jumps and keep aerial impact as specials only.
- Specials exist, but live UX presents them mainly as combo rows/shop finishers instead of fast contextual SOR4-style specials.
- Grabs are absent as a first-class state machine.
- Web export/networking are absent.

## Product Target

This is not a full SOR4 clone. Target a Gravity Fist vertical slice with 3D side-scrolling readability, punch-heavy pressure, no normal jump button, Superman punch/block/parry as the signature loop, Gravity Fist jump slam as the first meter special, contextual specials from existing kick/backfist/stomp animations, radial enemy pressure, small varied enemy roster, simple scrolling roguelike level generation, web-first export, and later low-maintenance secure co-op.

## Phase 0: Stabilize Web Target And Validation

- Fix or bypass the local Godot wrapper so `godot --headless --path gravity-fist --quit` runs.
- Add `PROJECT_ORIENTATION.md` to Gravity Fist with main scene, scripts, validation commands, target platform, asset policy, and archive warning.
- Add a minimal `tools/smoke_project.gd` that loads `world.tscn`, checks player/enemy/controller nodes, parses `player_attacks.json` and `security_titan.json`, and exits nonzero on failure.
- Add a Web export preset. Target Compatibility/WebGL 2 for Godot 4 web export.
- Export to local `build/web`, serve over HTTP, verify first scene and console.
- Decide thread support early. If enabled, hosting must support cross-origin isolation headers for `SharedArrayBuffer`; if not, accept audio/performance constraints and test on mobile browsers.

Acceptance: headless smoke runs, JSON parses, web preset exists, local web build reaches playable scene.

## Phase 1: Combat Contract Lock

- Remove normal jump from player input. Keep jump slam as a special animation/attack only.
- Convert the five-combo branch from live complexity into a smaller baseline chain plus contextual special slots.
- Keep standard chain to three or four clear punches: Jab, Cross, Hook/Uppercut, finisher.
- Repurpose current specials:
  - `SupermanPunch`: gap-close/check/counter-chase special.
  - `LowBackKick` / `FrontKick`: crowd push or armor-break contextual special.
  - `Backfist`: behind/side threat response.
  - `CurbStomp`: prone contextual special.
  - `GravityFistSlam`: meter special using the existing jump slam animation.
- Add move-role fields to attack JSON: `standard`, `defensive_counter`, `contextual_special`, `meter_special`, `prone_special`.
- Add meter costs/gains to attack JSON instead of hard-coding every special.

Acceptance: tap chain is reliable, swipe/block/Superman remain distinct, hold special does not steal basic attacks, no normal jump is reachable in live play.

## Phase 2: Momentum Special Meter

Recommended model:

- `special_meter_max = 100`.
- Normal hit gain: 5-8.
- Heavy/special hit gain: 8-12, but never self-refunds full cost.
- Parry gain: 12-18.
- Stomp/prone finisher gain: small or zero if it is already a payoff.
- Damage taken: immediate meter loss scaled by damage.
- Inactivity decay starts after 2.0-3.0 seconds without hit/parry and drains slowly.
- Meter tiers: 25 contextual special, 50 enhanced cancel/counter, 75-100 Gravity Fist slam.

Implementation anchors:

- Add meter state in `scripts/player.gd` or a small `CombatMeter` autoload.
- Use `_notify_style_hit_hook()` / `_on_hitbox_body_entered()` for successful hit gain.
- Use `try_block_hit()` for parry gain.
- Use `take_damage()` for meter loss.
- Add a HUD bar in `scenes/world.tscn` and update it from `scenes/world.gd`.
- Keep XP hidden/internal for run rewards; make special meter the main combat HUD.

Acceptance: sustained offense/parries earn Gravity Fist slam, damage visibly hurts meter, kiting drains meter, specials cannot be spammed at neutral.

## Phase 3: Grabs

Minimal grab contract:

- Enter grab on close-range forward tap/hold against a non-prone, non-attacking, non-boss enemy.
- Short clinch lock state for both player and enemy.
- Options: strike throw, directional throw into enemy/container, meter grab special.
- Enemy grab immunity during active attack, prone standup, or armored state.

Implementation anchors:

- Add `is_grabbable()`, `begin_grabbed_by(player)`, `release_grabbed()` to `ai_controller.gd`.
- Add `_grab_state`, `_grab_target`, `_start_grab_attempt()`, `_finish_grab_throw()` to player.
- Reuse knockback collision/impact code for throw payoffs.

Acceptance: grab does not break radial AI, grabbed enemy cannot attack/flee, throws produce readable impact.

## Phase 4: Enemy Variety And Radial Pressure

Keep `AIConductor` as the pressure brain. Add archetypes through data and scene variants before separate controllers.

Slice roster:

- Grunt: current SecurityTitan behavior.
- Bruiser: slower, armored startup, high knockback, grab-resistant.
- Harrier: circles wider radial slots, darts in with long cooldown, low health.
- Shield/Guard: blocks frontal standard hits, vulnerable to parry, grab, backfist, or guard-break kick.
- Optional Launcher/Stomper: creates prone/stomp opportunities.

Improvements:

- Add `enemy_archetype` export or data field.
- Add conductor limits per archetype.
- Replace pure respawn timer with wave budget and encounter cards.
- Preserve one active attacker or very small attacker count; readability beats crowd spam.

Acceptance: player can identify at least three enemy behaviors in a 3-minute slice, radial slots avoid pileups, parry/block has meaningful threats.

## Phase 5: Simple Scrolling Roguelike Level Generation

- Segment-based side-scroller: 20-35 meter chunks along X.
- Segment scenes: straight walkway, container choke, open arena, hazard lane, supply/shop alcove, miniboss gate.
- Each segment declares spawn anchors, obstacle anchors, camera lock bounds, and exit trigger.
- Run director picks weighted segment cards and increases pressure over time.
- Use existing container/walkway assets first; DALL-E for non-character texture variants; Meshy for new props/enemies.

Implementation anchors:

- Create `data/level_segments/*.json` or `.tres` resources.
- Create `scenes/level_segment_*.tscn` chunks.
- Add `LevelDirector` under `world.tscn`.
- Move spawning decisions from raw timer to segment/wave events while keeping `AIConductor` for local combat behavior.

Acceptance: player scrolls through at least 5 segments, camera gates fights and releases after clear, obstacles do not break nav/staging.

## Phase 6: Visual Polish And Blur

Priorities:

- Tune outline shader for strong silhouettes.
- Hit flashes on hit, block, parry, armor.
- Motion streaks/ghosts for Superman punch and Gravity Fist slam.
- Fix current `world.gd` slow/freeze constants; `_SLOW_FREEZE_DURATION` is currently `42`, which reads as seconds in comments and is dangerous for live hitstop.
- Add deterministic shake presets per hit class.
- Use selective special-only blur, not full-time blur.
- Replace giant debug-like labels with compact health/meter/combo HUD.
- Add parry clang, meter full sting, slam impact, and layered hit SFX.

Web constraints:

- Godot 4 web export targets WebGL 2 / Compatibility renderer. Budget expensive post-processing, dynamic lights, and particles.
- Test shaders/effects in browser early.

Asset pipeline:

- Meshy AI: character/enemy 3D models, textures, rigs, enemy variants.
- DALL-E: non-character texture sheets, signage, ground decals, container/walkway variants, UI backing textures.
- Track generated asset provenance and keep `.import`/`.uid` sidecars with assets.

Acceptance: Superman punch, parry, grab throw, and Gravity Fist slam read clearly from screenshots; web build holds frame pacing in a 5-enemy fight.

## Phase 7: Networked Play

Defer until single-player vertical slice is stable. First target should be two-player co-op, server-authoritative enough that clients cannot award damage, XP, meter, or wave clears.

Options:

1. W4 Cloud matchmaker/dedicated servers: best fit if Godot-native low maintenance matters most. Current docs describe lobby/matchmaking, WebRTC signaling, and automatic dedicated server allocation. Risk: platform dependency and pricing/availability need live check before commitment.
2. Godot dedicated server on a small managed host: portable and controllable. Export Linux dedicated server, run headless, strip visuals. More ops work.
3. WebRTC peer-to-peer with signaling: lowest server cost but weaker security unless a trusted authority exists. Fine for prototype co-op, not secure progression.
4. WebSocket client/server: browser-compatible and simple for lobby/chat/low-frequency state, but TCP is not ideal for fast action.

Recommended path:

- Phase 7a: local two-client multiplayer prototype with a server authority abstraction.
- Phase 7b: choose W4 Cloud if low maintenance beats portability; choose hosted dedicated server if control beats convenience.
- Phase 7c: add authentication only after persistence matters. Early co-op can use short-lived lobby tokens.

Security rules:

- Client sends input intentions, not damage results.
- Server owns enemy AI, hit resolution, special meter, health, pickups, wave progression, and rewards.
- Client prediction may smooth player movement, but server reconciles.
- Never trust browser client state for unlocks or score.

## Suggested First Implementation Slice

1. Fix validation/web export path.
2. Add `PROJECT_ORIENTATION.md` to Gravity Fist.
3. Add combat meter with hit/parry gain, damage/inactivity decay, and HUD.
4. Add one meter spend: Gravity Fist slam.
5. Remove normal jump input from live play.
6. Convert current contextual finishers into meter/context specials in data.
7. Add one enemy archetype by variant data, not new controller.
8. Add one scrolling segment director with 3 segment types.
9. Browser smoke test.

## External Docs Checked

- Godot 4.5 Web export docs: `https://docs.godotengine.org/en/4.5/getting_started/workflow/export/exporting_for_web.html`
- Godot WebSocket docs: `https://docs.godotengine.org/en/latest/tutorials/networking/websocket.html`
- Godot WebRTC docs: `https://docs.godotengine.org/en/4.5/tutorials/networking/webrtc.html`
- Godot dedicated server docs: `https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_dedicated_servers.html`
- W4 Cloud matchmaker docs: `https://docs.w4.gd/getting_started/matchmaker/index.html`
