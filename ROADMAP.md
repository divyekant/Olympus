# Olympus roadmap

The roadmap is evidence-gated. A later phase cannot turn an untested claim into a feature
promise.

| Phase | Status | Evidence |
| --- | --- | --- |
| 1 — Fixed framework | complete | lean baseline `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` |
| 2 — One target harness | complete | Codex simple conformance; loader fix `0d7705069a90ffea996a1de33a0eb52b023acb66`; fresh-clone install `e6a70e777213afb0935ac9c572e558d600624bb1` |
| 3 — Dogfood | complete | Codex correctness pilot `214be8163ba672d42b62ec7ad8ebe8fa71b466b5` |
| 4 — Large-codebase proof | complete, mixed | D02 failed; Issue #750 tied with no P0-P2 defects; see D05 |
| 5 — Second harness and unrelated project | complete | Claude bounded mutation-path pass; unrelated Codex mutation pass; see D03-D04 |
| 6 — OSS readiness | private experimental releases | Apache-2.0; private canonical repository; `v0.5.1` released with core-authority and specification-convergence fixes |
| Role and state quality | static pass, live test pending | all existing charters strengthened at `d894317851b5ceacc0337578b9d684729401e7b6`; C17-C18 specified |
| Catalog and workflow expansion | static contract added; live evidence pending | the catalog now has fifteen roles, including a provider-neutral Release Agent and five fixed request boundaries with an owner-selected role allowlist; see the [release boundary](references/PROTOCOL.md#release-boundary), [owner-selected workflow](references/PROTOCOL.md#owner-selected-workflow), and [V1–V12 fixtures](docs/CONFORMANCE.md#v1-v12-release-agent-and-custom-workflow-fixtures) |

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

Core-framework changes use the normal repository workflow. A separate run may dogfood the
merged change at one immutable commit. That run supplies bounded evidence and never governs
or authorizes the core edit.

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

**Outcome:** The first Claude trial was `unsupported`. Claude later passed one bounded
Builder-to-fresh-Reviewer mutation path. The unrelated-project Codex mutation is
`pass`.
These scenario results are recorded in D03-D04 and do not establish general harness support.

## Phase 6 — OSS release readiness

**Deliver:** selected open-source license; release version and immutable source commit;
fresh-clone installation; known limits and unsupported paths; conformance evidence; and
owner approval for public remote, tag, package, or release actions.

**Outcome:** Experimental releases use Apache-2.0 and remain private. Version `0.3.0`
strengthened the fixed role and state contracts. Version `0.4.0` added the
provider-neutral Release Agent and owner-selected workflow boundaries. Version `0.5.0`
made onboarding compact and removed protocol ceremony. The current private experimental
`0.5.1` fixes core-change authority and specification convergence without adding a
feature. Claude passed guided onboarding and one bounded mutation path. No live provider
behavior, production readiness, or general Claude support is established. Keep the
canonical repository private until the owner approves public version `1.0.0`.

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
