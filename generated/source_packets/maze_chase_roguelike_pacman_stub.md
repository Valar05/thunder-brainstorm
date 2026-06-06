# Source Packet Stub: Arcade Maze-Chase Roguelike

## Working Offer

Make an arcade maze-chase roguelike inspired by the mechanical feel of classic Pac-Man: a tight maze, constant pursuit, route planning under pressure, temporary predator/prey reversal, collectible objectives, and scoring tension. Do not use Pac-Man names, characters, sprites, mazes, sounds, or trade dress. Treat the source as a rules inspiration, not an asset or content source.

## Core Arcade Spine

The base game loop to preserve in abstract form:

1. Player enters a fixed-screen maze.
2. The maze contains many small required collectibles and a few powerful reversal pickups.
3. Several pursuers patrol/chase using distinct movement priorities.
4. Normal contact with a pursuer costs a life/run state.
5. Reversal pickups temporarily make pursuers vulnerable and turn chase pressure into a scoring/opportunity window.
6. Bonus items appear briefly and reward risky route changes.
7. Clearing required collectibles advances the level.
8. Later levels increase speed, reduce reversal safety, and demand stronger route mastery.

## Roguelike Mutation Goals

Convert memorized arcade routing into run-based tactical variation without losing immediate readability.

- Maze changes each floor, but remains tile-readable and route-plannable.
- Pursuers keep stable identities across the run, but their rules mutate.
- Power reversal remains rare, legible, and timed.
- Clearing the board is still the main objective, but optional greed creates risk.
- Upgrades should change routing decisions, not only stats.
- Death should feel like a route/planning failure, not random ambush.

## Theme Overlay Slots

Pick one theme layer before content drafting. The mechanic should survive theme changes.

1. **Plague Monastery**: player is a novice collecting sealed prayers while hunger-spirits patrol cloisters.
2. **Scrap Cathedral**: player is a maintenance drone reclaiming charged rivets while security choirs hunt by sound.
3. **Dream Train**: player moves through sleeper cars collecting memories before conductors erase them.
4. **Sunken Signal Lab**: player gathers signal pearls while pressure shadows patrol flooded corridors.
5. **Fleshpunk Nerve Maze**: player harvests nerve sparks while immune hunters guard living junctions.

Recommended first theme: **Scrap Cathedral**, because it maps cleanly to pellets as charge, power pellets as breaker overload, ghosts as security routines, fruit as rare salvage, and roguelike upgrades as hardware modules.

## Mechanic Cards To Pull From Thunder Brainstorm

Use these existing pattern cards as inspiration, not limits:

- `pressure_arena_event_cloud`: each floor is a pressure arena with changing pursuer rules.
- `deck_pressure_run_manager`: floor modifiers, pursuer mutations, and bonus events can be drawn from small decks.
- `delayed_consequence_stack`: greed choices can create later patrol changes or locked gates.
- `touch_lane_combat`: if mobile, input must be lane/grid clean and buffer turns before intersections.
- `pursuer_rearm_gap`: after a hit, stun, or escape, pursuers need fair reset/rearm rules.
- `artifact_recipe_unlocks`: upgrades unlock from behavior evidence, not only random drops.
- `review_surface_browser`: a local viewer should show generated maze, pursuer rules, and floor modifiers.

## Roguelike Systems

### Floor Generation

Each floor should generate:

- Maze topology: loops, corridors, gates, safe pockets, and high-risk shortcuts.
- Collectible distribution: required charge nodes plus optional greed clusters.
- Reversal pickups: few, visible, and reachable by deliberate routing.
- Pursuer spawn/home zone: predictable enough to plan around.
- Bonus item spawn path: a temporary route challenge.
- Exit rule: all required charge nodes collected, or alternate exit unlocked by rare upgrade.

Generation constraints:

- Every required collectible must be reachable.
- There must be at least two meaningful loops around the center.
- No dead-end should contain required collectibles unless it is clearly high reward/high risk.
- Reversal pickups should not spawn adjacent to the player start.
- Early floors should teach pursuer personalities before stacking modifiers.

### Pursuer Personalities

Keep pursuers readable through distinct rules:

1. **The Direct One**: favors shortest path to player.
2. **The Ambusher**: targets the tile ahead of the player, punishing autopilot routes.
3. **The Flanker**: tries to cut off escape routes or patrol intersections.
4. **The Erratic One**: alternates between chase and scatter, creating uncertainty but not pure randomness.

Roguelike mutations:

- One pursuer can gain a modifier each floor: faster on straightaways, pauses at gates, ignores one wall type, guards bonus items, shadows power pickups, or splits into a delayed echo.
- Mutations must be announced with an icon/short label before the floor starts.
- Never mutate all pursuers at once in early floors.

### Player Upgrades

Upgrades should change route planning:

- **Buffered Turn Plus**: queue one turn earlier at intersections.
- **Static Decoy**: drop a short-lived lure at a junction.
- **Breaker Bite**: reversal pickup lasts less time but grants a burst after eating a pursuer.
- **Greed Magnet**: nearby small collectibles pull in, but pursuers hear the charge.
- **Gate Key**: pass through one locked gate per floor.
- **Echo Step**: first lethal contact per floor rewinds the player three tiles, then disables.
- **Cold Circuit**: pursuers rearm slower after being eaten, but reversal pickups are rarer.

Bad upgrades to avoid:

- Flat speed only.
- Flat score only.
- Invisible probability changes.
- Upgrades that remove pursuit pressure entirely.

### Scoring And Run Pressure

Scoring can become roguelike pressure:

- Small collectibles: baseline progress.
- Chain bonus: collecting continuously without reversing direction.
- Reversal chain: eating multiple vulnerable pursuers during one reversal window.
- Greed clusters: optional high-risk zones.
- Bonus salvage: appears briefly and changes route priorities.
- Floor debt: leaving optional clusters may reduce reward, but over-greeding risks death.

Run meta should track:

- floor number
- lives or core integrity
- upgrade modules
- pursuer mutation history
- greed debt / salvage streak
- unlocked maze tile types

## Tile And Modifier Ideas

Tile types:

- Normal corridor
- Slow sludge / friction wire
- One-way current
- Gate door
- Alarm tile
- Cracked wall shortcut
- Safe alcove with no collectibles
- Bonus lane
- Pursuer-only tunnel

Floor modifiers:

- Lights flicker: reveal pursuer intent only near intersections.
- Overcharged maze: reversal pickups last shorter but recharge one gate.
- Alarm floor: collecting greed clusters increases chase speed briefly.
- Broken map: some pellets are decoys; clear by listening/marking.
- Flooded corridors: player and pursuers slide until an intersection.

## First Playable Stub

Build the smallest testable version:

- 21x21 tile maze or similar compact grid.
- One player.
- Four pursuers with distinct target rules.
- Required collectibles.
- Four reversal pickups.
- One bonus item spawn.
- Three upgrades chosen between floors.
- Five generated floors.
- Debug overlay showing each pursuer target tile and current mode.

## Validation Plan

Before content polish, validate:

1. All collectibles are reachable.
2. Player can clear floor without relying on random pursuer behavior.
3. Pursuer modes are visible in debug overlay.
4. Reversal timer and vulnerability state are readable.
5. Generated mazes have loops and avoid unfair dead-end requirements.
6. Upgrades alter routing decisions in at least one observable way.
7. A floor seed can be replayed exactly for debugging.

## Source-Packet Prompt For A Writing/Design Agent

Draft a themed arcade maze-chase roguelike using the **Scrap Cathedral** theme. Preserve the mechanical spine of an arcade maze chase: required collectibles, distinct pursuers, temporary reversal pickups, bonus item route temptation, and escalating floor pressure. Do not use Pac-Man names, sprites, mazes, sounds, fruit identities, or trade dress. Output structured JSON-like design notes with: `theme_pitch`, `tile_types`, `pursuer_personalities`, `floor_modifiers`, `player_upgrades`, `scoring_rules`, `first_playable_scope`, and `validation_checks`. Keep all mechanics readable on a small grid.

## Open Questions

- Should the run be real-time arcade, turn-based roguelike, or tick-based simultaneous movement?
- Should upgrades persist only for a run, or unlock into a meta pool?
- Should generated mazes be fully procedural, hand-authored chunks, or hybrid chunk assembly?
- Should combat only happen during reversal windows, or can upgrades create other limited interactions?
- Should the theme be cute, grim, industrial, religious, fleshpunk, or abstract arcade?
