# Last Convoy — Constraint Substitution From Snake

**Date:** 2026-09-14
**Status:** user-provenance design lineage + source-backed mechanic context

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

## Source-backed context

Existing Last Convoy archaeology records a snake-style convoy follow chain, player inertia/joystick control, convoy pickup vehicles, weapon-role followers, enemy-wave escalation, and several hostile pressure types. Those mechanics support the user's description that the game retained Snake-like continuous convoy motion while relocating much of the interesting constraint to hostile interaction.

## Design lesson

The inherited rule was not sacred. Its function was.

```text
Snake:
movement obligation + self-generated spatial constraint

Last Convoy:
movement obligation + enemy-generated spatial constraint
```

The useful generalization is **constraint substitution**:

> When a new system creates a richer version of the same decision pressure, remove the inherited constraint rather than stacking both by default.

This is not simply difficulty reduction. It reallocates the player's maneuvering budget toward more interesting contact.

## Contact / consequence / adapt

The resulting movement loop is better aligned with:

```text
CONTACT -> CONSEQUENCE -> ADAPT
```

because movement remains available for dealing with enemies, convoy geometry, projectiles, and route state instead of being prematurely consumed by self-collision.

## Compact rule

> **Preserve the function, not the inherited rule.**

> **If the world already supplies a better opponent, do not make the player's own tail compete for the same job.**
