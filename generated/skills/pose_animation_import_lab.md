# pose-animation-import-lab Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/pose-animation-import-lab/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: pose-animation-import-lab
description: Use when working with Phalanx-style pose tools, imported GLB/Blend animation clips, skeleton profiles, bone maps, stick rigs, onion poses, IK toggles, orbit viewports, retargeting, or animation inspection for Godot combat prototypes.
---

# Pose/Animation Import Lab

Use this skill for animation tooling and imported rig/clip analysis.

## Workflow

1. Identify source model/clip files and import sidecars.
2. Inspect skeleton profile JSON: bone map, source joints, display bones, default interpolation, smooth channels.
3. Inspect rig scripts for selected bones, controls, onion poses, IK, and transform mode.
4. For Godot-sourced assets, inspect the scene AnimationPlayer and AnimationTree before runtime mapping. Export linked .res clips and scene-embedded animation subresources from the actual scene when the GLB inventory is incomplete.
5. For GLB-embedded rigs, enumerate the real `animations[].name` inventory from the asset before trusting aliases or UI labels. Use actual clip names and durations when choosing hurt, restart, death, or locomotion candidates.
6. Compare imported animation timing to runtime combat needs.
7. Update source manifests or handoff docs when import ownership changes.

## Search

```sh
python thunder-brainstorm/thunder_brainstorm.py search-index "bone" --mechanic pose_animation_tools --index thunder-brainstorm/generated/index_combined/mechanic_source_refs.jsonl
```

## Guardrails

- Do not mutate source assets or sidecars casually.
- Keep tool rig assumptions separate from runtime rig assumptions.
- Treat retargeted motion quality as silhouette/readability, not just file conversion.
