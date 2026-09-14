# Arcane Manifold — Phone Habitat, Verb Compression, and the Safe Parry Floor

**Date:** 2026-09-14
**Status:** active brainstorm / evidence-backed session learning
**Source game:** `Valar05/arcane-manifold`

## Why this belongs in Thunder

This is not a project summary. It is a reusable design lesson recovered by comparing Drew's remembered play experience against the live Arcane Manifold source.

The current Arcane Manifold repository describes itself as **"A survivorlike fps"**. Its control code is not desktop-first logic with mobile controls bolted on afterward. The player is authored around touch interaction: D-pad movement, screen-drag camera, touch firing, touch block, touch jump, and tap/drag disambiguation.

The useful generalization is:

> **When the developer lives inside the target interaction surface, UX friction becomes unavoidable training data.**

Phone coding did not begin as a deliberate UX curriculum. It became one because Drew had to inhabit the controls while building the game.

## Habitat theorem extension

Repeated residence in a constrained environment can train taste without a separate practice phase:

```text
IMPORTANT ENVIRONMENT
+ UNAVOIDABLE REPEATED EXPOSURE
+ HIGH AGENCY
+ HONEST FEEDBACK
= IMPLICIT EXPERTISE
```

Examples now visible across Drew's work:

- Blender -> obtuse-systems / abundance literacy.
- Pose Lab -> animation judgment through failure scars.
- Substance Designer -> procedural material causality.
- Phone coding -> touch-control and interaction literacy.

The critical property is residence, not occasional testing.

## Arcane Manifold as a phone-native design result

The game combines several influences without merely cloning them:

```text
Brutal Doom immediacy
+ survivorlike / Vampire Survivors accumulation
+ touch-native authorship
= Arcane Manifold
```

The repository's upgrade table confirms the survivorlike mutation layer: projectile count, spread, projectile speed, fire-rate multipliers, progressive firing acceleration, homing strength, explosion radius, explosion damage, shields, nova size, and mixed upgrades all mutate the same basic combat verbs.

The important touch-design consequence is **semantic depth per button** rather than button multiplication.

## Projectile intelligence

`projectile.gd` does not simply home toward the nearest enemy.

Target selection uses:

- forward-angle preference as the dominant cost;
- distance as a smaller cost;
- target stickiness to reduce flicker;
- a close-range override bonus;
- bounded turn rate and homing strength.

Thus projectiles possess a small local targeting policy during normal flight.

## Block rewrites the battlefield

The strongest mechanic recovered from the live source is the block-driven projectile recall.

Normal state:

```text
live projectile target = camera ray target / local enemy targeting
```

Blocking state:

```text
live projectile target = player position + vertical offset
is_returning_to_player = true
```

The projectile then temporarily receives extreme homing authority and drives back toward the player. At the return radius it impacts; its explosion damage is promoted to at least its direct damage.

The result is not merely "boomerang bullets."

Blocking changes the topology of the player's existing offense:

```text
OUTBOUND SWARM
-> BLOCK
-> GLOBAL RECALL
-> CONVERGING SWARM
```

The history of previous shots remains physically present in the battlefield and becomes the next attack.

Enemies that survived or were bypassed by outbound projectiles can be struck from behind when those projectiles return.

### General pattern

> **A defensive verb can become more interesting when it transforms already-existing offensive state instead of spawning a disconnected defensive effect.**

This is PERSIST in game-mechanic form:

```text
next combat state = f(previous projectile state, current player verb)
```

not:

```text
block pressed -> spawn unrelated cool shield effect
```

## Touch scarcity creates verb compression

On phone, every additional button consumes scarce thumb-space and attention.

That pressure can improve game design when the answer is not smaller buttons but **deeper verbs**.

Arcane Manifold's BLOCK carries multiple meanings:

- defend;
- open a parry timing window;
- redirect every active projectile;
- recall the existing projectile field;
- create converging trajectories;
- create a counterattack from prior state.

One touch region carries an unusually large causal sentence.

```text
FEW COMFORTABLE TOUCH VERBS
-> MORE SEMANTIC DEPTH PER VERB
```

## Parry should be block performed beautifully

The live player source already implements Drew's preferred counter contract.

Pressing block:

- enters blocking immediately;
- records a parry timestamp;
- opens a roughly 0.5 second parry window.

If damage arrives during the parry window, the player gets the special parry payoff (currently a nova).

If timing is imperfect but block capacity remains, the action still functions as an ordinary block.

This yields:

```text
BLOCK = safe floor
GOOD TIMING = block + counter bonus
```

rather than:

```text
PARRY = binary gamble between large reward and eating the attack
```

### Design law

> **Skill should raise the ceiling without removing the floor when the base verb is already useful.**

This is especially compatible with high-frequency implicit learning:

```text
cheap failure
-> more attempts
-> more timing samples
-> better intuition
```

A catastrophic parry trains by repeatedly killing or heavily punishing the player. A block-with-parry-window trains while play continues.

Compactly:

> **Parry is not a separate verb. It is block performed beautifully.**

## Why the mechanic feels "Drew-shaped"

The player does not need a separate recall button, parry button, weapon-mode button, and defensive button.

One existing verb is asked to do more causal work.

The mechanic is therefore another instance of vicious compression:

```text
small input surface
+ persistent world state
+ strong systemic consequence
= large reconstructed play event
```

## Perturbations for future Thunder passes

When mining older games, ask:

1. Which mechanics arose because phone controls made button count expensive?
2. Which defensive verbs transform existing offensive state instead of merely canceling damage?
3. Which actions have a safe floor plus a timing-dependent skill ceiling?
4. Where does previous projectile / enemy / terrain state remain meaningful instead of being reset?
5. Which game mechanics are deeper specifically because the target platform forced semantic compression?
6. Which "weird" mechanic becomes legible when treated as a consequence of residence in the target habitat?

## Evidence boundary

The following are directly supported by the current Arcane Manifold source:

- repo identity and survivorlike-FPS description;
- touch-native input paths;
- projectile pooling;
- projectile homing / scoring logic;
- block-driven retargeting to the player;
- return-to-player impact behavior;
- parry-window timing layered on top of ordinary blocking;
- survivorlike upgrade mutations.

The Brutal Doom / Vampire Survivors lineage and the remembered experiential quality are Drew's autobiographical interpretation and should remain labeled as such until additional historical source artifacts are recovered.
