# Thunder Brainstorm Mechanics Index

- Records: 724920
- Origins: local=724920

## Mechanics

### asset_import_pipeline (500226)
- local AGENTS.md [AGENTS.md:19]: 7. Treat generated audio, imported assets, `.uid` files, and archives as project-owned artifacts. Do not clean or regenerate them unless the task calls for it.
- local AGENTS.md [AGENTS.md:27]: - `Diorama Descent/`: Godot prototype with strong agent docs under `docs/agent/`, movement/combat docs, import tools, and debug smoke scripts.
- local AGENTS.md [AGENTS.md:34]: - `phalanx/`: Godot pose/animation lab with imported clip generation, skeleton profiles, and handoff docs.
- local AGENTS.md [AGENTS.md:37]: - `but-multiple-choice/`: Story/branching design workspace with generation, critique, source, schema, and TTS docs.
- local AGENTS.md [AGENTS.md:50]: - Trigger: editing Godot scripts, scenes, imports, autoloads, project settings, combat, movement, UI, or data-driven runtime behavior.

### pose_animation_tools (434441)
- local AGENTS.md [AGENTS.md:28]: - `gothic-throne/`: Godot prototype with Diorama-like docs and `AGENTS.md`.
- local AGENTS.md [AGENTS.md:29]: - `fleshpunk--inner-heart/`: Godot 4.5 mobile/text roguelike with scenario, corpus, mechanics, TTS, smoke, and bootstrap tooling.
- local AGENTS.md [AGENTS.md:30]: - `nightmare-voyage/`: Godot text roguelike fork/variant with similar scenario, corpus, mechanics, TTS, smoke, and bootstrap tooling.
- local AGENTS.md [AGENTS.md:31]: - `revelation/`: Godot text roguelike with Revelation-specific scenario, corpus, TTS, artifact, and pressure tooling.
- local AGENTS.md [AGENTS.md:34]: - `phalanx/`: Godot pose/animation lab with imported clip generation, skeleton profiles, and handoff docs.

### tts_audio_pipeline (388128)
- local AGENTS.md [AGENTS.md:19]: 7. Treat generated audio, imported assets, `.uid` files, and archives as project-owned artifacts. Do not clean or regenerate them unless the task calls for it.
- local AGENTS.md [AGENTS.md:29]: - `fleshpunk--inner-heart/`: Godot 4.5 mobile/text roguelike with scenario, corpus, mechanics, TTS, smoke, and bootstrap tooling.
- local AGENTS.md [AGENTS.md:30]: - `nightmare-voyage/`: Godot text roguelike fork/variant with similar scenario, corpus, mechanics, TTS, smoke, and bootstrap tooling.
- local AGENTS.md [AGENTS.md:31]: - `revelation/`: Godot text roguelike with Revelation-specific scenario, corpus, TTS, artifact, and pressure tooling.
- local AGENTS.md [AGENTS.md:32]: - `gravity-fist/`: Godot action/combat project with scripts, scenes, attacks, audio, and theme files; no root orientation doc found.

### ai_pressure (96724)
- local AGENTS.md [AGENTS.md:17]: 5. For Godot projects, inspect `project.godot` for `config/name` and `run/main_scene`.
- local AGENTS.md [AGENTS.md:35]: - `aegis-of-victory/`: HTML/JS narrative roguelike prototype with domain/event-cloud docs, Claude packet workflow, and local servers.
- local AGENTS.md [AGENTS.md:47]: - Procedure: identify target project, read local orientation/agent docs, inspect Godot main scene or web entrypoint, find validation commands, note archive/generated boundaries.
- local AGENTS.md [AGENTS.md:51]: - Procedure: read `project.godot`, inspect main scene and attached scripts, make scoped edits, run headless smoke tests when available, avoid unrelated sidecar churn.
- local AGENTS.md [AGENTS.md:55]: - Procedure: discover `tools/*smoke.gd`, run the relevant `godot --headless --path PROJECT --script SCRIPT` commands, summarize pass/fail and missing Godot binary issues.

### text_console_runtime (84515)
- local AGENTS.md [AGENTS.md:37]: - `but-multiple-choice/`: Story/branching design workspace with generation, critique, source, schema, and TTS docs.
- local AGENTS.md [AGENTS.md:47]: - Procedure: identify target project, read local orientation/agent docs, inspect Godot main scene or web entrypoint, find validation commands, note archive/generated boundaries.
- local AGENTS.md [AGENTS.md:55]: - Procedure: discover `tools/*smoke.gd`, run the relevant `godot --headless --path PROJECT --script SCRIPT` commands, summarize pass/fail and missing Godot binary issues.
- local AGENTS.md [AGENTS.md:58]: - Trigger: adding or revising player-facing rooms, events, endings, follow-ups, choices, or results in Fleshpunk/Nightmare/Revelation-style projects.
- local AGENTS.md [AGENTS.md:59]: - Procedure: use source packets and external writing-agent drafts for prose, integrate accepted patches, validate schemas/actions/payoffs, run room/follow-up smoke tests.

### web_choice_player (55217)
- local AGENTS.md [AGENTS.md:7]: Before doing anything else in this workspace, load the active project's `PROJECT_ORIENTATION.md` and the workspace Motivated Mode contract if present. Treat `docs/MOTIVATED_MODE...
- local AGENTS.md [AGENTS.md:18]: 6. Check for project-specific `tools/project_bootstrap.py`, smoke tests, local web servers, or validation agents before changing runtime/data behavior.
- local AGENTS.md [AGENTS.md:23]: When moving, copying, exporting, or resizing files for external use in Android-visible folders such as `/storage/emulated/0/Pictures`, `/storage/emulated/0/Download`, or `/stora...
- local AGENTS.md [AGENTS.md:35]: - `aegis-of-victory/`: HTML/JS narrative roguelike prototype with domain/event-cloud docs, Claude packet workflow, and local servers.
- local AGENTS.md [AGENTS.md:36]: - `omnitread/`: HTML/JS mission-deck adaptation workspace with story engine, corpus, quality audit, and Claude/local agent tooling.

### touch_lane_combat (41660)
- local AGENTS.md [AGENTS.md:32]: - `gravity-fist/`: Godot action/combat project with scripts, scenes, attacks, audio, and theme files; no root orientation doc found.
- local fleshpunk--inner-heart [fleshpunk--inner-heart/Enemy.gd:14]: @onready var attack_sprite: Sprite2D = $AttackSprite
- local fleshpunk--inner-heart [fleshpunk--inner-heart/Enemy.gd:45]: attack_sprite.visible = false
- local fleshpunk--inner-heart [fleshpunk--inner-heart/Enemy.gd:55]: attack_sprite.visible = false
- local fleshpunk--inner-heart [fleshpunk--inner-heart/Enemy.gd:65]: attack_sprite.visible = false

### writing_corpus_review (32926)
- local AGENTS.md [AGENTS.md:23]: When moving, copying, exporting, or resizing files for external use in Android-visible folders such as `/storage/emulated/0/Pictures`, `/storage/emulated/0/Download`, or `/stora...
- local AGENTS.md [AGENTS.md:37]: - `but-multiple-choice/`: Story/branching design workspace with generation, critique, source, schema, and TTS docs.
- local AGENTS.md [AGENTS.md:38]: - `legion-writing-tool/`: Local-first Termux/Android writing tool with corpus analysis, draft preservation rules, web/session tooling, and installer bootstrap.
- local AGENTS.md [AGENTS.md:59]: - Procedure: use source packets and external writing-agent drafts for prose, integrate accepted patches, validate schemas/actions/payoffs, run room/follow-up smoke tests.
- local AGENTS.md [AGENTS.md:62]: - Trigger: asking Claude or another writing agent to draft scenario/domain/room content.

### source_packet_generation (31545)
- local AGENTS.md [AGENTS.md:29]: - `fleshpunk--inner-heart/`: Godot 4.5 mobile/text roguelike with scenario, corpus, mechanics, TTS, smoke, and bootstrap tooling.
- local AGENTS.md [AGENTS.md:30]: - `nightmare-voyage/`: Godot text roguelike fork/variant with similar scenario, corpus, mechanics, TTS, smoke, and bootstrap tooling.
- local AGENTS.md [AGENTS.md:31]: - `revelation/`: Godot text roguelike with Revelation-specific scenario, corpus, TTS, artifact, and pressure tooling.
- local AGENTS.md [AGENTS.md:35]: - `aegis-of-victory/`: HTML/JS narrative roguelike prototype with domain/event-cloud docs, Claude packet workflow, and local servers.
- local AGENTS.md [AGENTS.md:36]: - `omnitread/`: HTML/JS mission-deck adaptation workspace with story engine, corpus, quality audit, and Claude/local agent tooling.

### delayed_consequences (31292)
- local AGENTS.md [AGENTS.md:59]: - Procedure: use source packets and external writing-agent drafts for prose, integrate accepted patches, validate schemas/actions/payoffs, run room/follow-up smoke tests.
- local AGENTS.md [AGENTS.md:70]: - Trigger: Aegis/Omnitread-style run structures with sampled domains, event lines, reactions, cascades, delayed echoes, and stateful consequences.
- local AGENTS.md [AGENTS.md:71]: - Procedure: work from domain/run schemas, validate event seeds individually, preserve run memory and delayed consequence models.
- local AGENTS.md [AGENTS.md:77]: 9. **Agent Handoff And Session Memory**
- local AGENTS.md [AGENTS.md:144]: - Consolidate common event/room/deck/payoff/action fields used by Fleshpunk, Nightmare, Revelation, Aegis, Omnitread, and But Multiple Choice.

### validation_pipeline (14185)
- local AGENTS.md [AGENTS.md:1] `GodotProjects Workspace Bootstrap`: # GodotProjects Workspace Bootstrap
- local AGENTS.md [AGENTS.md:5] `Motivated Bootstrap`: ## Motivated Bootstrap
- local AGENTS.md [AGENTS.md:18]: 6. Check for project-specific `tools/project_bootstrap.py`, smoke tests, local web servers, or validation agents before changing runtime/data behavior.
- local AGENTS.md [AGENTS.md:27]: - `Diorama Descent/`: Godot prototype with strong agent docs under `docs/agent/`, movement/combat docs, import tools, and debug smoke scripts.
- local AGENTS.md [AGENTS.md:29]: - `fleshpunk--inner-heart/`: Godot 4.5 mobile/text roguelike with scenario, corpus, mechanics, TTS, smoke, and bootstrap tooling.

### vehicle_survival (9558)
- local fleshpunk--inner-heart [fleshpunk--inner-heart/events.json:152] `line_2`: "line_2": "Fighting can earn biomass. Slipping past avoids injury now and raises danger later.",
- local fleshpunk--inner-heart [fleshpunk--inner-heart/events.json:342] `line_2`: "line_2": "If I linger, this lane will set around me. I move before it hardens.",
- local fleshpunk--inner-heart [fleshpunk--inner-heart/events.json:484] `action`: "action": "slip_green_spores",
- local fleshpunk--inner-heart [fleshpunk--inner-heart/events.json:490]: "slip green spores"
- local fleshpunk--inner-heart [fleshpunk--inner-heart/events.json:525] `label`: "label": "Mute the lane",

### resource_upgrade_loop (8130)
- local AGENTS.md [AGENTS.md:169]: Make a concept a skill when it has a repeatable trigger, a fragile workflow, project-specific validation, or bundled scripts/resources that future agents should use. Keep it as ...
- local fleshpunk--inner-heart [fleshpunk--inner-heart/events.json:595] `line_2`: "line_2": "No resource opens here. I keep moving before the branch reacts to my pace.",
- local fleshpunk--inner-heart [fleshpunk--inner-heart/events.json:745] `line_2`: "line_2": "No resource opens here. I leave before the split reacts again.",
- local fleshpunk--inner-heart [fleshpunk--inner-heart/events.json:926] `line_2`: "line_2": "Bonding gives one symbiote and kills the rest. Fighting wakes the ward. Leaving keeps my gait mine.",
- local fleshpunk--inner-heart [fleshpunk--inner-heart/events.json:1230] `id`: "id": "healing_pool_offer",

### event_clouds (5898)
- local AGENTS.md [AGENTS.md:35]: - `aegis-of-victory/`: HTML/JS narrative roguelike prototype with domain/event-cloud docs, Claude packet workflow, and local servers.
- local AGENTS.md [AGENTS.md:62]: - Trigger: asking Claude or another writing agent to draft scenario/domain/room content.
- local AGENTS.md [AGENTS.md:70]: - Trigger: Aegis/Omnitread-style run structures with sampled domains, event lines, reactions, cascades, delayed echoes, and stateful consequences.
- local AGENTS.md [AGENTS.md:71]: - Procedure: work from domain/run schemas, validate event seeds individually, preserve run memory and delayed consequence models.
- local AGENTS.md [AGENTS.md:147]: - Centralize public-domain/source adaptation rules currently repeated across corpus workflows.

### deck_pressure (4265)
- local AGENTS.md [AGENTS.md:36]: - `omnitread/`: HTML/JS mission-deck adaptation workspace with story engine, corpus, quality audit, and Claude/local agent tooling.
- local AGENTS.md [AGENTS.md:144]: - Consolidate common event/room/deck/payoff/action fields used by Fleshpunk, Nightmare, Revelation, Aegis, Omnitread, and But Multiple Choice.
- local fleshpunk--inner-heart [fleshpunk--inner-heart/encounter_decks.json:1]: {
- local fleshpunk--inner-heart [fleshpunk--inner-heart/encounter_decks.json:2] `base_bpm`: "base_bpm": 20.0,
- local fleshpunk--inner-heart [fleshpunk--inner-heart/encounter_decks.json:3] `corruption_spike_threshold`: "corruption_spike_threshold": 3,
