# Gravity Fist Three.js / itch.io Correction

Date: 2026-06-06

## Correction

The final target is not a Godot Web export. The final target is the Three.js browser project at `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs`, hosted on itch.io as an HTML5 game. The Godot project at `/storage/emulated/0/Documents/GodotProjects/gravity-fist` remains the source of truth for combat design, attack data, animations/assets, and behavior references.

The earlier Thunder packet `generated/design_packets/gravity_fist_vertical_slice_plan_2026-06-06.md` is still useful for feature phasing, but all platform/build tasks should be read through this correction:

- Replace "Godot Web export preset" with "Three.js static web release package".
- Replace "Godot browser smoke" with "local HTTP + Chromium/browser smoke against `gravity-fist-threejs/index.html`".
- Replace "Godot dedicated server first" with "server-authoritative networking plan for a Three.js client, with Godot source logic translated or reimplemented server-side as needed".
- Keep Godot as reference/source of truth, not the shipped runtime.

## Current Three.js Project Orientation

Project: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs`

Entry points:

- `index.html`: itch/browser entry point with CDN import map for Three.js.
- `src/main.js`: Three.js scene, fixed-step simulation, phone gestures, combat, AI, audio, and rendering.
- `styles.css`: fullscreen phone-first layout and HUD.
- `data/player_attacks.json`: copied from the active Godot source project.
- `data/security_titan.json`: copied from the active Godot source project.
- `assets/asset_manifest.json`: provenance for copied Godot assets.
- `tools/build_web_release.py`: deterministic zip builder.
- `release/gravity-fist-threejs-web.zip`: current itch-ready package shape.

Local project docs already state that this is a browser port of the current Godot combat vertical slice, not a progression-system rewrite. The source Godot move shop/progression stack remains intentionally excluded unless explicitly revived.

## Current Validation

Validated on 2026-06-06:

```sh
node --check src/main.js
python3 -m json.tool data/player_attacks.json >/dev/null
python3 -m json.tool data/security_titan.json >/dev/null
python3 -m json.tool assets/asset_manifest.json >/dev/null
python3 tools/build_web_release.py
```

Result: all passed. The release builder wrote `release/gravity-fist-threejs-web.zip` with 34 entries.

## itch.io Packaging Notes

Official itch.io HTML5 upload docs require a ZIP containing the game files, including an `index.html` entry point. The current Three.js release package satisfies the basic package shape: `index.html` is at the zip root.

Relevant docs checked:

- itch.io HTML5 upload docs: `https://itch.io/docs/creators/html5`
- butler push docs: `https://itch.io/docs/butler/pushing.html`

For a release pass, use the existing release-operator/butler workflow only after a browser smoke test confirms the package boots locally.

## Updated Phase 0

Goal: make the Three.js build the verified shipping target while preserving Godot as source of truth.

Tasks:

1. Keep `/storage/emulated/0/Documents/GodotProjects/gravity-fist` as source reference; do not edit the archive mirror under `gothic-throne`.
2. Keep `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs` as the active implementation target.
3. Add or maintain a clear source-sync workflow: attack JSON, GLBs/textures/audio, and behavior notes copied from Godot into Three.js with provenance in `assets/asset_manifest.json`.
4. Add an explicit smoke command set for Three.js: `node --check`, JSON validation, build zip, local HTTP server, browser/Chromium smoke.
5. Ensure the release zip keeps `index.html` at the root and includes all local assets needed by itch.io.
6. Decide whether to vendor Three.js locally for itch/offline robustness. Current `index.html` imports Three.js from `unpkg.com`; that is simple, but local vendoring avoids CDN dependency and is safer for a packaged itch build.
7. Keep Godot Web export out of the plan unless we intentionally need it for comparison or asset extraction.

## Updated Feature Phasing

Feature phases remain mostly the same, but implementation lands in `gravity-fist-threejs/src/main.js` and adjacent web assets:

1. Combat meter and special HUD in Three.js.
2. Gravity Fist slam as the first meter spend.
3. Remove any normal jump-equivalent from the Three.js live controls; keep aerial force as a special only.
4. Contextual specials from existing Godot-derived attack data.
5. Grab state in Three.js simulation using Godot behavior as reference.
6. Enemy archetypes via Three.js data/constructor variants, with Godot AI conductor as the behavior reference.
7. Segment-based scrolling roguelike level generation in Three.js, using Godot walkway/container assets first.
8. Browser polish: silhouettes, hit flashes, motion streaks, special-only blur, camera shake, audio layering.
9. itch.io package and butler upload after local browser smoke.

## Networking Correction

The networked play target should be planned as a Three.js web client. For secure low-maintenance co-op:

- Client sends input intentions, not damage results.
- Server owns enemy AI, hit validation, health, meter, wave state, rewards, and run state.
- Godot can remain the design reference, but a shipped authoritative server must either reimplement the relevant combat rules in JavaScript/TypeScript or run a separate authoritative runtime that speaks to the Three.js client.
- For the first multiplayer slice, prefer a small Node/WebSocket authoritative prototype before committing to a managed provider.
- W4 Cloud is less directly aligned now because the client is Three.js, not Godot-native. It may still be useful only if a Godot server remains part of the architecture.

## Immediate Next Slice

1. Add a Three.js implementation backlog file or update `PROJECT_ORIENTATION.md` with the corrected final target.
2. Vendor Three.js/addons locally or explicitly accept CDN dependency for early prototypes.
3. Add special meter/HUD to `src/main.js` and `index.html`.
4. Add Gravity Fist slam as meter spend using current stomp/nova assets as placeholder if the exact animation is not ready.
5. Build zip and smoke locally before any itch upload.
