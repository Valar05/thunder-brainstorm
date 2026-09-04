# Playtest-Derived Deterministic Regression Loop

Date: 2026-09-04
Project: Infinite Brutality Product One controller grid
Status: implemented guardrail; live user play remains acceptance

## Pattern

A human playtest is the source of the test harness. Record the shipped controller at its fixed simulation boundary, seal initial state plus each normalized input/yaw/jump edge and resulting state, and preserve the user's verdict separately. A reported failure promotes that tape into a deterministic red regression before runtime repair. Machine replay then converges at CPU speed, but never replaces the next live play verdict.

The terminal UI is part of the evidence transaction. `End Test` first stops input, flushes the final tape chunk, emits the terminal event, and only then lets the authenticated loopback Overwatch owner finalize the sealed attempt and return focus to Termux. Ending before movement is an explicit valid aborted tape rather than missing evidence.

## Root-Cause Lesson

A nominally valid top-edge coordinate can fail exact support containment at floating-point boundaries and make ordinary straight contact look angle-sensitive. Landing centers must include the physics controller skin inside the standable footprint. If Rapier clips intended horizontal motion but omits a wall classification, recovery may consult only the nearest real registered walkable cuboid swept by that same tick; no inferred, remote, or invented geometry is eligible.

## Anti-False-Green Gates

- Normal production replay must complete the user-derived off-center straight approach.
- Suppressing mantle ownership must make that same case red.
- Removing wall classification must remain green through bounded real-geometry recovery.
- Removing both classification and recovery must make the case red.
- Frozen ancestor hashes remain unchanged.
- Local replay is a guardrail. The user's next live run is the visual and feel acceptance lane.
