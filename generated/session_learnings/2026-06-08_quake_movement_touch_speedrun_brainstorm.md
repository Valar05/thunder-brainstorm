# Quake Movement Touch-Speedrun Brainstorm

Date: 2026-06-08

## Source Signals

- Quake III Arena GPL source release, `code/game/bg_pmove.c`, movement parameters and friction/air move paths.
- QuakeWorld / ezQuake `src/pmove.c`, jump gating, ramp-jump handling, and the discrete jump impulse.
- Current target runtime: `infinite-brutality`, which already has a touch-first camera/look loop, running arc, jump charge, and mobile HUD buttons.

## Core Read

Quake movement is not about simply moving faster. It is about preserving and redirecting momentum while friction, acceleration, and jump timing stay readable enough for skill expression.

The important part for a touch-first game is that the control scheme should expose the momentum model instead of hiding it behind a sprint button. If the player only gets a faster walk, they lose the thing that makes Quake movement worth learning.

## What The Source Says

- Quake III keeps movement parameters separate: ground acceleration, air acceleration, friction, water friction, and special-state friction are distinct knobs.
- Quake III's movement code keeps ground and air movement as separate paths, which is the right shape for a speed game.
- QuakeWorld jump logic is release-gated: `jump_held` and `jump_msec` prevent pogoing, and jump adds a discrete upward impulse.
- QuakeWorld also has ramp-jump support that can lift max ground speed on slopes, which is useful for slope-driven launch tech.

## Touch-First Translation

My read is that a viable mobile-speedrun controller should not try to mimic keyboard/mouse exactly. It should expose the same skill shape with thumb-friendly verbs.

Recommended shape:

- Left stick: analog move and strafe blend.
- Right drag: camera yaw for air steering.
- Jump: immediate takeoff on press, with a short landing-buffer window and a short front-loaded hold assist.
- No crouch button for Infinite Brutality. The crouch/duck-jump idea was rejected and folded into running-jump / bunny-hop timing so the phone HUD stays sparse.
- No dedicated sprint as the primary speed tool. Sprint can exist as a fallback, but the real speed should come from momentum carry, air steering, ramp launch, and jump timing.

## Viable Speedrun Tech For This Prototype

1. Jump buffering.
   Let the player queue the next hop a fraction before landing. This is the touch equivalent of repeated Quake jump timing without turning the game into an autopogo machine.

2. Air steering.
   Use camera drag plus left stick direction to shape wishdir in air. The goal is to make angle mastery matter even on a thumb screen.

3. Ramp / bridge launch.
   If the player jumps while entering a slope, stair lip, bridge crest, or raised landing at speed, let the surface contribute to launch instead of flattening it away. This is the Infinite Brutality replacement for crouch-slide tech.

4. Bunny-hop running jump.
   Running jump is the merged movement verb: forward acceleration, release-gated jump timing, and air steering create bunny-hop lines without adding a separate crouch input.

5. Directional jump thrust.
   Keep the running jump as a real launch, but let the launch vector follow current momentum and facing instead of forcing a generic vertical hop.

## Tuning Constraint

The biggest mistake would be to turn this into a normal mobile platformer with a sprint bar. That kills the Quake flavor.

The right pattern is: preserve momentum, limit friction, make jump timing tight, and make running-jump/ramp/bridge interactions do something visible.

## Suggested Next Step

Before touching the current runtime again, rework jump as a buffered momentum launch and design room geometry around bunny-hopable running-jump lines. Do not add a crouch button. The test is whether the player can discover route tech through bridge spacing, stair lips, ramps, landings, and air steering, not just run faster in a straight line.


## Recovered Level Generation Lesson

The lost level-design correction was: stop making generic boxes with junk scattered inside them. Quake-style room generation should produce readable movement sentences: approach lane, acceleration runway, jump lip, bridge/landing target, side recovery path, and visible reward or threat.

For Infinite Brutality, the current authored skull guillotine hall is closer to the target than the earlier junk-box rooms because it has a triple-bridge structure: central commitment bridge, side galleries, upper crossing, and a visible focal landmark. Future procedural rooms should be generated from traversal line templates first, then dressed with props. Props are secondary; route grammar is primary.

No crouch verb: crouch-slide/duck-jump ideas from generic Quake translation are superseded here. Bunny-hop feel lives in running jump, jump buffering, air steering, ramp/bridge lips, and landing spacing.
