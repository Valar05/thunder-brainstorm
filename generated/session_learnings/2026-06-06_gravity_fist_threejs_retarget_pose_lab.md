# Gravity Fist Three.js Retarget Pose Lab - Session Learnings

Date: 2026-06-06

## Durable Paths

- Browser pose lab: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/pose-lab.html`
- Pose lab runtime: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/src/pose-lab.js`
- Pose lab styles: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs/src/pose-lab.css`
- Phalanx source reference: `/storage/emulated/0/Documents/GodotProjects/phalanx/docs/PROJECT_HANDOFF.md`

## Implemented Slice

The Gravity Fist Three.js pose lab now has a Retarget panel that can build clips from one loaded actor to another. The current loaded rigs are Ares and SecurityTitan.

Correction added after user feedback: the first pass was only a GLB retarget/channel wrapper. The current pass adds actual Phalanx-style loaded-skeleton editing through a Bones panel.

Bone controls:

- Bone dropdown populated from the selected actor's real loaded skeleton.
- Visible bone handles and parent lines in the scene.
- Tap/click selection of visible bone handles.
- Independent local Translate, Rotate, and Scale toggles for the selected bone.
- Local Move X/Y/Z, Rotate X/Y/Z, and Scale sliders.
- Reset selected bone and reset all edited bones.
- Bone status/readout with raw bone name, edit count, local delta, channel mask, and scale.

Retarget controls:

- Source actor selector.
- Target actor selector.
- Independent Translate, Rotate, and Scale channel toggles.
- Position policy selector: hips only, all keyed, or none.
- Build and Swap buttons.

The Xform panel now separates:

- Move X/Y/Z.
- Rotate X/Y/Z.
- Scale.
- Basis X/Y/Z.

This follows the Phalanx lesson that transform concerns should stay separable during diagnosis. Instead of treating pose editing as one combined mode, retarget tests can isolate whether translation tracks, quaternion rotation tracks, or scale tracks are causing a bad transfer.

Bone edits are local to the selected actor and reapply after the animation mixer updates, so they can be used over a stopped pose or a playing clip. This is not yet Phalanx IK/foot-anchor editing; it is the browser-side foundation for real bone selection and local transform diagnosis.

## Retargeting Boundary

This is a practical browser-lab foundation, not a solved universal retargeter. It still uses Three.js `SkeletonUtils.retargetClip` and will work best when the source and target rigs have compatible humanoid structure and discoverable hip/bone names.

Treat retarget quality as a silhouette/readability test:

1. Correct actor Move/Rotate/Scale/Basis first.
2. Build Rotate-only retargets before adding translation.
3. Add hips-only translation next.
4. Use all keyed translation only when the source rig's authored positions make sense for the target.
5. Keep scale disabled unless the source clip intentionally animates scale and the target tolerates it.

## Validation

Validated:

```sh
node --check src/pose-lab.js
node --check src/main.js
python3 -m json.tool assets/asset_manifest.json >/dev/null
python3 tools/build_web_release.py
curl -I http://127.0.0.1:8793/pose-lab.html
```

Termux Chromium DOM smoke confirmed the Retarget panel and new Xform controls were present. Headless Chromium with `--disable-gpu` reported `Error creating WebGL context`, which is expected for this WebGL page on this Termux headless path. A no-`--disable-gpu` run was unstable in Chromium itself, so final visual judgment still needs a real browser session.
