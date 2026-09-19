# Driftfield — Origin Archaeology and Unresolved Space-Melee Donor

Captured: 2026-09-19  
Status: OPEN ARCHAEOLOGY QUESTION  
Evidence classes: current repo evidence + Drew firsthand report

## Current proven shape

The current Driftfield repository is a standalone Three.js browser project with two explicit branches:

- Arcade Mode: cockpit Asteroids-like survival;
- Expedition Mode: Descent-like 6DOF asteroid-interior exploration.

Current project orientation also states that Driftfield belongs to the same browser schema family as the modern `infinite-brutality`.

Current repo:

- https://github.com/Valar05/driftfield
- https://github.com/Valar05/driftfield/blob/main/PROJECT_ORIENTATION.md

## Firsthand historical correction

Drew reports that the project lineage reaches farther back than the current Driftfield documentation shows.

Before the recognizable Asteroids form, an earlier **space-based melee game** from the period when Drew was mostly pseudocoding through AI supplied or preceded the original game concept/material.

The exact donor repository/name is currently unresolved.

Do not replace this firsthand report with the cleaner but incomplete story "Driftfield began as Asteroids."

## What has been checked

The present Driftfield orientation, agent guide, development guide, current asteroid generator, and existing Thunder Driftfield mirrors do not identify the earlier melee-space donor by name.

The old capitalized repository `Valar05/InfiniteBrutality` was also inspected as a possible historical clue. Its currently surfaced Godot scene is a flat navigation arena with a player, environment, and spawn controller. That evidence is not sufficient to identify it as the space-melee donor.

Therefore:

> **DONOR = UNRESOLVED. DO NOT GUESS.**

## Current asteroid implementation is not proof of origin

Current `src/visuals.js` constructs Arcade asteroids from a subdivided icosahedron with deterministic axis scaling and procedural ridge/dent displacement.

That describes the present implementation only.

It does not establish where the original asteroid/game idea came from.

## Next archaeology targets

Prefer evidence in this order:

1. earliest Driftfield git commits/blobs before current architecture;
2. local workspace recovery index for older sibling repos not obvious from current GitHub names;
3. project docs/handoffs from the pseudocode-through-AI period;
4. old branches, stashes, or archived local worktrees;
5. only then semantic matching against candidate repos.

A candidate donor should earn the label by showing at least two of:

- space/6DOF or zero-gravity setting;
- melee/contact-first combat;
- asteroid/rock field or a directly inherited asteroid routine;
- matching control/momentum vocabulary;
- explicit historical cross-reference.

## Lineage note

Drew also reports a broader mutation chain in which the Asteroids-era work later fed into work that became Infinite Brutality, while modern Infinite Brutality is itself expected to evolve further into Taste Trap.

Preserve this as **human-reported lineage** until exact code/repo inheritance is recovered.

The useful general pattern is already clear even while names remain incomplete:

> projects are not franchises; useful verbs and pressure systems migrate into new bodies.

## Existing Thunder Driftfield records

Do not duplicate:

- `generated/session_learnings/2026-06-14_driftfield_asteroid_mine_grammar.md`
- `generated/session_learnings/2026-06-14_driftfield_expedition_cave_meshy_handoff.md`
- `generated/project_links/driftfield_project_links.md`

Those records cover current Expedition/cave/runtime knowledge. This file owns the unresolved historical-origin question.
