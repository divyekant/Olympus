---
name: glbuilding
description: >-
  Use when an owner asks to activate GLBuilding or run a project goal with
  scoped fresh-role orchestration in Codex or Claude.
---

# GLBuilding

GLBuilding is a fixed Markdown instruction pack. It has no runtime, service, or
self-modifying project machinery. Load the shared [runtime protocol](references/PROTOCOL.md)
before routing work. Load a role charter only when that role runs.

## Activation

- In `manual` boot mode, use one explicit goal invocation for one goal.
- In any session, `Activate GLBuilding orchestration` temporarily routes later
  project-changing requests until owner deactivation or session end.
- In `orchestration` boot mode, routing starts automatically in every session.
  Session deactivation is temporary; a persistent mode change uses the Configurer.
- `Deactivate GLBuilding orchestration` stops new routing only. It does not cancel an
  active goal.
- Casual questions do not create a graph. An explicit read-only audit may use an
  Explorer or Reviewer without mutation.
- The root Orchestrator is the repository hub and the sole semantic writer of
  `.glbuilding/tasks/<goal-id>.md`. It routes only the fixed roles.

## Fixed workflow

1. Use read-only checks to verify the pinned pack, project configuration, repository
   state, and expected delivery capabilities.
2. Route missing or changed configuration only to the [System Configurer](agents/SYSTEM_CONFIGURER.md).
3. Freeze the goal values for [templates/TASK.md](templates/TASK.md), including source,
   base, intended branch or worktree, capability envelope, and delivery boundary.
4. Perform required Git setup. On success, write the task record in the selected goal
   checkout. On failure, write a `blocked` record in the original checkout. Do either
   before any role or target-project mutation. Never downgrade the delivery boundary.
5. Use the [Explorer](agents/EXPLORER.md) only for required bounded repository questions.
6. For mutation, send the accepted task and evidence to the [Builder](agents/BUILDER.md).
7. After mutation, send the exact frozen diff to a fresh [Reviewer](agents/REVIEWER.md).
8. Repair actionable findings, then start a fresh review. Stop at the configured cap.
9. Record verification and one terminal status: `complete`, `blocked`, `failed`, or
   `cancelled`.

The protocol defines ownership, activation, Git, approval, persistence, capability,
and recovery rules. Roles cannot talk peer-to-peer, spawn agents, edit goal records,
change the graph, or modify this external pack. Only the System Configurer changes
`.glbuilding/PROJECT.md` and the two bootstrap sentinel blocks. Goal-required target-
project tooling can include scripts, dependencies, CLIs, and tests; keep GLBuilding
machinery out of target goals.

Ambient memory is read-only evidence during onboarding and goals. Do not create, update,
or delete it. Distillation or evolution requires a separate owner-approved Configurer
proposal.

## Load on demand

- Configurer: [charter](agents/SYSTEM_CONFIGURER.md), [project schema](templates/PROJECT.md),
  and [bootstrap block](templates/BOOTSTRAP.md)
- Explorer: [charter](agents/EXPLORER.md)
- Builder: [charter](agents/BUILDER.md)
- Reviewer: [charter](agents/REVIEWER.md)
- Orchestrator goal record: [task schema](templates/TASK.md)
