# Marrow Runner — Origin, Link-First Distribution, and Motion as Action

Captured: 2026-09-19  
Status: durable lineage note  
Evidence classes: current repo evidence + Drew firsthand report

## Why this note exists

Thunder already contains the implementation pattern `recursive_knockback_dash_core`, Marrow Runner release learnings, and the phone-first Canvas release workflow. Do not duplicate those records here.

This note captures historical origin and higher-level design lineage that were not present in the existing Thunder records.

## Firsthand origin

Drew reports that Marrow Runner was:

- made as a Pac-Man-derived game for Jackie while she was in the hospital;
- one of Drew's first games developed substantially from the phone;
- the first clear experiment in the pattern **one prompt = one game**, immediately after Thunder Brainstorm itself became usable;
- the moment browser-native distribution stopped being an abstract platform choice and became a human constraint: Jackie could receive a link and play the game where she actually was.

Treat those statements as firsthand project history. They are not reconstructed from repository metadata.

## Browser-native lesson

The important distribution discovery was not merely "HTML5 is portable."

The actual constraint was:

> Can the intended person play the thing now, from the device and situation she already has?

That produces a stronger reusable rule:

**A GAME CAN BE A URL.**

When immediate human access is part of the commission, browser delivery is not the compromise build. It can be the native habitat.

This later supports the browser-first family that includes Armor Command, Driftfield, Infinite Brutality's modern Three.js branch, and Armored Bus Stop, but direct code inheritance should be claimed only where source evidence proves it.

## Pseudopod Ram authorship

Drew explicitly identifies Pseudopod Ram as an original Marrow Runner invention rather than an inherited mechanic.

Existing Thunder card `recursive_knockback_dash_core` correctly captures the implementation:

- burst from rest;
- launch instead of direct kill;
- launched enemies become physics-like projectiles;
- wall or enemy contact resolves kills;
- recursive chains become the reward.

The missing design law is broader:

## Motion Is the Action System

In Marrow Runner, movement is not only transport to the next action.

The movement commitment **is** the action.

```text
intent
-> committed movement
-> force transfer
-> changed body trajectory
-> geometry/body contact
-> consequence
```

This lets one input carry combat, positioning, risk, spectacle, and chain creation without adding a separate attack surface.

### Generalized pattern

A movement verb becomes mechanically dense when:

1. input commits the player to a trajectory or impulse;
2. contact transfers state or force into another body;
3. the affected body continues to matter after contact;
4. environment geometry or other bodies complete the outcome;
5. recovery/rearm creates a readable rhythm rather than allowing continuous spam.

Pocket law:

> **MOTION IS NOT TRANSPORTATION. MOTION IS THE ACTION SYSTEM.**

## Later resonance

Armored Bus Stop independently expresses the same grammar at a larger systemic scale:

- gravel drift preserves trajectory history;
- rams turn vehicle mass into attack;
- boots-first commandos turn carried troops into committed moving bodies;
- touch recovery makes contact mechanically meaningful again;
- fortifications change future trajectories instead of merely adding enemy HP.

This is a design-lineage resonance, not a claim that Armored Bus Stop copied Marrow Runner code.

## Source anchors

Current Marrow Runner repository:

- https://github.com/Valar05/marrow-runner
- README: https://github.com/Valar05/marrow-runner/blob/main/README.md

Existing Thunder records that remain authoritative for implementation/release detail:

- `generated/session_learnings/2026-06-05_marrow_runner_release_handoff.md`
- `generated/session_learnings/2026-06-06_marrow_runner_upgrade_leakfix_rc4.md`
- `generated/project_links/marrow_runner_project_links.md`
- pattern card `recursive_knockback_dash_core`

## Do not flatten

Do not rewrite Marrow Runner as "Pac-Man with a biology skin."

Pac-Man supplied a recognizable scaffold. The authored mutation is the shift from avoidance/collection toward force transfer, launched bodies, wall resolution, and recursive contact chains.
