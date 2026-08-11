"""Fail-closed contracts at the model/engine boundary."""
from typing import Any

MODES = {"PLAYABLE_COMPILE", "CAMPAIGN_PLAN"}
ACTION_BY_MODE = {
    "PLAYABLE_COMPILE": {"compile_playable", "park"},
    "CAMPAIGN_PLAN": {"plan_campaign", "park"},
}

class ContractError(ValueError):
    pass

def _require_keys(value: dict[str, Any], required: set[str], where: str) -> None:
    missing = required - value.keys()
    if missing:
        raise ContractError(f"{where} missing: {', '.join(sorted(missing))}")

def validate_envelope(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ContractError("envelope must be an object")
    _require_keys(value, {"version", "mode", "action", "provenance"}, "envelope")
    if value["version"] != 1:
        raise ContractError("unsupported envelope version")
    mode = value["mode"]
    if mode not in MODES:
        raise ContractError(f"unknown mode: {mode!r}")
    action = value["action"]
    if not isinstance(action, dict):
        raise ContractError("action must be an object")
    _require_keys(action, {"name", "arguments"}, "action")
    if action["name"] not in ACTION_BY_MODE[mode]:
        raise ContractError(f"action {action['name']!r} is not allowed in {mode}")
    if not isinstance(action["arguments"], dict):
        raise ContractError("action arguments must be an object")
    provenance = value["provenance"]
    if not isinstance(provenance, dict):
        raise ContractError("provenance must be an object")
    _require_keys(provenance, {"producer", "prompt_hash"}, "provenance")
    return value

def validate_playable(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ContractError("playable must be an object")
    _require_keys(value, {"version", "id", "title", "inputs", "state", "actions", "causality", "accessibility", "lineage"}, "playable")
    action_ids: set[str] = set()
    for action in value["actions"]:
        _require_keys(action, {"id", "label", "input", "effect"}, "playable action")
        if action["id"] in action_ids:
            raise ContractError(f"duplicate action id: {action['id']}")
        action_ids.add(action["id"])
    _require_keys(value["causality"], {"visible_before", "visible_after", "later_consequence"}, "causality")
    _require_keys(value["accessibility"], {"keyboard", "screen_reader", "captions", "reduced_motion"}, "accessibility")
    return value
