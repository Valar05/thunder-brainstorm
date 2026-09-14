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

## Excavation question

When comparing Ruined Air to the later canonical implementation, inspect not only visual similarity but which constants, phase laws, contact rules, and authority boundaries survived unchanged. A seamless model swap is evidence that those surviving relations are closer to the real animation primitive than the original skeleton was.
