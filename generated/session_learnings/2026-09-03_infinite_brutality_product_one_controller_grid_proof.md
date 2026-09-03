# Product One Controller-Grid Proof: Copypasta Before Invention

Date: 2026-09-03

## Scope

This is a narrow Thunder-first learning record for the Infinite Brutality-derived Product One controller-grid proof. Controller v1 is already complete; the missing deliverable is the proof that exercises it. This phase records the existing ore and stops before product coding.

Thunder Brainstorm was incomplete for the current controller-kata proof: the older Infinite Brutality note covered touch movement, Quake-influenced feel, and full-game level design, but did not index the present controller-kata arena or distinguish its deliberately generic proof geometry from production environment grammar.

## Binding Anti-Reinvention Policy

Copypasta is enforced. Before writing implementation code, search Thunder first and GitHub second, then copy or adapt an existing working owner. Never invent code that can be copied or adapted. Preserve the existing public contract and make only the smallest adapter needed to expose it.

For Product One, the local owners are already identifiable:

- Movement tuning and the ground/air motor: `infinite-brutality/src/main.js`, especially `commitJump()` and `updatePlayer()`.
- Touch, look, jump, gyro, and keyboard normalization ore: the input state and handlers in `infinite-brutality/src/main.js`.
- Collision: `infinite-brutality/src/physics-world.js`, which owns the vendored Rapier character controller, static collider registration, grounded/contact results, and fixed 60 Hz world step.
- Arena/proof candidate: `infinite-brutality/src/controller-kata.js`, its current full-runtime integration in `src/main.js`, and the thin standalone candidate in `src/controller-kata-runtime.js`.

Do not rewrite movement from memory, invent contact physics, or maintain a second movement approximation merely because a standalone page is easier to assemble. The proof must exercise controller v1 through an adapter and make that shared ownership inspectable.

## Controller-Grid Proof Boundary

The controller grid is an isolated proof surface, not a full-game Infinite Brutality level. Deterministic generic boxes are allowed here because they provide collision, steering, acceleration, jump, obstruction, and exit-reaching probes. The full-game rule against random boxes and junk-filled rooms still applies to authored environments; it does not forbid generic boxes in this deliberately isolated controller proof.

The boxes are hosts for controller evidence, not authored traversal atoms and not a new level-design direction. Their existence must not be cited to relax the project's route grammar, district identity, landmark, recovery, or environment-quality requirements.

## Existing Candidate And Missing Proof

`generateControllerArena()` already supplies a deterministic seeded floor, spawn, exit, and generic cube field. `buildControllerKataSlice()` already realizes that arena through the full runtime, while `controller-kata-runtime.js` demonstrates a thin standalone surface with fixed-step movement, touch/keyboard input, and Rapier collision.

Those artifacts are proof candidates, not automatic acceptance. The outstanding proof is that the isolated surface uses controller v1 rather than a newly typed approximation, and that the accepted evidence lane demonstrates the controller against the grid. Repeating constants or behavior in another runtime is not proof of shared ownership.

## Binding Correction: Direct Mantle, Not Climbing

Product One excludes climbing. The general Infinite Brutality climb system—wall attachment, hanging, shimmying, terrain projection, climb detachment, and the full-game climb/mantle state machine—is not part of this proof and must not be imported as Product One scope.

The current `climb` lane in `tools/test_controller_kata.sh` is a false green for Product One. It runs `test_player_climb_contract.mjs`, which checks source markers for the full Infinite Brutality climb implementation; it does not drive controller input through the Product One proof, does not require a deliberately bounded mantle obstacle, and does not prove a mantle from input through completion.

The missing Product One deliverable is a direct bounded input-driven mantle. The proof must drive the real Product One input/controller path against an explicit bounded mantle candidate and demonstrate the direct mantle transition and completion within that bounded fixture. It must not require or validate a preceding general climb, cling, shimmy, terrain-climb, or full-game traversal mode.

Do not repair, refactor, broaden, or accept the full Infinite Brutality climb system as part of this correction. Its behavior and tests remain separate full-game concerns. Product One acceptance stays narrow: direct mantle evidence only, using the existing controller owner and a bounded proof adapter.

## Phase Handoff

Thunder is now the first lookup surface for this Product One slice. The matching manual source-reference ledger records exact current anchors without copying source bodies. No Infinite Brutality code, tests, deployment, GitHub state, or visual acceptance was changed in this Thunder-only phase.
