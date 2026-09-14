# Last Convoy — Throttle as Temporal Density

**Date:** 2026-09-14
**Status:** user-provenance design evolution + direct source-backed mechanic analysis

## User observation

Drew reports that throttle was added later and expanded the game enormously. The player can touch the movement surface and reduce speed gradually. Slowing may be useful or disastrous.

This is not merely a convenience control. It changes how one existing movement verb interacts with several systems that run on different clocks.

## Direct source evidence

In `Valar05/last-convoy/scripts/player.gd`:

- when the touch control is not being touched, the player preserves current velocity and keeps moving;
- while touching, input magnitude becomes a speed command after a deadzone/remap;
- velocity lerps toward `direction * SPEED * input_magnitude`, so a smaller touch magnitude can decelerate the vehicle rather than stopping instantly;
- body rotation still follows movement direction;
- the main cannon auto-fires on a fixed `fire_rate = 1.5` second timer, independent of travel speed;
- the convoy trail is recorded at a rate proportional to current speed ratio.

The speed-scaled trail sampling is especially important. At lower travel speed, fewer trail points are recorded per unit time, approximately preserving spatial spacing between recorded points rather than allowing the convoy history to become arbitrarily dense simply because the leader slowed down.

## Why throttle expands the game

The fixed-time cannon means speed changes the *spatial* density of firing opportunities.

Approximate relation:

```text
distance traveled per lead-cannon shot ~= speed * 1.5 seconds
```

Slowing therefore means more firing events can occur over the same distance traveled, while moving faster spreads those events farther apart in space.

At the same time, orientation is still steering and steering still writes the future convoy path. Throttle therefore changes the geometry in which those shared obligations must be solved:

```text
DIRECTION
-> immediate heading / next shot direction
-> future convoy path

MAGNITUDE
-> travel speed
-> distance between timed shots
-> spatial turning curvature
-> amount of real time spent exposed to ongoing threats
```

Because the body's turn response is time-based while translation is speed-dependent, slowing also permits tighter spatial redirection: roughly the same heading correction can happen over less traveled distance.

The tactical trade is therefore not simply `fast versus slow`. Slowing can improve alignment, maneuvering precision, and spatial fire density, but it also spends more world-time in the same region and can increase exposure to enemies or other time-based pressure.

## Purity consequence

Throttle is a strong example of adding a **degree of freedom to an existing verb** instead of adding a new verb.

The control surface remains compact, but the decision space grows sharply because one scalar changes the relationships among several existing systems.

```text
same verb
+ one continuous parameter
+ several coupled consequences
= large new decision space
```

This helps explain how Last Convoy remains compressed while supporting substantial tactical depth.

## Candidate law

> **Do not add a new button when one more dimension of an existing control can create the needed conflict.**

And:

> **Throttle is not speed selection. It is control over how much world-time is spent per unit distance.**
