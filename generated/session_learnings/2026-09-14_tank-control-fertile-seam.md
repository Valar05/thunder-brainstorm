# Tank Control as a Fertile Seam

**Date:** 2026-09-14
**Status:** cross-project session learning / experiment candidate

## User observation

Drew identifies a strong connection between the newly excavated Last Convoy control grammar and recurring tank work in both Lexen WWII and Sherman Factory Floor. He considers this a genuinely fertile place to begin working.

This statement is autobiographical provenance. The supporting artifact evidence is kept separate below.

## Last Convoy source-backed mechanism

Direct source inspection of `Valar05/last-convoy/scripts/player.gd` shows:

- movement persists when the touch control is released;
- touch direction controls body orientation;
- touch magnitude controls commanded travel speed;
- the main cannon fires automatically on a fixed 1.5-second timer;
- the shot inherits current body rotation;
- position history becomes later convoy geometry.

The result is a compressed machine where movement, aim, fire timing, throttle, and formation history compete through a tiny control surface.

## Sherman Factory Floor evidence

Retrieved project artifacts show a `SHERMAN FACTORY FLOOR` interface exposing left/right track values, track links, wheel counts, `MACHINE / MECHANISM / CHASSIS` views, and explicit test/pause/reset state. This lane treats the tank as an inspectable mechanical system rather than only a finished visual subject.

## Lexen WWII evidence

Retrieved Lexen WWII material places command inside a Sherman / DD-Sherman crew system with explicit driver, gunner, wireless, bilge-pump, flotation, track, and landing states. Decisions occur under incomplete information and other crew members bear their consequences.

## Connection

The same object supports three useful views:

```text
LAST CONVOY      -> compressed control
SHERMAN FACTORY  -> exposed mechanism
LEXEN WWII       -> human consequence
```

The recurring tank interest may therefore be partly structural: tanks naturally couple movement, orientation, traction, timing, weapon geometry, mechanical failure, crew roles, and consequence.

## Candidate experiment

Do not begin by committing to another large tank game.

Test the smallest possible question:

> **Can a tank game be complete when the player only drives the tracks?**

Candidate toy:

```text
left track
right track
fixed-cadence gun
no dedicated aim button
no dedicated fire button
one screen
just enough opposition / terrain for heading and timing to matter
```

This would test whether the machine itself can generate the game through coupled obligations.

## Working rule

> **A tank can be a control surface before it is a content theme.**

> **Mechanism first; breadth only after the contact/consequence/adapt loop proves itself.**
