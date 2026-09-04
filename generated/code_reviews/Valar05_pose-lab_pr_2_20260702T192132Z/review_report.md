# Claude PR Review: Valar05/pose-lab#2

Summary: This PR introduces a `parentMode: 'hand-fk'` option for the Meshy Character weapon proxy, which parents the synthetic WeaponGrip bone directly to the RightHand bone (FK-driven) instead of the model root. It also updates the `gripLocalPosition` for the Meshy sabre attachment and adds a trace/validation tool. The logic is mostly sound, but there is one correctness risk around null-safety for `rightHand` in the `hand-fk` branch, and one dead function in the new test script.

Perspectives used: Foreman (implementation sequencing, null-safety, control flow), Gasket/Auditor (failure modes, missing guards, dead code)
Verified inline findings: 2
Report-only or rejected findings: 0

## Verified Findings

- medium `src/pose-lab.js:3860` Null dereference on `rightHand` when `handFkParent` is true but `rightHand` is null
  Recommendation: Add a null check before the new branch: `else if (handFkParent && rightHand) rightHand.add(root); else if (handFkParent) { console.warn('hand-fk parentMode requires a valid handBone'); return null; }`. Alternatively, extend the early-return guard to also cover the `hand-fk` case: `if (!rightHand && !sourceSocket && !handFkParent) return null; if (handFkParent && !rightHand) return null;`.
- low `tools/test_meshy_hand_fk_hilt_trace.mjs:55` Dead function `worldPosition` is defined but never called
  Recommendation: Remove the unused `worldPosition` function, or replace the manual `localPointFromWorld` call with it if that was the original intent.

## Report-Only Findings

No rejected findings.

## Test Gaps

- No automated test covers the `hand-fk` branch in `updateWeaponProxy` (the new runtime update path in pose-lab.js lines 3889-3907). The new trace tool validates the profile data and hilt oracle but does not exercise the live `updateWeaponProxy` code path, so the `boneRest` mutation and the `animatedSocketRotation` guard in that branch are untested.
- No test covers the null-safety scenario where `parentMode === 'hand-fk'` is set but `handBone` resolves to null (e.g., bone not found in model).
- The `--compare` assertion in the trace tool (`assert(payload.comparison.numericallyChangedFromBaseline, ...)`) will always pass when run without a baseline, meaning the comparison path is only exercised in CI if a baseline file is explicitly provided via `--compare`.

## Non-Postable Concerns

- No CI checks are registered for this PR head SHA (165213f6d5abc3a16cddc6d9323533d4893f225a), so there is no automated gate on the new test tool or the runtime changes.
- The `modelLocalOffset` field is applied in the `hand-fk` update path (line 3894) even though the bone is now parented to the hand, not the model. Depending on the coordinate frame intent, adding a model-space offset to a hand-local position may produce unexpected results if the hand is not at the model origin. This is a design question rather than a clear bug, since the current profile values appear to have been tuned empirically.
- The `positionMode` field in the `meshyCharacter` weaponProxy config is set to `'right-hand'` alongside `parentMode: 'hand-fk'`. The `userData.positionMode` is still written as `'right-hand'` (line 3840 base, unchanged), which is consistent, but any downstream code that reads `positionMode` to decide update behavior should be verified to not conflict with the new `hand-fk` early-return path.

## Read Log

- Tools used: get_pr_metadata, list_pr_files, get_pr_diff, read_file_at_ref, read_file_at_ref, list_ci_checks, search_repo_at_ref, search_repo_at_ref, search_repo_at_ref, search_repo_at_ref, search_repo_at_ref, search_repo_at_ref, search_repo_at_ref, search_repo_at_ref, read_file_at_ref, read_file_at_ref, search_repo_at_ref, search_repo_at_ref
- Files read: src/pose-lab.js, src/rig-profiles.js, tools/test_meshy_pose_parity_arm_contract.mjs
