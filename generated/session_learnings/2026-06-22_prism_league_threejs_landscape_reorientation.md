# Prism League Three.js Landscape Reorientation - Session Learnings

Date: 2026-06-22
Project: `/storage/emulated/0/Documents/GodotProjects/prism-league`

## Decision

Canvas was the wrong layer for this prototype. The correct target is a landscape-first Three.js arcade match where the player controls two magic rackets and Gasket remains the goblin-ball commentator.

## What Changed

- The runtime is now Three.js-first instead of Canvas-first.
- The intended play mode is landscape only.
- Left-half and right-half touch/mouse input now drive separate rackets.
- Racket orientation is 3D and procedural strike curves change the outgoing rally path.
- The goblin remains the mechanic, not a mascot portrait.

## Reusable Rule

When the user says the game is Pong but the ball is the goblin and the paddles are magic rackets, keep the simulation small, keep the scene in Three.js, and let the racket angle be part of the joke and part of the control feel.

## Validation

- `npm test`
- `npm run validate`
- `node --check src/game-core.mjs`
- `node --check src/game.mjs`
- `node --check src/asset-layer.mjs`
- HTTP 200 on `/` and `/src/index.html` from the local static server

## Source Notes

- Local project docs now describe the runtime as landscape-first Three.js.
- The rule source remains in `src/game-core.mjs`.
- The scene source remains in `src/asset-layer.mjs`.
