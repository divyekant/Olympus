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

GLBuilding keeps the distillation mechanism and only four roles.

## Source ledger

The 16-character SHA-256 prefix identifies the local source inspected during this
distillation. Local paths are provenance, not runtime requirements.

| Source | SHA-256 prefix | Extracted mechanism | Destination |
|---|---|---|---|
| `conductor/SKILL.md` | `9c18251a9f1bfcf` | task classification, one routing owner, phase boundaries | Orchestrator in `SKILL.md` |
| `shaping/SKILL.md` | `fed50ece39203878` | separate requirements from mechanisms, surface unknowns, keep documents consistent | System Configurer, Explorer |
| `brainstorming/SKILL.md` | `b3c4258ef82ace57` | inspect first, ask only material questions, present an exact design before edits | System Configurer |
| `ponytail/SKILL.md` | `1316a2f3f95741d2` | full simplicity ladder, reuse before addition, smallest useful check | Builder, Reviewer, Orchestrator |
| `resilience/SKILL.md` | `ae44db490c31e91a` | material hazard, blast radius, degraded behavior, recovery, fail-closed unknowns | all fixed roles |
| `systematic-debugging/SKILL.md` | `4999cb851360485e` | reproduce, gather evidence, trace cause, test one hypothesis | Explorer, Builder |
| `test-driven-development/SKILL.md` | `7dee67b4af6bdccc` | prove a material behavior can fail before relying on a check | Builder |
| `using-git-worktrees/SKILL.md` | `de9dcde34840eee0` | isolation from committed bases, dirty-state safety, baseline verification | Orchestrator protocol |
| `verification-before-completion/SKILL.md` | `ea52d15aabaf72bc` | fresh command evidence before completion claims | Builder, Reviewer, Orchestrator |
| `requesting-code-review/SKILL.md` | `1c9e975642c859c4` | exact review unit, independent feedback, evidence-backed response | Reviewer, Orchestrator |
| `council/SKILL.md` | `b26802cf3464184d` | adversarial design review and deterministic critical-challenge resolution | GLBuilding design process only |
| `skill-creator/SKILL.md` | `6656e54755638e8e` | valid skill metadata, progressive disclosure, behavioral evaluation | pack structure and conformance |

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
- Council is not a fifth runtime role. Material owner decisions are surfaced to the owner.
- No source skill can automatically modify a charter.

## Evolution process

1. Record the changed source path, version, and digest.
2. State the observed GLBuilding escape or material new source behavior.
3. Propose the smallest charter delta and its exact effective result.
4. Run the System Configurer conflict check.
5. Obtain owner approval.
6. Publish a new immutable GLBuilding revision only after conformance.
7. Apply the revision to new goals. Restart an active goal only with explicit owner approval.

If a source changed but no GLBuilding behavior needs to change, record no charter delta.
