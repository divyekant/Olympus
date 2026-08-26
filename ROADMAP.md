# Olympus roadmap

The roadmap is evidence-gated. A later phase cannot turn an untested claim into a feature
promise.

| Phase | Status | Evidence |
| --- | --- | --- |
| 1 — Fixed framework | complete | lean baseline `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` |
| 2 — One target harness | complete | Codex simple conformance; loader fix `0d7705069a90ffea996a1de33a0eb52b023acb66`; fresh-clone install `e6a70e777213afb0935ac9c572e558d600624bb1` |
| 3 — Dogfood | complete | Codex correctness pilot `214be8163ba672d42b62ec7ad8ebe8fa71b466b5` |
| 4 — Large-codebase proof | complete, mixed | D02 failed; Issue #750 tied with no P0-P2 defects; see D05 |
| 5 — Second harness and unrelated project | complete | Claude `unsupported`; unrelated Codex mutation `pass`; see D03–D04 in `docs/CONFORMANCE.md` |
| 6 — OSS readiness | preparing | Version `0.1.0` selected; license, canonical URL, tag, and publication approval remain open |
| Catalog expansion | dogfood started | Issue #750 used framework `3d67f064821c3e4a05b5e87118eeea19119a16e6`; not every conditional role was invoked |

## Phase 1 — Specify the fixed framework

**Goal:** Define the smallest complete Markdown protocol.

**Deliver:** vision and boundary, Council-backed architecture and decisions, source distillation,
installation contract, host-neutral protocol, one Orchestrator entrypoint, four worker
charters, templates, and conformance scenarios.

**Exit:** Every shared rule has one canonical home. No rule requires a runtime.

## Phase 2 — Prove the simple flow on one target harness

**Goal:** Complete a clean end-to-end local run.

**Prove:** exact pin loading; instruction-preserving onboarding; all three activation
modes; separate Builder and fresh Reviewer; bounded repair; owner gates; and unsupported
classification when a harness cannot preserve the contract.

Run Codex first. If it is unsupported, run Claude. Dogfood starts only after one target
harness installs and completes one reviewed manual goal. Phase 2 closes only after all
listed cases have evidence.

**Exit:** One target harness has a recorded end-to-end pass.

**Outcome:** Codex simple conformance, activation and deactivation, repair-cap and
owner-gate dry-runs, loader preservation, clean-cache installation, and fresh-clone
installation passed. The loader ambiguity fix is recorded in the phase table.

## Phase 3 — Dogfood Olympus

**Gate:** Start only after Phase 2 passes.

Use Olympus to improve its own Markdown files. Each change is a new goal with a frozen
prior framework revision. A running goal cannot change the rules that govern it.

**Outcome:** The Codex correctness pilot passed. Keep fixes tied to observed escapes,
confusion, false claims, or unnecessary cost.

## Phase 4 — Large-codebase proof

**Goal:** Test the context-loss problem that Olympus exists to solve.

Run a representative task in a large Git repository. Use scoped Explorers only when the
Builder lacks evidence. Compare it with one unstructured session.

**Exit:** Scoped context, acceptance coverage, independent review, and owner correction
are no worse than the control. A failed comparison is a product finding.

**Outcome:** Mixed. D02 failed and added no obedience machinery. D05 then produced a
controlled correctness tie: both implementations had no P0-P2 defect, while Olympus
produced broader test evidence. This is sufficient for an experimental release and larger
tests. It does not prove a quality advantage.

## Phase 5 — Second-harness and unrelated-project proof

**Goal:** Run the simple flow on the second harness and one unrelated project.

Keep harness-specific mappings outside the semantic core.

**Outcome:** The Claude trial is `unsupported`. The unrelated-project Codex mutation is
`pass`, recorded in D03–D04.

## Phase 6 — OSS release readiness

**Deliver:** selected open-source license; release version and immutable source commit;
fresh-clone installation; known limits and unsupported paths; conformance evidence; and
owner approval for public remote, tag, package, or release actions.

**Outcome:** Preparing experimental `0.1.0`. The owner approved the version and larger
experiments. License, canonical public URL, tag, and public release approval remain owner
decisions.

## Deferred until evidence requires it

- Multi-repository orchestration.
- Multiple independent root Orchestrators in one repository.
- Durable cross-host checkpoint service.
- Distributed locks.
- CLI installer or background execution.
- Graph configuration language or runtime roles.
- Automatic updates or self-evolution.
- Telemetry, analytics, or a dashboard.
- Non-Git project support.
- Cryptographic proposal manifests or transcript provenance.
- Custom Git transaction and recovery machinery.
