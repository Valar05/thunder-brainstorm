# Thunder Archaeology Recovery Campaign

## Purpose

Make the existing local Thunder Brainstorm archaeology crawl self-verifying and self-recovering for ChatGPT/Fortress Online. Drew must not have to paste machine output back into chat.

This campaign does **not** replace `tools/turbo_survey.py`, Thunder Brainstorm, Phone Hands, Computer Hands, or Fortress Online. It verifies and promotes their existing outputs.

## Canonical implementation

- Crawl and merge: `tools/turbo_survey.py`
- Receipt-gated recovery wrapper: `tools/thunder_recovery_campaign.py`
- Execution bodies: Home Center → Phone Hands → `primary-phone`; Home Center → Computer Hands → `windows-hands-01` / THECAULDRON
- Durable recovery surface: Home Center Drive

## Required machine evidence

For each physical machine, locate or produce the current Thunder scan directory containing:

- `survey.json`
- `repos.jsonl`
- `receipt.json`

Validate `survey.json` schema `thunder.turbo-survey.v1`, machine identity, repo count, and SHA-256 against that directory's `receipt.json`.

The two required physical identities are:

- Android/Termux: `primary-phone`
- Windows: `THECAULDRON` / `windows-hands-01`

Do not accept repository files, GitHub Actions, historical receipts, or assistant summaries as substitutes for physical-machine survey output.

## Recovery sequence

1. Inspect durable Home Center runtime evidence and existing Thunder outputs before launching anything.
2. If a current scan already exists on a machine, verify and reuse it. Do not duplicate long-running work.
3. If missing, stale, corrupt, or incomplete, resume/re-run `tools/turbo_survey.py scan` through that machine's authorized execution body.
4. Bring the two verified scan directories into a body that can see both without destroying unique local evidence.
5. Run `tools/thunder_recovery_campaign.py --phone <phone-dir> --laptop <laptop-dir> --out <recovery-dir>`.
6. Require `RECEIPT_BACKED_COMPLETE` before claiming crawl acceptance.
7. The recovery directory must contain and validate:
   - `recovery_manifest.json`
   - `kingdom_survey.json`
   - `excavation_queue.jsonl`
   - kingdom `receipt.json`
8. Persist the recovery result through Home Center Drive. Maintain one canonical native recovery ledger/document plus inspectable durable machine-readable artifacts or references supported by the authorized Home Center lane.
9. Read the durable Home Center record back. Record file/document IDs, hashes where available, machine identities, repo counts, duplicate-group count, top excavation targets, and the exact source references needed to retrieve the full result.
10. Future ChatGPT sessions recover the campaign from Home Center Drive first. Never ask Drew to paste crawl output that the authorized bodies or Home Center can retrieve.

## ChatGPT recovery contract

When Drew says `Fortress Online`, `Thunder archaeology`, `local code crawl`, `Singularity Engine`, or asks what the crawl found:

1. Retrieve the canonical Home Center Drive recovery record.
2. Verify its status is `RECEIPT_BACKED_COMPLETE` and inspect its source references/readback evidence.
3. Use that durable result as the archaeology substrate.
4. If it is `CONTINUE_REQUIRED`, continue the earliest incomplete physical-machine/merge/delivery transition instead of asking Drew to reconstruct context.
5. Keep requested, implemented, tested, deployed, callable, executed, receipt-backed, delivered, and accepted states separate.

## Singularity Engine handoff

The Singularity Engine does not create a second crawler. It consumes Thunder's verified kingdom and excavation queue as the source for recovered mechanics, systems, art pipelines, rendering tricks, accessibility patterns, tooling, architecture, and reusable project ore. Loopit-style interaction and Hunger evaluation sit downstream of this archaeology substrate.
