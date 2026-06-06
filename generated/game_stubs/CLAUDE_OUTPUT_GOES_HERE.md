# Claude Candidate Drop Zone

Paste Claude's JSON candidate here, then ask Codex to integrate it.

Expected source prompt:

- `thunder-brainstorm/generated/source_packets/claude_maze_chase_roguelike_prompt.md`

Codex integration checklist after Claude returns:

1. Save candidate as `generated/game_stubs/scrap_cathedral_maze_chase_claude_candidate.json`.
2. Compare against `generated/game_stubs/scrap_cathedral_maze_chase.json`.
3. Preserve only generalized mechanics; reject any direct Pac-Man names/assets/trade dress.
4. Fold useful mechanics into `data/pattern_cards.json` only if they are reusable beyond this one stub.
5. If moving toward implementation, create a schema for floors, pursuers, upgrades, modifiers, and run state.
