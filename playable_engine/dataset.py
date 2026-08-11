"""Deterministic synthetic training and evaluation data oracle."""
import random
from typing import Iterator
from .baseline import propose
from .canonical import content_hash

PROMPTS = [
    "A phone game about refusing a hungry machine and living with the later consequence.",
    "Turn a haunted convoy idea into a playable two-action loop with visible state.",
    "Break a campaign for local profiles, remix lineage, and QR export into parallel tasks.",
    "Plan schemas, plugin adapters, accessibility checks, and offline replay receipts.",
]

def generate_examples(seed: int = 0, count: int = 32) -> Iterator[dict]:
    rng = random.Random(seed)
    for index in range(count):
        prompt = PROMPTS[index % len(PROMPTS)]
        mode = "PLAYABLE_COMPILE" if index % 2 == 0 else "CAMPAIGN_PLAN"
        if index >= len(PROMPTS):
            prompt = f"{prompt} Variant {rng.randrange(1_000_000):06d}."
        envelope = propose(prompt, mode)
        example = {"id": f"synthetic-{seed}-{index:05d}", "split": "train" if index % 10 else "evaluation", "source": "deterministic-synthetic-v1", "prompt": prompt, "mode": mode, "target": envelope}
        example["provenance_hash"] = content_hash(example)
        yield example
