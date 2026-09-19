# Infinite Brutality — Two-Repo Lineage Anchor — 2026-09-19

## Why this note exists

Drew supplied the historical repository:

- `Valar05/InfiniteBrutality` — private, Godot 4.2 Mobile project, last pushed 2025-01-08.

This must be distinguished from the modern repository:

- `Valar05/infinite-brutality` — public, current Three.js browser prototype for a first-person melee/platformer roguelike in Limbo.

The shared title and melee focus make the historical repo a concrete lineage anchor. Direct file/code inheritance between the two repos is not yet proven and should not be invented.

## Historical capital-I repo: proven shape

Repository:
- https://github.com/Valar05/InfiniteBrutality

Proven runtime facts from current `main`:
- Godot 4.2, Mobile renderer.
- Main scene: `game.tscn`.
- First-person player with mobile touch controls.
- Left-side joystick for movement.
- Right-side touch surface multiplexes camera, attack, and defense:
  - tap = attack;
  - drag = turn camera;
  - hold = block.
- Blocking has a short parry window.
- Stamina absorbs blocked damage before health.
- Five-step fist chain with authored transition and hitbox timing.
- Additional animation vocabulary includes sprint, air, crouch, power, kick/parry, knife, one-hand, and wand families.
- Enemy pressure is currently Orc-based; the spawn controller increases active population as kills accumulate, capped at 15.
- The game is already mobile-first melee rather than a desktop-first port.

## Important control archaeology

This repo shows an early high-density touch mapping:

```text
left thumb:
  move / run

right touch:
  tap  -> strike
  drag -> turn
  hold -> block / parry
```

That is not low-input in the later survivorlike sense. It is instead an early attempt to make a full first-person melee grammar fit on a phone without a forest of buttons.

This is relevant to later Drew control design because it exposes the pressure that later projects often solve by moving verbs into:
- movement,
- contact,
- automation,
- state,
- context,
- and build choice.

Do not rewrite this repo as already having the later one-stick doctrine. It is useful precisely because it shows an earlier, more explicit combat surface.

## Modern lowercase repo

Repository:
- https://github.com/Valar05/infinite-brutality

Current proven identity:
- Three.js landscape mobile prototype.
- First-person melee/platformer roguelike in Limbo.
- Browser-native.
- Current explicit action buttons include Strike and Jump.
- Modern systems include generated districts, terrain grammars, first-person arms, combat ownership contracts, and procedural world work.

The modern repo preserves the name and the first-person melee center while radically changing engine, world architecture, and production method.

## Lineage statement

Safe statement:

> `InfiniteBrutality` proves that Infinite Brutality existed as a mobile-first Godot first-person melee project by January 2025. The modern `infinite-brutality` is a later same-title first-person melee project in Three.js. The naming and mechanic continuity are strong lineage evidence; exact code inheritance remains unproven.

## Relation to Driftfield archaeology

The historical capital-I repo is **not** enough to resolve Driftfield's earlier space-melee donor.

Why:
- surfaced historical InfiniteBrutality is a ground arena;
- enemy set is Orc-based;
- current evidence does not establish a space setting, asteroid field, or inherited asteroid routine.

Therefore the existing Driftfield donor status remains:

> **UNRESOLVED. DO NOT GUESS.**

The historical InfiniteBrutality repo should be treated as a newly identified lineage anchor, not retrofitted into the missing donor slot.

## Relation to Taste Trap

Drew reports that modern Infinite Brutality is expected to evolve into Taste Trap.

Preserve that as firsthand future-project lineage, not as current runtime fact.

This creates a now-better-supported long arc:

```text
historical InfiniteBrutality (Godot mobile melee)
        ↓  same-title / melee lineage, exact code transfer unproven
modern infinite-brutality (browser melee/platformer roguelike)
        ↓  Drew-reported future evolution
Taste Trap
```

## Durable lesson

Names may persist even when implementations mutate aggressively.

In Drew's project family, continuity may live more strongly in:
- combat grammar,
- control pressure,
- taste,
- recurring verbs,
- and the problem being pursued

than in engine or source-tree continuity.

Pocket law:

> **TRACK THE VERB, NOT JUST THE REPO.**
