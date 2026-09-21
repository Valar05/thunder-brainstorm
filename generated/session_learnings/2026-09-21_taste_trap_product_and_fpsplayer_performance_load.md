# Taste Trap — Product Breakout + FPSPlayer Performance Donor — 2026-09-21

## Status

ACTIVE PRODUCT / ASSET ARCHAEOLOGY

## Product boundary

Taste Trap is a portable modular package family, not merely one game.

Target adapters:
- Unity
- Unreal
- Three.js
- additional adapters later

Free core must remain genuinely shippable. Paid modules sell authored excellence and new relationships with the world.

Current paid-module candidates:
- biome grammars
- Boxcraft / structure packs
- enemy/ecology packs
- advanced traversal
- VFX/effect families
- Ruined Air flight/glider module
- other cathedral organs

Pocket law:

> THE WORLD IS THE SHOWROOM. SELL THE ORGANS.

## Open-world showroom

The current Taste Trap showroom direction is a generated open world without checklist filler.

The world should produce intentions from geography rather than icon chores.

A biome is a parameter packet that changes topology, sightlines, traversal, risk, settlement, and combat affordances.

Current firsthand retrieval anchors:
- Fjord
- Desert
- lost water-propagation failure
- broader old biome family not yet source-recovered

Mars is a strong flagship family because canyon, crater, volcanic, dune, polar, channel, and basin grammars can share one coherent world model.

## Ruined Air is the first clear premium traversal organ

Repo: `Valar05/ruined-air`

Source-backed behavior from `scripts/player.gd`:
- mass
- wing area
- air density
- lift coefficient
- angle-of-attack response
- maximum lift
- parasitic drag
- induced drag
- trim angle
- stall angle
- max speed
- camera-relative 3D steering
- optional thrust
- heat / overheat / recovery

The player computes dynamic pressure, lift, drag, gravity, steering and thrust.

`models/PlayerBoneHandler.gd` scales the glider open/closed and rolls it with steering.

Commercial law:

> PREMIUM SHOULD CREATE A NEW RELATIONSHIP WITH THE WORLD, NOT MERELY ADD MORE CONTENT TO THE SAME VERB.

## FPSPlayer donor recovery

Drew uploaded `FPSPlayer (1).blend`.

The raw source is archived in Drive:

`Singularity Engine / Taste Trap / Donor Assets / FPSPlayer_source_2024-10.blend`

Runtime GLB reference archived beside it:

`FPSPlayer_runtime_reference.glb`

### Blend source observations

Container binary inspection:
- Blender source version: 4.04
- lineage string: `FPSPlayer.fbx`
- `Armature`, `Arms`, `Arms.001`
- `Player` material
- `PlayerTexture` image reference
- old material path under `thedarkbelow/Assets/Models/Materials/PlayerTexture.png`
- authored actions include Climbing, ClimbingSide, Mantle, FistAttack, OneHandAttack and others

Important conclusion:

> THE MESH IS NOT THE FLESH.

The form, rig, weights, UVs and animation library are separable from the surface fiction.

### Runtime GLB exact stats

Source: recovered `FPSPlayer.glb`, 2,337,180 bytes.

- 3 meshes
- arm meshes: 963 vertices, 1,306 triangles
- placeholder weapon: 80 vertices, 38 triangles
- total: 1,043 vertices, 1,344 triangles
- 1 skin
- 45 joints
- 55 animations
- ~52.7 seconds total clip duration
- 1 material
- 0 embedded textures/images

The visible first-person body is therefore only about 1.3k triangles.

That is extremely light by contemporary standards.

## Performance implication

A single ~1.3k-triangle skinned first-person rig should be a negligible geometry load on modern hardware.

Large high-resolution sprite-sheet libraries can exceed this asset's memory footprint very quickly.

Reference:
- uncompressed 2048x2048 RGBA8 = ~16 MiB
- uncompressed 4096x4096 RGBA8 = ~64 MiB

This is not a universal proof that 3D beats 2D. Actual performance still depends on:
- texture compression
- atlas residency
- overdraw/transparency
- batching
- shader cost
- skinning path
- active animation count

But current evidence strongly supports:

> FPSPLAYER IS NOT THE PERFORMANCE PROBLEM.

Thirdskin Commander can radically reduce texture pressure with true low-resolution pixel art, aggressive atlas packing, compression, and sparse-key/deformation reuse. Without that, its sprite-sheet approach may use substantially more texture memory/bandwidth than FPSPlayer.

## Mars arm material direction

Do not repaint flesh.

Keep the mesh/rig and replace the material fiction.

First witnesses:
1. Legacy Flesh control
2. Mars EVA pressure/combat suit
3. Synthetic myomer / pseudo-muscle

Procedural material partitions:
- glove
- forearm reinforcement
- fabric/undersuit
- seals
- joints
- armor/composite
- abrasion
- dust accumulation
- optional emissive/utility marks

The old Blender source references an external PlayerTexture rather than forcing an embedded flesh texture, so procedural re-materialization is a natural route.

## Pose Lab lineage

`Valar05/pose-lab-v2` directly references:

`../pose-lab/assets/models/FPSPlayer.glb`

for pose extraction, candidate baking and fist/one-hand review.

Modern `Valar05/infinite-brutality` also identifies FPSPlayer as copied from Pose Lab for first-person arm/animation runtime use.

Therefore FPSPlayer is already a proven reusable donor, not merely nostalgic baggage.

## Durable laws

> THE MESH IS NOT THE FLESH.

> THE WORLD IS THE SHOWROOM.

> SELL NEW RELATIONSHIPS WITH THE WORLD.

> KEEP THE CHEAP RIG. SPEND TASTE ON THE SURFACE.


## Grounding lock — 2026-09-21

Drew correction: Taste Trap should be fairly grounded in recognizable near-future reality.

Aerospace / Mars industrial language can clearly evoke contemporary private-spaceflight engineering culture, but should remain an original fictional identity rather than literally using or copying SpaceX.

Default visual/world constraints:
- practical pressure suits;
- believable aerospace hardware;
- recognizable current-to-near-future engineering lineage;
- restrained stylization;
- equipment should look plausibly manufacturable.

Explicit exclusion:
- no Fleshpunk crossover by default;
- no living machinery, tendon cables, flesh armor, organic guns, or biological-industrial horror language.

FPSPlayer material correction:
- keep Legacy Flesh only as a control/reference;
- primary Mars witness = EVA/combat pressure suit;
- secondary witness = alternate grounded technical suit;
- remove synthetic-myomer as the leading Taste Trap direction.

Pocket law:

> TASTE TRAP IS GROUNDED NEAR-FUTURE, NOT FLESHPUNK.
