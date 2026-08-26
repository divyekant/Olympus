# GLBuilding decision record

## Decision method

The design was reviewed through a Council sequence:

1. An Architect drafted the smallest complete baseline.
2. A Skeptic challenged trust, concurrency, Git, and enforcement claims.
3. A User Advocate challenged onboarding, recovery, and daily cost.
4. A Pragmatist ran a three-month failure pre-mortem.
5. The Architect rebutted every challenge.
6. A neutral refiner produced the revised recommendation.
7. The deterministic resolver selected the revision because critical challenges existed.

The result is high-stakes because the challenges affected owner authority and the product's trust claims. The Council did not recommend a runtime.

## Accepted decisions

### D001 — Markdown-only kernel

GLBuilding contains instructions, role charters, templates, and documentation. It has no application runtime, service, database, queue, scheduler, or project package dependency.

### D002 — One repository-root Orchestrator

One root Orchestrator owns routing for a repository. It starts bounded child goal graphs. Independent root Orchestrators in the same repository are unsupported.

### D003 — Four fixed roles

The fixed roles are System Configurer, Explorer, Builder, and Reviewer. Owners can configure fixed slots. They cannot add roles, remove duties, change state transitions, or enable peer-to-peer control.

### D004 — Hub-only communication and record writes

Roles return structured results to the Orchestrator. They do not talk to each other. Only the Orchestrator accepts evidence and writes `.glbuilding/tasks/<goal-id>.md`.

### D005 — One canonical source pin

`.glbuilding/PROJECT.md` stores one owner-approved canonical repository URL and full immutable commit. Stable `AGENTS.md` and `CLAUDE.md` blocks read that value. Loaders also require a clean checkout. The pin provides identity and drift evidence, not trust authentication.

### D006 — Three activation paths, one protocol

Manual invocation runs one goal. Session activation routes later project-changing goals until deactivation or session end. Project boot routes them in every session. Deactivation stops new routing, not active goals. Questions do not start graphs. Explicit read-only audits are supported without mutation authority.

### D007 — Adaptive worktree isolation

A simple single goal can use a clean current checkout. Concurrent goals, relevant dirty state, or policy-required isolation use worktrees from committed bases. Worktrees do not replace orchestration ownership or semantic conflict checks.

### D008 — Per-goal frozen contract

Each goal freezes the framework commit, project configuration revision, committed base, goal identity, delivery boundary, and maximum capability envelope. Stage packets may narrow authority and add accepted evidence.

### D009 — Bounded review

Every mutation receives a fresh independent review. Explorer is conditional. Review and repair default to two rounds, allow one to three, and stop as `blocked` at the cap. Unknown evidence cannot produce `pass`.

### D010 — Git persistence has levels

Validated onboarding creates one local commit with only the approved configuration and
loader paths. Tracked local records then support local recovery. Cross-host recovery
requires an approved remote checkpoint or tested host persistence. GLBuilding does not
equate a local commit with cloud durability.

### D011 — Configuration uses double opt-in

The System Configurer derives values and presents one exact configuration and patch with
per-file hashes. One digest over a canonical, non-recursive manifest binds the attached
target ref, its HEAD, and those bytes.
The owner approves that identifier and digest. The Configurer then writes only the
approved project record and loader blocks, without adding post-approval metadata. The
harness transaction packet carries approval time and evidence. Configuration and
evolution changes apply only to new goals. An omitted or shortened artifact cannot be
approved; output limits block the proposal.

### D012 — Customization only narrows fixed slots

Custom instructions and evolutions are named, scoped additions or narrowings. The protected base wins. Ambiguity blocks. Sources are recorded for later re-mining but are not runtime dependencies.

### D013 — Project knowledge has three classes

Intent is approved direction. Map locates the system. Validation falsifies claims. Map and Validation are rechecked at the frozen source revision. Memory and ambient skills are evidence, not authority.

### D014 — Capabilities use semantic labels

Codex and Claude mappings describe outcomes, not tool names. Each capability is labeled `native-enforced`, `workflow-instructed`, or `unavailable`. Required unavailable capabilities block the current path.

### D015 — Behavioral limits are explicit

Protected Markdown is not a security sandbox. The framework does not claim that an instruction prevents a noncompliant agent or trusted repository writer from changing a file.

### D016 — Target-project machinery is allowed when the goal needs it

Builders can add project scripts, dependencies, command-line interfaces, and tests when acceptance requires them. They cannot add GLBuilding runtime machinery during a project goal.

### D017 — Codex first, Claude before release

Codex is the first dogfood harness. Claude must pass the same minimum semantic conformance cases before version-one release.

## Runtime-audit corrections

The Council shape passed a second adversarial runtime audit before implementation proof.
The baseline changed as follows:

- initial onboarding uses the owner-supplied URL and commit before installed loaders exist;
- cached framework checkouts must match origin and `HEAD` and have empty Git status;
- the Orchestrator can create branches and worktrees but cannot edit target code;
- read-only audits, repair return, retry records, takeover, and deactivation have explicit paths;
- active-root checks scan non-terminal task records and disclose the remaining start race;
- native host instruction precedence remains above the GLBuilding configuration layer;
- owner identity and approval are limited to the principal control that the harness proves;
- provider tool, model, and budget mappings freeze through one execution-profile digest;
- inactive manual sessions and fresh roles load only the files they need;
- duplicate protocol tables collapsed into PROJECT and one append-only task event log.
- approval hashes moved out of PROJECT to remove a self-referential postimage loop;
- the installation prompt suppresses unrelated ambient onboarding graphs when host
  precedence permits.

The audit did not justify a runtime, lease service, installer, or database.

## Safe defaults awaiting owner policy confirmation

These defaults let local baseline work continue without external authority. They remain explicit onboarding choices.

### O001 — External action authority

Safe default: every push, pull-request creation, merge, deploy, publish, force operation, secret change, remote deletion, or hard-to-reverse external effect needs fresh owner approval.

No standing preauthorization is included in the version-one baseline. This rule governs
runtime behavior until an owner-approved framework revision changes it; project custom
instructions cannot widen it.

### O002 — Delivery boundary

Onboarding creates one local configuration commit. Goals use one project default:
verified local change, committed goal branch, or an explicit remote outcome. A remote
boundary does not remove the fresh action approval requirement.

### O003 — Cross-host resume

Safe default: off. Enable only with an approved exact checkpoint destination or a tested persistent host workspace.

### O004 — Git requirement

Council recommendation: require an existing Git repository and a resolvable committed base in version one. Non-Git support is deferred.

### O005 — License and release authority

Select an open-source license before public release. Creating a public remote, tag, package, or release requires owner approval.

## Explicit deferrals

- Multi-repository orchestration.
- Multiple independent root Orchestrators per repository.
- Distributed locks.
- Cross-host checkpoint service.
- CLI installer.
- Background execution.
- Runtime graph engine.
- Extra role types.
- Automatic framework updates or self-modification.
- General graph configuration.
- Telemetry and dashboards.
- Non-Git projects.

## Rejected shapes

- One giant `AGENTS.md`: consumes context and duplicates detailed policy.
- One task file for all goals: conflicts under concurrency.
- One Orchestrator per goal: fragments repository authority.
- One worktree for every trivial goal: creates avoidable cleanup and integration cost.
- Three copied source pins: increases drift without adding trust.
- Peer-to-peer role communication: adds topology and state that the baseline does not need.
- A runtime for persistence: solves a future problem before the baseline proves it.
