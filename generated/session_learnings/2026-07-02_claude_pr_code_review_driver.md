# Claude PR Code Review Driver - Session Learnings

Date: 2026-07-02
Project: thunder-brainstorm
Status: durable workflow note

## Knowledge Capture

### Rules

- Claude is the better default automated critic when Codex/OpenAI may have authored the implementation. The author model can explain intent or propose fixes, but it should not be the sole reviewer of its own work.
- Thunder owns the Claude PR review runner and artifacts. Agent Closet supplies perspective doctrine; the workspace skill supplies invocation.
- Do not build source packets for PR review. Claude must read the PR/repo through read-only tools. If repo or PR access fails, the run fails hard instead of reviewing pasted source context.
- Dry-run is the default. Inline GitHub comments require explicit `--post` and only verified changed-line findings are posted.
- Quartermaster/Codex remains the verifier and synthesis layer. Claude findings are not true until they map back to repository evidence and changed diff lines.

### Patterns

- Use a mission-and-tools review shape: concise mission, bounded client tools, tool transcript, strict final JSON, local verifier, report/payload artifacts.
- Keep review tools read-only and narrow: PR metadata, file list, diff, file-at-ref reads, repo search, CI checks, and final review submission. Avoid general shell execution inside the model tool loop.
- Preserve `repo_read_log.json`, `tool_transcript.jsonl`, `claude_review.json`, `verified_findings.json`, `github_review_payload.json`, and `review_report.md` so later agents can audit what was read, what Claude claimed, and what was considered postable.
- Add offline fixtures for PR review development. Capturing PR metadata, diff, file contents, and checks once saves model tokens and avoids repeated live GitHub/API dependency during tests.

### Design Decisions

- Build a new `tools/claude_code_review.py` instead of stretching `tools/call_claude_packet.py`. The existing helper is source-packet-shaped; PR review now explicitly rejects source-packet fallback.
- Use stdlib HTTP and `gh api` rather than adding dependencies. Thunder tools already follow this low-dependency Termux-friendly pattern.
- Put the Codex entrypoint in `/storage/emulated/0/Documents/GodotProjects/.codex/skills/claude-pr-code-review/` because this is a workspace-level skill, not one product repo's private doctrine.
- Add `tools/capture_pr_review_fixture.py` as the next sanity-saving tool. It turns live PR reads into deterministic `--mock-github` fixtures.

### Discoveries

- Thunder had packet conventions under `generated/source_packets/`, but the review workflow deliberately uses `generated/code_reviews/` because review runs need mission/read-log/report artifacts rather than source packets.
- The prior `code-review-claude-critics` skill remains useful prior art for review standards, but its packet mechanism is now superseded for PR review.
- The workspace skill validates with `quick_validate.py`, and the runner validates with stdlib tests in `tools/test_claude_code_review.py`.

## Friction Audit

### Missing Scripts

- Before `tools/capture_pr_review_fixture.py`, every realistic review-driver test required either live GitHub access or hand-built mock files.
- Still missing: `tools/validate_code_review_artifacts.py generated/code_reviews/...` to check all expected artifacts and internal consistency after a real run.

### Missing Tools

- No local checkout adapter yet. If GitHub API reads are insufficient but a local repo exists, the runner still cannot use that checkout as a read backend.
- No provider-comparison abstraction yet. That is intentionally deferred until Claude-first review proves useful in practice.

### Missing Tests

- Still needed: transcript replay tests for real Claude `tool_use` / `tool_result` sequences.
- Still needed: multi-file PR payload tests and deleted-line comment payload tests.
- Still needed: failure test for Claude finalizing after only metadata/diff reads without reading touched file contents.

### Missing Documentation

- Thunder README now names the Claude PR review runner, but it still needs a fuller environment checklist for `gh auth`, `ANTHROPIC_API_KEY`, PR read permissions, and `--post` write permissions.
- The distinction between old Claude packet review and new direct-repo Claude PR review should be captured in any future code-review index or Agent Closet workflow map.

### Missing Automation

- No one-command smoke target exists yet for runner syntax, unit tests, skill validation, and diff check.
- The runner prints the output directory, but future automation should also print the exact report, payload, and verified-findings paths for fast opening.

## Build Next

Build `tools/validate_code_review_artifacts.py` next. It should accept a `generated/code_reviews/...` directory and verify required artifacts, JSON validity, changed-line payload consistency, and report presence.
