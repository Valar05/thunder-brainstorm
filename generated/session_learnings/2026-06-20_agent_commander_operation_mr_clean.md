# Agent Commander Operation Mr Clean Learnings

Date: 2026-06-20
Project: Agent Commander
Scope: local-first Termux command center for write-enabled Codex agents

## Knowledge Capture

### Rules

- Agent Commander web work is incomplete unless the durable `agent-commander-ui` tmux service is running or the blocker is explicitly reported.
- Cleanup must be archive-first. Failed runs, prompts, source packets, and generated context are evidence until a specific policy says otherwise.
- `data/agent_commander.sqlite3` is the database of record; `data/agent_commander.db` is legacy junk only when it is zero bytes.
- Project execution requires repo context, but basic command-center planning, shell actions, and maintenance actions must not be paralyzed by missing project selection.
- On Android shared storage, controlled writes plus immediate readback are safer than retrying patch tools after sandbox/path rejection.

### Patterns

- Acceptance Over Activity: report satisfied criteria and validation evidence, not effort.
- Challenge The Solution: preserve the intended outcome, not every described mechanism; the user asked for a cleanup, but the product needed a reusable maintenance operation.
- Extract The Plan: turn vague/frustrated requests into a short objective, approach, risk, and success condition before execution.
- Mine The Gold: convert repeated failure modes into durable docs, tests, or command surfaces.
- Maintenance as UI: if an operation is routine and user-facing, expose it in Command Center instead of requiring terminal archaeology.

### Design Decisions

- Added `scripts/maintenance.py` as an importable CLI plus admin action surface instead of a one-off cleanup script.
- Dry-run is the default; applying cleanup requires explicit `--apply --yes` or the `Apply cleanup` admin button.
- Stale queued/running admin jobs are marked `cancelled`, not deleted, so the process table stops lying while history remains inspectable.
- Runtime junk is moved to `archive/maintenance/<timestamp>/` with `manifest.json` and `report.md`, not deleted.
- The new `.gitignore` excludes runtime DB/log/archive state but keeps generated source packets and current agent context visible to Git.

### Discoveries

- The first cleanup dry-run found two stale queued admin jobs, two old info alerts, five duplicate `job-000001` generated folders, and one zero-byte legacy DB.
- After applying cleanup, a post-clean dry-run reported zero stale jobs, zero eligible alerts, and zero archive candidates.
- The test harness originally accepted appended tests after `unittest.main()` without discovering them; test count is part of evidence, not trivia.
- Current validation count is 61 tests after adding maintenance coverage.
- `gh` is authenticated for `Valar05`, but this repo initially had no `origin`; first push must create or attach a remote.

## Friction Audit

### Missing Scripts

- No pre-push script combines tests, maintenance dry-run, durable UI status, and secret scan into one publish gate.

### Missing Tools

- No built-in generated-log sanitizer or classifier exists yet. The repo can preserve context, but the tool should distinguish source packets from noisy stderr sludge.

### Missing Tests

- The suite now covers maintenance dry-run/apply/admin buttons, but it does not yet assert the durable tmux server contract from Python.
- There is no integration test for creating a fresh repo, pushing, and preserving private/public repository policy.

### Missing Documentation

- `PROJECT_ORIENTATION.md` now names the durable server commands, but it should also point to `docs/maintenance_policy.md` and this deep-ocean note.

### Missing Automation

- Cleanup preview/apply exists, but no scheduled or startup reconciliation marks stale jobs automatically.
- The admin UI can expose cleanup actions, but it does not yet show the latest maintenance report as a compact status widget.

## Build Next

Build one `scripts/preflight_publish.sh` command that runs:

1. `sh scripts/test.sh`
2. `python3 scripts/maintenance.py --dry-run`
3. `sh scripts/server_tmux.sh status`
4. a narrow secret scan excluding `.git`, `data`, and `archive`

The point is simple: before the boss says commit/push, the console should already know whether the package is clean. The broom should not need a pep talk.
