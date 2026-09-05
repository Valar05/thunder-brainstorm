# Level Design Environment Grammar Skill

Thunder Brainstorm corpus skill note for environment-first level design, procedural district structure, screenshot-driven critique, and critique-improvement maintenance loops. This is a Thunder-visible workflow note, not an installed Codex skill.

## Trigger

Use when a project is making disconnected rooms, unreadable vertical spaces, or shallow procedural variation, and needs a stronger environment-first level-design workflow.

## Core Direction

Do not begin from rooms or arenas.

A recurring general failure mode: adding stairs, platforms, and local vertical setpieces inside a mostly flat world graph does not create meaningful three-dimensionality. Macro topology must carry verticality first; room detail should reinforce it after path validation.

Begin from a place with a purpose, then derive traversal, combat, and hazards from that purpose.

Questions that should anchor the pass:

- What is this place for?
- What circulates through it?
- What districts would a functioning version of this place need?
- What maintenance, waste, transport, or ritual routes exist beside the main path?
- What can change state and therefore change the route?

## Workflow

1. Read the live project orientation, local agent docs, runtime generator code, and recent screenshot/playtest evidence before proposing changes.
2. Define the environment as a system: `purpose`, `districts`, `circulation`, `state`, `landmarks`.
3. Choose a hardware-appropriate world structure. On constrained devices, prefer seeded district graphs, district-scale gauntlets, loops, and streamed neighbors over giant seamless worlds.
4. Generate route bundles inside each district: official route, recovery route, maintenance route, shortcut or secret.
5. For vertical spaces, force explicit silhouettes. Descent, climb, and overlook spaces need upper/lower structure that reads in one screenshot.
6. Critique from screenshots first. If the space reads as random blockers or floating walls, remove generic clutter before adding detail.
7. Implement bounded slices. Prove the direction with one biome contract, a few district archetypes, or one special-case route grammar before attempting the full system.
8. Before dressing geometry, validate that macro topology already produces visible climbs, descents, and over-under relationships.
9. For rock or voxel-derived terrain, validate the active rendered mesh path. A fallback generator or inactive harness can pass while the visible terrain still fails.

## Maintenance Loop

This workflow should update itself as it is used.

After any meaningful critique or implementation pass:

1. Record the durable lesson in this Thunder note if it generalizes beyond one project.
2. Record the project-specific version in that project's local workflow note.
3. Keep updates small and concrete: failure mode, correction pattern, validation check, and any new litmus test.
4. Do not wait for the user to explicitly request the update when the level-design lesson is clearly durable.

## Reusable Litmus Tests

- Remove enemies: does the place still feel like a functioning environment?
- Remove props: does the route still read?
- Remove combat: is there still tension from structure, exposure, and state?
- Replay the seed: are the differences structural rather than cosmetic?
- Check one screenshot: can the player read purpose, route, and height relationship immediately?
- Check whether rock terrain reads as shaped geology or as crisp cubes. Passing topology tests do not excuse a kitbashed-block silhouette.

## General Patterns

- `purpose-driven biome`
- `seeded district graph`
- `route bundle instead of filler room`
- `explicit descent silhouette`
- `maintenance path plus official path`
- `stateful shortcut machine`
- `screenshot-first geometry correction`
- `process-driven terrain silhouette`

## Terrain Shape Grammar

For floating terrain, caves, islands, cliffs, or rock-heavy worlds, do not start from random noise or deformed spheres. Start from a named landform and the force that shaped it.

Reusable terrain rule:

- macro: name the silhouette from far away, such as mesa, cliff, slab, pillar, arch, bridge fragment, fortress foundation, canyon wall, or broken stair mass
- meso: define the playable traversal read, such as ledges, shelves, ramps, terraces, cracks, collapsed platforms, or climbable breaks
- micro: add close support detail only after macro and meso read clearly
- process: sediment, erosion, fracture, collapse, volcanic cooling, shearing, impact, gravity, water flow, or construction damage must be legible in the shape
- gameplay: every chunk needs a stand point, route, combat purpose, recovery possibility, or landmark job

Reject terrain that reads as potato, asteroid, smooth blob, melted mound, random spike scatter, crisp voxel cube stack, or kitbashed block pile. If a screenshot cannot answer what shaped the terrain and where the player moves next, the generator should revise the form before adding props or texture detail.

If collision or grammar uses voxels, keep that as the hidden truth field and weather only the visible emitted mesh. Deterministic shared-vertex offsets, erosion shelves, chipped lips, and sediment shear can break the cube grid without reopening non-manifold seams. Texture and normal maps should support this pass, not substitute for it.

## Infinite Brutality Companion

The tailored companion note for the current suspended-shanty-town direction lives at:

- `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/docs/LEVEL_DESIGN_WORKFLOW.md`
- `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/docs/ROCK_SHAPE_GRAMMAR.md`

Related Thunder records:

- `generated/session_learnings/2026-06-08_infinite_brutality_prototype_lessons.md`
- `generated/session_learnings/2026-06-15_infinite_brutality_rock_shape_grammar.md`
- `generated/project_links/infinite_brutality_project_links.md`
