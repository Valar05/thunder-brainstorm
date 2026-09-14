# Armored Bus Stop — Endless Pressure + Behavioral Adaptation

## Playtest decision
The map is no longer the progression axis. Combat is the level; **time is the difficulty clock**.

A finite-looking battlefield can recycle objectives indefinitely. This avoids spending design budget on terrain breadth before the combat system needs it.

## Implemented run spine
- Pressure increases every 42 seconds.
- Active engagements receive reinforcements at an interval that contracts with run time.
- Later pressure introduces differentiated enemy roles (ordinary infantry, suppressive gunners, flankers, heavies) rather than only inflating HP.
- Recovered objectives relocate and reseed defenders, so the three visible objective slots can sustain an endless run.
- The run ends when the carrier or squad is lost, not after consuming three authored points.

## Procedural commandos
The squad adapts from what it actually did instead of opening an upgrade-menu interruption.

The mod surface is the commando lifecycle itself:

EMBARKED -> LAUNCH -> AIRBORNE -> LAND -> FIGHT -> RECOVER

Current adaptations:
- **Sky Gunnery** — improves airborne firing cadence, range, suppression, and damage.
- **Boot Meteor** — turns landing into a localized shock/damage event.
- **Hobo Hook** — after sufficient successful recoveries, returning commandos can throw themselves back into a moving APC, deliberately earning the right to violate the normal stopped-ingress rule.

Selection is weighted by observed run behavior (air shots/kills, landing contacts, recovery history), so capability can crystallize from how the squad was actually used.

## Useful design rule
> Do not procedurally mutate only numbers. Mutate phase transitions.

Launch conditions, airborne behavior, landing consequences, ground doctrine, and recovery rules are all higher-value procedural surfaces than generic +10% damage upgrades.

## Current sentence
**Time makes the enemy worse. Combat makes the squad stranger.**
