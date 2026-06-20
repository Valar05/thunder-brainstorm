# Claude Prompt: Infinite Brutality Hanging Gardens Nook Story Pilot II

Return one JSON object only. No prose wrapper. No markdown fences.

## Output Schema

```json
{
  "packet_updates": [
    {
      "id": "hg2_np_01_bell_tongue_reliquary",
      "replacement_text_fragments": ["...", "..."],
      "voice_note": "..."
    }
  ]
}
```

## Hard Rules

- Cover all 12 packet IDs exactly once.
- Keep `replacement_text_fragments` to 2 to 4 items.
- Keep most fragments under 16 words.
- Do not invent new packet IDs.
- Do not rename packet IDs.
- Do not rewrite packet structure.
- Do not add visible living people.
- Do not add named heroes.
- Do not write omniscient lore.
- Do not use modern phrasing.
- Do not use codex-entry voice.
- Keep the writing practical, local, pressured, and speaker-bound.
- Reuse the existing motifs and hidden run-story state.
- Fragments should feel like rules, tallies, vows, warnings, memorials, child copy lines, or work notes.
- `voice_note` must be one sentence only.

## Quality Bar

The text should read like environmental residue left by real custodians, clerks, mourners, caretakers, children, and workers after the warning system failed.

Prefer compression over flourish.
Prefer implication over explanation.
Prefer witness, rule, and burden language over grand mythology.
