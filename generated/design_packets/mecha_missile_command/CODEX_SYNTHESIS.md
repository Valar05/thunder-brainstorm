# Mecha Missile Command - Codex Synthesis

## Recommended Direction

Build Proposal 1 as the MVP: a bottom-screen heroic chibi mecha defending a base from descending threats. Tap fires shoulder missiles at a target point. Hold/drag activates rifle spray toward the live finger position. Four drones orbit in a square and slave-fire in parallel.

Borrow from Proposal 3 only for drone behavior: drones can independently rotate toward their own nearest valid threat while still firing only when the player is holding/tapping. This gives visual richness without adding input complexity.

Do not start with Proposal 2's zone-mode model. It is interesting, but it adds input semantics before the base feel is proven.

## Arm Tracking

Start with single-bone shoulder-pivot rotation:

- Generate torso and arm/rifle as separate sprites.
- Arm-rifle sprite is drawn pointing right in source art.
- Runtime computes `angle = atan2(target.y - shoulder.y, target.x - shoulder.x)`.
- Clamp angle to a readable front/up arc.
- Lerp current arm angle toward target angle for mechanical smoothness.
- Draw with `translate(shoulder)`, `rotate(angle)`, `drawImage` using an anchor at the shoulder end.

Polish path: split upper arm and forearm into two assets and add two-bone IK, hiding the shoulder seam with chunky armor caps.

## First Image Packet

Generate modular assets, not poses:

- chibi sleek anime mecha torso/body, front-facing, shoulder sockets visible
- planted leg/base assembly
- combined right-facing arm + one-handed rifle sprite
- left and right shoulder missile pods
- small square drone gun body with visible barrel
- missile projectile
- rifle tracer/bolt
- explosion ring sprite sheet
- enemy descending projectile/missile

Use flat chroma background or transparent workflow, then cut out assets and record provenance.

## First Canvas Systems

1. Touch classifier: tap vs hold/drag using about 150ms and 10px movement threshold.
2. Sprite renderer with anchor-point rotation.
3. Arm tracker with clamp + lerp.
4. Projectile pools for missiles, bullets, enemy missiles.
5. Explosion manager with radius collision.
6. Wave spawner.
7. Drone formation renderer and slave-fire behavior.

## MVP Build Shape

- `index.html`, `styles.css`, `src/main.js`
- `assets/asset_manifest.json`
- `assets/mech/`, `assets/weapons/`, `assets/effects/`
- `harness.html` once the core canvas exists

Suggested working title placeholder: `mecha-command` until the theme/name is settled.
