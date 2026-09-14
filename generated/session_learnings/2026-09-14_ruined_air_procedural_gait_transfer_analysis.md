# Ruined Air — Procedural Gait, Recoil Timing, and Model Transfer

**Date:** 2026-09-14
**Status:** evidence-backed session learning + user lineage correction
**Primary source repo:** `Valar05/ruined-air`
**Primary source revision inspected:** `models/PlayerBoneHandler.gd` sha `8780afa34ff38397b4c7ca988175f87ac32e64ea`; `scenes/foot_ik_root.gd` sha `f002ef331a68a8a7f42bb0bc4ce7f2e7f35f1edd`

## Lineage correction

Drew corrected the chronology: the later canonical IK-based automatic gait system was not the origin. **Ruined Air came first.** The transition to the later model/system was seamless enough that the ancestry became easy to forget.

This matters because the Ruined Air implementation demonstrates that the transferable object was not a baked walk animation. It was a **runtime motion law**.

## What the source actually does

`PlayerBoneHandler.gd` drives locomotion from velocity, phase, IK targets, and semantic bones.

Key structure:

- cadence ranges from `1.2` to `2.4` cycles/sec;
- right-foot phase is the gait cycle; left-foot phase is offset by `0.5`;
- each foot is planted for phase `0.25 .. 0.75`;
- the moving half of a foot cycle is split around the wrap:
  - `0.75 .. 1.0`: lift / recoil-like departure from plant;
  - `0.0 .. 0.25`: fast placement toward the next forward target;
- stride distance is derived from actual horizontal velocity and cadence rather than being baked into a clip;
- strafe shortens stride and adds a lateral offset;
- midair resets planted-foot state and lifts both targets toward airborne rest positions;
- hip bob is procedural and runs two sinusoidal pulses per gait cycle, matching the two-foot cadence;
- landing temporarily amplifies only the downward half of the bob, then clears the boost.

At the configured cadence range, one full gait cycle lasts about **417–833 ms**. Each 25% active subphase is therefore only about **104–208 ms**. At the midpoint cadence of 1.8 cycles/sec, a lift or placement chunk is about **139 ms**, while the planted hold is about **278 ms**.

That is the important animation read: **brief motion, long proof.**

## Recoil grammar

Drew compared the gait to good first-person recoil: the gun does not need to fly across the screen. A hand/end-effector makes a small, fast, legible displacement, the chain/body reacts, and the system rapidly returns to a stable relationship.

Ruined Air uses the same grammar at the feet:

```text
PLANT
-> brief lift
-> brief placement
-> PLANT / HOLD
```

The perceived force comes from timing, endpoint displacement, and contact authority rather than large total travel.

Body-facing code uses the same compressed correction style:

- body yaw chase: `540 deg/sec`;
- chest-to-body yaw bleed: `720 deg/sec`;
- chest counter-yaw prevents the camera from snapping when the body rotates.

The system therefore moves local authorities quickly while preserving the player's visual frame. This is recoil logic generalized to embodied locomotion.

## Why it transferred so well

The crucial portability mechanism is that gait is represented in **task / endpoint space**, not mainly as model-specific joint rotations.

`foot_ik_root.gd` removes the foot-target root from the player hierarchy and reparents it to the scene root. It follows only player yaw. Thus the IK targets are not passively dragged around by the animated skeleton or body translation; their world relationship is explicitly authored by the locomotion controller.

`PlayerBoneHandler.gd` then:

1. discovers semantic bones (`Hips`, `Spine02`, `LeftFoot`, `RightFoot`);
2. stores each model's own foot rest positions;
3. computes desired foot endpoints from velocity, phase, direction, and those rest positions;
4. lets `SkeletonIK3D` solve the model's leg geometry;
5. applies pelvis/chest compensation separately.

The reusable object is therefore approximately:

```text
GAIT = contact schedule
     + endpoint trajectory
     + cadence law
     + rest-relative geometry
     + body compensation
     + solver constraints
```

not:

```text
GAIT = a long list of joint rotations copied from Model A
```

This explains the observed transfer. A new body can inherit the same *obligations* even when its exact joints differ.

## Important caveat

Ruined Air is not magically rig-agnostic. The implementation hardcodes semantic bone names and node paths, and the target model must expose compatible leg chains and reachable IK geometry. The **motion law** is highly portable; the adapter layer is not free.

That distinction is useful because it prevents an accidental claim that retargeting vanished. What vanished was the need to transfer an entire baked gait performance joint-by-joint.

## Compared with a traditional IK walk

A common traditional game-character IK walk is **animation-led**:

```text
BAKED WALK CLIP
-> play / blend clip
-> raycast or solve feet onto ground
-> IK corrects contact error
```

The authored clip owns most of the gait: stride timing, pelvis motion, knee trajectory, arm swing, personality, and often nominal speed. IK is usually a corrective layer. It repairs foot penetration, slope mismatch, stair contact, or leg reach while trying not to destroy the authored motion.

Ruined Air is much closer to **IK-led procedural locomotion**:

```text
PLAYER VELOCITY + INPUT
-> cadence / phase law
-> explicit foot plant and move windows
-> desired world-space endpoints
-> IK solves the leg
-> procedural hip / chest / body compensation
```

Here IK is not primarily repairing a walk. The runtime law creates most of the walk.

### What Ruined Air does better

1. **Speed responsiveness without clip stretching.** Stride length and cadence are derived from actual movement. A traditional clip often needs playback-rate changes, blend trees, or multiple walk/run clips to cover the same speed range.
2. **Directional adaptation.** Strafing changes stride length and lateral placement directly. The gait responds to the controller's current movement sentence instead of selecting among a library of authored directional clips.
3. **Model transfer.** Because the reusable representation is endpoint/contact law plus target-local IK, the same gait can survive a body swap with far less dependence on matching source joint rotations.
4. **First-person embodiment.** Chest/body yaw compensation is integrated with locomotion. Camera continuity, visible body orientation, and foot behavior are solved as one runtime system rather than as a third-person clip viewed from an inconvenient camera.
5. **Cheap iteration.** Changing cadence, plant ratio, step height, stride law, strafe compression, or landing response changes the whole locomotion family immediately. No clip has to be reopened and reauthored.
6. **Low asset burden.** The system can produce convincing locomotion with little or no dedicated baked walk animation. This was especially useful for an AI-assisted prototype where the desired behavior was specified directly in code/pseudocode.
7. **Contact clarity.** Half-cycle plant holds give the eye long, stable evidence that a foot owns the ground. The motion phases can remain extremely brief without making the gait unreadable.

### What a traditional IK walk still does better

1. **Authored personality.** A strong animator can encode swagger, fatigue, injury, fear, asymmetry, anticipation, shoulder rhythm, and character-specific timing directly into a clip. Ruined Air's law is comparatively neutral unless those traits are added procedurally.
2. **Whole-body sophistication.** The Ruined Air source procedurally handles feet, hip bob, chest/body yaw, and landing emphasis, but it does not automatically create the nuanced spine, shoulder, arm, hand, and head choreography a good full-body walk cycle can contain.
3. **Uneven-terrain truth.** The inspected Ruined Air gait does not show a per-foot ground-raycast / terrain-height sampling layer in the stride function itself. It uses world-space IK targets and player grounded state, but a conventional modern foot-IK stack may outperform it on stairs, rocks, sharply changing slopes, and independently varying support heights because it explicitly samples the ground under each foot.
4. **Edge-case stability.** Purely procedural IK can produce knee popping, unreachable targets, ugly singularities, leg crossing, or strange poses on extreme proportions. Traditional animation gives the solver a strong prior pose and usually constrains it to smaller corrections.
5. **Deliberate transitions.** Start, stop, pivot, stumble, limp, turn-in-place, and emotionally loaded locomotion transitions often benefit from authored clips or a richer procedural state machine.

### The important distinction

Ruined Air is not "better IK" in every dimension. It changes **where authorship lives**.

Traditional IK locomotion:

```text
ANIMATOR AUTHORS THE GAIT
IK PRESERVES CONTACT
```

Ruined Air:

```text
SYSTEM AUTHORS THE GAIT LAW
IK EMBODIES IT
```

That makes Ruined Air unusually strong when the target is responsiveness, portability, first-person presence, low asset count, and fast systemic iteration. It is weaker when the target is highly character-specific performance or difficult terrain without additional probing.

The most promising hybrid is therefore not to replace traditional animation entirely, but to let authored animation own **character and semantic extrema** while Ruined Air-style procedural logic owns **contacts, cadence, speed response, body/camera authority, and model-local adaptation**.

Compactly:

> **Traditional IK fixes a performance to fit the world. Ruined Air asks the body to perform the world's current requirements.**

## Animation-theory consequence

This is strong evidence for Semantic Extremum / causal animation work:

> **The gait is not stored in the bones. It is stored in the relationships the bones are required to satisfy.**

And the timing is compressed in exactly the same way as effective recoil:

> **Move the load-bearing endpoint briefly. Hold the resulting truth long enough to read.**

## Transfer theorem candidate

**Motion-law portability:**

A motion system transfers well across bodies when the representation preserves task-space obligations (contacts, endpoints, timing, support state, and intent) while delegating model-specific joint resolution to the target embodiment.

Compact form:

```text
PORTABLE MOTION
= semantic obligations
+ sparse temporal extrema
+ target-local solving
```

The target body does not copy the old body's pose history. It solves the same causal sentence in its own anatomy.

## AI-coding authorship note

Drew identifies Ruined Air as an unusually clear counterexample to the feeling that AI-assisted coding means the human 'did nothing.' That feeling is accurate only if contribution is measured as keystrokes or transcription labor, which Drew intentionally minimizes.

According to Drew's recollection, the machine did relatively little conceptual work on this mechanism. He described the desired locomotion behavior in pseudocode-like terms and the implementation followed that causal specification. This is autobiographical provenance unless the original prompt transcript is recovered.

The useful distinction is:

```text
IMPLEMENTATION LABOR != DESIGN AUTHORSHIP
```

For this system, the load-bearing contribution was choosing the representation:

- feet as world/task-space obligations rather than copied joint animation;
- alternating plant/move phases;
- cadence derived from motion;
- stride derived from velocity;
- body/chest compensation preserving first-person presence;
- model-local IK solving the same behavioral law on different anatomy.

The source code verifies that this representation exists. Drew's recollection supplies the authorship history: he wanted Dark-Messiah-like full-body presence without manually authoring a conventional walk cycle, specified the behavior, and used AI as an implementation translator rather than as the origin of the mechanism.

This yields a broader AI-coding rule:

> **Authorship is not proportional to the amount of syntax personally typed. It is proportional to how much of the artifact's causal structure, constraints, judgment, and acceptance criteria came from the author.**

A useful test is whether the human can explain why the mechanism exists, what tradeoff it solves, which invariants matter, how it fails, and why a revision is better. When those answers live upstream of generated syntax, minimizing manual coding is successful abstraction, not absence of authorship.

In this frame, pseudocode can function as a compressed executable design language and the model as a compiler with judgment assistance. The machine may expand the sentence; the author still owns the sentence's causal grammar when that grammar originated with them.

## Excavation question

When comparing Ruined Air to the later canonical implementation, inspect not only visual similarity but which constants, phase laws, contact rules, and authority boundaries survived unchanged. A seamless model swap is evidence that those surviving relations are closer to the real animation primitive than the original skeleton was.
