# Last Convoy HTML5 Port Lessons

## Source And Target

- Source: `C:\Users\dclar\workspace\convoy` on THECAULDRON.
- Source project name: `Last Convoy`.
- Source main scene: `uid://qpmpjuxxt6fj`.
- Target: `/storage/emulated/0/Documents/GodotProjects/last-convoy-html5`.
- Local play URL: `http://127.0.0.1:8796/?v=20260607-shader-shatter-2`.

## What Was Ported

The port keeps Last Convoy in the workspace's 2D canvas style instead of moving to Three.js. The important retained mechanics are:

- player inertia and joystick control
- speed-scaled position trail
- snake-style convoy follow chain
- convoy pickup vehicles as upgrade roles
- Raidrunner projectile turret
- Hellkat sticky-target flamethrower
- enemy wave escalation
- Rustrammer, motorcycle, drone strike, and bomb pressure
- pause, high contrast, sound mute, music mute
- source-owned sprites/audio and a Godot source snapshot for parity checks

## Useful Implementation Lessons

1. Source parity needs a local Godot snapshot.
   The port keeps `source_godot/` so future fixes can compare against `player.gd`, `ConvoyVehicle.gd`, `GameManager.gd`, scenes, and shaders without reconnecting to Cauldron first.

2. HTML cache busting matters on Android.
   After shader and fragmentation fixes landed, the browser still served stale JS until `index.html` referenced versioned `styles.css` and `src/main.js` query strings.

3. Godot hidden state does not map one-to-one to browser CSS.
   The pause overlay initially appeared over the start screen because CSS display rules beat the `hidden` attribute. A global `[hidden] { display: none !important; }` rule is part of the working pattern.

4. The root vehicle should not draw a permanent cannon bolt.
   In Godot, the player's `Cannon` is a marker, while the cannon visual is projectile/effect state. The first canvas pass wrongly drew `Maincanon.png` on the player every frame; removing it restored the intended read.

5. Sprite fragmentation should preserve texture identity.
   Generic square particles lost the Godot feel. The improved port uses jittered grid cells, alternating triangle/quad cuts, textured clipping, radial impulses, damping, spin, and fade timing based on `shatter_polygon2d.gd`.

6. The fire shader can stay in a 2D canvas game via an offscreen WebGL pass.
   The Hellkat flamethrower uses an offscreen WebGL translation of `WaveDistort.gdshader`, then draws the rendered result back into the main 2D canvas. The fire material has no explicit mask texture, so the port uses a white mask to follow the flame branch.

7. Sprite orientation must be audited per asset.
   The drone sprite appeared rotated 90 degrees clockwise until the draw call applied the same directional convention as the other Godot-derived sprites.

## Reusable Pattern Cards

- `snake_convoy_upgrade_chain`: a player-led position trail where pickups become role-specific convoy segments, and lost middle segments repair follower links rather than collapsing the whole run.
- `source_parity_canvas_port`: copy source scenes/scripts/assets, implement conservative numeric parity first, then iterate presentation mismatches from live play feedback.
- `canvas_webgl_shader_bridge`: keep the runtime in 2D canvas but render isolated shader-heavy effects through offscreen WebGL textures.
- `textured_fragmentation_port`: translate Godot `Polygon2D` shatter into canvas clipped image pieces instead of generic debris.
- `android_cachebusted_canvas_iteration`: add versioned CSS/JS query strings after runtime changes when testing in Android browsers.

## Validation Performed

- `node --check src/main.js`
- `python3 -m json.tool assets/asset_manifest.json`
- local HTTP checks for `/`, versioned `src/main.js`, and runtime assets

## Open Followups

- Tune fragment force and lifetime by comparing against the Godot export.
- Confirm Hellkat fire shape/origin against live play; the WebGL shader is now ported, but positioning may still need small offsets.
- Add a debug toggle for shard density and shader fallback if weaker Android WebGL contexts fail.
