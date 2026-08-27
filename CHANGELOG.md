# Changelog

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
