# Infinite Brutality Nook Story Placement And Second State

Date: 2026-06-11

## Project

The Hanging Gardens story system now has two concrete district states instead of one, plus a first placement-rule layer that connects story packets to actual district structure vocabulary.

## What Changed

- Added a second contrasting pilot focused on shrine-rim witness culture.
- Added placement sets that map story packet clusters onto real district archetypes and structural pockets.
- Added a thin runtime metadata hook so district templates now carry `storyPilotId` and `storyPlacementSet`.

## Why This Matters

The first failure mode of procedural story systems is abstraction: good prose that has no spatial home.

The second failure mode is monoculture: one good pilot that makes every future district feel like the same people in different lighting.

This pass addresses both.

## Second Pilot Difference

Pilot I:

- domestic survival in intake/customs infrastructure
- poisoned water memory
- concealment and rationed speech

Pilot II:

- witness culture on shrine rims
- silent bells and failed warnings
- ritual substitution over doctrinal purity
- folded names, handprint law, and sealed-route hope

## Placement Rule Lesson

A story nook should attach to a real spatial condition:

- underdeck recess
- wall niche
- customs alcove
- stair landing veil
- bell corner
- watch berth
- service table
- hidden cache
- memorial arch shadow
- water shelf or capped route station

If it has no real spatial host, it should not spawn.

## Runtime Hook Lesson

A small metadata hook is enough to keep the system honest early:

- `storyPilotId`
- `storyPlacementSet`

That lets future geometry or UI passes find the correct story family without forcing full text rendering immediately.
