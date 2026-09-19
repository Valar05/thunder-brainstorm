# Diorama of Descension → Diorama Descent — Recombinant Combat/Route Lineage — 2026-09-19

## Two distinct repositories

Old source game:
- https://github.com/Valar05/diorama-of-descension
- Godot title: **Diorama of Descension**

Recombinant successor:
- https://github.com/Valar05/diorama-descent
- Godot title: **Diorama Descent**

Do not collapse the two names into one project.

## What Diorama of Descension actually contributes

The older game is a 2D sprite character-action system with:
- five-hit light string ending in `SlashDown`;
- hold-driven heavy branches whose result depends on combo depth;
- `Boot` as its own beat before a separate follow-up input;
- launcher, heavy stab, multistab, cross slash;
- dash meter;
- dash slash;
- parry;
- kick;
- coordinated enemy attack ownership.

This is not merely "sprite combat." It already contains several recurring Drew design signatures.

### Motion commits the outcome

The README explicitly preserves a subtle but important parry rule:

> parry bounce follows the **original dash course**, not the enemy position.

The player commits to a trajectory. Contact does not erase that history and snap the result to the target.

That is an early clean specimen of:

> **MOTION HAS MEMORY.**

and it fits the later cross-project law:

> **MOTION IS NOT TRANSPORTATION. MOTION IS THE ACTION SYSTEM.**

The older game's movement/combat coupling also includes:
- stick-edge / flick dash detection;
- slash dash;
- dash-meter bonus damage;
- successful parry immediately filling the dash meter;
- parry triggering a `SlashDown` follow-up;
- attack direction preferring recent dash/movement direction.

Movement state is not just where the character is. It is part of combat authority.

## Input is grammar, not button count

Diorama of Descension's combat surface is unusually grammatical:
- tap;
- hold past threshold;
- buffered hold during active light;
- combo depth;
- Boot pause;
- separate follow-up tap;
- swipe direction;
- joystick direction;
- dash commitment.

The important pattern is not "lots of gestures." It is that **timing and motion state change the meaning of the same small input surface**.

Compact law:

> **COMPRESS INPUTS; EXPAND MEANING THROUGH STATE.**

This rhymes with later low-button work even though this game is much more explicit/action-heavy than Armored Bus Stop or Redneck Zombie Shotgun Turtles.

## Enemy pressure is composed

`ai_conductor.gd` proves that enemies are not intended to become a pile of simultaneous attackers.

The conductor:
- chooses one attack owner;
- parks other enemies in support slots around the player;
- discourages the last attacker from immediately owning the next turn;
- pushes wounded enemies away from attack ownership;
- sends wounded enemies into flee behavior;
- retains/assigns stable support positions instead of letting every enemy dogpile.

This gives another reusable law:

> **ENEMY COUNT IS NOT PRESSURE. PRESSURE IS CHOREOGRAPHED ACCESS TO THE PLAYER.**

That later matters anywhere Drew wants "many bodies" without unreadable dogpiling.

## Diorama Descent is explicit capability recombination

The successor repo states directly that it is built from:
- **Diorama of Descension** for slash combat, sprite characters, and background language;
- **SteamPile** for action highlighting and procedural map-generation feel.

This is unusually valuable lineage evidence because the recombination is documented by the project itself rather than reconstructed after the fact.

The source manifest mirrors both donors locally.

So this project is a literal example of the broader lineage law:

> **THE PROJECT DIES. THE CAPABILITY MIGRATES.**

and adds a stronger variant:

> **CAPABILITIES FROM DIFFERENT DEAD PROJECTS CAN BREED.**

## What SteamPile contributes

The SteamPile donor is source-backed, not speculative.

Its map runtime includes:
- a bounded grid;
- generated critical path;
- branches;
- carved rooms;
- path-length targets;
- highlights for player influence / walkability / rock interaction;
- enemy highlights;
- procedural route construction.

Diorama Descent names this donor directly.

So the recombinant sentence is:

```text
STEAMPILE
route grammar
+ procedural critical path / branches / rooms
+ highlighted spatial intention
        ×
DIORAMA OF DESCENSION
sprite combat
+ directional attack grammar
+ dash/parry trajectory
+ choreographed enemy pressure
        ↓
DIORAMA DESCENT
3D board + sprite bodies
movement telegraphs
approach-angle initiative
close-range slash combat
```

## Navigation becomes combat state

The successor concept contains the strongest mutation.

Its planned flow says:
- grid movement;
- enemies preview next move;
- contact triggers a clash;
- **approach angle determines who receives the free hit**;
- then camera transitions into close combat;
- swipes drive directional slashes.

That means the board is not merely how you reach combat.

Your route into contact **preloads combat advantage**.

Compact law:

> **APPROACH IS PART OF THE ATTACK.**

This is another version of Drew's repeated preference for making movement carry consequence instead of resetting into a separate combat mode with no memory of arrival.

## Current implementation boundary

The current `diorama-descent` Phase 1 is still an early slice.

Implemented:
- 3D board;
- sprite player;
- grid movement;
- direction filtering;
- enemy move preview;
- basic sprite facing.

Still documented as not yet in that slice:
- close-combat slash attacks;
- clash damage resolution;
- full procedural dungeon generation;
- multiple-enemy combat groups.

Do not report the whole concept as already implemented.

## Retrieval handles

- Diorama of Descension;
- Diorama Descent;
- SteamPile donor;
- motion has memory;
- parry bounce original dash course;
- Boot gets its own beat;
- combo-state input grammar;
- AI conductor;
- one attack owner;
- support slots;
- wounded enemies flee;
- approach angle free hit;
- navigation becomes combat state;
- capabilities from different dead projects can breed.
