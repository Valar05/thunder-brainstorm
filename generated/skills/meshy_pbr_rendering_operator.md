# Meshy PBR Rendering Operator

Use when a Meshy-generated or Meshy-textured model looks flat, plastic, or disconnected from nearby PBR environment art.

## Workflow

1. Inspect a fresh screenshot first and compare foreground model response against nearby world materials.
2. Verify the maps exist and use correct color spaces: albedo in sRGB, normal/roughness/metalness in linear/no-color space.
3. Verify UV transform and atlas region before blaming the texture itself.
4. Make the maps visible through material and lighting response: normal scale, roughness/metalness scalar authority, environment intensity, and foreground scene lights.
5. Do not weaken normal maps as the first response when the complaint is that no normal/roughness/metalness is visible.
6. Cache-bust the module chain and validate with syntax checks plus screenshot review.

## Driftfield / Infinite Brutality Notes

- Driftfield imported cockpit/cannons use `src/visuals.js` and cache-busted imports from both Arcade and Expedition modes.
- Infinite Brutality FPS arms use `FPSPLAYER_MESHY_VISUAL_OVERLAY` in `src/main.js` and render in a separate camera-space `armsScene`.
