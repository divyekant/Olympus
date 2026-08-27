---
name: olympus
description: >-
  Use when an owner asks to onboard Olympus, activate orchestration, or run
  a project goal through its fixed role workflow.
---

# Olympus

Olympus is a fixed Markdown workflow. It adds no runtime, service, database, or project
dependency. Read the [runtime protocol](references/PROTOCOL.md) before routing work; load
only the charter needed for the next role.

## Activation

- `Use Olympus for: <goal>` runs one goal.
- `Activate Olympus orchestration` routes later project-changing requests in the current session.
- PROJECT boot mode `orchestration` routes project-changing requests in every session.
- `Deactivate Olympus orchestration` stops new routing in the current session.
- Questions do not create goals. An explicit read-only audit uses Explorer.

The [runtime protocol](references/PROTOCOL.md) defines the fixed roles, goal flow,
handoffs, owner gates, states, activation rules, and Git workflow.

## Load on demand

- Configurer: [canonical guided onboarding contract](references/ONBOARDING.md), [charter](agents/SYSTEM_CONFIGURER.md), [project template](templates/PROJECT.md), [bootstrap block](templates/BOOTSTRAP.md)
- Explorer: [charter](agents/EXPLORER.md)
- Spec Writer: [charter](agents/SPEC_WRITER.md)
- Claims Reviewer: [charter](agents/CLAIMS_REVIEWER.md)
- Spec Reviewer: [charter](agents/SPEC_REVIEWER.md)
- Plan Writer: [charter](agents/PLAN_WRITER.md)
- Plan Verifier: [charter](agents/PLAN_VERIFIER.md)
- Builder: [charter](agents/BUILDER.md)
- Docs Writer: [charter](agents/DOCS_WRITER.md)
- Reviewer: [charter](agents/REVIEWER.md)
- Design Reviewer: [charter](agents/DESIGN_REVIEWER.md)
- Decision Council: [charter](agents/DECISION_COUNCIL.md)
- Liaison: [charter](agents/LIAISON.md)
- Orchestrator: [task template](templates/TASK.md)
