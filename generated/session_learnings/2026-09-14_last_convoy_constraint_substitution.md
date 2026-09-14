# Last Convoy — Constraint Substitution From Snake

**Date:** 2026-09-14
**Status:** user-provenance design lineage + direct source-backed mechanic analysis

## User lineage correction

Drew describes Last Convoy as an early compressed specimen descended from Snake.

The transformation preserved:

```text
constant movement
+ movement as the primary player verb
+ no dedicated attack buttons
```

It deliberately removed self-tail collision.

Drew's reason is functional: in the Snake comparison, there are no enemies, so the player's own tail can serve as the main spatial constraint. Last Convoy introduces enemies, and those enemies create a more interesting movement problem. Keeping self-tail collision would interfere with maneuvering around the richer external threat system.

This autobiographical design intent is separate from source-backed implementation facts.

## Direct source evidence

The live `Valar05/last-convoy` repository confirms the compression more strongly than the earlier archaeology summary did.

In `scripts/player.gd`:

- the player continues moving even when the touch control is released;
- movement direction also drives player rotation;
- a `fire_timer` advances every physics frame;
- when it reaches `fire_rate = 1.5`, the main cannon fires automatically;
- `fire()` spawns the projectile at the cannon and copies the player's current `rotation` into the shot;
- the player's moving position is continuously recorded into `position_trail` for the convoy.

In `scripts/projectile.gd`, the projectile simply advances along `Vector2.RIGHT.rotated(rotation)`. The main cannon therefore has no separate aim control. Its aim is sampled from the player's body heading at the instant the automatic fire timer resolves.

In `scripts/ConvoyVehicle.gd`, followers recover positions from the player's position trail using convoy-index-dependent spacing. The same steering choices that orient the lead cannon also write geometry into the path the convoy will occupy afterward.

Approximate control law:

```text
shot times:      t_n ~= n * 1.5 s
shot direction:  heading(t_n)
convoy path:     stored position history p(t)
follower i:      delayed / spaced sample of p(t)
```

## The delicious conflict

Drew's additional correction is crucial: the main cannon still fires. The absence of an attack button does not mean the player lacks offensive control.

Instead, offensive control has been folded into locomotion and timing.

To aim the next cannon shot, the player wants the vehicle pointed toward a target when the fire timer resolves. But changing heading and position also changes the trail geometry that the convoy will later inherit.

So one steering decision serves two competing obligations:

```text
SHORT HORIZON
orient the lead vehicle so the next automatic shot is useful

LONG HORIZON
shape the route that the convoy will subsequently occupy
```

The player is therefore not merely moving and not merely aiming. The player is arranging a future body state at a known recurring firing event while simultaneously authoring delayed formation geometry.

Compactly:

> **Steering is both reticle and choreography.**

This is stronger than "no attack buttons." It is a case of **shared-verb conflict**: one low-level control channel carries multiple legitimate goals that cannot always be optimized simultaneously.

## Design lesson

The inherited Snake rule was not sacred. Its function was.

```text
Snake:
movement obligation + self-generated spatial constraint

Last Convoy:
movement obligation + enemy-generated spatial constraint
                + sampled cannon timing
                + convoy-shaping consequence
```

The useful generalization is **constraint substitution**:

> When a new system creates a richer version of the same decision pressure, remove the inherited constraint rather than stacking both by default.

This is not simply difficulty reduction. It reallocates the player's maneuvering budget toward more interesting contact.

A second generalization is **shared-verb conflict**:

> A tiny control vocabulary can produce deep decisions when one verb affects multiple systems on different time horizons.

## Contact / consequence / adapt

The resulting loop is unusually dense:

```text
CONTACT
steer / orient

CONSEQUENCE NOW
the next sampled cannon shot inherits that orientation

CONSEQUENCE LATER
the convoy inherits the path just written

ADAPT
correct heading, formation geometry, and threat response without ever leaving the movement verb
```

## Compact rules

> **Preserve the function, not the inherited rule.**

> **If the world already supplies a better opponent, do not make the player's own tail compete for the same job.**

> **Steering is both reticle and choreography.**

> **One verb becomes deep when its consequences arrive on different clocks.**
