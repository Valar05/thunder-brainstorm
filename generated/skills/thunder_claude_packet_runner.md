# thunder-claude-packet-runner Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/thunder-claude-packet-runner/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: thunder-claude-packet-runner
description: "Use when Codex needs to use the user's Thunder Brainstorm workspace to send a bounded source packet to Claude through the Anthropic API, especially for release-page copy, scenario/design handoffs, structured JSON drafts, or Claude-authored alternate wording. Prefer this over Claude CLI; use Thunder Brainstorm's local tools/call_claude_packet.py, preserve API keys, save raw/JSON outputs, then validate and integrate the result locally."
---

# Thunder Claude Packet Runner

## Core Rule

Use the Thunder Brainstorm API helper, not Claude CLI. The helper lives at:

```text
/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/tools/call_claude_packet.py
```

It reads `ANTHROPIC_API_KEY` from `~/.secrets/anthropic.env`, `~/.bashrc`, or `~/.profile`. Do not print, copy, commit, or package the key. If the helper is missing or the key is missing, stop and ask the user before installing tools or changing credential storage.

## Workflow

1. Identify the Thunder Brainstorm root:

```sh
cd /storage/emulated/0/Documents/GodotProjects/thunder-brainstorm
```

2. Build a narrow source packet under `generated/source_packets/`. Include only facts Claude needs: current draft text, release version, target audience, constraints, exact output schema, asset/provenance facts, and things Claude must not invent.

3. Write a paired Claude prompt under `generated/source_packets/`. Require JSON unless the downstream integration explicitly needs freeform text. This keeps Codex in control of validation and final integration.

4. Confirm key presence without exposing it:

```sh
sh -lc '. ~/.bashrc >/dev/null 2>&1; if [ -n "$ANTHROPIC_API_KEY" ]; then echo ANTHROPIC_API_KEY=set; else echo ANTHROPIC_API_KEY=missing; fi'
```

5. Call Claude through the helper. Keep outputs beside the target project or under `generated/` with clear names:

```sh
python3 tools/call_claude_packet.py \
  --prompt generated/source_packets/<prompt>.md \
  --source generated/source_packets/<source>.md \
  --out <target>/claude_<task>.json \
  --raw-out <target>/claude_<task>_raw.txt \
  --response-json <target>/claude_<task>_response.json \
  --max-output-tokens 3500
```

6. Inspect the returned JSON before integrating. Reject or revise any invented feature, unsupported claim, missing required field, or wording that conflicts with project facts.

7. Integrate the accepted result into the local release doc, data file, or content file. Preserve raw and JSON Claude outputs when useful for traceability.

8. Validate the target artifacts after integration. For release copy this usually means JSON validation for Claude output/manifests, link/path checks, and checking that no API key appears in generated artifacts or release zips.

## Release Page Copy Pattern

For itch/release pages, use `references/itch-page-copy.md` as a compact packet template. Keep page copy manually pasteable because itch page metadata generally cannot be managed by butler. Butler is for build uploads.

## Safety Checks

- Never include secrets in prompts, release docs, zips, manifests, or command output.
- Do not send broad repo dumps to Claude. Send narrow packets.
- Do not let Claude be the integrator. Claude drafts; Codex validates and applies.
- If a better package/tool is needed, ask the user before working around it.
- If network/API calls fail, keep the packet files so the request can be retried without rebuilding context.

## Club Crucible / Nuxt Post Pattern

For Club Crucible posts, use Claude only as a bounded drafting agent.

1. Build source and prompt packets under Thunder Brainstorm `generated/source_packets/`.
2. Require strict JSON with `slug`, `frontmatter`, `markdown_body`, and optional link/callout fields.
3. Include exact facts: target section, live URL, post purpose, forbidden claims, release state, and any links.
4. After Claude returns, validate JSON and correct unsupported claims before integration. Watch for overstated release status, invented audience reception, duplicated links, or inaccurate asset-generation statements.
5. Save raw/JSON output under `generated/release_packets/<topic>/`.
6. Copy the final Markdown into the downstream site only after validation, then run that site's build/deploy checks.

Club Crucible observed target:

```text
content/valarsbeard-development/<slug>.md
https://clubcrucible.web.app
```

