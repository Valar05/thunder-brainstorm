# Thunder Brainstorm Mechanics Index

- Records: 5767
- Origins: github=5767

## Mechanics

### vehicle_survival (4691)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L6]: - Loop processor: `scripts/prepare_vehicle_loops.py`
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L16]: c:/Users/dclar/workspace/long-haul/.venv-1/Scripts/python.exe scripts/prepare_vehicle_loops.py --in audio/raw_previews --out audio/processed --target-sr 48000 --fade-ms 25 --xfa...
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L29]: - Use separate players/buses for engine, tire roll, and slip layers.
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L30]: - Crossfade engine layers by normalized RPM.
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L31]: - Drive slip loop volume from tire slip ratio.

### ai_pressure (1365)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/project.godot#L14] `run/main_scene`: run/main_scene="uid://6iyy776jej33"
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_sourcing_plan.md#L32]: - `throttle_input`: scales high-band gain + transient trigger probability.
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_sourcing_plan.md#L33]: - `vehicle_speed_mps`: scales tire rolling layer gain and LPF cutoff.
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_sourcing_plan.md#L41]: 4. Normalize conservatively (headroom retained).
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L1]: extends Sprite3D

### tts_audio_pipeline (562)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/project.godot#L18]: [audio]
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L1] `Audio Pipeline Usage`: # Audio Pipeline Usage
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L3] `What Was Added`: ## What Was Added
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L4]: - Manifest: `audio/freesound_cc_manifest.json`
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L5]: - Downloader: `scripts/download_freesound_previews.py`

### web_choice_player (287)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/project.godot#L35]: [rendering]
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/project.godot#L37]: renderer/rendering_method="mobile"
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L5]: - Downloader: `scripts/download_freesound_previews.py`
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L9] `Download CC Preview Assets`: ## Download CC Preview Assets
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L11]: c:/Users/dclar/workspace/long-haul/.venv-1/Scripts/python.exe scripts/download_freesound_previews.py

### asset_import_pipeline (267)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/project.godot#L38]: textures/vram_compression/import_etc2_astc=true
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L4]: - Manifest: `audio/freesound_cc_manifest.json`
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L7]: - Attribution file: `audio/ATTRIBUTION.md`
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L9] `Download CC Preview Assets`: ## Download CC Preview Assets
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_sourcing_plan.md#L4]: Build a convincing vehicle audio system for Long Haul using only Creative Commons assets from Freesound (CC0 first, CC-BY optional).

### resource_upgrade_loop (223)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L471]: if zombie.get_meta(&"harvested", false):
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L490]: if zombie.get_meta(&"harvested", false):
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L492]: zombie.set_meta(&"harvested", true)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L553]: _destruction_material.resource_local_to_scene = true
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/cockpit_hud.gd#L51]: @onready var _level_up_resource_label: Label = $LevelUpPanel/ResourceLabel

### touch_lane_combat (204)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L14]: @export var lane_center_x := -1.0354184
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L17]: @export var attack_distance_feet := 30.0
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L22]: @export var attack_fire_interval := 1.15
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L119]: global_position = Vector3(lane_center_x, ground_y + (sprite_height * 0.5), player.global_position.z - (_road_forward_sign * follow_distance))
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L124]: var attack_distance := _get_attack_distance()

### pose_animation_tools (194)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L26]: - Keep normalization conservative (`--peak-db -1` to `-3`) to avoid clipping in game mix.
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L32]: - Trigger one-shot skid samples when slip crosses a threshold.
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_sourcing_plan.md#L32]: - `throttle_input`: scales high-band gain + transient trigger probability.
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_sourcing_plan.md#L35]: - `tire_slip_norm` in [0, 1]: fades slip loop + triggers skid one-shots.
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_sourcing_plan.md#L39]: 2. Trim each clip into loop-ready segments.

### text_console_runtime (160)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_sourcing_plan.md#L41]: 4. Normalize conservatively (headroom retained).
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/cockpit_hud.gd#L15]: @onready var _dashboard_sprite: Sprite2D = get_node_or_null("Sprite2D") as Sprite2D
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/cockpit_hud.gd#L44]: @onready var _retry_button: Button = $GameOverOverlay/RetryButton
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/cockpit_hud.gd#L45]: @onready var _pause_button: Button = $PauseButton
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/cockpit_hud.gd#L46]: @onready var _settings_button: Button = $SettingsButton

### writing_corpus_review (82)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_sourcing_plan.md#L46]: - `audio/raw_previews/`: original downloaded previews.
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/split_tree_atlas.py#L268]: original_alpha = rgba_array[:, :, 3]
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/split_tree_atlas.py#L269]: has_meaningful_alpha = bool(np.any(original_alpha < 250))
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/split_tree_atlas.py#L277]: foreground_mask |= original_alpha > 0
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/split_tree_atlas.py#L297]: export_rgba[:, :, 3] = np.where(foreground_mask, original_alpha, 0).astype(np.uint8)

### deck_pressure (29)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_pipeline_usage.md#L32]: - Trigger one-shot skid samples when slip crosses a threshold.
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L305]: trail.draw_order = GPUParticles3D.DRAW_ORDER_LIFETIME
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L310]: var tracer_mesh := trail.draw_pass_1 as RibbonTrailMesh
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L344]: tracer_material.depth_draw_mode = BaseMaterial3D.DEPTH_DRAW_ALWAYS
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L359]: trail.draw_pass_1 = tracer_mesh

### source_packet_generation (25)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/apc_chaser.gd#L327]: trail.transform_align = GPUParticles3D.TRANSFORM_ALIGN_Y_TO_VELOCITY
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/cockpit_hud.gd#L136]: var _vehicle_hud_base_transform := Transform3D.IDENTITY
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/cockpit_hud.gd#L340]: _rear_mirror_camera.global_transform = _rear_camera_anchor.global_transform
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/cockpit_hud.gd#L695]: _vehicle_hud_base_transform = _vehicle_hud_root.transform
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/cockpit_hud.gd#L712]: var rotated_basis := _vehicle_hud_base_transform.basis * Basis.from_euler(Vector3(deg_to_rad(_vehicle_hud_pitch_deg), 0.0, deg_to_rad(_vehicle_hud_roll_deg)))

### validation_pipeline (10)
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/docs/audio_sourcing_plan.md#L43]: 6. Audition and replace weak candidates with alternates.
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/vehicle_audio.gd#L53]: @export var debug_force_idle_audition := true
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/vehicle_audio.gd#L86]: if debug_force_idle_audition:
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/vehicle_audio.gd#L98]: if debug_force_idle_audition and debug_use_test_tone:
- github long-haul Valar05/long-haul [https://github.com/Valar05/long-haul/blob/HEAD/scripts/vehicle_audio.gd#L101]: if debug_force_idle_audition:
