# Prospector WWDD Behavioral Distillation: Thunder Brainstorm

Date: 2026-06-22
Operator: Drew Clarke
Corpus: `Valar05/thunder-brainstorm` plus indexed local/Cauldron/GitHub source-reference records already mirrored into Thunder Brainstorm.
Mode: Prospector / behavioral evidence extraction.

## Purpose

This is not a project summary. This document reconstructs observed judgment from repeated artifacts in the Thunder Brainstorm corpus.

Question answered:

> What does Drew repeatedly do when confronted with this class of problem?

Evidence priority:

1. Repeated preserved session learnings.
2. Generated skill notes and workflow guardrails.
3. Project link records and source-reference indexes.
4. Validation commands, release packets, manifests, and regression harnesses.
5. Repeated implementation shapes across unrelated projects.

Excluded:

- Unsupported opinions.
- Aspirational self-descriptions.
- One-off preferences with no behavioral evidence.

---

# 1. Observed Evidence

## Finding A — Source Parity Before Tuning

Classification: GENIUS / LATENT DOCTRINE

Observed behavior:
When porting, rebuilding, or fixing feel, Drew repeatedly anchors against the source project before changing constants.

Evidence:

- Last Convoy preserved a local Godot source snapshot specifically so future fixes could compare against original scripts, scenes, and shaders without reconnecting to the Cauldron machine.
  - Evidence: `generated/session_learnings/2026-06-07_last_convoy_html5_port_lessons.md`, lines 28-31.
- Gravity Fist dash/pushback debugging explicitly corrected visible feel by inspecting source movement math rather than tuning by eye.
  - Evidence: `generated/session_learnings/2026-06-07_gravity_fist_threejs_dash_pushback_parity.md`, lines 9-18.
- The reusable Gravity Fist rule says to compare scheduling, hitbox arming, dash easing, gap clamp, and formula order before changing constants.
  - Evidence: same file, lines 40-42.
- Thunder's README describes source-packet and corpus-to-mechanic workflows as part of what the system generalizes.
  - Evidence: `README.md`, lines 52-58.

Judgment reconstructed:
Drew treats source behavior as law until proven wrong. Feel bugs are often translation bugs, not tuning bugs.

Crucible:

- Repetition Score: 5/5
- Utility Score: 5/5
- Compression Score: 5/5
- Transferability Score: 5/5
- Inheritance Score: 5/5

Promote: YES

---

## Finding B — Validation Harnesses Replace Guesswork

Classification: GENIUS / RECURRING DECISION / LATENT DOCTRINE

Observed behavior:
When subjective playtest feedback appears, Drew repeatedly converts it into checks, probes, smoke tests, or build validation commands.

Evidence:

- Gravity Fist video feedback was converted into an in-page regression suite with named beacons, after extracting frames and counting issues.
  - Evidence: `generated/session_learnings/2026-06-06_gravity_fist_video_regression_suite.md`, lines 7-10 and 26-47.
- The same pass recorded static/build validation commands and rebuilt a release archive.
  - Evidence: same file, lines 70-83.
- Marrow Runner release handoff preserved repeatable validation commands: JS syntax check, JSON manifest checks, and release build.
  - Evidence: `generated/session_learnings/2026-06-05_marrow_runner_release_handoff.md`, lines 38-48.
- Marrow Runner RC4 added zip integrity validation and browser smoke notes.
  - Evidence: `generated/session_learnings/2026-06-06_marrow_runner_upgrade_leakfix_rc4.md`, lines 49-66.
- Armor Command preserved validation commands for JS, JSON, atlas, and release build.
  - Evidence: `generated/session_learnings/2026-06-05_armor_command_prototype_lessons.md`, lines 77-86.
- Thunder's combined mechanics index contains a major `validation_pipeline` category with thousands of records.
  - Evidence: `generated/index_combined/mechanic_index_report.md`, lines 73-79.

Judgment reconstructed:
Drew does not trust vibes after the first pass. If a problem hurts twice, he wants a test, beacon, counter, or harness.

Crucible:

- Repetition Score: 5/5
- Utility Score: 5/5
- Compression Score: 5/5
- Transferability Score: 5/5
- Inheritance Score: 5/5

Promote: YES

---

## Finding C — Mobile-First HTML5 Canvas Is the Shipping Default

Classification: GENIUS / RECURRING DECISION

Observed behavior:
When choosing a practical release target, Drew repeatedly biases toward mobile-first HTML5/canvas with local play URLs, itch packaging, and Android validation.

Evidence:

- Armor Command design snapshot states mobile-first HTML5 canvas and local browser play.
  - Evidence: `generated/session_learnings/2026-06-05_armor_command_prototype_lessons.md`, lines 88-99.
- Marrow Runner release notes preserve standalone web release commands, itch target, Android fullscreen/iframe controls, and local/remote publication facts.
  - Evidence: `generated/session_learnings/2026-06-05_marrow_runner_release_handoff.md`, lines 27-37 and 38-78.
- Gravity Fist Three.js is explicitly described as the active itch HTML5 target, with normal Three.js checks.
  - Evidence: `generated/session_learnings/2026-06-06_gravity_fist_meshy_asset_workflow.md`, lines 43-64.
- FPS Platformer concept starts with phone-first landscape Three.js, touch movement/look, Android capture hooks, and sparse controls.
  - Evidence: `generated/session_learnings/2026-06-07_fps_platformer_arcane_ik_brainstorm.md`, lines 15-19, 57-68, and 80-89.
- README quick start and docs repeatedly expose local servers and doc-server URLs.
  - Evidence: `README.md`, lines 21-24 and 90-99.

Judgment reconstructed:
Drew defaults to the lowest-friction playable surface: phone browser first, release zip second, store/backend later only if earned.

Crucible:

- Repetition Score: 5/5
- Utility Score: 5/5
- Compression Score: 4/5
- Transferability Score: 4/5
- Inheritance Score: 5/5

Promote: YES

---

## Finding D — Provenance Is Part Of The Asset, Not Paperwork

Classification: GENIUS / LATENT DOCTRINE

Observed behavior:
Generated assets, imported models, source snapshots, manifests, and release files are preserved beside the work so future agents can verify origin, assumptions, and reuse boundaries.

Evidence:

- Meshy asset workflow requires a per-asset folder containing a manifest with prompt, provider, task IDs, request settings, downloaded files, target project, and timestamps.
  - Evidence: `generated/session_learnings/2026-06-06_gravity_fist_meshy_asset_workflow.md`, lines 15-22.
- The same workflow says to distinguish generated source images, model outputs, and runtime-ready mirrored copies, and to avoid long-term reliance on hosted URLs.
  - Evidence: same file, lines 190-196.
- Armor Command requires saving prompt, source image, runtime copy, atlas metadata, and source-pose assumptions in manifests.
  - Evidence: `generated/session_learnings/2026-06-05_armor_command_prototype_lessons.md`, lines 54-60.
- Marrow Runner records generated art/music/SFX in manifests and preserves sibling copies for screenshots/upload assets.
  - Evidence: `generated/session_learnings/2026-06-05_marrow_runner_release_handoff.md`, lines 116-121.
- Thunder README defines the corpus index as source records with origin, project, path, line number, symbol/key/heading, mechanic tags, and evidence line.
  - Evidence: `README.md`, lines 72-82.

Judgment reconstructed:
Drew's asset pipeline assumes future confusion. Provenance is stored at creation time because rediscovery is more expensive than metadata.

Crucible:

- Repetition Score: 5/5
- Utility Score: 5/5
- Compression Score: 5/5
- Transferability Score: 5/5
- Inheritance Score: 5/5

Promote: YES

---

## Finding E — Additive Systems Beat Replacement Systems Unless Replacement Is Explicit

Classification: GENIUS / LATENT DOCTRINE

Observed behavior:
Across upgrade/combat systems, Drew repeatedly prefers stacking behaviors, conditional synergies, and independent flags over exclusive enums or replacement trees.

Evidence:

- Armor Command Content Drop 2 formalized an additive trait mutation rule: if a run advertises multiple weapon mutations, default to additive composition unless replacement is explicit.
  - Evidence: `generated/session_learnings/2026-06-05_armor_command_prototype_lessons.md`, lines 117-131.
- Marrow Runner RC4 says to extend the existing additive mutation model rather than creating a parallel upgrade system.
  - Evidence: `generated/session_learnings/2026-06-06_marrow_runner_upgrade_leakfix_rc4.md`, lines 31-37.
- Armor Command records independent cooldown per missile rack as an upgrade payoff: more racks means more fire opportunities, not merely a faster shared reload.
  - Evidence: `generated/session_learnings/2026-06-05_armor_command_prototype_lessons.md`, lines 41-47.

Judgment reconstructed:
Drew protects player-earned behavior. New toys should compose with old toys unless the UI honestly says a choice replaces something.

Crucible:

- Repetition Score: 4/5
- Utility Score: 5/5
- Compression Score: 5/5
- Transferability Score: 5/5
- Inheritance Score: 5/5

Promote: YES

---

## Finding F — Pressure Systems Are Preferred Over Raw Difficulty

Classification: GENIUS / RECURRING DECISION

Observed behavior:
Drew repeatedly designs difficulty as layered pressure: spawn cadence, enemy branches, delayed consequences, high-risk zones, readable escalation, and player choice under strain.

Evidence:

- Armor Command difficulty tuning increases pressure across multiple visible axes: missile count, spawn cadence, speed, hot-missile chance, and HP.
  - Evidence: `generated/session_learnings/2026-06-05_armor_command_prototype_lessons.md`, lines 48-53.
- Armor Command added a second enemy branch with drop pods, robot paratroopers, small rockets, and kill-chain scoring.
  - Evidence: same file, lines 101-108.
- Marrow Runner uses infection nests / ghost-cage equivalents as readable high-risk spawn zones.
  - Evidence: `generated/session_learnings/2026-06-05_marrow_runner_release_handoff.md`, lines 27-37.
- Thunder's README says it generalizes pressure arenas, event clouds, delayed consequences, and deck-driven pacing.
  - Evidence: `README.md`, lines 52-58.
- The mechanics index shows durable pressure-related categories: `ai_pressure`, `delayed_consequences`, `event_clouds`, and `deck_pressure`.
  - Evidence: `generated/index_combined/mechanic_index_report.md`, lines 24-30, 66-72, 94-100, and 108-113.

Judgment reconstructed:
Drew tends to make games harder by creating readable pressure fields, not just increasing numbers.

Crucible:

- Repetition Score: 5/5
- Utility Score: 5/5
- Compression Score: 4/5
- Transferability Score: 5/5
- Inheritance Score: 5/5

Promote: YES

---

## Finding G — Convert Fragile Workflows Into Skills And Reusable Pattern Cards

Classification: GENIUS / LATENT DOCTRINE

Observed behavior:
When a workflow becomes fragile, repeated, or easy to forget, Drew turns it into a skill, pattern card, manifest, source reference, or session learning.

Evidence:

- Thunder README defines generated pitch output around pattern stack, content pipeline, validation plan, and risks.
  - Evidence: `README.md`, lines 60-70.
- Thunder's corpus index stores mechanics source references and reports, explicitly as an audit trail for extracted mechanics.
  - Evidence: `README.md`, lines 72-82.
- The Thunder Corpus Indexer skill exists specifically to preserve source references with file paths and line numbers and to update/search Thunder indexes.
  - Evidence: `generated/skills/thunder_brainstorm_corpus_indexer.md`, lines 15-23 and 32-58.
- README records generalized pattern cards from Armor Command, Marrow Runner, and Last Convoy passes.
  - Evidence: `README.md`, lines 117-119 and 146-169.
- Last Convoy session learning ends with reusable pattern cards for convoy upgrade chain, source parity canvas port, shader bridge, textured fragmentation, and Android cache-busting.
  - Evidence: `generated/session_learnings/2026-06-07_last_convoy_html5_port_lessons.md`, lines 51-58.

Judgment reconstructed:
Drew treats repeated friction as an asset-generation event. If the workflow is fragile, the deliverable is not only the fix; it is the future operator skill.

Crucible:

- Repetition Score: 5/5
- Utility Score: 5/5
- Compression Score: 5/5
- Transferability Score: 5/5
- Inheritance Score: 5/5

Promote: YES

---

## Finding H — Small Playable Slice Before Architecture Cathedral

Classification: GENIUS / RECURRING DECISION

Observed behavior:
Drew repeatedly narrows new ideas into a first prototype slice, a local playable URL, or a lab page before deep implementation.

Evidence:

- FPS Platformer first prototype slice starts with export, project setup, one greybox outdoor landscape, touch movement/look, import lab, motor/camera bob, IK later, and only one enemy/target dummy after traversal reads.
  - Evidence: `generated/session_learnings/2026-06-07_fps_platformer_arcane_ik_brainstorm.md`, lines 80-100.
- Gravity Fist Meshy workflow says to use a pose lab to inspect orientation, scale, and animations before wiring into runtime.
  - Evidence: `generated/session_learnings/2026-06-06_gravity_fist_meshy_asset_workflow.md`, lines 47-55.
- Armor Command accepted local personal best as enough for early itch prototypes, with backend scoreboards deferred until the game earns them.
  - Evidence: `generated/session_learnings/2026-06-05_armor_command_prototype_lessons.md`, lines 41-47.
- README exposes local play URLs and small prototype launch commands for Armor Command and Immune Maze.
  - Evidence: `README.md`, lines 21-24 and 121-130.

Judgment reconstructed:
Drew ships tiny playable proof before investing in infrastructure. Architecture is earned by friction, not imagined in advance.

Crucible:

- Repetition Score: 4/5
- Utility Score: 5/5
- Compression Score: 5/5
- Transferability Score: 5/5
- Inheritance Score: 5/5

Promote: YES

---

## Finding I — WASTE: Tuning By Eye Before Instrumenting Feel

Classification: WASTE

Observed waste pattern:
When feel is wrong, pure visual tuning risks chasing the symptom instead of the source mismatch.

Evidence:

- Gravity Fist dash/pushback feedback felt delayed or nonexistent; the important correction was to inspect source movement math rather than tune visible distances.
  - Evidence: `generated/session_learnings/2026-06-07_gravity_fist_threejs_dash_pushback_parity.md`, lines 9-18.
- The final reusable rule explicitly requires comparing scheduling, hitbox arming, easing, clamp, and formula order before constants.
  - Evidence: same file, lines 40-42.
- Video readability feedback became regression beacons because live combat was hard to parse without checks.
  - Evidence: `generated/session_learnings/2026-06-06_gravity_fist_video_regression_suite.md`, lines 11-24 and 34-47.

Waste reconstructed:
Visual guessing burns attention. Instrumented probes win.

Crucible:

- Repetition Score: 3/5
- Utility Score: 5/5
- Compression Score: 5/5
- Transferability Score: 5/5
- Inheritance Score: 4/5

Promote: YES, as anti-pattern doctrine.

---

## Finding J — WASTE: Generated Asset Drift Without Manifests

Classification: WASTE

Observed waste pattern:
Generated art/model pipelines become unreliable when prompts, pose assumptions, source files, and runtime copies are not preserved distinctly.

Evidence:

- Armor Command found generated sprite sheets needed prompt/source/runtime/atlas/source-pose preservation, because centering and pose assumptions were not reliable.
  - Evidence: `generated/session_learnings/2026-06-05_armor_command_prototype_lessons.md`, lines 54-60.
- Meshy workflow requires manifests and warns against trusting generated output until scale, skeleton, axis, retargeting, hitboxes, and attachment points are verified.
  - Evidence: `generated/session_learnings/2026-06-06_gravity_fist_meshy_asset_workflow.md`, lines 23-42.
- Meshy workflow also warns not to rely on Meshy-hosted URLs and to keep source/model/runtime-ready copies distinguishable.
  - Evidence: same file, lines 190-196.

Waste reconstructed:
Untracked generated assets become mystery meat. Mystery meat is not a pipeline; it is a fridge crime scene.

Crucible:

- Repetition Score: 4/5
- Utility Score: 5/5
- Compression Score: 5/5
- Transferability Score: 5/5
- Inheritance Score: 5/5

Promote: YES, as anti-pattern doctrine.

---

## Finding K — WASTE: Mobile Environment Friction Is Predictable And Must Be Systematized

Classification: WASTE / LATENT DOCTRINE

Observed waste pattern:
Android/Termux/browser/file-system friction recurs: stale browser cache, media index invisibility, external binary incompatibility, browser launcher false failures, fullscreen/resize churn.

Evidence:

- Last Convoy needed cache-busted CSS/JS query strings because Android browser served stale JS.
  - Evidence: `generated/session_learnings/2026-06-07_last_convoy_html5_port_lessons.md`, lines 33-37 and 57.
- Marrow Runner records the Android external file rule: refresh media/file indexing before reporting completion.
  - Evidence: `generated/session_learnings/2026-06-05_marrow_runner_release_handoff.md`, lines 106-114.
- Armor Command records Termux butler source-build notes because the official Linux ARM64 binary can fail under Android's linker.
  - Evidence: `generated/session_learnings/2026-06-05_armor_command_prototype_lessons.md`, lines 109-115.
- Gravity Fist Android browser capture can report no requests when the browser launcher fails; this must be treated as a launcher/lock-state failure, not runtime parse failure.
  - Evidence: `generated/session_learnings/2026-06-06_gravity_fist_video_regression_suite.md`, lines 86-88.
- Marrow Runner RC4 hardened against duplicate input binding, duplicate animation loops, stale transforms, resize bursts, and repeated New Run choppiness.
  - Evidence: `generated/session_learnings/2026-06-06_marrow_runner_upgrade_leakfix_rc4.md`, lines 39-48.

Waste reconstructed:
Mobile environment friction is not exceptional. It is a recurring tax. Handle it as doctrine or keep paying goblin tolls.

Crucible:

- Repetition Score: 5/5
- Utility Score: 5/5
- Compression Score: 5/5
- Transferability Score: 5/5
- Inheritance Score: 5/5

Promote: YES, as anti-pattern and checklist doctrine.

---

# 2. Behavioral Distillation

## Behavior 1

Preserves source snapshots and compares source behavior before tuning ports.

→ Skill: Source Parity Operator

→ Capability Unlock: Future agents can fix port regressions by proving behavioral equivalence instead of nudging constants until the goblin stops screaming.

## Behavior 2

Turns subjective feedback into regression beacons, counters, harnesses, or validation commands.

→ Skill: Feedback-To-Harness Converter

→ Capability Unlock: Ambiguous playtest complaints become repeatable pass/fail evidence.

## Behavior 3

Defaults to mobile-first HTML5/canvas/Three.js release paths with local URLs and itch-ready build artifacts.

→ Skill: Phone-First Web Release Operator

→ Capability Unlock: New prototypes can reach playable/public state without store infrastructure or backend ceremony.

## Behavior 4

Stores generated/imported asset provenance beside the asset.

→ Skill: Asset Provenance Steward

→ Capability Unlock: Future agents can reuse, audit, regenerate, or replace assets without archaeology panic.

## Behavior 5

Designs upgrades as additive, composable traits unless replacement is explicit.

→ Skill: Additive Upgrade Architect

→ Capability Unlock: Progression systems preserve earned player behavior and support emergent synergies.

## Behavior 6

Builds pressure through readable axes, enemy branches, delayed consequences, and high-risk zones.

→ Skill: Pressure Field Designer

→ Capability Unlock: Difficulty can escalate without becoming unfair sludge.

## Behavior 7

Promotes repeated workflows into skills, pattern cards, source refs, and session learnings.

→ Skill: Friction-To-Doctrine Promoter

→ Capability Unlock: Each solved pain point becomes reusable judgment for future agents.

## Behavior 8

Creates import labs, first slices, local servers, and tiny playable proofs before broad architecture.

→ Skill: Smallest Playable Slice Cutter

→ Capability Unlock: Projects can validate feel before architecture overgrowth.

---

# 3. WWDD Candidate Rules

Only supported candidates are listed.

1. When confronted with a port that feels wrong, Drew repeatedly compares source behavior, timing, formulas, and asset assumptions before tuning constants.
2. When confronted with subjective feedback, Drew repeatedly converts the complaint into a measurable harness, beacon, counter, or regression check.
3. When confronted with a new prototype, Drew repeatedly seeks a mobile-first playable web slice before store/backend infrastructure.
4. When confronted with generated or imported assets, Drew repeatedly preserves provenance, source assumptions, manifests, and runtime-ready copies.
5. When confronted with upgrade design, Drew repeatedly favors additive composition unless the player is explicitly told something is being replaced.
6. When confronted with difficulty tuning, Drew repeatedly creates layered pressure systems instead of only inflating numbers.
7. When confronted with repeated workflow pain, Drew repeatedly turns the fix into a skill, pattern card, checklist, or source-reference record.
8. When confronted with uncertain runtime behavior on Android/Termux/browser surfaces, Drew repeatedly adds cache busting, smoke checks, media refreshes, and environment-specific guardrails.
9. When confronted with asset import risk, Drew repeatedly builds or uses a lab page before wiring the asset into production runtime.
10. When confronted with release readiness, Drew repeatedly runs syntax checks, JSON validation, build scripts, and archive/package checks before calling the work complete.

---

# 4. Gold Promotions

Promoted findings:

## Gold 1 — Source Parity Before Tuning

Doctrine:
Before tuning a port or remake, prove the source behavior. Compare source scheduling, formulas, easing, clamps, orientation, asset assumptions, and lifecycle before changing constants.

Use when:
- A port feels delayed, weak, rotated, stale, or visually wrong.
- A remake does not match the original feel.
- A browser/Three.js/canvas version diverges from Godot.

## Gold 2 — Feedback Becomes Harness

Doctrine:
A subjective complaint is raw ore. Extract a failing check, beacon, screenshot comparison, counter, or repro harness before doing broad fixes.

Use when:
- User says “feels bad,” “hard to read,” “delayed,” “choppy,” or “not working.”
- Visual feedback depends on timing, orientation, layout, or readability.

## Gold 3 — Phone-First Web Slice

Doctrine:
Default new prototypes to a mobile-first playable web surface unless the project has a stronger reason not to. Backend, platform store, and account systems are earned later.

Use when:
- Building arcade, action, narrative, or experimental game prototypes.
- User needs a fast playable loop from phone.

## Gold 4 — Provenance Is Runtime Infrastructure

Doctrine:
Generated/imported assets must carry provenance: prompt/source, provider, task IDs, pose assumptions, file lineage, runtime copy, manifest, and validation notes.

Use when:
- Generating images, Meshy assets, audio, SFX, sprites, atlases, or release page assets.

## Gold 5 — Additive Unless Replacement Is The Fantasy

Doctrine:
Upgrade systems should compose earned behaviors by default. If a choice removes behavior, the UI must say replacement explicitly.

Use when:
- Designing mutation trees, weapon branches, capstones, synergies, or class upgrades.

## Gold 6 — Pressure Field Over Number Soup

Doctrine:
Difficulty should escalate through readable pressure axes: spawn cadence, enemy families, map zones, delayed consequences, resource tension, and feedback clarity.

Use when:
- Tuning waves, enemy branches, roguelike event decks, pursuit, heat, infection, or arena pressure.

## Gold 7 — Friction Promotes To Doctrine

Doctrine:
If a workflow hurts twice, write the operator skill/checklist/source-ref now. The fix is incomplete until future agents can inherit it.

Use when:
- The same environment, release, asset, validation, or handoff problem recurs.

## Gold 8 — Android Is A Hostile Little Goblin, Treat It As Such

Doctrine:
Android/Termux/browser friction needs explicit guardrails: cache busting, media scanner refresh, local linker/tool compatibility, lifecycle guards, and launcher-failure interpretation.

Use when:
- Testing on phone browser.
- Moving files to shared storage.
- Running Termux binaries.
- Rebuilding web releases.

---

# 5. Recommended New Doctrine

## Doctrine: Behavioral Evidence Beats Self-Description

Rule:
When mining WWDD, ignore what Drew says he values unless repeated artifacts show him doing it. Promote only behavior with evidence.

Why:
The corpus is valuable because it shows actual decisions under friction.

## Doctrine: Every Pain Point Needs A Preservation Surface

Rule:
A pain point is not fully solved until its fix exists in one of these surfaces:

- validation command
- harness
- manifest
- source ref
- pattern card
- skill note
- project link
- release packet
- doctrine document

Why:
Otherwise the solution decays back into chat exhaust.

## Doctrine: Port Bugs Are Translation Bugs Until Proven Otherwise

Rule:
Do not tune constants first. Inspect source scheduling, lifecycle, geometry, shader assumptions, orientation, and formula order.

Why:
Multiple ports showed that the visible bug was downstream of mismatched source behavior.

## Doctrine: Prototype Infrastructure Must Earn Its Rent

Rule:
Start with a playable phone/web slice, local storage, local server, and release zip. Add backend, scoreboard, platform store, or accounts only after the prototype proves it deserves them.

Why:
Repeated successful projects reached playable state by avoiding premature infrastructure.

## Doctrine: Generated Assets Are Evidence Objects

Rule:
Treat generated assets as evidence objects with lineage, not loose files. Preserve prompt, source, provider, task ID, pose assumptions, runtime copy, validation status, and release usage.

Why:
Generated assets drift, expire, and confuse future agents unless captured at birth.

## Doctrine: Additive Progression Preserves Trust

Rule:
Player-earned mechanics should remain active and compose unless replacement is clearly communicated.

Why:
Repeated upgrade-system fixes show that hidden replacement feels like theft.

---

# Recommended Follow-Up Artifacts

1. `generated/skills/source_parity_operator.md`
2. `generated/skills/feedback_to_harness_converter.md`
3. `generated/skills/asset_provenance_steward.md`
4. `generated/doctrine/wwdd_gold_rules.md`
5. `generated/checklists/android_phone_web_release_checklist.md`

These should be created as first-class operator assets if this pass is accepted.
