# Olympus decision record

The initial Council review covered architecture, trust, onboarding, and failure modes.
The owner reset version one to its product goal: faster, correct software building.

## Accepted decisions

| ID | Decision | Meaning and boundary |
| --- | --- | --- |
| D001 | Markdown-only framework | Instructions, charters, templates, and docs only. No runtime, service, database, scheduler, queue, or project package dependency. |
| D002 | Five-role baseline (superseded) | The original baseline roles were Orchestrator, System Configurer, Explorer, Builder, and Reviewer. D018 replaces this catalog while retaining the baseline authority and review boundaries. |
| D003 | Hub-only communication | The Orchestrator routes work and owns task records. Workers return bounded packets to it and do not talk to each other or change the graph. |
| D004 | Configuration uses double opt-in | The owner requests onboarding or a change. The Configurer shows the complete effective configuration and exact affected file changes. Only explicit approval of that proposal permits the write. |
| D005 | One source pin | PROJECT stores one repository URL and full immutable commit. The source may advance, but the pin identifies content, not authentication. Resolve it in a clean checkout or cache, not from a mismatched source working tree. |
| D006 | Three activation paths, one goal flow | Manual runs one goal. Session activation routes project changes until deactivation or session end. Project boot routes them in every session. Questions do not create goals. |
| D007 | Project knowledge is explicit | PROJECT stores owner Intent plus Map and Validation hints. Agents check hints against current code and record missing or stale documentation. PROJECT and current repository evidence remain sources of truth; ambient setup cannot change fixed duties or owner authority. |
| D008 | One simple record per goal | Record the request, criteria, paths, source base, isolation, owner decisions, role results, checks, and outcome. Whole conversations, transcript proof, cryptographic manifests, and telemetry are not task state. |
| D009 | Explorer and worktrees are conditional | Use Explorer only for a material repository question. Use a current checkout or branch for clean sequential work, and a worktree for concurrent or unrelated dirty work. Commit or explicitly include relevant dirty work; serialize overlap. |
| D010 | Fresh review is mandatory and bounded | Every mutation gets a Reviewer that did not build it. It checks every criterion and returns `pass`, `repair`, or `blocked`. The cap is one to three rounds, default two; open findings at the cap stop the goal. |
| D011 | Use normal Git | Use project named-path staging, hooks, and local commit policy. Do not reimplement commits, freeze identity, or claim cross-host durability from a local commit. |
| D012 | Major and external actions go to the owner | Routine approved local work is allowed. Major scope or architecture choices and every push, pull request, merge, deploy, publish, release, force operation, secret change, remote deletion, destructive effect, paid service, or hard-to-reverse effect need fresh owner approval. Configuration cannot preauthorize them. |
| D013 | Harness failure is a support result | Codex and Claude are target harnesses. A mutation harness must preserve separate Builder and fresh Reviewer roles. A harness that cannot follow the Markdown contract is `unsupported`; do not add obedience machinery. |
| D014 | Charters are distilled, not linked | Charters are derived from useful skills and experience, not loaded as runtime dependencies. Source changes have no automatic effect; an owner-approved Configurer proposal is required for a new charter revision. |
| D015 | One repository can hold several goals | One Orchestrator can route non-overlapping goals, each with its own record and isolation when needed. Multi-repository orchestration is deferred. |
| D016 | Target substantial software goals | Separate contexts and fresh review are for goals where codebase scope, context loss, or risk justifies them. Small tasks can test conformance; their elapsed time does not measure product speed. |
| D017 | Evidence gates claims and maturity | A simple conformance pass does not prove product value. Failed or tied comparisons remain visible product findings. A controlled no-defect comparison can support an experimental release for larger tests, but it cannot support a superiority or production-readiness claim. |
| D018 | Fixed conditional 14-role catalog | The catalog and order are Orchestrator, System Configurer, Explorer, Spec Writer, Claims Reviewer, Spec Reviewer, Plan Writer, Plan Verifier, Builder, Docs Writer, Reviewer, Design Reviewer, Decision Council, and Liaison. Protocol triggers determine invocation. The Orchestrator remains the sole hub; paired verification, fresh review, owner gates, and protected authority remain fixed. |
| D019 | Olympus product identity | The framework is Olympus. Its fixed collection of specialized roles is the Pantheon. Project paths, records, loader markers, commands, and documentation use the Olympus name. |
| D020 | Experimental version 0.1.0 | The Issue #750 A/B result is enough to start larger experiments. Version `0.1.0` makes no production-readiness or quality-superiority claim. |
| D021 | Apache-2.0 license | Olympus uses Apache-2.0. It is permissive and includes an explicit contributor patent grant. |
| D022 | Private incubation through 0.x | The canonical repository is `https://github.com/divyekant/Olympus`. Keep it private through experimental `0.x` releases. Make it public only with owner approval for version `1.0.0`. |

## Removed hardening rationale

Early trials exposed instruction and delivery failures, so the project briefly added
proposal hashes, custom Git transactions, identity freezing, transcript provenance, and
exhaustive recovery cases. They increased ceremony without improving product delivery.
Version one removes them and keeps four useful lessons:

1. show the complete configuration and affected files before approval;
2. stage named paths and preserve unrelated owner work;
3. require a real fresh review with acceptance evidence;
4. label a noncompliant harness `unsupported`.

Git history preserves the detailed experiments as rationale, not runtime rules.

## Release visibility

- Keep the canonical repository private through `0.x`.
- Public visibility starts only with explicit owner approval for `1.0.0`.

## Explicit deferrals

- Multi-repository orchestration and multiple independent root Orchestrators in one repository.
- Distributed locks and cross-host checkpoint services.
- CLI installer and background execution.
- Runtime graph engine or graph configuration language.
- Automatic self-evolution.
- Cryptographic proposal manifests and transcript provenance.
- Custom Git transaction or recovery machinery.
- Telemetry, analytics, dashboards, and non-Git projects.
