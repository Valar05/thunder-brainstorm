# Claude PR Review: Valar05/pose-lab#2

Summary: This PR introduces a new `parentMode: 'hand-fk'` weapon proxy mode for the Meshy character rig, which parents the synthetic weapon bone directly to the right-hand FK bone instead of the model root. It also updates the `gripLocalPosition` oracle in the Meshy weapon attachment profile and adds a standalone trace/verification tool. The runtime logic changes are small and targeted; the main risks are a semantic offset-space mismatch, a dead function in the new test tool, and a fragile `--compare` assertion invariant. No CI checks are configured for this repo.

Perspectives used: Foreman: implementation sequencing, null-safety, and variable-scope verification, Gasket/Auditor: contradiction detection, failure modes, and test assertion correctness
Verified inline findings: 4
Report-only or rejected findings: 0

## Verified Findings

- medium `src/pose-lab.js:3897` `modelLocalOffset` added in hand-local space despite its name implying model space
  Recommendation: Either (a) rename the field to `handLocalOffset2` / `handExtraOffset` to make the space explicit, (b) document clearly that in `hand-fk` mode both `handLocalOffset` and `modelLocalOffset` are summed in hand-local space, or (c) transform `modelLocalOffset` from model space to hand-local space before adding it, consistent with how the two-hand-center path handles it.
- low `tools/test_meshy_hand_fk_hilt_trace.mjs:52` `worldPosition` helper function is defined but never called
  Recommendation: Remove the unused `worldPosition` function, or use it in place of the inline `localToWorld` calls to reduce duplication.
- low `tools/test_meshy_hand_fk_hilt_trace.mjs:176` `--compare` mode asserts that the baseline and current MUST differ, making the test fail if run twice against the same output
  Recommendation: Reconsider the assertion direction. A regression test should assert that the current value matches the baseline (i.e., `assert(!numericallyChangedFromBaseline, ...)`), or the `--compare` flag should be documented as a 'verify change was applied' mode with a clear comment explaining why divergence is required.
- low `tools/test_meshy_hand_fk_hilt_trace.mjs:155` `rightHand.updateMatrixWorld(true)` is called after `localToWorld` operations that depend on up-to-date world matrices
  Recommendation: Move `rightHand.updateMatrixWorld(true)` to immediately before the `localToWorld` calls (after all scene-graph mutations are complete), or call it once after all `add`/`position`/`quaternion` mutations and before any world-space queries.

## Report-Only Findings

No rejected findings.

## Test Gaps

- No automated test verifies the runtime behavior of `parentMode: 'hand-fk'` in `pose-lab.js` itself — the new trace tool only validates the profile data and a simplified offline scene graph, not the actual `buildWeaponProxy` / `updateWeaponProxy` code paths.
- The existing `test_meshy_pose_parity_arm_contract.mjs` contract does not assert anything about `parentMode: 'hand-fk'` or the new update branch, so a regression in the new code path would not be caught by that contract.
- No test covers the interaction between `parentMode: 'hand-fk'` and `animatedSocketRotation` being truthy (i.e., when a clip animates the WeaponGrip quaternion track while in hand-fk mode).

## Non-Postable Concerns

- No CI checks are configured for this repository (list_ci_checks returned 0 check runs). There is no automated gate preventing regressions from merging.
- The `pose-lab.js` file is very large (~3900+ lines) and was truncated by the read tool; the exact definition site and scope of `animatedSocketRotation` in the update function could not be directly verified from source. The existing test contract (`test_meshy_pose_parity_arm_contract.mjs`) asserts `js.includes('if (!animatedSocketRotation)')`, confirming the variable exists in the file, but its declaration relative to the new `hand-fk` block could not be confirmed line-by-line.
- The `gripLocalPosition` change from `[0.6535, -0.02302, -0.07317]` to `[0.69507, -0.02421, -0.06231]` is a tuning/calibration change. Its correctness depends on the physical sabre model geometry and cannot be verified through static analysis alone.

## Read Log

- Tools used: get_pr_metadata, list_pr_files, get_pr_diff, read_file_at_ref, read_file_at_ref, list_ci_checks, search_repo_at_ref, search_repo_at_ref, search_repo_at_ref, search_repo_at_ref, search_repo_at_ref, read_file_at_ref, search_repo_at_ref, search_repo_at_ref, search_repo_at_ref, search_repo_at_ref, read_file_at_ref, search_repo_at_ref, search_repo_at_ref
- Files read: src/pose-lab.js, src/rig-profiles.js, tools/test_meshy_pose_parity_arm_contract.mjs
