# scenario-source-packet-builder Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/scenario-source-packet-builder/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: scenario-source-packet-builder
description: Use when preparing narrow source packets for Claude/OpenAI/another writing agent to draft rooms, events, domains, scenario patches, dialogue, endings, or corpus-grounded game content without handing over an entire repo.
---

# Scenario Source Packet Builder

Use this skill before asking a writing agent to draft content.

## Packet Contents

Include only:

- target project and content track
- fixed IDs and schema expectations
- current room/event/domain/scenario seed
- relevant source/corpus influences
- for environmental or nook writing: former use, survival use, speaker class, dominant verb, taboo/rule, and hidden run-story axes
- voice/style constraints
- forbidden drift
- output JSON shape
- validation commands

## Workflow

1. Read the project orientation and relevant source-packet workflow docs.
2. Build a packet under `generated/source_packets/` or equivalent.
3. Keep the packet narrow, normally around a 7k input-token budget unless the user sets another budget.
4. Ask the writing agent for structured output, not repo changes.
5. Integrate with `validation-first-content-integrator`.

## Guardrails

- Codex integrates and validates; writing agents draft player-facing prose.
- Do not include broad repo dumps.
- Do not let generated text invent action IDs unless engine work is planned.
