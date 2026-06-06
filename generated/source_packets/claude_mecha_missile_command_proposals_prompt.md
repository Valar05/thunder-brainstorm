# Prompt

Using the source packet, draft three distinct but buildable proposals for the mecha missile-command prototype.

Return only strict JSON with this shape:

```json
{
  "proposals": [
    {
      "title": "",
      "one_sentence_pitch": "",
      "core_loop": [],
      "mobile_input_model": "",
      "mvp_weapon_set": {
        "shoulder_missiles": "",
        "one_handed_rifle": "",
        "four_drones": ""
      },
      "arm_tracking_solution": {
        "mvp": "",
        "polish_path": "",
        "image_gen_asset_requirements": []
      },
      "art_direction": "",
      "survivorlike_growth": [],
      "first_prototype_scope": [],
      "risks": [],
      "why_this_version": ""
    }
  ],
  "shared_recommendations": {
    "best_arm_tracking_approach": "",
    "best_mvp_input_rule": "",
    "first_image_generation_packet": [],
    "first_canvas_systems_to_build": []
  }
}
```

Requirements:

- Exactly three proposals.
- Keep each proposal concrete and feasible for one HTML5 canvas prototype.
- Make the mecha style sleek anime plus heroic chibi proportions.
- Each proposal should differ meaningfully in feel or structure, not just names.
- Arm tracking must be explained as runtime 2D transforms/IK using modular generated assets.
- Include practical image generation requirements for the modular sprite art.
- No invented external IP comparisons.
- No full production roadmap. Focus on MVP and first playable path.
