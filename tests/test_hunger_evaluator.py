from __future__ import annotations

import unittest

from tools.hunger_evaluator import evaluate_idea, evaluate_payload


class HungerEvaluatorTests(unittest.TestCase):
    def test_passes_pitch_with_agency_consequence_refusal_and_mutation(self) -> None:
        idea = {
            "title": "A",
            "core_fantasy": "The player survives pressure and reshapes the route.",
            "player_loop": ["Choose how to interrupt an offer.", "Resolve a later consequence."],
            "signature_systems": ["Spend one visible resource."],
            "content_pipeline": ["Show state before and after the choice."],
            "validation_plan": ["Audit the changed state."],
            "early_risks": ["Hidden cost"],
        }

        result = evaluate_idea(idea)

        self.assertEqual("PASS", result["verdict"])
        self.assertEqual([], result["failed_hard_gates"])
        self.assertIn("Hidden cost", result["invoice"])

    def test_fails_closed_when_actor_refusal_and_consequence_are_absent(self) -> None:
        result = evaluate_idea({"title": "Pretty Fog", "core_fantasy": "A beautiful static image."})

        self.assertEqual("RED", result["verdict"])
        self.assertIn("agency", result["failed_hard_gates"])
        self.assertIn("consequence", result["failed_hard_gates"])
        self.assertIn("refusal", result["failed_hard_gates"])

    def test_payload_rejects_missing_ideas_list(self) -> None:
        with self.assertRaisesRegex(ValueError, "ideas"):
            evaluate_payload({})


if __name__ == "__main__":
    unittest.main()
