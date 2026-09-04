# Quartermaster Verification - Valar05/pose-lab#2

Date: 2026-07-02
Mode: dry-run review, no GitHub comments posted

## PR Truth

- PR #1: `SUPERSEDED / DO NOT MERGE`, draft/open, 90 files, +10234/-323.
- PR #2: draft/open, 3 files, +232/-2.
- PR #2 changed files:
  - `src/pose-lab.js`
  - `src/rig-profiles.js`
  - `tools/test_meshy_hand_fk_hilt_trace.mjs`
- PR #2 head: `165213f6d5abc3a16cddc6d9323533d4893f225a`.
- GitHub check runs: 0.

## Clean Worktree Verification

A detached worktree at PR #2 head was used for execution checks.

Passing:

```sh
node tools/test_meshy_hand_fk_hilt_trace.mjs --out generated/quartermaster_hilt_trace/review
node tools/test_meshy_pose_parity_arm_contract.mjs
```

Failing:

```sh
node tools/test_meshy_core_retarget_contract.mjs
node tools/test_manual_weapon_placement_lock.mjs
node tools/test_socket_solver.mjs
node tools/test_meshy_weapon_path_ik.mjs
```

The failures all point to the changed Meshy `gripLocalPosition` literal. Existing contracts still lock the Meshy manual/semantic hilt candidate to `[0.6535, -0.02302, -0.07317]`, while PR #2 changes it to `[0.69507, -0.02421, -0.06231]`.

## Review Conclusion

PR #2 is narrow and does not smuggle the superseded PR #1 diff, but it is not merge-ready while existing repository contracts fail. Either preserve the locked literal and move the new oracle into a clearly promoted replacement contract, or intentionally update all affected contracts/docs with evidence explaining why the previous manual truth is no longer canonical.

Claude's static findings remain useful secondary issues, especially the `modelLocalOffset` coordinate-space ambiguity in `hand-fk` mode and the stale matrix update ordering in the new trace tool.
