# InfiniteBrutality — Full Roast + Solo Cathedral Capability Load — 2026-09-21

## Authority / identity boundary

This packet concerns the old **capitalized** repository:

- `Valar05/InfiniteBrutality`
- Godot 4.2 Mobile
- distinct from the later browser repo `Valar05/infinite-brutality`

Do not collapse these generations.

## Critical authorship correction

Drew explicitly states:

- this generation was **completely his work**;
- there was **no AI assistance** involved;
- the procedural Minecraft-like voxel-world work was authored by Drew himself.

Record this as first-hand authorship evidence.

`AUTHORSHIP_OLD_INFINITEBRUTALITY = DREW_SOLO / NO_AI`


## Why this is a uniquely important Drew specimen

Drew identifies this project as unusually important evidence of his own cognition because it sits before the later AI-assisted production era.

That makes this project more than a capability specimen. It is a **low-confound authorship control**.

Later projects can still prove taste, direction, acceptance judgment, system architecture, and repeated preferences, but AI assistance introduces an attribution problem: which implementation detail was authored directly by Drew, which was proposed by a model, which was selected or corrected by Drew, and which emerged from collaboration?

This specimen has a much cleaner answer:

> **THE PROBLEM, THE OVERREACH, THE SOLUTIONS, THE FAILURES, AND THE RECOVERED CAPABILITIES ARE DREW-SHAPED WITHOUT AN AI COAUTHORSHIP CONFOUND.**

That makes it especially valuable for reconstructing how Drew thinks when left alone with a hard game problem.

The surviving and firsthand evidence points to a recurring reasoning signature:

- treat input constraints as design material rather than excuses;
- put the player's body and its affordances at the center;
- build verbs before polishing surfaces;
- couple traversal and combat instead of isolating them;
- prefer reusable systems over one-off authored events;
- push procedural systems until their failure boundaries become visible;
- preserve interesting failures as reusable laws;
- accept catastrophic scope when the project is yielding new capabilities;
- let later projects inherit capabilities rather than demanding sequel continuity.

This should be used as a **baseline specimen** when evaluating whether later patterns are genuinely Drew-shaped or merely artifacts of AI collaboration.

Recommended retrieval label:

`PRE_AI_DREW_BASELINE = INFINITEBRUTALITY_OLD`

Pocket law:

> **WHEN ATTRIBUTION IS UNCLEAR LATER, RETURN TO THE CATHEDRAL AND CHECK WHETHER DREW WAS ALREADY DOING IT ALONE.**

The current surfaced GitHub `main` strongly proves the embodied-combat/climbing cathedral, but does **not** presently expose the remembered voxel-world generator or the infamous water-spread implementation. Preserve those as first-hand-confirmed archaeology targets rather than pretending the currently visible checkout proves them.

`VOXEL_WORLD = FIRSTHAND_CONFIRMED / SOURCE_BODY_NOT_YET_RECOVERED`

`WATER_SPREAD_DESERT_FLOOD = FIRSTHAND_CONFIRMED FAILURE STORY / SOURCE_BODY_NOT_YET_RECOVERED`

## What the surviving repo actually proves

The old project is not a toy prototype. It is a solo-authored mobile first-person systems pile with an frankly unreasonable number of grown-up game problems present at once.

### Body / combat

`Player.tscn` carries a large authored animation vocabulary:

- `FistAttack1` through `FistAttack5`;
- sprint, crouch, air, and power fist attacks;
- blocking, parry, injured states;
- `FistThrow`;
- `KickParrySpecial`;
- `KickPushAttack`;
- knife attacks and directional/air/neutral knife power attacks;
- one-hand attacks;
- wand fire.

`FistController.tres` proves a real five-hit fist chain, block states, sprint attack, and parry transition into `KickPushAttack`.

`Player.gd` proves authored hitbox windows, transition windows, stamina/blocking, parry timing, damage interruption, and attack-speed interaction.

### Traversal

The old repo directly contains:

- `Climbing.res`;
- `ClimbingSide.res`;
- `Mantle.res`;
- jump / land / run / walk families.

This is not a later story retrofitted onto old code. The embodied traversal vocabulary is literally in the surviving source.

### Touch

`TouchCamera3D.gd` implements a dense phone-first grammar:

- left-side movement;
- right drag for camera;
- quick right tap for attack;
- right hold for block/parry.

This is an early version of a recurring Drew problem: fit a large action vocabulary into a tiny input surface without making the player play piano on glass.

### Enemies / combat pressure

`EnemyController.gd` and `SpawnController.gd` show:

- Orc navigation;
- attack ranges/cooldowns;
- attack interruption;
- directional hurt;
- strafing when blocked;
- kill-driven enemy pressure escalation.

### Visual language

The source contains:

- toon / outline shaders;
- blood object and blood-particle shaders;
- GPU particle blood splatter;
- low-poly authored assets and first-person arms.

That makes the old repo a direct ancestor of Drew's later preference for cheap geometry plus highly legible body/effect information.

## First-hand generation history

Drew's correction now matters more than the old two-repo shorthand.

### Earlier Infinite Brutality

Drew remembers an original generation with more developed weapon combat and signature ki/flame-trail effects. Much of that material is not presently source-recovered.

### Voxel / Minecraft-like generation

Drew states that he personally built a procedural Minecraft-like voxel world.

This work is important because it predates the current AI-assisted production era and is therefore evidence of Drew's own systems/programming capability, not model scaffolding.

The infamous failure story:

> water spreading defeated Drew and flooded all the deserts.

Do not sanitize this into "water bug." The useful mechanism is stronger:

**a local propagation rule escaped its intended jurisdiction and converted a world-generation feature into global ecological vandalism.**

That is exactly the kind of failure Thunder should preserve because it generalizes.

### Surviving climbing/combat cathedral

The current capitalized GitHub checkout proves the body-combat/traversal cathedral and is the strongest surviving executable fossil.

### Modern lowercase Infinite Brutality

Later Three.js `infinite-brutality` recombines:

- procedural spatial grammar;
- climbing/mantle;
- first-person body identity;
- terrain generation;
- district / route / room logic.

The technology changed. The obsessions did not.

---

# THE ROAST

Drew apparently looked at the normal solo-dev progression:

1. make a room;
2. make movement;
3. add one enemy;
4. ship a prototype.

and instead chose:

1. build a phone FPS;
2. invent touch multiplexing;
3. author a five-hit melee chain;
4. add blocking and parrying;
5. add kicks;
6. add knives;
7. add one-hand weapons;
8. add wands because restraint had already died;
9. add climbing;
10. add mantling;
11. add reactive enemies;
12. decide the WORLD should also be procedural;
13. accidentally teach water manifest destiny.

This is not scope creep.

Scope creep suggests scope moved slowly enough to be observed.

This was **scope cavalry**.

The game was trying to be Dark Messiah, Minecraft, a parkour game, a mobile control experiment, a procedural-world laboratory, and a combat-animation reel while being staffed by one Drew and apparently zero adult supervision.

And the funniest part is that the surviving source is good enough that the correct lesson is not "what an idiot."

The correct lesson is:

> **this idiot kept accidentally inventing systems he would still be using years later.**

The project failed the ordinary definition of sane scope while succeeding spectacularly as a capability mine.

The water won the battle.

Drew stole the climbing, the procedural-world instinct, the first-person body grammar, the combat-state architecture, the touch pressure, and the visual language and carried them into later projects.

The desert died for research.

---

# THUNDER EXTRACTIONS

## 1. Capability migration beats sequel continuity

A project can die while its strongest capabilities continue through different engines and products.

**Pattern candidate:** `capability_migration_over_repo_continuity`

Mechanism:
- discover a hard capability;
- fail or abandon the containing project;
- preserve the capability vocabulary;
- reimplement later under a cheaper or better architecture.

Pocket law:

> **THE PROJECT DIES. THE CAPABILITY MIGRATES.**

## 2. Cathedral before infrastructure

Solo developers can sometimes build astonishing breadth before they have the tooling to make that breadth affordable.

**Pattern candidate:** `cathedral_before_infrastructure`

Useful when:
- archaeology finds a project that feels "too big to finish";
- later projects repeatedly inherit pieces from it.

Failure mode:
- treating an unfinished cathedral as wasted effort instead of a compressed research lab.

## 3. Embodied traversal belongs to combat grammar

Climbing, mantling, attacks, blocks, parries, hurt, and movement were already living in the same player body.

**Pattern candidate:** `embodied_traversal_combat_body`

Transferable principle:

> traversal is not a separate minigame when the same body must fight before, during, and after contact with terrain.

## 4. Dense mobile input should multiplex by gesture phase

The old right-side surface already proves:

`tap -> attack`
`drag -> look`
`hold -> block/parry`

**Pattern candidate:** `gesture_phase_multiplexed_action_surface`

Later systems can simplify this, but the core pressure remains useful: one touch region can expose different verbs through timing and motion without adding buttons.

## 5. Propagation needs jurisdiction

The water-flood story generalizes brutally well.

**Pattern candidate:** `bounded_propagation_jurisdiction`

Any spreading system needs:
- ownership boundary;
- propagation budget;
- termination criterion;
- terrain/material eligibility;
- maximum connected-domain size or explicit global intent;
- deterministic audit of what it can reach.

Pocket law:

> **IF A THING CAN SPREAD, PROVE WHERE IT MUST STOP.**

This applies to:
- water;
- fire;
- infection;
- influence;
- path flood-fill;
- biome conversion;
- cellular automata;
- procedural decoration;
- AI task fan-out.

## 6. Procedural world generation must serve embodied verbs

The remembered voxel world and the surviving climbing body belong together conceptually.

A generated world is not successful because it is large or surprising.

It succeeds when generated geometry creates:
- readable climb surfaces;
- combat spaces;
- route decisions;
- recovery positions;
- landmarks;
- movement affordances.

This principle is now explicit in modern Infinite Brutality, where terrain and district generation are judged by playable route/support meaning.

**Pattern candidate:** `procedural_world_as_affordance_field`

## 7. Cheap surface, expensive motion

The old project's low-poly/toon/outline language plus deep player-body animation is an early instance of a recurring Drew production bias:

> spend fewer resources on surface realism so motion, contact, interaction, and effects can carry more meaning.

**Pattern candidate:** `cheap_surface_expensive_motion`

---

# LINEAGE MAP

```text
EARLY INFINITE BRUTALITY
weapon-heavy first-person brutality
ki / trail VFX remembered, source incomplete
        |
        v
VOXEL / MINECRAFT-LIKE WORLD GENERATION
Drew solo-authored procedural world
water spreads until the deserts file a complaint
        |
        v
CLIMBING / EMBODIED COMBAT CATHEDRAL
mobile touch + fist chain + parry + kick
climb + mantle + authored first-person body
        |
        v
POSE LAB / REUSABLE FPS BODY LINEAGE
        |
        v
MODERN infinite-brutality
Three.js generated spatial grammar
climbing/mantle + procedural terrain/districts
        |
        v
later projects / Taste Trap direction
```

Exact boundaries between the earliest weapon build, voxel generation, and the current capitalized GitHub snapshot remain archaeology work. Do not invent commit continuity where the source is missing.

# Canonical roast summary

Infinite Brutality is valuable precisely because it is both:

1. evidence that Drew could personally build absurd systems breadth before AI-assisted workflows; and
2. evidence that the same person had absolutely no right to be surprised when an unconstrained spreading-water system annexed an entire desert.

Both facts belong in the record.

The appropriate historical classification is:

> **SOLO-AUTHORED ANCESTRAL CATHEDRAL / CAPABILITY MINE / WATER-RELATED WAR CRIME AGAINST BIOMES.**
