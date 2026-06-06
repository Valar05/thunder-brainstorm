# Prompt

Using the source packet, draft a Nuxt Content Markdown post for Club Crucible announcing Marrow Runner.

Return only strict JSON with this shape:

```json
{
  "slug": "marrow-runner-ai-first-phone-workflow",
  "frontmatter": {
    "title": "...",
    "description": "...",
    "date": "2026-06-04",
    "author": "Club Crucible"
  },
  "markdown_body": "Markdown body without frontmatter",
  "link_text": "Short sentence suitable for a link to the itch page"
}
```

Requirements:

- `slug` must be filesystem-safe lowercase kebab-case.
- `markdown_body` should be 900 to 1400 words.
- Include one link to Marrow Runner on itch using Markdown link syntax.
- Include a short section about the AI-first workflow.
- Include a short section about building from a phone with Termux.
- Include a short section about what Marrow Runner actually is as a game.
- Use headings, but do not make it feel like documentation.
- The post should feel authored by a solo developer reflecting on the work, not by a product marketer.
- Do not include YAML frontmatter in `markdown_body`; frontmatter is separate in the JSON.
