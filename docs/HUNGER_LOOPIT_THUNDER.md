# Hunger → Loopit → Thunder Brainstorm

## Recovered commission

Drew’s durable command is: “Run Hunger on Loopit automatic generation, Thunder Brainstorm, automatic submission via ChatGPT scheduling.” Drew later selected the lane: “Command center use GitHub.”

No external Loopit service, API, repository, credential, destination account, or submission schema was identified in the durable record. This implementation therefore uses `Loopit` only as Drew’s protected workflow name for a bounded repository-local generation loop. It does not install or impersonate the unrelated public `dimkah/loopit` project.

## Implemented contract

`tools/loopit_thunder.py` repeatedly asks Thunder Brainstorm for a deterministic pitch, sends each pitch through `tools/hunger_evaluator.py`, accepts only Hunger `PASS` records into a candidate bundle, quarantines `RED` records, and stops after a bounded number of attempts.

The Hunger gate asks five evidence-bearing questions:

1. Who acts or wants?
2. What does the system or actor want?
3. Who must carry or verify the consequence?
4. Can the actor refuse or change form?
5. Does the act change the next available state?

Agency, consequence, and refusal are hard gates. A pass only permits human review. It grants no canon, publication, deployment, account access, or acceptance.

## Local use

```sh
python -m unittest discover -s tests -v
python tools/loopit_thunder.py --focus "mobile action" --count 3 --seed 17 --out generated/automation/hunger-loopit-thunder.json
```

## GitHub callability

`.github/workflows/hunger-loopit-thunder.yml` exposes only `workflow_dispatch`. It runs tests, creates the bundle, and uploads the JSON as a short-lived GitHub Actions artifact. The workflow has read-only repository permissions and does not publish or contact an external platform.

After this workflow is merged into the default branch, Command Center can dispatch `hunger-loopit-thunder.yml` with `focus`, `count`, and `seed` inputs. A ChatGPT schedule can be commissioned separately to perform that dispatch and report the run/artifact. No schedule is created or enabled by this repository change.

## Remaining authority gates

- Drew must identify any external Loopit product or submission destination before an adapter can be built.
- Drew must choose cadence, timezone, default focus/count/seed policy, and notification behavior before a recurring ChatGPT automation is enabled.
- Drew or the repository’s normal merge authority must merge the implementation before the workflow becomes callable from the default branch.
