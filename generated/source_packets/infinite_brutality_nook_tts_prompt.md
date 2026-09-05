# Claude Prompt: Infinite Brutality Nook TTS Lines

Return one JSON object only. No prose wrapper. No markdown fences.

## Output Schema

```json
{
  "packet_lines": [
    {
      "packet_id": "hg_np_01_cistern_sleep_ledge",
      "spoken_text": "..."
    }
  ]
}
```

## Rules

- Cover all packet IDs from both pilots exactly once.
- `spoken_text` must be exactly one sentence.
- Usually 8 to 18 words.
- No quotes.
- No dialogue formatting.
- No first person.
- No omniscient mythology.
- Do not invent packet IDs.
- Do not omit any packet IDs.
- These lines will be spoken aloud as proximity narration, so they should be clean and sayable.
- Prefer environmental truth over flourish.

## Quality Bar

Each line should make the nook feel more lived in by naming the pressure, ritual, loss, or survival habit encoded there.
