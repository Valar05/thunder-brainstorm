# Thunder Brainstorm

Thunder Brainstorm is a local game-idea engine built from generalized patterns observed across this workspace and GitHub repository metadata. It is intentionally not a repo copier: it stores pattern cards, source observations, and generated pitches, not source code from inspected projects.

## Armor Command / Page Assets

Newest prototype release/page materials are mirrored as actual Thunder docs first, with link records and lessons below them:

- `generated/page_assets/armor_command_page_copy.md`: actual Armor Command itch/page copy.
- `generated/page_assets/armor_command_icon_512.png`: actual 512px Armor Command icon.
- `generated/page_assets/armor_command_icon_1024.png`: actual 1024px Armor Command icon.
- `generated/page_assets/armor_command_page_assets_manifest.json`: Thunder mirror manifest for the page copy and icon files.
- `generated/release_packets/armor_command_itch/DEVLOG_v1.0.0.md`: Armor Command v1.0 devlog copy in the Marrow Runner scribe style.
- `generated/release_packets/armor_command_itch/TWITTER_v1.0.0.md`: Armor Command v1.0 Twitter/X post copy with a 280-character primary version.
- `generated/project_links/armor_command_project_links.md`: Armor Command copy, icon paths, release asset links, and current pitch.
- `generated/project_links/armor_command_project_links.json`: machine-readable paths for page copy and icon assets.
- `generated/session_learnings/2026-06-05_armor_command_prototype_lessons.md`: prototype lessons from the Armor Command pivot, input tuning, sprite atlas, generated assets, WebAudio SFX, drop-pod enemy branch, kill-chain scoring, and release workflow.
- `generated/skills/armor_command_html5_release_operator.md`: Thunder-visible workflow skill note for Armor Command-style HTML5/canvas release operations.
- `generated/source_refs_manual/armor_command_prototype_source_refs.jsonl`: manual source-reference records for Armor Command artifacts.
- Local play URL: `http://127.0.0.1:8791/`
- Thunder docs URL: `http://127.0.0.1:8765/`
- Published itch page: `https://valarsbeard.itch.io/armor-command`

## Quick Start

```sh
python thunder_brainstorm.py list
python thunder_brainstorm.py generate --count 5 --seed 17
python thunder_brainstorm.py generate --focus "mobile action" --count 3
python thunder_brainstorm.py inspect-local --root .. --out generated/local_scan.json
python thunder_brainstorm.py inspect-gh --owner Valar05 --out generated/gh_scan.json
python thunder_brainstorm.py mine-gh-repo --owner Valar05 --repo motion-dungeon --out-dir generated/repo_mining
python thunder_brainstorm.py mine-gh-owner --owner Valar05 --out-dir generated/repo_mining --max-files 24
python thunder_brainstorm.py critical-manifest --summary generated/repo_mining/Valar05_overnight_summary.json --out-dir generated/critical_thunder_manifest
python thunder_brainstorm.py compose-motion-dungeon
python thunder_brainstorm.py export-motion-dungeon-targets
python thunder_brainstorm.py index-corpus --root .. --out-dir generated/index
python thunder_brainstorm.py index-corpus --root .. --include-gh --owner Valar05 --gh-limit 20 --out-dir generated/index_full
python thunder_brainstorm.py index-corpus --skip-local --include-gh --owner Valar05 --gh-limit 10 --max-gh-files-per-repo 25 --out-dir generated/index_github
python thunder_brainstorm.py index-corpus --skip-local --include-gh --owner Valar05 --repo long-haul --max-gh-files-per-repo 30 --out-dir generated/index_long_haul
python thunder_brainstorm.py index-corpus --root .. --include-generated --out-dir generated/index_with_generated
python thunder_brainstorm.py search-index "rearm gap" --index generated/index_github/mechanic_source_refs.jsonl
python thunder_brainstorm.py search-index --mechanic touch_lane_combat --project gravity-fist --index generated/index/mechanic_source_refs.jsonl
python thunder_brainstorm.py search-index "phoenix" --project Phoenix-Simulator --index generated/index_combined/mechanic_source_refs.jsonl
```

## Thunder-First JIT Source Transactions

`tools/thunder_source_transaction.py` is the offline transaction half of Thunder-first engineering. `gap` reuses the existing combined-index search and emits `NEEDS_THUNDER_SOURCE` only after owner evidence and a sealed local `NO_REUSABLE_SOURCE`. GitHub lookup remains an external read-only intake ordered as Valar05 first, then bounded authoritative public repositories. `publish` accepts only a provenance-complete packet matching that gap, validates in an isolated worktree, creates exactly one local commit, and fast-forwards a still-clean canonical checkout. It never pushes or accesses the network.

```sh
python tools/thunder_source_transaction.py gap --repo . --query "missing capability" --capability capability-id --project project-id --owner-evidence path/to/owner.py:42 --out /absolute/temp/gap.json
python tools/thunder_source_transaction.py publish --repo . --gap /absolute/temp/gap.json --packet /absolute/temp/packet.json --recovery-dir /absolute/temp/recovery
python tools/thunder_source_transaction.py recover-lock --repo .
python tools/test_thunder_source_transaction.py
```

Canonical Thunder must be clean at entry and exit. Live or ambiguous portable locks fail closed. Dead-lock recovery requires matching owner/journal state and unchanged clean HEAD. The add-to-commit dirty window defaults to 60 seconds; an overrun aborts before publication and preserves an external recovery receipt.

## Second-Pass Coverage

The second pass digs into newer/local projects by metadata, docs, schema keys, top-level trees, and identifier names. Added coverage includes:

- `long-haul`: highway vehicle survivorlike, cockpit HUD zones, pursuer rearm gaps, layered vehicle audio, CC asset sourcing.
- Current workspace projects: Godot text-choice stacks, event-cloud web prototypes, combat/action prototypes, Phalanx pose lab, SteamPile resource microloops, and Legion writing/corpus tooling.
- Phoenix search status: no `phoenix` repo, local file, or GitHub code-search hit was found under `Valar05` during this pass.

## What It Generalizes

- Pressure arenas, event clouds, delayed consequences, and deck-driven pacing.
- Source-packet and corpus-to-mechanic workflows.
- Godot mobile combat, touch lanes, handoff-to-duel presentation, and survivorlike offer loops.
- Text-console choice runtimes, local review surfaces, and web choice players.
- Validation-first content pipelines, TTS manifests, and nondestructive writing labs.

## Output Shape

Generated pitches include:

- core fantasy
- pattern stack
- player loop
- signature systems
- content pipeline
- validation plan
- risks to prototype early

## Corpus Index

`index-corpus` treats local projects and optional GitHub repositories as a mechanics corpus. It does not clone repositories. It writes:

- `mechanic_source_refs.jsonl`: one source-reference record per indexed evidence point.
- `mechanic_index_summary.json`: counts by mechanic, project, origin, and representative examples.
- `mechanic_index_report.md`: readable mechanic headings with source examples.

Each source record includes the origin, project/repo, path, line number, symbol/key/heading when detected, mechanic tags, and a compact evidence line. This is the audit trail for extracted mechanics.

Generated folders are skipped by default to keep the index focused on code, docs, schemas, and project metadata. Use `--include-generated` when you want generated content patches and drafts indexed too.

Cauldron laptop workspace records use origin `cauldron` and `ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/...#L...` source URLs. The generated catalog lives in `generated/cauldron_workspace_catalog.*`, and indexed Cauldron records live in `generated/index_cauldron/`.

## Boundary

The included pattern cards are derived from structural observations: file names, docs categories, function/key names, repo descriptions, and repeated workflows. Do not paste repository code into pattern cards. If the extractor scans code, keep only abstract signals such as identifier names, file categories, schema keys, and concept tags.

## Claude PR Code Review

Thunder owns the Claude-backed PR review runner for independent code critique. The runner gives Claude read-only GitHub tools instead of source packets; if the repo or PR cannot be read, the run fails rather than synthesizing a review from pasted context. Dry-run is the default, and inline GitHub review comments are posted only with `--post` after mechanical verification maps findings to changed diff lines.

```sh
python tools/claude_code_review.py --pr Valar05/example#123
python tools/claude_code_review.py --pr Valar05/example#123 --post
python tools/capture_pr_review_fixture.py --pr Valar05/example#123 --out generated/code_reviews/fixtures/example_pr_123
```

Artifacts are written under `generated/code_reviews/` with the mission, tool transcript, read log, Claude JSON, verified findings, GitHub payload, and Markdown report. Use `tools/capture_pr_review_fixture.py` to capture a real PR once for offline `--mock-github` review-driver tests.

## Doc Server

Run a local document browser for generated stubs, source packets, corpus reports, and index files:

```sh
python tools/doc_server.py --host 127.0.0.1 --port 8765
```

Open `http://127.0.0.1:8765/`. JSON files render as structured documents, Markdown/text files render as readable pages, and large JSONL indexes include a search preview instead of dumping the whole file.

## Armor Command / Prototype Learnings

Armor Command learnings from the missile-command survivorlike prototype are preserved for future brainstorming passes:

- `generated/session_learnings/2026-06-05_armor_command_prototype_lessons.md`: vehicle pivot, touch/missile input tuning, per-rack cooldowns, generated sprite-sheet atlas pitfalls, ground/sky composition, local personal best, and page asset workflow.
- `generated/project_links/armor_command_project_links.md`: durable links for copy, icons, release assets, local play URL, and project paths.
- `generated/source_refs_manual/armor_command_prototype_source_refs.jsonl`: manual source-reference records for artifacts that normal corpus indexing may skip.
- `generated/release_packets/armor_command_itch/DEVLOG_v1.0.0.md`: Armor Command v1.0 devlog copy, written as a Thunder release packet in the Marrow Runner scribe style.

## Marrow Runner / Release Learnings

Recent release-session knowledge is preserved for future agents and brainstorming passes:

- `generated/session_learnings/2026-06-05_marrow_runner_release_handoff.md`: standalone repo, itch, Club Crucible, Android/Termux, input-feel, and asset lessons.
- `generated/session_learnings/2026-06-06_marrow_runner_upgrade_leakfix_rc4.md`: upgrade branch/capstone/synergy implementation, New Run choppiness lifecycle fix, rc4 itch target, and validation lessons.
- `generated/project_links/marrow_runner_project_links.md`: durable links for Marrow Runner, Club Crucible, itch, Firebase, and Thunder packets.
- `generated/source_refs_manual/marrow_runner_release_source_refs.jsonl`: manual source-reference records for release artifacts that normal corpus indexing may skip.
- `generated/skills/`: doc-viewer mirrors of installed workflow skills, including Android file refresh, Club Crucible publishing, Marrow Runner release ops, generated image asset pipeline, Claude packet running, and itch butler deployment.

New generalized pattern cards from this pass include `mobile_canvas_release_workbench`, `recursive_knockback_dash_core`, `bounded_ai_release_scribe`, and `generated_asset_provenance_loop`.

## Immune Maze Canvas Prototype

A first playable HTML canvas prototype lives in `prototypes/immune-maze-canvas/`. Run it with:

```sh
cd prototypes/immune-maze-canvas
python -m http.server 8787
```

Open `http://127.0.0.1:8787/`.

## Gravity Fist Meshy Asset Workflow

Generated-asset workflow notes for Gravity Fist and the Three.js port are preserved in:

- `generated/session_learnings/2026-06-06_gravity_fist_meshy_asset_workflow.md`
- `generated/session_learnings/2026-06-06_gravity_fist_video_regression_suite.md`
- `generated/session_learnings/2026-06-07_gravity_fist_godot_animation_contract.md`
- `generated/session_learnings/2026-06-07_gravity_fist_threejs_dash_pushback_parity.md`
- `generated/project_links/gravity_fist_project_links.md`
- `generated/skills/threejs_phone_game_port_agent.md`

The workspace CLI is `../tools/meshy_asset_workflow.py`. Use it to generate or track DALL-E/OpenAI concept images, Meshy image-to-3D tasks, Meshy rigging tasks, downloads, and per-asset provenance manifests.


## Armor Command 1.0 Corpus Additions

Armor Command 1.0 added generalized pattern cards and source refs for:

- `tap_hold_missile_command_survivorlike`
- `branching_airborne_enemy_family`
- `visible_kill_chain_multiplier`
- `web_audio_buffer_sfx_bus`
- `generated_canvas_background_and_sprite_sheet_loop`
- `itch_html_cachebusted_release`
- `additive_trait_mutation_stack`

The manual source refs live in `generated/source_refs_manual/armor_command_prototype_source_refs.jsonl`, and the Thunder-visible workflow skill note lives in `generated/skills/armor_command_html5_release_operator.md`.

## Last Convoy / HTML5 Port Learnings

Last Convoy source-parity and canvas-port learnings are preserved for future vehicle/snake-convoy prototypes:

- `generated/session_learnings/2026-06-07_last_convoy_html5_port_lessons.md`: source-parity canvas port lessons, textured fragmentation, offscreen WebGL fire shader bridge, cache busting, and root-cannon visual correction.
- `generated/project_links/last_convoy_project_links.md`: durable links for the Cauldron source project, local HTML5 port, cache-busted play URL, and Thunder records.
- `generated/source_refs_manual/last_convoy_html5_source_refs.jsonl`: manual source-reference records for Last Convoy source, canvas runtime, shader bridge, sprite fragmentation, and asset provenance.
- Local play URL: `http://127.0.0.1:8796/?v=20260607-shader-shatter-2`

New generalized pattern cards from this pass include `snake_convoy_upgrade_chain`, `source_parity_canvas_port`, `canvas_webgl_shader_bridge`, `textured_fragmentation_port`, and `android_cachebusted_canvas_iteration`.

## FPS Platformer / Arcane IK Brainstorm

A new first-person action platformer direction is captured in:

- `generated/session_learnings/2026-06-07_fps_platformer_arcane_ik_brainstorm.md`: phone-landscape Three.js platformer concept using FPSPlayer arm animations and Arcane Manifold-inspired lower-body IK.
- `generated/project_links/fps_platformer_arcane_ik_project_links.md`: local copied Blender assets, Arcane Manifold source pointers, and Three.js reference project links.

The design target is a phone-first landscape Three.js runtime: arms sell weapon variety, while procedural foot planting, landing compression, slope contact, and body/camera yaw separation sell platforming feel.

## Infinite Brutality Prototype Learnings

Infinite Brutality runtime and design notes are preserved for future first-person melee/platformer passes:

- `generated/session_learnings/2026-06-08_infinite_brutality_prototype_lessons.md`: creative direction, room/level bible, movement goals, runtime build state, low-poly visual lessons, dungeon graph direction, and diegetic lighting plan.
- `generated/project_links/infinite_brutality_project_links.md`: local project paths, play URL, Thunder docs URL, and related notes.
- `generated/source_refs_manual/infinite_brutality_source_refs.jsonl`: manual source-reference records for runtime systems that normal indexing may skip or flatten.
- `generated/skills/level_design_environment_grammar.md`: general environment-first level-design workflow and critique-improvement loop.
- `../infinite-brutality/docs/LEVEL_DESIGN_WORKFLOW.md`: Infinite Brutality-specific companion workflow note.
- `../infinite-brutality/docs/VERTICAL_DISTRICT_REALIZATION_PLAN.md`: corrective implementation plan for moving Infinite Brutality from a flat graph with room garnish to a true 3D district spine.
- Local play URL: `http://127.0.0.1:8798/infinite-brutality/index.html`


## Quake Route Grammar Curriculum

Infinite Brutality now has a route-grammar extractor and bootstrap curriculum for Quake-style level generation without copying Quake layouts or data:

- `tools/quake_route_grammar.py`: sequential extractor for local `.map`, `.bsp`, Quake `.pak`, and `.pk3`/`.zip` sources.
- `generated/quake_route_grammar/quake_route_grammar_curriculum.md`: abstract route-template report.
- `generated/quake_route_grammar/quake_route_grammar_curriculum.json`: generator-facing curriculum data.
- `../infinite-brutality/LEVEL_GENERATION_CONTRACT.md`: project-local hard rules.
- `../infinite-brutality/data/level_route_templates.json`: current route templates.

Current curriculum is trained from the legal Quake map-source archive isolated under `generated/external_sources/quake_map_sources/`: 63 total sources, 41 playable maps trained, 22 item/prefab sources metadata-only. Infinite Brutality consumes only abstract route sentences and ML level-design lessons, not Quake geometry or assets.

## Fleshpunk Maze Progression Gallery

Thunder serves the content-addressed Fleshpunk visual archaeology at `http://127.0.0.1:8765/gallery/fleshpunk-maze`. It preserves six ordered stages, including rejected work, deterministic source selection, the current full-resolution pressure-valve champion, and its binary training projection. Rebuild the mirror with:

```sh
python tools/build_fleshpunk_gallery.py --source-root ../infinite-brutality
```

The durable server session is named `thunder-gallery`.
