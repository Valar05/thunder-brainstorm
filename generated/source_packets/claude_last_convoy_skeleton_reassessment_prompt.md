# Claude Prompt: Last Convoy Skeleton Reassessment

Return only a JSON object. Do not include prose outside JSON.

Use the source packet to reassess Last Convoy before implementation continues. The user suspects the current skeleton is not worth putting meat on yet. Your job is to critique the current skeleton and propose stronger core-loop directions.

Required JSON shape:

{
  "overall_read": {
    "verdict": "continue_current|pivot_skeleton|hybridize",
    "one_sentence_reason": "...",
    "main_risk": "..."
  },
  "current_skeleton_diagnosis": {
    "what_is_promising": ["..."],
    "what_is_weak": ["..."],
    "missing_core_tension": "...",
    "what_not_to_build_yet": ["..."]
  },
  "candidate_skeletons": [
    {
      "name": "...",
      "core_thesis": "...",
      "player_loop_20_seconds": "...",
      "why_convoy_matters": "...",
      "pressure_model": "...",
      "upgrade_model": "...",
      "what_to_reuse_from_current_port": ["..."],
      "what_to_cut_or_delay": ["..."],
      "biggest_design_risk": "...",
      "first_test": {
        "implementation_scope": "...",
        "success_signal": "...",
        "failure_signal": "..."
      }
    }
  ],
  "recommended_next_slice": {
    "slice_name": "...",
    "why_this_before_meat": "...",
    "must_build": ["..."],
    "must_not_build": ["..."],
    "tuning_knobs": ["..."],
    "test_script": ["..."]
  },
  "armor_command_adaptations": {
    "use_directly": ["..."],
    "adapt_carefully": ["..."],
    "do_not_import": ["..."]
  },
  "decision_gate": {
    "playtest_questions": ["..."],
    "kill_the_direction_if": ["..."],
    "greenlight_more_content_if": ["..."]
  }
}

Constraints:
- Provide exactly 3 candidate_skeletons.
- At least one candidate must be a real pivot, not just current + upgrades.
- Avoid vague advice like "add more juice" unless tied to a testable mechanic.
- Keep suggestions implementable in the current HTML5 canvas project with existing assets.
- Treat Codex as the integrator; do not write code.
