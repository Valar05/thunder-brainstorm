# InfiniteBrutality (capitalized) — Ancestral Cathedral and Two-Generation Transmission — 2026-09-19

## Identity boundary

This note concerns the old Godot repository:

- https://github.com/Valar05/InfiniteBrutality
- repository name: `InfiniteBrutality`
- Godot project name: `InfiniteBrutality`

Do not silently collapse it into the later browser/Three.js repository:

- https://github.com/Valar05/infinite-brutality

Drew identifies them as generations in one design lineage, not the same checkout.

## Drew's corrected chronology

Drew remembers **two important old Infinite Brutality generations before the modern lowercase project**:

### Generation 1 — tunnel-maze Infinite Brutality

The earliest Infinite Brutality was the **tunnel / maze** version.

Drew remembers it as a piecemeal dungeon/tunnel-maker style game and had previously wondered whether voxel terrain belonged to this period.

The currently surfaced capitalized GitHub `main` does not prove that generator. Preserve this as firsthand history and an archaeology target rather than forcing the current flat-arena snapshot to stand in for the first generation.

Status:

`GEN_1_TUNNEL_MAZE = FIRSTHAND_CONFIRMED / SOURCE BODY NOT YET RECOVERED`

### Generation 2 — climbing / embodied-combat Infinite Brutality

The next major generation was the **climbing** version.

This is strongly consistent with the surviving capitalized repository. Its `Player.tscn` contains:
- `Climbing`;
- `ClimbingSide`;
- `Mantle`;
- jump / land / run / walk states;
- a large first-person melee animation library.

Drew identifies this climbing generation as the version whose capabilities were inherited into the modern lowercase Infinite Brutality.

Status:

`GEN_2_CLIMBING = FIRSTHAND_LINEAGE + SURVIVING_ASSET_EVIDENCE`

## The ancestral first-person combat cathedral

The surviving old repo proves a much richer combat body than a simple prototype.

`Player.tscn` imports `Models/FPSPlayer.glb` and exposes:
- fist attacks 1-5;
- sprint, air, crouch, and power fist attacks;
- block / blocking / parry / injury states;
- `FistThrow`;
- `KickParrySpecial`;
- `KickPushAttack`;
- knife attacks 1-4 plus directional / air / neutral power attacks;
- one-hand attacks 1-5;
- wand fire;
- climbing, side-climbing, mantle, jump, land, run, and walk states.

`FistController.tres` proves an active five-hit fist chain, sprint attack, block states, and a parry transition into `KickPushAttack`.

`Player.gd` proves:
- five-step combo progression;
- hitbox windows;
- transition windows;
- stamina;
- hold-to-block;
- an early 0.5-second parry window;
- damage interruption;
- post-attack movement slowdown.

`TouchCamera3D.gd` proves a phone-first touch grammar:
- left side = movement;
- right drag = look;
- quick right tap = attack;
- right hold feeds the block state.

`EnemyController.gd` proves real orc combat:
- navigation toward player;
- attack ranges / cooldowns;
- lateral strafing when blocked;
- attack hitboxes;
- directional hurt;
- attack interruption;
- death animation and cleanup.

This is why "ancestral cathedral" is the correct retrieval phrase: many later systems existed together here before Drew had the current production workflow for preserving and reusing them cheaply.

## Dark-Messiah-like physical combat

Drew remembers the game as physically vicious:
- kick orcs down;
- throw weapons at orcs;
- melee that felt unusually satisfying.

The surviving source directly supports the **kick** side:
- `KickPushAttack` exists as an active combat state;
- attack data gives `KickPushAttack` a 3x multiplier and invulnerability flag;
- parry can transition into the kick state.

The repository contains `FistThrow` plus large knife / one-hand weapon animation families, but the currently surfaced active controller does not independently prove the complete weapon-throw runtime.

Preserve:

`WEAPON_THROW = FIRSTHAND_CONFIRMED / COMPLETE CODE PATH UNRECOVERED`

## First-person arm transmission

The old repo directly imports:

`res://Models/FPSPlayer.glb`

Drew reports:
- these are the ancestral first-person arms;
- the old version wore metal bracers;
- he removed the bracers later to reduce the fantasy read.

The modern lowercase `infinite-brutality` repo explicitly documents `assets/models/FPSPlayer.glb` as its first-person arm / animation source copied through Pose Lab.

That yields a strong transmission chain:

```text
old InfiniteBrutality FPSPlayer
    ↓
bracer-removal / less-fantasy visual edit
    ↓
Pose Lab reusable arm lineage
    ↓
modern infinite-brutality
    ↓
future Taste Trap
```

The bracer-removal step is firsthand history. The old and modern `FPSPlayer` endpoints are source-backed.

Pocket law:

> **THE ARMS ARE OLDER THAN THE CURRENT GAME.**

## Climbing transmission is visible, not merely remembered

This is the key new archaeology result.

The old capitalized project contains authored climbing assets:
- `Climbing.res`;
- `ClimbingSide.res`;
- `Mantle.res`.

The modern lowercase project contains a live traversal model with:
- explicit `climbSurfaces`;
- player mode `climb`;
- climb attach / face offsets;
- vertical and horizontal climb speeds;
- mantle duration and forward displacement;
- detach / regrab timing.

So the transmission is not just "same vibe." A concrete capability family survives across generations:

```text
GEN 2 authored climbing / mantle
        ↓
reusable FPS arm + traversal vocabulary
        ↓
modern runtime climbing / mantle system
```

The implementation technology changed from Godot animation/state machinery to browser Three.js runtime logic, but the **capability survived the engine change**.

## Tunnel-to-climb-to-modern synthesis

Drew's corrected sequence suggests three distinct inheritances:

```text
GEN 1: tunnel maze
    contributes spatial ambition / dungeon circulation
            ↓
GEN 2: climbing cathedral
    contributes embodied traversal + FPS combat + arm vocabulary
            ↓
MODERN INFINITE BRUTALITY
    recombines generated spatial grammar + climbing/mantle + inherited first-person combat body
            ↓
TASTE TRAP
```

This is a strong example of Drew's project lineage behaving as **capability transmission rather than sequel repetition**.

The old project does not need to survive unchanged for its design work to remain alive.

Compact law:

> **THE PROJECT DIES. THE CAPABILITY MIGRATES.**

## Terrain / dungeon archaeology boundary

The current capitalized GitHub `main` surfaces:
- a flat arena/navigation plane in `game.tscn`;
- authored wall / ceiling / moulding / pillar OBJ geometry in `Environment.tscn`.

It does not presently prove the remembered Generation-1 tunnel maker.

By contrast, the modern lowercase project now has:
- carved voxel fortress terrain;
- generated room batches;
- district intent / assembly systems;
- route templates and room junction generation.

Do not back-project those modern systems into Generation 1 without evidence.

Keep:
`GEN_1_GENERATOR_IMPLEMENTATION = OPEN ARCHAEOLOGY`

## Why the cathedral was hard

Drew remembers regretting that he stopped working on this game, while also remembering that it was extremely difficult.

The source explains why.

It was simultaneously trying to own:
- phone-first FPS controls;
- camera look;
- combo combat;
- stateful blocking and parrying;
- stamina;
- movement-speed interaction with attacking;
- large authored animation libraries;
- multiple weapon families;
- climbing / mantling;
- enemy navigation and group pressure;
- reactive enemy combat;
- environment / level work.

This was a cathedral before the later workflow had cheap reusable infrastructure for all those domains.

That difficulty is not evidence the idea was wrong. It is evidence that too many expensive capabilities were coupled into one early build.

## Retrieval handles

Use these phrases to recover this note:
- ancestral cathedral;
- capitalized InfiniteBrutality;
- first tunnel maze;
- second climbing version;
- FPSPlayer arms;
- metal bracers;
- Dark Messiah kick;
- FistThrow;
- KickPushAttack;
- climbing transmission;
- the project dies, the capability migrates.
