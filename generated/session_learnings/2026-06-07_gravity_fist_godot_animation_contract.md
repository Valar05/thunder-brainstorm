# Gravity Fist Godot Animation Contract - Session Learnings

Date: 2026-06-07

## Trigger

A new Android video (`/storage/emulated/0/Download/screen-recorder-unlimited-2026-06-07-09-09-32.mp4`) showed the Three.js port still had character alignment/readability problems: the stage sat low in the portrait viewport, enemy attack tells read like generic stepping/guarding, and enemies did not clearly face or step into the player during attacks.

## Concrete Animation Inventory

The durable source list now lives in:

```text
/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/docs/godot_animation_usage.md
```

Important source facts:

- Player state machine: `Jab`, `Cross`, `Block`, `Headbutt`, `LowBackKick`, `FrontKick`, `Backfist`, `SpinningHighKick`, `AxeKick`, `AxleKick`, `LeftHook`, `LeftUppercut`, `RightUppercut`, `SupermanPunch`, `CurbStomp`, `GravityFist`, `HitHeadLeft`, `HitHeadRightBig`, `Run`, and `Locomotion` with `Step*` blend animations.
- Player data-driven attacks come from `player_attacks.json`; standard chain is `Jab`, `Cross`, `LeftHook`, `LeftUppercut`, `RightUppercut`; specials include `Headbutt`, `SupermanPunch`, `LowBackKick`, `FrontKick`, `Backfist`, `SpinningHighKick`, `AxeKick`, and `AxleKick`.
- Security Titan state machine: `Jab`, `Cross`, `HitHeadLeft`, `HitHeadRight`, `BackImpact`, `KnockedBack`, `ProneBack`, `ProneBackDamage`, `ProneBackStandUp`, `ProneFront`, `ProneFrontDamage`, `StandUp`, `Death`, `Run`, and `Locomotion` with `Step*` blend animations.
- Security Titan attack data only names `Jab` and `Cross` in `security_titan.json`.

## Web Port Import Gap

`Ares.glb` contains the broad named animation set. `SecurityTitan.glb` only contains five clips: two unnamed `Armature.001|mixamo.com|Layer0*` clips, one `Armature|mixamo.com|Layer0`, `HitHeadLeft`, and `HitHeadRight`.

Therefore Security Titan parity in Three.js must retarget from Ares or hold native Titan frames. The current policy is:

- Native held idle and native locomotion remain in use because looping retargeted `Run`, `Idle`, and broad `Step*` clips still sample too horizontal/crouched.
- Titan attack tells now use Godot-named retargeted clips:
  - `Jab` -> `shared-retarget:Jab-Enemy` held at `0.7s`.
  - `Cross` -> `shared-retarget:Cross-Cross-Enemy` held at `0.35s`.

## Validation Artifacts

- New video frame sheet: `/data/data/com.termux/files/usr/tmp/video-critique/gravity-fist-2026-06-07-090932/contact.jpg`
- Pose strip JSON: `/data/data/com.termux/files/usr/tmp/gf_titan_pose_strip_after_attack_tells.json`
- Pose strip PNG: `/data/data/com.termux/files/usr/tmp/gf_titan_pose_strip_current.png`

Android browser capture could not rerun after this change because both `am` and `termux-open-url` returned success while the browser made zero local HTTP requests. This is the known capture handoff failure, not a runtime parse result.
