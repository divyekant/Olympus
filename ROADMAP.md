# GLBuilding roadmap

The roadmap is evidence-gated. A later phase cannot convert an untested claim into a feature promise.

| Phase | Status | Evidence |
| --- | --- | --- |
| 1 — Fixed framework | complete | lean baseline `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` |
| 2 — One target harness | in progress | Codex onboarding partially exercised; reviewed manual goal passed |
| 3 — Dogfood | complete | Codex correctness pilot ended at `214be8163ba672d42b62ec7ad8ebe8fa71b466b5` |
| 4 — Large-codebase proof | not run | — |
| 5 — Second harness and unrelated project | not run | — |
| 6 — OSS readiness | not run | — |

## Phase 1 — Specify the fixed framework

**Goal:** Define the smallest complete Markdown protocol.

**Deliver:**

- vision and product boundary;
- architecture and white paper;
- Council-backed decision record;
- source-skill distillation ledger;
- installation and onboarding contract;
- host-neutral protocol, one Orchestrator entrypoint, and four worker charters;
- project, goal, and bootstrap templates;
- conformance scenarios.

**Exit:** Every shared rule has one canonical home. No rule requires a GLBuilding runtime.

## Phase 2 — Prove the simple flow on one target harness

**Goal:** Complete a clean end-to-end local run.

**Prove:**

- exact pinned framework loading;
- onboarding preserves existing project instructions;
- manual, session, and project activation route through one graph;
- one mutation gets a fresh independent review;
- the repair cap stops the loop;
- remote and destructive actions stop for fresh approval;
- a harness that cannot keep Builder and Reviewer separate is marked unsupported.

Run Codex first. If it is unsupported, run Claude. Dogfood can start after one target
harness installs and completes one reviewed manual goal. Phase 2 closes only after all
listed cases have evidence.

**Exit:** One target harness has a recorded end-to-end pass.

## Phase 3 — Dogfood GLBuilding

**Gate:** Start only after one target harness can install and run one goal.

Use GLBuilding to improve its own Markdown files. Treat each framework change as a new goal with a frozen prior framework revision. A running goal cannot change the rules that govern it.

Keep only fixes tied to observed escapes, confusion, false claims, or unnecessary cost.

## Phase 4 — Large-codebase proof

**Goal:** Test the context-loss problem that GLBuilding exists to solve.

Run a representative task in a large existing Git repository. Use scoped Explorers only when the Builder lacks necessary evidence. Compare the result with a single unstructured session.

**Exit:** Evidence shows scoped context, correct acceptance coverage, independent review, and no increase in owner correction. A failed comparison is a product finding, not a result to hide.

## Phase 5 — Second-harness and unrelated-project proof

Run the same simple flow on the second target harness and record `pass` or `unsupported`.
Then complete one goal in an unrelated project. Keep harness-specific mappings outside
the semantic core.

## Phase 6 — OSS release readiness

**Deliver:**

- selected open-source license;
- release version and immutable source commit;
- installation copy tested from a fresh clone;
- known limits and unsupported paths;
- dogfood and conformance evidence;
- owner approval for any public remote, tag, package, or release.

## Deferred until evidence requires it

- multi-repository orchestration;
- durable cross-host checkpoint service;
- distributed locks;
- a CLI installer;
- background execution;
- a graph configuration language;
- extra runtime roles;
- automatic updates or self-evolution;
- telemetry, analytics, or a dashboard;
- non-Git project support.
- cryptographic proposal manifests or transcript provenance;
- custom Git transaction and recovery machinery.
