# Vanguard Blend Excavation — 2026-09-14

## Source identity

- Source upload: `Vanguard (1).blend`
- Embedded source path: `C:\Users\dclar\OneDrive\Documents\Vanguard.blend`
- SHA-256: `5a94e77f78d6c887cc87517d0f8020ca19edc1a12c68dd8cecf17d6368ac38b7`
- Size: 10,454,904 bytes
- Blender header: 2.80, 64-bit little-endian
- The file also contains historical strings referring to `C:\Users\dclar\Modern Paladin\ArtSources\Vanguard.blend\Object\`.

## This is actual Vanguard source lineage

The source contains exactly three non-Rigify-widget objects:

```text
Body
Long_Sword
rig
```

This object contract matches the Vanguard import lane already preserved in Pose Lab V2. The uploaded file has 19 surviving `bAction` datablocks, while the Pose Lab sibling source/runtime manifest records 20 and includes `SwordAttack3` as the additional clip. For the 19 shared actions, fcurve counts match the Pose Lab manifest exactly. Treat the upload as a closely related Vanguard source revision, not as byte-identical proof of the current imported copy.

## Geometry budget

The actual authored visible model is tiny.

### Body

- 1,032 vertices
- 1,923 edges
- 910 polygons
- 3,626 loops
- 884 quads
- 20 triangles
- 6 five-sided polygons
- every Body polygon is stored flat-shaded in this revision
- one Armature modifier; no subdivision or Edge Split modifier

### Long sword

- 321 vertices
- 605 edges
- 288 polygons
- 1,154 loops
- 280 quads, 4 triangles, 2 pentagons, 2 hexagons
- smooth-shaded face flags
- one `Basis` shape key only; no actual morph target survives
- effectively every sword vertex is weighted to `Weapon.R`

### Total visible authored budget

```text
1,353 vertices
1,198 polygons
```

That is dramatically below Lionheart while still carrying a strongly specific character identity.

## Proportion and weapon scale

Body local bounds are approximately:

```text
width: 1.529
thickness: 0.646
height: 2.054 Blender units
```

Sword local bounds are approximately:

```text
crossguard width: 0.303
length: 1.514
thickness: 0.050
```

The sword is therefore about 74% of full character height in this source. It reads as a real long weapon rather than a generic hand prop.

The sword itself separates cleanly into five connected components: broad guard, long blade, grip, pommel, and a tiny joining piece. The blade component alone runs about 1.17 Blender units.

## Silhouette construction

The Body mesh is 22 disconnected geometric components rather than one continuous sculpt.

Largest components:

- central torso / pelvis / legs: 367 vertices / 362 faces;
- left arm assembly: 173 vertices / 166 faces;
- right arm assembly: 173 vertices / 166 faces;
- head / helmet mass: 49 vertices;
- neck / upper chest plate mass: 24 vertices.

This makes the character closer to a deliberately assembled low-poly armored figure than a skinned smooth body with detail carved onto it.

### The asymmetric pauldron is structural

Three detached components on one shoulder contain 30 + 12 + 12 vertices and are weighted entirely to the custom `Pauldron.R` control.

The rig also contains:

```text
Pauldron.helper.R
Pauldron.R
```

There is no symmetric `Pauldron.L` counterpart in the same custom-control role.

So Vanguard's shoulder asymmetry is not just a paint decision. It is a separately rigged silhouette system.

### The plume / hair is made from repeated blades

Ten separate 15-vertex components sit behind / above the head and are weighted completely to `ORG-head`, plus additional 18- and 22-vertex head components.

The source therefore builds the crest as repeated low-poly blade / feather strips rather than a continuous hair mass.

That is a highly efficient identity device: very little geometry creates a large, unmistakable directional silhouette.

## Rig sophistication vs mesh simplicity

The actual armature contains roughly 437 bones because it is a full Rigify-style control / mechanism / deformation hierarchy around an extremely small authored mesh.

Notable custom functional bones include:

```text
root
Weapon.L
Weapon.R
Pauldron.helper.R
Pauldron.R
BackSheath
HipSheath
```

The Body object exposes 62 deformation groups, while the sword is effectively owned by `Weapon.R`.

This is a useful high-powered-low-poly asymmetry:

```text
very cheap visible geometry
+
highly expressive control rig
=
large motion / identity envelope
```

The model spends complexity on articulation and authored state, not on static vertex count.

## Material state in this exact upload

Two materials survive:

- `VanguardBody`
- `LowPolyProps`

`VanguardBody` has only `Material Output` and `Diffuse BSDF` nodes in this exact revision. The Body loop-color layer is effectively white. No authored albedo image datablock survives here besides Blender's `Render Result`.

This differs from the later Pose Lab sibling-source history, which records missing external albedo paths from a `Warrior Apocalypse` texture pipeline. Therefore this upload should not be used to infer the final palette. It is best treated as a geometry / rig / motion source revision.

## Action inventory

Nineteen `bAction` datablocks survive:

- `0T-Pose`
- `ClubIdle`
- `Idle`
- `Jump`
- `JumpCrouch`
- `JumpForward`
- `Land`
- `LedgeClimb`
- `LedgeGrab`
- `LedgeGrabHang`
- `Midair`
- `MidairSwordAttack1`
- `MidairSwordAttack2`
- `RunForwardOld`
- `SpinAttack`
- `SwordAttack1`
- `SwordAttack2`
- `SwordAttack4`
- `SwordAttack5`

This is not merely a character model. It is a compact action-platform / sword-combat body with authored traversal, aerial combat, ledge behavior, stance variants, and grounded attacks.

The Pose Lab sibling runtime adds `SwordAttack3` as the twentieth clip.

## Sword attacks are body travel, not arm gestures

The strongest motion finding is root travel.

`SwordAttack1` root-Y keys:

```text
0: 0.000
7: +0.153     # brief preload / retreat
8: -0.017
11: -0.559
14: -1.081
16: -1.308
20: -1.263
27: -1.202
38: -1.813
```

Given a body height of about 2.05 units, the action ends roughly 0.88 body-heights forward from its start.

Other measured root travel:

- `SwordAttack2`: about -0.775 final, with a +0.275 preload;
- `SpinAttack`: about -1.520 final;
- `SwordAttack4`: about -0.864 final, with a +0.283 preload;
- `SwordAttack5`: about -2.418 final, more than one body-height of travel;
- `RunForwardOld`: about -4.488 across 46 frames.

The attack grammar is therefore not stationary upper-body sword waving.

It is closer to:

```text
LOAD BACK
-> BODY CROSSES DISTANCE
-> BLADE ARRIVES WITH BODY
-> CONSEQUENCE PERSISTS INTO END STATE
```

That is a strong historical ancestor for later Vanguard doctrines about planted feet, body commitment, and weapon path.

## Timing compression

The grounded sword attacks use many rig channels but comparatively few semantic time positions.

Examples:

`SwordAttack1` unique keyed times:

```text
0, 7, 8, 9, 11, 13, 14, 15, 16, 20, 27, 38
```

`SwordAttack2`:

```text
0, 8, 9, 11, 12, 14, 15, 18, 24, 41
```

`SpinAttack`:

```text
0, 5, 12, 15, 16, 17, 18, 21, 27, 35, 39, 42, 48, 53
```

The dense information sits around the commitment / contact region and then opens into longer recovery spacing.

By contrast `RunForwardOld` is keyed nearly every two frames, and several jump / land actions contain much denser source traces. The file also contains many `McpQuat` channels, especially in traversal actions, so a MakeHuman / mocap-style retargeting tool clearly touched part of the animation pipeline. Exact authorship per clip remains UNKNOWN without Drew's production memory.

## HEMA provenance — correction to the earlier interpretation

USER_MEMORY from Drew materially changes the causal interpretation of the sword animation.

Vanguard's sword motion was not an action-game animation that accidentally converged on plausible body mechanics. Drew practiced HEMA with a small local group and integrated the animation directly with people from that group. The movement therefore belongs in the chain:

```text
HEMA PRACTICE / EMBODIED FEEDBACK
-> ANIMATION TRANSLATION
-> GAMEPLAY
```

The measured root travel should therefore be read first as martial measure / whole-body weapon action expressed in game animation, not merely as a game-design gap-closer. The sword, feet, hips, torso and hands participate in one committed action whose geometry changes distance.

Exact named-technique mapping for `SwordAttack1`–`SwordAttack5` remains UNKNOWN unless separately remembered or source-proven.

### Drew's bimodal sparring style

USER_MEMORY:

Drew describes the early HEMA group as small. Kenneth was the strongest fighter and teacher: multi-style, opponent-adaptive, and willing to dramatize an imperfect application so a student could physically feel why a technique worked. David was also highly competent and could nearly fight Kenneth to a draw, but Drew's own matchup with David behaved strangely because Drew's physical and tactical policy was extremely compressed.

David's remembered summary of Drew's repertoire was essentially two moves:

1. a heavily overcommitted Zornhau;
2. a very cautious, very long-range poke exploiting Drew's long reach.

Drew therefore describes his combat policy as **bimodal** rather than broadly adaptive.

The important structure is not simply `two moves`. The two modes are opposite risk regimes:

```text
MODE A — OVERCOMMIT
accept contact / collapse measure / impose mass and initiative

MODE B — DENY
preserve measure / exploit reach / force opponent to cross danger first
```

This creates an unusual opponent-model problem. A normal fighter often occupies intermediate commitment states. Drew's remembered style jumped between the extremes:

```text
VERY FAR / CAUTIOUS
<-------------------->
VERY COMMITTED / INSIDE
```

The middle was comparatively underused.

This helps explain why a technically stronger opponent could find the matchup disproportionately frustrating. It is a style-interaction effect, not evidence that Drew was the more skilled swordsman. Kenneth's defining advantage, by contrast, was adaptation across styles and opponents.

Candidate law:

> A narrow repertoire can still be difficult to solve when its few actions occupy sufficiently different regions of the opponent's decision space.

And a stronger formulation:

```text
REPERTOIRE WIDTH != DECISION-SPACE WIDTH
```

Two moves can create a large decision problem if one punishes entering and the other punishes staying out.

This also provides a plausible embodied root for Vanguard's contrast between long-range weapon geometry and violent full-body commitment, but that lineage remains INFERRED rather than source-proven.

## Current-canon continuity

Pose Lab V2's 2026 Vanguard preservation contract gives the current appearance authority to the accepted Fleshpunk idle frames and explicitly protects anatomy, proportions, armor coverage, plume / hair mass, face, and sword dimensions.

This old 3D source already contains several of those identity anchors:

- tall narrow armored body;
- hard planar / faceted construction;
- aggressively directional head plume;
- long sword as a major silhouette line;
- asymmetric shoulder architecture;
- full-body committed sword movement.

Do not claim pixel-level visual identity between this source and current Fleshpunk Vanguard. The valuable fact is structural continuity: several later protected identity features already exist as load-bearing geometry or motion here.

## Style extraction

### Silhouette grammar

```text
TALL NARROW CORE
+ ONE LOUD SHOULDER
+ BACKWARD BLADE-FEATHER CREST
+ LONG THIN SWORD VECTOR
```

The body is globally simple and symmetrical enough to read immediately, then a very small number of asymmetric / directional decisions make it specific.

### Shape language

- hard wedges and prismatic armor planes;
- narrow tapering lower legs;
- angular joint breaks rather than smooth anatomy;
- repeated blade strips for hair / plume;
- slim rectangular limb armor;
- sword built around one very long low-thickness blade plane.

### Detail economy

This may be the purest archaeology example yet of identity compression.

The model does not need Lionheart's heraldic density. It achieves specificity by spending very little geometry on a few extremely high-leverage visual mutations.

## Durable lessons

1. **Weirdness can be geometry-efficient.** A single asymmetric shoulder and a blade-feather crest can carry more memorability than thousands of generic detail polygons.
2. **Control complexity can substitute for mesh complexity.** Vanguard's visible body is tiny; the rig / action space is enormous by comparison.
3. **Weapon combat should move the body through space.** Several attacks literally translate the root by a large fraction of character height or more, now with USER_MEMORY that this motion was integrated against HEMA practice rather than discovered accidentally.
4. **Identity can survive technology changes when it is structural.** The plume, shoulder asymmetry, long weapon line and faceted proportions recur in later Vanguard preservation doctrine even as rendering style changes.
5. **Repertoire width is not decision-space width.** A bimodal policy can be strategically awkward when its two modes threaten opposite commitment regimes.

## Compact Thunder record

```text
slug: vanguard-source-280
mechanism: ultra-low-poly armored swordfighter whose identity is carried by asymmetry, plume, long weapon vector, and root-driven full-body attacks informed by HEMA practice (USER_MEMORY)
style: tall narrow faceted body; single loud pauldron; repeated blade-feather head crest; long thin sword; almost no decorative surface dependency
strongest lesson: spend identity on a few geometry/motion decisions strong enough to survive every later rendering pipeline
motion law: whole-body sword action changes measure; measured clips often preload briefly backward and then commit the body through the strike
sparring analogue: Drew remembers a bimodal personal policy — overcommitted Zornhau vs cautious extreme-range poke — creating wide decision-space coverage from a tiny repertoire
lineage: direct structural ancestor / sibling source for Pose Lab Vanguard; current Fleshpunk appearance remains separately authoritative
source: Vanguard (1).blend @ 5a94e77f78d6c887cc87517d0f8020ca19edc1a12c68dd8cecf17d6368ac38b7
```
