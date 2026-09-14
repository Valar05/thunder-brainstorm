# Armored Bus Stop — Control Surface Truth

**Date:** 2026-09-14
**Status:** playtest correction / known-good pattern reuse

## Playtest failure

Drew reported that the first Armored Bus Stop touch controls felt simultaneously unresponsive and inaccurate to touch position.

Inspection found that the problem was not primarily vehicle physics. The control visualization and the input math described different surfaces:

- the drawn steering zone occupied only the lower-left area, while steering math normalized against the entire left half of the viewport;
- the drawn pedal zone occupied only the lower-right area, while throttle/brake/reverse math normalized Y across roughly 12%–92% of the entire viewport;
- steer, throttle, and brake commands were additionally smoothed before reaching vehicle physics, so control lag was stacked on top of the intended vehicle inertia.

The result violated a basic input contract: the player's finger and the game's displayed control did not refer to the same geometry.

## Known-good patterns reused

Do not invent another mobile control scheme. Reuse patterns already proven in Drew's own games.

### Long Haul

- bounded steering region;
- bounded vertical pedal strip;
- exact screen-position-to-control mapping using the actual control rectangle;
- explicit brake band between forward and reverse;
- steering deadzone and nonlinear response curve;
- fast throttle response while vehicle momentum remains independently simulated.

### Marrow Runner

- pointer capture and stable pointer ownership;
- visible touch origin/pip feedback;
- visual feedback that tracks the same coordinates used by the input calculation.

## Corrected architecture

```text
FINGER
-> truthful visible control surface
-> fast control command
-> vehicle dynamics
-> weight / grip / slip / skew
```

Do not put the desired heaviness between the thumb and the command. Put it between the command and the vehicle response.

## Compact rules

> **The control surface must tell the same geometric truth as the input function.**

> **Put inertia in the machine, not in the thumb.**

> **Before inventing input, steal the control law that already survived play.**
