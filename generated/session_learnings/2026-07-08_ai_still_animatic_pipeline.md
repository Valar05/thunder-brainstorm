# AI Still-Frame Animatic Pipeline Lessons

Date: 2026-07-08

## Pattern

A practical AI-video pipeline on Android/Termux is not full generated animation first. The stable slice is:

1. Write a beat packet with duration, dialogue, character locks, style contract, and acceptance criteria.
2. Generate a concept sheet and optional 3D/Meshy scaffold to stabilize silhouette and costume grammar.
3. Generate one still per beat with repeated continuity nouns and a style that tolerates painterly drift.
4. Generate one TTS clip per beat, not one monolithic track.
5. Assemble a browser animatic for review and an MP4/GIF/WAV export set for sharing.
6. Keep prompts, manifests, generated asset paths, provider task ids, and final export paths together.

## Doctrine

- Animatic first. Do not spend the first pass solving 24 fps motion when key frames, timing, and voice will answer whether the scene works.
- Style can be a technical control surface. Noir ink, watercolor, historical painting, and surreal shadow language make small face and texture variance less damaging than clean photorealism.
- Meshy is useful even when final frames are generated stills. A model or rig can anchor pose language, camera angles, silhouette, and asset provenance.
- The portable artifact matters. Browser playback is a review surface; MP4 is the handoff.
- Toolchain health is part of the creative pipeline. Broken ffmpeg or media indexing blocks the artifact as surely as a bad prompt.

## Android/Termux Tooling Note

The July 2026 Holding Vigil run hit a Termux ffmpeg linker failure through `libplacebo`:

```text
cannot locate symbol __from_chars_floating_point... referenced by libplacebo.so
```

The symbol existed in Termux `libc++_shared.so`; the failing environment omitted `/data/data/com.termux/files/usr/lib` from the effective library search path. A practical fix was to reconfigure the package with the correct `LD_LIBRARY_PATH` and add `$HOME/bin/ffmpeg` and `$HOME/bin/ffprobe` wrappers that prepend `/data/data/com.termux/files/usr/lib` before execing the real binaries.

## Pain Points

- Still generation created occasional baked text and face variance; prompts and crops must forbid signage/text and lean into painterly style.
- Cartesia voice generation needs a speaker-profile preflight so default voices do not silently stand in for character casting.
- The Meshy rig was not yet used as an active renderer for camera-locked pose sheets.
- MP4 creation was assembled manually after ffmpeg repair; it should be one command.
- Android media scanner refresh needs to be part of export automation.

## Build Next

Create a reusable `ai_animatic_packet` workflow script or skill with these commands:

- `check-ffmpeg`
- `build-stills`
- `build-voice`
- `make-mp4`
- `export-android`
- `audit-packet`

The first acceptance test should assert that a packet can produce a final MP4 with expected duration, H.264 video, AAC audio, and a manifest listing every source prompt and final exported file.
