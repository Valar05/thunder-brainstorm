# Ruined Air Full-Rig Walk Pattern For Infinite Brutality

## Purpose

Capture the implementation-relevant pattern from Ruined Air's canonical full-body player rig after importing it into the standalone Pose Lab. This is intended for a later Infinite Brutality implementation pass, not as a direct runtime copy.

## Imported Pose Lab Asset

Pose Lab now has a `Ruined Air` actor preset backed by `pose-lab/assets/models/ruined_air/Scavenger_new.fbx`. The source scene reference is preserved under `pose-lab/assets/source/ruined_air/scenes/Player.tscn`, with `player.gd`, `PlayerBoneHandler.gd`, and `foot_ik_root.gd` copied beside it for provenance.

A Three.js FBXLoader inventory of `Scavenger_new.fbx` found 9 embedded clips: `Armature|Idle`, `Armature|Swing1`, `Armature|Swing2`, `Armature|Swing3`, `Armature|Swing4`, `Armature|Swing5`, `Armature|Stab`, `Armature|0TPose`, and `Camera|Idle`. It found two skinned meshes, `char1` and `input`, and a full body skeleton with duplicated FBX bone nodes including hips, legs, spine, head, shoulders, arms, and hands.

The separate locomotion FBXs load as own clips with embedded names:

- `Animation_Walking_withSkin.fbx` -> `Armature|Armature|walking_man|baselayer`
- `Animation_Walk_Backward_withSkin.fbx` -> `Armature|Armature|Walk_Backward|baselayer`
- `Animation_Idle_Step_Turn_Left_withSkin.fbx` -> `Armature|Armature|Idle_Step_Turn_Left|baselayer`
- `Animation_Idle_Turn_Right_withSkin.fbx` -> `Armature|Armature|Idle_Turn_Right|baselayer`

## Pattern Extracted

Ruined Air does not rely on a baked walk clip alone. The reusable pattern is a layered full-body controller:

1. The visible character is `Scavenger_new.fbx`, not the hidden legacy `Character_output.fbx`. `Player.tscn` binds `PlayerBoneHandler.gd` directly to the visible `Model` instance.
2. The full-body model owns the camera and head attachments, while a chest bone pose override applies look pitch/yaw on `Spine02`.
3. Body yaw chases flat camera forward every frame, then chest yaw is countered so camera view does not snap; while moving, the leftover chest yaw bleeds back into body yaw.
4. Hip bob and cadence are computed from actual horizontal velocity. Cadence lerps between min/max values, step length scales from velocity, and landing boosts temporarily amplify downward bob.
5. Foot IK targets are external Node3D targets under `FootIKRoot`, not baked into the skinned mesh. `foot_ik_root.gd` moves those targets to scene root and keeps only their yaw aligned with the player.
6. Grounded stride alternates left and right phases by half a cycle. Each foot moves during phase windows `< 0.25` and `>= 0.75`, and remains planted through the middle of the cycle.
7. Strafe motion shortens stride distance and adds lateral target offsets, preventing side movement from looking like a full forward step.
8. Midair state lerps feet toward lifted rest targets and resets planted phases, so jump/glide transitions do not preserve stale floor plants.
9. Foot twist compensation exists but is separate from stride target placement; it rotates foot bone poses against body yaw overflow and eases them back to rest.

## Infinite Brutality Implementation Direction

For Infinite Brutality, this argues for a full-rig actor pipeline with separate responsibilities:

- Keep controller-owned world translation and collision authoritative, as Infinite Brutality already does for traversal.
- Treat authored clips as silhouette and combat sources: idle, sabre swing/stab, and optional native walk/back/turn clips.
- Add a runtime procedural locomotion overlay that drives hip bob, chest/camera yaw offset, and foot target placement from the existing player velocity and input vector.
- Do not bake Ruined Air root motion directly into Infinite Brutality movement. Strip or ignore horizontal root translation for traversal clips, preserving vertical/limb motion where it improves silhouette.
- Port the walk as a Three.js rig-controller concept: cache bones by semantic names (`Hips`, `Spine02`, `LeftFoot`, `RightFoot`, leg chains), create left/right foot target objects in world space, and solve/approximate IK or pose overrides each frame.
- Before runtime adoption, fix or consciously handle the Ruined Air source drift where `player.gd` can request `Armature|Swing0`, but the parsed Scavenger FBX exposes `Swing1..Swing5` plus `Stab`.

## Source References

- `ruined_air/scenes/Player.tscn:3-12` identifies the player script, legacy and visible model FBXs, `foot_ik_root.gd`, `PlayerBoneHandler.gd`, glider, and SteamSaber material.
- `ruined_air/scenes/Player.tscn:171-177` shows visible `Model` is `Scavenger_new.fbx` with `PlayerBoneHandler.gd` and tuned cadence/step settings.
- `ruined_air/scenes/Player.tscn:410-413` shows the legacy `AnimationTree` still points at hidden `Model_old`, a migration caveat.
- `ruined_air/models/PlayerBoneHandler.gd:79-105` binds camera, glider, skeleton, chest, hips, feet, SkeletonIK3D roots, and external foot IK targets.
- `ruined_air/models/PlayerBoneHandler.gd:117-150` applies camera look deltas to chest pitch/yaw, body-yaw chase, yaw bleed, and chest bone pose.
- `ruined_air/models/PlayerBoneHandler.gd:258-285` computes velocity-smoothed cadence, step length, hip bob, and landing bob boost.
- `ruined_air/models/PlayerBoneHandler.gd:288-355` separates midair foot reset from grounded alternating planted-foot stride phases.
- `ruined_air/models/PlayerBoneHandler.gd:357-401` computes stride targets from rest positions, input direction, strafe strength, lift phase, and lateral offset.
- `ruined_air/models/PlayerBoneHandler.gd:405-448` records the foot twist compensation layer.
- `ruined_air/scenes/foot_ik_root.gd:4-16` makes foot targets scene-rooted and yaw-aligned to the player.
- `ruined_air/scripts/player.gd:102-106` binds camera and AnimationPlayer to the visible `Model` and starts `Armature|Idle`.
- `ruined_air/scripts/player.gd:332-334` cycles sabre attacks through `Armature|SwingN`, with a detected clip-name caveat around `Swing0`.
