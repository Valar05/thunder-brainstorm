"""Thunder Brainstorm adapter for deterministic playable proposals."""
import random
from typing import Any
from thunder_brainstorm import build_pitch, choose_cards, load_cards

MANIFEST = {"id": "thunder.brainstorm", "version": "1.0.0", "actions": ["generate_pitch"], "capabilities": ["pattern_cards", "seeded_random"]}

def handle(request: dict[str, Any]) -> dict[str, Any]:
    if request["action"] != "generate_pitch":
        raise ValueError("unsupported Thunder action")
    arguments = request["arguments"]
    seed = int(arguments.get("seed", 0))
    focus = str(arguments.get("focus", "open")).strip() or "open"
    rng = random.Random(seed)
    cards = choose_cards(load_cards(), focus, rng)
    return {"seed": seed, "focus": focus, "pitch": build_pitch(cards, focus, rng)}
