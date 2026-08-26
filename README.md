# GLBuilding

GLBuilding is a small, opinionated Markdown framework for reliable agent-led software development.

It gives a coding agent one fixed orchestration graph, five fixed roles, bounded review, and Git-backed handoffs. It adds no runtime, service, database, package, or scheduler.

## Why it exists

Long agent sessions lose scope on large codebases. They can mix discovery, implementation, and self-review in one context. GLBuilding separates those duties and carries only accepted evidence between fresh role sessions.

## The fixed system

- One repository-root Orchestrator owns routing and goal records.
- The System Configurer onboards the project and applies approved configuration changes.
- Explorers answer bounded repository questions without edits.
- Builders make the smallest approved project change.
- Fresh Reviewers verify each mutation and return `pass`, `repair`, or `blocked`.
- Clean sequential goals can use branches. Concurrent goals use Git worktrees when their scopes do not overlap.

Project owners can configure fixed slots, tools, models, review rounds, project instructions, and activation mode. They cannot change the five role duties, agent communication, graph ownership, or protected rules.

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

Project boot is routing authority, not a background process. Questions do not create graphs. Project-changing goals do.

## Read next

- [Vision](VISION.md)
- [Framework white paper and architecture](docs/WHITEPAPER.md)
- [Decision record](docs/DECISIONS.md)
- [Skill-to-charter distillation](docs/DISTILLATION.md)
- [Installation and onboarding](docs/INSTALLATION.md)
- [Conformance plan and evidence](docs/CONFORMANCE.md)
- [Roadmap](ROADMAP.md)

## Current status

The lean Markdown baseline is under construction. Codex and Claude are target harnesses,
not confirmed supported harnesses. No public release is claimed yet.

## Enforcement limit

Markdown rules are behavioral controls. They are not a security sandbox. Host permissions, filesystem controls, Git review, and branch protection can add enforcement, but GLBuilding does not claim that enforcement itself.
