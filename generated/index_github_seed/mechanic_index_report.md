# Thunder Brainstorm Mechanics Index

- Records: 3552
- Origins: github=3552

## Mechanics

### source_packet_generation (1638)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L7]: The source PDF is `Aegis of Victory (1).pdf`. A searchable text extraction lives at `generated/corpus/aegis_of_victory_source.txt`.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L43]: - `generated/rooms/dionysus_room_scaffolds.json`: generated room scaffolds for document review and Claude handoff.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L44]: - `docs/source_vibe_guide.md`: source-grounded vibe guide for generated rooms and packets.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L79] `Claude Architecture/Event Workflow`: ## Claude Architecture/Event Workflow
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L81]: Claude should be used for architecture and event generation the same way the Fleshpunk workflow used it: Codex builds narrow source packets, validates, and integrates; Claude dr...

### tts_audio_pipeline (620)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L105]: - `generated/corpus/`: source manifests, power seeds, artifact generator, and source extraction.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/canon_source_map.md#L21]: - Coins: intent/meaning interfaces tied to powers and disciplines. Theo's coin creates/contacts the Logos Fracture. A raider's Poseidon-aligned coin drives water/ice spear work....
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/canon_source_map.md#L55]: 14. Missing section: likely Bacchus manifestation and escalation.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/corpus_driven_room_generation.md#L20]: For required path variants, preserve the required outcome while changing the myth-backed circumstances. In Dionysus, seed acquisition must still produce `blood_sap_seed`; sprout...
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/corpus_driven_room_generation.md#L54]: Required artifact state changes must happen on the page. For Thorn Rod sprouting, Claude must describe where the seed is, how it cracks or roots, how the shaft and thorns form, ...

### validation_pipeline (472)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L81]: Claude should be used for architecture and event generation the same way the Fleshpunk workflow used it: Codex builds narrow source packets, validates, and integrates; Claude dr...
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L87]: python tools/aegis_domain_agent.py validate
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/README.md#L47]: Claude drafts architecture and event content from narrow source packets. Codex validates, integrates, and keeps local tooling working.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/README.md#L51]: python tools/aegis_domain_agent.py validate
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/claude_domain_workflow.md#L5]: Aegis uses Claude for architecture and event content while Codex integrates and validates.

### ai_pressure (467)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L5]: Aegis is now a local HTML/JS narrative roguelike prototype built from mythic domains and event clouds.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L37]: - `domains.json`: domain pool and event-cloud pressure plans.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L41]: - `domain_event_seeds.json`: individually iterable event seeds used by event lines.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L42]: - `domain_progression.json`: current domain sampling and run-state buckets.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L46]: - `.agent-memory/domain_event_contract.md`: event cloud quality bar.

### asset_import_pipeline (426)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L7]: The source PDF is `Aegis of Victory (1).pdf`. A searchable text extraction lives at `generated/corpus/aegis_of_victory_source.txt`.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L44]: - `docs/source_vibe_guide.md`: source-grounded vibe guide for generated rooms and packets.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L81]: Claude should be used for architecture and event generation the same way the Fleshpunk workflow used it: Codex builds narrow source packets, validates, and integrates; Claude dr...
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L88]: python tools/aegis_domain_agent.py source-packet --domain dionysus_dregs_domain --event-line dionysus_reflection_refusal_line --event-seed dionysus_reflection_pool_seed --out ge...
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L91]: Then build the packet without `--dry-run` and send only that packet to Claude. Keep the default source-packet budget at 7000 input tokens unless the user gives another budget.

### text_console_runtime (426)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L43]: - `generated/rooms/dionysus_room_scaffolds.json`: generated room scaffolds for document review and Claude handoff.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L44]: - `docs/source_vibe_guide.md`: source-grounded vibe guide for generated rooms and packets.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L110]: 2. Keep Theo active. He is vulnerable, but not cargo. His choices should change event clouds.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L114]: 6. Player choices should trigger concrete reactions and later echoes.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L126] `Room Generation`: ## Room Generation

### web_choice_player (312)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L5]: Aegis is now a local HTML/JS narrative roguelike prototype built from mythic domains and event clouds.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L9]: Run the document/review server:
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L12]: python tools/local_web_server.py --host 127.0.0.1 --port 3001
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L21]: Run the playable game server:
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L24]: python tools/local_game_server.py --host 127.0.0.1 --port 3002

### pose_animation_tools (226)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L5]: Aegis is now a local HTML/JS narrative roguelike prototype built from mythic domains and event clouds.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L36]: - `run_model.json`: run-level roguelike/event-cloud structure.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L38]: - `event_lines.json`: quest-line-like action/reaction/cascade threads.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L50]: Nikia and Theo are taken into Sophion's Ascent because Theo has prophetic vision. Nikia is dismissed into service work, but becomes physically sharper inside Sophion's walls. In...
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L52]: Back at Sophion, the Logarenes try to remove Theo's coin to close a Logos Fracture. Nikia interrupts the extraction, Griefshard tears the ritual open, and Nikia and Theo fall th...

### writing_corpus_review (204)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L81]: Claude should be used for architecture and event generation the same way the Fleshpunk workflow used it: Codex builds narrow source packets, validates, and integrates; Claude dr...
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L115]: 7. Event seeds are design units first; draft/revise them individually.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L133]: Room scaffolds are generated locally from structured seeds. Claude should draft final prose/content from the source packet before promotion.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/README.md#L47]: Claude drafts architecture and event content from narrow source packets. Codex validates, integrates, and keeps local tooling working.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/README.md#L65]: Room scaffolds are generated locally from structured seeds. Claude should draft final prose/content from the source packet before promotion.

### delayed_consequences (153)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L46]: - `.agent-memory/domain_event_contract.md`: event cloud quality bar.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L64]: A domain is a pressure arena. It can open with different event lines on different runs. Player actions mutate run memory, unlock or suppress event lines, queue delayed reactions...
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L76]: - `thorn_memory_line`: pain becomes memory instead of root.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L100]: - `.agent-memory/setting_backbone.md`: setting, factions, recurring forces, and run architecture.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L101]: - `.agent-memory/domain_event_contract.md`: quality bar for event clouds and event seeds.

### deck_pressure (124)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L68]: - `logos_threshold`: prologue/transition cloud around the broken extraction and fracture fall.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L96]: - `docs/mythic_source_strategy.md`: how to draw on Greek material without copying translation text.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/anthology_corpus_notes.md#L8]: - Quest skeletons: impossible task, helper debt, monster threshold, trophy, return cost.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/canon_source_map.md#L49]: 8. Missing section: likely Theo follows or is drawn to a reflection pool.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/corpus_driven_room_generation.md#L36]: - Borrow cadence and pressure grammar from `docs/source_vibe_guide.md`.

### event_clouds (120)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L5]: Aegis is now a local HTML/JS narrative roguelike prototype built from mythic domains and event clouds.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L37]: - `domains.json`: domain pool and event-cloud pressure plans.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L38]: - `event_lines.json`: quest-line-like action/reaction/cascade threads.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L40]: - `sample_event_cloud_runs.json`: sample paths through shared content.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L41]: - `domain_event_seeds.json`: individually iterable event seeds used by event lines.

### resource_upgrade_loop (60)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/canon_source_map.md#L23]: - Mythic realms: broken divine domains inside or beyond the fracture. Each realm offers a temptation, a pressure, a local artifact, and a way forward.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/canon_source_map.md#L50]: 9. Reflection pool offers Theo coinless peace; he refuses forgetting.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/canon_source_map.md#L54]: 13. False banquet offers food, family memory, rest, and relief.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/canon_source_map.md#L56]: 15. Bacchus fragment offers forgetting to both siblings.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/canon_source_map.md#L61]: 20. Thales offers to cut away the rod and preserve Nikia's grief as beautiful memory.

### touch_lane_combat (34)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L50]: Nikia and Theo are taken into Sophion's Ascent because Theo has prophetic vision. Nikia is dismissed into service work, but becomes physically sharper inside Sophion's walls. In...
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/anthology_corpus_notes.md#L33]: `Greek Anthology epigram mode + shield boss + absent sibling + Ares witness = a boss that blocks one killing blow, but records whether Nikia moved toward Theo or away from him.`
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/canon_source_map.md#L30]: 4. In the forest, a Poseidon-aligned raider attacks and chains Theo with Griefshard.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/canon_source_map.md#L43]: 2. Maenads invite them to dance/rest/forget, then attack.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/canon_source_map.md#L45]: 4. Theo resists a comfort attack by showing truth.

### vehicle_survival (16)
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/PROJECT_ORIENTATION.md#L123]: 4. Broaden Dionysus pressure beyond surrender: wine, passion, rage, frenzy, insanity, appetite, performance, and riot.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/anthology_corpus_notes.md#L16]: - Berens/Guerber/Bulfinch: broad overview and quick myth routing; cross-check before treating a detail as ancient-source pressure.
- github aegis-of-victory Valar05/aegis-of-victory [https://github.com/Valar05/aegis-of-victory/blob/HEAD/docs/corpus_workflow.md#L30]: - Riot/ballistic shield tactics: best for cover, lane discipline, threshold movement, visibility cost, and protecting someone behind the shield.
- github fleshpunk--inner-heart Valar05/fleshpunk--inner-heart [https://github.com/Valar05/fleshpunk--inner-heart/blob/HEAD/PROJECT_ORIENTATION.md#L69]: - External writing-agent work must start from a narrow source packet, not a broad repo prompt. Use `.agent-memory/source_packet_workflow.md` before asking Claude/OpenAI/another ...
- github fleshpunk--inner-heart Valar05/fleshpunk--inner-heart [https://github.com/Valar05/fleshpunk--inner-heart/blob/HEAD/PROJECT_ORIENTATION.md#L149]: python tools/mechanics_agent.py brainstorm --mock --action break_spike_lane
