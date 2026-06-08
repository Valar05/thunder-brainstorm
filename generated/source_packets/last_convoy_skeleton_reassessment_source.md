# Last Convoy Skeleton Reassessment Source Packet

## User Direction

The user likes the first-pass port but says: "i dont think the skeleton is worth putting meat on it yet". Treat this as a request to reassess the core game skeleton before implementing more upgrades, polish, or content.

## Current Playable Prototype

Project: /storage/emulated/0/Documents/GodotProjects/last-convoy-html5
Local URL: http://127.0.0.1:8796/?v=20260607-projectile-plan-3
Source Godot project: C:\Users\dclar\workspace\convoy on THECAULDRON
Source project name: Last Convoy

Current mechanics:
- 2D canvas vehicle action game.
- Player/root vehicle moves with joystick inertia.
- Player auto-fires a main cannon projectile.
- Player records a speed-scaled position trail.
- Pickups become convoy segments that follow the trail like a snake body.
- Raidrunner segment has a projectile turret.
- Hellkat segment has sticky targeting and flamethrower fire.
- Rustrammer enemies chase and collide.
- Motorcycles are faster explosive-contact enemies.
- Drone strike crosses the arena and drops bombs.
- Enemy waves escalate spawn counts/cadence.
- Convoy segment loss repairs follower links and reindexes the convoy.
- Textured sprite fragmentation and an offscreen WebGL fire shader bridge exist now.

Current concern:
- The mechanics are present, but the core skeleton may not yet justify deeper content investment.
- We need a stronger thesis for why the convoy body, pickups, enemy pressure, and upgrades create a distinctive loop.

## Last Convoy Lessons Already Captured

- Source parity matters: keep source_godot/ for future fixes.
- Android browser cache busting matters.
- The root vehicle should not have baked weapon visuals that contradict source scene intent.
- Sprite fragmentation must preserve texture identity to keep Godot feel.
- The Hellkat fire shader can be run as an offscreen WebGL pass while keeping the main game 2D canvas.
- Sprite orientation must be audited per asset.

Reusable patterns from the current work:
- snake_convoy_upgrade_chain: player-led position trail where pickups become role-specific convoy segments; lost middle segments repair follower links.
- source_parity_canvas_port: copy source scenes/scripts/assets, implement numeric parity first, then iterate presentation mismatches from live play feedback.
- canvas_webgl_shader_bridge: 2D canvas runtime plus isolated WebGL effects.
- textured_fragmentation_port: Godot Polygon2D shatter translated into clipped canvas image pieces.
- android_cachebusted_canvas_iteration: versioned CSS/JS query strings for Android testing.

## Armor Command Lessons To Consider

Armor Command is a separate mobile HTML5/canvas prototype that had stronger loop lessons:

- Vehicle silhouettes read better than humanoid/mecha sprite sheets when the battlefield camera needs a clear anchored platform.
- Baked hull art, live rotating turrets, drones, projectiles, and explosions need explicit role separation.
- Weapon/projectile sprite source-pose assumptions matter; runtime often needs +PI or similar rotation offsets.
- Independent cooldown per missile rack gave upgrades visible mechanical payoff.
- Tap and hold input both supporting the core fantasy mattered.
- Local personal bests were enough for early release.
- Difficulty should scale on several visible axes: count, cadence, speed, HP, special chance.
- Extra HP needs visible armor rings or scaling so survival is legible.
- Ground/sky or lane/zone separation improves immediate read.
- A second enemy branch helped: drop pods, paratroopers, small rockets.
- Kill-chain scoring worked as a formal mechanic: kills in a short window raise a visible multiplier; damage/timer expiry resets it.
- Additive trait mutation pattern: if upgrades sound like additions, they should stack unless UI explicitly says replacement.
- Upgrade state should use independent flags/levels/caps and snapshot projectile traits when fired.
- Repeated upgrades must show concrete deltas.

## Existing Update Plan Before This Reassessment

The current plan proposed:
- debug overlay and shader fallback
- kill-chain scoring and local bests
- additive upgrade state scaffold
- one upgrade choice beat after a pickup threshold or kill-chain milestone
- initial options: Raidrunner twin barrel, Hellkat wider flame, Root plating
- future support segments: interceptor car, repair truck, armor truck

Do not assume this is correct. Claude should critique whether this builds on the right skeleton.

## Design Constraints

- Keep it in 2D canvas unless a narrow WebGL effect is required.
- Do not suggest a broad 3D/Three.js rewrite.
- Do not suggest content polish before the core loop thesis is strong.
- Do not assume new generated art is available; prefer mechanics that can use current vehicle sprites and simple canvas effects.
- Prefer a small number of decisive prototype experiments over a large feature list.
- Preserve what is valuable from the Godot source: snake convoy, role segments, shatter, fire shader, mobile input.
- Be willing to say the current skeleton should pivot.

## Desired Brainstorm Role

Act as a tough game systems designer. The task is to decide what skeleton is worth testing next, not to add meat to the current one by default.
