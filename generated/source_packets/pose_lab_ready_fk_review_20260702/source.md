# Pose Lab Ready Weapon FK Follow Review Packet

## Mission
Review the latest Codex-authored commit as a red-build code review. The human feedback is:

> red build no op no new screenshots, static code churn.

Assume the visual bug is NOT fixed until a fresh screenshot proves it.

## Repository / Branch
- Repo: Valar05/pose-lab
- Local worktree: /storage/emulated/0/Documents/GodotProjects/pose-lab-quartermaster
- Branch: codex/meshy-pose-salvage-from-main
- Latest commit under review: fb9277f `Fix Meshy Ready weapon FK follow order`
- Base before latest commit: 3499b1a

## Fresh User Visual Evidence Before Latest Commit
- T-pose screenshot: `/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-130645.png`
  - Visual read: T-pose weapon placement is correct / acceptable.
- Ready screenshot: `/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-130642.png`
  - Visual read: Ready hands look corrected, but the sword stays in rest/T-pose orientation instead of following the final right-hand FK pose.
- No post-fix screenshot exists. That is the user's current red-build complaint.

## Constraints / Repository Truth
- Manual weapon placement literals are repository truth and must not be changed casually.
- Accepted Ready clip should remain pose-only: do not promote old `weaponKeyConvert`, `Weapon.R`, or `WeaponGrip` animation tracks.
- If a code change claims to fix the visual sword follow bug without fresh visual proof, treat that as unproven.
- Review should prioritize whether the latest commit is a real runtime behavior fix or merely static/test churn.

## Latest Commit Summary
```text
fb9277f (HEAD -> codex/meshy-pose-salvage-from-main) Fix Meshy Ready weapon FK follow order
 .../meshy_ready_weapon_fk_follow_latest.json       | 25 +++++++++
 pose-lab.html                                      |  4 +-
 src/pose-lab.js                                    |  9 +--
 tools/test_meshy_full_body_weapon_attachment.mjs   |  5 +-
 .../test_meshy_ready_weapon_fk_follow_contract.mjs | 64 ++++++++++++++++++++++
 5 files changed, 99 insertions(+), 8 deletions(-)

```

## Current Dirty State
```text
?? generated/test_runs/socket-solver-29727/
?? generated/test_runs/socket-solver-29911/
?? generated/test_runs/socket-solver-30187/

```

Untracked generated socket-solver directories are diagnostic leftovers and not part of this review.

## Branch Diff Stat From Main
```text
 .../meshy_ready_weapon_fk_follow_latest.json       |  25 +
 pose-lab.html                                      |   4 +-
 src/meshy-ready-runtime.mjs                        | 540 +++++++++++++++++++++
 src/pose-lab.js                                    |  55 ++-
 src/rig-profiles.js                                |  73 +--
 tools/test_bone_touch_selection.mjs                |   4 +
 tools/test_meshy_core_retarget_contract.mjs        |  29 +-
 tools/test_meshy_full_body_weapon_attachment.mjs   |   5 +-
 tools/test_meshy_pose_parity_arm_contract.mjs      |  41 +-
 .../test_meshy_ready_weapon_fk_follow_contract.mjs |  64 +++
 tools/test_meshy_visual_ik_ready_pose_contract.mjs |  24 +
 tools/test_meshy_weapon_path_ik.mjs                |  19 +-
 tools/test_no_cache_server_contract.mjs            |  12 +-
 13 files changed, 769 insertions(+), 126 deletions(-)

```

## Latest Commit Diff
```diff
diff --git a/generated/visual_red_build/meshy_ready_weapon_fk_follow_latest.json b/generated/visual_red_build/meshy_ready_weapon_fk_follow_latest.json
new file mode 100644
index 0000000..0484fd8
--- /dev/null
+++ b/generated/visual_red_build/meshy_ready_weapon_fk_follow_latest.json
@@ -0,0 +1,25 @@
+{
+  "schema": "pose-lab-ready-weapon-fk-red-build-v1",
+  "generatedAt": "2026-07-02T13:06:45-05:00",
+  "observedCacheToken": "pose-editor-130",
+  "currentFixCacheToken": "pose-editor-131",
+  "runtimeBuild": "meshy-fps-sword-upper-body-retarget",
+  "actorKey": "meshyCharacter",
+  "readyClipName": "OneHandReady -> meshyCharacter [FPS-VISUAL-IK R-120 L-90]",
+  "tPoseClipName": "0T-Pose -> meshyCharacter:FPS-REST-ARMS-CAL--120",
+  "tPoseCapturePath": "/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-130645.png",
+  "readyCapturePath": "/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-130642.png",
+  "visualRead": "Fresh Android screenshots show Meshy Character T-pose weapon placement is correct, while the Ready clip has corrected hands but the visible sabre remains in rest/T-pose orientation instead of following the final right-hand FK pose.",
+  "visualAssertions": {
+    "freshAndroidScreenshotsInspected": true,
+    "tPoseWeaponPlacementAccepted": true,
+    "readyHandsCorrected": true,
+    "readySwordNotFollowingFinalFk": true,
+    "failureIsRuntimeWeaponFollowNotPoseRetarget": true,
+    "manualWeaponPlacementMustRemainLocked": true,
+    "normalReadyClipMustNotKeyWeaponGrip": true,
+    "expectedNextReadySwordFollowsFinalRightHandFk": true,
+    "freshPostFixScreenshotRequired": true
+  },
+  "nextVerificationUrl": "http://127.0.0.1:8798/pose-lab-quartermaster/pose-lab.html?mode=standard&actor=meshyCharacter&clip=OneHandReady%20-%3E%20meshyCharacter%20%5BFPS-VISUAL-IK%20R-120%20L-90%5D&weaponDebug=1&cacheBust=pose-salvage-fk-follow-20260702"
+}
diff --git a/pose-lab.html b/pose-lab.html
index b6c44ce..395bf55 100644
--- a/pose-lab.html
+++ b/pose-lab.html
@@ -328,11 +328,11 @@
         './vendor/three/examples/jsm/controls/OrbitControls.js',
         './vendor/three/examples/jsm/utils/SkeletonUtils.js',
         './src/godot-rest-poses.js?v=pose-editor-128',
-        './src/rig-profiles.js?v=pose-editor-130',
+        './src/rig-profiles.js?v=pose-editor-131',
         './src/startup-policy.mjs?v=pose-editor-128',
         './src/clip-search.js?v=pose-editor-128',
         './src/lab-mode.mjs?v=pose-editor-128',
-        './src/pose-lab.js?v=pose-editor-130',
+        './src/pose-lab.js?v=pose-editor-131',
       ];
       show('Booting module...');
       window.addEventListener('error', (event) => {
diff --git a/src/pose-lab.js b/src/pose-lab.js
index 8395782..f965171 100644
--- a/src/pose-lab.js
+++ b/src/pose-lab.js
@@ -5,13 +5,13 @@ import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
 import { clone as cloneSkinnedObject, retargetClip } from 'three/addons/utils/SkeletonUtils.js';
 import { applyGodotRestPose } from './godot-rest-poses.js?v=pose-editor-128';
 import { buildMeshyFpsVisualIkReadyClip } from './meshy-ready-runtime.mjs?v=pose-editor-130';
-import { RIG_PROFILES, actorTransform, clipOptions } from './rig-profiles.js?v=pose-editor-130';
+import { RIG_PROFILES, actorTransform, clipOptions } from './rig-profiles.js?v=pose-editor-131';
 import { preferSavedClipForActor } from './startup-policy.js?v=pose-editor-128';
 import { resolveLabMode } from './lab-mode.mjs?v=pose-editor-128';
 import { clipLabel, defaultClipEntries, isSf2PoseClip, searchableClipEntries, searchClipEntries } from './clip-search.js?v=pose-editor-128';
 
 const LAB_BUILD = 'meshy-fps-sword-upper-body-retarget';
-const LAB_CACHE_TOKEN = 'pose-editor-130';
+const LAB_CACHE_TOKEN = 'pose-editor-131';
 const LAB_MODE = resolveLabMode(window.location.search || '');
 const STATUS_PREFIX = LAB_MODE === 'critique' ? 'critique' : 'lab';
 
@@ -4569,10 +4569,11 @@ class PoseActor {
     this.activeAction = next;
     if (!this.applyCritiqueClipState(next._clip)) this.resetAllBoneEdits();
     this.mixer.setTime(0);
+    this.reapplyBoneEdits();
     this.applyGrounding();
+    this.updateWeaponProxyVisibility();
     this.updateDebugHelpers();
     this.updateBoneOverlay();
-    this.updateWeaponProxyVisibility();
     this.rememberClip(name);
   }
 
@@ -4629,9 +4630,9 @@ class PoseActor {
 
   update(dt) {
     this.mixer.update(dt);
-    this.updateWeaponProxyVisibility();
     this.reapplyBoneEdits();
     this.applyGrounding();
+    this.updateWeaponProxyVisibility();
     this.updateLegSymmetryOverlay();
     this.updateDebugHelpers();
     this.updateBoneOverlay();
diff --git a/tools/test_meshy_full_body_weapon_attachment.mjs b/tools/test_meshy_full_body_weapon_attachment.mjs
index 80a42d4..7a34e2e 100644
--- a/tools/test_meshy_full_body_weapon_attachment.mjs
+++ b/tools/test_meshy_full_body_weapon_attachment.mjs
@@ -30,10 +30,11 @@ assert(js.includes('weaponDebugForceVisible()') && js.includes('weaponDebugForce
 for (const metric of ['hiltToHandDistance', 'bladeLength', 'basketFrontErrorDeg', 'socketForwardToBladeErrorDeg']) {
   assert(js.includes(metric), `live weapon diagnostics should expose ${metric}`);
 }
-assert(profiles.includes("clipTag: 'FPS-SWORD-UPPER'") && profiles.includes("sourceHand: 'Hand.R'") && profiles.includes("leftHandBone: 'LeftHand'"), 'FPS-SWORD-UPPER should convert authored Hand.R/Weapon.R upper-body contribution and keep a Meshy socket');
+assert(profiles.includes("clipTag: 'FPS-VISUAL-IK-GOLDEN'") && profiles.includes("retargetMode: 'meshy-fps-visual-ik-ready'") && profiles.includes("leftHandBone: 'LeftHand'"), 'FPS-VISUAL-IK Ready should keep the real Meshy socket without promoting the old FPS-SWORD-UPPER weapon path');
+assert(!profiles.includes("sourceWeapon: 'Weapon.R'") && !profiles.includes("targetWeapon: 'WeaponGrip'"), 'accepted Ready pose should not emit authored weapon tracks; runtime socket follows final FK');
 assert(!profiles.includes("{ from: 'mixamorigHips', to: 'Hips'"), 'rejected full-body hips mapping must not remain');
 assert(manifest.includes('meshy_french_revolution_sabre_runtime_glb') && manifest.includes('WeaponGrip'), 'asset manifest should document the Meshy sabre runtime socket');
 assert(manifest.includes('meshy_character_sheet_fps_sword_upper_clip_binding'), 'asset manifest should document the FPS sword upper-body Meshy clip binding');
 
 if (failures.length) throw new Error(failures.join('\n'));
-console.log(JSON.stringify({ checked: ['meshy-upper-body-fps-sword', 'real-sabre-weapongrip-attachment', 'manifested-sabre-provenance'] }, null, 2));
+console.log(JSON.stringify({ checked: ['meshy-visual-ik-ready-socket-follow', 'real-sabre-weapongrip-attachment', 'manifested-sabre-provenance'] }, null, 2));
diff --git a/tools/test_meshy_ready_weapon_fk_follow_contract.mjs b/tools/test_meshy_ready_weapon_fk_follow_contract.mjs
new file mode 100644
index 0000000..021bc75
--- /dev/null
+++ b/tools/test_meshy_ready_weapon_fk_follow_contract.mjs
@@ -0,0 +1,64 @@
+import fs from 'node:fs';
+import path from 'node:path';
+
+const projectRoot = path.resolve(import.meta.dirname, '..');
+const runtimePath = path.join(projectRoot, 'src', 'pose-lab.js');
+const profilesPath = path.join(projectRoot, 'src', 'rig-profiles.js');
+const evidencePath = path.join(projectRoot, 'generated', 'visual_red_build', 'meshy_ready_weapon_fk_follow_latest.json');
+const runtime = fs.readFileSync(runtimePath, 'utf8');
+const profiles = fs.readFileSync(profilesPath, 'utf8');
+const failures = [];
+function assert(condition, message) { if (!condition) failures.push(message); }
+
+function currentCacheToken() {
+  const match = runtime.match(/const\s+LAB_CACHE_TOKEN\s*=\s*['"]([^'"]+)['"]/);
+  return match?.[1] || '';
+}
+
+function assertOrdered(source, markers, label) {
+  let cursor = -1;
+  for (const marker of markers) {
+    const next = source.indexOf(marker, cursor + 1);
+    assert(next > cursor, `${label}: expected marker after previous marker: ${marker}`);
+    cursor = next;
+  }
+}
+
+assert(fs.existsSync(evidencePath), 'missing ready weapon FK visual red-build evidence artifact');
+const evidence = JSON.parse(fs.readFileSync(evidencePath, 'utf8'));
+assert(evidence.schema === 'pose-lab-ready-weapon-fk-red-build-v1', 'ready weapon FK evidence schema mismatch');
+assert(evidence.currentFixCacheToken === currentCacheToken(), `evidence currentFixCacheToken should match ${currentCacheToken()}`);
+assert(fs.existsSync(evidence.tPoseCapturePath), 'T-pose screenshot evidence path should exist');
+assert(fs.existsSync(evidence.readyCapturePath), 'Ready screenshot evidence path should exist');
+assert(evidence.visualAssertions?.tPoseWeaponPlacementAccepted === true, 'evidence should record accepted T-pose weapon placement');
+assert(evidence.visualAssertions?.readyHandsCorrected === true, 'evidence should record corrected Ready hands');
+assert(evidence.visualAssertions?.readySwordNotFollowingFinalFk === true, 'evidence should record the red Ready sword FK-follow failure');
+assert(evidence.visualAssertions?.expectedNextReadySwordFollowsFinalRightHandFk === true, 'evidence should state the next visible acceptance target');
+
+assertOrdered(runtime, [
+  'this.mixer.setTime(0);',
+  'this.reapplyBoneEdits();',
+  'this.applyGrounding();',
+  'this.updateWeaponProxyVisibility();',
+  'this.updateDebugHelpers();',
+], 'clip start should update weapon after final pose edits');
+
+const updateStart = runtime.indexOf('  update(dt) {');
+const updateEnd = runtime.indexOf('\n  }', updateStart + 1);
+const updateBlock = runtime.slice(updateStart, updateEnd);
+assertOrdered(updateBlock, [
+  'this.mixer.update(dt);',
+  'this.reapplyBoneEdits();',
+  'this.applyGrounding();',
+  'this.updateWeaponProxyVisibility();',
+  'this.updateLegSymmetryOverlay();',
+], 'per-frame update should make weapon follow final FK pose');
+
+assert(runtime.includes('proxy.root.quaternion.copy(modelWorldQuat.multiply(worldQuaternionOf(proxy.rightHand))).normalize();'), 'synthetic WeaponGrip should copy final right-hand world rotation when no socket track exists');
+assert(!profiles.includes("targetWeapon: 'WeaponGrip'") && !profiles.includes("sourceWeapon: 'Weapon.R'"), 'normal Ready clip must not key WeaponGrip or Weapon.R');
+assert(!profiles.includes('weaponKeyConvert: {'), 'normal Ready profile must not re-enable weapon conversion');
+assert(profiles.includes('handLocalOffset: [0.095, 0.035, -0.01]') && profiles.includes('modelLocalOffset: [-0.11512, 0.00773, -0.01127]'), 'Meshy manual weapon socket placement must remain locked');
+assert(profiles.includes('rotationDeg: [90, 0, -55.145]') && profiles.includes('gripLocalPosition: [0.6535, -0.02302, -0.07317]'), 'Meshy manual saber attachment placement must remain locked');
+
+if (failures.length) throw new Error(failures.join('\n'));
+console.log(JSON.stringify({ checked: ['ready-weapon-fk-red-evidence', 'weapon-after-final-pose-order', 'manual-saber-literals-locked'], evidencePath: path.relative(projectRoot, evidencePath), cacheToken: currentCacheToken() }, null, 2));

```
