# Lionheart — High-Powered Low-Poly High-Water Mark — 2026-09-14

## Source identity

- Source: `Lionheart.blend`
- SHA-256: `31667dc375db5921aed13ce6afedbc4d7db5052e31181ec6574862f45ed0fa92`
- Size: 10,732,840 bytes
- Blender header: 2.80, 64-bit little-endian
- Historical path: `C:\Users\dclar\OneDrive\Documents\Lionheart.blend`
- Source contains an external action-path string pointing at `CrusaderInquisitor.blend\Action\Attack2_Alt`; treat exact animation ancestry as INFERRED until corroborated.
- Source directly references `//Allegorithmic\Substance Painter\export\Lionheart_Material_BaseColor.png`, making Substance Painter use SOURCE-VERIFIED for this specimen.

## User-memory status

USER_MEMORY from Drew:

- Lionheart is arguably his coolest-looking model.
- It was objectively / practically among the least-used models.
- It represents the high-water mark of his "high-powered low-poly" modeling phase.

The source strongly supports the high-powered low-poly description. "Coolest" remains an aesthetic judgment; "least used" remains production memory until project history corroborates it.

## Visible modeling budget

Excluding Rigify widget meshes, the visible authored geometry is approximately:

```text
4,484 vertices
4,308 polygons
```

Object allocation:

- `Body`: 1,749 verts / 1,473 polys
- `LionsFlail`: 1,266 verts / 1,296 polys
- `Shield`: 657 verts / 621 polys
- `Maille`: 333 verts / 349 polys
- `Cape`: 184 verts / 302 polys
- `LionsMace`: 153 verts / 119 polys
- `LeftArm`: 142 verts / 148 polys

This is a remarkably small budget for the amount of visible design information.

## Polygon allocation is semantic

The strongest style lesson is not simply "low poly." It is **where the polygons are spent**.

### Quiet mass

The cape covers a huge portion of the full-body silhouette with only 184 vertices. Its job is broad mass, vertical continuity, and negative-space framing, so it receives large quiet planes.

### Focal complexity

The body concentrates density around:

- head / helmet crest;
- angular shoulder and gorget architecture;
- chest transition;
- silhouette-critical armor breaks.

The face and shoulder area therefore carries much more geometric information per square unit than the cape or lower body.

### Prop complexity

The shield receives 657 vertices because it is not a blank defensive plate. It contains a deep relief / heraldic composition that reads as a second focal object.

The flail receives 1,266 vertices mostly because repeated chain links and the terminal weapon need real articulated geometry. This is not ornamental tessellation spread everywhere; it is topology spent where repetition and mechanical structure require it.

Working law:

```text
LOW POLY != uniformly simple
LOW POLY = spend geometry only where semantics require it
```

## Topology grammar

The model is mostly quad-built rather than triangle soup:

- Body: 1,314 quads, 149 triangles, only a handful of larger n-gons.
- LeftArm: 136 quads, 12 triangles.
- Maille: 317 quads, 32 triangles.
- LionsMace: 113 quads, 4 triangles.
- Shield: 523 quads, 84 triangles plus a few larger polygons.
- Cape is the exception: 248 triangles / 46 quads, consistent with a thin draped planar surface where faceted directional folds matter more than loop regularity.

No visible mesh uses shape keys in this recovered file.

## Silhouette grammar

Diagnostic projection of the recovered source shows a highly disciplined hierarchy:

1. tall narrow central figure;
2. huge shield mass on the left-hand side of the combat body;
3. long weapon / flail vector on the opposite side;
4. oversized angular shoulders creating a hard upper-body crown;
5. long quiet cape mass stabilizing the composition;
6. relatively small feet and lower-leg armor so the upper body remains visually sovereign.

The model is not made interesting by local detail everywhere. It is made interesting by **large asymmetric masses with dense focal punctuation**.

## Shape language

- repeated wedges, pyramidal armor breaks, and pointed shoulder masses;
- rectangular / prismatic limb armor linking focal regions;
- shield as a large convex wedge / heraldic field;
- weapon heads built from radial hard-surface facets;
- long cloth/cape planes used as visual rest between dense mechanical regions;
- helmet / hair crest built as repeated stacked blade-like strips rather than a smooth coiffure.

The design repeatedly alternates:

```text
DENSE ANGULAR CLUSTER
-> LONG QUIET PLANE
-> DENSE ANGULAR CLUSTER
```

That rhythm is one reason the model reads as rich without becoming noisy.

## Material/tool discontinuity

This is the first archaeology specimen in the current run that directly proves Substance Painter in the source path.

The surviving `.blend` references only the BaseColor image as an Image datablock, so it does not by itself prove a full packed multi-channel material set. However, it proves that the Substance Painter export pipeline had entered production.

This makes Lionheart a useful bridge from the pre-material control represented by Remhir toward the later doctrine:

```text
geometry carries form
material channels can carry objecthood
```

Do not infer absent roughness / metalness / normal files from the surviving source alone.

## Animation inventory

Fourteen actions survive:

- `0T-Pose`
- `Attack1`
- `Attack2`
- `Attack3`
- `Block`
- `BlockInit`
- `EmptyAction`
- `GuardBlock1`
- `GuardBlock2`
- `HeavyCombo1`
- `HeavyCombo2`
- `Idle`
- `LionsFlailAction`
- `RunForward`

The model is substantially more animation-complex than Slime or Remhir, but the keying pattern is mixed.

`RunForward` is densely keyed almost every frame, consistent with imported / baked motion.

The authored attack and block actions still contain semantically clustered extrema rather than a perfectly uniform frame cadence. Weapon and shield controls are explicit (`SwordBone.R`, `ShieldBone.L`).

`Attack1/2/3` strongly involve feet, chest, root, hands, weapon and shield, indicating full-body combat rather than isolated weapon-arm animation.

## The paradox: visual high-water mark, low utilization

If later project history corroborates Drew's memory that Lionheart was barely used, this creates an important design warning:

```text
artifact quality != system leverage
```

A highly resolved model can be an artistic success while being a poor multiplier for the game around it.

That is not an indictment of the model. It means archaeology should track at least two axes independently:

```text
OBJECT QUALITY
SYSTEM USE / DESIGN LEVERAGE
```

Lionheart may be a useful counterexample to Remhir:

- Remhir: comparatively primitive-looking source, very high remembered play leverage.
- Lionheart: highly resolved visual artifact, very low remembered utilization.

If that contrast survives more evidence, it becomes a major Thunder design lesson.

## Durable lessons

1. **Polygon budget should follow semantic importance, not surface area.** Huge cape planes stay cheap; focal armor, shield relief, and mechanical chain geometry receive the budget.
2. **Low poly can be information-dense without being noisy.** Alternate dense angular clusters with long quiet planes.
3. **Silhouette hierarchy outranks local ornament.** Shield, shoulder crown, weapon vector, cape mass and helmet crest define the character before texture detail.
4. **Tool capability and design leverage are separate axes.** A visually mature artifact can still be underused; a crude artifact can dominate play value.
5. **Substance Painter marks a real pipeline discontinuity.** This file directly places Painter in the production chain, making it a key specimen for tracking when material channels began sharing semantic labor with geometry.

## Compact Thunder record

```text
slug: lionheart
mechanism: highly resolved low-poly knight whose geometry budget is concentrated in silhouette-critical armor, heraldic shield relief, and real articulated weapon structure
style: tall narrow knight; angular shoulder crown; giant asymmetric shield; long flail vector; quiet cape planes between dense wedge clusters
production significance: source-verified Substance Painter era; visual high-water mark in Drew's low-poly phase (USER_MEMORY + strong source support)
strongest lesson: spend polygons where meaning changes, not where surface area is large
counter-lesson candidate: coolest-looking artifact may have had the least system leverage (USER_MEMORY, pending project corroboration)
source: Lionheart.blend @ 31667dc375db5921aed13ce6afedbc4d7db5052e31181ec6574862f45ed0fa92
```
