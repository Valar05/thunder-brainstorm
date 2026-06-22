# Prism League / Goblinball — Gasket Simulation Gold

Date: 2026-06-22
Source project: `Valar05/prism-league`
Primary source file: `docs/GASKET_CHARACTER_BIBLE.md`

## Promotion Summary

Prospector's Gasket work produced corpus-grade doctrine. The bark lines are content and should stay in Prism League. The reusable value is the design pattern underneath: Gasket is not merely a mascot or voice pack; he is a gameplay-coupled judgment engine.

## Gold 1: Mascot-as-Mechanic

A mascot is not decoration.

A mascot becomes a mechanic when its behavior, commentary, animation, and emotional state are mechanically derived from gameplay events.

If the mascot can be removed without changing gameplay perception, the mascot is not yet a mechanic.

### Why It Matters

This turns character feedback into part of the game loop instead of surface charm. Gasket's role as the ball makes every bark, squint, spin, complaint, and moment of respect part of play feedback.

### Transfer

Applies to:

- Goblinball / Prism League
- Working Dog
- Archanochoir
- Accessibility assistants
- Any narrator, companion, announcer, guide, or reactive mascot

## Gold 2: Commentary Is Telemetry

If the player needs feedback, prefer expressing it through character reaction instead of detached UI whenever readability permits.

### Pattern

Gameplay event -> Character judgment -> Useful feedback

Examples from Gasket:

- Centered hit -> reluctant respect
- Edge hit -> complaint plus readable feedback
- Long rally -> escalating panic and pride
- Miss -> taunt and quick reset

### Why It Matters

The player receives performance feedback without a tutorial panel. The game teaches through personality.

## Gold 3: Rival With A Microphone

Gasket is best modeled as a rival with a microphone.

This is stronger than mascot, narrator, or companion because it explains why he talks, judges, celebrates, panics, gets annoyed, notices improvement, and keeps the player wanting another round.

### Design Use

When writing or implementing Gasket, ask:

- What would a competitive rival notice here?
- What would a biased commentator exaggerate?
- What would make the player want to prove him wrong?

## Gold 4: Judgment Engine Wearing A Goblin Costume

Gasket is not a dialogue system.

Gasket is a judgment engine wearing a goblin costume.

### Architecture Implication

Do not start with static funny lines. Start with observations and opinions.

Gameplay state should produce:

1. Observations
2. Pattern detection
3. Opinion state
4. Commentary triggers
5. Bark selection or generation

## Promotion Doctrine

The bark lines are ore/content, not corpus doctrine. Keep them in the project. Promote the reusable system patterns.

## Cross-Link Terms

- Mascot-as-Mechanic
- Commentary Is Telemetry
- Rival With A Microphone
- Judgment Engine Wearing A Goblin Costume
- Simulation Artifact
- Gameplay-Coupled Commentary
- Character Feedback
- Pressure System
- Observation -> Judgment -> Feedback

## Crucible Result

Promote:

- Mascot-as-Mechanic
- Commentary Is Telemetry
- Rival With A Microphone
- Judgment Engine Wearing A Goblin Costume

Keep local to Prism League:

- Individual bark lines
- Specific Gasket content examples
- Project-specific animation priorities

## Acceptance Test

After ten minutes of play, the player should feel like Gasket has been watching them.

They should be able to say things like:

- Gasket thinks I rely too much on bank shots.
- Gasket hates my upgrade choices.
- Gasket actually respected that save.

When that happens, the ball has become a witness.
