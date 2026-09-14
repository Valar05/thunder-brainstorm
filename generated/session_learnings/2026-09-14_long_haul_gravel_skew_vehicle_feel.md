# Long Haul — Gravel Skew Driving Feel

**Date:** 2026-09-14
**Status:** direct source-backed driving analysis + APC brainstorm input
**Source repo:** `Valar05/long-haul`
**Source file:** `scripts/vehicle_controller.gd` sha `02ba5cbec3ea4c58b578d5f1cd4c52da13c8f2df`; `scripts/vehicle_audio.gd` sha `f2642e818dfa4a466ec1eed00c06851ed69b456f`

## User observation

Drew identifies Long Haul as a strong first-person driving-feel reference. The important sensation is that the vehicle **skews around like gravel**. The new APC toy does not need to be first-person; the useful thing to inherit is the movement law that makes the vehicle feel like mass traveling through imperfect grip.

## What the source actually does

Long Haul does not equate vehicle facing with velocity.

The controller keeps several distinct states:

```text
body rotation / facing
+ drive heading
+ forward speed
+ lateral velocity
+ momentum velocity
+ drift amount
```

Turning uses a wheelbase / steering-angle yaw calculation, but high-speed steering can also build drift. The default drift configuration begins above roughly 50 mph and reaches full speed contribution around 72 mph. Drift can add lateral velocity, lower effective grip, increase turn response, and delay the drive heading's recovery toward the body's new facing.

The key relationship is therefore:

```text
NOSE TURNS
!=
MOMENTUM TURNS IMMEDIATELY
```

`_update_drive_heading()` lets the previous travel direction persist during sharp, drifting turns. `_update_momentum_velocity()` then blends old momentum toward the newly desired velocity according to effective grip. At stronger slip, that alignment happens more slowly.

That is the gravel-skew sensation: the body can point somewhere before the mass fully agrees.

## Perceptual reinforcement

The first-person presentation amplifies the same physical law rather than creating it from nothing.

- camera yaw follows steering and speed;
- camera roll grows with speed, steering, and drift amount;
- impact events add bounded camera displacement;
- tire-roll audio rises with speed;
- tire-slip audio rises from the same drift state;
- engine layers crossfade and pitch from speed / gear / throttle.

So the player receives the same state through trajectory, cockpit motion, and sound.

## What should transfer to the APC experiment

Do **not** copy Long Haul's constants blindly. An APC may be slower, heavier, and operate on different terrain.

Transfer the relationship:

```text
STEERING changes facing
TRACTION controls how quickly momentum consents
SURFACE changes traction
SPEED changes how expensive a correction becomes
```

This works in first person, third person, overhead, or another camera. The first-person cockpit is an optional amplifier.

For the APC / bus-stop toy, a small amount of persistent lateral momentum could make deployment geometry richer without adding actions. Arriving at a stop is no longer only `reach marker`; it can be `manage mass well enough to arrive with useful heading, speed, and position`.

## Compact rule

> **Borrow the skew, not necessarily the camera.**

> **A vehicle feels physical when its facing can change faster than its momentum agrees.**
