# Armored Bus Stop — commando egress + combined arms

## Playtest correction
Drew reported the first stop clear felt vicious and correct, but the next stop failed to dismount. The stronger doctrine is not “arrive and politely unload.” These are commandos riding an armored vehicle. Egress should be opportunistic and aggressive; ingress should remain constrained.

## Asymmetric custody rule
- Egress can happen at speed when the carrier is approaching a live objective.
- Infantry inherit some carrier momentum, kick clear of the rear hatch, and may begin firing during the dismount.
- Reboarding remains strict: survivors must physically reach the rear hatch while the APC is nearly stopped.

Compact rule: **Getting out is a tactical opportunity. Getting back in is a custody problem.**

## Combined-arms structure added
The APC and fireteam now perform different but complementary jobs.

### APC
- mobility and protected delivery
- armored screening: the hull can physically block enemy fire headed toward infantry
- shock action: ramming heavy enemies creates a short shock state
- armor breach window: heavy ram temporarily makes the target more vulnerable to the squad
- mass weapon: ordinary enemies are squished by useful-speed hull contact

### Fireteam
- primary combat power
- center member acts as base of fire
- outer members form maneuver/flanking element
- base-of-fire suppression creates windows for the assault pair to close
- team concentrates on one target instead of splitting into unrelated duels
- crossfire increases effectiveness when members achieve separated attack angles
- squad gains extra value when the APC pins or shocks a target from another axis

This creates an actual sequence rather than merely co-located weapon systems:

> **MOBILITY → DISMOUNT → SUPPRESS → MANEUVER → SHOCK/PIN → CROSS-FIRE → CLEAR → RECOVER**

The intended emotional result is that the player feels powerful partly because the autonomous squad is visibly competent with the geometry the player creates.

## Second-stop reliability
The deployment trigger now considers the APC’s predicted near-future path, not only its current distance from the painted bus-stop circle. A fireteam may bail before the vehicle reaches the marker when the path is about to carry it through a live objective. This also better matches the “hobos jumping trains” image: the squad uses the passing vehicle as an opportunity, not a ceremonial curb.

A deterministic VM smoke test exercised all three objectives in sequence and confirmed that stops 1, 2, and 3 each mark serviced and consume one carried team. An additional test placed the APC 250 world units before stop 1 at speed and confirmed early egress before reaching the stop ring.

## Design sentence
**The carrier creates openings. The squad exploits them.**
