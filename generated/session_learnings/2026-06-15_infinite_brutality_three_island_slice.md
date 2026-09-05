# Infinite Brutality Three-Island Slice Lesson

Date: 2026-06-15

A live Android screenshot showed the Infinite Brutality runtime reading as a long, expensive bridge/tunnel gauntlet. The useful correction was to stop treating the 48-room batch as the current playable surface and instead prove a compact three-node Hanging Gardens slice.

## Generator Rule

For the current mobile slice, build exactly three close, vertically layered islands:

- `Cistern Customs Terrace`: low intake/water/customs node with household survival story traces.
- `Graft Market Crown`: middle market/garden repair node with room for buildings and graft tables.
- `Witness Cistern Stair`: high shrine/witness/sealed-route node.

The islands should be close enough to see as one place, offset by seeded noise so they do not read as a grid, and connected by short stair-stepped rock ramps. The top surfaces should be terraced and buildable, while the silhouettes stay organic rock rather than square rooms.

## Runtime Hooks

- `src/main.js`: `PLAYABLE_SLICE_ROOM_COUNT = 3`, `generateDistrictPlan()`, and `addIslandArtSteppedRamp()` define the slice.
- `src/district-geometry.js`: terraced district mass anchors build shared voxel support/mesh fields.
- `src/island-geometry.js`: `buildRoomIslandField(size, seed, terraced)` makes terracing opt-in so the older smooth island quality contract still passes.
- `tools/test_island_grammar_contract.mjs` and `tools/test_island_collision_contract.mjs`: updated contracts for three-island slice behavior.

## Validation

Validated with module parse checks plus island geometry, mesh integrity, collision, surface truth, grammar, spawn anchor, and support sweep tests. The Android browser loaded `src/main.js?v=0.8.153`; Android blocked direct `screencap`, so final visual inspection still needs a user screenshot.
