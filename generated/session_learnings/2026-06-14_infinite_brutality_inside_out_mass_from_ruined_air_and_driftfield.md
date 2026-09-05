# Infinite Brutality Inside-Out Mass Extraction

## Summary

Ruined Air and Driftfield Expedition suggest a clear path for Infinite Brutality's next environment leap: stop treating masses as decorated route segments and start generating one or two dominant floating bodies whose interiors are carved into traversable void.

The reusable synthesis is:

- `ruined_air` contributes old-school voxel mass composition: inverted lobe solids, MST-connected anchor graph, and capsule bridge solids.
- `driftfield` contributes the corrective discipline: authored semantic layout first, scalar carve second, same-field collision truth, and architectural dressing only after the void is valid.

## Ruined Air patterns worth reusing

- scalar field is built from a small set of exported tuning variables, not hidden constants
- room centers are chosen with separation rules, then connected by MST plus a few extra edges
- masses are positive solids in the field, not merely empty room slots
- bridge solids are explicit field participants rather than later mesh garnish
- chunk generation is async and modular, keeping heavy voxel work bounded

## Driftfield patterns worth reusing

- authored graph owns semantics before geometry exists
- connectors carry radii, path points, and pattern tags
- field carve is derived from rooms plus connectors plus shell constraint
- visible shell and collision truth are emitted from the same field pass
- architecture is attached after the shell is known, preserving rock-as-truth

## Infinite Brutality recommendation

Generate one memorable inside-out Hanging Gardens mass as a first slice:

- 3-4 anchor lobes
- 1-2 major throats
- one underside reveal
- one shrine or burial side pocket
- crystal-assisted climb recovery around the lower rim

This should feel like a hollow hanging body, not a room network that later received a shell.

## Explicit anti-pattern

Do not import Ruined Air's procedural walk cycle or foot IK root into Infinite Brutality. That code belongs to glide/ground recovery and body-yaw synchronization in a different movement model. Extract the mass logic only.
