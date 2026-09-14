# Armored Bus Stop — Regular Joystick, Not Exact Inheritance

**Date:** 2026-09-14
**Status:** playtest correction

Drew identified that preserving Last Convoy's exact release behavior was now fighting the new game's core interaction. In Last Convoy, releasing the joystick restores constant movement. That is elegant there because movement is the persistent primary verb. In Armored Bus Stop, however, a bus stop asks the player to deliberately arrive and settle inside a spatial zone. Constant-cruise release makes the stop itself awkward.

The correction is to preserve the **useful control grammar**, not the exact inherited rule:

```text
floating joystick anywhere
angle = desired travel direction
radius = desired speed
release = zero desired velocity
```

The vehicle may still take time and distance to stop because the interesting math remains downstream:

```text
player intent
-> desired velocity
-> body orientation / acceleration response
-> traction and terrain grip
-> momentum lag / skew
-> actual vehicle path
```

This preserves Long Haul's useful distinction between facing, requested travel, and momentum without making the thumb fight a historical quirk from Last Convoy.

## Design rule

> **Inherit the mechanism that creates decisions, not every control behavior that happened to accompany it.**

> **Regular input can feed irregular physics.**

The control should be legible enough that difficulty comes from the carrier and terrain, not from decoding what release means.

## Bus-stop consequence

A bus stop makes stopping accuracy load-bearing. Therefore stopping must be available through the primary movement grammar itself. No brake button is required:

```text
stick magnitude -> desired speed
release -> desired speed zero
vehicle dynamics -> stopping distance
```

The interesting decision remains when and where to release, at what incoming speed, on what surface, and with what arrival angle.
