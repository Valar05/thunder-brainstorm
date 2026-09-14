# Remhir Blend Excavation — 2026-09-14

## Source identity

- Source: `Remhir.blend`
- SHA-256: `ce670c397e3acad64c29a5b6498df3bd578f418a99b971f38c1d6634e6c0051b`
- Size: 6,290,220 bytes
- Blender header: 2.77, 64-bit little-endian
- Historical path embedded in the file: `C:\Users\dclar\OneDrive\Documents\Remhir.blend`
- The file also contains the string `Remhir.fbx`; treat FBX import ancestry as INFERRED until corroborated.

## Direct structural observations

The source is much more informative than the intake memory suggested.

The main `Body` mesh is one object with 2,655 vertices, 5,354 edges, 2,704 polygons, and 10,682 loops. Nearly all polygons are quads. The body has an Edge Split modifier at 30 degrees and no subdivision modifier on the character mesh. Two armature modifiers are present, with `metarig` and generated `rig` armatures plus embedded Rigify scripts.

This is source evidence for an intentionally faceted, hard-plane character language rather than a smooth/subdivision-first body.

The body silhouette is dominated by very large bat/gargoyle wings. In the recovered base mesh the wingspan is roughly 4.88 Blender units while total vertical extent is about 2.83. The central torso is visually subordinate to the wing mass. Horns, narrow central torso, enlarged upper legs, long tapering lower legs, and segmented wing membranes create a strong horizontal / architectural silhouette.

## Combat action inventory

The blend contains 14 actions:

- `0T-Pose`
- `Block`
- `Block_hold`
- `CombatStance`
- `Counter`
- `Damaged`
- `HeavyKick`
- `Jump`
- `LightCombo1`
- `LightCombo2`
- `LightCombo3`
- `Midair`
- `Parry`
- `WalkForward`

This does not prove the exact shipped input map, but it verifies that the surviving character source was authored around a compact melee / defense vocabulary rather than a sword-only moveset.

### Timing extrema

The actions are key-compressed rather than continuously keyed at every frame. Representative unique authored times:

- `Block`: 0, 1, 4
- `Counter`: 0, 1, 2, 4, 9, 10, 11, 12, 18
- `Parry`: 0, 3, 5, 6, 7, 12
- `HeavyKick`: 0, 5, 6, 7, 8, 9, 10, 16, 22, 25
- `LightCombo1`: 0, 2, 4, 6, 7, 12, 15, 16, 18, 25
- `LightCombo2`: 0, 2, 4, 5, 6, 8, 9, 13, 18, 20, 21, 26
- `LightCombo3`: 0, 2, 4, 7, 9, 10, 11, 20, 25, 30

The source therefore supports the broader animation-compression history: authored extrema and sparse timing were already central to the file.

## The wings are gameplay anatomy

The strongest surprise is `Block`.

Measured curve change in `Block` is dominated by wing hinge / wing base controls, while hand and torso translation changes are comparatively small. `Counter` and `Parry` also move wing controls materially, and the later light-combo actions rotate wing bases as part of the body sentence.

This means the wings are not merely decorative silhouette. They participate in defensive and offensive state changes.

Current interpretation:

```text
WIDE THREAT SILHOUETTE
-> WING COMPRESSION / DEFENSE
-> REVERSAL
-> RE-EXPANSION
```

That is an unusually character-specific combat grammar. It also creates whole-body squash/stretch through silhouette compression even when the mesh itself is not rubber-scaled.

Status: MEASURED for wing-control motion, INFERRED for the exact visible silhouette until a Blender render of the actions is available.

## Counter is whole-body, not hand-only

`Counter` is only 18 frames long but has meaningful changes in both hands, torso, both feet, head, wing controls, and a dedicated `Hitbox` control. The left hand and right hand are the largest control changes, but the feet and torso also move strongly.

This supports a compact causal reading:

```text
READ / RECEIVE
-> BODY REORIENTS
-> HITBOX BECOMES TRUE
-> REVERSE OWNERSHIP
-> RECOVER
```

The counter is not a decorative reaction layered over neutral stance. The entire body changes tactical state.

## Animation literally contains gameplay code

The rig includes a dedicated `Hitbox` control and keys it inside attacks such as `Counter` and `HeavyKick`.

That is direct evidence for the current theory that animation and code are unusually entangled: gameplay collision state is authored on the same timeline as visible body state.

## Sword-to-hand pivot is physically encoded in the mesh

The `Body` mesh has three shape keys:

- `Basis`
- `HandMode`
- `SwordMode`

Current values in the recovered file are `HandMode = 1.0`, `SwordMode = 0.0`.

`HandMode` changes only 70 of 2,655 vertices, but several of those vertices move about 1.6 Blender units. In the recovered geometry this collapses the long right-side sword/blade geometry into the hand region. `SwordMode` changes 184 vertices around the hand / weapon relationship.

The shape keys are driven by inverse expressions:

```text
HandMode  = 1 - var * 2
SwordMode = var * 2
```

The surviving file therefore contains an actual morphology switch between hand-focused and sword-focused states. The earlier sword-first design instinct was not merely historical context; it remains encoded as a selectable geometry mode inside the character.

This is especially useful lineage evidence because the later punch-centered game did not need to erase the sword history. It reassigned primary combat meaning from weapon geometry to body/state grammar.

## Style extraction

### Silhouette grammar

- extreme horizontal wing span;
- narrow central body under a huge architectural wing canopy;
- horns as small upward punctuation;
- enlarged thighs / knees over long narrow lower legs;
- wing membrane panels create repeated wedge / trapezoid negative spaces.

### Shape language

- broad planar wedges in the wings;
- blocky / faceted torso masses;
- tapering lower limbs;
- small spikes / horns used sparingly at silhouette-critical locations;
- large simple planes carry more identity than surface detail.

### Surface / topology grammar

- low-poly / faceted presentation is source-supported by the mesh and 30-degree Edge Split;
- there is one legacy `BodyMaterial` in this `.blend`, no image datablocks, and no node-based PBR material setup preserved here;
- therefore later Substance Painter / full-channel material observations must remain USER_MEMORY / cross-corpus evidence rather than being attributed to this file.

## Material-channel A/B observation to carry forward

USER_MEMORY / prior production observation from Drew:

When stylized low-poly assets were compared with full PBR-style material channels versus diffuse-only, diffuse-only did not read as merely less polished. It read as incomplete.

Working law:

```text
material channels can be semantic, not cosmetic
```

Geometry answers what shape exists. Base color answers designed region identity. Roughness / metalness / normal / related channels can answer what kind of material reality the region belongs to.

Important correction:

```text
strip decorative surface noise != strip material truth
```

This should be tested specimen by specimen instead of becoming a universal assumption.

## Durable lessons

1. **Minimal verb count can coexist with high expressive depth when reversal is strong.** The surviving action set verifies compact punch / defense / counter vocabulary, while Drew remembers the infinite loop as unusually fun.
2. **Character anatomy should carry mechanics.** Remhir's wings materially participate in Block, Counter, Parry, and attacks, so defense is gargoyle-specific rather than generic humanoid blocking.
3. **A defensive contraction can be squash-and-stretch.** The wide wing silhouette can compress for defense and reopen for action without literal cartoon bone scaling.
4. **The sword-to-punch transition is encoded as a mode switch, not a clean historical replacement.** `HandMode` and `SwordMode` coexist in the mesh, while the remembered game centers the body.
5. **Keep material truth separate from surface noise.** Later full-channel material work may enrich simple geometry by adding semantic objecthood rather than by adding more modeled detail.

## Current compact record

```text
slug: remhir
mechanism: compact body-first melee where defense/reversal uses the gargoyle's wings and whole body
style: huge faceted bat-wing silhouette, narrow horned core, hard planar low-poly geometry, sparse spikes
strongest lesson: make the character's unique anatomy carry the verb instead of decorating a generic combat verb
lineage: likely early ancestor / contrast surface for later Gravity Fist body-first combat; exact causal lineage remains USER_MEMORY + INFERRED
source: Remhir.blend @ ce670c397e3acad64c29a5b6498df3bd578f418a99b971f38c1d6634e6c0051b
```

## Related Thunder notes

- `generated/session_learnings/2026-09-14_remhir_counter_fail_soft_precision.md` — preserves the fail-soft precision counter design decision and its nested block/counter timing model.
- `generated/session_learnings/2026-09-14_remhir_design_implications.md` — preserves the broader implications: tacit judgment before explicit theory, state-depth minimalism, anatomy-as-mechanics, perceptual squash/stretch, capability-vs-design-quality separation, and Remhir as a pre-material control specimen.
- `generated/source_refs_manual/blend_archaeology_source_refs.jsonl` — keeps measured source claims and USER_MEMORY claims separate for later corroboration.
