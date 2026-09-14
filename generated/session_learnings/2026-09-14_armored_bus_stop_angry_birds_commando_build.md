# Armored Bus Stop — Angry Birds: Commando Edition build

Live playtest produced three linked corrections:

1. Commando egress was too early.
2. Egress should be visually and mechanically violent, closer to projectile launch than polite dismount.
3. The prototype accidentally started with three separate three-person teams, causing excess commandos and pre-occupied objective logic. The intended structure is one three-person squad that is recovered and redeployed.

Implemented playtest build:

- Initial squad inventory is exactly one team of three: `passengerTeamStrengths = [3]`.
- A serviced objective cannot spawn duplicate commandos.
- The team must be recovered before it can be deployed at the next stop.
- Objective commitment uses a shorter lookahead and tighter launch radius, so the squad waits longer before bailing out.
- Once committed, commandos are launched from the rear hatch toward the objective on a fast ballistic chord.
- Launch duration is roughly 0.30–0.46 s and launch speeds are several hundred world units per second in the deterministic test case.
- A visible air arc and ground shadow make the projectile handoff legible.
- Commandos can fire while airborne, then land directly into the existing suppression / base-of-fire / maneuver combined-arms behavior.
- Ingress remains asymmetric: they may launch aggressively, but reboarding still requires the APC to stop.

Deterministic logic smoke test verified:

- 250 units before Stop 1 at 200 units/s: no early deployment.
- 120 units before Stop 1 at 200 units/s: exactly three commandos launch.
- Re-running service on the same stop does not create duplicates.
- Forced recovery returns exactly one three-person team to the APC.
- Stop 2 can then deploy exactly that same three-person team.
- Mid-flight arc rises above 60 world units in the test and resolves cleanly to assault mode.

Build hashes:

- `index.html` SHA-256: `1e2678d3f6acad63bedb6f17dcbb3bb7a87ca8077e5af0dfc41bd3cc9fad4294`
- `armored-bus-stop.zip` SHA-256: `432092ba6cbc547f051e9bed9eb067f472fde925e4b1004ba807dbadc8839d14`

Compact rule:

> Delay the decision, then make the handoff violent.

And the accounting rule:

> One squad. Recover it. Redeploy it. Do not manufacture commandos at objectives.
