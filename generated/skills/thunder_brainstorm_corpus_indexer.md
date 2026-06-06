# thunder-brainstorm-corpus-indexer Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/thunder-brainstorm-corpus-indexer/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: thunder-brainstorm-corpus-indexer
description: Use when treating the user's local projects, GitHub repositories, or Cauldron laptop workspace as a corpus for game/mechanic extraction, updating Thunder Brainstorm indexes, searching mechanic_source_refs.jsonl, or preserving source references with file paths and line numbers.
---

# Thunder Brainstorm Corpus Indexer

Use this skill when the user asks to index projects as corpus, fold new sources into Thunder Brainstorm, search extracted mechanics, or update source observations.

## Core Paths

- Workspace root: `/storage/emulated/0/Documents/GodotProjects`
- Engine: `thunder-brainstorm/thunder_brainstorm.py`
- Combined index: `thunder-brainstorm/generated/index_combined/mechanic_source_refs.jsonl`
- Combined summary: `thunder-brainstorm/generated/index_combined/mechanic_index_summary.json`
- Code examples: `thunder-brainstorm/generated/index_combined/mechanic_code_source_examples.md`

## Workflow

1. Read `thunder-brainstorm/README.md` and the relevant generated summary before changing the index.
2. For local disk corpus, run:
   ```sh
   python thunder-brainstorm/thunder_brainstorm.py index-corpus --root . --out-dir thunder-brainstorm/generated/index_local
   ```
3. For targeted GitHub corpus, prefer repo-specific indexing:
   ```sh
   python thunder-brainstorm/thunder_brainstorm.py index-corpus --skip-local --include-gh --owner Valar05 --repo REPO --max-gh-files-per-repo 30 --out-dir thunder-brainstorm/generated/index_REPO
   ```
4. For Cauldron, use the `cauldron-remote-workspace-inspector` skill first, then merge `index_cauldron` into `index_combined`.
5. When answering extraction questions, cite source records by origin, project/repo, path, line, symbol, and evidence.

## Search

Use `search-index` for quick evidence:

```sh
python thunder-brainstorm/thunder_brainstorm.py search-index "query" --mechanic touch_lane_combat --index thunder-brainstorm/generated/index_combined/mechanic_source_refs.jsonl
```

## Guardrails

- Do not copy repo bodies into pattern cards. Keep source code as references, not pasted content.
- Include exact references for mechanic claims.
- Keep generated-content indexing optional with `--include-generated`; default indexes should focus on code, docs, schemas, and project metadata.

## Marrow Runner Release Records

Marrow Runner and Club Crucible release-session records are preserved in Thunder Brainstorm:

```text
generated/session_learnings/2026-06-05_marrow_runner_release_handoff.md
generated/project_links/marrow_runner_project_links.md
generated/project_links/marrow_runner_project_links.json
generated/source_refs_manual/marrow_runner_release_source_refs.jsonl
```

When updating combined corpus references, include these manual records or cite them directly when the normal index skips generated/release folders.

Marrow Runner standalone project:

```text
/storage/emulated/0/Documents/GodotProjects/marrow-runner
```

