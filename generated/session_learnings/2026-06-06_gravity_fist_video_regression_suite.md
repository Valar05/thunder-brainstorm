# Gravity Fist Three.js Video Regression Suite - Session Learnings

Date: 2026-06-06

## Trigger

The newest Android screen recording in Downloads showed orientation and timing/readability problems in the Gravity Fist Three.js port. The useful workflow was to extract frames, count visible issues, then convert them into in-page regression beacons before fixing runtime behavior.

## Video Issues Counted

10 issues were grouped into regression checks:

1. Portrait recording used a tiny 16:9 landscape band instead of filling the browser surface.
2. Large unused black/browser area reduced gameplay readability.
3. Diagnostics panel blocked combat.
4. Floating joystick could overlap the health HUD.
5. Support enemies could face their movement slot instead of the player.
6. Player/enemy facing during contact needed stronger automated orientation checks.
7. Damage timing needed active-window proof, not just visual guessing.
8. Enemy attack hold needed a readable standing attack pose.
9. Enemy cap/crowding made live combat hard to parse.
10. Knockdown/prone/death silhouettes needed continued state-lineup protection.

## Implemented Test

`gravity-fist-threejs/src/main.js` now exposes `?test=video-regression-suite`. Run it with Android capture:

```sh
node tools/android_browser_capture.mjs --full-assets --path='/?test=video-regression-suite' --frames=3 --frame-interval-ms=500 --timeout-ms=70000 --out=/data/data/com.termux/files/usr/tmp/gf-three-android/video-regression-suite.png
```

The suite publishes individual `stage=test` beacons for:

- `portrait-viewport-fill`
- `debug-panel-hidden-by-default`
- `joystick-clears-health-hud`
- `active-enemy-count-readable`
- `support-enemies-face-player`
- `enemy-damage-active-window-only`
- `enemy-attack-hold`
- `knockdown-threshold`
- `titan-state-lineup`
- `lineup-orientation-yaw`

The first red run failed 6/10 checks: portrait fill, debug visibility, joystick safe top, active enemy cap, support-facing, and an overly strict yaw assertion. The corrected pass had 0 failures with full assets loaded.

## Runtime Changes Preserved

- `styles.css` fills the phone viewport instead of enforcing a 16:9 letterbox.
- `index.html` shows diagnostics only with `?debug=1` and cache-busts the JS module to `0.4.8`.
- `src/main.js` uses a portrait camera base, clamps joystick origins below the HUD, reduces active enemy cap to 3, increases minimum respawn interval to 1.0s, and makes support enemies face the player after moving to their slot.
- `PROJECT_ORIENTATION.md` now treats forced landscape letterboxing as a phone-recording regression.

## Validation Evidence

Passing report:

```text
/data/data/com.termux/files/usr/tmp/gf-three-android/video-regression-suite-pass1.json
```

Representative capture:

```text
/data/data/com.termux/files/usr/tmp/gf-three-android/video-regression-suite-pass1_frame_000.png
```

Static/build validation:

```sh
node --check src/main.js
python3 -m json.tool data/player_attacks.json >/dev/null
python3 -m json.tool data/security_titan.json >/dev/null
python3 -m json.tool assets/asset_manifest.json >/dev/null
python3 tools/build_web_release.py
```

Release archive rebuilt:

```text
/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/release/gravity-fist-threejs-web.zip
```

## Android Capture Caveat

The Android browser capture harness can still report `no-browser-requests` when `am` or `termux-open-url` returns success but the browser does not fetch the local URL. Treat that as a launcher/lock-state failure when reports show zero requests, not as a runtime parse failure. The passing regression report did load the page, full assets, beacons, and PNG captures.
