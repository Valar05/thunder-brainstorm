# FPS Platformer Arcane IK Brainstorm

Date: 2026-06-07

## Source Signals

- First-person weapon/arm animation source: `/storage/emulated/0/Download/models/FPSPlayer.blend` copied from `C:\Users\dclar\Downloads\FPSPlayer.blend` on THECAULDRON.
- Additional compact Blender sources: `/storage/emulated/0/Download/models/`, with source mapping in `cauldron_blend_manifest.tsv`.
- Arcane Manifold source: `ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold`.
- Arcane IK files inspected: `models/PlayerBoneHandler.gd`, `scenes/foot_ik_root.gd`, `scripts/player.gd`, `scripts/world_generator.gd`.
- Three.js reference target: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs`, especially its pose lab, rig profiles, Android capture tooling, and mobile-first fullscreen runtime.

## Core Pitch

Build a landscape-first, phone-first Three.js action platformer where first-person arms carry the weapon fantasy and a procedural lower-body model carries physical feel: foot planting, slope contact, landing compression, jump recovery, wall/ledge readability, and camera/body separation.

The player does not need to see full legs constantly. The leg IK matters because it makes the camera, shadow, body collider, weapon sway, and landing cadence feel connected to ground. Arms sell combat. Legs sell platforming trust.

## Arcane IK Pattern To Port

Do not port Godot nodes literally. Port these behaviors into a Three.js character controller layer:

- independent left/right foot target state
- velocity-scaled cadence and stride length
- planted phases where one foot stays fixed while the other swings
- midair foot reset toward rest offsets
- landing bob boost after floor reacquisition
- body yaw chase with chest/camera counter-yaw so turning does not snap view
- shoulder roll/turn cues from movement and look input
- foot twist compensation while turning in place
- separate visual skeleton state from collision/controller state

Arcane's `scenes/foot_ik_root.gd` keeps the foot target root yaw-aligned to the player after reparenting to the scene root. That maps cleanly to a Three.js `FootIKRig` object outside the skinned mesh that follows player position/yaw and owns target helpers.

## Improvements For Three.js

1. Replace phase-only foot targets with terrain-aware raycasts.
   Raycast from each candidate target down onto the landscape collision mesh. Store hit point, normal, and confidence. Use foot lock only when confidence is high.

2. Add slope-normal ankle alignment.
   Rotate foot bones toward the hit normal with a clamp, and keep toe direction aligned to body yaw or move vector. This avoids feet cutting through ramps and stairs.

3. Add coyote-time foot memory.
   When leaving ground, preserve the last two planted points briefly so camera bob and shadow do not pop at ledge edges.

4. Keep platformer verbs authoritative.
   Jump, dash, wall-kick, mantle, slide, and stomp should drive IK state. IK follows gameplay state; it never decides collision truth.

5. Use arms as the primary animation layer.
   FPSPlayer weapon clips should drive hands, weapon, recoil, reload, inspect, swap, and melee. Lower-body IK should only influence camera bob, body shadow, landing feel, and rare visible legs/shadow shots.

6. Build an import lab first.
   Before runtime wiring, create a Three.js lab page that loads `FPSPlayer.blend` exports, lists arm clips, previews weapon families, and reports bone names. The lab should output a JSON rig profile for runtime.

## Phone Landscape Control Sketch

- Left thumb: floating movement stick, with analog walk/run magnitude.
- Right thumb drag: camera look.
- Right tap: fire/primary action.
- Right hold: aim/charge/alt fire depending on weapon.
- Swipe up/right-side: jump or mantle assist when context is present.
- Swipe down/right-side: slide/drop/stomp depending on state.
- Two-finger tap or small top button: weapon swap.
- Optional gyro assist: subtle aim smoothing only, never required.

Controls should be forgiving on a landscape phone. Keep buttons sparse and let gestures become context verbs around the camera thumb zone.

## Runtime Architecture

- `PlayerMotor`: fixed-step capsule movement, slopes, coyote time, jump buffering, wall checks, platform contacts.
- `TouchInput`: landscape touch zones, gesture resolver, input buffering.
- `FirstPersonRig`: camera, arms, weapon sockets, recoil, weapon animation mixer.
- `FootIKRig`: procedural gait state, raycast target selection, foot locks, slope alignment, landing compression.
- `WorldRuntime`: streamed landscape chunks, collision mesh, material zones, navigation hints.
- `WeaponRuntime`: weapon profiles mapping inputs to FPSPlayer arm clips and projectile/melee behavior.
- `PoseImportLab`: asset inspection, clip aliasing, rig profile export, visual capture hooks.

## First Prototype Slice

1. Export `FPSPlayer.blend` to GLB with all arm clips preserved.
2. Create a new Three.js project or branch using the Gravity Fist Three.js tooling style: fullscreen canvas, import map or Vite-lite setup, Android capture hooks, deterministic build script.
3. Build a greybox outdoor landscape: ramps, ledges, one wall-kick lane, one moving platform, one drop/stomp line.
4. Implement touch movement/look in landscape before desktop polish.
5. Load arms and weapon clips in a pose/import lab; define clip aliases for pistol/rifle/melee/reload/swap.
6. Implement motor plus camera bob without IK.
7. Add Arcane-style foot cadence and landing compression as data, then upgrade to terrain raycast foot targets.
8. Add one enemy or target dummy only after traversal and weapon feel are readable.

## Risks

- Blender `.blend` may need desktop Blender export to GLB; Termux may not have Blender available.
- FPS arms may be authored for a specific camera/weapon alignment, so clip aliases and sockets must be inspected visually before assuming runtime names.
- Full-body IK in Three.js can become expensive or unstable on mobile; start with procedural target helpers and minimal bone overrides, then add a lightweight IK solver only where visible.
- Landscape collision must be simple. Rendered terrain can be rich, but mobile physics should use low-poly proxy collision.

## Suggested Next Action

Create a small project packet before coding: asset export requirements, Arcane IK behavior map, control contract, and a one-screen first prototype spec. Then build the import lab and motor as the first real slice.
