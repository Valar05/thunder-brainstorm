# Mecha Missile Command Prototype Source Packet

## Goal

Draft 2-3 distinct design proposals for a mobile-first HTML5 prototype that uses the Marrow Runner workflow: fast canvas MVP, phone-first touch testing, AI-generated bitmap art as modular assets, source-packet design, provenance tracking, and later itch-style release packaging.

## Working Premise

The game is the user's style of roguelike Missile Command:

- Mobile-first HTML5 canvas.
- Touch to fire.
- Hold to spray automatic weapons.
- Survivorlike progression.
- Player controls a heroic chibi-proportioned anime mecha.
- Style: sleek anime mecha, heroic chibi silhouette, readable and toyetic, but with chunky body/weapon inspiration from Marrow Runner and Fleshpunk.
- The mecha starts with one gun and can gain attachments:
  - shoulder missile pods, semi-auto
  - shotgun, short-range cone
  - heavy pistols, slower punchy shots
  - four drone gun slots around the player, slaved to player fire and aiming in parallel
- MVP loadout:
  - missile pods on left/right shoulder
  - one-handed rifle
  - four gun drones in a square around the mech

## Desired MVP

Classic missile-command skeleton:

- Defended zone or base at the bottom.
- Enemy projectiles descend from top.
- Player taps target point to fire interceptors.
- Holding/dragging sprays automatic weapons toward finger.
- Explosions or projectile impacts clear incoming missiles.
- Waves escalate.
- Upgrades/attachments are future-facing, but MVP should include one missile weapon, one rifle weapon, and four drone slots.

## Art / Runtime Constraint

Do not solve arm aiming by generating every pose.

Prefer modular image-generated assets plus runtime transforms:

- torso/body
- shoulder pods
- shoulder armor caps
- upper arm
- forearm/hand
- rifle sprite
- drone body sprite
- muzzle/flash/projectiles/explosions

Runtime should use pivot anchors:

- shoulder pivot
- elbow pivot if using two-bone arm
- wrist/weapon pivot
- muzzle point

The design should explain how the mech's rifle/shotgun/pistol arms track the target with 2D canvas transforms or simple IK while preserving the generated art style.

## Design Priorities

- Mobile feel first.
- Screen should be readable on phone portrait.
- One-finger input should be enough.
- Touch/hold distinction must be clear and not frustrating.
- Make aiming feel powerful without requiring precision.
- Preserve the Missile Command fantasy of intercepting descending threats.
- Preserve survivorlike growth through attachments/slots.
- Keep MVP small enough to build quickly as a standalone sibling folder.

## What To Avoid

- Do not propose a full complex roguelike metagame for MVP.
- Do not require 3D, skeletal animation packages, or heavy external frameworks.
- Do not suggest generating dozens of arm poses.
- Do not over-index on gritty military realism; keep heroic chibi anime mecha.
- Do not copy Marrow Runner's immune theme; only borrow the chunky, tactile readability and workflow lessons.
