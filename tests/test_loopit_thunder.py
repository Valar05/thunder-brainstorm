from __future__ import annotations

import unittest
from unittest.mock import patch

from tools.loopit_thunder import build_submission_bundle


class LoopitThunderTests(unittest.TestCase):
    def test_bundle_is_reproducible_except_for_timestamp(self) -> None:
        first = build_submission_bundle(focus="mobile action", count=2, seed=17)
        second = build_submission_bundle(focus="mobile action", count=2, seed=17)
        first.pop("generated_at")
        second.pop("generated_at")

        self.assertEqual(first, second)
        self.assertTrue(first["summary"]["complete"])
        self.assertEqual(2, first["summary"]["accepted_for_human_review"])

    def test_red_results_are_quarantined_and_loop_is_bounded(self) -> None:
        red = {
            "method": "hunger-v1",
            "verdict": "RED",
            "score": 0,
            "score_out_of": 5,
            "hard_gates": ["agency", "consequence", "refusal"],
            "failed_hard_gates": ["agency"],
            "dimensions": {},
            "invoice": [],
            "boundary": "test",
        }
        with patch("tools.loopit_thunder.evaluate_idea", return_value=red):
            bundle = build_submission_bundle(focus="open", count=1, seed=1, max_attempts=2)

        self.assertFalse(bundle["summary"]["complete"])
        self.assertEqual(2, bundle["summary"]["attempted"])
        self.assertEqual(2, bundle["summary"]["quarantined"])
        self.assertEqual([], bundle["submissions"])

    def test_request_size_is_bounded(self) -> None:
        with self.assertRaisesRegex(ValueError, "between 1 and 20"):
            build_submission_bundle(focus="open", count=21, seed=1)
        with self.assertRaisesRegex(ValueError, "exceed 200"):
            build_submission_bundle(focus="open", count=1, seed=1, max_attempts=201)


if __name__ == "__main__":
    unittest.main()
