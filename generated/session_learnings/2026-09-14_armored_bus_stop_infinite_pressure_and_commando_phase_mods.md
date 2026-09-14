# Armored Bus Stop — Infinite Pressure + Commando Phase Mods

## Playtest/design observation
The map does not need to be an authored route. It can be effectively infinite or recycled around the camera because the combat interaction is the valuable part. The important run axis is time: difficulty escalates as the survival clock advances, consistent with Drew's other games.

## Core separation

WORLD SIZE != RUN PROGRESSION

The world may be one-screen-like, streaming, or practically infinite. Difficulty should be primarily a function of elapsed run time rather than distance traveled.

Let t = elapsed run time.

A director can derive:
- spawn budget B(t)
- elite/heavy probability H(t)
- reinforcement cadence R(t)
- enemy role diversity C(t)
- threat range / projectile pressure P(t)
- terrain complication / obstruction density T(t)

Prefer new relationships and enemy role combinations over pure HP inflation. The combined-arms behavior is visibly legible in playtest, so escalation should preserve causal readability.

## Commando lifecycle as procedural surface

The commando is not one state. It has a phase machine:

EMBARKED -> LAUNCH -> AIRBORNE -> LAND -> FIGHT -> RECOVER -> EMBARKED

Each phase is a procedural modification seam.

### Launch-condition mods
- jump earlier/later based on target density
- jump only if a heavy is exposed
- jump when APC creates a flank/crossfire geometry
- jump when projected path intersects an objective
- hold inside until suppression threshold / vehicle shock exists

### Launch-physics mods
- higher inherited APC velocity
- deliberate lateral spread
- spearhead launch toward priority target
- tighter/larger dispersion
- staggered launch timing
- ricochet / bounce / grappling variants if stylistically appropriate

### Airborne mods
- fire while airborne
- throw smoke / grenade on arc
- mark targets while airborne
- steer slightly toward a landing solution
- land behind cover or behind a heavy

### Landing mods
- landing shock / suppression burst
- instant prone / roll / spread
- impact damage on ordinary enemies
- breach soft cover on landing
- establish a temporary base-of-fire zone

### Ground-doctrine mods
- suppression stronger
- maneuver elements more aggressive
- wider flanking angles
- heavy-target focus
- med/repair/support roles
- leapfrog advance

### Recovery mods
Base rule remains asymmetric: easy to get out, hard to get back in. However, procedural upgrades may deliberately bend the rule.

Examples:
- grapnel / boarding line lets commandos intercept a moving APC
- magnetic boots / running-board catch increases allowable reboard speed
- commandos can launch themselves back toward the carrier as a reverse ballistic recovery
- recovery trigger depends on APC trajectory rather than total stop

This should feel earned as a capability, not silently erase the custody constraint.

## Key principle

TIME CREATES PRESSURE.
COMBAT CREATES FRUIT.
PROCEDURAL MODS CHANGE THE COMMANDO LIFECYCLE.

The endless map is infrastructure. The escalating fight is the run.

## Candidate one-line design

> An effectively infinite battlefield where time increases enemy combined-arms pressure while a three-person commando squad mutates across launch, flight, landing, fighting, and recovery.
