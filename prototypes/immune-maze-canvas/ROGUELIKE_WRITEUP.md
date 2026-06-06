# Marrow Runner Roguelike Writeup

## Current Identity

Marrow Runner is becoming a mobile-first immune-cell maze chase game. The base language is Pac-Man: collect all pickups, survive roaming enemies, trigger a temporary power state, and exit through a gate. The difference is that the game is no longer trying to be a clean grid maze. It should feel like navigating living tissue: blobby chambers, narrow capillaries, infection nests, suction, ramming, and cellular pressure.

The player is a phagocyte moving through an organic tissue maze. The core verbs are:

- collect antibodies
- vacuum nearby pickups
- collect complement power
- ingest enemies during complement
- use Pseudopod Ram from rest to launch enemies into walls or other enemies
- cleanse the infection nest after all antibodies are collected
- reach the lymph gate to descend

The latest direction is roguelike structure on top of a readable arcade base: each run has a seed, every level is deterministic for that seed and depth, and advancing increases pressure through enemy count and enemy archetype variety.

## Why It Was Feeling Samey

The previous roguelike pass saved and replayed seeds, but most of the layout was still anchored by fixed percentage positions. The seed changed organic noise and small texture variation, while the big landmarks still appeared in familiar places. That made new runs technically different but perceptually the same.

The current fix moves seed influence into the macro layout:

- marrow start can appear anywhere on the grid, not only the upper-left area
- lymph exit can appear anywhere on the grid, not only the lower-right area
- start and exit use separation scoring so they stay meaningfully apart
- infection, complement, and one extra room are seeded by scatter placement instead of fixed bands
- room placement rejects tight overlaps and favors different spatial compositions
- corridor graph archetypes are seeded: spine, hub, fork, or loop
- corridor links are seeded inside each graph archetype
- infection nest and complement chamber remain guaranteed
- the HUD shows the active run seed

This preserves replayability: same seed plus same depth produces the same layout, but New Run now changes the whole screen composition instead of merely nudging familiar anchors.

## Core Loop

A level should read in three phases.

1. Forage

The player enters from the marrow pocket and starts sweeping antibodies. This should feel quick and tactile. The joystick is radial and responsive, not strict gridlock, but the maze still needs enough structure to make route choice matter.

2. Survive and Exploit

Enemies emerge from the infection nest and path through the tissue. The player can avoid them, use complement to ingest them, or line up Pseudopod Ram chains. Ram is not a direct attack by itself; it launches enemies. Kills happen when knocked enemies hit walls or other enemies.

3. Cleanse and Exit

Once all antibodies are collected, the infection zone visibly neutralizes. This is the level-complete emotional beat before the player reaches the lymph gate. The gate then advances the run to the next depth.

## Movement Feel

The current movement has shifted away from classic stepped Pac-Man movement into free radial movement with grid assistance. That was the right direction for touch feel. The player should not feel like they are fighting exact tile alignment, but the maze still needs to reward intentional turning.

Current movement principles:

- full-screen touch input, no separate joystick button required
- strong movement response even at imperfect thumb magnitude
- fast turning toward the current input direction
- helper logic that pulls movement toward usable gaps and corners
- tile collision still defines the maze, but control should feel analog

The remaining movement risk is gap precision. If corridors are too narrow or too straight, mobile play feels fussy. The organic generation should prefer two-wide approaches into occasional one-wide throats, not long one-tile hallways.

## Pseudopod Ram

Pseudopod Ram is the signature control mechanic. It gives the phagocyte an immune-cell physicality instead of making it only a Pac-Man reskin.

Rules:

- Ram arms when input magnitude drops below 0.25.
- Initial movement from rest triggers a short burst.
- During the burst, the player uses frame 4.
- Direct ram contact launches an enemy, but does not instantly kill it.
- A knocked enemy dies if it hits a wall.
- A knocked enemy dies if it hits another enemy.
- The hit enemy should be launched onward, enabling recursive chains.
- Complement overrides this: complemented player contact/vacuum ingests enemies directly.

Design goal: ram should create planned, readable violence. It should feel like lining up a shove through an infection cluster, not like a melee attack button.

## Pickups and Complement

Antibodies are the level-clear objective. They should be numerous enough to create route planning, but not so dense that every tile is a dot. The antibody vacuum helps reduce cleanup friction and also creates an upgrade hook.

Complement is the power state. It should be rare enough to matter and placed so the player makes a timing decision. Complement pickups are suckable, matching the antibody vacuum language. During complement, enemies can be vacuum-ingested, but suction should respect walls so it does not feel unfair or visually wrong.

Possible future upgrade hooks:

- longer antibody vacuum range
- complement pickup vacuum from farther away
- stronger enemy suction during complement
- ram rearm threshold becomes more forgiving
- ram chain hitbox becomes wider
- cleanse wave gives a temporary shield at next depth

## Enemy Archetypes

The game needs the ghost archetypes represented, but they should feel like infection behaviors rather than literal ghosts.

Current planned set:

- Pursuer: targets the player directly.
- Ambusher: targets ahead of the player's movement vector.
- Flanker: pressures from side offsets.
- Wanderer: drifts around the player with less direct pursuit.

Run structure should start simple and add variety over depth:

- Depth 1: pursuer only
- Depth 2: add ambusher
- Depth 3: add flanker
- Depth 4+: add wanderer

Enemy count increases with depth, capped to prevent unreadable clumps. Enemies should spawn from the infection nest, not the exit. The nest is the ghost-cage equivalent: a high-risk, visually marked area the player can learn and exploit.

## Map Generation

The maze should feel grown, not built. Current generation uses organic room blobs and wavy corridors, but the target is stronger:

- no long rectangular corridors when avoidable
- contiguous wall and floor masses
- cellular noise on edges
- chambers with irregular silhouettes
- neckdowns that make tactical chokepoints
- enough loops to prevent one-corridor play
- no huge barren rooms on phone
- no dense unreadable clutter on desktop

Responsive grid sizing remains important:

- phone portrait: around 18 columns, taller maze
- tablet: intermediate grid
- desktop: wider landscape maze

The same room count can work across form factors, but room scale and corridor width need responsive tuning.

## Visual Direction

The art direction should be fleshy cellular tissue, not abstract swooshes or flat MS Paint color. The player sprite sets the style target: readable, crisp, biological, a little gross, but not noisy.

Sound direction:

- Build one sound at a time against a named gameplay event.
- Prefer local synthesis for tiny UI/game-feel sounds to avoid licensing ambiguity.
- If online fair-use or Creative Commons sounds are layered in later, keep attribution and source URLs with the asset manifest.
- Eat antibody target: short wet organic pop plus bright immune glint, fast enough for repeated pickups.

Visual priorities:

- dark floor with subtle tissue texture
- red/pink fleshy walls with vein detail
- contiguous masked texture, not obvious repeated square tiles
- irregular wall boundaries with cellular edge noise
- clear infection nest indicator
- enemies should look cellular/pathogenic, not capsule cartoons
- cleanse effect should visibly neutralize infected tissue

The generated background and sprite sheet are placeholders for direction, not final art. They are useful because they pushed the prototype away from flat procedural color, but the enemy art still needs stronger matching to the phagocyte style.

## Roguelike Structure

Runs are seed-based and saved to localStorage. A seed should be a promise: replaying it gives the same room layout at the same depth.

Menu behavior:

- New Run generates a fresh seed and starts at depth 1.
- Tutorial is a standalone main-menu item. Completing it returns to the menu and satisfies the first-run tutorial check.
- The first New Run prompts the player to play a tutorial before entering that generated seed only if tutorial has not been completed or dismissed.
- The tutorial teaches movement, Pseudopod Ram, knockback kills, and chain reactions in a prepared training tissue scene.
- Dismissing the first-run prompt or completing the tutorial marks it resolved in localStorage.
- Resume continues the active seed and depth.
- Replay Seed starts an old seed from depth 1.
- Advance increases depth on the current seed.

Depth should modify:

- enemy count
- enemy archetype pool
- possible room variants
- pickup density or complement availability
- infection nest intensity

Depth should not destroy readability. The game should get more dangerous through pressure and composition, not just by filling the map with enemies.

## Current Technical State

The prototype is dependency-free HTML canvas in `prototypes/immune-maze-canvas/`.

Audio is handled by one persistent shuffled music player. It starts from the first user input/start/tutorial action to satisfy browser autoplay rules, then keeps playing across menu, death, restart, tutorial, and seed transitions. It can be disabled from the HUD/canvas music control or `M`; the disabled preference is saved. Page Visibility and page lifecycle events pause playback when the browser tab/app is backgrounded and resume it only if it was playing before.

Important files:

- `index.html`: canvas shell and desktop HUD
- `styles.css`: responsive/fullscreen layout
- `src/main.js`: runtime, generation, input, enemies, rendering, menu, seed logic
- `harness.html`: browser-based canvas harness
- `assets/asset_manifest.json`: generated asset record

Known validation:

- `node --check src/main.js` catches syntax regressions.
- `python -m http.server 8787` serves the prototype.
- `harness.html` can inspect basic canvas/runtime state.
- Deterministic smoke checks can compare zone signatures for seed stability.

## Immediate Next Decisions

1. Art pass

The biggest presentation gap is enemy and tissue cohesion. The next art pass should replace the capsule-like enemy look and improve fleshy texture/boundary integration.

2. Generation pass

Now that macro seed variation exists, tune organic maze quality. Focus on room scale, neckdowns, loops, and avoiding both barren phone maps and generic corridor maps.

3. Enemy feel pass

Enemies need faster, clearer pathing without clumping. Their spawn timing and nest telegraph should make the infection area feel risky but understandable.

4. Run progression pass

Add roguelike upgrades or mutations only after the base loop feels good. The strongest candidates are vacuum range, ram chain forgiveness, complement duration, and temporary shields.

5. Documentation and harness pass

The canvas harness should include seed controls, deterministic layout comparison, and a few visual snapshots so we can prove New Run is changing the map without relying on manual screenshots every time.

## Design Position

The best version is not pure Pac-Man and not pure roguelike maze soup. It is an arcade chase game with a roguelike run wrapper and a distinctive immune-cell control mechanic.

Classic structure gives readability:

- collect all dots
- avoid enemies
- power up and reverse the threat
- exit the level

Mutations give identity:

- organic tissue maps
- suction pickups
- complement ingestion
- Pseudopod Ram chains
- infection nest cleanse
- seeded depth progression

The base should stay simple enough that a player understands a run in seconds. The weirdness should come from the biological verbs and escalating infection composition, not from complicated rules.
