# tts-audio-manifest-preflight Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/tts-audio-manifest-preflight/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: tts-audio-manifest-preflight
description: Use when generating, auditing, deduping, syncing, or repairing TTS/audio manifests, speaker profiles, spoken cues, MP3/WAV clips, playback sync, vehicle loop audio, Creative Commons audio sourcing, or attribution manifests.
---

# TTS/Audio Manifest Preflight

Use this skill before paying for generated audio or accepting audio wiring.

## Workflow

1. Identify displayed text, spoken text, speaker profile, and clip key.
2. Normalize spoken cues before generation.
3. Audit for stale clips, one-word clips, duplicate text, and manifest drift.
4. Preserve source/license metadata for downloaded or Creative Commons audio.
5. Run audio smoke tests or playback-sync tests when available.

## For Vehicle Audio

Track:

- engine idle/mid/high loops
- tire roll and slip loops
- skid one-shots
- surface selection
- RPM/speed/slip parameter mapping
- attribution manifest

## Guardrails

- Do not regenerate unchanged clips casually.
- Do not mix generated TTS and sourced audio without provenance.
- Keep speaker voice, cue text, file path, and dedupe key aligned.

## Local Synthesized Game SFX

For browser/canvas game SFX generated with local command-line tools, treat them like generated assets:

- Keep one-shot and loop names semantic, for example `eat_antibody_01.wav`, `pseudopod_ram_start_01.wav`, `knockback_chain_impact_01.wav`.
- Trim or synthesize with no leading silence; latency bugs can survive preloading if the waveform itself has space at the front.
- Record the generation preset/tool and target trigger in the SFX manifest.
- Wire pickup/impact sounds at the gameplay event that changes state, not at delayed animation completion.
- Validate loops separately from one-shots; short siren/complement loops must be seamless enough to repeat while active.

