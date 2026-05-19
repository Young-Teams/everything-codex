# everything-codex: AI Coding Profile

AI coding workflow profile for Claude Code and Codex. It combines the shared
Codex baseline from `main` with selected reusable Superpowers development
skills.

## Layout

```text
AGENTS.md             Shared assistant behavior guidance
CLAUDE.md             Claude Code entrypoint
.codex/
  config.toml         Codex model and MCP configuration from main
.agents/
  skills/*/SKILL.md   Codex-visible skills
.claude/
  skills/*/SKILL.md   Claude Code-visible skills
THIRD_PARTY_NOTICES.md
LICENSES/
```

## Included AI Coding Skills

Selected from Superpowers:

- `brainstorming`
- `writing-plans`
- `test-driven-development`
- `systematic-debugging`
- `subagent-driven-development`
- `dispatching-parallel-agents`
- `executing-plans`
- `requesting-code-review`
- `receiving-code-review`
- `using-git-worktrees`
- `finishing-a-development-branch`
- `verification-before-completion`

Hooks and non-Superpowers skills are intentionally excluded from this profile.

## MCP Baseline

| MCP | Configured | Notes |
| --- | --- | --- |
| `context7` | yes | Uses `npx -y @upstash/context7-mcp@latest` for current docs. |
| `firecrawl` | yes | Requires `FIRECRAWL_API_KEY`. |
| `exa` | yes | Configured as `https://mcp.exa.ai/mcp`. |
| `sequential-thinking` | yes | Optional reasoning helper. |

## Using This Profile

Checkout this branch in the target project or clone:

```bash
git checkout profile/ai-coding
```

Start Claude Code or Codex from the branch root so project-scoped config and
skills are discovered.

## Repository Rules

- Do not commit upstream clone metadata, local source-material directories,
  credentials, `.DS_Store`, or generated paper artifacts.
- Keep hooks out of the profiles unless there is a concrete workflow need.
- Preserve third-party license and attribution notes when copying skills.
- Keep profile branches focused and reviewable.
