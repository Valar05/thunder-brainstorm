#!/usr/bin/env python3
"""Bounded Loopit orchestration for Thunder generation and Hunger review."""
from __future__ import annotations

import argparse
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from thunder_brainstorm import build_pitch, choose_cards, load_cards  # noqa: E402
from tools.hunger_evaluator import evaluate_idea  # noqa: E402


def build_submission_bundle(
    *,
    focus: str,
    count: int,
    seed: int,
    max_attempts: int | None = None,
) -> dict[str, Any]:
    """Generate pitches until enough pass Hunger or the bounded loop is exhausted."""
    if not 1 <= count <= 20:
        raise ValueError("count must be between 1 and 20")
    attempt_limit = max_attempts if max_attempts is not None else max(count * 4, count)
    if attempt_limit < count:
        raise ValueError("max_attempts must be greater than or equal to count")
    if attempt_limit > 200:
        raise ValueError("max_attempts must not exceed 200")

    cards = load_cards()
    rng = random.Random(seed)
    accepted: list[dict[str, Any]] = []
    quarantined: list[dict[str, Any]] = []

    for attempt in range(1, attempt_limit + 1):
        chosen = choose_cards(cards, focus, rng)
        idea = build_pitch(chosen, focus or "open", rng)
        idea["loopit_attempt"] = attempt
        idea["hunger"] = evaluate_idea(idea)
        if idea["hunger"]["verdict"] == "PASS":
            accepted.append(idea)
        else:
            quarantined.append(idea)
        if len(accepted) >= count:
            break

    return {
        "schema": "hunger-loopit-thunder.v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "request": {
            "focus": focus or "open",
            "count": count,
            "seed": seed,
            "max_attempts": attempt_limit,
        },
        "summary": {
            "attempted": len(accepted) + len(quarantined),
            "accepted_for_human_review": len(accepted),
            "quarantined": len(quarantined),
            "complete": len(accepted) == count,
        },
        "submissions": accepted,
        "quarantine": quarantined,
        "delivery_boundary": (
            "This bundle is a GitHub Actions artifact candidate. No external account, "
            "publication surface, canon state, or recurring schedule is changed."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Thunder generation through a bounded Hunger/Loopit loop.")
    parser.add_argument("--focus", default="open")
    parser.add_argument("--count", type=int, default=3)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--max-attempts", type=int)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    bundle = build_submission_bundle(
        focus=args.focus,
        count=args.count,
        seed=args.seed,
        max_attempts=args.max_attempts,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(bundle["summary"], indent=2))
    return 0 if bundle["summary"]["complete"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
