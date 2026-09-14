# blend-archaeology-analyst Skill

Use this skill when inspecting Drew's old Blender projects as a design corpus.

The goal is not to inventory everything. The goal is to recover compact, evidence-backed lessons about game feel, animation grammar, character design, visual style, production method, tool-capability shifts, and lineage, while keeping working context small.

## Architecture

Thunder Brainstorm owns the durable observations and abstractions.

Pose Lab V2 owns Blender-native inspection, renders, motion evidence, and the canonical `.blend` archive.

```text
CANONICAL BLEND (Pose Lab V2)
-> compact structural / rendered evidence
-> Thunder source observation
-> style + motion + mechanic extraction
-> durable lesson / lineage
```

Do not copy full project bodies into Thunder.

## Read order

For a new specimen:

1. Read this skill.
2. Read the one relevant source-observation / session-learning record.
3. Read related specimens only when testing lineage.
4. Read raw Pose Lab evidence only when a claim needs re-verification.

Do not preload the full archaeology corpus.

## Evidence labels

Every important claim must be tagged mentally or explicitly as one of:

- `OBSERVED`: directly visible in source/rendered evidence.
- `MEASURED`: deterministic source measurement.
- `USER_MEMORY`: Drew's production/play memory.
- `INFERRED`: interpretation supported by evidence.
- `VERIFIED`: independent evidence channels agree.
- `UNKNOWN`: unresolved; do not fill the gap.

User memory is valuable historical evidence but must not silently become source observation.

## Required extraction lenses

### 1. Identity

Recover only what helps route the specimen:

- project / character name;
- likely date / Blender version when available;
- original vs derivative source;
- gameplay role;
- source hash.

### 2. Mechanic / game-feel grammar

Ask:

- What are the smallest verbs?
- What changes state per input?
- Where is tension stored?
- What does the player read?
- What commits?
- What reverses or counters?
- What makes repetition stay interesting?
- What is the reset / persistence law?

Prefer a vicious set of 3-7 verbs over move-list transcription.

### 3. Animation grammar

When animation exists, extract semantic extrema rather than narrating every frame.

Useful concepts:

```text
READ
LOAD
COMMIT
BREAK
COUNTER
RETURN
```

Also inspect:

- support / planted invariants;
- anticipation vs release duration;
- contact state change;
- recovery cost;
- root motion vs pose motion;
- squash and stretch, including perceptual silhouette expansion without literal scale;
- authored holds;
- key deletion / compression;
- camera-relative read.

### 4. Production method

Record how the result was made when known:

- fully authored;
- mocap-derived;
- mocap with keys removed;
- retimed source;
- retargeted;
- procedural;
- hybrid;
- unknown.

This is load-bearing evidence. Opposite production methods that converge on the same grammar are especially important.

### 5. Style analysis

Every model gets style analysis, even if animation is absent.

Analyze style structurally rather than with mood adjectives.

Record only the load-bearing visual choices:

**Silhouette grammar**
- dominant masses;
- width / height logic;
- center of visual gravity;
- readable appendages;
- asymmetry;
- negative-space shapes.

**Proportion grammar**
- head / hand / foot emphasis;
- limb length;
- torso compression or elongation;
- heroic, grotesque, compact, lanky, squat, etc., but explain the geometry that earns the label.

**Shape language**
- wedge / block / cylinder / curve / spike / plate / bulb / taper families;
- repetition and contrast;
- where hard vs soft forms live.

**Surface / material grammar**
- smooth vs faceted;
- organic vs machined transitions;
- painted / vertex / procedural / PBR choices when source proves them;
- whether material boundaries reinforce anatomy / mechanics;
- whether wear, roughness, edge treatment, cavities, and material separation imply use/history rather than generalized noise.

**Causal surface test**

Do not call a surface 'realistic' merely because it is detailed.

Ask whether the surface implies a believable cause:

```text
handling -> wear
edge exposure -> abrasion
recess -> accumulation
material identity -> distinct roughness / response
impact / use -> local history
```

A surface may be stylized and still be causally true. General scratches, chips, grime, or noise with no implied cause are surface persuasion, not evidence.

**Detail economy**
- where detail clusters;
- where surfaces are deliberately quiet;
- whether readability comes from detail or gross form.

**Deformation style**
- squash/stretch;
- rigid-body feel;
- elastic joints;
- silhouette cheats;
- scaling, shear, or foreshortening tricks.

**Camera dependence**
- whether the design only works from one view;
- whether first-person, side-view, three-quarter, or gameplay camera changes the style read.

**Era / tool fingerprint**
- only when source evidence supports it;
- note obvious Blender-era techniques, topology habits, material limitations, or pipeline constraints without treating them as artistic failure.

**Capability discontinuity**

Track moments when a new tool changed what Drew could express cheaply enough to become part of style.

Examples include Substance Painter, better rigging, mocap, procedural tooling, image generation, or a new engine feature.

Use this shape:

```text
BEFORE: specificity required expensive channel A
NEW TOOL: channel B becomes cheap / available
AFTER: style reallocates information into B
```

Example hypothesis from USER_MEMORY:

```text
BEFORE Substance Painter: visual specificity leaned harder on geometry.
AFTER Substance Painter: simple form could carry manufacturing/use/history through material channels.
```

Do not promote the causal claim until specimen evidence supports the timing and surface change.

**Recurring Drew signature**
- only after comparison across specimens;
- do not declare a signature from one model.

### 6. Style lineage

When later work echoes the specimen, name the transferable geometry or material logic rather than merely saying it 'looks similar.'

Examples:

```text
broad fist emphasis -> later contact-frame enlargement
stone-weight gargoyle -> later planted heavy-body combat
wedge armor + exposed joint rhythm -> later Fleshpunk structural vocabulary
causal wear -> later material-honesty doctrine
```

Lineage can be `ancestor-of`, `descendant-of`, `echoes`, or `contrasts-with` and must retain evidence status.

### 7. Reduction test

Before promoting a lesson, ask:

> If I remove this observation, what future design decision becomes worse?

If the answer is 'none,' do not carry it forward.

Cap durable lessons at five per specimen.

## Context firewall

Raw Blender inventories, bone dumps, complete action lists, render grids, and frame-by-frame notes are evidence, not conversational memory.

After a specimen is reduced, future work should carry only:

```text
slug
one-line mechanism
one-line style signature
strongest lesson
related specimen slugs
source path/hash
```

Re-open raw evidence only when challenged.

## Pose Lab handoff

Pose Lab V2 should store canonical source blends under a dedicated archive path and produce inspection evidence under ignored/generated paths.

Thunder stores only compact references and extracted observations.

Machine checks are diagnostic. Human-visible truth still controls animation and style judgments.

## Final rudder

Do not ask only:

> What is in this Blender file?

Ask:

> What did this file teach Drew's design nervous system, what visual style did it encode, what capability made that style possible, and which parts can the surviving evidence actually prove?
