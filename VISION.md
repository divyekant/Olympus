---
shaping: true
---

# GLBuilding vision

## Source

> “Basically i want to build a full graph/Loop system which can be used in any project for building.”

> “it should be ready to use but tweakable.”

> “Double opt in.”

> “The main and only aim of this project is to ensure faster and correct building.”

> “Its just a set of MD files in my opinion and nothing more.”

## Vision

Make agent-led software development faster and more correct on codebases where one long model session loses scope or invents context.

Give project owners a ready-to-use build system. Do not require them to design, route, or maintain an agent architecture.

## End state

An owner points Codex or Claude at one installation guide and one exact GLBuilding commit. A System Configurer inspects the Git repository, derives the smallest useful configuration, and asks only questions that change owner intent or authority.

The owner approves one exact effective configuration and one exact installation patch. The project then supports:

- one-off GLBuilding goals;
- session-wide orchestration;
- project-default orchestration;
- multiple non-overlapping goals in isolated worktrees;
- fresh discovery, implementation, and review contexts;
- bounded repair and evidence-backed completion.

The owner can adjust supported knobs inside fixed slots. The owner cannot change the four roles, their duties, hub communication, graph ownership, or protected state transitions.

## Product principles

- Ready to use by default.
- Tweakable only inside named boundaries.
- Every configuration change uses double opt-in.
- One repository-root Orchestrator owns all goal graphs.
- Role sessions receive bounded inputs and return structured results.
- Exploration is conditional. Fresh review is mandatory for mutations.
- Unknown evidence cannot pass review.
- Repair is bounded. The default cap is two rounds.
- Git stores configuration and goal records.
- Worktrees isolate concurrent or dirty work when needed.
- Exact pins identify framework content. They do not prove trust.
- Markdown protection is behavioral unless the host adds enforcement.
- Framework changes never alter an active goal.
- New machinery requires observed evidence that Markdown and native Git are insufficient.

## Not the goal

- A blank agent toolkit.
- A general graph language.
- A background worker or autonomous daemon.
- A server, database, queue, dashboard, or scheduler.
- An npm, Python, or binary project dependency.
- Automatic self-modification or automatic framework updates.
- Multi-repository orchestration in version one.
- A new test framework.

## Success

An owner completes onboarding, starts a real goal, receives a verified result, and does not route agents manually.

GLBuilding must prove the same semantic contract on Codex and Claude. It must then dogfood itself and complete a representative task in a larger codebase before its first public release.

The result must reduce owner correction or elapsed delivery time without reducing correctness. If its administration costs more than the change, the framework has failed its purpose.
