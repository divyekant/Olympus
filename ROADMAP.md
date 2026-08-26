# GLBuilding roadmap

The roadmap is evidence-gated. A later phase cannot turn an untested claim into a feature
promise.

| Phase | Status | Evidence |
| --- | --- | --- |
| 1 — Fixed framework | complete | lean baseline `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` |
| 2 — One target harness | complete | Codex simple conformance; loader fix `0d7705069a90ffea996a1de33a0eb52b023acb66`; fresh-clone install `e6a70e777213afb0935ac9c572e558d600624bb1` |
| 3 — Dogfood | complete | Codex correctness pilot `214be8163ba672d42b62ec7ad8ebe8fa71b466b5` |
| 4 — Large-codebase proof | failed | Codex comparison; see D02 in `docs/CONFORMANCE.md` |
| 5 — Second harness and unrelated project | complete | Claude `unsupported`; unrelated Codex mutation `pass`; see D03–D04 in `docs/CONFORMANCE.md` |
| 6 — OSS readiness | blocked | Phase 4 failed; fresh-clone evidence exists, but owner release decisions remain open |

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

## Phase 3 — Dogfood GLBuilding

**Gate:** Start only after Phase 2 passes.

Use GLBuilding to improve its own Markdown files. Each change is a new goal with a frozen
prior framework revision. A running goal cannot change the rules that govern it.

**Outcome:** The Codex correctness pilot passed. Keep fixes tied to observed escapes,
confusion, false claims, or unnecessary cost.

## Phase 4 — Large-codebase proof

**Goal:** Test the context-loss problem that GLBuilding exists to solve.

Run a representative task in a large Git repository. Use scoped Explorers only when the
Builder lacks evidence. Compare it with one unstructured session.

**Exit:** Scoped context, acceptance coverage, independent review, and owner correction
are no worse than the control. A failed comparison is a product finding.

**Outcome:** `fail`, recorded in D02. It is not release-qualified, and no obedience
machinery was added.

## Phase 5 — Second-harness and unrelated-project proof

**Goal:** Run the simple flow on the second harness and one unrelated project.

Keep harness-specific mappings outside the semantic core.

**Outcome:** The Claude trial is `unsupported`. The unrelated-project Codex mutation is
`pass`, recorded in D03–D04.

## Phase 6 — OSS release readiness

**Deliver:** selected open-source license; release version and immutable source commit;
fresh-clone installation; known limits and unsupported paths; conformance evidence; and
owner approval for public remote, tag, package, or release actions.

**Outcome:** `blocked`. Phase 4 failed. License, canonical public URL, version/tag, and
public release approval remain owner decisions. No public release or release candidate is
claimed.

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
