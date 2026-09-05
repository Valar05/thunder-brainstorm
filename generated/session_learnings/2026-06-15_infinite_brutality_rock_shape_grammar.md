# Infinite Brutality Rock Shape Grammar Handoff

Date: 2026-06-15

## Durable Lesson

Infinite Brutality floating terrain should not be generated as random blobs, asteroids, potatoes, or noise-deformed spheres. Terrain should read as broken land fragments: torn-out cliffs, mesas, collapsed fortress foundations, canyon walls, basalt column fields, eroded arches, and architecture fused into stone.

The practical generator rule is: every terrain chunk must imply a shaping process and a gameplay purpose.

## Shape Contract

Each terrain piece needs three reads:

- macro: the named silhouette visible from far away
- meso: the playable traversal form, such as ledges, terraces, ramps, shelves, cracks, bridges, or collapsed platforms
- micro: surface support detail, such as chipped edges, fracture lines, sediment bands, foothold cuts, and directional erosion

Accepted grammar families:

- sedimentary mesa for main traversal islands and arenas
- canyon wall for vertical boundaries, climb faces, perches, and dramatic backdrop reads
- basalt column for volcanic or void-touched platforming rhythm
- hoodoo or spire for sparse landmarks and hazards
- fractured fortress for Infinite Brutality identity, where architecture looks swallowed by terrain or torn out with it

Rejected patterns:

- smooth lumpy islands
- round asteroid fields
- melted or inflated forms
- platforms with no geological explanation
- random spikes everywhere
- caves or holes whose traversability is unclear

## Implementation Bias

Before generating or accepting a new island, answer:

- What force shaped it?
- What is the silhouette name?
- Where does the player stand?
- Where does the player move next?
- What combat or traversal purpose does it serve?
- What makes it different from nearby chunks?
- Does the texture explain the form instead of hiding it?

If the answers are unclear, revise the shape before adding props, enemies, or texture detail.

## Project Integration

Local contract:

- `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/docs/ROCK_SHAPE_GRAMMAR.md`

Update this record when the generator gains explicit rock grammar archetypes, macro silhouette tests, or screenshot-based acceptance checks.

## Build 0.8.174 Sandstone Mesh Harness Correction

A screenshot showed the sandstone rewrite had drifted into broken flat slabs, dark holes, likely non-manifold edges, and bad normals while the older blob-era tests still passed. The failure was that the integrity harness tested legacy surface-net room and bridge meshes, not the active sedimentary mesa mesh path.

The accepted correction is to keep sedimentary visual mesh output tied directly to the collision voxel field, remove diagonal-only voxel contacts before meshing, and require the active sedimentary island and bridge meshes to pass watertight, manifold-edge, and outward-normal checks in `tools/test_island_mesh_integrity_contract.mjs`. Future terrain rewrites should extend this active-path harness before accepting screenshots or triangle-budget wins.

## Build 0.8.175 Visual Weathering Correction

A follow-up screenshot still read as crisp kitbashed cubes. The accepted diagnosis is that material weathering alone is insufficient when every visible sandstone vertex remains on an axis-aligned voxel grid.

The correction keeps voxel collision and manifold exposed-face meshing, but applies deterministic shared-vertex sediment shear and erosion offsets to the visual mesh. This breaks the exact cube-grid read without reintroducing random noise blobs, open edges, or mismatched collision. `tools/test_rock_grammar_contract.mjs` now requires most sedimentary mesh vertices to move off the exact grid while the mesh integrity contract still checks watertight manifold output.
