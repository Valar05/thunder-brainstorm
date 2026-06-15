# Driftfield Asteroid Mine Grammar Learning

Driftfield Expedition shifted from stitched rooms toward a scalar-carved asteroid interior. The next design layer treats the level as a mine system inside a volatile asteroid: cave/lava formation first, mining circulation second, sci-fi reinforcement third.

## Durable Pattern

Generate spaces by purpose, not by room label. A generated segment must answer what natural force formed it or what mining operation required it.

## Core Families

- Human mine architecture: haulage drifts, crosscuts, stopes, ore passes, vent raises, pump sumps, crusher stations, refuge bays, security bulkheads.
- Cave formation: lava tubes, collapse breakthroughs, jagged pockets, basalt ribs, fractured seams.
- Lava systems: magma pools, lavafall chimneys, heat vents, orange cracks, cooled crossing edges.
- Sci-fi overlay: coolant runs, transit gates, security locks, drone-readable markers.

## Implementation Hook

The Driftfield runtime now has a local pattern manifest and module that tags each generated room/connector with family, route role, carve hints, architecture, hazards, and signposting. This preserves Thunder's abstract pattern style while keeping render/collision/traversal tied to Driftfield's scalar field.

## Spatial Correction

Do not turn the corpus into a pure verticality rule. Driftfield should balance horizontal and vertical, curved and straight, based on the surface being emulated. Human-worked mine and security spaces can be flat, orthogonal, and boxy. Natural asteroid, collapse, and lava-formed spaces should bias organic curves, oblique angles, shelves, and diagonal breaches. Pure vertical focus remains valid only when the archetype demands it: ore passes, vent raises, lavafall chimneys, and descent landmarks.
