"""Deterministic grammar baseline used before and beside the trained model."""
from .canonical import content_hash

def propose(prompt: str, mode: str) -> dict:
    normalized = " ".join(prompt.split())
    ambiguous = len(normalized) < 8 or normalized.lower() in {"make it", "do it", "something fun"}
    action = "park" if ambiguous else ("compile_playable" if mode == "PLAYABLE_COMPILE" else "plan_campaign")
    arguments = {"reason": "prompt lacks enough concrete intent", "missing": ["play fantasy or deliverable"]} if ambiguous else {"prompt": normalized}
    return {
        "version": 1,
        "mode": mode,
        "action": {"name": action, "arguments": arguments},
        "provenance": {"producer": "deterministic-grammar-v1", "prompt_hash": content_hash(normalized)},
    }
