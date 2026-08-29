# Olympus

Olympus is an opinionated, Markdown-only build system for reliable agent-led software
development. Version `0.4.0` is a private experimental feature release.

It gives a coding agent one fixed orchestration graph, fifteen conditional roles, bounded
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
- The Release Agent prepares or reconciles one owner-requested release action. Execution
  needs separate owner approval; the role has no file or standing external authority.
- Decision Council gives read-only advice for unresolved material trade-offs.
- Liaisons answer human status and explanation requests from current evidence.
- Clean sequential goals can use branches. Concurrent goals use Git worktrees when their scopes do not overlap.

The [runtime protocol](references/PROTOCOL.md) defines the fixed order, triggers, packets,
and authority. Project owners can configure role preferences, tools, models, review rounds,
project instructions, activation mode, and matching standards. They cannot change role
duties, suppress triggers, enable peer communication, change graph ownership, or bypass
protected rules. An owner may provide one ordered role allowlist and one request boundary;
fixed triggers, paired checks, owner gates, and sole-hub routing remain mandatory. The
[release boundary](references/PROTOCOL.md#release-boundary) and
[owner-selected workflow](references/PROTOCOL.md#owner-selected-workflow) are canonical
protocol sections.

## Install

Give an authorized agent `https://github.com/divyekant/Olympus` and an immutable commit,
then ask it to follow [the installation guide](docs/INSTALLATION.md).

Approved onboarding creates one local Git commit with only PROJECT and both loader files.
Remote persistence still needs fresh owner approval.

The [guided onboarding contract](references/ONBOARDING.md) defines the inspect-first
conversation, the compact proposal, full exact detail on request before approval, the
second opt-in, six local stages, and truthful reports. Plain text retains all required
meaning.

Every wake and activation request first runs the [canonical activation preflight](references/PROTOCOL.md#canonical-activation-preflight)
against the target repository. Missing state enters guided onboarding; partial, malformed,
or changed state stops; complete state permits the requested activation route only after an
unchanged immediate recheck.

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
- Guided entry: `Awaken Olympus` opens onboarding or reports readiness; it never activates a session.
- Stop session routing: `Deactivate Olympus orchestration`

Each entry runs the canonical preflight before routing. Project boot is routing authority, not
a background process. Questions do not create goals. Project-changing requests do.

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

Olympus `0.4.0` adds a provider-neutral Release Agent and owner-selected custom workflow
boundaries within the fixed graph. The Release Agent prepares or reconciles one owner-requested
release action; execution needs separate owner approval, and the role has no standing file or
external authority.

The release boundary and custom workflow are static Markdown contracts. The V1–V12 fixtures
provide bounded checks, not live provider or release results. The focused C19 dogfood fixture
run passed 142/142 rows across Olympus and unrelated targets, but this remains bounded
Markdown-contract evidence. These results do not prove live provider support, release
execution, production readiness, or general harness support. Lower-model equivalence remains
untested. See
[current harness evidence](docs/CONFORMANCE.md#current-harness-evidence) for exact limits.

Olympus remains a private experimental `0.x` project. Existing dogfood shows mixed results
and does not prove quality superiority or production readiness. Public visibility starts
only with owner approval for version `1.0.0`.

## License

Apache-2.0. See [LICENSE](LICENSE).

## Enforcement limit

Markdown rules are behavioral controls. They are not a security sandbox. Host permissions, filesystem controls, Git review, and branch protection can add enforcement, but Olympus does not claim that enforcement itself.
