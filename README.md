# everything-codex

Profile-based AI assistant configuration for Codex, Claude Code, and Cursor.
This repository uses long-lived branches as installable configuration profiles.

## Branches

| Branch | Purpose | Primary tools |
| --- | --- | --- |
| `main` | Shared instructions, Codex baseline, branch index, and notices. | Codex |
| `profile/ai-coding` | AI coding workflows based on reusable Superpowers skills. | Claude Code, Codex |
| `profile/paper-writing` | Research and paper-writing workflows, MCPs, and prompt index. | Cursor, Codex |
| `profile/fullstack-dev` | Reserved placeholder for a future full-stack profile. | TBD |

## Main Layout

```text
AGENTS.md             Shared assistant behavior guidance
CLAUDE.md             Claude Code entrypoint pointing at shared guidance
.codex/
  AGENTS.md           Codex project behavior rules
  config.toml         Codex runtime and MCP settings
THIRD_PARTY_NOTICES.md
```

## MCP Baseline

| MCP | Configured | Notes |
| --- | --- | --- |
| `context7` | yes | Uses `npx -y @upstash/context7-mcp@latest` for current docs. |
| `firecrawl` | yes | Requires `FIRECRAWL_API_KEY`. |
| `exa` | yes | Configured as `https://mcp.exa.ai/mcp`. |
| `sequential-thinking` | yes | Optional general reasoning helper. |

## Using A Profile

Checkout the branch that matches the workflow you want:

```bash
git checkout profile/ai-coding
git checkout profile/paper-writing
git checkout profile/fullstack-dev
```

Start the relevant assistant from the branch root so project-scoped config is
discovered.

## Repository Rules

- Do not commit upstream clone metadata, local source-material directories,
  credentials, `.DS_Store`, or generated paper artifacts.
- Keep hooks out of the profiles unless there is a concrete workflow need.
- Preserve third-party license and attribution notes when copying skills.
- Keep profile branches focused and reviewable.
