---
name: github-collaboration
description: "Use when coordinating multi-person GitHub work: branch strategy, commit scope, PR creation or updates, review feedback, CI failures, merge/rebase choices, conflict resolution, fork/upstream sync, collaborative docs/content writing, and safe use of GitHub plugin tools, gh CLI, and local git."
---

# GitHub Collaboration

## Overview

Use this skill as the collaboration layer around GitHub work. It is not a replacement for local judgment: first understand the repo, branch, PR, and human collaboration state, then choose the smallest safe next action.

## Tool Choice

- Prefer the GitHub plugin connector for structured PR, issue, review, comment, label, reviewer, and commit status data.
- Use local `git` for worktree state, branch creation, diffs, staging, commits, rebases, merges, and conflict resolution.
- Use `gh` when the connector does not cover the job well: auth checks, current-branch PR discovery, Actions logs, fork/head edge cases, and command-line PR operations.
- Treat networked writes as explicit actions. Do not push, merge, post comments, request reviewers, update labels, resolve review threads, or publish PRs unless the user asked for that exact action or confirmed the target.

## First Pass

1. Resolve the repository, current branch, default/base branch, remotes, and whether a PR already exists.
2. Inspect local state before changing anything: modified files, staged files, untracked files, and commits ahead/behind the base branch.
3. Separate user or teammate changes from the requested scope. Never stage unrelated work silently.
4. Identify the collaboration mode: new work, publish a branch, update an existing PR, handle review feedback, debug CI, resolve conflicts, sync a fork, prepare release notes, or collaborate on docs/content.
5. State assumptions and blockers before changing shared state.

## Branch And Scope

- Prefer short-lived branches from the current default branch.
- Use branch names that describe ownership and intent: `feat/...`, `fix/...`, `docs/...`, `chore/...`, or `codex/...` for assistant-owned work when no repo convention exists.
- Keep PRs reviewable. If the diff spans unrelated behaviors or large unrelated files, recommend splitting before publishing.
- For shared branches, avoid rewriting history. Use merge or new commits unless the team has clearly chosen a rebase workflow.
- For private branches, rebase onto the base branch when it keeps history clearer. Use `--force-with-lease` only after confirming no one else depends on the branch.

## Commit Standard

- Make commits atomic: one logical change per commit.
- Prefer Conventional Commits when the repo has no stronger convention:
  - `feat`: new capability
  - `fix`: bug fix
  - `docs`: docs or authored content
  - `test`: tests
  - `refactor`: structure without behavior change
  - `chore`: maintenance
  - `ci`: CI or workflow changes
- Write commit subjects in imperative mood, under 72 characters, with no trailing period.
- Use the commit body for why the change exists, migration notes, risks, issue links, or conflict-resolution rationale.
- Add trailers only when useful: `Refs #123`, `Fixes #123`, or `Co-authored-by: Name <email>`.

## PR Standard

Before opening or updating a PR:

1. Compare against the intended base branch.
2. Summarize changed files by purpose, not by filename alone.
3. Run the most relevant local checks available for the touched surface.
4. Use the repo PR template if one exists.

If there is no template, use:

```markdown
## Summary

## Why

## Changes

## Testing

## Risks / Rollback

## Related Issues
```

Default to a draft PR when the change is still being shaped, CI is unknown, review scope is large, or the user has not explicitly asked for ready-for-review.

## Review Feedback

- Fetch PR metadata, diff, review submissions, comments, and thread state when available.
- Group feedback by behavior area or file.
- Separate actionable requests from questions, duplicates, stale comments, and already-resolved threads.
- Confirm which feedback cluster to address unless the user asked to handle all unresolved actionable comments.
- For explanation-only feedback, draft a reply instead of forcing a code change.
- Do not post replies, submit reviews, approve, request changes, or resolve threads without explicit approval.

## CI And Merge Readiness

When CI fails:

1. Read failing check names and logs, not just the red/green summary.
2. Classify the failure as real regression, flaky test, missing dependency, environment issue, or unrelated base-branch breakage.
3. Fix locally when the failure is in scope, then rerun the smallest meaningful check.
4. Record what was verified and what remains unverified.

A PR is merge-ready only when the intended scope is clear, CI and required checks pass or have documented exceptions, approvals are satisfied, unresolved conversations are handled, conflicts are gone, and release/docs impacts are covered.

## Conflict Resolution

1. Fetch the latest remote state before resolving.
2. Determine whether merge or rebase is appropriate:
   - Merge for shared branches or when preserving collaborative history matters.
   - Rebase for private branches when linear history is the team norm.
3. Resolve conflicts semantically, not by blindly choosing one side. Check nearby code/docs to preserve both intents where possible.
4. For content and documentation conflicts, preserve author voice and structure unless the user asked for an editorial rewrite.
5. After resolving, run relevant checks or preview affected docs/content.
6. Commit conflict resolutions with a clear message that names the base branch or PR being integrated.

## Collaborative Writing

For docs, articles, specs, README files, and other authored content:

- Treat GitHub as the source of truth for reviewable text changes.
- Keep editorial and code changes in separate commits when possible.
- Preserve existing tone, terminology, headings, links, and frontmatter unless the task is to change them.
- Use PR descriptions to explain editorial intent, affected audience, and review focus.
- For overlapping edits, prefer narrow patches and comments over broad rewrites.

## Output Expectations

End each GitHub collaboration task with:

- current branch or PR state
- actions taken or recommended
- files or review threads touched
- checks run and their result
- external actions still waiting on user approval
- the next safest collaboration step
