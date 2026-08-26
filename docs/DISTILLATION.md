# Skill-to-charter distillation

## Purpose

GLBuilding role charters are self-contained. They are distilled from selected skills and prior FPLGuru charter work, but those sources are not loaded at runtime.

Distillation means:

1. inspect the complete source;
2. extract the behavior needed by a fixed GLBuilding role;
3. remove source-specific commands, host names, and workflow machinery;
4. write the behavior directly into the charter;
5. record source identity and exclusions;
6. test the resulting charter through conformance scenarios.

A source update changes nothing automatically. A deliberate re-mine creates a versioned charter change that applies only to new goals.

## FPLGuru evidence

The preserved FPLGuru framework at commit `d77b93ba` established the reusable pattern:

- `.agents/charters/EVOLUTION.md` says charters are distilled, not linked.
- `.agents/charters/README.md` keeps one canonical charter copy with thin Codex and Claude mappings.
- writer and reviewer charters separate mutation from fresh review.
- loop ownership and termination live in one Orchestrator charter.

The pattern worked, but the earlier FPLGuru attempt also showed what not to copy: twelve project-specific roles, review history inside artifacts, unbounded review pressure, duplicated loop rules, provider-specific delivery paths, and claims that untested checks would converge.

GLBuilding keeps the distillation mechanism and five roles: one Orchestrator and four
worker roles.

## Source ledger

Local source paths record what was inspected. They are design provenance, not runtime
requirements.

| Source | Extracted mechanism | Destination |
|---|---|---|
| `conductor/SKILL.md` | task classification, one routing owner, phase boundaries | Orchestrator in `SKILL.md` |
| `shaping/SKILL.md` | separate requirements from mechanisms, surface unknowns, keep documents consistent | System Configurer, Explorer |
| `brainstorming/SKILL.md` | inspect first, ask only material questions, present a design before edits | System Configurer |
| `ponytail/SKILL.md` | simplicity ladder, reuse before addition, smallest useful check | Builder, Reviewer, Orchestrator |
| `resilience/SKILL.md` | material hazard, blast radius, degraded behavior, fail-closed unknowns | all fixed roles |
| `systematic-debugging/SKILL.md` | reproduce, gather evidence, trace cause, test one hypothesis | Explorer, Builder |
| `test-driven-development/SKILL.md` | prove a material behavior can fail before relying on a check | Builder |
| `using-git-worktrees/SKILL.md` | conditional isolation, dirty-state safety, baseline verification | Orchestrator protocol |
| `verification-before-completion/SKILL.md` | current command evidence before completion claims | Builder, Reviewer, Orchestrator |
| `requesting-code-review/SKILL.md` | exact review unit, independent feedback, evidence-backed response | Reviewer, Orchestrator |
| `council/SKILL.md` | adversarial design review and challenge resolution | design process only |
| `skill-creator/SKILL.md` | valid metadata and progressive loading | pack structure and conformance |

## Role synthesis

### System Configurer

The charter combines shaping and onboarding discipline with minimal configuration. It inspects first, derives Map and Validation, asks only about unresolved intent or authority, and shows one complete effective result. Resilience adds conflict and rollback behavior. Ponytail prevents an onboarding interview from becoming a workflow builder.

### Explorer

The charter combines bounded spikes, root-cause evidence, and current-revision verification. It returns exact evidence and uncertainty. It never turns missing evidence into a conclusion and never edits the repository.

### Builder

The charter contains the full Ponytail ladder rather than a vague “keep it simple” sentence. It adds root-cause investigation, the smallest falsifiable check, project-pattern reuse, and fresh verification. It does not mandate a new test suite or test framework.

### Reviewer

The charter combines exact-unit review, adversarial evidence, failure-surface analysis, protected-path checks, and verification honesty. It starts fresh for every mutation and recheck. Missing evidence returns `blocked`, not `pass`.

### Orchestrator

The skill entrypoint combines classification, activation, Git isolation, state transitions, handoff acceptance, approval gates, and bounded termination. It is the only place that owns loop consequences.

## Deliberate exclusions

- Source skill names and invocation commands are not runtime dependencies.
- Source model names are not copied. Projects map capability tiers or explicit models inside fixed slots.
- Full test-driven development ceremony is not universal. Nontrivial behavior leaves the smallest check that can fail.
- FPLGuru pull-request labels, branches, continuous-integration providers, declarations, and review lanes are not copied.
- Council is not a runtime role. Material owner decisions are surfaced to the owner.
- No source skill can automatically modify a charter.

## Evolution process

1. Record the changed source path and version.
2. State the observed GLBuilding escape or material new source behavior.
3. Propose the smallest charter delta and its exact effective result.
4. Run the System Configurer conflict check.
5. Obtain owner approval.
6. Publish a new immutable GLBuilding revision only after conformance.
7. Apply the revision to new goals. Restart an active goal only with explicit owner approval.

If a source changed but no GLBuilding behavior needs to change, record no charter delta.
