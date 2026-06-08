# FPS Platformer Arcane IK Project Links

Date: 2026-06-07

## Local Assets

- FPS player source blend: `/storage/emulated/0/Download/models/FPSPlayer.blend`
- Copied Blender asset folder: `/storage/emulated/0/Download/models`
- Blend source manifest: `/storage/emulated/0/Download/models/cauldron_blend_manifest.tsv`

## Source References

- Arcane Manifold remote repo: `ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/arcane-manifold`
- Arcane leg/body IK script: `C:\Users\dclar\workspace\arcane-manifold\models\PlayerBoneHandler.gd`
- Arcane IK root script: `C:\Users\dclar\workspace\arcane-manifold\scenes\foot_ik_root.gd`
- Arcane player controller: `C:\Users\dclar\workspace\arcane-manifold\scripts\player.gd`

## Thunder Notes

- Brainstorm note: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/session_learnings/2026-06-07_fps_platformer_arcane_ik_brainstorm.md`
- Three.js phone-port reference skill note: `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/skills/threejs_phone_game_port_agent.md`
- Gravity Fist Three.js reference target: `/storage/emulated/0/Documents/GodotProjects/gravity-fist-threejs`

## Implementation Direction

Use FPSPlayer arm animations for first-person weapon feel. Use the Arcane Manifold leg IK pattern as a procedural lower-body/platforming feel layer, improved with terrain raycasts, slope-normal foot alignment, coyote-time foot memory, and platformer-state authority.
