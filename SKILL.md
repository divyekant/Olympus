---
name: glbuilding
description: >-
  Use when an owner asks to onboard GLBuilding, activate orchestration, or run
  a project goal through its fixed role workflow.
---

# GLBuilding

GLBuilding is a fixed Markdown workflow. It adds no runtime, service, database, or project
dependency. Read the [runtime protocol](references/PROTOCOL.md) before routing work; load
only the charter needed for the next role.

## Activation

- `Use GLBuilding for: <goal>` runs one goal.
- `Activate GLBuilding orchestration` routes later project-changing requests in the current session.
- PROJECT boot mode `orchestration` routes project-changing requests in every session.
- `Deactivate GLBuilding orchestration` stops new routing in the current session.
- Questions do not create goals. An explicit read-only audit uses Explorer.

The [runtime protocol](references/PROTOCOL.md) defines the five fixed roles, goal flow,
handoffs, owner gates, states, activation rules, and Git workflow.

## Load on demand

- Configurer: [charter](agents/SYSTEM_CONFIGURER.md), [project template](templates/PROJECT.md), [bootstrap block](templates/BOOTSTRAP.md)
- Explorer: [charter](agents/EXPLORER.md)
- Builder: [charter](agents/BUILDER.md)
- Reviewer: [charter](agents/REVIEWER.md)
- Orchestrator: [task template](templates/TASK.md)
