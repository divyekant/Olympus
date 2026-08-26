---
name: glbuilding
description: >-
  Use when an owner asks to onboard GLBuilding, activate orchestration, or run
  a project goal through its fixed role workflow.
---

# GLBuilding

GLBuilding is a fixed Markdown workflow. It adds no runtime, service, database,
or project dependency. Read the [runtime protocol](references/PROTOCOL.md) before
routing work. Load a role charter only when that role runs.

## Activation

- `Use GLBuilding for: <goal>` runs one goal.
- `Activate GLBuilding orchestration` routes later project-changing requests in
  the current session.
- Project boot mode `orchestration` routes project-changing requests in every session.
- `Deactivate GLBuilding orchestration` stops new routing in the current session.
- Questions do not create goals. An explicit read-only audit can use Explorer.

## Fixed workflow

1. Read `.glbuilding/PROJECT.md`. Confirm the framework pin, project rules, and boot mode.
2. Create one simple task record from [templates/TASK.md](templates/TASK.md). Record the
   goal, acceptance criteria, scope, base, and branch or worktree decision.
3. Use [Explorer](agents/EXPLORER.md) only for a material question that blocks the build.
4. Give a bounded packet to a separate [Builder](agents/BUILDER.md). The Builder makes
   the smallest in-scope change and runs the relevant checks.
5. Give the goal, exact diff, and check results to a fresh
   [Reviewer](agents/REVIEWER.md). The Reviewer returns `pass`, `repair`, or `blocked`.
6. If repair is required, return the findings to Builder. Stop at the configured cap.
7. Verify the accepted result, update the task record, and use normal project Git policy
   for a local commit.
8. Ask the owner before a major scope or architecture choice, or any remote, destructive,
   irreversible, secret, publish, merge, or deploy action.

The five roles are Orchestrator, System Configurer, Explorer, Builder, and Reviewer.
The Orchestrator is the hub. Other roles return bounded packets to it and do not control
each other. Only [System Configurer](agents/SYSTEM_CONFIGURER.md) changes PROJECT or the
managed loader blocks.

Ambient skills, project instructions, documentation, and memory can supply context.
They do not change the fixed role duties or owner approval boundary.

## Load on demand

- Configurer: [charter](agents/SYSTEM_CONFIGURER.md),
  [project template](templates/PROJECT.md), and [bootstrap block](templates/BOOTSTRAP.md)
- Explorer: [charter](agents/EXPLORER.md)
- Builder: [charter](agents/BUILDER.md)
- Reviewer: [charter](agents/REVIEWER.md)
- Orchestrator: [task template](templates/TASK.md)
