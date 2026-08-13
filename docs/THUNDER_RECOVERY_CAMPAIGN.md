# Thunder Archaeology Recovery Campaign

## Purpose

Make the existing local Thunder Brainstorm archaeology crawl self-verifying and self-recovering for ChatGPT/Fortress Online. Drew must not have to paste machine output back into chat.

This campaign does **not** replace `tools/turbo_survey.py`, Thunder Brainstorm, Phone Hands, Computer Hands, or Fortress Online. It verifies and promotes their existing outputs.

## Canonical implementation

- Crawl and merge: `tools/turbo_survey.py`
- Receipt-gated local recovery verifier: `tools/thunder_recovery_campaign.py`
- Execution bodies: Home Center → Phone Hands → `primary-phone`; Home Center → Computer Hands → `windows-hands-01` / THECAULDRON
- Durable recovery surface: Home Center Drive
- Canonical recovery ledger: `Thunder Archaeology Recovery — Canonical Ledger`, Drive file ID `1kLHfricUFzvKb9KiFZdvrA1Yw123Eg44yxe5B9X5ScY`

## State law

The local recovery verifier may prove **LOCAL RECOVERY VERIFIED** only. Its successful state is `RECOVERY_VERIFIED_PENDING_HOME_CENTER_DELIVERY`.

It may never grant campaign acceptance. Campaign `ACCEPTED` / `RECEIPT_BACKED_COMPLETE` exists only after the verified recovery artifacts or exact durable references are delivered through Home Center Drive and read back there.

Requested, implemented, tested, deployed, callable, executed, receipt-backed, delivered, and accepted remain separate states.

## Required machine evidence

For each physical machine, locate or produce the current Thunder scan directory containing:

- `survey.json`
- `repos.jsonl`
- `receipt.json`

Validate `survey.json` schema `thunder.turbo-survey.v1`, non-empty repo coverage, expected machine label, environment-machine provenance, timestamp freshness, repo count, and SHA-256 against that directory's `receipt.json`.

The two required physical identities are:

- Android/Termux: `primary-phone`
- Windows: `THECAULDRON` / `windows-hands-01`

Caller labels alone are not physical-body proof. Preserve the corresponding Home Center / Phone Hands / Computer Hands execution ticket or receipt reference. Do not accept repository files, GitHub Actions, historical chat claims, or assistant summaries as substitutes for physical-machine output.

## Venice hard gates

`tools/thunder_recovery_campaign.py` schema `thunder.recovery-campaign.v3` must enforce:

- expected machine labels and receipt identity;
- default 24-hour freshness unless explicitly changed by the campaign;
- non-empty survey coverage;
- survey/receipt timestamp, repo-count, and SHA-256 agreement;
- nonzero merge process exits fail closed;
- exact kingdom machine-set equality with the two verified inputs;
- exact repository membership equality between verified surveys and the kingdom, not merely matching counts;
- exact excavation queue repository membership equality with the kingdom, not merely matching counts;
- valid JSONL for the excavation queue;
- hashes for survey, receipt, kingdom, queue, and kingdom receipt in the recovery manifest;
- explicit separation between `local_recovery_verified` and `campaign_accepted`.

## Recovery sequence

1. Read the canonical Home Center recovery ledger and current Thunder implementation.
2. Inspect live Home Center runtime receipts and existing Thunder outputs before launching anything.
3. If a current scan already exists on a machine, verify and reuse it. Do not duplicate long-running work.
4. If missing, stale, corrupt, empty, or incomplete, resume/re-run `tools/turbo_survey.py scan` through that machine's authorized execution body.
5. Bring the two verified scan directories into a body that can see both without destroying unique local evidence.
6. Run `tools/thunder_recovery_campaign.py --phone <phone-dir> --laptop <laptop-dir> --out <recovery-dir>` with physical execution receipt references where available.
7. Require `local_recovery_verified=true`, `campaign_accepted=false`, and state `RECOVERY_VERIFIED_PENDING_HOME_CENTER_DELIVERY` before advancing to delivery.
8. The recovery directory must contain and validate:
   - `recovery_manifest.json`
   - `kingdom_survey.json`
   - `excavation_queue.jsonl`
   - kingdom `receipt.json`
9. Persist the recovery result or exact durable artifact references through Home Center Drive.
10. Update and read back the canonical recovery ledger with machine identities, environment identities, execution receipts, timestamps, repo counts, duplicate groups, hashes, top excavation targets, and full artifact IDs/references or exact authorized-body paths.
11. Only after Home Center readback may the campaign ledger advance to `ACCEPTED` / `RECEIPT_BACKED_COMPLETE`.

## ChatGPT recovery contract

When Drew says `Fortress Online`, `Thunder archaeology`, `local code crawl`, `Singularity Engine`, or asks what the crawl found:

1. Retrieve the canonical Home Center Drive recovery ledger first.
2. Inspect its source references/readback evidence.
3. If the ledger is `ACCEPTED` / `RECEIPT_BACKED_COMPLETE`, use that durable result as the archaeology substrate.
4. If it is `CONTINUE_REQUIRED` or `RECOVERY_VERIFIED_PENDING_HOME_CENTER_DELIVERY`, continue the earliest incomplete physical-machine, merge, delivery, or readback transition instead of asking Drew to reconstruct context.
5. Never ask Drew to paste crawl output that authorized bodies or Home Center can retrieve.

## Singularity Engine handoff

The Singularity Engine does not create a second crawler. It consumes Thunder's verified kingdom and excavation queue as the source for recovered mechanics, systems, art pipelines, rendering tricks, accessibility patterns, tooling, architecture, and reusable project ore. Loopit-style interaction and Hunger evaluation sit downstream of this archaeology substrate.
