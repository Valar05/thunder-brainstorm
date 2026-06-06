# Devlog: Marrow Runner v0.9.0-rc4

I have been keeping the ledger while Marrow Runner learned how to mutate.

This release candidate is a systems pass more than a content-surface pass. The old run loop was playable, loud, and readable, but the mutation layer was still a sketch. v0.9.0-rc4 gives that layer a real shape: upgrade branches, capstones, cross-branch synergies, and a cleanup pass for a New Run choppiness issue that showed up after repeated restarts.

## Upgrade Branches

The mutation screen now has four branch surfaces:

- **Pseudopod Impact**: ram force, chain forgiveness, Ram Breach, Knockback Excavation, and tissue-breaking capstones.
- **Complement Storm**: longer complement duration, stronger enemy suction, and storm synergies.
- **Antibody Orbit**: stronger pickup vacuum, pickup flares, and antibody-fed synergies.
- **Blood Slipstream**: movement current, ram rearm forgiveness, fever control, and pickup-driven speed pressure.

The important design rule is additive behavior. These mutations are not meant to replace each other. They stack into a run identity.

## Block Breaking

Ram Breach and Knockback Excavation now make tissue walls part of the run strategy. A ram can tear open a short tunnel, and launched germs can break walls when they impact. Marrow Drill pushes that further as a capstone. Tunnel Current turns those broken passages into brief movement current, joining the block-breaking route with Blood Slipstream.

The temporary free Ram Breach test grant is gone. Block breaking now has to be earned through the branch.

## Blood Slipstream

Blood Slipstream is the new movement-pressure branch. Picking up antibodies can create a short current behind the phagocyte. Quick Clot Rearm makes ram easier to rearm without a full release. Hematic Afterimage extends the current and helps bleed fever while the player is moving well.

This gives cleanup routes more texture: late-level antibody collection can become a fast, risky movement pattern instead of only a slow search for the last pickup.

## Capstones And Synergies

The pass adds new late-run payoffs:

- **Hematic Afterimage** for Blood Slipstream.
- **Lysis Wave** for Pseudopod Impact plus Complement Storm.
- **Hemoglobin Current** for Complement Storm plus Blood Slipstream.
- **Red Cell Halo** for Antibody Orbit plus Blood Slipstream.
- **Tunnel Current** for Pseudopod Impact plus Blood Slipstream.

Existing synergy ideas like Opsonin Slingshot, Serum Storm, and Cytokine Breaker now sit inside a broader branch model.

## New Run Choppiness Fix

There was a nasty report: each New Run felt choppier than the last.

The fix hardens the runtime lifecycle. Starting or replacing a run now clears old feedback particles, particle pools, active sound loops, held input, joystick state, canvas transforms, stale button bounds, and pending viewport resets. The input binding and animation loop also have guards so they cannot stack if startup paths run more than once.

On mobile browsers, resize and fullscreen events can arrive in bursts. Those resets are now debounced so they do not rebuild a fresh run right after New Run starts.

## Release Notes

v0.9.0-rc4 is now uploaded on the `html` channel.

```text
itch target: valarsbeard/marrow-runner:html
version: v0.9.0-rc4
build: #1710635
```

Validation for this pass included JavaScript syntax checks, manifest JSON checks, release zip rebuild, zip integrity check, and a Termux Chromium DOM smoke. The DevTools automation path was unreliable on this Android Chromium build, so repeated-run profiling should get an in-page churn harness next if the choppiness report comes back.

For now, the marrow mutates, the tunnels open, the blood moves, and New Run should stop carrying old run weight behind it.
