# Thunder Brainstorm Mechanics Index

- Records: 20258
- Origins: cauldron=20258

## Mechanics

### ai_pressure (6531)
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L8]: @export var attack_power: int = 1
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L13]: @export var enemy_name: String = "Auctioneer"
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L21]: @export var audio_pattern : Array[bool]
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L25]: @onready var beat_player = $AudioStreamPlayer2D
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L27]: @onready var attack_label: RichTextLabel = _resolve_attack_label()

### touch_lane_combat (4270)
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L8]: @export var attack_power: int = 1
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L27]: @onready var attack_label: RichTextLabel = _resolve_attack_label()
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L41]: _update_attack_label()
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L84]: "natural": anim_name = &"attack"
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L85]: "flat":    anim_name = &"block"

### asset_import_pipeline (4059)
- cauldron FontForger.py [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/FontForger.py#L1]: import fontforge
- cauldron FontForger.py [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/FontForger.py#L2]: import os
- cauldron FontForger.py [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/FontForger.py#L19]: glyph.importOutlines(os.path.join(svg_dir, filename))
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\project.godot#L34]: textures/vram_compression/import_etc2_astc=true
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\battle_manager.gd#L108]: if source and source in enemy_instances and source.has_method("apply_status_effects"):

### vehicle_survival (2044)
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\player.gd#L78] `_project_on_plane`: func _project_on_plane(v: Vector3, n: Vector3) -> Vector3:
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\player.gd#L83]: var f := _project_on_plane(forward, u)
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\world_generator.gd#L33]: @export var top_noise_repeat_m: float = 48.0        # larger = broader bumps
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\world_generator.gd#L34]: @export var top_noise_power: float = 1.0            # >1 emphasizes peaks (1 = linear)
- cauldron armorture [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/armorture\scripts\player.gd#L187]: # Pitch relative to world XZ plane, derived from the forward vector

### text_console_runtime (2030)
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\battle_manager.gd#L80] `can_show_raise_button`: func can_show_raise_button() -> bool:
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\card_manager.gd#L64]: if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT:
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\card_manager.gd#L77]: if event is InputEventMouseMotion and Input.is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\pause_ui.gd#L37] `_set_settings_button_visible`: func _set_settings_button_visible(is_visible: bool) -> void:
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\pause_ui.gd#L38]: var settings_button = get_node_or_null("../SettingsButton")

### web_choice_player (1725)
- cauldron FontForger.py [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/FontForger.py#L10]: # Directory where your glyph SVGs are saved
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\project.godot#L18]: [autoload]
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\project.godot#L31]: [rendering]
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\project.godot#L33]: renderer/rendering_method="mobile"
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\aria.gd#L3]: const AriaNoteProfile = preload("res://scripts/note_profiles/aria_note_profile.gd")

### pose_animation_tools (1693)
- cauldron FontForger.py [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/FontForger.py#L21]: glyph.right_side_bearing = 20
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L109]: # This will be handled by the battle manager or music composer
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\battle_manager.gd#L122]: # Player-facing statuses are global for the choir right now.
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\battle_manager.gd#L236]: "right":
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\battle_manager.gd#L398]: "right":

### resource_upgrade_loop (1638)
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\choir_unit.gd#L42]: var player_status_effects: Resource
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scripts\player_stats.gd#L1]: extends Resource
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scripts\status_effects.gd#L1]: extends Resource
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scripts\note_profiles\choir_note_profile.gd#L1]: extends Resource
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\player_stats.gd#L1]: extends Resource

### tts_audio_pipeline (1160)
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L21]: @export var audio_pattern : Array[bool]
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\enemy.gd#L25]: @onready var beat_player = $AudioStreamPlayer2D
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\project.godot#L20]: MusicPlayer="*res://audio/music_player.gd"
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\card_manager.gd#L175]: if AccessibilityTooltipService.is_tooltip_audio_active(scene_root):
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\world.gd#L130]: if AccessibilityTooltipService.is_tooltip_audio_active(self):

### writing_corpus_review (625)
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\battle_manager.gd#L544]: var original_offset = camera.offset
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\battle_manager.gd#L552]: camera.offset = original_offset + Vector2(
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\battle_manager.gd#L559]: camera.offset = original_offset
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\choir_unit.gd#L20]: var original_index: int = -1
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\choir_unit.gd#L95]: original_index = i

### deck_pressure (373)
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\card_manager.gd#L16]: var starting_deck = [{"index": 0, "count": 4}, {"index": 1, "count": 4}, {"index": 2, "count": 1}, {"index": 3, "count": 1}, {"index":4, "count":2}]
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\card_manager.gd#L17]: var current_deck: Array[int] = []
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\card_manager.gd#L40]: _build_current_deck()
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\card_manager.gd#L41]: current_deck.shuffle()
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\card_manager.gd#L43]: await _draw_cards(CARD_DRAW)

### delayed_consequences (157)
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\world.gd#L4]: @onready var raise_button = $RaiseChoirButton
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\world.gd#L44]: $AnimationPlayer.play("RaiseChoir")
- cauldron arcanachoir [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcanachoir\scenes\world.gd#L318]: print("RaiseChoir pressed - no raise_choir() on BattleManager")
- cauldron Belly_of_Defiance [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/Belly_of_Defiance\scripts\card.gd#L123]: await delayed_effect(vfx_timing, card_values.damage_multi * player.attack_power, card_values.target_effects)
- cauldron ClubCrucible [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/ClubCrucible\package-lock.json#L1210] `hookable`: "hookable": "^5.5.3",

### source_packet_generation (111)
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\player.gd#L243]: new_projectile.global_transform = Transform3D(projectile_basis, spawn_pos)
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\radar.gd#L87]: var rel: Vector3 = e.global_transform.origin - _player.global_transform.origin
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\voxel_chunk.gd#L43]: var rel:Vector3 = (global_transform.origin - world.WORLD_ORIGIN) / VOXEL_SIZE
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\voxel_chunk.gd#L51]: global_transform.origin = world.WORLD_ORIGIN + Vector3(chunk_voxel_origin) * VOXEL_SIZE
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\voxel_chunk.gd#L255]: # Transform world normals into local space of this chunk

### event_clouds (55)
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\world_generator.gd#L86]: var room_warp_noise: FastNoiseLite     # domain warp
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\world_generator.gd#L205]: # optional domain warp
- cauldron armorture [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/armorture\scripts\world_generator.gd#L68]: var room_warp_noise: FastNoiseLite       # optional domain warp
- cauldron Belly_of_Defiance [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/Belly_of_Defiance\scripts\world_generator.gd#L86]: var room_warp_noise: FastNoiseLite     # domain warp
- cauldron Belly_of_Defiance [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/Belly_of_Defiance\scripts\world_generator.gd#L205]: # optional domain warp

### validation_pipeline (41)
- cauldron arcane-manifold [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold\scripts\projectile.gd#L94]: # Acquire/validate target
- cauldron ClubCrucible [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/ClubCrucible\package-lock.json#L5700] `utf-8-validate`: "utf-8-validate": ">=5.0.2"
- cauldron ClubCrucible [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/ClubCrucible\package-lock.json#L5706] `utf-8-validate`: "utf-8-validate": {
- cauldron ClubCrucible [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/ClubCrucible\package-lock.json#L12899] `utf-8-validate`: "utf-8-validate": ">=5.0.2"
- cauldron ClubCrucible [ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/ClubCrucible\package-lock.json#L12905] `utf-8-validate`: "utf-8-validate": {
