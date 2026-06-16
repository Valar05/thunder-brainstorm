# Infinite Brutality Meshy PBR Rendering Handoff

Date: 2026-06-15

A live Android screenshot showed the important material contrast: the island rocks read correctly, while first-person arms only improved once the foreground render path made the supplied Meshy PBR channels visible. The texture files were not the problem.

## Durable Lesson

When a Meshy foreground model looks like flat clay but nearby PBR rocks read well, diagnose render response first:

- texture color spaces and map assignment
- UV transform into the correct atlas region
- normal scale and tangent/normal availability
- roughness/metalness scalar authority
- environment intensity and foreground scene lighting
- cache-busted runtime imports

Do not reduce the normal map as the first fix. If the complaint is that no roughness/normal/metalness is visible, the fix is to make the maps participate.

## Runtime Anchors

- `infinite-brutality/src/main.js`: `armsScene`, environment lighting, `FPSPLAYER_MESHY_VISUAL_OVERLAY`, and the camera-space FPSPlayer material setup.
- `infinite-brutality/src/materials.js`: Meshy-derived readable island rock PBR set and edge/readability overlay.
- `infinite-brutality/assets/asset_manifest.json`: FPSPlayer Meshy GLB, external PBR maps, and readable rock texture provenance.
- `infinite-brutality/PROJECT_ORIENTATION.md` and `docs/DISTRICT_RUNTIME_CONTRACT.md`: local agent-facing PBR rendering contract.

## Screenshot Rule

Foreground arms are judged visually. Passing parse checks and manifest checks only prove asset wiring, not visible PBR response. End material passes with a fresh screenshot when possible.
