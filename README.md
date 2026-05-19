# everything-codex: Paper Writing Profile

Research and paper-writing workflow profile for Codex and Cursor. It combines
the minimal shared baseline from `main` with the paper-writing skills currently
provided in the local `skills/` source directory, plus original ready-to-copy
prompt templates inspired by common research-writing workflows.

## Layout

```text
AGENTS.md             Shared assistant behavior guidance
CLAUDE.md             Claude Code bridge to shared guidance
.codex/config.toml    Codex model and MCP configuration from main
.agents/skills/*      Codex-visible writing skills
.cursor/mcp.json      Cursor MCP configuration
.cursor/skills/*      Cursor-visible writing skills
prompts/              Ready-to-copy research-writing prompt templates
THIRD_PARTY_NOTICES.md
```

The local source directories `skills/` and `awesome-ai-research-writing/` are
intentionally not committed.

## Included Skills

| Skill | Purpose |
| --- | --- |
| `ml-paper-writing` | Draft and revise ML/AI papers for NeurIPS, ICML, ICLR, ACL, AAAI, and COLM; includes templates, citation discipline, and checklist workflows. |
| `eda-journal-writing` | Draft EDA/CAD journal papers for IEEE TCAD, TVLSI, TODAES, ESL, and related venues. |
| `latex-build-fix` | Compile and repair LaTeX projects with a repeatable build chain. |
| `humanizer` | Remove common AI-writing patterns while preserving meaning and author voice. |
| `docx` | Work with Word `.docx` files, including reading, editing, comments, and tracked changes. |
| `doc-coauthoring` | Run a structured context-gathering, drafting, refinement, and reader-testing workflow. |

## Prompt Library

The prompt library in `prompts/research-writing.md` includes full templates for:

- translation and rewriting for LaTeX and Word
- paragraph shortening and expansion
- English and Chinese paper polishing
- logic checks and reviewer-style paper review
- AI-writing cleanup
- figure, table, caption, and experiment-analysis prompts
- model-choice guidance
- skill usage recipes

## MCP Baseline

| MCP | Location | Notes |
| --- | --- | --- |
| `context7` | `.codex/config.toml`, `.cursor/mcp.json` | Current library and API documentation. |
| `exa` | `.codex/config.toml`, `.cursor/mcp.json` | Web and academic search helper. |
| `firecrawl` | `.codex/config.toml`, `.cursor/mcp.json` | Page extraction; requires `FIRECRAWL_API_KEY`. |
| `sequential-thinking` | `.codex/config.toml`, `.cursor/mcp.json` | Optional reasoning helper. |

## Using This Profile

Checkout the branch and start Codex or Cursor from the repository root:

```bash
git checkout profile/paper-writing
```

For Codex, skills are available under `.agents/skills`. For Cursor, skills are
available under `.cursor/skills`.

## Repository Rules

- Do not commit local source-material directories, upstream `.git` metadata,
  credentials, `.DS_Store`, generated PDFs, or LaTeX auxiliary files.
- Keep profile branches focused: profile-specific skills and prompt indexes
  belong here; shared baseline configuration belongs on `main`.
- Preserve third-party license and provenance notes when copying skills.
