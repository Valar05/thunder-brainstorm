import copy
import json
import tempfile
import unittest
from pathlib import Path
from playable_engine.canonical import content_hash
from playable_engine.compiler import OfflineCompiler
from playable_engine.config import load_config
from playable_engine.contracts import ContractError
from playable_engine.dataset import generate_examples
from playable_engine.model_adapter import FunctionGemmaBoundary
from playable_engine.planner import build_plan, validate_plan
from playable_engine.plugins import PluginRegistry

class PlayableEngineTests(unittest.TestCase):
    def test_playable_compile_is_replayable_and_causal(self):
        compiler = OfflineCompiler()
        prompt = "A hungry fortress where refusal changes the next encounter."
        first = compiler.run(prompt, "PLAYABLE_COMPILE", seed=19)
        self.assertEqual(first, compiler.run(prompt, "PLAYABLE_COMPILE", seed=19))
        self.assertEqual(first["status"], "PASS")
        self.assertTrue(first["playable"]["causality"]["later_consequence"])
        self.assertIn("refuse", {action["id"] for action in first["playable"]["actions"]})

    def test_ambiguous_prompt_parks(self):
        self.assertEqual(OfflineCompiler().run("make it", "PLAYABLE_COMPILE")["status"], "PARK")

    def test_campaign_plan_covers_atoms_and_parallelizes(self):
        plan = build_plan("Build schemas. Add plugins; prove accessibility plus export receipts.")
        self.assertEqual({a["id"] for a in plan["atoms"]}, {x for t in plan["tasks"] for x in t["atom_ids"]})
        self.assertEqual({"atom-materialization"}, {t["parallel_group"] for t in plan["tasks"]})
        self.assertTrue(all(len(atom["source_span"]) == 2 for atom in plan["atoms"]))
        sequential = build_plan("Build schemas then validate the schemas. Add plugins.")
        self.assertEqual(["T001"], sequential["tasks"][1]["dependencies"])
        self.assertEqual([], sequential["tasks"][2]["dependencies"])

    def test_planner_rejects_shared_writes(self):
        broken = copy.deepcopy(build_plan("Build schemas. Add plugins."))
        broken["tasks"][1]["writes"] = broken["tasks"][0]["writes"]
        with self.assertRaisesRegex(ContractError, "shared writable"):
            validate_plan(broken)

    def test_planner_rejects_cycle(self):
        broken = copy.deepcopy(build_plan("Build schemas. Add plugins."))
        broken["tasks"][0]["dependencies"] = [broken["tasks"][1]["id"]]
        broken["tasks"][1]["dependencies"] = [broken["tasks"][0]["id"]]
        with self.assertRaisesRegex(ContractError, "cycle"):
            validate_plan(broken)

    def test_config_extensions_cannot_replace_base(self):
        with tempfile.TemporaryDirectory() as directory:
            extension = Path(directory) / "extension.json"
            extension.write_text(json.dumps({"version": 1, "actions": {"park": {}}}), encoding="utf-8")
            with self.assertRaisesRegex(ContractError, "attempts to replace"):
                load_config("config/default.json", [extension])

    def test_plugin_registry_denies_shell_capability(self):
        with self.assertRaisesRegex(ContractError, "forbidden"):
            PluginRegistry().register({"id": "bad", "version": "1", "actions": ["run"], "capabilities": ["shell"]}, lambda request: {})

    def test_model_boundary_rejects_unknown_action(self):
        payload = {"version": 1, "mode": "PLAYABLE_COMPILE", "action": {"name": "run_shell", "arguments": {}}, "provenance": {"producer": "test", "prompt_hash": "sha256:x"}}
        model = FunctionGemmaBoundary(
            lambda prompt, mode: json.dumps(payload),
            {"checkpoint_hash": "sha256:c", "tokenizer_hash": "sha256:t", "runtime": "test", "decoding": "greedy"},
        )
        with self.assertRaisesRegex(ContractError, "not allowed"):
            model.propose("concrete prompt", "PLAYABLE_COMPILE")
        valid_action_wrong_receipt = {
            "version": 1, "mode": "CAMPAIGN_PLAN",
            "action": {"name": "plan_campaign", "arguments": {"prompt": "concrete prompt"}},
            "provenance": {"producer": "test", "prompt_hash": "sha256:wrong"},
        }
        wrong = FunctionGemmaBoundary(
            lambda prompt, mode: json.dumps(valid_action_wrong_receipt),
            {"checkpoint_hash": "sha256:c", "tokenizer_hash": "sha256:t", "runtime": "test", "decoding": "greedy"},
        )
        with self.assertRaisesRegex(ContractError, "returned mode"):
            wrong.propose("concrete prompt", "PLAYABLE_COMPILE")

    def test_dataset_is_deterministic_and_hashed(self):
        first = list(generate_examples(seed=7, count=12))
        self.assertEqual(first, list(generate_examples(seed=7, count=12)))
        for example in first:
            value = dict(example)
            receipt = value.pop("provenance_hash")
            self.assertEqual(receipt, content_hash(value))

if __name__ == "__main__":
    unittest.main()
