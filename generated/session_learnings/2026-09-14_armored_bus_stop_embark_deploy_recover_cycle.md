# Armored Bus Stop — Embark / Deploy / Recover Cycle

**Date:** 2026-09-14
**Status:** active brainstorm / candidate core loop

## Observation

The bus stop does not need to be the place where infantry dismounts. It may be more interesting if the bus stop is where personnel **embark into the carrier/convoy**, becoming carried capability rather than followers.

Combat, not the bus stop, becomes the deployment trigger.

```text
WAITING AT BUS STOP
-> carrier arrives / stops
-> EMBARKED
-> carrier moves through the world
-> combat becomes active
-> AUTO-DEPLOYED
-> fight
-> combat clears
-> RECOVERABLE
-> carrier must stop near survivors
-> EMBARKED again
```

## Critical constraint

Personnel **cannot re-enter while the carrier is still driving**.

Reboarding therefore requires a low-speed or stopped carrier near the surviving team after combat. Driving away leaves them on the ground.

This is important because it gives stopping a second meaning without adding a button:

```text
stop at bus stop -> load capability
stop after combat -> recover capability
keep moving -> leave that capability behind
```

## Why this is stronger than follower infantry

Followers make the infantry visually attached to the carrier but mechanically vague.

Embarked/deployed state makes custody explicit:

```text
carrier moving = protects + transports capability
combat contact = releases capability into terrain
carrier stopped after combat = offers recovery
carrier departure = commits to leaving survivors behind
```

The APC is therefore not simply a unit with nearby soldiers. It is a **mobile custody state machine**.

## Auto-deploy preserves the no-action-button grammar

The player still only drives.

No `DISMOUNT` button is required. Deployment can occur from a clear combat-state transition such as hostile commitment, incoming fire, or enemies crossing a bounded threat radius.

The interesting choice moves earlier:

> **Where and how do I drive into combat, knowing the people inside will inherit that geometry when contact begins?**

This preserves the earlier idea of aiming people at terrain, but moves it from bus-stop placement to **combat-entry geometry**.

## Recovery creates a real cost to continued motion

After a fight, continuing to drive is no longer neutral.

If the player wants the surviving fireteam back, the carrier must slow or stop near them long enough to board. If the player leaves immediately, the team remains behind.

That creates a clean decision without adding interface:

```text
STOP -> recover future capability
LEAVE -> preserve tempo / abandon or garrison present capability
```

Leaving a team behind does not have to be pure failure. In some situations it can become a persistent local force or garrison. The important rule is that **recovery is not free while moving**.

## Contact / Consequence / Adapt

```text
CONTACT
enter a bus stop or enter combat

CONSEQUENCE
people change state: waiting -> embarked -> deployed -> recoverable

ADAPT
choose route, combat-entry geometry, whether to stop for recovery, or whether to leave the team in place
```

## Compact rules

> **Bus stops load capability. Combat unloads it. Stopping recovers it.**

> **The carrier owns mobility; the infantry owns local combat.**

> **If you keep driving, the world is allowed to keep your soldiers.**

> **No new button is required because the meaningful transitions are already encoded in vehicle state and battlefield state.**
