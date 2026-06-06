# Club Crucible Marrow Runner Announcement Source Packet

## Goal

Draft a Club Crucible blog post announcing Marrow Runner and describing the workflow behind it.

## Target Site

- Site: Club Crucible
- Live URL: https://clubcrucible.web.app
- Repository: Valar05/club-crucible
- Framework: Nuxt Content / Markdown posts
- Target section: `content/valarsbeard-development/`
- Frontmatter shape:

```yaml
---
title: "Post Title"
description: "Short description"
date: 2026-06-04
author: Club Crucible
---
```

## Marrow Runner Facts

- Title: Marrow Runner
- Itch URL: https://grailawakeninggames.itch.io/marrow-runner
- Current release candidate: v0.9.0-rc3
- Format: browser-playable HTML/canvas game, mobile-first but playable on desktop.
- Genre: immune-cell maze chase with seeded roguelike runs.
- Player fantasy: guide a phagocyte through living tissue, collect antibodies, cleanse infection, and escape through a lymph gate.
- Signature move: Pseudopod Ram. Release input to rearm, then move from rest to burst forward. Rammed germs become projectiles; wall and enemy impacts can trigger knockback chain reactions.
- Other systems: complement power pickup, antibody suction, infection nest, four ghost-style germ archetypes, tutorial, generated tissue art, music, SFX, localStorage seed replay, fullscreen/mobile controls.
- Status: close to v1.0, release candidate / public testing stage. Mutations are planned for a later version rather than this announcement.

## Workflow Facts

- The project was built with an AI-first solo-development workflow, but do not imply the AI made all decisions or replaced craft.
- Codex worked as a dedicated coding/scribe agent inside the workspace.
- Claude is used for bounded writing packets and draft generation, not as an unchecked integrator.
- Generated art and music were used where appropriate; runtime assets track provenance in manifests.
- Sound effects were locally synthesized and wired into the game.
- The development environment is unusually mobile:
  - Android phone
  - Termux shell
  - local HTML/canvas game server
  - git/LFS
  - butler upload tooling for itch
  - Firebase/Nuxt deployment from the connected Windows PC when needed
- Marrow Runner was split out of Thunder Brainstorm into its own standalone sibling repo with Git and Git LFS.

## Tone

Use the Club Crucible / Valarsbeard development voice:

- First person.
- Direct, reflective, and a little dramatic.
- Technical enough to be credible.
- Not corporate.
- No hype-copy cliches.
- Mention the strange joy of building a browser game from a phone through Termux.
- The post can credit Codex/Claude as tools, but the authorial voice should remain Club Crucible.

## Constraints

- Do not invent dates, platforms, enemies, features, pricing, or public reception.
- Do not mention private keys, API keys, secret paths, or operational credentials.
- Do not say v1.0 is shipped.
- Do not overstate AI ownership. Frame it as an AI-assisted solo workflow with human direction.
- Keep the post markdown ready for Nuxt Content.
