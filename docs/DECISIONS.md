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
| D009 | Explorer is conditional; isolation superseded | Use Explorer only for a material repository question. The original conditional-worktree rule is superseded by D030: each goal defaults to its own worktree. Commit or explicitly include relevant dirty work; serialize overlap. |
| D010 | Fresh review is mandatory and bounded | Every mutation gets a Reviewer that did not build it. It checks every criterion and returns `pass`, `repair`, or `blocked`. The cap is one to three rounds, default two; open findings at the cap stop the goal. |
| D011 | Use normal Git with exact review identity | Use project named-path staging, hooks, and local commit policy. Record the exact specification, plan, diff, and commit identity needed for review. If the unit changes, invalidate the pass and review the new unit. Do not replace Git with custom transaction machinery or claim cross-host durability from a local commit. |
| D012 | Major and external actions go to the owner | Routine approved local work is allowed. Major scope or architecture choices and every push, pull request, merge, deploy, publish, release, force operation, secret change, remote deletion, destructive effect, paid service, or hard-to-reverse effect need fresh owner approval. Configuration cannot preauthorize them. |
| D013 | Harness failure is a support result | Codex and Claude are target harnesses. A mutation harness must preserve separate Builder and fresh Reviewer roles. A harness that cannot follow the Markdown contract is `unsupported`; do not add obedience machinery. |
| D014 | Charters are distilled, not linked | Charters are derived from useful skills and experience, not loaded as runtime dependencies. Source changes have no automatic effect; an owner-approved Configurer proposal is required for a new charter revision. |
| D015 | One repository can hold several goals | One Orchestrator can route non-overlapping goals, each with its own record and isolation when needed. Multi-repository orchestration is deferred. |
| D016 | Target substantial software goals | Separate contexts and fresh review are for goals where codebase scope, context loss, or risk justifies them. Small tasks can test conformance; their elapsed time does not measure product speed. |
| D017 | Evidence gates claims and maturity | A simple conformance pass does not prove product value. Failed or tied comparisons remain visible product findings. A controlled no-defect comparison can support an experimental release for larger tests, but it cannot support a superiority or production-readiness claim. |
| D018 (superseded) | Fixed conditional 14-role catalog | Historical catalog and order were Orchestrator, System Configurer, Explorer, Spec Writer, Claims Reviewer, Spec Reviewer, Plan Writer, Plan Verifier, Builder, Docs Writer, Reviewer, Design Reviewer, Decision Council, and Liaison. The current [15-role catalog](../references/PROTOCOL.md#1-fixed-catalog) supersedes this decision while retaining the sole hub, paired verification, fresh review, owner gates, and protected authority. |
| D019 | Olympus product identity | The framework is Olympus. Its fixed collection of specialized roles is the Pantheon. Project paths, records, loader markers, commands, and documentation use the Olympus name. |
| D020 | Experimental version 0.1.0 | The Issue #750 A/B result is enough to start larger experiments. Version `0.1.0` makes no production-readiness or quality-superiority claim. |
| D021 | Apache-2.0 license | Olympus uses Apache-2.0. It is permissive and includes an explicit contributor patent grant. |
| D022 | Private incubation through 0.x | The canonical repository is `https://github.com/divyekant/Olympus`. Keep it private through experimental `0.x` releases. Make it public only with owner approval for version `1.0.0`. |
| D023 | v0.1 core changes stay outside Olympus | Implement and review core-framework changes through the normal repository workflow. An enhancement needs concrete dogfood evidence, then a new isolated dogfood run at the changed immutable commit. Each run is scenario evidence only; one scenario cannot establish general support or production readiness. External actions and protected repository controls do not change. |
| D024 | Specification handoffs are hash-checked | Persist one complete Writer body before two fresh reviewers receive it. Each reviewer recomputes the body hash and stops on a mismatch; a defective handoff consumes no round and stays recorded. The hash is an integrity checksum, not an authority proof or proposal manifest. The earlier acknowledgement handshake and round reservation were removed as message overhead without a defect they prevented. |
| D025 | Fixed roles need operational craft | Each role charter defines a narrow jurisdiction, bounded input, evidence method, readiness check, complete return packet, and stop boundary. Shared protocol remains canonical; charters add role-specific craft instead of copying workflow rules. |
| D026 | Attempts and review units have explicit state | Count a specification round only after both complete reviewer packets return. Preserve provisional findings from halted attempts, allow one fresh retry, and invalidate any passed specification, plan, or mutation unit that later changes. |
| D027 | Provider-neutral Release Agent boundary | The current 15-role catalog includes a Release Agent for owner-requested preparation, remote reconciliation, or one release-boundary action. The [release boundary](../references/PROTOCOL.md#release-boundary) keeps preparation separate from execution, requires one exact single-use owner approval per action kind and target, gives the role no file or standing external authority, and permits at most one provider action submission per approval. Read-only provider evidence calls do not consume that allowance. The contract does not claim live provider or production support. The original byte-canonical request format, hex owner rendering, dual clock samples, and consumption ledger were removed as behavioral theater: Markdown cannot enforce them, and the simple gate preserves the same owner authority. |
| D028 | Owner-selected narrow workflow | An owner may provide at most one ordered role allowlist and one request boundary. The [owner-selected workflow](../references/PROTOCOL.md#owner-selected-workflow) defines five exhaustive boundaries, invalid declarations, default routing, trigger closure, pending expansion, explicit cancellation, and mandatory fixed gates. A selection is not a new graph or an invocation list, and invalid input dispatches no worker. |
| D029 | Ref request, resolved pin | The owner requests a URL plus an optional branch, tag, or commit; the ref defaults to `main`. Onboarding resolves the ref once to a full immutable commit and PROJECT records only that commit. Sessions load the pin; upgrades are an explicit Configurer repin. The owner never has to type a commit; the system still never follows a moving ref. |
| D030 | Worktree per goal with closure | Each goal defaults to one worktree from the committed working-directory HEAD, so the owner's checkout is never edited and parallel goals are natural. Goal closure records the branch disposition and removes the worktree; unmerged work is never deleted. Project policy may permit current-checkout goals. |
| D031 | Express onboarding and affirmative approval | The exact request sentence `Defaults pre-approved.` is the second opt-in given in advance, valid only for a pure-defaults, conflict-free proposal on the three named paths; any deviation falls back to the gated flow. An unchanged proposal also accepts a clear, unconditional affirmative; a question or conditional reply never approves. Byte-exact approval phrasing was dropped as ceremony without a defect it prevented. |

## Removed hardening rationale

Early trials exposed instruction and delivery failures, so the project briefly added
proposal manifests, custom Git transactions, transcript provenance, and
exhaustive recovery cases. They increased ceremony without improving product delivery.
Version one removes them and keeps four useful lessons:

1. show the complete configuration and affected files before approval;
2. stage named paths and preserve unrelated owner work;
3. require a real fresh review of an exact, unchanged unit with acceptance evidence;
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
