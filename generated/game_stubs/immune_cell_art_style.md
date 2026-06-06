# Immune Cell Maze-Chase Art Style Inference

## Source Assets Inspected

Visual inference is based on the existing Fleshpunk sprite and room assets, especially:

- `fleshpunk--inner-heart/HymnIdleBack.png`, `HymnCombatIdle.png`, `HymnAttack.png`
- `fleshpunk--inner-heart/BloodHunter.png`, `BloodHunterAttack.png`
- `fleshpunk--inner-heart/Mutation_open.png`, `Merchant.png`, `SymbioteHost.png`
- `fleshpunk--inner-heart/red_corridor.png`, `bone_corridor.png`, `Healing_pool.png`
- `fleshpunk--inner-heart/hymn.tscn` lines 4-18 and 560-579
- `fleshpunk--inner-heart/EnemySpriteShader.gdshader` lines 13-24 and 120-165
- `fleshpunk--inner-heart/world.tscn` lines 3-10 and 367-388
- `fleshpunk--inner-heart/room_dialogue.json` lines 4-6, 45-47, 102-105, 143-165

## Inferred Existing Style

The current assets read as **high-detail painterly fleshpunk fantasy cutouts**:

- Highly rendered, semi-realistic digital painting rather than pixel art or flat vector.
- Black-background transparent/cutout character sprites for actors and enemies.
- Portrait-scale assets with dense texture: chitin plates, layered bone, torn membrane, wet tissue, hair strands, skull/bone piles, veins, roots, sacs, claws, spines.
- A narrow dominant material palette: bone ivory, ochre, old gold, umber, dried blood red, black void, and amber-orange internal glow.
- Orange glow is the main readability color. It marks eyes, cores, mutation heat, active organs, attacks, and UI/outline energy.
- Silhouettes are exaggerated and readable from far away: Hymn's crescent tail-blade, BloodHunter's long proboscis and wings, Merchant's many arms, Mutation egg's clawed shell.
- Characters are front/side/back/attack paintings, not animation-sheet cartoons. Motion is implied by swapping poses, rotation, scale, skew, glow, and smear arcs.
- Environments are vertical first-person corridor paintings with central depth vanishing point, organic side walls, strong vignette, and glowing biological nodes.
- Runtime shader treatment reinforces a white inner outline, amber outer outline, dissolve/noise, glow radius, optional grayscale remap, and UV stretch/squash.


## Silhouette Pivot: Organic Maze-Icon Profile

New direction: keep Fleshpunk's detail density, but make the player read at maze scale as a simple **round engulfing cell silhouette**. The closest abstract profile is a circular maze-chase icon with an open eating/engulfing mouth, but it must be biologically transformed rather than copied.

Player silhouette rules:

- Primary read: round or oval white blood cell body, roughly circular at gameplay scale.
- Engulfing notch/mouth: an asymmetric open membrane cleft or phagocytosis fold, not a clean geometric wedge.
- Organic wobble: uneven edge, soft pseudopod bumps, membrane ruffles, cilia, or little grasping lobes.
- Fleshpunk detail: dense chitin/membrane surface, amber nucleus glow, wet highlights, small bone-like antibody hooks embedded in the rim.
- Directional clarity: the mouth/notch points toward travel direction, with subtle squash/stretch and glow pulse on turns.
- Readability first: at small scale, the player should reduce to “round pale cell with a bite-like engulfing opening.”

Avoid exact arcade-copy traits:

- No perfectly smooth yellow disk.
- No exact triangular wedge mouth.
- No flat single-color fill.
- No copied maze-character proportions, colors, or animation rhythm.

Better phrasing for prompts:

> Organic round white blood cell maze hero, circular blobby phagocyte silhouette with an open engulfing membrane cleft, pearl-white fleshpunk tissue surface, amber glowing nucleus, tiny pseudopod ruffles, dense painterly chitin detail, readable arcade-scale silhouette, dark background, not a flat yellow icon.

This gives us the gameplay readability of a classic maze-chase protagonist while preserving the Fleshpunk asset language.

## Transfer To Immune-Cell Game

For the white-blood-cell maze-chase, keep the same asset family but simplify the camera grammar for play readability.

### Player

The player should be a **heroic leukocyte warrior-cell**, not a cute blob:

- Pale ivory or pearl-white body with bone/chitin membrane plates.
- Rounded cell mass partly armored by ridged cytoplasm plates.
- Fine hairlike cilia, short tendrils, or pseudopod fingers for directional motion.
- One strong signature silhouette feature, equivalent to Hymn's crescent tail: maybe a crescent phagocyte mantle, hooked membrane shield, or sweeping antibody scythe arc.
- Warm amber immune-core glow visible through a central nucleus-like organ.
- Readable four-state poses: idle drift, chase/route movement, complement-overdrive, engulf/attack.

### Infection Agents

Infections should not be generic ghosts. Give each one a different biological silhouette while staying in the same material language:

- Direct hunter: spined bacterium/needle larva, narrow forward body, glowing infection eyes.
- Ambusher: fungal hyphae knot, filament arms, pale tendrils extending toward junctions.
- Flanker: plasmid swarm or membrane-stain organism with ring/coil motif.
- Erratic fever pressure: swollen viral sac with pulsing red-orange core and shed particles.

Use amber-red/orange glow for infection heat, but make infection bodies darker, wetter, and more red-black than the player.

### Antibodies And Pickups

- Antibodies should be tiny readable ivory/amber glyphs, shaped like Y-spurs, bone forks, or glowing immune tags.
- Complement bursts should be larger orange-white nodes, visually close to Fleshpunk mutation cores: hot, round, veined, and dangerous.
- Memory antigens should be darker gold or green-gold objects with an eye-like or fingerprint-like pattern, suggesting recognition debt.

### Maze/Tissue Board

Do not use pure flat tiles if we want the Fleshpunk feel. Use a **painted tissue-board hybrid**:

- Play surface can be top-down or three-quarter, but tiles should look like membrane slabs, capillary channels, scar seams, necrotic pockets, and lymph gates.
- Walls should be raised membrane/bone ridges with wet dark creases.
- Navigable corridors should have enough value contrast to read instantly.
- Important pickups get glow halos; background organic details stay lower contrast.
- Vignette and depth can exist, but never obscure path boundaries.

## Recommended Visual Target

**Painterly dark-biological roguelike board with cutout hero/enemy sprites.**

This means:

- Keep Fleshpunk's high-detail materials and amber glow.
- Reduce corridor-painting complexity into a readable maze layer.
- Use black/dark tissue void around the board and bright outline shaders around actors.
- Use animation by pose swaps, squash/stretch, glow pulses, and smear trails rather than full frame animation.

## Prompt Language For New Assets

Use this for AI/image-generation or art briefs:

> High-detail painterly dark biological fantasy game sprite, transparent black background, ivory chitin and bone membrane, wet tissue texture, amber-orange internal glow, sharp readable silhouette, grotesque but elegant fleshpunk anatomy, dramatic rim light, dense hand-painted detail, not pixel art, not flat vector, no cute cartoon style.

For the player specifically:

> Heroic white blood cell warrior, pearl-white leukocyte body with chitinous membrane armor, glowing amber nucleus core, pseudopod limbs, crescent phagocyte mantle, readable top-down game silhouette, dark transparent background, high-detail painterly fleshpunk fantasy sprite.

For the board:

> Top-down readable maze board made of living tissue channels, membrane walls, capillary corridors, antibody glyph pickups, amber complement nodes, necrotic red pockets, dark vignette, high-detail painterly organic texture, clear gameplay path contrast.

## Anti-Style Rules

Avoid:

- Cute blob-cell mascot art.
- Neon medical infographic style.
- Sterile blue/white hospital palette.
- Flat icon/vector enemies.
- Pixel art unless the whole game pivots deliberately.
- Fully realistic microscopy. The current style is mythic biological fantasy, not science illustration.
- Overbusy board tiles that hide path boundaries.

## Prototype Asset Plan

1. One player leukocyte cutout, 512-1024 px, four poses: idle, move, overdrive, engulf.
2. Four infection sprites, 512-1024 px, one pose each plus glow/scale animation.
3. Antibody pickup glyph, complement node, memory antigen, lymph gate.
4. A 21x21 tissue tile set: floor, wall, slow inflamed zone, necrotic greed pocket, scar trail, rearm niche.
5. One dark UI frame using the Fleshpunk dashboard idea: parchment/bone panels, amber highlights, minimal text.

## Practical Note

Fleshpunk's current orientation says required play is text-only and room visuals are deprecated as design requirements. For Thunder Brainstorm, this art style should be treated as inspiration from archived/current assets, not a requirement to change Fleshpunk itself.

## Generated Prototype Sheet

A first generated 4-frame phagocyte sheet is available here:

```text
generated/assets/phagocyte_4frame_sprite_sheet.png
```

Doc server preview:

```text
http://127.0.0.1:8765/doc/generated/assets/phagocyte_4frame_sprite_sheet.png
```

The copied asset is recorded in `generated/assets/asset_provenance.json`; the original Codex generated image remains in place under `.codex/generated_images/`.

