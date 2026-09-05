# Quake Route Grammar Curriculum

This file stores abstract route grammar only. It must not contain copied Quake geometry, textures, entity dumps, or layouts.

- Levels processed: 63
- Playable levels trained: 41
- Prefab/item sources retained as metadata: 22
- Infinite Brutality reference: authored triple-bridge skull guillotine hall
- Forbidden pattern: generic boxes with scattered junk

## ML Level Design Lessons

- Training scope: playable Quake maps only when present; item prefab maps are retained as source metadata but excluded from route-template training
- Generator biases:
  - Prefer readable vertical layering with side recovery over flat box rooms.
  - Place long acceleration lanes before lips, bridges, stairs, or upper landings.
  - Show goals before blocking them, then create a physical return shortcut after the route change.
  - Use pickups and monsters as breadcrumbs along an already-valid movement sentence, not as random filler.
  - Keep teleport use as recontextualization or shortcut punctuation; do not rely on it as the only loop connector.
  - Exclude crouch vocabulary; bunny-hop feel comes from running jump timing, buffered jumps, air steering, and recoverable landings.
- Feature counts:
  - entity_vertical_pressure: 41
  - long_acceleration_lanes: 40
  - vertical_layering: 40
  - reward_breadcrumbing: 40
  - teleport_recontextualization: 38
  - lock_or_gate_pacing: 37
  - switch_route_change: 34
  - dense_combat_pressure: 32

## Templates

### quake_seq_01_layered_read
- Source level: `quake-maps/start.map`
- Route sentence: entry_floor_read -> visible_upper_goal -> ramp_or_stair_lip -> mid_height_recovery -> upper_exit
- Movement lesson: height changes should teach the next jump line before the player commits
- Infinite Brutality use: Use for readable stacked rooms where upper routes are visible before they are reached.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_02_gate_loop_return
- Source level: `quake-maps/e1m1.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_03_gate_loop_return
- Source level: `quake-maps/e1m2.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_04_gate_loop_return
- Source level: `quake-maps/e1m3.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_05_gate_loop_return
- Source level: `quake-maps/e1m4.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_06_gate_loop_return
- Source level: `quake-maps/e1m5.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_07_gate_loop_return
- Source level: `quake-maps/e1m6.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_08_gate_loop_return
- Source level: `quake-maps/e1m7.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_09_gate_loop_return
- Source level: `quake-maps/e1m8.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_10_gate_loop_return
- Source level: `quake-maps/e2m1.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_11_gate_loop_return
- Source level: `quake-maps/e2m2.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_12_gate_loop_return
- Source level: `quake-maps/e2m3.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_13_gate_loop_return
- Source level: `quake-maps/e2m4.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_14_gate_loop_return
- Source level: `quake-maps/e2m5.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_15_gate_loop_return
- Source level: `quake-maps/e2m6.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_16_gate_loop_return
- Source level: `quake-maps/e2m7.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_17_gate_loop_return
- Source level: `quake-maps/e2m10.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_18_gate_loop_return
- Source level: `quake-maps/e3m1.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_19_gate_loop_return
- Source level: `quake-maps/e3m2.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_20_gate_loop_return
- Source level: `quake-maps/e3m3.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_21_gate_loop_return
- Source level: `quake-maps/e3m4.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_22_gate_loop_return
- Source level: `quake-maps/e3m5.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_23_gate_loop_return
- Source level: `quake-maps/e3m6.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_24_gate_loop_return
- Source level: `quake-maps/e3m7.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_25_gate_loop_return
- Source level: `quake-maps/e4m1.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_26_gate_loop_return
- Source level: `quake-maps/e4m2.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_27_gate_loop_return
- Source level: `quake-maps/e4m3.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_28_gate_loop_return
- Source level: `quake-maps/e4m4.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_29_gate_loop_return
- Source level: `quake-maps/e4m5.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_30_gate_loop_return
- Source level: `quake-maps/e4m6.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_31_gate_loop_return
- Source level: `quake-maps/e4m7.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_32_gate_loop_return
- Source level: `quake-maps/e4m8.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_33_gate_loop_return
- Source level: `quake-maps/dm1.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_34_gate_loop_return
- Source level: `quake-maps/dm2.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_35_layered_read
- Source level: `quake-maps/dm3.map`
- Route sentence: entry_floor_read -> visible_upper_goal -> ramp_or_stair_lip -> mid_height_recovery -> upper_exit
- Movement lesson: height changes should teach the next jump line before the player commits
- Infinite Brutality use: Use for readable stacked rooms where upper routes are visible before they are reached.
- Extracted features: long_acceleration_lanes, vertical_layering, teleport_recontextualization, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_36_layered_read
- Source level: `quake-maps/dm4.map`
- Route sentence: entry_floor_read -> visible_upper_goal -> ramp_or_stair_lip -> mid_height_recovery -> upper_exit
- Movement lesson: height changes should teach the next jump line before the player commits
- Infinite Brutality use: Use for readable stacked rooms where upper routes are visible before they are reached.
- Extracted features: long_acceleration_lanes, vertical_layering, teleport_recontextualization, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_37_gate_loop_return
- Source level: `quake-maps/dm5.map`
- Route sentence: visible_locked_goal -> side_loop_drop -> switch_or_key_pressure -> changed_route_read -> return_shortcut -> committed_exit_crossing
- Movement lesson: route memory turns the second crossing into skill expression
- Infinite Brutality use: Use when the player should understand a destination early, earn it through a side route, then move faster on the return.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, switch_route_change, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_38_layered_read
- Source level: `quake-maps/dm6.map`
- Route sentence: entry_floor_read -> visible_upper_goal -> ramp_or_stair_lip -> mid_height_recovery -> upper_exit
- Movement lesson: height changes should teach the next jump line before the player commits
- Infinite Brutality use: Use for readable stacked rooms where upper routes are visible before they are reached.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_39_layered_read
- Source level: `quake-maps/dm7.map`
- Route sentence: entry_floor_read -> visible_upper_goal -> ramp_or_stair_lip -> mid_height_recovery -> upper_exit
- Movement lesson: height changes should teach the next jump line before the player commits
- Infinite Brutality use: Use for readable stacked rooms where upper routes are visible before they are reached.
- Extracted features: long_acceleration_lanes, vertical_layering, reward_breadcrumbing, entity_vertical_pressure

### quake_seq_40_layered_read
- Source level: `quake-maps/dm8.map`
- Route sentence: entry_floor_read -> visible_upper_goal -> ramp_or_stair_lip -> mid_height_recovery -> upper_exit
- Movement lesson: height changes should teach the next jump line before the player commits
- Infinite Brutality use: Use for readable stacked rooms where upper routes are visible before they are reached.
- Extracted features: entity_vertical_pressure

### quake_seq_41_vertical_bridge_line
- Source level: `quake-maps/end.map`
- Route sentence: approach_lane -> stair_or_ramp_lip -> air_steer_gap -> upper_bridge_landing -> side_recovery_gallery -> visible_exit
- Movement lesson: running-jump bunny-hop line across vertical bridge targets
- Infinite Brutality use: Use for triple-bridge rooms with upper crossings and recoverable side galleries.
- Extracted features: long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, reward_breadcrumbing, entity_vertical_pressure

## Sequential Source Summary

1. `quake-maps/start.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, reward_breadcrumbing, entity_vertical_pressure
2. `quake-maps/e1m1.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
3. `quake-maps/e1m2.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
4. `quake-maps/e1m3.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
5. `quake-maps/e1m4.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
6. `quake-maps/e1m5.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
7. `quake-maps/e1m6.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
8. `quake-maps/e1m7.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
9. `quake-maps/e1m8.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
10. `quake-maps/e2m1.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
11. `quake-maps/e2m2.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
12. `quake-maps/e2m3.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
13. `quake-maps/e2m4.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
14. `quake-maps/e2m5.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
15. `quake-maps/e2m6.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
16. `quake-maps/e2m7.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
17. `quake-maps/e2m10.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
18. `quake-maps/e3m1.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
19. `quake-maps/e3m2.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
20. `quake-maps/e3m3.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
21. `quake-maps/e3m4.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
22. `quake-maps/e3m5.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
23. `quake-maps/e3m6.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
24. `quake-maps/e3m7.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
25. `quake-maps/e4m1.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
26. `quake-maps/e4m2.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
27. `quake-maps/e4m3.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
28. `quake-maps/e4m4.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
29. `quake-maps/e4m5.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
30. `quake-maps/e4m6.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
31. `quake-maps/e4m7.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
32. `quake-maps/e4m8.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
33. `quake-maps/dm1.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
34. `quake-maps/dm2.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
35. `quake-maps/dm3.map` (trained): long_acceleration_lanes, vertical_layering, teleport_recontextualization, reward_breadcrumbing, entity_vertical_pressure
36. `quake-maps/dm4.map` (trained): long_acceleration_lanes, vertical_layering, teleport_recontextualization, reward_breadcrumbing, entity_vertical_pressure
37. `quake-maps/dm5.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, switch_route_change, reward_breadcrumbing, entity_vertical_pressure
38. `quake-maps/dm6.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, reward_breadcrumbing, entity_vertical_pressure
39. `quake-maps/dm7.map` (trained): long_acceleration_lanes, vertical_layering, reward_breadcrumbing, entity_vertical_pressure
40. `quake-maps/dm8.map` (trained): entity_vertical_pressure
41. `quake-maps/b_armor1.map` (metadata-only): unknown_route_shape
42. `quake-maps/b_armor2.map` (metadata-only): unknown_route_shape
43. `quake-maps/b_armor3.map` (metadata-only): unknown_route_shape
44. `quake-maps/b_backpk.map` (metadata-only): unknown_route_shape
45. `quake-maps/b_barrel.map` (metadata-only): unknown_route_shape
46. `quake-maps/b_batt0.map` (metadata-only): unknown_route_shape
47. `quake-maps/b_batt1.map` (metadata-only): unknown_route_shape
48. `quake-maps/b_bh10.map` (metadata-only): unknown_route_shape
49. `quake-maps/b_bh100.map` (metadata-only): unknown_route_shape
50. `quake-maps/b_bh25.map` (metadata-only): unknown_route_shape
51. `quake-maps/b_bomb.map` (metadata-only): unknown_route_shape
52. `quake-maps/b_exbox2.map` (metadata-only): unknown_route_shape
53. `quake-maps/b_explob.map` (metadata-only): unknown_route_shape
54. `quake-maps/b_key1.map` (metadata-only): unknown_route_shape
55. `quake-maps/b_key2.map` (metadata-only): unknown_route_shape
56. `quake-maps/b_nail0.map` (metadata-only): unknown_route_shape
57. `quake-maps/b_nail1.map` (metadata-only): unknown_route_shape
58. `quake-maps/b_nail2.map` (metadata-only): unknown_route_shape
59. `quake-maps/b_rock0.map` (metadata-only): unknown_route_shape
60. `quake-maps/b_rock1.map` (metadata-only): unknown_route_shape
61. `quake-maps/b_shell0.map` (metadata-only): unknown_route_shape
62. `quake-maps/b_shell1.map` (metadata-only): unknown_route_shape
63. `quake-maps/end.map` (trained): long_acceleration_lanes, vertical_layering, lock_or_gate_pacing, teleport_recontextualization, dense_combat_pressure, reward_breadcrumbing, entity_vertical_pressure
