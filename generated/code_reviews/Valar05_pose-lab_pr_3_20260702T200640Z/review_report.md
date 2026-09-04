# Claude PR Review: Valar05/pose-lab#3

Summary: This PR replaces browser/device visual capture with a repo-owned offline/web "truth parity" harness for the Meshy Ready weapon-follow feature (new src/ready-weapon-truth.mjs, src/meshy-ready-runtime.mjs, tools/meshy_ready_weapon_offline_visual_truth.mjs, and supporting workflow_lib/promotion-gate changes), and updates docs to deprecate screenshots as acceptance evidence. The infrastructure itself is well-instrumented (schema'd artifacts, readback validation, contract tests). However, the PR also changes src/rig-profiles.js so the `SwordReady` clip alias now points at the new, still-red (`parity.visualVerdict: "red"`) `OneHandReady -> meshyCharacter [FPS-VISUAL-IK R-120 L-90]` candidate instead of the previously accepted `[FPS-REST-ARMS roll -120]` clip. This directly contradicts both the accepted baseline (`generated/workflow_state/meshy_fps_accepted_baseline.json` protects `swordReadyAliases` as the old value) and the PR's own restated policy ('Do not wire a candidate to startupClip, SwordReady, RestProbe... manually'), and it breaks two pre-existing, unmodified regression tests (tools/test_meshy_sabre_selection_contract.mjs and tools/test_pose_lab_no_bad_promotions.mjs) that assert SwordReady stays on the accepted T-pose clip and that protected selection surfaces do not drift from baseline. Separately, the new contract test tools/test_meshy_ready_weapon_fk_follow_contract.mjs unconditionally throws whenever the offline verifier's parity verdict is not "fixed" — and the generated evidence committed in this same PR is "red" — so this new test will fail every run until a follow-up fixes the actual weapon-follow pose, leaving the test suite red immediately after merge.

Perspectives used: F, o, r, e, m, a, n,  , (, s, e, q, u, e, n, c, i, n, g, /, v, e, r, i, f, i, c, a, t, i, o, n,  , o, f,  , t, h, e,  , p, r, o, m, o, t, i, o, n, -, g, a, t, e,  , a, n, d,  , s, e, l, e, c, t, i, o, n, -, s, u, r, f, a, c, e,  , p, r, o, t, e, c, t, i, o, n, s, ), ,,  , G, a, s, k, e, t, /, A, u, d, i, t, o, r,  , (, c, o, n, t, r, a, d, i, c, t, i, o, n,  , b, e, t, w, e, e, n,  , s, t, a, t, e, d,  , p, o, l, i, c, y, /, p, r, o, t, e, c, t, e, d,  , b, a, s, e, l, i, n, e,  , a, n, d,  , a, c, t, u, a, l,  , c, o, d, e,  , c, h, a, n, g, e, ;,  , u, n, v, e, r, i, f, i, e, d, /, s, e, l, f, -, f, a, i, l, i, n, g,  , t, e, s, t,  , s, h, i, p, p, e, d, )
Verified inline findings: 2
Report-only or rejected findings: 0

## Verified Findings

- high `src/rig-profiles.js:227` SwordReady alias is repointed to the unpromoted, currently-red FPS-VISUAL-IK Ready candidate instead of the accepted FPS-REST-ARMS calibration, contradicting the protected baseline and the repo's own promotion policy.
  Recommendation: Revert the SwordReady alias to the accepted FPS-REST-ARMS clip (or update generated/workflow_state/meshy_fps_accepted_baseline.json's swordReadyAliases through the actual promotion gate once the offline/web parity verdict is 'fixed'), and update/keep tools/test_meshy_sabre_selection_contract.mjs consistent so the protected-surface tests continue to pass.
- medium `tools/test_meshy_ready_weapon_fk_follow_contract.mjs:88` The new contract test unconditionally fails while the committed offline/web parity artifact's verdict is 'red', which it is in this same PR.
  Recommendation: Either gate this assertion behind an explicit 'expected red' allowlist/flag documented in the PR description, or land this test only once the offline/web parity gate is actually green, so the test suite state communicates truth rather than shipping a known-red assertion silently.

## Report-Only Findings

No rejected findings.

## Test Gaps

- No test was added/updated to confirm generated/workflow_state/meshy_fps_accepted_baseline.json's selectionSurfaces intentionally changed alongside src/rig-profiles.js's SwordReady alias; the two existing protection tests (test_meshy_sabre_selection_contract.mjs, test_pose_lab_no_bad_promotions.mjs) were left unmodified and will now fail.
- No CI check runs are configured/visible for this PR (list_ci_checks returned 0), so there is no external verification that the full test suite (including the newly-added always-red contract test) was actually run before merge.

## Non-Postable Concerns

- Could not execute the Node test suite directly in this environment; the failure conclusions for tools/test_meshy_sabre_selection_contract.mjs and tools/test_pose_lab_no_bad_promotions.mjs are derived from static string-substring analysis of the diff and unmodified test source, which is how these particular tests operate (literal profiles.includes(...) checks), so confidence is high but not execution-verified.
- The overall offline/web truth parity design (shared src/ready-weapon-truth.mjs module used by both browser runtime and the Node verifier) is a reasonable approach to reduce reliance on flaky device screenshots; this review does not flag that architecture itself as a problem.

## Read Log

- Tools used: get_pr_metadata, list_pr_files, get_pr_diff, list_ci_checks, read_file_at_ref, search_repo_at_ref, read_file_at_ref, read_file_at_ref, search_repo_at_ref, read_file_at_ref, read_file_at_ref, search_repo_at_ref, read_file_at_ref, read_file_at_ref, read_file_at_ref, read_file_at_ref, read_file_at_ref
- Files read: generated/workflow_state/meshy_fps_accepted_baseline.json, src/rig-profiles.js, tools/pose_lab_workflow_lib.mjs, tools/pose_lab_workflow_status.mjs, tools/test_meshy_joint_fk_onehand_ready_contract.mjs, tools/test_meshy_ready_weapon_fk_follow_contract.mjs, tools/test_meshy_ready_workbench_contract.mjs, tools/test_meshy_sabre_selection_contract.mjs, tools/test_pose_lab_no_bad_promotions.mjs
