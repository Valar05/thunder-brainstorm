# Workspace Bootstrap Skill Stack

Thunder Brainstorm mirror of the cross-cutting Codex workflows that are worth treating as general workspace bootstrap skills. This note is intentionally separate from the installed skill set; it records what the workspace already verifies and why.

## Included Skills

### Thunder Brainstorm Corpus Indexer
Use when local projects, GitHub repos, or Cauldron workspaces need corpus indexing or mechanic extraction.

Workflow:
- Read `thunder-brainstorm/README.md` and the relevant generated summary first.
- Run `index-corpus` or `search-index` on the narrowest useful scope.
- Preserve source refs with origin, path, line, symbol, and evidence.
- When a pass produces durable rules, save them as Thunder session learnings plus manual source refs.

### Workspace Write Operator
Use when writing to shared storage, `.codex`, or any sandbox-sensitive path.

Workflow:
- Classify the target path before editing.
- Choose a writable strategy that matches the path class.
- Do not keep retrying `apply_patch` on rejected paths.
- Verify immediately with readback or validation.

### Visual QA Harness
Use when browser/game visuals look wrong, a build is stale, or tests pass but the screen still fails.

Workflow:
- Run fresh capture on the target page or project.
- Inspect the contact sheet and representative frames before diagnosing.
- Treat capture failures as harness failures, not as visual proof.
- Rerun capture after the fix.

### Android Live Visual Critique
Use when the user provides fresh screenshots, browser captures, or screen recordings.

Workflow:
- Inspect the newest evidence first.
- Judge visible pose, orientation, and readability over telemetry.
- Sample distinct states before concluding.
- Prefer the latest capture over older video context.

### Asset Provenance Hygiene
Use when adding, moving, generating, importing, archiving, or licensing assets.

Workflow:
- Preserve sidecars and manifests with the asset.
- Record source, license, generator/tool, and target use.
- Keep source libraries separate from project-owned runtime assets.
- Refresh Android file indexing for external files before reporting completion.

### Pose / Animation Import Lab
Use when imported GLB/Blend/FBX clip inventories, skeleton profiles, or retargeting need inspection.

Workflow:
- Inspect actual clip inventory and rig metadata before trusting labels.
- Compare imported timing to runtime combat needs.
- Preserve source manifests and handoff docs when import ownership changes.

### Three.js Pose Lab Import
Use when the Three.js pose-lab import pipeline needs normalization, rig overrides, or phone-first 3D combat mapping.

Workflow:
- Confirm the source project root.
- Read orientation docs and inspect asset inventory before copying behavior.
- Preserve stable rig values in project data.
- Validate the result with screenshots or pose strips when visible behavior matters.

### Android External File Refresh
Use when creating or moving files into Android-visible storage.

Workflow:
- Verify the final external files exist.
- Refresh media/file indexing before reporting completion.
- Prefer a scoped refresh for the touched files or parent folder.
