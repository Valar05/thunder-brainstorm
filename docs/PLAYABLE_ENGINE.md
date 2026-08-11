# Thunder Playable Engine

This package turns a prompt into either a finite local playable package or an atom-preserving campaign plan.

## Authority boundary

The embedded model is a proposer. It emits a versioned command envelope and receives no shell, network, or raw-filesystem capability. The engine validates the envelope, allowlists its action, runs deterministic code, validates the result, then records a canonical SHA-256 receipt. Invalid or underspecified work parks instead of guessing.

FunctionGemmaBoundary is the first embedded-runner adapter. It records the checkpoint, tokenizer, runtime, and decoding receipt. The runner stays injectable so LiteRT-LM or another phone-local runtime can be integrated without placing model code inside the executor.

## Modes

- PLAYABLE_COMPILE: Thunder pattern cards plus a seed produce a configuration-complete two-action playable with visible state, refusal, and a later consequence.
- CAMPAIGN_PLAN: the prompt becomes an atom ledger, isolated task leaves, safe parallel groups, and a single merge gate.

The deterministic grammar baseline remains available for offline bootstrap, golden-data generation, failure recovery, and comparison against trained checkpoints.

## Phone-local product

The default profile binds to 127.0.0.1, requires no network, and names /storage/emulated/0/Documents/GodotProjects as the phone workspace. PWA/WebView UI, SQLite event storage, content-addressed artifacts, remix lineage, recordings, file/QR transfer, and nonvisual interaction are integration surfaces; this branch establishes the compiler contracts they consume.

No Loopit code, private content, user-generated content, branding, cloud quotas, engagement ranking, or hidden telemetry is incorporated. The retained idea is an atomic playable post with local feed, remix lineage, and creator collections.

## Training path

tools/generate_training_data.py emits reproducible JSONL prompt/envelope pairs with source and split metadata. The next retained-model gates are: freeze a baseline; add reviewed Thunder and Hunger PASS/RED examples plus hard-negative PARK cases; supervised fine-tune; evaluate exact contract validity and downstream simulation; optionally preference-tune; quantize/convert; and pass airplane-mode phone acceptance. Accepted envelopes are hashed and replayed because model inference itself is not presumed byte-deterministic.

## Commands

    python tools/playable_compiler.py "A hungry fortress where refusal changes the next draw." --seed 19
    python tools/playable_compiler.py "Build schemas. Add plugins. Prove phone-local replay." --mode CAMPAIGN_PLAN
    python tools/generate_training_data.py --seed 7 --count 32
    python -m unittest discover -s tests -v
