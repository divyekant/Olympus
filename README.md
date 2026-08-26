# GLBuilding

GLBuilding is a small, opinionated Markdown framework for reliable agent-led software
development.

It gives a coding agent one fixed orchestration graph, fourteen conditional roles, bounded
review, and Git-backed handoffs. It adds no runtime, service, database, package, or
scheduler.

## Why it exists

Long agent sessions lose scope on large codebases. They can mix discovery, implementation, and self-review in one context. GLBuilding separates those duties and carries only accepted evidence between fresh role sessions.

## The fixed system

- One repository-root Orchestrator owns routing and goal records.
- The System Configurer onboards the project and applies approved configuration changes.
- Explorers answer bounded repository questions without edits.
- Spec Writers, Claims Reviewers, and Spec Reviewers define and falsify substantial goals.
- Plan Writers and Plan Verifiers cover dependent or cross-layer implementation steps.
- Builders make the smallest approved project change.
- Docs Writers synchronize approved documentation when the contract requires it.
- Fresh Reviewers verify each mutation and return `pass`, `repair`, or `blocked`.
- Design Reviewers check material user-facing changes against project-provided standards.
- Decision Council gives read-only advice for unresolved material trade-offs.
- Liaisons answer human status and explanation requests from current evidence.
- Clean sequential goals can use branches. Concurrent goals use Git worktrees when their scopes do not overlap.

The [runtime protocol](references/PROTOCOL.md) defines the fixed order, triggers, packets,
and authority. Project owners can configure role preferences, tools, models, review rounds,
project instructions, activation mode, and matching standards. They cannot change role
duties, suppress triggers, enable peer communication, change graph ownership, or bypass
protected rules.

## Install

Give an agent the exact GLBuilding repository URL and immutable commit, then ask it to follow [the installation guide](docs/INSTALLATION.md).

Approved onboarding creates one local Git commit with only PROJECT and both loader files.
Remote persistence still needs fresh owner approval.

The target repository receives:

```text
AGENTS.md                         # stable Codex loader block
CLAUDE.md                         # stable Claude loader block
.glbuilding/PROJECT.md            # approved project configuration and framework pin
.glbuilding/tasks/<goal-id>.md    # one tracked record per goal
```

The framework stays outside the target repository and is resolved at the exact commit in `PROJECT.md`.

## Use

- One goal: `Use GLBuilding for: <goal>`
- This session: `Activate GLBuilding orchestration`
- Every session: choose `boot mode: orchestration` during onboarding
- Stop session routing: `Deactivate GLBuilding orchestration`

Project boot is routing authority, not a background process. Questions do not create goals.
Project-changing requests do.

## Read next

- [Vision](VISION.md)
- [Framework white paper and architecture](docs/WHITEPAPER.md)
- [Decision record](docs/DECISIONS.md)
- [Skill-to-charter distillation](docs/DISTILLATION.md)
- [Installation and onboarding](docs/INSTALLATION.md)
- [Conformance plan and evidence](docs/CONFORMANCE.md)
- [Roadmap](ROADMAP.md)

## Current status

The lean Markdown system now defines a fixed conditional 14-role catalog. Existing
harness evidence remains tied to the immutable commits listed in
[current harness evidence](docs/CONFORMANCE.md#current-harness-evidence); no 14-role
execution has been run. The representative large-codebase comparison failed; see that
evidence for the exact failure and limits.

No public release or release candidate is claimed. License, public URL, version, tag, and
release approval remain owner decisions.

## Enforcement limit

Markdown rules are behavioral controls. They are not a security sandbox. Host permissions, filesystem controls, Git review, and branch protection can add enforcement, but GLBuilding does not claim that enforcement itself.
