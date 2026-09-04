# Animatic Frame Eligibility Doctrine

Date: 2026-07-09
Project surface: reusable animatic scene-direction workflow
Pattern name: audio-led frame eligibility
Status: promoted doctrine

## Problem

A still-frame animatic can fail even when every individual image is good. The common failure is scheduling a frame because it contains a matching visual noun or appears next in a contact sheet, while the frame actually represents the wrong narrative state.

Examples of the general failure:

- an interior or character-reaction image appears before the script grants access to that space or person.
- an arrival, aftermath, injury, victory, collapse, or other consequence appears before the story reaches it.
- a dramatic later image replaces a quieter exposition/detail beat because it looks more active.
- source contact-sheet order is treated as edit order without checking the audio beat.

## Doctrine

Audio, script, or player-facing text is the editorial source of truth. Before rendering, each beat must name the audience knowledge state, allowed visual states, forbidden visual states, eligibility class, and asset decision.

Eligibility classes:

- `current`: directly true for the current beat.
- `memory_or_echo`: deliberate return to a previous state.
- `foreshadow`: permitted only when the script intentionally points forward.
- `not_yet`: forbidden because it reveals a future state.
- `new_asset_required`: no existing image can truthfully carry the beat.

## Practical Rule

A visual noun match is not a narrative-state match. Reusing a correct earlier frame is better than cutting to a new frame that violates chronology. If no eligible image exists, create an insert/canonical frame or mark the beat as needing new art.

## Failure Labels Added

- `noun_match_state_mismatch`
- `premature_consequence`
- `unauthorized_access`
- `contact_sheet_as_timeline`

## Durable Locations

- `.codex/skills/animatic-scene-direction/SKILL.md`
- `.codex/skills/animatic-scene-direction/references/SCENE_DIRECTION_RUBRIC.md`
- `thunder-brainstorm/generated/skills/animatic_scene_direction.md`
