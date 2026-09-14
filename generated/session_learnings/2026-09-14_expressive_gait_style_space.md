# Expressive Procedural Gait — Style Space Beyond Recorded Performance

**Date:** 2026-09-14
**Status:** active brainstorm / theory extension from Ruined Air
**Parent specimen:** Ruined Air procedural IK gait

## Challenge to the earlier limitation

The procedural gait should not be treated as inherently neutral or incapable of character. That would confuse the current parameterization with the limits of the representation.

The stronger goal is to treat expressive walking as a measurable modification of a portable gait law.

A recorded performance is not necessarily the final animation asset. It can be a calibration specimen from which the system estimates the mechanical differences that make one walk read differently from another.

## Core representation

Let the procedural gait controller be:

```text
G(anatomy, velocity, direction, phase, support_state, style)
```

where `style` is a compact parameter vector rather than a baked animation clip.

Candidate measurable style channels include:

- cadence bias relative to travel speed;
- duty factor / planted-foot proportion;
- stride-length scale;
- step-height / toe-clearance scale;
- vertical and lateral center-of-mass excursion;
- pelvis yaw/roll amplitude and phase;
- torso lean and counter-rotation;
- arm-swing amplitude, phase, and asymmetry;
- head/camera stabilization versus body participation;
- plant stiffness / impact sharpness;
- acceleration and deceleration profile;
- left-right asymmetry;
- timing variance and repeatability;
- recoil / recovery speed after contact.

These are hypotheses to measure, not stereotypes. Do not assume in advance that 'happy' means bouncy or 'angry' means stompy. Record performances, extract the differences, and let the observed mechanics define the style vector.

## Style deltas

Record a neutral walk and one or more expressive walks under controlled conditions. Normalize for body scale, travel speed, path, and camera where possible. Fit each recording back into the same procedural controller.

Then define:

```text
neutral = s0
happy specimen = s0 + Δhappy
angry specimen = s0 + Δangry
```

The useful artifact is not the recorded clip alone. It is the recovered `Δstyle`.

A runtime can then evaluate:

```text
s = s0 + α Δhappy + β Δangry + γ Δother
```

with biomechanical and semantic clamps.

This makes intensity continuous, permits interpolation between styles, and allows bounded extrapolation beyond what the actor personally performed.

## Why this becomes explosive

Once style is represented as causal parameters rather than a clip library, the actor no longer needs to physically perform every final variation.

Human performance supplies examples of what certain style regions mean. Mathematics supplies the transform. IK and the target body solve the resulting obligations.

The production chain becomes:

```text
HUMAN PERFORMANCE
-> MEASURED STYLE DIFFERENCE
-> PARAMETRIC STYLE VECTOR
-> PROCEDURAL GAIT LAW
-> TARGET-LOCAL IK SOLVE
-> NEW BODY / NEW INTENSITY / NEW COMBINATION
```

This is not unconstrained synthesis. Extrapolation can leave the plausible region, produce unreadable mixtures, or collide with anatomy and terrain. Therefore every generated style needs plausibility and recognition tests.

## Important distinction

An emotion label is not assumed to be a universal gait vector. 'Happy,' 'angry,' 'afraid,' 'tired,' or any other label may contain multiple valid performances and actor-specific habits.

The robust object is therefore a **style manifold**, not one canonical vector per emotion.

Drew's performances can seed directions in that space without imprisoning the system inside Drew's acting range.

## Proposed experiment

Capture the same short path at matched speeds for neutral plus several intentionally distinct walks. Extract foot-contact timing, foot trajectories, root/pelvis/chest/head trajectories, arm swing, and phase relationships. Fit those measurements into Ruined Air-style controller variables. Render the recovered styles on the same rig, then on a second rig. Test whether observers can distinguish the intended styles without labels.

The critical proof is not that a classifier can name the emotion. It is that the procedural parameter changes preserve the meaningful physical difference while surviving a body swap.

## Theory consequence

Ruined Air suggests that locomotion identity may be decomposed into two layers:

```text
GAIT TRUTH = support/contact law + embodiment solver
GAIT CHARACTER = style modulation of that law
```

If this holds, expressive animation becomes portable in the same sense as the base gait.

Compact doctrine:

> **Do not store the expressive walk as a clip if the expression can be recovered as a change in the laws that generate the walk.**

And the larger claim:

> **Performance can be evidence for a motion law rather than the boundary of the final performance.**

## Restraint specimen — diagonal hip yaw was consciously deferred

Drew recalls that the desired Ruined Air version included hip turning into diagonal travel, but the feature became disproportionately difficult. He deliberately stopped pursuing it so the game itself could continue. This is useful evidence of restraint rather than an unresolved defect.

The shipped behavior is a coherent locomotion style: comparatively camera/body-forward movement with more strafing across diagonal travel, rather than strongly rotating the pelvis into each movement vector. The omitted feature would have changed the **movement-direction coupling**, not repaired a broken walk.

Represent the distinction with a style parameter rather than a correctness flag. Let:

```text
θ_view  = facing / camera-relative heading
θ_move  = horizontal travel heading
κ_hip   = movement-direction coupling in [0, 1] (or a wider bounded expressive range)
```

Then a conceptual pelvis target is:

```text
θ_hip_target = shortest-angle blend(θ_view, θ_move, κ_hip)
```

Interpretation:

```text
κ_hip ≈ 0   -> strafe-dominant gait; pelvis preserves facing
κ_hip ≈ 1   -> travel-dominant gait; pelvis turns into movement
0 < κ_hip < 1 -> hybrid body-leading / strafing styles
```

The real controller may use separate coupling, rate, phase, and clamp terms rather than one scalar, for example pelvis coupling, chest counter-rotation, maximum yaw offset, turn-in rate, and turn-out recovery. The important theoretical point is that the unimplemented idea belongs naturally inside the expressive parameter space.

This reframes the historical stopping point:

> **A deferred feature can expose a style dimension even when the current implementation is already correct.**

It also supplies a concrete example of sufficiency discipline. The project did not need to maximize locomotion sophistication before becoming a game. The existing strafe-dominant solution was complete enough to ship forward, while the unrealized hip-turn behavior remained recoverable as a later axis of expression.

This is especially relevant to expressive gait. Anger, confidence, caution, injury, armor, weapon posture, or individual character may plausibly alter how strongly the pelvis commits to the travel vector. That claim should be measured from performance rather than assumed, but Ruined Air already gives the system a place to encode the result.

## Future repo candidate

This theory is now large enough to justify a dedicated experimental repository when implementation begins. Until then, preserve it in Thunder Brainstorm as the design seed rather than prematurely choosing a production architecture.
