# Infinite Brutality Prototype Lessons

Date: 2026-06-08

## Project

Infinite Brutality is a Three.js landscape-phone first-person melee/platforming prototype at:

- Local project: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality`
- Local play URL: `http://127.0.0.1:8798/infinite-brutality/index.html`
- Runtime entry: `src/main.js`
- Current documented build: `0.7.2`

The project grew from the FPSPlayer/Arcane Manifold first-person platformer brainstorm into a darker low-poly melee-platformer direction. The current prototype uses FPSPlayer first-person arms, touch movement/look controls, Quake-influenced acceleration, procedural room composition, low-poly primitive architecture, and diegetic light sources.

## Creative Direction

Core fantasy: a normal human trapped in Limbo, a combat afterlife where violence has become geography. The tone is not heroic destiny or cosmic transformation. The player is flesh, breath, blood, and refusal.

World direction:

- Nightmare medieval surrealism, closer to Quake/Hexen than realistic kingdoms.
- Giant architecture should make the player feel small.
- Low-poly hard-edged geometry is a strength, not a placeholder.
- Rooms are combat sentences: each room must force a different tactical question.
- Environment should tell story through landmarks, hazards, scale, and impossible spaces.

Color/visual language:

- Primary: black stone, dark gray, aged bronze, dried blood red.
- Secondary: sickly green/corpsefire, pale blue flame, purple fog, molten orange.
- Avoid cheerful fantasy palettes and one-note dark-blue or beige washes.

## Current Runtime Shape

The prototype is intentionally a playable game surface, not a landing page. The first screen is the canvas runtime with touch controls. The user has repeatedly judged by Android screenshots, so fresh screenshots should be treated as source of truth when visuals disagree with code expectations.

Implemented runtime areas as of build `0.7.2`:

- Fullscreen Three.js scene with FPS arms rendered in a separate camera-space pass.
- Landscape phone controls: left floating stick, right look drag, always-visible Strike and Jump buttons.
- First-person melee arm animation wiring from `assets/models/FPSPlayer.glb`.
- Quake-inspired acceleration model with run build-up, air control, jump hold taper, and running jump boost; crouch is not a movement verb.
- Earlier procedural rooms: chasm, switchback, and spire archetypes. Current visual/level target is the authored triple-bridge skull guillotine hall, not generic boxes with scattered junk.
- Runtime-composed level graph: rooms are instantiated together rather than swapped one at a time.
- Dungeon layout pass: six rooms placed on a small grid with turns, vertical offsets, and loop links.
- Connector causeways: solid floors, side walls, landings, and stairs when room heights differ.
- Wall and central spire collision via simple AABB solids.
- Low-poly hard-edged primitive aesthetic with beveled boxes, tile fields, rubble, pillars, chains, and room props.
- Diegetic lighting pass: visible braziers/corpsefire meshes with actual point lights and flicker.

## Combat Bring-Up Contract

Gravity Fist exposed the stable combat pattern to reuse in Infinite Brutality: attack ownership must be explicit, attack permission must be state-gated, hitboxes arm on a timeline, damage must carry context, hurt reactions must be overlays, and attack stalls must be able to block reassignment.

Useful source refs for the pattern:

- `../gravity-fist/scenes/ai_conductor.gd` for attack ownership, permission gating, stalled owner release, and reassignment blocking
- `../gravity-fist/scripts/player.gd` for attack scheduling, dash timing, hitbox arming, damage context, knockback, and hurt reaction handling
- `../gravity-fist/scenes/world.gd` for authored move timing fields such as `dash_start` and `attack_end`

Design consequence for Infinite Brutality:

- do not let attack, hurt, movement, and room placement all change in the same slice
- do not use proximity alone as the attack rule
- do not reseat the enemy every room rebuild
- do not restart hurt from frame 0 every frame
- do not let combat feedback own placement or path replanning

## Level Design Bible Distilled

A good Infinite Brutality room should answer these questions:

1. Where am I? Landmark, silhouette, light, sound, material, sky break, blood river, weapon shrine.
2. Where can I go? Main path readable quickly, side paths visible and tempting.
3. What is the immediate threat? Enemy, trap, height, ranged pressure, ambush, narrowing exit, collapsing floor.
4. What is the first tactical choice? Charge, kite, climb, retreat, kick, throw, flank, use hazard, grab weapon.
5. What makes this fight spatial? Height, cover, ledges, pits, stairs, chokepoints, loops, pillars, bridges, doors, breakables.
6. What is the room toy? A hazard or affordance the player can exploit.
7. What is being taught or tested? One clear mechanic at a time.
8. What can the player see but not immediately reach? Visible destinations create desire.
9. How does the player leave smarter? They learn enemy behavior, route logic, weapon utility, hazard use, or level shape.
10. What is the memorable image? Every room needs a visual identity.

Important room composition lesson: stitching rooms in a straight line is not enough, but neither is filling a box with props. Rooms should be movement sentences with readable lanes, bridge commitments, side recoveries, elevation changes, and landmarks. Critical path and optional loop links should both be physically present.

## Procedural Level Direction

Current direction for level generation:

- Use a small grid graph rather than a linear hallway.
- Place six room nodes with x/z turns and y-level offsets.
- Maintain a critical path, then add loop connectors between adjacent non-consecutive cells.
- Use side portals on east/west walls and north/south portals so connectors can enter from multiple directions.
- Generate L-shaped connectors between room socket positions.
- Use stairs, bridge lips, ramps, and raised landings as bunny-hop/running-jump timing surfaces when endpoints differ in elevation.
- Keep connector floors continuous and forgiving for touch movement, while spacing landings to reward running-jump rhythm and air steering.
- Use diegetic lights at connector landings to read route changes.

Next needed design improvement: room archetypes should expose named socket poses and intended connector direction instead of using broad always-open wall portals. That will let the generator align doors, ledges, drops, lifts, and stairs semantically rather than only by grid position.

## Visual Lessons From Screenshots

Repeated screenshot feedback established several concrete visual rules:

- Dark geometry becomes unreadable under real phone/browser lighting conditions. Do not rely on global fog and a hidden key light.
- Props must be bottom-origin anchored. Center-origin props read as floating.
- Decorative horizontal ridge bars read like broken fence pieces when suspended without support. Remove or attach them to architecture.
- Causeways need side walls and continuous floors; gaps are unacceptable with touch movement.
- The central spire/landmark must be both visible and collidable if it looks physically important.
- The level map should be visibly composed, not merely a teleporting room sequence or a straight line.

## Lighting Direction

The current lighting model is moving away from invisible global light toward visible in-world sources:

- Warm braziers mark the main route and room corners.
- Blue-green corpsefire marks vertical/loop/secret-feeling links.
- Point lights are attached to visible flame meshes and flicker at runtime.
- Global hemisphere/key lights are reduced to readability fill.
- ACES tone mapping and sRGB output are enabled to reduce muddy contrast.

Open next step: design a stricter light grammar. For example: bronze fire = critical path, corpsefire = loop/secret/vertical danger, lava orange = hazard, pale blue = goal/exit.

## Controls And Movement Direction

Current movement goals:

- Touch-first landscape controls.
- Left side spawns/uses virtual joystick.
- Right side drag aims camera; action buttons should not block aim drag behavior.
- Run should build after forward movement, not be a constant toggle.
- Jump should be responsive on press, with short hold extension tapering quickly.
- Running jumps give directional boost and are the merged bunny-hop verb; do not add crouch-slide as a separate movement control.
- Air control should allow correction and overshoot prevention without removing abusable velocity.

The movement target is not strict Quake simulation. It is touch-friendly Quake/Hollow Knight hybrid: acceleration-backed, speedrun-capable, but forgiving enough that floating platforms, bridge chains, and connector causeways can be judged on a phone. Crouch is not part of the movement vocabulary.

## Open Issues / Next Pass

Short-term implementation checks:

- Verify build `0.8.3` in live Android browser after cache-busted reload.
- Check that the newly added side portals and loop connectors do not create wall collision traps.
- Inspect whether room-level open portals make rooms feel too porous; if so, move to socket-specific portals.
- Confirm diegetic light source count is not too expensive on Android.
- Re-test central spire collision and top-platform support.
- Revisit enemy behavior; level generation currently leads architecture, while enemy placement is still simplistic.

Design next steps:

- Convert room bible into data: traversal sentence, room question, toy, landmark, threat, tactical choice, memorable image.
- Make each room archetype emit explicit sockets with local position, direction, height, and intended connector type.
- Add authored seed templates for known-good room graph shapes, starting from the triple-bridge skull guillotine hall pattern.
- Add affordances: shove/kick hazards, spike walls, ledges, traps, collapsing platforms.
- Give the player a destination/goal in each generated level, not only room traversal.



## Recovered Quake-Style Level Generation Notes

A later correction recovered missing session knowledge: the earlier procedural approach was drifting into boxes with junk in them. That is not the target. Quake-style level generation for this project should start from route grammar, not prop scatter.

Current accepted direction:

- The authored skull guillotine hall / triple-bridge room is the current reference point. It has a central bridge commitment, side galleries, upper crossing, visible focal threat, and recovery/alternate routes.
- Future rooms should be generated as traversal lines: acceleration runway, timing lip, jump/air-steer gap, bridge or landing target, side recovery path, and visible next goal.
- Dress the movement sentence after it works. Rubble, chains, pillars, and decorative blocks should support silhouettes and cover, not become random junk.
- No crouch movement verb. The earlier crouch-slide idea is superseded. Bunny-hop feel is merged into running jump, buffered jump timing, bridge/ramp/stair lips, and air steering.
- Level templates should include explicit speed lines and safe recovery lanes so touch players can learn the route without a keyboard/mouse control burden.

## Source Anchors

- Runtime: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/src/main.js`
- Entry: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/index.html`
- Project orientation: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/PROJECT_ORIENTATION.md`
- FPS arm asset manifest: `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/assets/asset_manifest.json`
- Precursor brainstorm: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/session_learnings/2026-06-07_fps_platformer_arcane_ik_brainstorm.md`

## Baked-Look Mobile Lighting Pass

Build `0.4.6` changed the diegetic lighting from many runtime point lights to fake baked lighting: dynamic shadows are disabled, per-brazier point lights are disabled by default, visible flame/corpsefire meshes remain, and cheap transparent floor glow pools provide route readability. Re-enable real lights only for controlled desktop capture or a much smaller light budget.


## Build 0.7.1 Skybox And Granular Texture Pass

A 2026-06-08 Android screenshot showed two visual failures: the black void behind architecture needed world context, and the active Delaunay material maps read as giant triangles rather than stone. Build `0.7.1` tried to address that with a follow-camera Limbo sky dome and `*-granular-*` texture siblings.

A follow-up screenshot rejected that direction: the granular textures still read as bitmap material pasted onto simple low-poly geometry, and the procedural sky still had too much gradient/bitmap feel. Treat `0.7.1` as a superseded visual experiment, not the current material direction.

Texture lesson from the failed pass: do not solve Infinite Brutality material readability by adding more raster detail. Stone should be authored as flat, hard-edged low-poly/vector material art that matches the mesh language.

## Build 0.7.2 Vector Material Sheet Pass

A follow-up Android screenshot showed the `0.7.1` granular textures still read like bitmap material pasted onto simple low-poly geometry. The correct direction is not another generated raster request: use actual vector/SVG source textures with flat polygon fills and hard seams, then let WebGL rasterize them only at texture-upload time.

Build `0.7.2` adds a project-owned vector material set: `ib-vector-stone-20260608.svg`, `ib-vector-bronze-20260608.svg`, `ib-vector-bone-20260608.svg`, `ib-vector-limbo-sky-20260608.svg`, and review sheet `ib-vector-material-sheet-20260608.svg`. These SVGs avoid gradients, filters, photographic grain, and image-gen bitmap source. Runtime material loading now points at the SVG assets.

Design rule: for Infinite Brutality, texture art should be authored like low-poly/vector game art. Stone can be tiled slabs and hard cracks, bronze can be flat plates, bone can be shard shapes, and the sky can be flat bands/spires. Avoid raster material realism unless the mesh style becomes equally detailed.


## Quake Route Grammar Training Pipeline

A sequential route-grammar extractor now exists at `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/tools/quake_route_grammar.py`. It accepts local `.map`, `.bsp`, Quake `.pak`, and `.pk3`/`.zip` sources and emits abstract route templates only. Do not commit or redistribute original Quake level data or copied layouts.

The legal Quake map-source archive has now been pulled into Thunder external sources, and the extractor trained 41 playable maps while retaining 22 item/prefab sources as metadata. The generated curriculum remains abstract: route sentences, feature counts, archetype counts, and generator biases only. Infinite Brutality should use these as ML level-design lessons, not as copied layouts.

Key learned biases: visible vertical layering, long acceleration lanes before timing lips, route-change gates with physical returns, pickups/enemies as breadcrumbs after the traversal sentence is valid, and no crouch vocabulary. The strongest archetype is gate_loop_return, but the implementation target remains new Infinite Brutality rooms anchored by the triple-bridge hall language.


## Build 0.7.3 Measured Quake Room Pass

Build `0.7.3` converts the active authored room away from the oversized gold hall into a compact measured Quake-style route space. The room footprint is now `24 x 36` instead of `38 x 60`, with a short entry read, runway lip, three offset bridge commitments, west recovery/gallery stair, upper crossing, east drop recovery, and visible skull exit gate.

Design lesson: keep the room tight enough that the player can understand the whole sentence from spawn. Movement should matter through lip timing, lateral air correction, narrow bridge commitment, and recovery-route choice. Props remain as landmarks: execution block at start, deadfall over the first commitment, corpsefire for recovery/exit reads, and skull gate at the goal. Do not expand this back into a giant hall unless the route sentence gains a real second loop.


## Room Junction Batch Planning

After the build `0.7.3` screenshot, the visual language is considered strong enough for overnight room batching: flat vector stone, bronze bridge slabs, bone/skull gate landmarks, dark chunky walls, and corpsefire route markers. The next bottleneck is topology coverage.

Room batching should distinguish authored prompt coverage from runtime frequency. Prompt coverage should be generous for one-connector terminals because terminals carry starts, exits, switches, secrets, rewards, traps, and vistas. Runtime generation should mostly use two-connector workhorse rooms, with three-connector junctions for loops/choice and four-connector hubs kept rare.

Project outputs:

- `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/docs/ROOM_JUNCTION_BATCH_LIST.md`
- `/storage/emulated/0/Documents/GodotProjects/infinite-brutality/data/room_junction_batch.json`

Batch coverage: 48 specs total: 14 one-connector terminals, 20 two-connector workhorses, 10 three-connector junctions, and 4 four-connector hubs.


## Build 0.7.4 Panorama Skybox Pass

A screenshot of build `0.7.3` showed the room visual language working, but the view beyond the gate still read as pure black. Build `0.7.4` adds `assets/textures/ib-vector-limbo-panorama-20260609.svg`, a project-owned flat vector panorama for the sky dome: distant walls, spires, bridge silhouettes, underworld color bands, and a non-black horizon.

Important implementation lesson: the old sky material color was dark and multiplied the SVG map, crushing the panorama toward black. The texture load path now sets sky material color to white after loading the SVG. Keep future sky art in the same vector/panorama direction; avoid starscape unless the fiction changes.


## Build 0.8.0 Generated Room Batch Runtime

The overnight room batch is now wired into runtime. `data/room_junction_batch.json` remains the source prompt/spec list, while `src/generated_room_batch.js` is the generated browser module with all 48 specs. `src/main.js` imports the batch, generates compact blockouts from connector signatures and semantic roles, and advances to the next room when the player reaches the exit marker.

Implementation compromise: the 48 rooms are generated from shared topology rules rather than hand-authored one by one. This is intentional for breadth and overnight productivity. Morning review should identify which generated blockouts deserve bespoke authored exceptions or silhouette fixes.


## Build 0.8.1 Real Bitmap Skybox

A real bitmap skybox has been generated and wired for Infinite Brutality: `assets/textures/ib-real-limbo-skybox-20260609.png`. The source was the built-in image generation output under Codex generated_images, then locally center-cropped/resized to `2048x1024` for the sky dome. The image gives the space a distant Limbo panorama with gothic walls, spires, bridges, red underworld haze, and sparse corpsefire accents.

This is now the runtime skybox path in `src/main.js`; the prior SVG panorama remains as a project-owned fallback/reference asset but is no longer the active sky texture.


## Build 0.8.3 Physical Gauntlet And Z-Fighting Fix

A fresh Android screenshot showed build `0.8.1` had collapsed the room batch into repeated one-bridge rooms with z-fighting. The generated-room baseline was wrong: every spec started from a central chasm/void and layered bridge slabs over the same floor planes. The user also rejected teleporting between rooms.

Build `0.8.3` fixes the generator baseline: floor-first compact chambers, no default giant side void, raised pads/route markers to avoid co-planar surfaces, and narrow gutter accents only for routes that actually call for bridge/gap/hazard timing. It also builds all 48 generated rooms into one continuous physical gauntlet with connector spans between adjacent room exit/spawn points. Ordinary room exits no longer teleport to the next room; only the final gauntlet exit wraps the run.
