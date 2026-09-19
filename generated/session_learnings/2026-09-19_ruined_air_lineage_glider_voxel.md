# Ruined Air — Body Presence, Floating Voxel Islands, and Hardcore Glider Transmission — 2026-09-19

## Repository identity

The active source repository is:

- https://github.com/Valar05/ruined-air
- default branch: `master`
- Godot project name: `Ruined_Air`

A second repository also exists:

- https://github.com/Valar05/ruined_air

but that underscore repository is currently empty. Do not mistake it for the source-bearing game.

## Firsthand lineage correction

Drew identifies Ruined Air as the successor to the still-unnamed asteroid prototype discussed in the 2026-09-19 archaeology pass.

The predecessor's distinctive world idea was:

> **put rooms inside a sphere**

Ruined Air inherited that spatial imagination, but mutated it outward:
- the enclosing sphere stopped being the world body;
- rooms / traversable nodes became **floating rock masses**;
- the player moved through open air between them;
- Arcane Manifold's embodied first-person player presence was carried forward into that new terrain model.

Preserve the predecessor as an unresolved-but-real lineage node:

`UNNAMED_ASTEROID_SPHERE_ROOMS`

The exact repository remains open archaeology.

## Arcane Manifold → Ruined Air body-presence transmission

This edge is unusually strong because the surviving code rhymes at implementation level, not merely at the level of taste.

Arcane Manifold and Ruined Air both use:
- a `CharacterBody3D` player;
- the same basic walk / run / jump constants;
- DPad-driven mobile movement;
- camera attached to a **full-body rig head bone**;
- `PlayerBoneHandler.gd`;
- world-up/body-forward helper math such as `_project_on_plane`, `_basis_from_up_forward`, and quaternion/basis body alignment;
- procedural full-body locomotion rather than a detached floating camera.

Arcane Manifold's `Player.tscn` uses `Forgeborn.glb` as the visible body, with:
- head-bone camera attachment;
- external foot IK targets;
- left/right `SkeletonIK3D`;
- chest/body bone handling.

Ruined Air's `Player.tscn` uses `Scavenger_new.fbx` with the same broad body architecture:
- head-mounted camera;
- full skeleton;
- external foot IK;
- `PlayerBoneHandler.gd`;
- body-facing and chest-yaw compensation.

The transmission is therefore better described as:

> **BODY PRESENCE BECAME INFRASTRUCTURE.**

The camera is not a ghost floating through the level. It lives inside a body whose hips, feet, chest, head, cadence, landing, strafe, and turning all remain part of the player's perceptual loop.

## Ruined Air's locomotion body

Existing Thunder continuity already extracted the full-rig walking pattern from Ruined Air. The key source-backed pieces are:
- body yaw chases camera-forward;
- chest yaw counters camera snapping and bleeds back into body yaw while moving;
- hip bob derives from actual horizontal velocity;
- cadence scales with velocity;
- landing adds temporary downward bob;
- external world-space foot targets support IK;
- planted-foot phases alternate through the gait cycle;
- strafing shortens stride and adds lateral offset;
- midair state resets stale planted feet.

This note does not replace that implementation note. It places that body system in the project lineage.

## Floating-rock world generation

Ruined Air's current `scenes/Main.tscn` is not hand-placed scenery around a glider.

It boots a real voxel world stack:
- `scripts/world_generator.gd`;
- `scripts/voxel_chunk.gd`;
- a triplanar rock material;
- chunked world generation.

The world generator explicitly calls its major masses **island blobs (inverted cones)**.

It builds:
- multiple separated room/island centers;
- noisy plateau tops;
- tapered floating masses;
- procedural bridge solids between selected islands;
- additional smaller rock fields;
- a minimum-spanning-tree graph plus extra graph edges.

The density field is then polygonized by the voxel chunk runtime using **Marching Cubes**, density-gradient normals, and generated collision.

That makes the floating rocks a gameplay substrate, not background decoration.

The structural mutation from the predecessor can be preserved as:

```text
unnamed asteroid prototype
rooms inside a sphere
        ↓
Ruined Air
rooms / graph centers become floating voxel islands
bridges become world-space traversal connections
        ↓
modern Infinite Brutality
floating rock / fortress / district terrain grammar
```

The first arrow is Drew's firsthand lineage report.
The Ruined Air middle is source-backed.
The modern Infinite Brutality relationship is a design/capability transmission, not a claim that the Godot voxel code was copied verbatim into Three.js.

## The glider is not decorative

Drew explicitly corrected any interpretation of the glider as a cosmetic traversal gimmick.

The source fully supports that correction.

Ruined Air's `scripts/player.gd` implements a real aerodynamic flight model with parameters for:
- mass;
- wing area;
- air density;
- base lift coefficient;
- lift slope versus angle of attack;
- maximum lift coefficient;
- parasitic drag;
- induced drag;
- trim angle;
- stall-angle clamp;
- maximum speed.

Each physics step while gliding computes:
1. airspeed and normalized flight direction;
2. body pitch relative to horizontal;
3. flight-path angle;
4. angle of attack = body angle - flight-path angle + trim;
5. stall-clamped lift coefficient;
6. drag coefficient including induced drag;
7. dynamic pressure `q = 0.5 * rho * v^2`;
8. lift force;
9. drag force;
10. acceleration from lift + drag + gravity.

The glider then layers a jet/boost system on top:
- camera-relative thrust vector;
- heat accumulation;
- overheat lockout;
- cool-down / resume threshold;
- separate boost and glide steering rates;
- 3D velocity-direction steering;
- quadratic high-speed stabilization;
- speed cap.

This is not CFD, but it is absolutely a **model-based flight mechanic**, not an animation attached to falling.

Pocket law:

> **IF THE BODY CHANGES MODE, THE PHYSICS SHOULD CHANGE WITH IT.**

The glider changes the player's actual equations of motion.

## Video confirmation — 2026-09-19

A user-supplied 24.3-second screen recording visually confirms the surviving design:
- visible first-person body / hands;
- a deployed wing / glider above the view;
- large floating rock masses and fragmented traversal geometry;
- traversal through open air among those rocks;
- dedicated glide/boost-style control icons.

The video and source agree on what the mechanic is doing.

## Ruined Air → modern Infinite Brutality

The transmission into modern `Valar05/infinite-brutality` is already partially documented by the current project itself.

Modern Infinite Brutality's Thunder links explicitly reference the Ruined Air full-rig walk pattern as a precursor.

The modern game also carries forward two larger Ruined Air ideas:

### 1. Embodied first-person presence
Ruined Air proves the full-body version:
- head camera;
- procedural body yaw;
- foot IK;
- locomotion body.

Modern Infinite Brutality currently renders first-person arms separately for readability, but its player language still treats traversal and combat as embodied motion rather than a disembodied cursor.

### 2. Floating terrain as gameplay
Ruined Air's world is a navigable graph of generated floating rock masses.

Modern Infinite Brutality later develops:
- floating geological fragments;
- carved voxel / fortress terrain;
- district terrain grammar;
- route-bearing rock/architecture fusion.

The engine and implementation changed, but the spatial ambition survived.

This is another strong specimen of the lineage law already recovered elsewhere:

> **THE PROJECT DIES. THE CAPABILITY MIGRATES.**

## Updated lineage chain

```text
UNNAMED ASTEROID GAME
rooms inside a sphere
        ↓
RUINED AIR
Arcane Manifold body presence
+ full-body procedural locomotion
+ floating voxel islands / bridges
+ real aerodynamic glider
        ↓
MODERN INFINITE BRUTALITY
embodied traversal
+ floating / carved terrain grammar
+ reusable Ruined Air locomotion lessons
        ↓
TASTE TRAP
```

## Retrieval handles

- Ruined Air;
- ruined-air;
- empty ruined_air repo;
- asteroid sphere rooms;
- rooms inside a sphere;
- Arcane Manifold body presence;
- Scavenger full rig;
- PlayerBoneHandler;
- floating rocks;
- inverted cone islands;
- Marching Cubes;
- MST bridges;
- glider aerodynamics;
- angle of attack;
- induced drag;
- stall clamp;
- boost heat;
- the glider is not decorative;
- ancestor of modern Infinite Brutality.
