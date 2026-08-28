# Changelog

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
