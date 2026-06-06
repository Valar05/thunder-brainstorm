# Claude Handoff Prompt: Arcade Maze-Chase Roguelike Stub

You are drafting a game-design candidate from a narrow source packet. Do not write code. Do not use copyrighted arcade names, sprites, maze layouts, sounds, character names, or trade dress. Preserve only abstract mechanics: maze chase, required collectibles, distinct pursuers, temporary reversal pickups, bonus route temptation, escalating pressure.

## Source Packet

Read and use this packet:

```text
SOURCE_PACKET_PATH: thunder-brainstorm/generated/source_packets/maze_chase_roguelike_pacman_stub.md
```

The packet's preferred theme is **Scrap Cathedral**.

## Task

Draft a structured design candidate for a roguelike arcade maze-chase game. The design should feel like a new game, not a reskin. Focus on playable logic and prototypeable systems.

## Required Output Format

Return a single JSON object with these top-level keys:

```json
{
  "candidate_id": "scrap_cathedral_maze_chase_v1",
  "theme_pitch": {},
  "core_loop": [],
  "movement_model": {},
  "maze_generation": {},
  "pursuers": [],
  "floor_modifiers": [],
  "player_upgrades": [],
  "scoring_and_pressure": {},
  "first_playable_scope": {},
  "debug_and_validation": [],
  "risks": [],
  "implementation_recommendation": {}
}
```

## Hard Constraints

- No Pac-Man names, ghost names, visual trade dress, fruit identities, sound references, or exact maze references.
- Keep four stable pursuer personalities, each with readable behavior.
- Player upgrades must alter route decisions, not merely score or speed.
- Maze generation must be deterministic from a seed.
- Every required collectible must be reachable.
- Temporary reversal must remain powerful but brief and legible.
- Include a debug overlay recommendation showing pursuer mode and target tile.
- Keep the first playable scope small enough for a Godot or browser prototype.

## Design Bias

Prefer simultaneous tick/grid movement over pure turn-based movement unless you make a strong argument otherwise. Keep the arcade pressure, but make logic inspectable for roguelike generation.

## Specific Questions To Answer

1. What makes each floor tactically different?
2. How do pursuer mutations stay readable?
3. How does greed create risk without forcing it?
4. What is the smallest viable prototype?
5. What validation checks catch unfair maze generation?
6. Which systems should be data-driven from JSON?

## Tone

Concrete, systems-forward, compact. Avoid lore-heavy prose. Use theme only where it clarifies mechanics.

## Length Bound

Keep the whole JSON object under 2500 output tokens. Use compact arrays: no more than 4 pursuers, 5 floor modifiers, 6 upgrades, 6 validation checks, and 5 risks. Each string should be one short sentence unless a field clearly needs a structured object.
