# GLBuilding decision record

## Decision method

The initial design used a Council sequence:

1. an Architect proposed the smallest complete system;
2. a Skeptic challenged trust, concurrency, and enforcement claims;
3. a User Advocate challenged onboarding cost and daily use;
4. a Pragmatist ran a failure pre-mortem;
5. a neutral refiner resolved the critical challenges.

The Council supported a Markdown-only system. Later harness trials pushed the design
toward proof and recovery machinery. The owner then reset version one to its product
goal: faster, correct software building.

## Accepted decisions

### D001 — Markdown-only framework

GLBuilding contains instructions, role charters, templates, and documentation. It has no
application runtime, service, database, scheduler, queue, or project package dependency.

### D002 — Five fixed roles

The roles are Orchestrator, System Configurer, Explorer, Builder, and Reviewer. Owners
can select models, tools, limits, and named instruction additions inside fixed slots.
They cannot add roles, remove duties, change hub ownership, or bypass fresh review.

### D003 — Hub-only communication

The Orchestrator routes work and owns task records. Worker roles return bounded packets
to it. They do not talk to each other or change the graph.

### D004 — Configuration uses double opt-in

The owner first requests onboarding or configuration. The Configurer then shows the
complete effective configuration and exact affected file changes. Only explicit approval
of that proposal permits the write.

### D005 — One source pin

PROJECT stores one framework repository URL and full immutable commit. Root loader blocks
read that pin. The pin identifies content and limits drift. It is not authentication.

### D006 — Three activation paths, one goal flow

Manual invocation runs one goal. Session activation routes later project-changing
requests until deactivation or session end. Project boot routes them in every session.
Questions do not create goals.

### D007 — Project knowledge is explicit

PROJECT stores Intent, Map, and Validation. Intent is owner direction. Map and Validation
are repository hints that agents check against current code. Missing or stale
documentation is recorded instead of replaced with invented context.

Ambient instructions, skills, and memory can supply context. They cannot change fixed
role duties or owner authority. PROJECT and current repository evidence remain the
project sources of truth. GLBuilding does not manage the host's ambient setup.

### D008 — One simple record per goal

Each goal records its request, acceptance criteria, paths, source base, isolation choice,
owner decisions, role results, checks, and outcome. Whole conversations, transcript
proof, cryptographic manifests, and internal agent telemetry are not task state.

### D009 — Explorer and worktrees are conditional

Use Explorer only for a material repository question. Use the current checkout or a
branch for clean sequential work. Use a worktree for concurrent work or unrelated dirty
state. Commit or explicitly include relevant dirty work. Serialize overlap.

### D010 — Fresh review is mandatory and bounded

Every mutation receives a Reviewer that did not build it. The Reviewer checks every
acceptance criterion and returns `pass`, `repair`, or `blocked`. The owner can choose one
to three review rounds; the default is two. Open findings at the cap stop the goal.

### D011 — Use normal Git

Installation and completed goals use the project's normal named-path staging and local
commit process. Project hooks and Git configuration remain in force. GLBuilding does not
reimplement commits, freeze Git identity, or claim cross-host durability from a local
commit.

### D012 — Major and external actions go to the owner

Routine in-scope local work can read, edit, check, isolate, and create local commits.
Major scope or architecture choices and every push, pull request, merge, deploy, publish,
release, force operation, secret change, remote deletion, or destructive external effect
need fresh owner approval.

### D013 — Harness failure is a support result

Codex and Claude are the first target harnesses. A mutation harness must run a separate
Builder and fresh Reviewer. If it cannot follow the simple Markdown contract, record it
as unsupported. Do not expand the framework to prove or force agent obedience.

### D014 — Charters are distilled, not linked

Role behavior is distilled from useful skills and prior project experience. Those skills
are not runtime dependencies. A source change has no automatic effect. An owner-approved
Configurer proposal is required for a new charter revision.

### D015 — One repository can hold several goals

One Orchestrator can route several non-overlapping goals in one repository. Each goal
gets its own record and isolation only when needed. Multi-repository orchestration is
deferred.

### D016 — Target substantial software goals

GLBuilding is for goals where codebase scope, context loss, or change risk justifies
separate role contexts and fresh review. Small tasks can test conformance. Their elapsed
time does not measure product speed.

## Superseded hardening experiment

Early Codex and Claude trials exposed real instruction and delivery failures. The project
briefly added:

- proposal manifests with file hashes;
- Git `commit-tree` and compare-and-swap finalization;
- author and committer identity freezing;
- transcript-level mutation provenance;
- exhaustive ownership, recovery, and hostile-harness conformance cases.

These mechanisms could improve audit proof. They did not improve the core product and
moved framework effort toward proving instruction obedience.

Version one removes those mechanisms. It retains four lessons:

1. show the complete configuration and affected file changes before approval;
2. stage named paths and preserve unrelated owner work;
3. require a real fresh review with acceptance evidence;
4. label a noncompliant harness unsupported.

Git history preserves the detailed experiments. They are rationale, not runtime rules.

## Open owner decisions

- Select an open-source license before public release.
- Select the canonical public repository URL before external installation.
- Approve any public remote, tag, release, or publication when release work begins.

## Explicit deferrals

- Multi-repository orchestration.
- Multiple independent root Orchestrators in one repository.
- Distributed locks and cross-host checkpoint services.
- CLI installer and background execution.
- Runtime graph engine or graph configuration language.
- Extra roles and automatic self-evolution.
- Cryptographic proposal manifests and transcript provenance.
- Custom Git transaction or recovery machinery.
- Telemetry, analytics, dashboards, and non-Git projects.

## Rejected shapes

- One giant project instruction file: wastes context and duplicates the framework.
- Peer-to-peer role graphs: add state without improving the fixed build flow.
- One worktree for every goal: adds cost to trivial changes.
- One task file for all goals: creates avoidable conflicts.
- A runtime for persistence: solves a deferred problem before the Markdown system proves
  value.
