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

### False-Green Regression Gate

A grounded wall contact that lifts the controller 1.315 metres to the center of a proof box is not a mantle; it is a false-green air boost. Forward input and collision alone cannot authorize Product One mantle.

The constrained direct-mantle gate requires all of the following at once: the player is airborne with positive jump velocity; the actual Rapier wall-contact normal agrees with camera facing; feet are inside a narrow height window below the contacted lip; the landing target is derived from the contact point just beyond that lip using the player radius plus the existing mantle-forward inset and is clamped within the top; the registered collision owner confirms landing support and body clearance; vertical and horizontal displacement stay within explicit caps; and the shared mantle updater completes with zero velocity.

Completion must land grounded without immediately repeating from the top. Product One must never enter the general CLIMB state. Full-game climbing remains separate, while the constrained proof adapter and its deterministic contract must fail closed on grounded activation, reversed contact normals, missing support, blocked clearance, out-of-window height, excessive displacement, or any climb precursor.

## Phase Handoff

Thunder is now the first lookup surface for this Product One slice. The matching manual source-reference ledger records exact current anchors without copying source bodies. No Infinite Brutality code, tests, deployment, GitHub state, or visual acceptance was changed in this Thunder-only phase.

## Deterministic QA Performance And Receipt Lesson

A deterministic gate can be logically correct and still fail as a practical pre-push handoff if Git change discovery scans unrelated large trees. Manifest `ignore_globs` must be applied by Git during tracked and untracked enumeration, not filtered only after Git has already walked the workspace. The same exclusions must govern the receipt dirty-state hash, or selection and receipt currentness disagree.

Ignore patterns are data-only, project-relative, and fail closed on absolute paths, parent traversal, backslashes, or control characters. Projects should ignore only artifacts demonstrably outside the enrolled proof. Any imported runtime dependency that can change the verdict remains in the case `source_globs`; Product One therefore binds its exact Three.js and Rapier module inputs even while unrelated assets, data, documentation, Boxcraft outputs, and local tooling are excluded.

For the current Product One proof, this reduced a cached quick check from 8459.6 ms to 1629.8 ms while preserving the shared controller, physics, mantle, arena, simulator, and imported runtime dependencies as impact owners. The reusable rule is: prune irrelevant trees at Git enumeration, bind the same scoped dirt in receipts, and keep every verdict-bearing owner explicit in case data.

## False-Green Correction: The Playable Arena Owns The Fixtures

The earlier deterministic controller result was a false green: its low edge and stairs existed only as simulator-local cuboids, while the playable page rendered only the grid floor, one mantle box, and the 28 random boxes. A simulator that proves nearby invented geometry does not prove the play surface and must be treated as RED when the visible page is unchanged.

The binding correction is one geometry owner. `generateControllerArena()` now emits a deterministic authored traversal lane containing a low edge, continuous stairs up to a top and back down to ground, a separate 1.2-metre grounded-blocking ledge, and the constrained direct-mantle ledge, with stable roles, identifiers, colors, scenario bounds, and geometry hash. Random boxes remain, but generation excludes the authored lane bounds. `main.js` renders and registers collision by iterating those exact fixture records, and deterministic QA mounts the same records without local dimensions or positions.

Acceptance guardrails now bind geometry hash `b6a6e69f`, the exact fixture-id sequence, every scenario mount, stair return-to-ground, and a negative control that withholds a real page fixture. Withholding `controller-kata-stair-2` produces both `playable traversal fixture withheld` and a failed stair ascent/return, so synthetic-nearby proof cannot silently replace the playable route again. These are guardrails; the user-visible build remains RED until the accepted hosted visual lane shows the authored traversal geometry.

## Relative Mantle Capability Rule And Boxcraft Gap

There is no absolute authored box-height category called mantleable. After a real jump, any visible walkable cuboid can become a mantle candidate only when its contacted top edge enters the player-relative feet-to-lip reach window while the player is still rising, and the same attempt also satisfies forward input, contact-normal facing, owned wall contact, landing support, and body clearance. Autostep height, eye height, jump speed, gravity, radius, mantle-forward inset, and the relative minimum/maximum reach window are controller capabilities, not global level-design constants.

A deterministic mantle course must therefore derive probe tops from an explicit capability profile: a grounded control below autostep, a low mantle just above autostep, a high mantle whose top starts above eye level but becomes relative-reachable during the ballistic rise, and an impossible control above ballistic apex plus the relative reach. These are profile-relative test relations, never an absolute policy for authored box heights.

At Boxcraft commit `34ad1981a44db104d635dc450dcf1ddaeb6818ac`, the engine emits structural `BLOCKMAP 1` and `PIPE 1` artifacts but no 3D mantle fixture records or capability-derived scenario bounds. Its `judgeControllerArena()` adapter reads only `arena.cubes` and always rejects the resulting scatter specimen. That judge remains valid for unauthored scatter criticism, but it cannot generate or validate a mantle course and must not be cited as one.


## Boxcraft Mantle Course Owner

Boxcraft commit `b4ff8625a0981ed39eb6d25a6ba88642b974e9b4` closes the recorded generator gap with the strict `validateControllerCapabilityProfile()` and `generateMantleCourse()` engine APIs, exposed as the seventh MCP tool `generate_mantle_course`. The output contract is `BOXCRAFT MANTLE COURSE 1`: normalized capability profile, deterministic cuboid fixture records, scenario records, content hash, and formula provenance, with optional content-addressed data-only JSON and ESM artifacts.

The derivations remain controller-relative: ballistic apex is `jumpSpeed^2 / (2 * gravity)`; the grounded and low probes straddle that profile's autostep height; the high probe begins above that profile's eye height but must enter its relative reach window during rise; and the impossible probe exceeds apex plus maximum relative reach. Broad tops and at least four metres of clear approach are fixture guarantees. This API does not turn any resulting height into a global mantle category.

The older `judgeControllerArena()` scatter rejection remains unchanged and distinct: it still rejects unauthored cube scatter, while `generateMantleCourse()` is the deterministic 3D fixture owner.

## Boxcraft-Owned Dynamic Course Integration

Infinite Brutality commit `44739e6d3c156cdca60642367a52e6303fe11b0e` consumes the data-only mantle course pinned to Boxcraft `b4ff8625a0981ed39eb6d25a6ba88642b974e9b4`, course hash `b4fbadc14e0b5be04285e02a21e361a5666d917b989bb99753b379f2cdfff969`. The arena preserves the visible legacy low edge, continuous stairs, grid, and all 28 seeded random cuboids while adding the four profile-derived Boxcraft probes. Random generation reserves every course approach and top footprint.

The Product One controller no longer accepts a fixture option. For each real Rapier wall contact it asks the physics owner for an exact walkable-cuboid record, computes current feet-to-lip reach, deterministically orders candidates by contact time, reach, and source, and delegates the bounded contact-normal/support/clearance plan to the existing climb owner. A successful queued jump arms the attempt; grounding, mantle start, completion, and reset clear that arm. Full-game CLIMB remains bypassed and fail-closed in Product One.

The deterministic QA mounts the exact page-owned floor, all traversal fixtures, and all 28 random cuboids. It proves grounded autostep for the old low edge/stairs and Boxcraft step, jump mantle for Boxcraft low/high plus actual seeded `cube-12`, rejection of the impossible probe, zero completion velocity, and no CLIMB. Its anti-vacuity controls reject disabled autostep, suppressed mantle lookup, planner-only evidence, grounded boost, single-fixture privilege, and a withheld actual course box. Two fresh uncached gates produced identical trace and result hashes. These remain local guardrails; visible success still requires the user's play verdict.


## Visible No-Op Correction: Shipped Input And Prospective Risk

The user's play verdict on build 0.8.221 invalidated the idealized green: the playable route did not naturally meet a mantle target, the controller retained stricter proof-fixture thresholds than the original Infinite Brutality traversal owner, the simulator supplied full forward input and perfect yaw, the jump action bypassed shipped event semantics, and Product One omitted the existing first-person arms update/render path. A perfect scripted trajectory therefore concealed an ordinary-input visible no-op.

Build 0.8.222 routes page and QA through one shipped Product One input adapter. The page spawn comes from the Boxcraft high-mantle scenario, jump buttons no longer steal the look pointer, controller thresholds are adapted from the original constrained traversal owner, and the proof reuses the existing Infinite Brutality arms load/update/render path. Generic Rapier cuboid lookup and the Boxcraft-relative mantle rules remain unchanged; Product One still never enters CLIMB.

The permanent robustness guardrail is engine-generated, not a single author-picked trajectory: partial-stick magnitudes, approach angles, normalized jump timing, and irregular frame rates exercise the shipped adapter and real fixed-step controller. The accepted mantle timing domain is all-or-nothing; a jump beyond half of the source-owned four-metre approach is a separate negative control that must commit a real jump, avoid airborne wall contact/mantle, and land safely within the arena. The direct queue bypass must remain absent. Current deterministic results are 7/7 stick, 9/9 angle, 7/7 timing, and 7/7 variable-frame samples, with real jump/contact, zero completion velocity, and no CLIMB.

Global deterministic QA now requires a prospective causal-risk packet for enrolled projects. Every planned boundary needs an assumption, bypass/no-op/test-lie mode, ordinary variation, falsifier, and guard; newly touched unmapped boundaries fail closed. The engine derives the served HTML/ESM production graph, injects a Node trace preload, and requires actual shipped-adapter move/jump/step events. It also rejects machine ownership of visual acceptance. This is deliberately bounded: static HTML/ESM and Node tracing cannot universally attest bundlers, dynamic imports, native runtimes, adversarial tests, genuine human foresight, or pixels. User play remains the visual acceptance owner.

Workspace `AGENTS.md` separately requires an agent-authored causal-chain pre-mortem before mutation, plus a post-mutation unknown-boundary audit. The global receipt and the acting-agent receipt are independent gates; neither may self-certify the other. The global aggregate engine test suite also carries a 90-second fail-closed traceback watchdog so buffered output cannot be mistaken for an unbounded green run. Two aggregate runs completed 21/21 in 27.068 seconds and 24.897 seconds.


## Binding Supersession: Copy The Existing Accessible Mantle

This section supersedes every earlier statement in this note that makes Product One mantle depend on a queued jump, rising-only contact, a timing window, full-stick input, perfect yaw, rendered hands, or entry into CLIMB. Those were rejected redesign premises, not the commissioned Infinite Brutality mantle. They remain historical false-green evidence only.

### Exact Local Provenance

Local Git identifies commit 3b2ceed3c2bc064f9fb74728ddac809574bd0dd5 (Advance district runtime, climbing, and AI throttle polish) as the introduction point for tryBeginClimb(), startMantleFromClimb(), and updatePlayerMantle() in src/main.js. Commit ac60d95036caacd97ef58ba9f5c5fad439af5ba9 (Add nook storytelling systems and extract runtime modules) moved that owner into src/player-climb.js.

The source-owned mantle is the behavior to reproduce: select and validate a standable top, derive a landing point across the contacted lip with the existing player-radius and mantle-forward inset, interpolate from the current position to that landing over the existing mantle duration with the existing eased lift, keep velocity zero during the constrained motion, then finish exactly on the top in GROUND. The current owner remains src/player-climb.js.

tryBeginClimb() and updatePlayerClimb() are provenance for the older attachment, hang, and top-out glue. Their CLIMB state, cling, shimmy, facing thresholds, and climb-input thresholds are explicitly not part of Product One. The box demo must adapt the smallest contact-to-mantle entry around the copied startMantleFromClimb() target construction and updatePlayerMantle() motion; it must not redesign the trajectory or smuggle the rejected climb mode back in.

### Confirmed Product One Accessibility Contract

Aggressive accessibility preserves the existing mantle's generous success envelope. On the controller-grid surface, ordinary movement into a valid walkable cuboid is the complete action:

- A short valid box automounts through the existing grounded step/autostep owner.
- Any taller box whose mantle point is within the current player's reachable height automatically begins the copied constrained mantle.
- Grounded, airborne, rising, and falling contact are all eligible. There is no jump-button, jump-arm, rising-only, camera-pitch, facing-dot, full-stick, or timing-chord burden.
- The only player-facing mantle rejection is that the mantle point is too high above the player's current reachable height. Valid walkable support, body clearance, and a safe landing are construction invariants the arena/runtime must provide, not extra player burdens.
- CLIMB/aclimb never activates, and Product One loads, updates, and renders no hands, arms, or weapon.
- The 28 deterministic random boxes remain real participants in the same rule. Their actual generated dimensions must include short autostep, reachable mantle, and too-high control tiers; a privileged authored mantle box or simulator-only proxy is not proof.

The playable route must naturally expose the step and mantle behaviors without an ideal full-forward/perfect-yaw script. Local deterministic simulation is a guardrail for source ownership, generated box coverage, state transitions, ordinary-input domains, and negative controls. It cannot claim visible success. User play is the visual acceptance owner, and a user-visible no-op keeps the build RED regardless of machine results.

### Commission-Fidelity Boundary

This is a reproduction commission. The authoritative source is the local Infinite Brutality history and current src/player-climb.js owner. Approved deviations are limited to removing hands, removing the separate CLIMB/aclimb behavior, and integrating the copied mantle into the controller-grid cuboids with automatic accessible entry. New jump/rising/facing formulas, generated capability categories, or parallel mantle trajectories are outside the confirmed commission.

## 2026-09-04 — Playtest Overwatch And Pressure-Run Lineage

The user explicitly confirmed the ordered thirteen-step Playtest Overwatch inception plan. Canonical plan hash: `b8023fba84bf331238d989f4df88da298283529e2cc8710a60b1ddd89c602e7d`. This confirmation authorizes telemetry and lineage work only; it does not authorize visual capture, a live foreground trial, or a change to Product One movement.

A Thunder corpus search found no general leaderboard or pressure-run ledger owner. The closest reusable records are prototype-local personal-best patterns. Infinite Brutality already owns its player-facing personal best in `src/main.js::completeGeneratedGauntlet()`: it derives the controller-kata elapsed time, compares it with the prior `localStorage` best, updates the displayed best, and persists that local value. This remains the project-facing display owner. Playtest Overwatch replaces neither that display nor gameplay timing.

The workspace Global QA tools are the existing neutral evidence owner and will own Playtest Overwatch evidence plus the canonical append-only `pressure-run-v1` ledger. Infinite Brutality remains the display owner and may later read a ledger projection; browser `localStorage` is not promoted into authoritative competitive history.

### Confirmed Overwatch Contract

- Par and hard stop are required task inputs. There is no default par. Overwatch must not infer or silently tune par from results.
- Accepting a proposed par creates a new ruleset. Historical attempts never mutate their ruleset or par.
- Overwatch records an independent clock alongside semantic start/finish time, raw-touch and semantic input telemetry, milestones, splits, result, integrity, par delta, remaining time, failure time, failure phase, challenge, ruleset, course, build, and compatibility hashes.
- Every attempt is append-only history. Under-par success and under-par failure are equally valid telemetry; failures remain visible for diagnosis and tuning.
- Leaderboard projections rank only completed, integrity-valid runs inside the exact ruleset/course/build compatibility partition. Cross-build comparison requires a future explicit equivalence declaration.
- Default rankings are local-only and make no account, network, cloud, public-upload, or competition-grade authority claim.
- The real foreground sequence is Termux to game to Termux with fail-closed focus recovery. It may happen only after the user says `ready`; before then, failure, focus, and timing behavior is simulated locally.
- Overwatch captures telemetry and retrospective data only. Video, screenshots, audio, browser/game launch, cloud, network, and premature focus mutation are outside this phase.
- Organ is the sole writer; root independently verifies implementation, frozen ancestors, and preservation of unrelated dirt.

### Infinite Brutality Adapter Boundary

The later Infinite Brutality change is limited to a thin telemetry adapter and mission data. It must not change mantle behavior, choose the unresolved mantle reach cap, alter controller physics, or revise the current personal-best display owner. The mantle issue remains separately blocked on source-backed reach authority.

Machine preflights and local simulation are guardrails only. A real Overwatch trial requires explicit `ready`, and no telemetry result constitutes visual acceptance.
