# Olympus

Olympus is an opinionated, Markdown-only build system for reliable agent-led software
development. Version `0.1.0` is experimental.

It gives a coding agent one fixed orchestration graph, fourteen conditional roles, bounded
review, and Git-backed handoffs. The fixed role catalog is the **Pantheon**. Olympus adds
no runtime, service, database, package, or scheduler.

## Why it exists

Long agent sessions lose scope on large codebases. They can mix discovery, implementation, and self-review in one context. Olympus separates those duties and carries only accepted evidence between fresh role sessions.

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

Give an authorized agent `https://github.com/divyekant/Olympus` and an immutable commit,
then ask it to follow [the installation guide](docs/INSTALLATION.md).

Approved onboarding creates one local Git commit with only PROJECT and both loader files.
Remote persistence still needs fresh owner approval.

The [guided onboarding contract](references/ONBOARDING.md) defines the inspect-first
conversation, complete proposal, second opt-in, six local stages, and truthful reports.

The target repository receives:

```text
AGENTS.md                         # stable Codex loader block
CLAUDE.md                         # stable Claude loader block
.olympus/PROJECT.md               # approved project configuration and framework pin
.olympus/tasks/<goal-id>.md       # one tracked record per goal
```

The framework stays outside the target repository and is resolved at the exact commit in `PROJECT.md`.

## Use

- One goal: `Use Olympus for: <goal>`
- This session: `Activate Olympus orchestration`
- Every session: choose `boot mode: orchestration` during onboarding
- Stop session routing: `Deactivate Olympus orchestration`

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
- [Changelog](CHANGELOG.md)

## Version status

Olympus `0.1.0` is the first experimental version. A controlled FPLGuru Issue #750 A/B
test found no P0-P2 defect in either the normal Codex or Olympus implementation. Olympus
produced broader focused-test evidence and caught an order-dependent combined-test problem;
normal Codex used less process. The result was a correctness tie, not proof of superiority.

This version exists so owners can run larger experiments. See
[current harness evidence](docs/CONFORMANCE.md#current-harness-evidence) for exact limits.
Version `0.1.0` is ready for a private tagged release. Keep the repository private through
the experimental `0.x` line. Public visibility starts only with owner approval for version
`1.0.0`.

## License

Apache-2.0. See [LICENSE](LICENSE).

## Enforcement limit

Markdown rules are behavioral controls. They are not a security sandbox. Host permissions, filesystem controls, Git review, and branch protection can add enforcement, but Olympus does not claim that enforcement itself.
