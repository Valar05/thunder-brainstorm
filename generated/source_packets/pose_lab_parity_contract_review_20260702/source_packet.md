# Pose Lab Parity Contract Review Source Packet

Generated: 2026-07-02T19:24:12.755147Z
Repo: /storage/emulated/0/Documents/GodotProjects/pose-lab-quartermaster
Branch: codex/meshy-pose-salvage-from-main
Commit under review: 546e65055121f4abad88cb446cbfb8f66458b54d

## Mission Context

The user requested an ironclad offline/web truth parity contract for a visual red build. Browser capture is deprecated as acceptance proof. The current build must remain red until offline truth, observed web truth, and linked artifacts agree that the Meshy Ready sword follows final FK and is visible.

Review the latest commit only. Do not review stale GitHub PR #2 findings unless visible in this commit.

## Current Working Tree

```text
?? generated/test_runs/socket-solver-29727/
?? generated/test_runs/socket-solver-29911/
?? generated/test_runs/socket-solver-30187/

```

Known untracked scratch dirs are pre-existing generated test runs and are not part of this review.

## Validation Already Run

Passing:
- node --check tools/pose_lab_workflow_lib.mjs
- node --check tools/meshy_ready_weapon_offline_visual_truth.mjs
- node --check src/pose-lab.js
- node --check src/ready-weapon-truth.mjs
- node --check tools/test_offline_web_parity_promotion_contract.mjs
- node tools/meshy_ready_weapon_offline_visual_truth.mjs -> result red, observed=sword-rest-space, offline=sword-hidden, visibility=weapon-hidden
- node tools/test_pose_lab_visual_red_build_contract.mjs
- node tools/test_offline_web_parity_promotion_contract.mjs
- node tools/test_manual_weapon_placement_lock.mjs
- node tools/test_meshy_weapon_path_ik.mjs
- node tools/test_meshy_visual_ik_ready_pose_contract.mjs
- node tools/test_visual_qa_instructions.mjs
- git diff --check
- python3 -m json.tool on the three changed JSON artifacts

Expected failing red gate:
- node tools/test_meshy_ready_weapon_fk_follow_contract.mjs fails with: RED BUILD: offline/web truth parity not fixed: observed=sword-rest-space offline=sword-hidden visibility=weapon-hidden parityFailure=offline-web-visual-class-diverged

## Commit Stat

```text
546e650 Harden offline web parity evidence readback
 .../meshy_ready_weapon_fk_follow/visual_truth.json |  11 ++-
 .../meshy_ready_weapon_fk_follow_latest.json       |  11 ++-
 ..._ready_weapon_fk_follow_observed_web_truth.json |   9 +-
 tools/meshy_ready_weapon_offline_visual_truth.mjs  |   4 +
 tools/pose_lab_workflow_lib.mjs                    |  70 +++++++++++++-
 .../test_offline_web_parity_promotion_contract.mjs | 102 ++++++++++++++++++---
 tools/test_pose_lab_visual_red_build_contract.mjs  |   3 +
 7 files changed, 188 insertions(+), 22 deletions(-)

```

## Full Latest Commit Diff

```diff
commit 546e65055121f4abad88cb446cbfb8f66458b54d
Author:     ValarsPhone <dclarke1005@gmail.com>
AuthorDate: Thu Jul 2 14:19:58 2026 -0500
Commit:     ValarsPhone <dclarke1005@gmail.com>
CommitDate: Thu Jul 2 14:19:58 2026 -0500

    Harden offline web parity evidence readback

diff --git a/generated/offline_visual_truth/meshy_ready_weapon_fk_follow/visual_truth.json b/generated/offline_visual_truth/meshy_ready_weapon_fk_follow/visual_truth.json
index c2f9f6d..a7953ae 100644
--- a/generated/offline_visual_truth/meshy_ready_weapon_fk_follow/visual_truth.json
+++ b/generated/offline_visual_truth/meshy_ready_weapon_fk_follow/visual_truth.json
@@ -1,110 +1,117 @@
 {
   "schema": "pose-lab-offline-web-truth-parity-ready-weapon-fk-v1",
-  "generatedAt": "2026-07-02T19:07:36.928Z",
+  "generatedAt": "2026-07-02T19:19:28.834Z",
   "proofMode": "offline-web-truth-parity",
   "browserCaptureDeprecated": true,
   "sourceActor": "FPS Arms",
   "targetActor": "Meshy Character",
   "actorKey": "meshyCharacter",
   "clipName": "OneHandReady -> meshyCharacter [FPS-VISUAL-IK R-120 L-90]",
   "runtimeBuild": "meshy-fps-sword-upper-body-retarget",
   "cacheToken": "pose-editor-131",
   "sharedTruthModule": "src/ready-weapon-truth.mjs",
   "observedWebTruthPath": "generated/visual_red_build/meshy_ready_weapon_fk_follow_observed_web_truth.json",
   "manualPlacementPolicy": "locked literals; verifier reads rig profile and does not tune offsets",
   "observedWebTruth": {
     "schema": "pose-lab-ready-weapon-fk-observed-web-truth-v1",
     "generatedAt": "2026-07-02T18:52:17.589Z",
     "cacheToken": "pose-editor-131",
     "runtimeBuild": "meshy-fps-sword-upper-body-retarget",
     "actorKey": "meshyCharacter",
     "clipName": "OneHandReady -> meshyCharacter [FPS-VISUAL-IK R-120 L-90]",
     "visualClass": "sword-rest-space",
     "evidenceSource": "human-visible-red-build",
     "browserCaptureDeprecated": true,
     "capturePaths": [
       "/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-130645.png",
       "/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-130642.png",
       "/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-131830.png"
     ],
-    "visualRead": "T-pose weapon placement reads correct; Ready hands improved, but the sabre remains visually rest-space / not following final FK. Browser capture is retained only as human-report context."
+    "visualRead": "T-pose weapon placement reads correct; Ready hands improved, but the sabre remains visually rest-space / not following final FK. Browser capture is retained only as human-report context.",
+    "visualAssertions": {
+      "tPoseWeaponPlacementAccepted": true,
+      "readyHandsCorrected": true,
+      "readySwordNotFollowingFinalFk": true,
+      "browserCaptureRejectedAsAcceptance": true,
+      "expectedReadySwordFollowsFinalFk": true
+    }
   },
   "offlineTruth": {
     "visualClass": "sword-hidden",
     "transformClass": "sword-follows-fk",
     "visibilityClass": "weapon-hidden",
     "reasons": [
       "weapon-not-visible-in-runtime"
     ],
     "metrics": {
       "hiltToHandDistance": 0.11497,
       "bladeAxisChangeFromRestDeg": 97.29,
       "socketToHandQuaternionErrorDeg": 0
     },
     "visibility": {
       "visible": false,
       "visibilityClass": "weapon-hidden",
       "matchedPattern": "",
       "patterns": [
         "\\[FPS-REST-ARMS"
       ],
       "reasons": [
         "runtime-visibility-hidden"
       ]
     }
   },
   "parity": {
     "parityMatches": false,
     "visualVerdict": "red",
     "parityFailure": "offline-web-visual-class-diverged"
   },
   "result": "red",
   "acceptance": {
     "generatedReadyClipResolved": true,
     "readyClipSampled": true,
     "readyHandDisplacedFromRest": true,
     "noGeneratedWeaponTracks": true,
     "runtimeVisibilityModeled": true,
     "manualSaberPlacementPreserved": true
   },
   "metrics": {
     "readyHandDisplacement": 0.41757,
     "readyDuration": 1.208333,
     "targetKeyCount": 30,
     "sourceKeyCount": 31,
     "hiltToHandDistance": 0.11497,
     "bladeAxisChangeFromRestDeg": 97.29,
     "socketToHandQuaternionErrorDeg": 0
   },
   "samples": [
     {
       "label": "ready-start",
       "time": 0,
       "hilt": [
         -0.4737,
         1.28061,
         0.19928
       ],
       "hand": [
         -0.35956,
         1.27299,
         0.21078
       ],
       "tip": [
         -0.89017,
         0.73678,
         0.54826
       ],
       "bladeAxis": [
         -0.54174,
         -0.70742,
         0.45395
       ],
       "socketForward": [
         -0.13698,
         -0.95172,
         0.27469
       ],
       "socketQuaternion": [
         0.588801,
         0.126358,
diff --git a/generated/visual_red_build/meshy_ready_weapon_fk_follow_latest.json b/generated/visual_red_build/meshy_ready_weapon_fk_follow_latest.json
index 49d83f0..98222c4 100644
--- a/generated/visual_red_build/meshy_ready_weapon_fk_follow_latest.json
+++ b/generated/visual_red_build/meshy_ready_weapon_fk_follow_latest.json
@@ -1,83 +1,90 @@
 {
   "schema": "pose-lab-ready-weapon-fk-offline-web-parity-gate-v1",
-  "generatedAt": "2026-07-02T19:07:36.928Z",
+  "generatedAt": "2026-07-02T19:19:28.834Z",
   "currentFixCacheToken": "pose-editor-131",
   "cacheToken": "pose-editor-131",
   "runtimeBuild": "meshy-fps-sword-upper-body-retarget",
   "actorKey": "meshyCharacter",
   "clipName": "OneHandReady -> meshyCharacter [FPS-VISUAL-IK R-120 L-90]",
   "readyClipName": "OneHandReady -> meshyCharacter [FPS-VISUAL-IK R-120 L-90]",
   "proofMode": "offline-web-truth-parity",
   "browserCaptureDeprecated": true,
   "browserCapturePolicy": "Browser screenshots, debug bridge state, Android screencap, and visual-QA browser capture are manual inspection aids only and cannot close this red build.",
   "sharedTruthModule": "src/ready-weapon-truth.mjs",
   "observedWebTruthPath": "generated/visual_red_build/meshy_ready_weapon_fk_follow_observed_web_truth.json",
   "observedWebTruth": {
     "schema": "pose-lab-ready-weapon-fk-observed-web-truth-v1",
     "generatedAt": "2026-07-02T18:52:17.589Z",
     "cacheToken": "pose-editor-131",
     "runtimeBuild": "meshy-fps-sword-upper-body-retarget",
     "actorKey": "meshyCharacter",
     "clipName": "OneHandReady -> meshyCharacter [FPS-VISUAL-IK R-120 L-90]",
     "visualClass": "sword-rest-space",
     "evidenceSource": "human-visible-red-build",
     "browserCaptureDeprecated": true,
     "capturePaths": [
       "/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-130645.png",
       "/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-130642.png",
       "/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-131830.png"
     ],
-    "visualRead": "T-pose weapon placement reads correct; Ready hands improved, but the sabre remains visually rest-space / not following final FK. Browser capture is retained only as human-report context."
+    "visualRead": "T-pose weapon placement reads correct; Ready hands improved, but the sabre remains visually rest-space / not following final FK. Browser capture is retained only as human-report context.",
+    "visualAssertions": {
+      "tPoseWeaponPlacementAccepted": true,
+      "readyHandsCorrected": true,
+      "readySwordNotFollowingFinalFk": true,
+      "browserCaptureRejectedAsAcceptance": true,
+      "expectedReadySwordFollowsFinalFk": true
+    }
   },
   "offlineTruth": {
     "visualClass": "sword-hidden",
     "transformClass": "sword-follows-fk",
     "visibilityClass": "weapon-hidden",
     "reasons": [
       "weapon-not-visible-in-runtime"
     ],
     "metrics": {
       "hiltToHandDistance": 0.11497,
       "bladeAxisChangeFromRestDeg": 97.29,
       "socketToHandQuaternionErrorDeg": 0
     },
     "visibility": {
       "visible": false,
       "visibilityClass": "weapon-hidden",
       "matchedPattern": "",
       "patterns": [
         "\\[FPS-REST-ARMS"
       ],
       "reasons": [
         "runtime-visibility-hidden"
       ]
     }
   },
   "parity": {
     "parityMatches": false,
     "visualVerdict": "red",
     "parityFailure": "offline-web-visual-class-diverged"
   },
   "offlineVisualTruth": {
     "artifactPath": "generated/offline_visual_truth/meshy_ready_weapon_fk_follow/visual_truth.json",
     "sheetPath": "generated/offline_visual_truth/meshy_ready_weapon_fk_follow/visual_truth_sheet.svg",
     "result": "red",
     "metrics": {
       "readyHandDisplacement": 0.41757,
       "readyDuration": 1.208333,
       "targetKeyCount": 30,
       "sourceKeyCount": 31,
       "hiltToHandDistance": 0.11497,
       "bladeAxisChangeFromRestDeg": 97.29,
       "socketToHandQuaternionErrorDeg": 0
     },
     "acceptance": {
       "generatedReadyClipResolved": true,
       "readyClipSampled": true,
       "readyHandDisplacedFromRest": true,
       "noGeneratedWeaponTracks": true,
       "runtimeVisibilityModeled": true,
       "manualSaberPlacementPreserved": true
     }
   }
 }
diff --git a/generated/visual_red_build/meshy_ready_weapon_fk_follow_observed_web_truth.json b/generated/visual_red_build/meshy_ready_weapon_fk_follow_observed_web_truth.json
index 1a87394..8ed5594 100644
--- a/generated/visual_red_build/meshy_ready_weapon_fk_follow_observed_web_truth.json
+++ b/generated/visual_red_build/meshy_ready_weapon_fk_follow_observed_web_truth.json
@@ -1,17 +1,24 @@
 {
   "schema": "pose-lab-ready-weapon-fk-observed-web-truth-v1",
   "generatedAt": "2026-07-02T18:52:17.589Z",
   "cacheToken": "pose-editor-131",
   "runtimeBuild": "meshy-fps-sword-upper-body-retarget",
   "actorKey": "meshyCharacter",
   "clipName": "OneHandReady -> meshyCharacter [FPS-VISUAL-IK R-120 L-90]",
   "visualClass": "sword-rest-space",
   "evidenceSource": "human-visible-red-build",
   "browserCaptureDeprecated": true,
   "capturePaths": [
     "/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-130645.png",
     "/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-130642.png",
     "/storage/emulated/0/Pictures/Screenshots/Screenshot_20260702-131830.png"
   ],
-  "visualRead": "T-pose weapon placement reads correct; Ready hands improved, but the sabre remains visually rest-space / not following final FK. Browser capture is retained only as human-report context."
+  "visualRead": "T-pose weapon placement reads correct; Ready hands improved, but the sabre remains visually rest-space / not following final FK. Browser capture is retained only as human-report context.",
+  "visualAssertions": {
+    "tPoseWeaponPlacementAccepted": true,
+    "readyHandsCorrected": true,
+    "readySwordNotFollowingFinalFk": true,
+    "browserCaptureRejectedAsAcceptance": true,
+    "expectedReadySwordFollowsFinalFk": true
+  }
 }
diff --git a/tools/meshy_ready_weapon_offline_visual_truth.mjs b/tools/meshy_ready_weapon_offline_visual_truth.mjs
index 4f4d145..f5df40f 100644
--- a/tools/meshy_ready_weapon_offline_visual_truth.mjs
+++ b/tools/meshy_ready_weapon_offline_visual_truth.mjs
@@ -90,160 +90,164 @@ function capturePose(root) {
     if (!node.isObject3D) return;
     pose.push({ node, position: node.position.clone(), quaternion: node.quaternion.clone(), scale: node.scale.clone() });
   });
   return pose;
 }
 function restorePose(root, pose) {
   for (const entry of pose) {
     entry.node.position.copy(entry.position);
     entry.node.quaternion.copy(entry.quaternion);
     entry.node.scale.copy(entry.scale);
     entry.node.updateMatrix();
   }
   root.updateMatrixWorld(true);
 }
 function sampleClip(THREE, root, restPose, clip, time) {
   restorePose(root, restPose);
   const mixer = new THREE.AnimationMixer(root);
   const action = mixer.clipAction(clip);
   action.enabled = true;
   action.weight = 1;
   action.reset().play();
   mixer.setTime(Math.max(0, Math.min(time, clip.duration || 0)));
   root.updateMatrixWorld(true);
   return mixer;
 }
 function projectBounds(states) {
   const pts = [];
   for (const state of states) pts.push(state.hilt, state.hand, state.tip);
   const min = { x: Math.min(...pts.map((p) => p.x)), y: Math.min(...pts.map((p) => p.y)) };
   const max = { x: Math.max(...pts.map((p) => p.x)), y: Math.max(...pts.map((p) => p.y)) };
   const span = Math.max(max.x - min.x, max.y - min.y, 0.001);
   return { cx: (min.x + max.x) / 2, cy: (min.y + max.y) / 2, scale: 220 / span };
 }
 function svgPoint(p, panel, bounds) {
   return [panel.x + panel.w / 2 + (p.x - bounds.cx) * bounds.scale, panel.y + panel.h / 2 - (p.y - bounds.cy) * bounds.scale];
 }
 function writeSheet(frames, file, observedWebTruth, offlineTruth, verdict) {
   const W = 1200;
   const H = 455;
   const panelW = W / frames.length;
   const bounds = projectBounds(frames.map((f) => f.state));
   const title = `Offline/web parity: observed=${observedWebTruth.visualClass} offline=${offlineTruth.visualClass} visibility=${offlineTruth.visibilityClass} verdict=${verdict.visualVerdict}`;
   const parts = [`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">`, '<rect width="100%" height="100%" fill="#06090d"/>'];
   parts.push(`<text x="20" y="28" fill="#fff4c2" font-family="monospace" font-size="18">${title}</text>`);
   frames.forEach((frame, index) => {
     const panel = { x: index * panelW + 12, y: 50, w: panelW - 24, h: 330 };
     const h = svgPoint(frame.state.hilt, panel, bounds);
     const hand = svgPoint(frame.state.hand, panel, bounds);
     const tip = svgPoint(frame.state.tip, panel, bounds);
     const opacity = offlineTruth.visibility?.visible ? 1 : 0.35;
     parts.push(`<rect x="${panel.x}" y="${panel.y}" width="${panel.w}" height="${panel.h}" fill="#0b1118" stroke="#344054"/>`);
     parts.push(`<text x="${panel.x + 8}" y="${panel.y + 22}" fill="#e5e7eb" font-family="monospace" font-size="13">${frame.label} t=${round(frame.time, 3)}</text>`);
     parts.push(`<line x1="${h[0]}" y1="${h[1]}" x2="${tip[0]}" y2="${tip[1]}" stroke="#facc15" stroke-width="5" opacity="${opacity}"/>`);
     parts.push(`<line x1="${h[0]}" y1="${h[1]}" x2="${hand[0]}" y2="${hand[1]}" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 4"/>`);
     parts.push(`<circle cx="${hand[0]}" cy="${hand[1]}" r="7" fill="#22c55e"><title>RightHand</title></circle>`);
     parts.push(`<circle cx="${h[0]}" cy="${h[1]}" r="6" fill="#ef4444" opacity="${opacity}"><title>WeaponGrip/hilt</title></circle>`);
     parts.push(`<circle cx="${tip[0]}" cy="${tip[1]}" r="5" fill="#facc15" opacity="${opacity}"><title>Blade tip</title></circle>`);
     parts.push(`<text x="${panel.x + 8}" y="${panel.y + panel.h - 16}" fill="#cbd5e1" font-family="monospace" font-size="12">hilt-hand=${round(frame.state.hiltToHandDistance, 4)}</text>`);
   });
   parts.push('<text x="20" y="410" fill="#94a3b8" font-family="monospace" font-size="13">Green=RightHand, red=WeaponGrip/hilt, yellow=blade tip. Dim weapon means runtime visibility hides this clip.</text>');
   parts.push('<text x="20" y="432" fill="#fca5a5" font-family="monospace" font-size="13">Red is expected until observed web truth and offline runtime truth both agree on sword-follows-fk.</text>');
   parts.push('</svg>');
   fs.writeFileSync(file, parts.join('\n') + '\n');
 }
 function readRuntimeField(name) {
   const runtime = fs.readFileSync(path.join(projectRoot, 'src', 'pose-lab.js'), 'utf8');
   const match = runtime.match(new RegExp(`const\\s+${name}\\s*=\\s*['\"]([^'\"]+)['\"]`));
   return match?.[1] || '';
 }
 function validateObservedWebTruth(observed, { cacheToken, runtimeBuild, clipName }) {
   const errors = [];
   if (observed.schema !== 'pose-lab-ready-weapon-fk-observed-web-truth-v1') errors.push(`observed web truth schema ${observed.schema || 'missing'} is invalid`);
   if (observed.cacheToken !== cacheToken) errors.push(`observed cacheToken ${observed.cacheToken || 'missing'} != ${cacheToken}`);
   if (observed.runtimeBuild !== runtimeBuild) errors.push(`observed runtimeBuild ${observed.runtimeBuild || 'missing'} != ${runtimeBuild}`);
   if (observed.actorKey !== 'meshyCharacter') errors.push(`observed actor ${observed.actorKey || 'missing'} != meshyCharacter`);
   if (observed.clipName !== clipName) errors.push(`observed clip ${observed.clipName || 'missing'} != ${clipName}`);
   if (!['sword-rest-space', 'sword-follows-fk', 'sword-hidden'].includes(observed.visualClass)) errors.push(`observed visualClass ${observed.visualClass || 'missing'} is invalid`);
   if (observed.browserCaptureDeprecated !== true) errors.push('observed web truth must mark browser capture deprecated');
   if (!String(observed.visualRead || '').trim()) errors.push('observed visualRead is required');
   if (!Array.isArray(observed.capturePaths) || observed.capturePaths.length < 1) errors.push('observed capturePaths must list human evidence paths');
+  const assertions = observed.visualAssertions || {};
+  for (const key of ['tPoseWeaponPlacementAccepted', 'readyHandsCorrected', 'readySwordNotFollowingFinalFk', 'browserCaptureRejectedAsAcceptance', 'expectedReadySwordFollowsFinalFk']) {
+    if (assertions[key] !== true) errors.push(`observed visual assertion must be true: ${key}`);
+  }
   if (errors.length) throw new Error(errors.join('\n'));
   return observed;
 }
 async function main() {
   const args = parseArgs(process.argv);
   ensureBrowserShim();
   const threeDir = ensureThreeSandbox();
   const THREE = await import(pathToFileURL(path.join(threeDir, 'build', 'three.module.js')));
   const { GLTFLoader } = await import(pathToFileURL(path.join(threeDir, 'examples', 'jsm', 'loaders', 'GLTFLoader.js')));
   const { clone: cloneSkinnedObject } = await import(pathToFileURL(path.join(threeDir, 'examples', 'jsm', 'utils', 'SkeletonUtils.js')));
   const { buildMeshyFpsVisualIkReadyClip } = await import(pathToFileURL(path.join(projectRoot, 'src', 'meshy-ready-runtime.mjs')));
   const { RIG_PROFILES } = await import(pathToFileURL(path.join(projectRoot, 'src', 'rig-profiles.js')));
   const profile = RIG_PROFILES.meshyCharacter;
   const runtimeBuild = readRuntimeField('LAB_BUILD');
   const cacheToken = readRuntimeField('LAB_CACHE_TOKEN');
   const fps = await loadGlb(GLTFLoader, path.join(projectRoot, 'assets', 'models', 'FPSPlayer.glb'));
   const meshy = await loadGlb(GLTFLoader, path.join(projectRoot, 'assets', 'models', 'meshy_character_sheet', 'animated', 'Meshy_AI_Meshy_Character_Sheet_biped_Animation_Walking_withSkin.glb'));
   const sabre = await loadGlb(GLTFLoader, path.join(projectRoot, profile.weaponAttachment.url));
   const sourceRoot = fps.scene;
   const targetRoot = meshy.scene;
   sourceRoot.updateMatrixWorld(true);
   targetRoot.updateMatrixWorld(true);
   const built = buildMeshyFpsVisualIkReadyClip(THREE, cloneSkinnedObject, sourceRoot, targetRoot, fps.animations, {
     clipName: 'OneHandReady -> meshyCharacter [FPS-VISUAL-IK R-120 L-90]',
     sourceClipName: 'OneHandReady',
     sourceRestClip: '0T-Pose',
     timeSourceBone: 'Hand.R',
     dropInitialRestKey: true,
     weaponAttachment: profile.weaponAttachment,
   });
   if (!built.clip) throw new Error(`failed to build Ready clip: ${built.reason}`);
   const observedWebTruth = validateObservedWebTruth(readJson(args.observed), { cacheToken, runtimeBuild, clipName: built.clip.name });
   const restPose = capturePose(targetRoot);
   const rightHand = requireNode(targetRoot, profile.weaponProxy.handBone || 'RightHand');
   const leftHand = profile.weaponProxy.leftHandBone ? find(targetRoot, profile.weaponProxy.leftHandBone) : null;
   const socket = new THREE.Object3D();
   socket.name = profile.weaponProxy.socketBone || profile.weaponAttachment.socketBone || 'WeaponGrip';
   targetRoot.add(socket);
   const weaponRoot = sabre.scene.clone(true);
   weaponRoot.name = profile.weaponAttachment.name || 'Meshy French Revolution Sabre';
   socket.add(weaponRoot);
   const tip = new THREE.Group();
   tip.name = profile.weaponAttachment.tipMarker || 'WeaponGrip_end';
   socket.add(tip);
   const updateTruth = () => {
     updateSyntheticWeaponSocketTransform(THREE, { model: targetRoot, root: socket, rightHand, leftHand, config: profile.weaponProxy, activeClipHasSocketRotation: false });
     applyWeaponAttachmentTruthTransform(THREE, { weaponRoot, tip, config: profile.weaponAttachment, fallbackTipOffset: profile.weaponProxy.tipOffset || [0, 0, 0.85] });
     targetRoot.updateMatrixWorld(true);
   };
   restorePose(targetRoot, restPose);
   updateTruth();
   const restState = measureReadyWeaponTruth(THREE, { socket, rightHand, weaponRoot, tip, attachmentConfig: profile.weaponAttachment });
   const sampleTimes = [0, built.clip.duration * 0.5, built.clip.duration].map((time) => Math.max(0, Math.min(built.clip.duration, time)));
   const frames = [];
   for (const [index, time] of sampleTimes.entries()) {
     sampleClip(THREE, targetRoot, restPose, built.clip, time);
     updateTruth();
     const state = measureReadyWeaponTruth(THREE, { socket, rightHand, weaponRoot, tip, attachmentConfig: profile.weaponAttachment });
     frames.push({ label: index === 0 ? 'ready-start' : (index === 1 ? 'ready-mid' : 'ready-end'), time, state });
   }
   restorePose(targetRoot, restPose);
   const restHand = rightHand.getWorldPosition(new THREE.Vector3());
   sampleClip(THREE, targetRoot, restPose, built.clip, 0);
   const readyHand = rightHand.getWorldPosition(new THREE.Vector3());
   const readyHandDisplacement = restHand.distanceTo(readyHand);
   const clipHasWeaponTracks = built.clip.tracks.some((track) => /WeaponGrip|Weapon\.R|WeaponR/.test(track.name));
   const visibility = classifyWeaponVisibility({ clipName: built.clip.name, clipUserData: built.clip.userData, config: profile.weaponProxy, weaponDebug: args.weaponDebug });
   const offlineTruth = classifyReadyWeaponTruth(THREE, { readyState: frames[1].state, restState, visibility });
   const parity = buildReadyWeaponParityVerdict({ observedWebClass: observedWebTruth.visualClass, offlineClass: offlineTruth.visualClass });
   const result = parity.visualVerdict;
   fs.mkdirSync(args.out, { recursive: true });
   const jsonPath = path.join(args.out, 'visual_truth.json');
   const sheetPath = path.join(args.out, 'visual_truth_sheet.svg');
   writeSheet(frames, sheetPath, observedWebTruth, offlineTruth, parity);
   const artifact = {
     schema: 'pose-lab-offline-web-truth-parity-ready-weapon-fk-v1',
     generatedAt: new Date().toISOString(),
     proofMode: 'offline-web-truth-parity',
     browserCaptureDeprecated: true,
     sourceActor: 'FPS Arms',
diff --git a/tools/pose_lab_workflow_lib.mjs b/tools/pose_lab_workflow_lib.mjs
index 390fbc5..7a523e0 100644
--- a/tools/pose_lab_workflow_lib.mjs
+++ b/tools/pose_lab_workflow_lib.mjs
@@ -31,189 +31,249 @@ export function currentCommit() {
     return execFileSync('git', ['-c', `safe.directory=${projectRoot}`, 'rev-parse', '--short', 'HEAD'], { cwd: projectRoot, encoding: 'utf8' }).trim();
   } catch (_err) {
     return '';
   }
 }
 
 export function gitStatusLines() {
   try {
     return execFileSync('git', ['-c', `safe.directory=${projectRoot}`, 'status', '--short'], { cwd: projectRoot, encoding: 'utf8' })
       .split(/\r?\n/)
       .map((line) => line.trimEnd())
       .filter(Boolean);
   } catch (_err) {
     return [];
   }
 }
 
 export function protectedDirtyFiles(lines = gitStatusLines()) {
   const protectedPrefixes = [
     'PROJECT_ORIENTATION.md',
     'docs/ANIMATION_WORKFLOW_TOOLING.md',
     'pose-critique.html',
     'pose-lab.html',
     'src/pose-lab.js',
     'src/rig-profiles.js',
     'generated/workflow_state/',
     'tools/promote_pose_candidate.mjs',
     'tools/pose_lab_workflow_status.mjs',
     'tools/pose_lab_workflow_lib.mjs',
   ];
   return lines.filter((line) => {
     const file = line.replace(/^.. /, '');
     return protectedPrefixes.some((prefix) => file === prefix || file.startsWith(prefix));
   });
 }
 
 export function currentMeshySelectionSurfaces() {
   const profiles = readText('src/rig-profiles.js');
   const meshyStart = profiles.indexOf('meshyCharacter:');
   const meshyEnd = profiles.indexOf('\n  meshyStatic:', meshyStart);
   const meshy = profiles.slice(meshyStart, meshyEnd > meshyStart ? meshyEnd : undefined);
   const startupClip = meshy.match(/startupClip:\s*\{\s*name:\s*'([^']+)'/)?.[1] || '';
   const lineFor = (name) => meshy.split(/\r?\n/).find((line) => line.includes(`${name}: [`)) || '';
   const stringValues = (line) => Array.from(line.matchAll(/'((?:\\'|[^'])*)'|"((?:\\"|[^"])*)"/g))
     .map((entry) => (entry[1] ?? entry[2] ?? '').replace(/\\\\/g, '\\').replace(/\\'/g, "'").replace(/\\"/g, '"'));
   return {
     startupClip,
     swordReadyAliases: stringValues(lineFor('SwordReady')),
     restProbeAliases: stringValues(lineFor('RestProbe')),
     weaponVisibleClipPatterns: stringValues(lineFor('visibleClipPatterns')),
   };
 }
 
 export function compareSelectionSurfaces(baseline, current = currentMeshySelectionSurfaces()) {
   const expected = baseline.selectionSurfaces || {};
   const mismatches = [];
   for (const key of ['startupClip', 'swordReadyAliases', 'restProbeAliases', 'weaponVisibleClipPatterns']) {
     const a = JSON.stringify(expected[key] ?? (Array.isArray(current[key]) ? [] : ''));
     const b = JSON.stringify(current[key] ?? (Array.isArray(expected[key]) ? [] : ''));
     if (a !== b) mismatches.push({ key, expected: expected[key], actual: current[key] });
   }
   return mismatches;
 }
 
 export function evidenceCacheToken(evidence) {
   return evidence.cacheToken || evidence.currentFixCacheToken || '';
 }
 
 export function evidenceClipName(evidence) {
   return evidence.clipName || evidence.readyClipName || '';
 }
 
 export function isParityEvidence(evidence) {
   return evidence?.schema === 'pose-lab-ready-weapon-fk-offline-web-parity-gate-v1';
 }
 
 export function isLegacyVisualEvidence(evidence) {
   return evidence?.schema === 'pose-lab-visual-evidence-v1';
 }
 
+
+export function resolveEvidencePath(file) {
+  if (!file) return '';
+  return path.isAbsolute(file) ? file : path.join(projectRoot, file);
+}
+
+function jsonEqual(a, b) {
+  return JSON.stringify(a) === JSON.stringify(b);
+}
+
+function readEvidenceJsonForValidation(file, label, errors) {
+  const resolved = resolveEvidencePath(file);
+  if (!file) {
+    errors.push(`parity evidence missing ${label}`);
+    return null;
+  }
+  if (!fs.existsSync(resolved)) {
+    errors.push(`parity evidence ${label} does not exist: ${file}`);
+    return null;
+  }
+  try {
+    return readJson(resolved);
+  } catch (error) {
+    errors.push(`parity evidence ${label} is invalid JSON: ${error.message}`);
+    return null;
+  }
+}
+
+export function validateParityEvidenceReadback(evidence) {
+  const errors = [];
+  if (!isParityEvidence(evidence)) return errors;
+  const observed = readEvidenceJsonForValidation(evidence.observedWebTruthPath, 'observedWebTruthPath', errors);
+  if (observed && !jsonEqual(observed, evidence.observedWebTruth)) {
+    errors.push('parity evidence embedded observedWebTruth does not match observedWebTruthPath file');
+  }
+  const offlineArtifactPath = evidence.offlineVisualTruth?.artifactPath || '';
+  const offline = readEvidenceJsonForValidation(offlineArtifactPath, 'offlineVisualTruth.artifactPath', errors);
+  if (offline) {
+    for (const key of ['cacheToken', 'runtimeBuild', 'actorKey', 'clipName', 'observedWebTruthPath', 'result']) {
+      if (!jsonEqual(offline[key], key === 'result' ? evidence.offlineVisualTruth?.result : evidence[key])) {
+        errors.push(`parity evidence offline artifact ${key} does not match wrapper`);
+      }
+    }
+    for (const key of ['observedWebTruth', 'offlineTruth', 'parity']) {
+      if (!jsonEqual(offline[key], evidence[key])) errors.push(`parity evidence offline artifact ${key} does not match wrapper`);
+    }
+    if (!jsonEqual(offline.sheet, evidence.offlineVisualTruth?.sheetPath)) {
+      errors.push('parity evidence offline artifact sheet does not match wrapper sheetPath');
+    }
+  }
+  const sheetPath = evidence.offlineVisualTruth?.sheetPath || '';
+  const resolvedSheet = resolveEvidencePath(sheetPath);
+  if (!sheetPath) {
+    errors.push('parity evidence missing offlineVisualTruth.sheetPath');
+  } else if (!fs.existsSync(resolvedSheet)) {
+    errors.push(`parity evidence sheetPath does not exist: ${sheetPath}`);
+  } else if (fs.statSync(resolvedSheet).size <= 0) {
+    errors.push(`parity evidence sheetPath is empty: ${sheetPath}`);
+  }
+  return errors;
+}
+
 export function latestEvidenceStatus(file = latestEvidencePath) {
   if (!fs.existsSync(file)) return { exists: false, path: file, stale: true, blocked: true, errors: ['missing visual evidence'] };
   let evidence = null;
   try {
     evidence = readJson(file);
   } catch (error) {
     return { exists: true, path: file, stale: true, blocked: true, errors: [`invalid evidence JSON: ${error.message}`] };
   }
   const cacheToken = currentCacheToken();
   const runtimeBuild = currentRuntimeBuild();
   const errors = [];
   const token = evidenceCacheToken(evidence);
   if (token !== cacheToken) errors.push(`evidence cacheToken ${token || 'missing'} != current ${cacheToken || 'missing'}`);
   if (evidence.runtimeBuild !== runtimeBuild) errors.push(`evidence runtimeBuild ${evidence.runtimeBuild || 'missing'} != current ${runtimeBuild || 'missing'}`);
   if (isParityEvidence(evidence)) {
     if (evidence.browserCaptureDeprecated !== true) errors.push('parity evidence must deprecate browser capture');
     if (evidence.parity?.visualVerdict !== 'fixed') errors.push(`parity evidence is ${evidence.parity?.visualVerdict || 'missing'}, not fixed`);
-    if (!evidence.offlineVisualTruth?.artifactPath) errors.push('parity evidence missing offline artifact path');
-    if (!evidence.observedWebTruthPath) errors.push('parity evidence missing observed web truth path');
+    errors.push(...validateParityEvidenceReadback(evidence));
   } else if (isLegacyVisualEvidence(evidence)) {
     if (evidence.liveVisualQa?.status === 'blocked' || evidence.captureKind === 'visual-qa-blocked') errors.push('evidence is blocked');
     if (evidence.motionEvidencePending === true) errors.push('motion evidence is pending');
   } else {
     errors.push(`visual evidence schema ${evidence.schema || 'missing'} is unsupported`);
   }
   return {
     exists: true,
     path: file,
     evidence,
     stale: token !== cacheToken || evidence.runtimeBuild !== runtimeBuild,
-    blocked: isParityEvidence(evidence) ? evidence.parity?.visualVerdict !== 'fixed' : evidence.liveVisualQa?.status === 'blocked' || evidence.captureKind === 'visual-qa-blocked',
+    blocked: isParityEvidence(evidence) ? evidence.parity?.visualVerdict !== 'fixed' || errors.length > 0 : evidence.liveVisualQa?.status === 'blocked' || evidence.captureKind === 'visual-qa-blocked',
     errors,
   };
 }
 
 export function validateCandidatePromotion({ baseline, candidate, evidence, metrics, cacheToken = currentCacheToken(), runtimeBuild = currentRuntimeBuild() }) {
   const errors = [];
   const warnings = [];
   if (!candidate || typeof candidate !== 'object') errors.push('candidate JSON is required');
   if (!evidence || typeof evidence !== 'object') errors.push('visual evidence JSON is required');
   if (!metrics || typeof metrics !== 'object') errors.push('metric evidence JSON is required');
   if (errors.length) return { ok: false, errors, warnings };
 
   const actorKey = candidate.actorKey || candidate.targetActorKey || baseline.actorKey;
   const clipName = candidate.clipName || candidate.name || candidate.targetClip || '';
   if (actorKey !== baseline.actorKey) errors.push(`candidate actor ${actorKey || 'missing'} does not match protected actor ${baseline.actorKey}`);
   if (!clipName) errors.push('candidate clipName/name/targetClip is required');
   if (candidate.status !== 'candidate-only') warnings.push(`candidate status is ${candidate.status || 'missing'}, expected candidate-only before promotion`);
   if (candidate.promotable === true) warnings.push('candidate was already marked promotable before gate validation');
 
   const token = evidenceCacheToken(evidence);
   const evidenceClip = evidenceClipName(evidence);
   if (token !== cacheToken) errors.push(`visual evidence cacheToken ${token || 'missing'} does not match ${cacheToken || 'missing'}`);
   if (evidence.runtimeBuild !== runtimeBuild) errors.push(`visual evidence runtimeBuild ${evidence.runtimeBuild || 'missing'} does not match ${runtimeBuild || 'missing'}`);
   if (evidence.actorKey !== baseline.actorKey) errors.push(`visual evidence actor ${evidence.actorKey || 'missing'} does not match ${baseline.actorKey}`);
   if (!String(evidenceClip || '').includes(clipName) && !String(clipName).includes(String(evidenceClip || '___missing___'))) {
     errors.push(`visual evidence clip ${evidenceClip || 'missing'} does not match candidate ${clipName}`);
   }
 
   if (isParityEvidence(evidence)) {
     if (evidence.browserCaptureDeprecated !== true) errors.push('parity evidence must deprecate browser capture');
     if (evidence.parity?.visualVerdict !== 'fixed') errors.push(`parity evidence visualVerdict ${evidence.parity?.visualVerdict || 'missing'} is not fixed`);
     if (evidence.parity?.parityMatches !== true) errors.push('parity evidence must have parityMatches=true');
     if (evidence.observedWebTruth?.visualClass !== 'sword-follows-fk') errors.push(`observed web truth ${evidence.observedWebTruth?.visualClass || 'missing'} is not sword-follows-fk`);
     if (evidence.offlineTruth?.visualClass !== 'sword-follows-fk') errors.push(`offline truth ${evidence.offlineTruth?.visualClass || 'missing'} is not sword-follows-fk`);
     if (evidence.offlineTruth?.visibilityClass !== 'weapon-visible') errors.push(`offline weapon visibility ${evidence.offlineTruth?.visibilityClass || 'missing'} is not weapon-visible`);
-    if (!evidence.offlineVisualTruth?.artifactPath) errors.push('parity evidence missing offline artifact path');
-    if (!evidence.offlineVisualTruth?.sheetPath) errors.push('parity evidence missing offline sheet path');
+    errors.push(...validateParityEvidenceReadback(evidence));
   } else if (isLegacyVisualEvidence(evidence)) {
     if (evidence.liveVisualQa?.status === 'blocked' || evidence.captureKind === 'visual-qa-blocked') errors.push('visual evidence is blocked');
     if (evidence.motionEvidencePending === true) errors.push('visual evidence still has motionEvidencePending=true');
     if (!evidence.visualRead || String(evidence.visualRead).length < 20) errors.push('visual evidence needs a concrete visualRead');
     if (!evidence.capturePath) {
       errors.push('visual evidence capturePath is required');
     } else {
       const capturePath = path.isAbsolute(evidence.capturePath) ? evidence.capturePath : path.join(projectRoot, evidence.capturePath);
       if (!fs.existsSync(capturePath)) errors.push(`visual evidence capturePath does not exist: ${evidence.capturePath}`);
     }
   } else {
     errors.push(`visual evidence schema ${evidence.schema || 'missing'} is unsupported`);
   }
 
   if (metrics.schema !== 'pose-lab-promotion-metrics-v1') errors.push(`metric evidence schema ${metrics.schema || 'missing'} is not pose-lab-promotion-metrics-v1`);
   if (metrics.actorKey !== baseline.actorKey) errors.push(`metric actor ${metrics.actorKey || 'missing'} does not match ${baseline.actorKey}`);
   if (!String(metrics.clipName || '').includes(clipName) && !String(clipName).includes(String(metrics.clipName || '___missing___'))) {
     errors.push(`metric clip ${metrics.clipName || 'missing'} does not match candidate ${clipName}`);
   }
   const assertions = metrics.assertions || {};
   for (const key of [
     'beatsOrPreservesBaseline',
     'noTposeLeak',
     'armLengthPreserved',
     'handPositionSane',
     'rollDoesNotMoveJoints',
   ]) {
     if (assertions[key] !== true) errors.push(`metric assertion must be true: ${key}`);
   }
   if (candidate.weaponIncluded || metrics.weaponIncluded || isParityEvidence(evidence)) {
     for (const key of ['saberGripAtHandCenter', 'basketHiltFacesAwayFromBody', 'bladeLongAxisSane']) {
       if (assertions[key] !== true) errors.push(`weapon metric assertion must be true: ${key}`);
     }
   }
 
   return { ok: errors.length === 0, errors, warnings };
 }
 
 export function relative(file) {
   return path.relative(projectRoot, file);
 }
diff --git a/tools/test_offline_web_parity_promotion_contract.mjs b/tools/test_offline_web_parity_promotion_contract.mjs
index 17406f3..9230c10 100644
--- a/tools/test_offline_web_parity_promotion_contract.mjs
+++ b/tools/test_offline_web_parity_promotion_contract.mjs
@@ -1,87 +1,165 @@
 import fs from 'node:fs';
 import os from 'node:os';
 import path from 'node:path';
 import { spawnSync } from 'node:child_process';
 import {
   baselinePath,
   currentCacheToken,
   currentRuntimeBuild,
   latestEvidenceStatus,
   projectRoot,
   readJson,
   validateCandidatePromotion,
 } from './pose_lab_workflow_lib.mjs';
 
 const failures = [];
 function assert(condition, message) { if (!condition) failures.push(message); }
+function writeJson(file, data) {
+  fs.mkdirSync(path.dirname(file), { recursive: true });
+  fs.writeFileSync(file, JSON.stringify(data, null, 2) + '\n');
+}
+function clone(value) { return JSON.parse(JSON.stringify(value)); }
+function validate(evidence, candidate, metrics, baseline) {
+  return validateCandidatePromotion({ baseline, candidate, evidence, metrics });
+}
 
 const baseline = readJson(baselinePath);
 const latest = latestEvidenceStatus();
 assert(latest.path.endsWith('meshy_ready_weapon_fk_follow_latest.json'), 'latest evidence should point at Meshy Ready parity gate');
 assert(latest.errors.some((entry) => entry.includes('parity evidence is red')), 'current red parity evidence should block promotion status');
 
 const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'pose-lab-parity-promotion-'));
 const candidate = {
   status: 'candidate-only',
   promotable: false,
   actorKey: 'meshyCharacter',
   clipName: 'OneHandReady -> meshyCharacter [READY-GATED-MOCK]',
   weaponIncluded: true,
 };
 const metrics = {
   schema: 'pose-lab-promotion-metrics-v1',
   actorKey: 'meshyCharacter',
   clipName: candidate.clipName,
   weaponIncluded: true,
   assertions: {
     beatsOrPreservesBaseline: true,
     noTposeLeak: true,
     armLengthPreserved: true,
     handPositionSane: true,
     rollDoesNotMoveJoints: true,
     saberGripAtHandCenter: true,
     basketHiltFacesAwayFromBody: true,
     bladeLongAxisSane: true,
   },
 };
+const observedPath = path.join(tmp, 'observed.json');
+const artifactPath = path.join(tmp, 'visual_truth.json');
+const sheetPath = path.join(tmp, 'visual_truth_sheet.svg');
+const observedWebTruth = {
+  schema: 'pose-lab-ready-weapon-fk-observed-web-truth-v1',
+  cacheToken: currentCacheToken(),
+  runtimeBuild: currentRuntimeBuild(),
+  actorKey: 'meshyCharacter',
+  clipName: candidate.clipName,
+  visualClass: 'sword-follows-fk',
+  evidenceSource: 'mock-human-approved-fixed-parity',
+  browserCaptureDeprecated: true,
+  capturePaths: [path.join(tmp, 'mock-fixed-capture.png')],
+  visualRead: 'Mock fixed visual truth for promotion validation: Ready sword visibly follows final FK.',
+  visualAssertions: {
+    tPoseWeaponPlacementAccepted: true,
+    readyHandsCorrected: true,
+    readySwordNotFollowingFinalFk: false,
+    browserCaptureRejectedAsAcceptance: true,
+    expectedReadySwordFollowsFinalFk: true,
+  },
+};
+fs.writeFileSync(observedWebTruth.capturePaths[0], 'mock fixed capture\n');
+writeJson(observedPath, observedWebTruth);
+fs.writeFileSync(sheetPath, '<svg xmlns="http://www.w3.org/2000/svg"><text>fixed parity mock</text></svg>\n');
 const fixedParityEvidence = {
   schema: 'pose-lab-ready-weapon-fk-offline-web-parity-gate-v1',
   cacheToken: currentCacheToken(),
   currentFixCacheToken: currentCacheToken(),
   runtimeBuild: currentRuntimeBuild(),
   actorKey: 'meshyCharacter',
   clipName: candidate.clipName,
   readyClipName: candidate.clipName,
   browserCaptureDeprecated: true,
-  observedWebTruthPath: 'generated/visual_red_build/mock_observed_web_truth.json',
-  observedWebTruth: { visualClass: 'sword-follows-fk' },
+  observedWebTruthPath: observedPath,
+  observedWebTruth,
   offlineTruth: { visualClass: 'sword-follows-fk', transformClass: 'sword-follows-fk', visibilityClass: 'weapon-visible' },
   parity: { parityMatches: true, visualVerdict: 'fixed', parityFailure: '' },
-  offlineVisualTruth: { artifactPath: 'generated/offline_visual_truth/mock/visual_truth.json', sheetPath: 'generated/offline_visual_truth/mock/visual_truth_sheet.svg', result: 'fixed' },
+  offlineVisualTruth: { artifactPath, sheetPath, result: 'fixed' },
+};
+const offlineArtifact = {
+  schema: 'pose-lab-offline-web-truth-parity-ready-weapon-fk-v1',
+  cacheToken: fixedParityEvidence.cacheToken,
+  runtimeBuild: fixedParityEvidence.runtimeBuild,
+  actorKey: fixedParityEvidence.actorKey,
+  clipName: fixedParityEvidence.clipName,
+  observedWebTruthPath: fixedParityEvidence.observedWebTruthPath,
+  observedWebTruth: fixedParityEvidence.observedWebTruth,
+  offlineTruth: fixedParityEvidence.offlineTruth,
+  parity: fixedParityEvidence.parity,
+  result: fixedParityEvidence.offlineVisualTruth.result,
+  sheet: fixedParityEvidence.offlineVisualTruth.sheetPath,
 };
-const redParityEvidence = JSON.parse(JSON.stringify(fixedParityEvidence));
+writeJson(artifactPath, offlineArtifact);
+
+const fixedValidation = validate(fixedParityEvidence, candidate, metrics, baseline);
+assert(fixedValidation.ok === true, `fixed parity evidence should pass validation: ${fixedValidation.errors.join('; ')}`);
+
+const redParityEvidence = clone(fixedParityEvidence);
 redParityEvidence.parity = { parityMatches: false, visualVerdict: 'red', parityFailure: 'offline-web-visual-class-diverged' };
 redParityEvidence.offlineTruth.visibilityClass = 'weapon-hidden';
 redParityEvidence.offlineTruth.visualClass = 'sword-hidden';
-
-const fixedValidation = validateCandidatePromotion({ baseline, candidate, evidence: fixedParityEvidence, metrics });
-assert(fixedValidation.ok === true, `fixed parity evidence should pass validation: ${fixedValidation.errors.join('; ')}`);
-const redValidation = validateCandidatePromotion({ baseline, candidate, evidence: redParityEvidence, metrics });
+const redValidation = validate(redParityEvidence, candidate, metrics, baseline);
 assert(redValidation.ok === false && redValidation.errors.some((entry) => entry.includes('visualVerdict red')), 'red parity evidence must fail validation');
 
+const missingObserved = clone(fixedParityEvidence);
+missingObserved.observedWebTruthPath = path.join(tmp, 'missing-observed.json');
+assert(validate(missingObserved, candidate, metrics, baseline).errors.some((entry) => entry.includes('observedWebTruthPath does not exist')), 'missing observed truth file must fail');
+
+const mismatchedObserved = clone(fixedParityEvidence);
+const mismatchObservedPath = path.join(tmp, 'mismatch-observed.json');
+writeJson(mismatchObservedPath, { ...observedWebTruth, visualClass: 'sword-rest-space' });
+mismatchedObserved.observedWebTruthPath = mismatchObservedPath;
+assert(validate(mismatchedObserved, candidate, metrics, baseline).errors.some((entry) => entry.includes('embedded observedWebTruth does not match')), 'mismatched observed truth file must fail');
+
+const missingArtifact = clone(fixedParityEvidence);
+missingArtifact.offlineVisualTruth.artifactPath = path.join(tmp, 'missing-artifact.json');
+assert(validate(missingArtifact, candidate, metrics, baseline).errors.some((entry) => entry.includes('offlineVisualTruth.artifactPath does not exist')), 'missing offline artifact must fail');
+
+const mismatchedArtifact = clone(fixedParityEvidence);
+const mismatchArtifactPath = path.join(tmp, 'mismatch-artifact.json');
+writeJson(mismatchArtifactPath, { ...offlineArtifact, offlineTruth: { ...offlineArtifact.offlineTruth, visibilityClass: 'weapon-hidden' } });
+mismatchedArtifact.offlineVisualTruth.artifactPath = mismatchArtifactPath;
+assert(validate(mismatchedArtifact, candidate, metrics, baseline).errors.some((entry) => entry.includes('offline artifact offlineTruth does not match')), 'mismatched offline artifact must fail');
+
+const missingSheet = clone(fixedParityEvidence);
+missingSheet.offlineVisualTruth.sheetPath = path.join(tmp, 'missing-sheet.svg');
+assert(validate(missingSheet, candidate, metrics, baseline).errors.some((entry) => entry.includes('sheetPath does not exist')), 'missing sheet must fail');
+
+const emptySheet = clone(fixedParityEvidence);
+const emptySheetPath = path.join(tmp, 'empty-sheet.svg');
+fs.writeFileSync(emptySheetPath, '');
+emptySheet.offlineVisualTruth.sheetPath = emptySheetPath;
+assert(validate(emptySheet, candidate, metrics, baseline).errors.some((entry) => entry.includes('sheetPath is empty')), 'empty sheet must fail');
+
 const candidateFile = path.join(tmp, 'candidate.json');
 const evidenceFile = path.join(tmp, 'evidence.json');
 const metricsFile = path.join(tmp, 'metrics.json');
-fs.writeFileSync(candidateFile, JSON.stringify(candidate, null, 2));
-fs.writeFileSync(evidenceFile, JSON.stringify(fixedParityEvidence, null, 2));
-fs.writeFileSync(metricsFile, JSON.stringify(metrics, null, 2));
+writeJson(candidateFile, candidate);
+writeJson(evidenceFile, fixedParityEvidence);
+writeJson(metricsFile, metrics);
 const gate = spawnSync('node', ['tools/promote_pose_candidate.mjs', '--candidate', candidateFile, '--evidence', evidenceFile, '--metrics', metricsFile], {
   cwd: projectRoot,
   encoding: 'utf8',
 });
 assert(gate.status === 0, `fixed parity evidence should pass promote dry-run: ${gate.stderr || gate.stdout}`);
 const gateReport = JSON.parse(gate.stdout);
 assert(gateReport.ok === true && gateReport.apply === false, 'fixed parity dry-run should validate without applying');
 
 if (failures.length) throw new Error(failures.join('\n'));
-console.log(JSON.stringify({ checked: ['latest-parity-status-red', 'fixed-parity-promotion-accepted', 'red-parity-promotion-rejected'] }, null, 2));
+console.log(JSON.stringify({ checked: ['latest-parity-status-red', 'fixed-parity-promotion-accepted', 'red-parity-promotion-rejected', 'linked-parity-artifacts-required'] }, null, 2));
diff --git a/tools/test_pose_lab_visual_red_build_contract.mjs b/tools/test_pose_lab_visual_red_build_contract.mjs
index a657fa1..ce3fe67 100644
--- a/tools/test_pose_lab_visual_red_build_contract.mjs
+++ b/tools/test_pose_lab_visual_red_build_contract.mjs
@@ -1,58 +1,61 @@
 import fs from 'node:fs';
 import path from 'node:path';
 
 const projectRoot = path.resolve(import.meta.dirname, '..');
 const evidencePath = path.join(projectRoot, 'generated', 'visual_red_build', 'meshy_ready_weapon_fk_follow_latest.json');
 const observedPath = path.join(projectRoot, 'generated', 'visual_red_build', 'meshy_ready_weapon_fk_follow_observed_web_truth.json');
 const runtimePath = path.join(projectRoot, 'src', 'pose-lab.js');
 const failures = [];
 function assert(condition, message) { if (!condition) failures.push(message); }
 function readRuntimeBuild() {
   const runtime = fs.readFileSync(runtimePath, 'utf8');
   const match = runtime.match(/const\s+LAB_BUILD\s*=\s*['"]([^'"]+)['"]/);
   return match?.[1] || null;
 }
 function readCacheToken() {
   const runtime = fs.readFileSync(runtimePath, 'utf8');
   const match = runtime.match(/const\s+LAB_CACHE_TOKEN\s*=\s*['"]([^'"]+)['"]/);
   return match?.[1] || null;
 }
 assert(fs.existsSync(observedPath), `missing observed web truth: ${path.relative(projectRoot, observedPath)}`);
 const observed = fs.existsSync(observedPath) ? JSON.parse(fs.readFileSync(observedPath, 'utf8')) : {};
 assert(observed.schema === 'pose-lab-ready-weapon-fk-observed-web-truth-v1', 'observed web truth schema mismatch');
 assert(observed.browserCaptureDeprecated === true, 'observed web truth must mark browser capture deprecated');
 assert(observed.visualClass === 'sword-rest-space', 'current human web truth should remain red');
 assert(observed.cacheToken === readCacheToken(), 'observed web truth cache token should match runtime');
 assert(observed.runtimeBuild === readRuntimeBuild(), 'observed web truth runtime build should match runtime');
 assert(Array.isArray(observed.capturePaths) && observed.capturePaths.length >= 1, 'observed web truth should preserve human evidence paths');
+for (const key of ['tPoseWeaponPlacementAccepted', 'readyHandsCorrected', 'readySwordNotFollowingFinalFk', 'browserCaptureRejectedAsAcceptance', 'expectedReadySwordFollowsFinalFk']) {
+  assert(observed.visualAssertions?.[key] === true, `observed web truth assertion should be true: ${key}`);
+}
 assert(!fs.readFileSync(path.join(projectRoot, 'tools', 'meshy_ready_weapon_offline_visual_truth.mjs'), 'utf8').includes("const observedWebTruth = {"), 'verifier must not hardcode observed web truth');
 
 assert(fs.existsSync(evidencePath), `missing offline/web parity gate: ${path.relative(projectRoot, evidencePath)}`);
 const evidence = fs.existsSync(evidencePath) ? JSON.parse(fs.readFileSync(evidencePath, 'utf8')) : {};
 assert(evidence.schema === 'pose-lab-ready-weapon-fk-offline-web-parity-gate-v1', 'red build gate should use offline/web parity schema');
 assert(evidence.browserCaptureDeprecated === true, 'browser/device capture must be deprecated as red-build proof');
 assert(String(evidence.browserCapturePolicy || '').includes('cannot close this red build'), 'browser capture policy should reject red-build closure');
 assert(evidence.currentFixCacheToken === readCacheToken(), 'evidence cache token should match runtime');
 assert(evidence.cacheToken === readCacheToken(), 'evidence promotion cache token should match runtime');
 assert(evidence.runtimeBuild === readRuntimeBuild(), 'evidence runtime build should match runtime');
 assert(evidence.sharedTruthModule === 'src/ready-weapon-truth.mjs', 'gate should require shared runtime/offline truth module');
 assert(evidence.observedWebTruthPath === path.relative(projectRoot, observedPath), 'gate should point to observed web truth artifact');
 assert(evidence.observedWebTruth?.visualClass === 'sword-rest-space', 'current human web truth should remain red');
 assert(evidence.offlineTruth?.visibilityClass === 'weapon-hidden', 'offline truth should model current Ready weapon visibility as hidden');
 assert(evidence.offlineTruth?.transformClass === 'sword-follows-fk', 'offline transform truth should remain separate from visibility');
 assert(evidence.parity?.visualVerdict === 'red', 'current parity gate should be red until visual truth changes');
 const offline = evidence.offlineVisualTruth || {};
 const artifactPath = path.join(projectRoot, offline.artifactPath || '');
 const sheetPath = path.join(projectRoot, offline.sheetPath || '');
 assert(fs.existsSync(artifactPath), `missing parity artifact ${offline.artifactPath}`);
 assert(fs.existsSync(sheetPath), `missing parity sheet ${offline.sheetPath}`);
 assert(fs.existsSync(sheetPath) && fs.statSync(sheetPath).size > 1000, 'parity sheet should be non-empty');
 const artifact = fs.existsSync(artifactPath) ? JSON.parse(fs.readFileSync(artifactPath, 'utf8')) : {};
 assert(artifact.schema === 'pose-lab-offline-web-truth-parity-ready-weapon-fk-v1', 'parity artifact schema mismatch');
 assert(artifact.browserCaptureDeprecated === true, 'parity artifact should reject browser capture as proof');
 assert(artifact.sharedTruthModule === 'src/ready-weapon-truth.mjs', 'parity artifact should name shared truth module');
 assert(artifact.observedWebTruthPath === path.relative(projectRoot, observedPath), 'parity artifact should name observed web truth artifact');
 assert(offline.result === artifact.result, 'gate result should mirror parity artifact result');
 assert(artifact.parity?.visualVerdict === 'red', 'infrastructure check should preserve the current red build');
 if (failures.length) throw new Error(failures.join('\n'));
 console.log(JSON.stringify({ checked: ['pose-lab-offline-web-parity-red-build-contract', 'observed-web-truth-artifact', 'runtime-visibility-modeled'], evidencePath: path.relative(projectRoot, evidencePath), observed: evidence.observedWebTruth?.visualClass, offline: evidence.offlineTruth?.visualClass, result: artifact.result }, null, 2));

```
