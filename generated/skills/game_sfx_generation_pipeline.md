# game-sfx-generation-pipeline Skill

Local skill path:

```text
/data/data/com.termux/files/home/.codex/skills/game-sfx-generation-pipeline
```

Bundled helper:

```text
/data/data/com.termux/files/home/.codex/skills/game-sfx-generation-pipeline/scripts/prepare_sfx.py
```

---

---
name: game-sfx-generation-pipeline
description: "Use when generating, sourcing, cleaning, cataloging, trimming, normalizing, looping, or wiring game sound effects for HTML/canvas, Godot, or other prototypes, especially Marrow Runner-style SFX manifests, low-latency pickup/impact/UI sounds, ffmpeg-based audio cleanup, fair-use/Creative Commons sound sourcing, and runtime trigger validation."
---

# Game SFX Generation Pipeline

Use this skill to create or repair game SFX end to end: design the sound, generate or source it, trim latency, normalize loudness, update manifests/provenance, wire runtime triggers, and validate playback timing.

## Core Rules

- Prefer project-owned generated audio or clearly licensed/sourced audio. Do not claim ownership/license without a manifest, certificate, source URL, or generation note.
- Keep effect files short and trigger-specific. For responsive UI, pickup, and impact sounds, remove leading silence aggressively.
- Use `ffmpeg` and `ffprobe` first for inspection, trimming, loudness, fades, format conversion, and loop checks. If missing, ask before installing, for example `pkg install ffmpeg` on Termux.
- Preserve source files. Write processed outputs to a project-owned SFX/audio folder with clear names.
- Record every accepted clip in the owning manifest, usually `assets/sfx/sfx_manifest.json` or `assets/asset_manifest.json`.
- For Android-visible outputs, use the `android-external-file-refresh` skill before reporting files are ready.

## Workflow

1. Read project orientation docs and existing audio manifests before editing.
2. Define the sound manifest first: trigger id, intent, duration target, loopable/non-loopable, target loudness, source/provenance, and runtime event.
3. Generate or source candidates:
   - Generated: record prompt, tool/model, date, and any ownership certificate.
   - Sourced: record source URL, license, author, title, and attribution requirement.
   - Procedural/CLI: record exact command or script.
4. Inspect candidates with `ffprobe`:
   ```sh
   ffprobe -hide_banner -show_format -show_streams path/to/input.wav
   ```
5. Process with the bundled helper when appropriate:
   ```sh
   python /data/data/com.termux/files/home/.codex/skills/game-sfx-generation-pipeline/scripts/prepare_sfx.py input.wav output.wav --trim-silence --target-lufs -16 --fade-in 0.003 --fade-out 0.025
   ```
6. For short one-shots, verify audible onset is near zero:
   ```sh
   ffmpeg -i output.wav -af silencedetect=noise=-45dB:d=0.02 -f null -
   ```
7. Wire runtime playback using the project’s existing audio path. Prefer preloaded pools or decoded buffers for low latency. Avoid creating a fresh `Audio()` at the exact gameplay trigger if the project already has pooled playback.
8. Validate:
   - JSON manifests parse.
   - Runtime code syntax checks pass.
   - The sound plays on the intended trigger, not a nearby trigger.
   - Pickup/UI sounds have no perceptible front delay after first load.
   - Loops start/stop cleanly and pause on tab/app background when needed.

## Naming

Use stable, trigger-oriented ids:

```text
pickup_antibody_01.wav
pickup_complement_01.wav
loop_complement_siren_01.wav
impact_dash_01.wav
impact_chain_knockback_01.wav
kill_wall_impact_01.wav
ui_pause_01.wav
ui_select_01.wav
level_clear_01.wav
```

Manifest ids should match runtime event names where possible.

## Common ffmpeg Patterns

Trim leading/trailing silence and normalize:

```sh
ffmpeg -y -i in.wav -af "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.005:stop_periods=1:stop_threshold=-50dB:stop_silence=0.035,loudnorm=I=-16:TP=-1.5:LRA=8,afade=t=in:st=0:d=0.003,afade=t=out:st=0.17:d=0.025" out.wav
```

Make a short loop from a longer siren or bed:

```sh
ffmpeg -y -ss 0.4 -t 1.2 -i in.wav -af "loudnorm=I=-20:TP=-2:LRA=6,afade=t=in:st=0:d=0.02,afade=t=out:st=1.15:d=0.05" loop_siren.wav
```

Convert to browser-friendly MP3 fallback:

```sh
ffmpeg -y -i in.wav -codec:a libmp3lame -q:a 3 out.mp3
```

## Marrow Runner Lessons

- Antibody pickup latency was caused by front silence, not only loading. Always inspect and trim source onset.
- Complement/power loops need explicit start/stop state and should not restart every frame.
- Chain impacts should allow repeated playback without cutting off the first hit; use a small pool or WebAudio buffers.
- Record `assets/sfx/sfx_manifest.json` before wiring many triggers so missing sounds are visible.

## References

- Use `references/manifest-patterns.md` when creating or repairing SFX manifests.

## Validation Commands

Adapt to the project, but start with:

```sh
node --check src/main.js
python3 -m json.tool assets/sfx/sfx_manifest.json >/dev/null
python3 -m json.tool assets/asset_manifest.json >/dev/null
```

For Godot projects, also run available headless smoke scripts from the project docs.

