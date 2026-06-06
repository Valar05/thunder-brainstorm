# Armor Command Prototype Lessons - Session Learnings

## Durable Project State

Armor Command lives as the standalone `armor-command` project:

```text
/storage/emulated/0/Documents/GodotProjects/armor-command
```

Local play URL:

```text
http://127.0.0.1:8791/
```

Current release/page assets:

```text
/storage/emulated/0/Documents/GodotProjects/armor-command/docs/armor_command_page_copy.md
/storage/emulated/0/Documents/GodotProjects/armor-command/release/page_assets/armor_command_page_copy.md
/storage/emulated/0/Documents/GodotProjects/armor-command/assets/page/armor_command_icon_1024.png
/storage/emulated/0/Documents/GodotProjects/armor-command/release/page_assets/armor_command_icon_512.png
```

Thunder link doc:

```text
/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/generated/project_links/armor_command_project_links.md
```

## Prototype Direction

- The original humanoid mecha direction looked impressive but did not fit the playfield perspective. A side-view armor/tank platform reads much better for a Missile Command survivorlike.
- Full-body character sprite sheets are risky for fixed-base games because baked pose perspective fights the battlefield camera. Vehicle silhouettes are easier to anchor to a ground/sky composition.
- Uploaded/generated modular sprites should be treated as parts with explicit source pose assumptions. For Armor Command, weapon and projectile sprites were left-facing; runtime needed `+PI` rotation for travel direction and base-side anchors for turrets.
- Baked hull turrets and separate weapon attachments can overlap unless each role is explicit: hull art, live rotating turret, missile batteries, drones, projectiles, explosions.

## Input And Weapon Feel

- Tap and hold should both launch ready missiles. If hold only sprays the gun, the missile command fantasy weakens.
- Independent cooldown per missile rack gives upgrades a visible, mechanical payoff: more racks means more fire opportunities, not only faster shared reload.
- Semi-auto grace feels better when described as a fixed forgiveness window. Current tuning: default `2.0s` per rack, quick release-tap can ignore the final `0.5s` of remaining rack cooldown.
- Local personal best is enough for early itch prototypes. Store best score and deepest wave in `localStorage`; add backend scoreboards later only if the game earns them.

## Difficulty Tuning

- Pressure should increase on several axes together, but visibly: missile count, spawn cadence, speed, hot-missile chance, and HP.
- Extra missile HP needs a visual cue. Armor rings and slight sprite scaling prevent “why did that survive?” confusion.
- Missile cooldown was lengthened to preserve meaningful target selection once missile HP and spawn pressure increased.

## Art / Atlas Lessons

- For generated sprite sheets, save the prompt, source image, runtime copy, atlas metadata, and source-pose assumptions in manifests.
- Do not rely on generated sprite centering. Uneven explosion frames should render into fixed centered destination cells to avoid animation jitter.
- When a sheet has transparent alpha but green RGB remains in transparent pixels, canvas rendering is fine; still record the fact for provenance.
- Keep original uploaded/generated files untouched and copy stable project-named versions into `assets/` and `release/page_assets/`.
- After creating or copying files into Android shared storage, run media scanner refresh so Google Files/upload pickers can see them.

## Background / Composition Lessons

- Ground/sky separation matters. A pure grid background made the tank feel like it floated in the same plane as missiles.
- The stronger composition uses: dark ground band, visible horizon line, sky/intercept field above, and subtle moving lines for tactical motion.
- The player platform should sit on the ground band, while enemy missiles occupy the sky. This gives the prototype an immediate read even before polish.

## Release Copy And Icon Lessons

- Page copy should be generated into both a source doc and a release-ready copy file:
  - `docs/armor_command_page_copy.md`
  - `release/page_assets/armor_command_page_copy.md`
- Icon generation should avoid text. For game icons, ask for a centered, thumbnail-readable subject and no labels/watermarks.
- Keep multiple icon sizes: source crop, 1024, 512, and release 512.
- Link release copy and icon assets at the top of Thunder docs so the doc viewer surfaces them first.

## Validation Commands

From the Armor Command project root:

```sh
node --check src/main.js
python3 -m json.tool assets/asset_manifest.json >/dev/null
python3 -m json.tool assets/vehicle/armor_vehicle_atlas.json >/dev/null
python3 tools/build_web_release.py
```

## Current Design Snapshot

- Mobile-first HTML5 canvas.
- Side-view armor/tank platform.
- Tap fires ready interceptor racks.
- Hold continuously fires ready racks and turret spray.
- Missile racks have independent cooldowns.
- Quick release-tap cadence ignores the final `0.5s` of rack cooldown.
- Upgrades include missile batteries, drones, wider bursts, pistol servo, scatter barrel, heavy shot, and plating.
- Enemy waves scale count, cadence, speed, hot-missile chance, and HP.
- Local personal best tracks score and wave in browser storage.


## Drop Pod Enemy And Kill Chain Lessons

- Armor Command now has a second enemy branch beyond incoming missiles: drop pods, robot paratroopers, and small rockets.
- The pod should be large enough to read as human-scale cargo relative to the tank. Destroying it spawns the trooper; ignoring it damages the base.
- The robot paratrooper descends slowly, fires small destructible rockets, has less HP than the pod, and shatters into falling debris on death.
- A shared hostile damage path prevents future enemy types from being missed by bullets, explosions, drones, and score logic.
- Kill-chain scoring is a formal mechanic: kills within a short timer raise a visible chain multiplier; base damage or timer expiry resets it.

## Termux Butler Source Build Notes

- The official Linux ARM64 butler binary can fail under Termux/Android because it targets the GNU/Linux loader instead of Android's linker.
- Go is installed at `/data/data/com.termux/files/usr/bin/go` and reports `go1.26.4 android/arm64`.
- Local butler is `/data/data/com.termux/files/usr/tmp/butler-android-bin/butler`, built from official `itchio/butler` source under `/data/data/com.termux/files/usr/tmp/butler-src-1780609690`.
- `butler version` reports `head, no build date`; `butler push` and `butler status` work. The `android-arm64-head/LATEST` 404 version-check message is harmless when commands continue.


## Additive Trait Mutation Pattern

The Content Drop 2 tuning pass exposed a durable upgrade-design rule: if a run advertises multiple weapon mutations, default to additive composition rather than replacement unless replacement is the explicit fantasy. Players expected Piercer Warheads, Radioactive Canisters, Splitter Payloads, and drone branches to stack because the UI verb for most other upgrades was "add".

Implementation shape from Armor Command:

- Store independent flags, levels, caps, and scalar stats on `state.stats` instead of a single exclusive type enum.
- On launch, snapshot active missile traits into the projectile (`radiation`, `piercer`, `splitter`) so later upgrades do not mutate already-fired missiles.
- On detonation, compose every active trait: base explosion, radiation cloud, splitter child bursts, and piercer damage/continuation all run from the same projectile event.
- Repeated upgrades must show concrete deltas in the offer UI, including nested values such as pierce count, child burst count, child damage scale, cloud radius/duration, and drone flame DPS/range.
- Piercer is clearest when treated as continuation rather than only damage: explode at the touch point, continue along trajectory for one or more upgraded pierces, and allow each subsequent impact to produce its own composed explosion package.
- Scatter/splitter reads better when child explosions chain forward along the missile trajectory after short delays, instead of all spawning instantly at one point.
- Drone branches follow the same rule: normal drone gunfire continues, while radioactive canisters, interceptor snaps, and flamethrower defense add side behaviors.

Reusable design test: after adding an upgrade, ask whether taking it prevents any previously earned behavior. If yes, the UI must say "replace" or the implementation should become additive.
