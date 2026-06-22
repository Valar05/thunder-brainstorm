# WWDD Gold Rules — Thunder Brainstorm Prospector Pass

Date: 2026-06-22
Source: `generated/behavioral_mining/prospector_wwdd_thunder_brainstorm_2026-06-22.md`

These are promoted WWDD rules extracted from observed Thunder Brainstorm behavior. Use these as operator doctrine for future agents.

## 1. Source Parity Before Tuning

When a port, remake, or runtime translation feels wrong, compare source behavior before changing constants.

Check:

- timing
- scheduling
- hitbox arming
- easing
- clamps
- formula order
- orientation
- asset assumptions
- lifecycle state

Default assumption:

> Port bugs are translation bugs until proven otherwise.

## 2. Feedback Becomes Harness

When feedback is subjective, convert it into evidence.

Convert:

- “feels delayed” → timing probe
- “hard to read” → screenshot/video regression
- “choppy” → lifecycle counters
- “not working” → smoke test
- “wrong orientation” → automated yaw/axis check

Default assumption:

> Vibes are ore. Harnesses are gold.

## 3. Phone-First Web Slice

When starting a prototype, default to the smallest playable mobile web slice unless the project clearly requires another target.

Prefer:

- HTML5/canvas/Three.js
- local play URL
- touch-first controls
- localStorage before backend
- itch/release zip before platform-store ceremony

Default assumption:

> Backend and store infrastructure must earn rent.

## 4. Provenance Is Runtime Infrastructure

Generated and imported assets must preserve lineage beside the asset.

Capture:

- prompt/source
- provider
- task IDs
- pose assumptions
- source files
- runtime-ready copies
- manifest
- validation status
- release usage

Default assumption:

> Mystery assets are future bugs wearing a funny hat.

## 5. Additive Unless Replacement Is Explicit

Upgrade systems should preserve earned player behavior by default.

Use additive composition for:

- weapon mutations
- branch upgrades
- capstones
- synergies
- drones/companions
- projectile traits

If behavior is removed, the UI must say replacement clearly.

Default assumption:

> Hidden replacement feels like theft.

## 6. Pressure Field Over Number Soup

Difficulty should escalate through readable pressure, not raw stat inflation alone.

Pressure axes:

- spawn cadence
- enemy families
- high-risk zones
- delayed consequences
- resource tension
- pursuit pressure
- score-chain tension
- visual clarity

Default assumption:

> Harder should mean more decisions under pressure, not more sludge.

## 7. Friction Promotes To Doctrine

If a workflow hurts twice, preserve the fix as an operator asset.

Valid preservation surfaces:

- validation command
- harness
- manifest
- source ref
- pattern card
- skill note
- project link
- release packet
- doctrine document

Default assumption:

> A fix that cannot be inherited is only a temporary exorcism.

## 8. Android Is A Hostile Little Goblin

Android/Termux/browser behavior should be handled with explicit guardrails.

Expect:

- stale browser cache
- shared-storage media index lag
- binary/linker mismatch
- browser launcher false success
- fullscreen/resize bursts
- duplicate animation/input loops

Use:

- cache-busted JS/CSS URLs
- media scanner refresh
- lifecycle guards
- event-loop guards
- smoke tests
- launcher-failure interpretation

Default assumption:

> The phone is not broken. It is merely being a tiny procedural dungeon.

## 9. Smallest Playable Slice First

Before architecture, build a slice that proves feel.

Prefer:

- one screen
- one loop
- one enemy/dummy
- one import lab
- one release command
- one validation path

Default assumption:

> Architecture is earned by friction, not imagined in advance.

## 10. Behavioral Evidence Beats Self-Description

When mining WWDD, promote only repeated observed behavior.

Ignore unless supported by artifacts:

- self-description
- aspiration
- opinion
- isolated preference
- vibes with no source trail

Default assumption:

> The corpus knows what Drew does. Ask the receipts.
