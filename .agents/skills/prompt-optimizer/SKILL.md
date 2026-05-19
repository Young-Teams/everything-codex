---
name: prompt-optimizer
description: >-
  Analyze raw prompts, identify intent and gaps, match Codex components
  (repo skills, Codex subagents, MCPs), and output a ready-to-paste optimized
  prompt. Advisory role only — never executes the task itself.
  TRIGGER when: user says "optimize prompt", "improve my prompt",
  "how to write a prompt for", "help me prompt", "rewrite this prompt",
  or explicitly asks to enhance prompt quality. Also triggers on Chinese
  equivalents: "优化prompt", "改进prompt", "怎么写prompt", "帮我优化这个指令".
  DO NOT TRIGGER when: user wants the task executed directly, or says
  "just do it" / "直接做". DO NOT TRIGGER when user says "优化代码",
  "优化性能", "optimize performance", "optimize this code" — those are
  refactoring/performance tasks, not prompt optimization.
origin: community
metadata:
  author: YannJY02
  version: "1.0.0"
---

# Prompt Optimizer

Analyze a draft prompt, critique it, match it to this Codex repo's available components,
and output a complete optimized prompt the user can paste and run.

## When to Use

- User says "optimize this prompt", "improve my prompt", "rewrite this prompt"
- User says "help me write a better prompt for..."
- User says "what's the best way to ask Codex to..."
- User says "优化prompt", "改进prompt", "怎么写prompt", "帮我优化这个指令"
- User pastes a draft prompt and asks for feedback or enhancement
- User says "I don't know how to prompt for this"
- User says "how should I use this Codex setup for..."
- User explicitly invokes `/prompt-optimize`

### Do Not Use When

- User wants the task done directly (just execute it)
- User says "优化代码", "优化性能", "optimize this code", "optimize performance" — these are refactoring tasks, not prompt optimization
- User is asking about Codex configuration or wants the task executed directly
- User says "just do it" or "直接做"

## How It Works

**Advisory only — do not execute the user's task.**

Do NOT write code, create files, run commands, or take any implementation
action. Your ONLY output is an analysis plus an optimized prompt.

If the user says "just do it", "直接做", or "don't optimize, just execute",
do not switch into implementation mode inside this skill. Tell the user this
skill only produces optimized prompts, and instruct them to make a normal
task request if they want execution instead.

Run this 6-phase pipeline sequentially. Present results using the Output Format below.

### Analysis Pipeline

### Phase 0: Project Detection

Before analyzing the prompt, detect the current project context:

1. Check if `.codex/AGENTS.md` or `AGENTS.md` exists in the working directory — read it for project conventions
2. Detect tech stack from project files:
   - `package.json` → Node.js / TypeScript / React / Next.js
   - `go.mod` → Go
   - `pyproject.toml` / `requirements.txt` → Python
   - `Cargo.toml` → Rust
   - `build.gradle` / `pom.xml` → Java / Kotlin (then check for `quarkus` in build file → Quarkus, or `spring-boot` → Spring Boot)
   - `Package.swift` → Swift
   - `Gemfile` → Ruby
   - `composer.json` → PHP
   - `*.csproj` / `*.sln` → .NET
   - `Makefile` / `CMakeLists.txt` → C / C++
   - `cpanfile` / `Makefile.PL` → Perl
3. Note detected tech stack for use in Phase 3 and Phase 4

If no project files are found (e.g., the prompt is abstract or for a new project),
skip detection and flag "tech stack unknown" in Phase 4.

### Phase 1: Intent Detection

Classify the user's task into one or more categories:

| Category | Signal Words | Example |
|----------|-------------|---------|
| New Feature | build, create, add, implement, 创建, 实现, 添加 | "Build a login page" |
| Bug Fix | fix, broken, not working, error, 修复, 报错 | "Fix the auth flow" |
| Refactor | refactor, clean up, restructure, 重构, 整理 | "Refactor the API layer" |
| Research | how to, what is, explore, investigate, 怎么, 如何 | "How to add SSO" |
| Testing | test, coverage, verify, 测试, 覆盖率 | "Add tests for the cart" |
| Review | review, audit, check, 审查, 检查 | "Review my PR" |
| Documentation | document, update docs, 文档 | "Update the API docs" |
| Infrastructure | deploy, CI, docker, database, 部署, 数据库 | "Set up CI/CD pipeline" |
| Design | design, architecture, plan, 设计, 架构 | "Design the data model" |

### Phase 2: Scope Assessment

If Phase 0 detected a project, use codebase size as a signal. Otherwise, estimate
from the prompt description alone and mark the estimate as uncertain.

| Scope | Heuristic | Orchestration |
|-------|-----------|---------------|
| TRIVIAL | Single file, < 50 lines | Direct execution |
| LOW | Single component or module | Single command or skill |
| MEDIUM | Multiple components, same domain | Plan, implement, review, verify |
| HIGH | Cross-domain, 5+ files | Planning pass first, then phased execution |
| EPIC | Multi-session, multi-PR, architectural shift | Multi-session plan with explicit phase gates |

### Phase 3: Codex Component Matching

Map intent + scope + tech stack (from Phase 0) to specific installed Codex components.

#### By Intent Type

| Intent | Skills | Codex subagents |
|--------|--------|-----------------|
| New Feature | agentic-engineering, coding-standards, python-patterns, python-testing | planner, code-architect, code-simplifier, code-reviewer |
| Bug Fix | agent-introspection-debugging, ai-regression-testing, python-testing | code-explorer, python-reviewer, code-reviewer |
| Refactor | coding-standards, python-patterns | code-explorer, code-simplifier, code-reviewer |
| Research | deep-research, literature-review, scholar-evaluation | docs-lookup |
| Testing | python-testing, ai-regression-testing | python-reviewer, code-reviewer |
| Review | coding-standards, agent-architecture-audit | code-reviewer, python-reviewer |
| Agent system design | agent-harness-construction, agent-architecture-audit, agent-eval | harness-optimizer, code-architect |
| Prompting | prompt-optimizer | planner |

#### By Tech Stack

| Tech Stack | Skills to Add | Codex subagent |
|------------|---------------|----------------|
| Python | python-patterns, python-testing, coding-standards | python-reviewer |
| AI agent / LLM app | agent-harness-construction, agent-architecture-audit, agent-introspection-debugging, agent-eval | harness-optimizer, code-architect |
| Research / papers | literature-review, scholar-evaluation, deep-research | docs-lookup |
| Other / Unlisted | coding-standards, ai-first-engineering | code-reviewer |

### Phase 4: Missing Context Detection

Scan the prompt for missing critical information. Check each item and mark
whether Phase 0 auto-detected it or the user must supply it:

- [ ] **Tech stack** — Detected in Phase 0, or must user specify?
- [ ] **Target scope** — Files, directories, or modules mentioned?
- [ ] **Acceptance criteria** — How to know the task is done?
- [ ] **Error handling** — Edge cases and failure modes addressed?
- [ ] **Security requirements** — Auth, input validation, secrets?
- [ ] **Testing expectations** — Unit, integration, E2E?
- [ ] **Performance constraints** — Load, latency, resource limits?
- [ ] **UI/UX requirements** — Design specs, responsive, a11y? (if frontend)
- [ ] **Database changes** — Schema, migrations, indexes? (if data layer)
- [ ] **Existing patterns** — Reference files or conventions to follow?
- [ ] **Scope boundaries** — What NOT to do?

**If 3+ critical items are missing**, ask the user up to 3 clarification
questions before generating the optimized prompt. Then incorporate the
answers into the optimized prompt.

### Phase 5: Workflow & Model Recommendation

Determine where this prompt sits in the development lifecycle:

```
Research → Plan → Implement → Review → Verify → Commit
```

For MEDIUM+ tasks, ask Codex to plan first, then implement in scoped phases. Do not reference slash commands unless they exist in this repo or the active Codex surface.

**Model recommendation** (include in output):

| Scope | Recommended Model | Rationale |
|-------|------------------|-----------|
| TRIVIAL-LOW | gpt-5.4-mini | Fast, cost-efficient for simple tasks |
| MEDIUM | gpt-5.4 | Strong default for standard coding and review |
| HIGH | gpt-5.5 for planning + gpt-5.4 for execution | Stronger reasoning for architecture, cheaper execution for scoped edits |
| EPIC | gpt-5.5 with phased checkpoints | Deep reasoning for multi-session planning |

**Multi-prompt splitting** (for HIGH/EPIC scope):

For tasks that exceed a single session, split into sequential prompts:
- Prompt 1: Research + plan with explicit assumptions and acceptance criteria
- Prompt 2-N: Implement one phase per prompt, each ending with concrete verification
- Final Prompt: Review changed files with code-reviewer/python-reviewer and run the relevant tests
- Preserve context in repo notes or README updates instead of relying on unavailable commands

---

## Output Format

Present your analysis in this exact structure. Respond in the same language
as the user's input.

### Section 1: Prompt Diagnosis

**Strengths:** List what the original prompt does well.

**Issues:**

| Issue | Impact | Suggested Fix |
|-------|--------|---------------|
| (problem) | (consequence) | (how to fix) |

**Needs Clarification:** Numbered list of questions the user should answer.
If Phase 0 auto-detected the answer, state it instead of asking.

### Section 2: Recommended Codex Components

| Type | Component | Purpose |
|------|-----------|---------|
| Skill | python-testing | Lightweight pytest and regression-test guidance |
| Skill | agent-harness-construction | Agent tool/action-space design guidance |
| Subagent | code-reviewer | Post-implementation review |
| Model | gpt-5.4 | Recommended for this scope |

### Section 3: Optimized Prompt — Full Version

Present the complete optimized prompt inside a single fenced code block.
The prompt must be self-contained and ready to copy-paste. Include:
- Clear task description with context
- Tech stack (detected or specified)
- skill and subagent usage at the right workflow stages
- Acceptance criteria
- Verification steps
- Scope boundaries (what NOT to do)

Only reference skills and subagents that exist in this repository unless you explicitly label a component as missing.

### Section 4: Optimized Prompt — Quick Version

A compact version for experienced Codex users. Vary by intent type:

| Intent | Quick Pattern |
|--------|--------------|
| New Feature | `Plan [feature], implement the smallest phase, then review with code-reviewer/python-reviewer and run tests.` |
| Bug Fix | `Write or identify a failing test for [bug], fix to green, then run targeted verification.` |
| Refactor | `Use code-explorer to map the area, code-simplifier for behavior-preserving cleanup, then code-reviewer.` |
| Research | `Use literature-review/deep-research for [topic], then synthesize evidence and gaps.` |
| Testing | `Use python-testing for [module], add regression coverage, then run pytest/ruff as available.` |
| Review | `Use code-reviewer and python-reviewer on the diff; focus on correctness, security, and missing tests.` |
| Agent system | `Use agent-harness-construction, then harness-optimizer or agent-architecture-audit.` |
| EPIC | `Break [objective] into phases with acceptance criteria and verification after each phase.` |

### Section 5: Enhancement Rationale

| Enhancement | Reason |
|-------------|--------|
| (what was added) | (why it matters) |

### Footer

> Not what you need? Tell me what to adjust, or make a normal task request
> if you want execution instead of prompt optimization.

---

## Examples

### Trigger Examples

- "Optimize this prompt for Codex"
- "Rewrite this prompt so Codex uses the right skills and subagents"
- "帮我优化这个指令"
- "How should I prompt Codex for this task?"

### Example 1: Vague Chinese Prompt (Project Detected)

**User input:**
```
帮我写一个用户登录页面
```

**Phase 0 detects:** `package.json` with Next.js 15, TypeScript, Tailwind CSS

**Optimized Prompt (Full):**
```
使用项目现有技术栈（Next.js 15 + TypeScript + Tailwind CSS）实现用户登录页面。

技术要求：
- 沿用项目现有的组件结构和路由约定
- 表单验证使用项目中已有的验证方案（检查是否已用 Zod/Yup/其他）
- 认证方式：沿用项目现有认证方案（如无，默认 JWT）
- 包含：邮箱/密码登录表单、表单验证、错误提示、加载状态、响应式布局

工作流：
1. 先让 planner/code-architect 规划组件结构和认证流程，参考现有页面的模式
2. 使用 python-testing 或项目现有测试约定，先写关键路径测试
3. 实现登录页面和认证逻辑
4. 使用 code-reviewer 审查实现
5. 运行项目已有 lint/test/build 命令，验证所有测试通过且页面正常渲染

安全要求：
- 密码不明文传输
- 防止暴力破解（rate limiting）
- XSS 防护
- CSRF token

验收标准：
- 所有测试通过，覆盖率 80%+
- 页面在移动端和桌面端正常渲染
- 登录成功跳转到 dashboard，失败显示错误信息

不要做：
- 不要实现注册页面
- 不要实现忘记密码功能
- 不要修改现有的路由结构
```

### Example 2: Moderate English Prompt

**User input:**
```
Add a REST API endpoint for user profile updates with validation
```

**Phase 0 detects:** `go.mod` with Go 1.22, Chi router

**Optimized Prompt (Full):**
```
Add a REST API endpoint for user profile updates (PATCH /api/users/:id).

Tech stack: Go 1.22 + Chi router (detected from project)

Requirements:
- PATCH /api/users/:id — partial update of user profile
- Input validation for fields: name, email, avatar_url, bio
- Auth: require valid token, users can only update own profile
- Return 200 with updated user on success
- Return 400 with validation errors on invalid input
- Return 401/403 for auth failures
- Follow existing API patterns in the codebase

Workflow:
1. Ask planner/code-architect to outline endpoint structure, middleware chain, and validation logic
2. Write table-driven tests for success, validation failure, auth failure, not-found
3. Implement following existing handler patterns
4. Review with code-reviewer
5. Run the full available test suite and confirm no regressions

Do not:
- Modify existing endpoints
- Change the database schema (use existing user table)
- Add new dependencies without checking existing ones first
```

### Example 3: EPIC Project

**User input:**
```
Migrate our monolith to microservices
```

**Optimized Prompt (Full):**
```
Plan in phases: "Migrate monolith to microservices architecture"

Before executing, answer these questions in the plan:
1. Which domain boundaries exist in the current monolith?
2. Which service should be extracted first (lowest coupling)?
3. Communication pattern: REST APIs, gRPC, or event-driven (Kafka/RabbitMQ)?
4. Database strategy: shared DB initially or database-per-service from start?
5. Deployment target: Kubernetes, Docker Compose, or serverless?

The plan should produce phases like:
- Phase 1: Identify service boundaries and create domain map
- Phase 2: Set up infrastructure (API gateway, service mesh, CI/CD per service)
- Phase 3: Extract first service (strangler fig pattern)
- Phase 4: Verify with integration tests, then extract next service
- Phase N: Decommission monolith

Each phase = 1 PR-sized change, with explicit verification between phases.
Preserve context in repo-tracked notes between phases.
Use git worktrees for parallel service extraction when dependencies allow.

Recommended: gpt-5.5 for planning, gpt-5.4 for scoped execution.
```

---

## Related Components

| Component | When to Reference |
|-----------|------------------|
| `agent-harness-construction` | Designing AI agent tools, action space, observations, and recovery |
| `agent-architecture-audit` | Auditing an LLM/agent application for wrapper, memory, tool, or retry issues |
| `agent-eval` | Comparing agents, prompts, or model configurations with reproducible tasks |
| `deep-research` | Current multi-source research with citations |
| `literature-review` | Academic or technical literature review workflow |
| `python-patterns` / `python-testing` | Python implementation and pytest guidance |
| `code-reviewer` / `python-reviewer` | Diff review after implementation |
