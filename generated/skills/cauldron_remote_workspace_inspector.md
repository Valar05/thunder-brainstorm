# cauldron-remote-workspace-inspector Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/cauldron-remote-workspace-inspector/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: cauldron-remote-workspace-inspector
description: Use when connecting to the user's Windows laptop THECAULDRON over SSH as dclar, cataloging C:\\Users\\dclar\\workspace, indexing Cauldron project source references, inspecting Phoenix-Simulator or other laptop-only projects, or merging Cauldron records into Thunder Brainstorm.
---

# Cauldron Remote Workspace Inspector

Use this skill for remote work on `THECAULDRON`.

## Connection

Host/IP observed:

```sh
ssh dclar@192.168.40.213
```

Credential is expected from `DCLAR_CREDS` in `~/.bashrc`. Do not print it.

Use the existing askpass helper if present:

```sh
env SSH_ASKPASS=/data/data/com.termux/files/usr/tmp/dclar_askpass.sh SSH_ASKPASS_REQUIRE=force DISPLAY=:0 ssh dclar@192.168.40.213 'cmd /c echo CONNECTED && whoami && cd'
```

## Catalog Artifacts

- `thunder-brainstorm/generated/cauldron_workspace_catalog.json`
- `thunder-brainstorm/generated/cauldron_workspace_catalog.md`
- `thunder-brainstorm/generated/index_cauldron/mechanic_source_refs.jsonl`

## Workflow

1. Verify SSH connection.
2. Catalog `C:\Users\dclar\workspace` with project markers.
3. For source indexing, upload/run the Cauldron scanner script from `thunder-brainstorm/generated/cauldron_index_workspace.ps1`.
4. Classify results with Thunder Brainstorm's mechanic rules.
5. Merge `index_cauldron` into `index_combined`.

## Guardrails

- Do not clone all laptop repos locally unless explicitly requested.
- Keep remote source URLs as `ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/...#L...`.
- Treat `Phoenix-Simulator` as laptop-local/non-git unless later evidence changes.

## ClubCrucible Firebase / Nuxt Notes

Observed ClubCrucible workspace:

```text
C:\Users\dclar\workspace\ClubCrucible
git@github.com:Valar05/club-crucible.git
https://clubcrucible.web.app
```

Useful remote commands:

```sh
env SSH_ASKPASS=/data/data/com.termux/files/usr/tmp/dclar_askpass.sh SSH_ASKPASS_REQUIRE=force DISPLAY=:0 ssh dclar@192.168.40.213 "powershell -NoProfile -Command "Set-Location 'C:\Users\dclar\workspace\ClubCrucible'; npm run generate""

env SSH_ASKPASS=/data/data/com.termux/files/usr/tmp/dclar_askpass.sh SSH_ASKPASS_REQUIRE=force DISPLAY=:0 ssh dclar@192.168.40.213 "powershell -NoProfile -Command "Set-Location 'C:\Users\dclar\workspace\ClubCrucible'; firebase deploy --only hosting --project clubcrucible""
```

Hosting facts:

- Firebase project: `clubcrucible`
- Hosting site: `clubcrucible`
- Live channel URL: `https://clubcrucible.web.app`
- Local Termux may not have `gcloud`; THECAULDRON has Cloud SDK and Firebase CLI.

Guardrail: the ClubCrucible worktree may contain unrelated dirty files. Stage only intended paths when committing, usually explicit content files.

