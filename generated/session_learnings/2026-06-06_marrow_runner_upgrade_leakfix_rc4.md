# Marrow Runner Upgrade Branch And Leak-Fix RC4 Lessons

## Release Snapshot

Standalone project:

```text
/storage/emulated/0/Documents/GodotProjects/marrow-runner
```

Itch target used successfully in this pass:

```text
valarsbeard/marrow-runner:html
```

Published build:

```text
version: v0.9.0-rc4
channel: html
upload: #17807876
build: #1710635 (from #1707945)
zip: release/marrow-runner-v0.9.0-rc4-web.zip
```

The older `grailawakeninggames/marrow-runner:html` target returned `bad user` with the current butler API key. Treat `valarsbeard/marrow-runner:html` as the working upload target unless the itch account setup changes.

## Upgrade Implementation Lessons

- Extend the existing additive mutation model rather than creating a parallel upgrade system. `currentRun.mutations`, `chooseMutationOffers()`, `drawMutationOffers()`, and `applyMutationChoice()` are the correct path.
- The four active branch surfaces are Pseudopod Impact, Complement Storm, Antibody Orbit, and Blood Slipstream. The block-breaking route lives inside Pseudopod Impact through Ram Breach, Knockback Excavation, Marrow Drill, and Tunnel Current.
- Blood Slipstream became the missing movement/pressure branch: antibody pickups and complement can create short speed currents, Quick Clot Rearm makes ram easier to rearm, and Hematic Afterimage/Red Cell Halo convert movement into fever relief.
- Capstones and synergies should stay additive and conditional. Cross-branch synergies such as Lysis Wave, Hemoglobin Current, Red Cell Halo, Cytokine Breaker, Opsonin Slingshot, Serum Storm, and Tunnel Current work because they reward mixed investment without replacing base branch behavior.
- The temporary `ram_breach` starter grant should remain removed for release builds. It was useful for tuning but undermined the intended branch choice.

## Runtime Leak / Choppiness Lesson

The reported symptom was that each New Run became choppier. The code did not show a simple per-run event-listener leak, but the safer fix was to harden the lifecycle around run replacement:

- Add a single input-binding guard so `bindInput()` cannot register duplicate listeners if startup/error paths run again.
- Add a single animation-loop guard so `requestAnimationFrame(loop)` cannot be started twice.
- Dispose old state before replacing it: stop sound loops, clear held input, reset joystick, clear canvas/game-surface transforms, clear feedback particles and particle pools, and remove stale button bounds.
- Debounce fullscreen/resize rebuilds and cancel pending viewport resets before starting a new run. Mobile browsers can fire resize/fullscreen bursts that otherwise rebuild the run shortly after New Run.
- Keep harness counters for future repros: `runSerial`, feedback particle count, particle-pool count, transforms, and event counts make churn tests easier.

## Validation Commands Used

From `marrow-runner`:

```sh
node --check src/main.js
python3 -m json.tool assets/asset_manifest.json >/dev/null
python3 -m json.tool assets/sfx/sfx_manifest.json >/dev/null
python3 -m json.tool release/page_assets/page_asset_manifest.json >/dev/null
python tools/build_itch_release.py
python3 - <<'PY'
import zipfile
with zipfile.ZipFile('release/marrow-runner-v0.9.0-rc4-web.zip') as z:
    print('bad', z.testzip(), 'entries', len(z.namelist()))
PY
```

Termux Chromium DOM smoke reached the page with the usual Android dbus/proxy noise. DevTools remote-debug automation was not reliable in this Termux Chromium run, so future repeated-run profiling should either use a real browser console or a tiny in-page churn harness.

## Git / Workspace Note

The standalone Marrow Runner repo is a git repo on branch `main`, but no remote was configured during this pass. Thunder Brainstorm in this workspace did not have its own `.git` directory, so this lesson note is local Thunder documentation rather than a Thunder git commit.
