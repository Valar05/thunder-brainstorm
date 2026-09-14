# Armored Bus Stop: Last Convoy Return

**Date:** 2026-09-14
**Status:** active playtest discovery

## Observation

Armored Bus Stop converged back onto Last Convoy rather than needing a new vehicle-control grammar.

The dedicated accelerator and dedicated movement area were both unnecessary.

The useful control is one floating stick available anywhere on the play surface:

```text
touch-down = local zero
drag direction = desired travel direction
drag magnitude = desired speed
release = resume constant cruise in current travel direction
```

This is source-backed by `Valar05/last-convoy/scripts/player.gd`: while the dpad is touched, `input_vector.length()` determines speed magnitude and the normalized vector determines direction; when the dpad is not touched, the current velocity direction is retained and the target returns to full `SPEED`.

So the Armored Bus Stop control law should not imitate a steering wheel plus accelerator. It should inherit the simpler Last Convoy sentence:

> **The stick commands velocity. Constant movement resumes when the player lets go.**

Marrow Runner contributes the floating-origin touch implementation, not the movement law itself.

## No dedicated movement region

If touch-down defines the joystick origin, there is no mechanical reason to reserve a patch of screen for movement. Any otherwise-unused gameplay surface can become the stick origin.

This removes control chrome while increasing input truth:

```text
ANYWHERE CONTACT
-> RELATIVE DRAG
-> VELOCITY COMMAND
```

## Hull contact as attack

The same compression applies to combat. The APC already has mass and velocity, so running over enemies should be a consequence of driving rather than another action button.

Candidate rule now implemented in the current playtest artifact:

```text
ordinary enemy + useful-speed hull contact
-> squish
-> remove enemy

heavy enemy + useful-speed hull contact
-> large ram damage
-> heavy may survive
```

This keeps combat inside the vehicle grammar.

## Compact doctrine

> **Do not add a control for a consequence the vehicle can already express through motion.**

> **When a newer prototype rediscovers an older successful control law, reuse the law instead of inventing around it.**
