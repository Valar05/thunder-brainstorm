"""Proposal to validation to deterministic execution."""
import re
from typing import Any
from . import baseline
from .canonical import content_hash
from .contracts import validate_envelope, validate_playable
from .planner import build_plan
from .plugins import PluginRegistry
from .thunder_plugin import MANIFEST as THUNDER_MANIFEST, handle as thunder_handle

class OfflineCompiler:
    def __init__(self, model: Any | None = None):
        self.model = model
        self.registry = PluginRegistry()
        self.registry.register(THUNDER_MANIFEST, thunder_handle)
        self.cache: dict[str, dict] = {}

    def propose(self, prompt: str, mode: str) -> dict:
        key = content_hash({"prompt": prompt, "mode": mode})
        if key not in self.cache:
            proposal = self.model.propose(prompt, mode) if self.model else baseline.propose(prompt, mode)
            self.cache[key] = validate_envelope(proposal)
        return self.cache[key]

    def run(self, prompt: str, mode: str, seed: int = 0) -> dict:
        envelope = self.propose(prompt, mode)
        name = envelope["action"]["name"]
        if name == "park":
            return {"status": "PARK", "envelope": envelope}
        if name == "plan_campaign":
            plan = build_plan(envelope["action"]["arguments"]["prompt"])
            return {"status": "PASS", "envelope": envelope, "plan": plan, "receipt": content_hash(plan)}
        thunder = self.registry.execute("thunder.brainstorm", "generate_pitch", {"focus": envelope["action"]["arguments"]["prompt"], "seed": seed})
        playable = self._playable_from_pitch(thunder["output"]["pitch"], prompt, seed)
        validate_playable(playable)
        return {"status": "PASS", "envelope": envelope, "playable": playable, "receipt": content_hash(playable)}

    @staticmethod
    def _playable_from_pitch(pitch: dict, prompt: str, seed: int) -> dict:
        slug = re.sub(r"[^a-z0-9]+", "-", pitch["title"].lower()).strip("-")
        return {
            "version": 1,
            "id": f"{slug}-{seed}",
            "title": pitch["title"],
            "prompt": prompt,
            "inputs": ["tap", "swipe", "keyboard"],
            "state": {"pressure": 0, "appetite": 1, "consequence_queue": []},
            "actions": [
                {"id": "commit", "label": "Commit", "input": "tap_or_enter", "effect": {"pressure": 1, "appetite": -1, "queue": "echo_commit"}},
                {"id": "refuse", "label": "Refuse", "input": "swipe_left_or_r", "effect": {"pressure": -1, "appetite": 1, "queue": "echo_refusal"}},
            ],
            "causality": {
                "visible_before": ["pressure", "appetite"],
                "visible_after": ["pressure delta", "appetite delta", "queued consequence"],
                "later_consequence": "the next draw resolves the queued echo before offering another choice",
            },
            "accessibility": {"keyboard": True, "screen_reader": True, "captions": True, "reduced_motion": True},
            "lineage": {"parent": None, "compiler": "thunder.brainstorm", "seed": seed},
            "pattern_stack": pitch["pattern_stack"],
            "player_loop": pitch["player_loop"],
        }
