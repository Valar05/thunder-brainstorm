# Marrow Runner Itch Page Claude Packet

This folder mirrors the source packet, Claude prompt, Claude output, final page copy, and page-asset provenance for the Marrow Runner v0.9.0-rc1 itch release-candidate workflow.

## Source Packet Inputs

- [Claude prompt](../../source_packets/claude_marrow_runner_itch_page_prompt.md)
- [Source packet](../../source_packets/marrow_runner_itch_page_source.md)

## Claude Outputs

- [Structured JSON result](claude_itch_page_copy.json)
- [Raw text result](claude_itch_page_copy_raw.txt)

## Integrated Release Docs

- [Final itch page copy draft](ITCH_PAGE_COPY.md)
- [Devlog v0.9.0-rc3](DEVLOG_v0.9.0-rc3.md)
- [Page asset provenance](page_asset_manifest.json)

## Runtime Release Assets

These remain in the prototype release folder rather than being duplicated into generated docs:

```text
prototypes/immune-maze-canvas/release/marrow-runner-v0.9.0-rc1-web.zip
prototypes/immune-maze-canvas/release/page_assets/marrow-runner-itch-cover-630x500.png
prototypes/immune-maze-canvas/release/page_assets/marrow-runner-phagocyte-frame4-transparent.png
```

## API Tool

The packet was sent through Thunder Brainstorm's Anthropic helper:

```text
tools/call_claude_packet.py
```

The reusable workflow is documented in the Skill mirror:

```text
generated/skills/thunder_claude_packet_runner.md
```
