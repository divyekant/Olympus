---
shaping: true
---

# Olympus vision

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

An owner points Codex or Claude at one installation guide and one Olympus repository URL, with an optional ref that defaults to `main` and resolves once to a recorded immutable commit. A System Configurer inspects the Git repository, derives the smallest useful configuration, and asks only questions that change owner intent or authority.

The owner approves one complete effective configuration and the proposed installation changes. The project then supports:

- one-off Olympus goals;
- session-wide orchestration;
- project-default orchestration;
- multiple non-overlapping goals, each in its own worktree by default;
- conditional specification, claims, planning, documentation, design, release, decision, and
  liaison contexts;
- owner-selected narrow workflows within fixed triggers, review gates, and owner gates;
- bounded discovery and build contexts, plus fresh review;
- bounded repair and evidence-backed completion.

The owner can adjust supported knobs inside fixed slots. The owner cannot change the
fifteen fixed role duties, hub communication, graph ownership, triggers, or protected
rules. The owner-selected workflow is an ordered allowlist, not a new graph. The
[runtime protocol](references/PROTOCOL.md) is the canonical catalog, graph, release
boundary, and workflow contract.

## Product principles

- Ready to use by default.
- Tweakable only inside named boundaries.
- Every configuration change uses double opt-in.
- One repository-root Orchestrator owns all goal graphs.
- Role sessions receive bounded inputs and return structured results to the Orchestrator.
- Every invoked role has explicit harness mapping and `supported`, `unsupported`, or
  `untested` evidence.
- Exploration is conditional. Fresh review is mandatory for mutations.
- Unknown evidence cannot pass review.
- Repair is bounded. Specification review permits at most ten completed rounds and expects
  closure in two or three. Other review brackets keep their smaller configured caps.
- Git stores configuration and goal records.
- Each goal runs in its own worktree by default; closure removes it only after merge,
  safe handoff, or explicit owner abandonment.
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

Olympus can dogfood after one target harness passes the simple contract. It must test each
invoked role through the harness, test Codex and Claude, and label unsupported modes
honestly. The original 14-role catalog began dogfood in the controlled Issue #750 A/B comparison;
not every conditional role has evidence. The earlier experimental version `0.3.0` strengthened
role craft and shared state after the Release Agent specification failed to converge. It exists
for larger tests, not to claim production readiness. The current private experimental `0.5.0`
scope has fifteen roles, including a provider-neutral Release Agent, owner-selected
workflow boundaries, compact guided onboarding with an express one-step path, and
worktree-per-goal isolation with closure. Claude has passed the guided onboarding
scenario only. Static contract evidence does not prove live provider support, release
execution, production readiness, or general harness support.

The result must reduce owner correction or elapsed delivery time without reducing correctness. If its administration costs more than the change, the framework has failed its purpose.
