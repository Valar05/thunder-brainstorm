# Armored Bus Stop — Drag Handle, Not Steering Wheel

**Date:** 2026-09-14
**Status:** playtest correction / control doctrine

## User correction

The steering still felt unintuitive even after making the visible control surface match the input rectangle. Drew described the desired behavior approximately as:

> If I drag left, it should drag the tank left.

The important distinction is that the previous control still treated the thumb as a **steering wheel / absolute steering control**, while Drew's hand expected a **direct-manipulation handle attached to the vehicle**.

## Failure mode

The corrected-but-still-wrong build used absolute horizontal position inside the steering zone to derive steering input. That means the control answered the question:

```text
where is the finger inside this steering rectangle?
```

rather than:

```text
which direction did the finger move from where it landed?
```

This made touch technically responsive but semantically opaque.

## Reused proven pattern

Use Marrow Runner's floating relative-drag grammar:

```text
TOUCH DOWN
-> that point becomes zero / origin

DRAG VECTOR
-> player intent direction

RELEASE
-> no directional command
```

For Armored Bus Stop, the vector is interpreted as requested **screen-space travel direction**, not a virtual wheel angle.

The right-side pedal remains a separate throttle / brake / reverse control.

## Vehicle response

The direct-manipulation command should be truthful immediately while the APC can remain physically imperfect:

```text
finger drag vector
-> requested travel direction
-> APC body turns toward it quickly
-> momentum / grip / terrain catch up more slowly
```

So gravel, mud, and inertia may delay the vehicle's obedience, but the input itself must not be ambiguous.

Compactly:

> **The thumb tells the truth immediately. Gravel gets to be the liar.**

This preserves Long Haul-style skew downstream of a Marrow Runner-style direct input.

## General lesson

A control can be geometrically accurate and still violate the user's mental model.

```text
CONTROL SURFACE TRUTH != CONTROL SEMANTIC TRUTH
```

When a player says “drag left,” first decide whether they mean:

- turn a virtual wheel left,
- rotate the nose left,
- or move the controlled object left.

Do not silently substitute one for another.

> **Put simulation between intent and outcome, not between the finger and intent.**
