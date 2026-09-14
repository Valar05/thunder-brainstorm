# Armored Bus Stop — First Playable Specimen

**Date:** 2026-09-14
**Status:** playable minimal functional unit

## Artifact

Repository: `Valar05/armored-bus-stop`

First playable source commit: `8695b767265e334eb7878baa123d9bdc7d30d96b`

The game is a dependency-free single-file HTML canvas prototype. It was created after the Last Convoy, Long Haul, and Through the Slit excavation converged on an APC rather than a tank.

## Control contract

There are no gameplay action buttons.

```text
LEFT THUMB  -> steering
RIGHT THUMB -> throttle / brake / reverse
```

The APC has no player-fired weapon and no dismount button.

## Core loop

```text
DRIVE
-> ARRIVE AT BUS STOP
-> SLOW ENOUGH
-> REAR DOORS OPEN AUTOMATICALLY
-> FIRETEAM INHERITS THE ARRIVAL GEOMETRY
-> INFANTRY MOVES TO COVER AND FIGHTS
-> DRIVE AGAIN
```

Three carried fireteams and three battlefield bus stops are enough for a complete run.

## Long Haul inheritance

The vehicle keeps a deliberately simplified version of Long Haul's useful separation between facing and travel momentum. Terrain changes grip. High-speed steering builds slip. The carrier can therefore arrive skewed instead of snapping its velocity instantly to its nose.

This preserves the relationship:

> **Borrow the skew, not necessarily the camera.**

The first specimen is top-down so the skew and deployment geometry remain legible.

## Last Convoy inheritance

Movement remains the primary player language. Capability is expressed through how the vehicle is driven rather than through a bank of action buttons.

The APC can ram hostile infantry through vehicle contact, but this is still movement-as-action rather than a separate attack input.

## Through the Slit inheritance

The passengers are not decorative cargo. Each stop deploys a three-person fireteam from the rear hatch. Fireteams move toward cover and fight automatically. Enemy pressure can kill deployed personnel or damage the carrier.

The source does not yet reproduce Through the Slit's full casualty/cohesion/suppression model. This first specimen preserves the structural lesson only: transported bodies are a real capability layer.

## Bus-stop consequence

A bus stop turns stopping into deployment without adding a button.

The player must enter the stop radius below the deployment speed threshold and remain controlled long enough for the doors to open. Because personnel spawn behind the carrier, arrival orientation determines the geometry the dismount inherits.

## Purity target

The prototype deliberately tests whether this sentence is already a game:

> **Drive an armored bus through dangerous ground and put armed people where they can matter.**

Everything after this should have to earn permission.
