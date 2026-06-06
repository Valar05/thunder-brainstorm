# club-crucible-firebase-publisher Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/club-crucible-firebase-publisher/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: club-crucible-firebase-publisher
description: "Use when publishing or updating Club Crucible content through the connected Windows PC THECAULDRON, especially Nuxt Content Markdown posts, Firebase Hosting deploys, gcloud/Firebase URL checks, and GitHub commits for Valar05/club-crucible."
---

# Club Crucible Firebase Publisher

Use this for Club Crucible site updates.

## Known Project

```text
Remote workspace: C:\Users\dclar\workspace\ClubCrucible
SSH: dclar@192.168.40.213
Repo: git@github.com:Valar05/club-crucible.git
Firebase project: clubcrucible
Hosting site: clubcrucible
Live URL: https://clubcrucible.web.app
```

## Workflow

1. Connect through the existing Cauldron SSH askpass helper. Do not print credentials.
2. Inspect `git status -sb` before editing; the worktree may contain unrelated dirty files.
3. Add or update content under the correct Nuxt Content folder, commonly `content/valarsbeard-development/`.
4. Run:
   ```powershell
   npm run generate
   ```
5. Deploy:
   ```powershell
   firebase deploy --only hosting --project clubcrucible
   ```
6. Verify the live URL with `Invoke-WebRequest` and check for expected title/link text.
7. If committing, stage only intended paths explicitly and push `main` unless the user asks for a branch/PR.

## Guardrails

- Do not stage unrelated dirty files.
- If Claude drafted the post, validate/correct factual claims before publishing.
- Do not enable missing GCP APIs casually; Firebase Hosting is the observed host, not Cloud Run or App Engine.

