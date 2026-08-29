# Changelog

## Unreleased

### Removed

- The canonical release-request byte format, base64url encoding, hexadecimal owner
  rendering, dual clock samples, expiry math, consumption records, and action-ledger
  states. The release boundary keeps the same owner authority with a simple contract:
  one single-use approval per action kind and target, at most one provider submission,
  read-back before and after, and complete blocked-recovery records.
- The specification intake handshake: acknowledgements, formal-attempt identifiers, and
  round reservation. Reviewers verify the packet hash directly; a mismatch is a handoff
  defect that consumes no round.
- The activation-preflight consistency-bracket prose. The preflight keeps the four-state
  classifier and a final re-read before activation; a difference is `changed` and
  requires a fresh preflight.
- Task-record tables that restated protocol rules. The task record now stores facts and
  accepted results and references the protocol for meanings.

### Changed

- Guided onboarding is compact by default. The `## Ready to awaken Olympus` approval
  surface is at most 12 nonblank Markdown lines. The complete proposal is still
  generated before that surface; `Show details` reveals the exact PROJECT bytes, both
  loader diffs, mappings, conflicts, and the commit plan on request.
- The managed loader block shrinks to four steps. Detail lives at the pinned framework,
  not in every target repository. See [templates/BOOTSTRAP.md](templates/BOOTSTRAP.md).
- `Awaken Olympus` accepts one optional final period with the same meaning in every
  state. The period no longer changes approval semantics.
- The six onboarding stages report compactly: the `Stages:` line in the success report,
  the six-row table in the failure report and on owner request, not on every
  transition.
- The PROJECT template records role support and preferences sparsely: one default row
  plus exception rows, instead of two mandatory 15-row tables.
- The onboarding contract references the PROJECT and bootstrap templates instead of
  embedding full copies.

### Added

- Ref-based install: the owner supplies a URL and an optional branch, tag, or commit;
  the ref defaults to `main` and is resolved once to the full commit PROJECT records.
- Express onboarding: the exact request sentence `Defaults pre-approved.` onboards a
  clean default-only repository in one step; any conflict or deviation falls back to
  the gated proposal.
- Affirmative approval: an unchanged proposal accepts `Awaken Olympus` in any accepted
  form or a clear, unconditional affirmative reply.
- Worktree-per-goal default with a goal-closure step: record the branch disposition,
  remove the worktree only after merge, safe handoff, or explicit owner abandonment,
  and otherwise retain it with its path and reason recorded.
- Optional canonical ASCII art for the onboarding proposal and success report. Art is
  decorative, carries no meaning, and does not count toward the approval-surface cap.
- One inspection rule for deriving Map and Validation: code first, Git history next,
  planning prose last.
- D08 dogfood evidence: Claude passed guided onboarding on a fresh repository, and the
  fresh-review gate caught a real template defect on the first run.

## 0.4.0 - 2026-08-28

### Added

- A provider-neutral Release Agent and 15-role Pantheon entry with source-only preparation,
  immutable execution handoffs, exact owner approval, bounded duplicate control, and truthful
  per-action release results.
- A canonical release boundary with inert request bytes, ASCII owner rendering, phased
  reconciliation, retry rules, and complete blocked-recovery records.
- Owner-selected custom workflow declarations with five fixed request boundaries, ordered role
  allowlists, trigger closure, and non-bypassable review, support, owner, and sole-hub gates.
- V1–V12 conformance assertions and fixtures for the role catalog, charter shape, links,
  state-aware claims, release contract, custom workflow, recovery, and bounded evidence.

### Changed

- Current documentation now identifies 15 roles and 14 worker charters. The canonical homes
  are the [release boundary](references/PROTOCOL.md#release-boundary),
  [owner-selected workflow](references/PROTOCOL.md#owner-selected-workflow), and
  [task release records](templates/TASK.md#release-boundary-records).
- The change adds no runtime, service, scheduler, dependency, provider client, or external
  action.

### Evidence and limits

- The contracts and fixtures are static Markdown evidence. They do not prove live provider
  support, release execution, production readiness, or general harness support.
- This private experimental release makes no claim of public visibility or completed release
  execution.

## 0.3.1 - 2026-08-28

### Added

- A canonical read-only activation preflight for manual, session, project-boot, and guided
  wake entries. It inspects target onboarding state before routing or an active-state claim
  and requires an unchanged immediate recheck.
- Progressive guided onboarding with a compact material summary, optional full exact
  configuration and patch detail before approval. Plain text retains all required meaning.

### Changed

- Missing onboarding state now routes to guided System Configurer inspection. Partial,
  malformed, or changed state stops without activation.
- Existing double opt-in, fresh exact-unit review, local-only boundary, and owner gates
  remain unchanged.

### Evidence and limits

- The bounded C19 dogfood fixture run passed 142/142 rows across Olympus and unrelated
  targets, including static and behavioral checks.
- This release adds no runtime or dependency. C19 is contract evidence, not a live harness
  or production-readiness result. Lower-model equivalence and general harness support remain
  untested.
- The fixed catalog remains fourteen roles. This release does not add a Release Agent.

## 0.3.0 - 2026-08-27

### Added

- Operational craft contracts for all thirteen worker charters in the fixed Pantheon.
- Adversarial conformance fixtures for role quality and shared workflow state.

### Changed

- Specification review now reserves a candidate round and attempt identifier before
  dispatch, and counts a round only after both complete reviewer packets return.
- Halted review attempts preserve provisional findings and permit one fresh automatic
  retry before escalation.
- Plans and review units now carry persisted identities and hashes. Any later change
  invalidates the prior pass and requires fresh review.
- Task state now records multiple pending causes, evidence-backed disputes, one bounded
  re-plan, skipped work, and uncertain external-action reconciliation.

### Known limits

- The strengthened role and state contracts have static review evidence, but no new live
  target-repository run. The owner will run the first manual test after release.
- Lower-model equivalence and model routing remain untested.
- The fixed catalog remains fourteen roles. This release does not add a Release Agent or
  a runtime.

## 0.2.0 - 2026-08-26

### Added

- Guided Olympus onboarding with an inspect-first owner conversation, one material
  question per turn, a complete proposal, double opt-in, and six truthful local stages.
- One canonical plain-Markdown onboarding contract linked from all five consumers.

### Changed

- Configuration review, commit, and hook-rereview packets now preserve the Orchestrator as
  the sole hub and name the exact uncommitted and committed units.

### Known limits

- No live target repository has run the guided onboarding contract yet.
- Plain Markdown specifies the flow but does not enforce future harness behavior.

## 0.1.1 - 2026-08-26

### Added

- Atomic specification intake with persisted packet bytes, SHA-256 body checks, and a
  two-phase barrier before formal review rounds.
- Lossless Spec Writer traceability and self-contained Claims Reviewer and Spec Reviewer
  results.

### Changed

- Olympus v0.1 core changes now use the normal repository workflow and require concrete,
  isolated dogfood evidence.

### Known limits

- The v0.1.1 handoff changes have not completed a new isolated dogfood run. This release
  does not establish general harness support or production readiness.

## 0.1.0 - 2026-08-26

First experimental release.

### Added

- One fixed conditional graph with the fourteen-role Pantheon.
- Manual, session, and project orchestration modes.
- Git-backed project configuration, goal records, and bounded handoffs.
- Conditional specification, planning, documentation, design, council, and liaison roles.
- Mandatory fresh review for project mutations.
- Apache-2.0 licensing.
- Codex installation and dogfood evidence, including the controlled FPLGuru Issue #750
  A/B comparison.

### Known limits

- Claude is unsupported based on the recorded second-harness trial.
- Multi-repository orchestration is deferred.
- Olympus provides behavioral Markdown controls, not a security sandbox.
- The Issue #750 comparison was a correctness tie and does not prove a quality advantage.
