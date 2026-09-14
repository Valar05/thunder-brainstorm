# Slime Blend Excavation — 2026-09-14

## Source identity

- Source: `Slime.blend`
- SHA-256: `9f8d3b5e8be174c06414d349fd4dcb560c41877e4db7617e9867a0c1bc5047b7`
- Size: 899,920 bytes
- Blender header: 2.78, 64-bit little-endian
- Historical path embedded in the file: `C:\Users\Drew\OneDrive\Documents\Slime.blend`
- Historical FBX export target embedded in the file: `C:\Users\Drew\Documents\hemomancy\Assets\Characters\Slime.fbx`
- One external skull reference image path survives in the file: `stock-photo-skull-model-set-on-isolated-white-background-183658367.jpg`.

## User-memory design intent

USER_MEMORY from Drew:

- fantasy slime with a transparent body;
- visible bones suspended inside the slime;
- the bones are not passive anatomy but the weapons used to attack while still encapsulated in slime;
- deliberately unusual minimalist fantasy morphology;
- remembered as one of Drew's most shape-key-heavy models;
- possible pre-Fleshpunk / Fleshpunk-before-Fleshpunk ancestor.

The surviving file strongly supports the bone-as-weapon morphology, but it does **not** preserve actual Blender shape-key datablocks or a source-transparent material state. Those two claims remain USER_MEMORY / unresolved version-history evidence unless another source file corroborates them.

## The source is a dual-skeleton creature

The most important structural finding is that the creature contains two different kinds of "skeleton."

### Invisible functional skeleton

The armature is tiny and highly abstract. It contains only:

```text
Root
RootBase
SlimeNeck
SlimeHead
RightPseudopod
LeftPseudopod
BackPseudopod
```

This is not a humanoid anatomical rig. It describes **functional soft-body regions**.

### Visible bone payload

The scene also contains ten separate bone-material source meshes plus one joined, rigged duplicate of those exact ten pieces.

The ten source bone meshes contain exactly 342 vertices total. The joined object `Skull.001` also contains exactly 342 vertices, and the rounded vertex multiset is identical to the union of those ten source meshes. This is direct evidence that the joined object is the animation-ready composite of the internal bone pieces.

The source pieces live on Blender layer 2. The armature, slime shell, and joined internal-bone composite live on layer 1. The scene enables both layers. This supports the interpretation that layer 2 preserves modeling/source pieces while layer 1 holds the rigged gameplay form.

## The bones really are mapped as weapons

The joined internal-bone composite is armature-deformed and uses exactly the same deformation vocabulary as the slime shell:

```text
RootBase
SlimeNeck
SlimeHead
RightPseudopod
LeftPseudopod
BackPseudopod
```

Dominant internal-bone vertex assignments:

- `SlimeHead`: 181 vertices
- `LeftPseudopod`: 61 vertices
- `SlimeNeck`: 44 vertices
- `RightPseudopod`: 44 vertices
- `BackPseudopod`: 12 vertices

The source-piece mapping is especially revealing:

- one 44-vertex internal piece maps entirely to `RightPseudopod`;
- one 61-vertex elongated internal piece maps entirely to `LeftPseudopod`;
- one 12-vertex elongated internal piece maps entirely to `BackPseudopod`;
- the remaining skull / neck / small-bone pieces map primarily to `SlimeHead`, `SlimeNeck`, and `RootBase`.

The outer slime shell is also distributed across the same pseudopod/head/neck control groups.

Therefore the hard internal payload and the soft external body are **coupled to the same semantic limbs while remaining separate geometry**.

This is stronger than "a slime with bones inside." It is:

```text
SOFT BODY REGION + INTERNAL BONE PAYLOAD = ONE FUNCTIONAL LIMB
```

The visible bone is not structural support for the slime. It is equipment carried by a soft-body region.

## Morphology inversion

Conventional anatomy says:

```text
bone -> support
muscle/flesh -> actuator
weapon -> external tool
```

This creature reassigns those jobs:

```text
slime -> actuator + container + body volume
invisible armature -> authoring/control abstraction
visible bone -> internal weapon / payload
```

So the skeleton stops being the body's hidden support architecture and becomes an **arsenal suspended inside the body**.

That is a strong candidate for genuine pre-Fleshpunk morphology because it reassigns biological structure by function rather than decorating conventional anatomy.

Status: structural echo is VERIFIED; historical lineage to later Fleshpunk remains INFERRED until more specimens establish continuity.

## Minimal rig, maximal morphology

The actual outer slime mesh is tiny:

- 91 vertices
- 175 polygons

The joined internal bone set is also modest:

- 342 vertices
- 310 polygons

The fantasy is therefore not being purchased with mesh density.

The outer form is a broad asymmetric low-poly blob / capsule around a highly legible internal bone arrangement. Large simple planes define the container; recognizable hard bone silhouettes supply internal punctuation.

This is fantasy minimalism by **ontological contrast** rather than detail count:

```text
ONE SOFT MASS
+
ONE HARD INTERNAL SYSTEM
+
ONE FUNCTIONAL INVERSION
=
complete creature concept
```

## Action inventory

The surviving blend contains only five actions:

- `0T-Pose`
- `Idle`
- `SlimeAttack`
- `SlimeDamaged`
- `SlimeForward`

Again, the vocabulary is aggressively small.

### Idle

Key times:

```text
0, 18, 33, 48
```

The largest measured local change is the head drift (~0.145 units). Pseudopods move only about 0.02–0.03 units. The idle therefore preserves the blob as a stable mass while allowing the internal/front region to breathe or wander.

### Forward

Key times:

```text
0, 6, 9, 12, 14, 19
```

The two lateral pseudopods each travel about 0.63 units from baseline, while the back pseudopod reaches ~0.52. Head and neck remain comparatively restrained.

Locomotion is therefore driven more strongly by pseudopod redistribution than by conventional leg cycling.

### Damaged

Key times:

```text
0, 1, 2, 4, 5, 12
```

The hit reaction is short and oscillatory. Back pseudopod movement reaches ~0.30 units; head and neck each move about 0.26–0.29. The early 1/2/4/5 keys create a fast reversal pattern before the 12-frame recovery.

### Attack

Key times:

```text
0, 15, 19, 21, 23, 24, 26, 28, 35
```

This is the clearest authored sentence in the file.

The first major pseudopod pose does not arrive until frame 15. Then the action becomes dense between frames 19 and 28 before returning at frame 35.

Measured maximum pseudopod local translation from baseline:

- BackPseudopod: ~1.151 units
- LeftPseudopod: ~0.936 units
- RightPseudopod: ~0.846 units

The neck compresses / shifts ~0.287 and the head ~0.376.

The `Root` also receives large keyed translation on individual axes during the attack, with one channel reaching ~2.188 around frame 23 and another ~2.892 around frame 28.

No meaningful bone-scale animation is present: the keyed scale channels remain 1.0.

So the attack's apparent deformation is achieved through **regional translation/rotation and skinning**, not cartoon bone scaling.

Working causal read:

```text
FLOAT / CONTAIN
-> LOAD / SPLAY
-> WHOLE BODY COMMITS
-> INTERNAL WEAPON REGIONS DIVERGE
-> PAYLOAD STRIKES
-> REABSORB / RETURN
```

The exact screen-space read still requires a Blender render or original gameplay footage, but the timing and rig relationships are source-measured.

## The shape-key discrepancy is important

Drew remembers this as possibly the most shape-key-heavy model he ever made.

The surviving `Slime.blend` contains **zero Blender `Key` datablocks**. Every mesh's `key` pointer is null.

Therefore this exact artifact cannot verify that memory.

Do not "correct" Drew's memory from one surviving file. Plausible explanations include an earlier working revision, applied/destructive shape keys, or a later export-prep copy, but none is presently proven.

This discrepancy is exactly why the archaeology corpus keeps USER_MEMORY separate from OBSERVED / MEASURED evidence.

## Transparency discrepancy

The file does preserve separate `MABone` and `MASlime` materials, but the legacy material data currently reads alpha 1.0 and contains no node-based PBR material network.

The transparent-body design therefore remains USER_MEMORY / intended runtime appearance rather than source-verified Blender material state in this recovered revision.

That does not weaken the morphology evidence: the shell and internal-bone system are independently modeled and rigged in a way that clearly anticipates simultaneous visibility.

## Style extraction

### Silhouette grammar

- huge simple asymmetrical blob envelope;
- very small internal hard silhouettes floating inside a much larger soft volume;
- skull/head cluster acts as a recognizable focal landmark;
- elongated bone tools create directional accents inside an otherwise nondirectional mass.

### Shape language

- outer body: broad irregular convex planes, low-frequency shape changes, almost no ornamental geometry;
- inner system: skull facets, cylindrical/club-like bone segments, wedges, spikes, joint-like ends;
- the visual interest comes from **hard internal punctuation against soft global mass**.

### Detail economy

The body has almost no fine surface detail. Identity comes from:

```text
CONTAINER SHAPE
+ INTERNAL ARRANGEMENT
+ MATERIAL CONTRAST
+ DEFORMATION
```

This is unusually efficient fantasy design.

### Camera dependence

Because the internal payload is spatially distributed, transparency / cutaway visibility is not garnish. The creature's idea depends on the viewer being able to read the relationship between shell and contents.

Future review should therefore test multiple gameplay angles, not only a silhouette render.

## Fleshpunk ancestry candidate

The strongest structural echo to later Fleshpunk is not "bones are gross."

It is:

> A biological component is detached from its assigned anatomical purpose and reassigned as a functional tool while remaining visibly biological.

That is the same family of reasoning later seen in Fleshpunk's negotiable biological functions.

The Slime is cleaner, simpler, and more fantasy-coded, but the conceptual move is already present.

Candidate lineage:

```text
Slime
-> visible internal biology as functional equipment
-> later biological function reassignment
-> Fleshpunk morphology grammar
```

Status: INFERRED, pending cross-specimen support.

## Durable lessons

1. **Separate body medium from weapon medium.** A creature can be mechanically richer when one material provides locomotion/containment and another provides force/direction.
2. **Reassign anatomy instead of adding accessories.** Bones become weapons without needing an external sword, inventory slot, or armor layer.
3. **One semantic rig can coordinate different materials.** The same pseudopod controls drive both slime shell and internal bone payload, creating coupled motion without collapsing them into one material object.
4. **Minimal fantasy can come from ontology, not austerity.** One soft envelope plus one hard internal arsenal produces more novelty than adding decorative fantasy nouns.
5. **Preserve memory/source disagreement.** The missing shape keys and nontransparent saved material are not failures of memory or source; they are evidence that revision history matters.

## Compact Thunder record

```text
slug: slime
mechanism: soft-body pseudopods carry hard internal bone payloads that function as weapons
style: enormous low-poly translucent-intent blob enclosing sparse skull/bone weapon silhouettes; hard-inside-soft contrast
motion: 15-frame attack load followed by dense 19–28 burst; three pseudopod weapon regions diverge strongly without scale cheats
strongest lesson: make material/anatomical categories perform different jobs instead of adding external equipment
lineage: strong structural candidate for pre-Fleshpunk biological function reassignment
source: Slime.blend @ 9f8d3b5e8be174c06414d349fd4dcb560c41877e4db7617e9867a0c1bc5047b7
```
