# Arcane Manifold — Combined-Arms Recall Counterattack and Homing Lineage

**Date:** 2026-09-14
**Status:** active brainstorm / mixed source + autobiographical provenance

## Source-backed mechanic

Current Arcane Manifold code establishes:

- live projectiles carry forward state and local homing logic;
- block retargets active projectiles toward the player;
- returning projectiles receive extreme homing authority;
- return impact can convert the existing projectile field into a converging counterattack;
- block also provides the safe floor for a timing-sensitive parry bonus.

## Combined-arms interpretation

The useful analogy is not a literal historical tactic but a functional one.

A modern combined-arms defense often separates two jobs:

1. **Block / shaping fires**: use fires, obstacles, suppression, terrain, and defensive positions to disrupt momentum, canalize movement, fix the attacker, and preserve friendly combat power.
2. **Counterattack**: once the attacker is committed, slowed, disorganized, or exposed, maneuver forces exploit that changed state rather than merely continuing to absorb pressure.

Arcane Manifold compresses both jobs into one touch verb.

```text
OUTBOUND FIRE FIELD
-> BLOCK / RECALL
-> ENEMY CONTINUES THROUGH PRIOR PROJECTILE GEOMETRY
-> PROJECTILES REVERSE
-> COUNTERATTACK ARRIVES FROM THE ENEMY'S REAR / FLANK / PREVIOUSLY CLEARED SPACE
```

The block is therefore not passive protection. It is the phase transition that converts pre-existing fires into maneuvering counterstroke.

Generalized design law:

> A satisfying counterattack should exploit a battlefield state created before the counterattack began.

This is stronger than spawning a fresh damage effect after a successful block because the counterattack inherits history.

## Why it feels like combined arms

Combined arms works by making one arm create the conditions in which another arm becomes disproportionately effective. Arcane Manifold does the same internally:

- firing creates distributed projectile presence;
- homing gives that presence local agency;
- blocking provides protection;
- recall changes projectile authority;
- enemy motion through the existing field creates vulnerable geometry;
- impact / explosion converts convergence into damage.

No single subsystem is the whole attack. The effect emerges from cooperation between prior fires, defensive timing, persistent state, and redirected movement.

## Safe parry floor

The same logic appears at the micro scale:

```text
BLOCK = preserve combat power
GOOD TIMING = preserve combat power + seize initiative
```

This resembles a competent defense followed by a counterstroke more than a binary parry gamble.

## Homing provenance

Drew identifies two direct experiential ancestors for Arcane Manifold homing:

- **Half-Life 2 rocket launcher**
- **Dark Messiah fireball**

Treat this as autobiographical design provenance unless older source notes are recovered.

The important common property is not simply "homing projectile." It is **steerable consequence after launch**: firing does not terminate authorship. The projectile remains a live relationship between player intent and world geometry.

Arcane Manifold then extends that relationship one step further:

```text
FIRE -> STEER / HOME -> PERSIST IN WORLD -> BLOCK -> GLOBAL RECALL
```

The novel pleasure is therefore not just guidance. It is revocation and reassignment of projectile purpose.

## Homing as transfer of authority

Drew's later recollection clarifies why Arcane Manifold could not simply copy the Half-Life 2 model.

Half-Life 2's rocket is a low-rate projectile whose guidance can remain continuously paired to the player's cursor. That works because the player is effectively authoring one important projectile at a time.

Arcane Manifold behaves more like a high-rate stream, closer in authored feel to walking MG42 fire. If every already-fired projectile remained permanently enslaved to the current cursor, sweeping the aim across multiple enemies would cause old projectiles to curve toward the newest cursor position. The stream would stop representing the temporal history of the sweep.

The design problem therefore became:

> **At what point should the player stop directly owning a projectile's target?**

The live source uses a distance-gated authority handoff. While a projectile remains near the player, it follows the current cursor / camera-ray target. Once it exceeds `target_homing_length`, it can acquire its own enemy target and use local homing policy instead.

```text
NEAR BODY
player cursor owns target

PAST HANDOFF RANGE
projectile acquires local target

BLOCK
player overrides local autonomy with global recall
```

This creates a three-tier command structure:

```text
DIRECT GUIDANCE
-> LOCAL AUTONOMY
-> GLOBAL RECALL OVERRIDE
```

The first stage preserves the tactile pleasure of Half-Life 2 / Dark Messiah style steering.
The second preserves the meaning of sweeping high-rate fire by allowing older shots to keep faith with the region they were sent through instead of all bending toward the newest cursor position.
The third turns the entire persistent field back into a coordinated counterstroke.

### Temporal-authorship law

A high-rate guided weapon can become less expressive when every past projectile obeys the player's newest intention.

Therefore:

> **Preserve current intention near the emitter, then preserve historical intention by releasing older projectiles into autonomy.**

Or more compactly:

```text
CURRENT AIM owns the NEWEST consequences.
PAST AIM deserves custody of the OLDER ones.
```

This is another PERSIST pattern. The projectile field records the history of player aim instead of being continuously rewritten into the present.

## Thunder extraction questions

- Which older games let projectiles remain player-authored after launch?
- Which mechanics transfer authority from direct player control to local autonomy rather than choosing only one?
- Which high-rate weapons preserve the temporal history of a sweep instead of retroactively rewriting old projectiles?
- Which mechanics convert defense into initiative without introducing a separate button?
- Which counterattacks inherit geometry established before the counterattack begins?
- Which games create combined-arms effects inside a single avatar by giving different subsystems distinct battlefield jobs?
- Where does "block" function as a state transformer rather than a damage canceler?
