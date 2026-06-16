# Driftfield Expedition Cave And Meshy Handoff

Driftfield now has two explicit modes: Arcade Mode remains the Asteroids-like cockpit survival branch, while Expedition Mode is the Descent-like 6DOF exploration fork at `expedition.html`.

## Runtime Shape

- `index.html` is a title screen that routes to `arcade.html` or `expedition.html`.
- Expedition is built from dedicated `src/expedition-*` modules instead of extending the arcade runtime.
- The current Expedition layer is a seeded cave-first asteroid mine segment with scalar-carved rooms/connectors, a 3D map, scanner pulses, salvage, key/gate progression, enemy encounters, lava, and a completion state.

## Durable Generation Rules

- Visible geometry, collision, navigation, and map read must come from the same source of truth.
- Never lie to the player: visible holes, tunnel mouths, and passages must be traversable unless visibly sealed.
- Cave shell validation now covers watertightness, inward-facing triangles, exterior sightline leaks, connector centerline crossings, fake sealed tunnels, local bend pinches, and UV/tile sanity.
- New areas should change structural grammar, not merely append another node to a flat loop.

## Meshy Infrastructure Lessons

- The first generated prop kit is `pipe_cable_kit_01`, sliced at runtime into connected GLB components and rendered through GPU `InstancedMesh` batches.
- Pipes/cables are visual-only infrastructure: they must reserve the traversal core, hug emitted cave collision triangles, read as continuous service systems, and never become loose clutter.
- Regression tests now assert tangent continuity, stretched coverage, endpoint mesh contact, supported junctions, disabled-anchor non-rendering, traversal-core clearance, and bracket attachment.

## Agent Workflow

- Screenshot-first critique matters for this project. Inspect fresh Android screenshots before reasoning about visual complaints.
- Repeated visual failures should become tests before another placement pass.
- Driftfield-local docs stay authoritative for implementation; Thunder records preserve reusable patterns and source pointers for future projects.


## Imported Cockpit PBR Lesson

The imported Meshy cockpit/cannon model uses the same principle as the Infinite Brutality FPS arms: if the foreground model looks flat while nearby PBR surfaces read correctly, make the supplied maps participate before blaming or weakening the maps. `src/visuals.js` now keeps the imported cockpit material map-driven with full normal/roughness/metalness scalar authority and cache-busted imports from both Arcade and Expedition.
