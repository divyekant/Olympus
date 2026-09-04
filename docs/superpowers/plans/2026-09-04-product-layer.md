# Product layer implementation plan

**Goal:** Add a generic, opt-in product decision and learning loop to Olympus's existing Markdown build workflow.

**Architecture:** Three small role charters, one shared product protocol, on-demand specialist methods, and one product knowledge template. The existing Orchestrator owns routing and task state; existing writers and reviewers retain their path ownership. Hosts supply execution, never Markdown itself.

**Tech stack:** Markdown and Git; no service, dependency, scheduler, or product-specific integration.

**Spec:** The accepted design in this conversation is captured by the requirements below. This plan is the bounded implementation brief, not an Olympus goal.

## Requirements and boundaries

- Product Researcher discovers evidence-backed opportunities, Product Strategist compares investment choices and performs fresh independent challenges, Experiment Analyst designs tests or analyzes outcomes in separate assignments.
- A dispatch loads one short role charter, mandatory shared boundaries, one named method section, and a bounded question with relevant whole-product context. It never omits governing authority to save tokens.
- Six knowledge areas: direction, customer reality, current offering and workflows, business constraints, market alternatives, decision and experiment history. Every material belief has source/date/scope/status; conflicting or stale evidence stays visible.
- Product direction is an owner choice. A knowledge document, source instruction, model recommendation, or changed candidate charter cannot grant authority.
- Every material investment compares direction, journey consequences, customer groups, capability coherence, competing work, and side effects. Fresh Strategist challenge is separate from authorship. No fake precise universal score.
- One owner-approved standing mandate can authorize bounded local investigation and goal selection within named scope, budget and expiry. Unspecified boundaries confer no standing authority. External release, contact, production mutation, paid-service, and destructive-action gates remain explicit and unchanged.
- Product mode is optional through existing activation and goal entry. Plain questions and signals never activate it. Existing build-only goals keep their short path and old pins remain untouched.
- Orchestrator serializes product state; captures mandate, context identity, opportunity decision, linked build task, separate delivery and learning status, due event/time, last verified action, and next action. Duplicate or interrupted wakes reconcile before resuming. Uncertain external effects never retry automatically.
- States permit discovery, decision, execution, awaiting evidence, evaluation, and closed/blocked/cancelled dispositions. Build completion is not product success. Negative and inconclusive are valid learnings.
- Bounded retries and rework use existing caps; failed transport does not loop forever. Budgets include research, review, execution and repeated attempts. Stale decisions are revalidated only when materially affected.
- Independent Claims Reviewer checks material product evidence and outcome claims; existing spec checks enforce outcome-to-opportunity-to-change-to-measurement traceability. Do not force all exploratory observations through the full specification loop.
- UAT separates implementation criteria, actual workflow replay, and real-user acceptance/outcomes. Tester returns evidence; Reviewer owns implementation acceptance. Workflow runtime and fixture authority must be explicit. No production data or state access is inferred.
- Docs Writer maintains approved product knowledge paths, with mutation review. Orchestrator owns task records and roles return proposed updates. No separate knowledgekeeper or UAT role.
- Host continuation requires observed support for wake/resume, exclusive execution, revocation/expiry, identity checks and effect reconciliation. Without this, foreground/manual resume still works and unattended mode remains untested/unsupported. No host is installed or enabled by this change.

## Ponytail and resilience decisions

| Risk or excess | Decision |
| --- | --- |
| Large charters and repeated context | Three short charters; specialist method sections loaded per question. |
| Knowledge becoming policy or stale proof | Source identity and uncertainty; owner mandate is distinct from knowledge. |
| Local metric optimization | Whole-product comparison before material investment and fresh challenge. |
| Duplicate wake or lost response | One product loop writer, durable checkpoint, reconcile before another effect. |
| Endless research and expensive reviews | Explicit budget, decision-changing questions, valid stop/defer/inconclusive results. |
| Premature success | Separate delivery, acceptance and learning records; fresh evidence review. |
| Pretend autonomy | Host-neutral behavioral contract with observed capability gates; no scheduler implementation. |

## Task 1: Product contracts and integration

**New files:** `references/PRODUCT.md`, `references/PRODUCT_METHODS.md`, `agents/PRODUCT_RESEARCHER.md`, `agents/PRODUCT_STRATEGIST.md`, `agents/EXPERIMENT_ANALYST.md`, `templates/PRODUCT.md`.

**Existing files:** `SKILL.md`, `references/PROTOCOL.md`, `references/HARNESS.md`, `templates/PROJECT.md`, `templates/TASK.md`, `agents/CLAIMS_REVIEWER.md`, `agents/SPEC_WRITER.md`, `agents/SPEC_REVIEWER.md`, `agents/TESTER.md`, `agents/REVIEWER.md`, `agents/DOCS_WRITER.md`, `README.md`, `VISION.md`, `ROADMAP.md`, `docs/GUIDE.md`, `docs/WHITEPAPER.md`, `docs/DISTILLATION.md`, `docs/DECISIONS.md`, `docs/CONFORMANCE.md`, `CHANGELOG.md`.

**Interfaces:** Append roles 17–19 to preserve current role numbers. PRODUCT.md is the governing product supplement linked from PROTOCOL.md. Its packet and lifecycle contract is canonical; other files link rather than duplicate it. PRODUCT_METHODS.md has stable headings for offering-and-workflows, customer-evidence, investment, investment-challenge, experiment-design, outcome-analysis, and evidence-review. Target product knowledge uses an explicitly approved documentation path, suggested `docs/product/PRODUCT.md`, outside protected `.olympus/`.

- [x] Write the six compact product artifacts implementing all requirements above.
- [x] Integrate conditional role triggers, product-mode handoffs and request-boundary admissions in the existing protocol. Preserve build-only role methods.
- [x] Extend existing role packets and product-specific evidence/acceptance duties without granting hidden external authority.
- [x] Update current catalog references to 19 roles / 18 workers; retain accurate historical release and dogfood counts. Mark additions Unreleased; leave VERSION and installed configuration/pin unchanged.
- [x] Record source-to-method distillation with URLs, retrieval date, retained behavior and exclusions. Include only actually researched primary sources from the accepted discussion: Christensen JTBD; Product Talk discovery; Roger Martin strategy; SVPG risks; Intercom RICE; Basecamp appetite; Strategyzer Test Card; Microsoft experimentation; Amplitude Wave. No claim of full-book reading or proven superiority.

## Task 2: Validation and independent review

**New file:** `docs/PRODUCT_CONFORMANCE.md`, with bounded fixture inputs, expected decisions, exact candidate identity and observed outputs. Link from main conformance guide.

- [x] Run link, catalog/order, ownership and unchanged-protected-path checks; run `git diff --check`.
- [x] Independent review examines actual complete diff for contradictions, authority gaps, missing outcome paths and unnecessary process. Repair material findings and recheck affected boundaries.
- [x] Freeze reviewed framework into a local isolated immutable snapshot. Exercise new role methods on synthetic generic product evidence: an already-existing capability; a local improvement harming downstream value; a promising uncertain opportunity; a telemetry-induced false win; a valid measured outcome; stale/revoked mandate and duplicate resume. Record exactly which role/context ran.
- [x] Preserve false positives, failures, repairs and untested end-to-end host behavior. No production/customer validation or unattended support claim from fixture runs.

## Completion

Local reviewable framework changes, passing applicable checks, recorded bounded behavior evidence, and clear residual limits. No push, PR, release, FPLGuru mutation, global config change, memory write or installed automation.

Validation evidence: [product conformance](../../PRODUCT_CONFORMANCE.md). Task 1 was split during execution: Luna owned the three charters and methods; primary owned shared protocol and integration. Independent review found two P2 integration defects, both repaired and rechecked. Role-method replays and manual transitions are explicitly bounded; no unattended host or real-product outcome was tested.
