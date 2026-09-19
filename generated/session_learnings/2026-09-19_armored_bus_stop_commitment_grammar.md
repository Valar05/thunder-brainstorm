# Armored Bus Stop — Commitment Through Motion

Captured: 2026-09-19  
Status: durable design extraction  
Primary source: current Armored Bus Stop V2 runtime/design documentation + Drew play/readback

## Existing project shape

Armored Bus Stop V2 is a phone-first one-stick combined-arms survivorlike centered on a wheeled APC.

Current loop:

`RAM -> GROW -> DEPLOY -> RECOVER -> FUSE -> COUNTER-EVOLVE`

The current project already contains doctrine progression, visible bus mutations, commandos, horde growth, telegraphs, combat engineering, fortifications, and a deliberately bounded phone-readable presentation.

This note captures the higher-level grammar revealed during play discussion rather than re-copying the README.

## The hinge: troops become verbs

The decisive design mutation was not "the APC can carry soldiers."

It was:

> What if those motherfuckers jump off the APC boots first?

Before that decision, carried troops can read as inventory.

After it, they become a physical action system:

```text
carrier approaches
-> troop commits
-> body leaves safety
-> body enters battlefield
-> contact/combat changes local state
-> physical recovery reattaches the troop to the carrier system
```

The launch creates animation, humor, risk, positioning, vulnerability, tactical timing, and recovery from one physical event.

Pocket law:

> **THEY DO NOT DISEMBARK. THEY COMMIT.**

## Commitment Through Motion

The game's apparently heterogeneous systems cohere because they repeatedly ask the same question:

**What does a moving body commit to, and what can still change before contact?**

Examples:

- gravel drift: steering is negotiation with retained momentum, not cursor translation;
- ram: vehicle trajectory becomes attack authority;
- commando launch: carried bodies become projectiles with agency after commitment;
- touch recovery: contact restores force composition;
- caltrops: reduce future mobility and change the cost of a route;
- barricades/funnels: rewrite the feasible trajectory set;
- telegraphs: communicate dangerous future geometry;
- doctrine hardware: makes build identity visible on the moving carrier itself.

This gives a useful action grammar:

```text
intent
-> trajectory
-> commitment
-> contact
-> altered option set
-> recovery or escalation
```

## One-stick pressure test

Armored Bus Stop's coherence comes partly from a severe implementation/design filter:

> Can this idea become physical at bus speed with one stick and no extra action button?

Ideas that survive this filter tend to become movement, geometry, contact, automatic deployment/recovery, or visible mutation rather than detached ability buttons.

That constraint compresses complexity instead of merely removing it.

## Battlefield authorship

Combat engineering added another layer without abandoning the same grammar.

Enemy engineers do not merely become tougher enemies. They alter the ground:

- caltrops attack momentum;
- barricades alter route cost;
- funnels remove options;
- casters exploit the resulting reduced route set.

The battlefield itself becomes an actor in the decision loop.

## Visual corollary

The carrier should own the frame.

At phone scale, presentation should answer quickly:

- that is me;
- those are mine;
- that is dangerous;
- that is where I can go.

Strangeness is an asset only after those reads survive.

Avoid polishing the game's biological/industrial oddness into generic professionalism.

## Relation to Marrow Runner

Marrow Runner's Pseudopod Ram is an earlier clean specimen of the same broader design signature:

> **MOTION IS NOT TRANSPORTATION. MOTION IS THE ACTION SYSTEM.**

The projects are mechanically different. The reusable connection is the preference for committed movement, transferred consequence, geometry, and contact over detached attack buttons.

## Source anchors

Current repository:

- https://github.com/Valar05/armored-bus-stop-v2
- README: https://github.com/Valar05/armored-bus-stop-v2/blob/main/README.md

Current source facts include V19 Doctrine Ramp and the Combat Engineering Doctrine. This note should remain a design extraction rather than a duplicate implementation handoff.
