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

- Every manual-goal, session, project-boot, or guided wake entry first runs the [canonical activation preflight](references/PROTOCOL.md#canonical-activation-preflight) and its immediate final recheck against the target repository root. No entry creates a goal, routes later requests, or reports Olympus as active before an unchanged complete result authorizes it.
- `Use Olympus for: <goal>` runs one goal only after an unchanged complete preflight state.
- `Activate Olympus orchestration` routes later project-changing requests in the current session only after an unchanged complete preflight state.
- PROJECT boot mode `orchestration` routes project-changing requests in every session only after an unchanged complete preflight state.
- `Awaken Olympus` or `Awaken Olympus.` is the guided entry phrase. It is never a session-activation alias.
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
- Tester: [charter](agents/TESTER.md)
- Docs Writer: [charter](agents/DOCS_WRITER.md)
- Reviewer: [charter](agents/REVIEWER.md)
- Design Reviewer: [charter](agents/DESIGN_REVIEWER.md)
- Release Agent: [charter](agents/RELEASE_AGENT.md)
- Decision Council: [charter](agents/DECISION_COUNCIL.md)
- Liaison: [charter](agents/LIAISON.md)
- Orchestrator: [task template](templates/TASK.md)
