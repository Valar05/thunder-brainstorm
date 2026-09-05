# Animatic Scene Direction Workflow Capture

Date: 2026-07-08

## Purpose

Created a workspace-local Codex skill for animatic, motion visual, parallax 2D-in-3D, and overall scene-direction work. The workflow is meant for projects that stage 2D assets as planes, billboards, matte layers, sprites, or cutouts inside 3D/camera-driven scenes.

## Reusable Pattern

Treat the scene as directed shot language first: inventory assets, map beats, build a depth stack, plan camera motion, implement in the existing runtime, verify with the accepted visual lane, then preserve reusable lessons in Thunder Brainstorm.

## Failure Modes Captured

- Layers sliding with no story function.
- Camera motion obscuring the subject.
- Subject scale popping between beats.
- Fog or particles hiding the named target.
- Generated or placeholder assets lacking provenance.
- Machine checks being mistaken for visual acceptance.

## Durable Paths

- Skill: `.codex/skills/animatic-scene-direction/SKILL.md`
- Rubric: `.codex/skills/animatic-scene-direction/references/SCENE_DIRECTION_RUBRIC.md`
- Thunder mirror: `thunder-brainstorm/generated/skills/animatic_scene_direction.md`
- Manual refs: `thunder-brainstorm/generated/source_refs_manual/animatic_scene_direction_skill_source_refs.jsonl`

## Follow-Up Critique

Two defects from the first Holding Vigil animatic became workflow rules:

- `dead_air_hold`: the prior animatic held too long between beats. Future dialogue animatics should keep conversational pace and reserve long holds for marked intentional pauses.
- `single_voice_cast`: narrator and main character should not be the same voice with only pitch shifting. Future Cartesia passes should preflight distinct voice profiles for narrator and major speakers, with pitch shift used only as a subtle effect.

## Camera Doctrine Update

The skill now distinguishes camera grammar instead of treating `camera path` as a generic flourish:

- locked camera is default for dialogue, testimony, and choice beats.
- push-in/zoom tightens realization, threat, intimacy, evidence, or pressure.
- pull-back reveals isolation, consequence, scale, exposure, or loss of control.
- pan/tilt connect subjects, objects, witnesses, posture, or vertical power.
- dolly/slide needs parallax anchors.
- shake must be motivated and settle quickly.
- roll/rotation is rare and reserved for disorientation, collapse, surreal pressure, or moral inversion.
- `idle_camera_drift` and `unmotivated_roll` are now failure labels.
