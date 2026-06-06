# Maze-Chase Roguelike Idea Flow

## Working Direction

The best mutation is not "Pac-Man with random levels." It is a **route-pressure roguelike** where each floor asks: can you clear a readable maze while four known pursuer minds gain one new constraint?

The arcade spine stays:

- collect the board
- avoid pursuers
- use rare reversal windows
- route toward temporary bonus objects
- escalate speed and pressure

The roguelike layer changes:

- floor topology
- pursuer modifiers
- route-changing upgrades
- optional greed clusters
- deterministic seeds for replay/debug

## Three Viable Versions

### 1. Scrap Cathedral

Player is a maintenance drone reclaiming charged rivets in a cathedral-machine. Security choir routines hunt by pathing logic.

Why it works:

- pellets become rivets
- power pellets become breaker overloads
- ghosts become security routines
- fruit becomes rare salvage
- upgrades become hardware modules

This is the recommended first stub because it maps cleanly onto mechanics without needing heavy narrative.

### 2. Dream Train

Player moves through sleeper cars collecting memories while conductors erase the train's identity.

Why it works:

- maze chunks can be train cars
- bonus items can be passenger memories
- pursuers can patrol by car rules
- floors can feel like new train arrangements

Risk: train cars can make mazes too linear unless each car has loops and side passages.

### 3. Fleshpunk Nerve Maze

Player harvests nerve sparks in a living junction while immune hunters patrol.

Why it works:

- pellets become nerve sparks
- power pickups become adrenal surges
- pursuers become immune responses
- tile modifiers can be tissue states

Risk: the theme can obscure the clean arcade readability unless visuals are restrained.

## Core Logic Mutations

### Pursuer Mutation, Not Pursuer Replacement

Keep four stable personalities. A roguelike floor should mutate one or two rules:

- Direct pursuer gets faster on straight corridors.
- Ambusher predicts farther ahead.
- Flanker camps the closest greed cluster.
- Erratic pursuer leaves a delayed echo every eight ticks.

This preserves learnability while creating run variety.

### Greed Clusters

Normal collectibles clear the floor. Greed clusters sit in dangerous dead ends or alarm corridors. They are optional but buy upgrades.

Rules:

- Greed clusters should be visually marked.
- Collecting one can temporarily raise chase speed.
- Leaving them behind should be valid.

### Reversal Windows As Tactical Debt

The reversal pickup should not just make enemies edible. It can create post-window consequences:

- eaten pursuers rearm slower but return angry
- gate opens only if a pursuer is eaten
- reversal chain increases bonus but shortens future reversal windows
- overusing reversal adds floor debt

### Upgrades Must Change Routes

Good upgrades:

- turn earlier
- open one gate
- lure a pursuer
- rewind after first contact
- pull collectibles from nearby corridors
- mark hidden alarm tiles

Bad upgrades:

- +10 score
- +5 percent speed
- vague luck chance
- permanent immunity

## First Stub Recommendation

Use `Scrap Cathedral` and build:

- 21x21 tick-based grid
- deterministic chunk-assembled mazes
- four pursuers with debug target tiles
- rivets, breaker overloads, bonus salvage
- five floor modifiers
- six route-changing upgrades
- replayable floor seed

Start with simultaneous ticks rather than free real-time movement. It keeps arcade pressure but gives the roguelike logic room to be understood and debugged.

## Implementation Notes

If Godot:

- `TileMapLayer` or simple grid nodes
- one `RunManager`
- one `MazeGenerator`
- one `PursuerBrain` resource per personality
- one `FloorModifier` resource
- debug overlay toggled by key/button

If browser:

- canvas grid renderer
- JSON floor seed/config
- deterministic PRNG
- local storage for run state
- simple review view for generated maze and pursuer target tiles

## Next Source Packet Needs

The next packet should ask for one of:

1. a Godot implementation plan
2. a browser-canvas implementation plan
3. a JSON schema for floors, pursuers, upgrades, and modifiers
4. a first playable floor generator spec
5. a visual direction pass for Scrap Cathedral
