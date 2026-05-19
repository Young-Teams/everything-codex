@AGENTS.md

## Claude Code

- This file is the Claude Code entrypoint for the same shared guidance Codex
  reads from `AGENTS.md`.
- Keep Claude-specific notes here brief. Put shared behavior in `AGENTS.md` so
  Codex and Claude Code stay aligned.
- Use `main` only as the minimal shared baseline. Put workflow-specific skills,
  prompts, MCPs, and tool configuration on the relevant `profile/*` branch.
