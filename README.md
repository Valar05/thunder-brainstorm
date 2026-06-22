# Thunder Brainstorm

Thunder Brainstorm is a local game-idea engine built from generalized patterns observed across this workspace and GitHub repository metadata. It is intentionally not a repo copier: it stores pattern cards, source observations, and generated pitches, not source code from inspected projects.

## Prospector / WWDD Behavioral Mining

Prospector artifacts mine the Thunder Brainstorm corpus for repeated operator judgment rather than project summaries:

- `generated/behavioral_mining/prospector_wwdd_thunder_brainstorm_2026-06-22.md`: evidence-backed behavioral distillation, WWDD candidates, Crucible scoring, gold promotions, and recommended doctrine.
- `generated/doctrine/wwdd_gold_rules_2026-06-22.md`: compact promoted WWDD rules for future agents.

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
python thunder_brainstorm.py index-corpus --root .. --out-dir generated/index
python thunder_brainstorm.py index-corpus --root .. --include-gh --owner Valar05 --gh-limit 20 --out-dir generated/index_full
python thunder_brainstorm.py index-corpus --skip-local --include-gh --owner Valar05 --gh-limit 10 --max-gh-files-per-repo 25 --out-dir generated/index_github
python thunder_brainstorm.py index-corpus --skip-local --include-gh --owner Valar05 --repo long-haul --max-gh-files-per-repo 30 --out-dir generated/index_long_haul
python thunder_brainstorm.py index-corpus --root .. --include-generated --out-dir generated/index_with_generated
python thunder_brainstorm.py search-index "rearm gap" --index generated/index_github/mechanic_source_refs.jsonl
python thunder_brainstorm.py search-index --mechanic touch_lane_combat --project gravity-fist --index generated/index/mechanic_source_refs.jsonl
python thunder_brainstorm.py search-index "phoenix" --project Phoenix-Simulator --index generated/index_combined/mechanic_source_refs.jsonl
```

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
