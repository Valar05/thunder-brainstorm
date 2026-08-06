#!/usr/bin/env python3
"""Deterministic Hunger gate for Thunder Brainstorm idea records.

The gate does not claim creative or canonical authority.  It checks whether a
generated pitch makes agency, appetite, consequence, refusal, and mutation
legible enough to enter an automatic submission bundle for human review.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Iterable


DIMENSIONS = {
    "agency": {
        "fields": ("core_fantasy", "player_loop", "signature_systems"),
        "terms": ("player", "choose", "authorize", "act", "decision"),
        "question": "Who acts or wants?",
    },
    "appetite": {
        "fields": ("core_fantasy", "player_loop", "pattern_stack", "signature_systems"),
        "terms": ("pressure", "resource", "offer", "need", "want", "spend", "gain", "extract"),
        "question": "What does the system or actor want?",
    },
    "consequence": {
        "fields": ("player_loop", "content_pipeline", "validation_plan", "early_risks"),
        "terms": ("consequence", "state", "change", "changed", "later", "echo", "risk", "cost", "debt"),
        "question": "Who must carry or verify the consequence?",
    },
    "refusal": {
        "fields": ("player_loop", "signature_systems", "design_questions"),
        "terms": ("choose", "interrupt", "refuse", "decline", "skip", "route", "exit", "stop", "alternative"),
        "question": "Can the actor refuse or change form?",
    },
    "mutation": {
        "fields": ("core_fantasy", "player_loop", "content_pipeline", "validation_plan"),
        "terms": ("reshape", "alter", "change", "next", "later", "echo", "replay", "mutate", "before and after"),
        "question": "Does the act change the next available state?",
    },
}

HARD_GATES = ("agency", "consequence", "refusal")


def _strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from _strings(item)


def _field_text(idea: dict[str, Any], fields: tuple[str, ...]) -> str:
    return "\n".join(text for field in fields for text in _strings(idea.get(field, "")))


def _first_evidence(text: str, terms: tuple[str, ...]) -> str:
    for raw_line in text.splitlines():
        line = re.sub(r"\s+", " ", raw_line).strip()
        if any(re.search(rf"\b{re.escape(term)}\b", line, re.IGNORECASE) for term in terms):
            return line[:240]
    return ""


def evaluate_idea(idea: dict[str, Any]) -> dict[str, Any]:
    """Return a stable, evidence-bearing Hunger verdict for one pitch."""
    dimensions: dict[str, dict[str, Any]] = {}
    for name, rule in DIMENSIONS.items():
        text = _field_text(idea, rule["fields"])
        evidence = _first_evidence(text, rule["terms"])
        dimensions[name] = {
            "question": rule["question"],
            "passed": bool(evidence),
            "evidence": evidence or "No explicit evidence in the generated pitch.",
        }

    passed_count = sum(1 for value in dimensions.values() if value["passed"])
    failed_hard_gates = [name for name in HARD_GATES if not dimensions[name]["passed"]]
    verdict = "PASS" if passed_count >= 4 and not failed_hard_gates else "RED"
    invoice = [str(x) for x in idea.get("early_risks", []) if str(x).strip()]

    return {
        "method": "hunger-v1",
        "verdict": verdict,
        "score": passed_count,
        "score_out_of": len(DIMENSIONS),
        "hard_gates": list(HARD_GATES),
        "failed_hard_gates": failed_hard_gates,
        "dimensions": dimensions,
        "invoice": invoice,
        "boundary": (
            "A PASS permits bundling for human review only. It does not grant canon, "
            "publication, deployment, account access, or acceptance."
        ),
    }


def evaluate_payload(payload: dict[str, Any]) -> dict[str, Any]:
    ideas = payload.get("ideas")
    if not isinstance(ideas, list):
        raise ValueError("input must contain an 'ideas' list")
    evaluated = []
    for idea in ideas:
        if not isinstance(idea, dict):
            raise ValueError("every idea must be a JSON object")
        item = dict(idea)
        item["hunger"] = evaluate_idea(idea)
        evaluated.append(item)
    return {"ideas": evaluated}


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply the deterministic Hunger gate to Thunder ideas.")
    parser.add_argument("input", type=Path, help="Thunder JSON file containing an ideas list.")
    parser.add_argument("--out", type=Path, required=True, help="Destination JSON file.")
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = evaluate_payload(payload)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
