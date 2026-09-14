# APC as Capability Carrier

**Date:** 2026-09-14
**Status:** active brainstorm / candidate toy direction

## Correction

The fertile vehicle concept should not default to a tank. Drew's correction is more interesting: make it an **armored personnel carrier**, and take the phrase literally enough to matter.

The vehicle's primary value is not that it is itself the strongest weapon. It **carries armored personnel** whose capabilities become available because the vehicle delivers them to useful geometry.

## Core grammar

```text
DRIVE
-> choose where the carrier exists
-> choose what danger it accepts
-> choose where carried capability can be released
-> personnel act from the delivered position
-> battlefield changes
-> drive again
```

This preserves the compressed-control doctrine discovered in Last Convoy. The player need not receive a bank of action buttons merely because the carrier contains many possible capabilities.

## Why APC may be stronger than tank for this line

A tank naturally invites the design toward direct weapon control. An APC makes **transport, positioning, protection, and deployment** the first-class verbs.

That creates a useful asymmetry:

```text
carrier = mobility + protection + custody
personnel = specialized action
```

The machine therefore becomes a way to move capability through dangerous space rather than a self-contained answer to every problem.

This also weakens the need for firing to be the carrier's central interaction. A weapon may exist, but it does not need to carry the game's meaning. The meaningful question can instead be whether the vehicle gets the right bodies to the right ground in a condition where they can still act.

## Through the Slit continuity

This links directly back to the infantry contribution in `Valar05/through-the-slit`.

The current infantry model is not decorative accompaniment. It models an eighteen-body friendly formation divided into six three-body fireteams. Casualties, cohesion, and suppression change how many teams can act and how quickly they fire. Fireteams choose targets through terrain-aware rifle lanes, can search for firing positions, and can deliberately suppress machine-gun or observer positions.

That matters for the APC idea because the transported personnel can be the **real capability layer** rather than visual passengers.

A carrier's movement could therefore determine:

```text
whether personnel arrive at all
+ which terrain they inherit
+ which firing lanes exist
+ how exposed they are while dismounting
+ whether their specialized capability can express itself
```

The APC does not need to be a weaker tank. It can be a machine whose combat meaning is **delivered infantry geometry**.

## Bus-stop deployment grammar

Drew's immediate answer to "what makes the doors open?" was: **bus stop**.

That may be the cleanest answer because it preserves the no-action-button lineage. The player does not press `DISMOUNT`. The world contains places where passengers are supposed to get off, and the driving decision determines whether the carrier services those stops well or disastrously.

Candidate minimal rule:

```text
ENTER STOP ZONE
+ reduce speed below threshold
-> doors open
-> eligible personnel dismount
```

This makes stopping itself an action without adding an action button.

The stop can therefore become a causal object rather than a mission marker:

```text
approach angle
+ arrival speed
+ dwell time
+ enemy pressure
+ terrain around the stop
= quality of deployment
```

A good stop gives personnel useful ground. A bad stop may unload them into fire, strand them behind obstruction, or force the carrier to spend dangerous time stationary.

This also creates a pleasing civilian/military inversion: an APC is literally operating a hostile bus route. The transport grammar is familiar, but every ordinary transit decision carries battlefield consequence.

The important purity point is that deployment is **externalized into location and motion state** rather than represented as a new button. The environment asks for the action; the player answers by how they drive.

## Optional breadth

A minimal toy could be complete with one carrier and a very small passenger vocabulary. Additional personnel types can remain externalized content rather than prerequisites for completeness.

Examples are deliberately not canon yet. The point is architectural: new capability can arrive by changing the payload rather than changing the player's control grammar.

## Contact / consequence / adapt

```text
CONTACT
enter a stop / choose route / speed / facing / deployment geometry

CONSEQUENCE
personnel inherit the delivered position and its risks

ADAPT
move, protect, recover, redeploy, or accept loss
```

## Compact rule

> **The carrier does not need to perform every capability. It needs to deliver capability into consequence.**

> **Put breadth in the payload before putting breadth in the controls.**

> **The APC's weapon can be secondary because the passengers are not cargo decoration; they are the capability being transported.**

> **If stopping is already a verb, a bus stop can turn it into deployment without adding a button.**
