# Claude Handoff Prompt: Marrow Runner Itch Page Copy

You are drafting concise itch.io page copy from a narrow release packet. Return only a JSON object. Do not invent features, prices, URLs, screenshots, team names, or claims not present in the packet. Do not reference copyrighted arcade game names. Keep the tone vivid and arcade-readable, biological but not excessively gross, confident but not hype-heavy.

## Required Output Format

Return a single JSON object with these top-level keys:

```json
{
  "short_description": "",
  "page_description_markdown": "",
  "controls_markdown": "",
  "features": [],
  "suggested_tags": [],
  "asset_disclosure": "",
  "release_notes": "",
  "page_theme_notes": {},
  "manual_upload_checklist": []
}
```

## Constraints

- `short_description` must be under 140 characters.
- `page_description_markdown` should be 3 to 5 short paragraphs.
- `features` should contain 6 to 9 compact bullets.
- `suggested_tags` should contain 10 to 14 itch-style lowercase tags.
- `page_theme_notes` should include `background_color`, `text_color`, `accent_color`, and `embed_recommendation`.
- Mention this is `v0.9.0-rc1`, a private release candidate before v1.0.
- Keep asset disclosure accurate: generated/project-owned visual/music assets and locally synthesized SFX, provenance manifests included.
- Keep copy suitable for a page where screenshots will be uploaded manually.
