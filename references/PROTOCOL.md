# Olympus runtime protocol

This is the shared contract for every Olympus goal. It stays small, conditional, and
Markdown-only.

## 1. Fixed catalog

The **Pantheon** is Olympus's fifteen fixed roles in this order. The Orchestrator is the
sole hub. A role is invoked only when its trigger holds, but no project setting can remove
a trigger.

| # | Role | Trigger | Responsibility |
| --- | --- | --- | --- |
| 1 | Orchestrator | every routed request | Owns classification, routing, packets, task records, gates, and result aggregation. |
| 2 | System Configurer | owner onboarding or configuration request, plus double opt-in | Owns configuration mutation. |
| 3 | Explorer | fresh for a material repository question blocking any required role, or an explicit audit | Answers one bounded question read-only. |
| 4 | Spec Writer | substantial, ambiguous, architectural, or cross-layer goal | Turns a bounded goal into a testable contract. |
| 5 | Claims Reviewer | every Spec Writer result | Owns only facts, evidence, citations, counts, hashes, and uncertainty. |
| 6 | Spec Reviewer | every Spec Writer result | Owns only completeness, coherence, authority boundaries, failure paths, joint satisfiability, and acceptance-testability. |
| 7 | Plan Writer | accepted contract has dependent steps, cross-layer or interface sequencing, or an explicit plan need | Produces an ordered implementation plan. |
| 8 | Plan Verifier | every Plan Writer result | Freshly verifies the whole plan read-only. |
| 9 | Builder | every non-configuration project mutation | Makes the approved project change in approved paths. |
| 10 | Docs Writer | Builder makes tracked documentation false, or the contract requires documentation synchronization | Updates approved documentation only. |
| 11 | Reviewer | every project or configuration mutation | Owns whether implementation evidence satisfies the accepted criteria, read-only. |
| 12 | Design Reviewer | material user-facing interface, interaction, visual design, or design-system change | Freshly checks the change against matching project design standards read-only. |
| 13 | Release Agent | owner-requested release preparation, remote reconciliation, or one release-boundary external action | Validates release evidence and performs at most one approved provider action submission. |
| 14 | Decision Council | unresolved material decision with viable trade-offs | Gives one read-only advisory recommendation. |
| 15 | Liaison | human status or explanation request | Rereads evidence and answers without changing the goal. |

Every role receives from and returns only to the Orchestrator. No role invokes or
communicates with another role. The Orchestrator decides which conditional roles run and
records each invoked role's result.

Only the System Configurer changes `.olympus/PROJECT.md` or managed loader blocks.
Only the Orchestrator writes `.olympus/tasks/<goal-id>.md`. Only the Builder changes
approved non-documentation project paths. Only the Docs Writer changes approved
documentation paths. Claims, Spec, Plan, Design, and general Reviewers are read-only.
Decision Council is advisory and has no gate. Release Agent changes no file, has no
standing external authority, and returns only to the Orchestrator. Liaison is read-only
and has no gate.

For Olympus dogfood only, an immutable earlier revision can govern a goal that edits a
separate target checkout for a prospective revision. The goal never reloads its own
in-progress edits as instructions.

## 2. Activation

Every manual-goal, session, project-boot, or guided wake entry first runs the [canonical
activation preflight](#canonical-activation-preflight)
against the target repository root. No entry may create a goal, route later requests, or
report Olympus as active before an unchanged complete result from that read-only preflight
and its immediate final recheck authorizes it. The target root is
the repository being activated, whether it is Olympus or an unrelated Git repository;
the framework checkout is never a substitute target.

- Manual mode: `Use Olympus for: <goal>` runs one goal only after an unchanged `complete`
  preflight state.
- Session mode: `Activate Olympus orchestration` routes later project-changing requests
  until session end or deactivation, only after an unchanged `complete` preflight state.
- Project mode: PROJECT boot mode `orchestration` activates routing in each new session,
  only after an unchanged `complete` preflight state.
- Guided entry: trim surrounding whitespace and accept `Awaken Olympus` with one optional
  final period. It is never an alias for session activation.
- `Deactivate Olympus orchestration` stops new session routing. It does not cancel an
  active goal or change PROJECT.
- Questions do not create goals. Explicit read-only audits use Explorer.

All three modes use the same goal flow.

### Canonical activation preflight

The Orchestrator performs this canonical read-only activation preflight before any activation or
guided wake result. It inspects exactly these target-root units:

- `.olympus/PROJECT.md`;
- the Olympus managed unit in root `AGENTS.md`; and
- the Olympus managed unit in root `CLAUDE.md`.

The preflight does not read a framework copy as target state. The first consistency bracket
opens before the initial PROJECT sample; no target, checkout, pinned-contract,
canonical-loader, or checkout-status read occurs before that bracket. It binds one exact
snapshot before routing. For each of the three paths it records presence and exact byte identity,
including the surrounding loader file for a managed unit, and records the resolved
framework checkout path, commit, readability, and clean status. An absent unit is recorded
as absent. A root loader file with no Olympus marker is an absent managed unit, even when
the file itself exists. An unreadable present file or unit is not treated as absent.

Each first and final capture is an explicit before-and-after identity bracket, not an
atomic filesystem snapshot. Inside the bracket, sample the identities of all three target
paths; read PROJECT or use a complete owner/request URL and full commit to resolve the
source; sample the resolved-checkout path, commit, readability, and clean status; read
PROJECT, both managed units, pinned `SKILL.md`, pinned `references/PROTOCOL.md`, canonical
loader bytes, and checkout evidence; then repeat the exact target and checkout samples.
Every target, resolved-checkout, pinned-contract, canonical-loader, and checkout-status
read is inside this explicit bracket. A capture is coherent only when all before and after
samples match. An internal mismatch returns `changed` and requires fresh preflight. The
final capture repeats the same bracket with the resolved source from the first coherent
capture. Stable invalid pin evidence does not stop the bracket; classify it as `malformed`
only after the coherent final capture. Only internal instability or differing coherent
captures returns `changed`.

Every present loader is canonical-compared against canonical loader bytes from a resolved
source identity before it can be valid in any state, including `partial`. Use the valid
PROJECT pin when PROJECT is present; otherwise use a complete owner/request URL and full
commit. A present loader without a resolvable source identity is unverifiable and therefore
`malformed`. Marker shape alone never makes a loader valid.

Classify the bound snapshot in this order:

1. `malformed` when any present unit is invalid, unreadable, conflicting, or
   noncanonical. This includes invalid PROJECT structure or fields; an invalid URL;
   a commit that is not exactly 40 characters; an invalid boot mode; an unreadable,
   unavailable, mismatched, or dirty resolved pin required by the present configuration;
   and duplicate, nested, incomplete, unequal, or noncanonical managed loader markers.
2. `missing` when all three managed units are absent: PROJECT is absent and neither root
   loader contains an Olympus marker. Existing root loader files without a marker still
   produce `missing`.
3. `complete` when all three units are present, valid, canonical, and matching, and the
   URL and full commit resolve to that exact readable, clean framework revision.
4. `partial` for every remaining combination in which every present unit is valid and
   every other unit is absent. Partial never means complete and never authorizes repair.

PROJECT is valid only when it passes the pinned framework's PROJECT structure and
configuration checks, contains a repository URL and a 40-character immutable commit, and
uses boot mode `manual` or `orchestration`. Each present root loader is valid only when it
contains exactly one complete, non-nested `OLYMPUS:BEGIN` and `OLYMPUS:END` pair. For a
`complete` result, the two managed units must be identical and must match the canonical
unit at the PROJECT pin. Any failed applicable check is `malformed`, not an inferred
`partial` or `complete` result.

The state result includes the exact present, absent, invalid, conflicting, unverifiable,
and noncanonical units, the three-file snapshot, and the resolved-checkout evidence. It also
includes the activation result. `missing` routes the request to existing System
Configurer guided onboarding without a write or activation. If the request does not
supply both source values, ask one blocking question that names only the missing framework
repository URL, full commit, or both; do not ask another question before inspection. The
first onboarding opt-in permits inspection and a proposal only. The second opt-in and all
existing exact-unit review and owner gates remain required for configuration mutation.

`partial` and `malformed` stop without activation, mutation, or automatic repair. Report
the exact state and the smallest safe System Configurer action: a fresh read-only
inspection and complete proposal after an owner configuration request. Do not hide a
conflict, unsupported role, unreadable pin, or missing identity behind a default. That
request must create a fresh preflight snapshot.

Before any outcome, capture and classify one coherent first snapshot and one coherent
final snapshot under the same bracket rules. An all-absent entry without identity may
classify candidate `missing`, but it still needs the final snapshot before its question or
report. A `changed` result means either capture is internally unstable or the two coherent
captures differ. A final read failure is `changed` only when the corresponding first
capture was readable; stable invalid, unreadable, mismatched, or dirty evidence is
`malformed`. A changed result reports only `changed`, does not route Configurer, and
requires fresh preflight. For unchanged evidence, the final captured snapshot is the
decision input; its state report and allowed route form one transition. The final coherent
capture and assignment form one transition. No repository read, role dispatch, or other step
occurs between final capture and assignment. A repository change after coherent final
capture is next-entry state, not an impossible guarantee inside this transition. Current
managed loaders and PROJECT remain unchanged; any later repin or loader update is a separate
Configurer double-opt-in after an immutable product commit.

Only `complete` may approach the activation sink. Use only the exact URL and full commit
from PROJECT bound by the final bracket. The immediate final recheck is the final bracket:
it re-reads the three target paths and rechecks the resolved checkout against the bound
snapshot. Compare every presence bit and exact content identity, the checkout path and
commit, readability, and clean status. Stop and discard the preflight result if any file
changes or any required state becomes unreadable, or if the checkout becomes mismatched
or dirty. An unchanged snapshot may honor only the requested canonical mode: `Use Olympus
for: <goal>` starts one goal, `Activate Olympus orchestration` starts session routing, and
PROJECT boot mode `orchestration` starts project routing. Existing host-conflict,
role-support, owner-gate, and project-instruction checks still apply.

`Awaken Olympus` is a guided entry, never a session activation. In `missing` state it
starts the guided onboarding route above. In `complete` state it reports verified
readiness, the boot state, and the canonical owner choices (`Use Olympus for: <goal>` and
`Activate Olympus orchestration`) without starting a new mode. In an unchanged `## Ready
to awaken Olympus` proposal, the exact reply `Awaken Olympus` is the one second-opt-in
action. Any changed proposal requires a new second opt-in. The optional period form
remains guided entry and does not bypass this gate.

The preflight and guided routing are read-only. They add no runtime, dependency, service,
state store, role, or remote authority. The Orchestrator remains the sole routing hub;
only System Configurer changes PROJECT or managed loader units; and fixed roles, double
opt-in, owner gates, and the local-only boundary remain in force.

## 3. Project configuration

PROJECT stores the framework repository URL, full immutable commit, boot mode, project
Intent, Map, Validation, boundaries, exact role preferences, harness evidence, and
approved custom instructions.

Initial onboarding starts from the URL and commit in the owner's request. Later sessions
read the pin from PROJECT. Load only that version. A source pin identifies content; it
does not authenticate the source.

Native host and project instructions still apply. Inside Olympus, use this order:

1. fixed protocol and role duties;
2. versioned defaults;
3. owner-approved project additions or narrowings;
4. owner-approved evolutions;
5. task-specific narrowing.

Lower layers cannot add roles, remove duties, enable peer control, bypass fresh review,
change protected paths, or grant standing authority for external actions. PROJECT can
make optional triggers more eager, add project matching details or standards/tools, and
record harness mappings. It cannot suppress a framework trigger, paired verifier, fresh
review, fixed order, or authority boundary.

Intent is owner direction. Map locates relevant code and documentation. Validation lists
commands and evidence sources. Map and Validation are hints until checked against current
code. Missing or stale documentation is a project risk, not a reason to invent facts.

Configuration uses double opt-in: the owner requests configuration, then approves the
complete effective configuration and exact loader changes. The Configurer applies only
that proposal without a commit. A fresh Reviewer reviews the exact uncommitted
`PROJECT.md` plus managed-loader unit. Only a passing review permits named-path staging
and the local commit. If a hook changes reviewed content, run a fresh review of the
committed content before completion. Repair beyond the approved proposal needs a new
owner opt-in. Configuration changes affect new goals only.

## 4. Goal flow

For each goal, the Orchestrator creates one task record with:

- the request, acceptance criteria, non-goals, and allowed paths;
- framework commit, PROJECT revision, and source base;
- branch or worktree choice;
- predicted and actual role population and each harness mapping;
- owner decisions, role results, checks, and final status;
- compact specification round summaries, one Orchestrator-owned finding ledger with minimum
  evidence and closure conditions, convergence state, and current specification body size;
- uncertainty and unsupported or untested evidence.

Use these states: `planned`, `active`, `reviewing`, `complete`, `blocked`, or `cancelled`.

Then:

1. Classify the request, confirm scope, and record the predicted roles and support
   evidence. Validate any single custom workflow and request boundary under [owner-selected
   workflow](#owner-selected-workflow); missing mapping for any required role blocks that
   path before dispatch.
2. For owner configuration requests, use the configuration flow. The first opt-in starts
   inspection and the proposal. The second opt-in starts configuration mutation.
3. Run Explorer fresh only when a material repository question blocks a required role or
   the request is an explicit audit. It can unblock any required role but returns only to
   the Orchestrator.
4. For a substantial, ambiguous, architectural, or cross-layer goal, run the
   specification bracket before planning or building:
   - send the bounded packet to Spec Writer;
   - on the first round, send the bounded goal packet; on repair, send only the current
     specification body and the open finding ledger;
   - persist the complete current Writer result before starting review. The specification
     body contains no earlier body, body diff, reviewer transcript, review history, round
     record, or defensive annotation;
   - update the task metadata from pending, then record the packet identifier and the
     lowercase SHA-256 hash of the exact persisted specification body bytes, and verify
     that hash against the Writer return;
   - give a fresh Claims Reviewer and a fresh Spec Reviewer the same immutable packet,
     identifier, and hash;
   - obtain an intake acknowledgement from both reviewers that identifies the packet and
     hash, confirms the required sections and current task metadata, and reports the hash
     each reviewer recomputed from its received specification body;
   - require each reviewer to stop after intake; only after both acknowledgements match,
     change the handoff to `formal-review`, reserve the next formal round number, record a
     unique formal-attempt identifier, and authorize both reviewers to review that exact
     packet;
   - require each reviewer to return its complete jurisdictional finding set in one pass,
     including an explicit empty set;
   - consume the reserved formal round only after both complete reviewer packets return. A
     `halted` reviewer or transport attempt stays recorded under its attempt identifier,
     consumes no formal round, and retries the same immutable packet with a new attempt
     identifier and fresh reviewers;
   - preserve every finding from a partial attempt as provisional evidence. The next fresh
     complete bracket must reproduce, withdraw, or maintain each provisional finding before
     it can pass. Permit one automatic retry for the same packet; a second halted attempt
     escalates to the owner or blocks the goal;
   - merge both complete sets, freeze one finding ledger for the round, route only ledger
     findings for repair, and run both fresh reviews over the repaired complete packet;
   - at the independent bracket cap, open findings block the goal.
5. If the accepted contract has dependent steps, cross-layer or interface sequencing, or
   an explicit plan need, send the accepted contract or specification verbatim to Plan
   Writer. Persist the complete plan, record its packet identifier and lowercase SHA-256
   hash, and send the same contract plus that frozen plan to a fresh Plan Verifier. A plan
   repair gets a new identity and complete fresh verification. Builder receives only the
   exact accepted plan identity.
6. For every non-configuration project mutation, send the accepted contract, accepted
   specification when used, accepted plan when used, allowed paths, evidence, and checks
   to Builder. Builder blocks before editing on a conflict, missing decision, or verified
   code contradiction.
7. If Builder makes tracked documentation false or the contract requires synchronization,
   send the complete behavior diff to Docs Writer. Docs Writer edits only approved docs
   and reports changed claims, links, checks, and uncertainty.
8. Send every project or configuration mutation to a fresh Reviewer. Reviewer checks the
   complete mutation, Builder or Configurer result, every criterion, and relevant checks.
9. If the mutation materially affects a user-facing interface, interaction, visual design,
   or design system, send the diff and matching project design standards to a fresh Design
   Reviewer. Missing required standards or matching evidence blocks that trigger. Design
   Reviewer cannot replace the general Reviewer pass.
10. On passing invoked reviews, run final relevant checks and compare the result with
    actual Git state. Do not claim an untested role, harness, or execution as passed.
11. After the exact reviewed commit and final checks exist, dispatch Release Agent only for
    an owner-requested release preparation, remote reconciliation, or one release-boundary
    external action. Send the source-only preparation handoff first. For `prepared`, the
    Orchestrator presents the exact block, rendering, digest, action, target, expiry, and
    residual risk for separate owner approval, then records verified one-use consumption
    before creating the immutable execution handoff. Each action kind and target remains a
    separate gate; Release Agent does not receive standing authority.
12. When a material decision has viable trade-offs that remain unresolved, the
    Orchestrator may ask Decision Council one balanced read-only question. Its advice is
    recorded but is not a gate and does not replace owner approval. For a high-stakes
    decision, the Orchestrator may use at most three fresh Council invocations for that
    same question. Record each packet separately and do not convert the set into a verdict
    or a new gate. Sequential or same-context execution is degraded independence.
13. For a human status or explanation request, Liaison rereads the current task record,
    artifacts, and Git evidence, answers first, cites evidence, and routes action requests
    back to the Orchestrator.

The Builder-to-Docs Writer step is conditional. The Docs Writer step precedes the fresh
general Reviewer whenever it runs. The Design Reviewer is conditional and does not replace
that Reviewer.

The numeric cap applies independently to specification, plan, configuration, and
implementation brackets. A repair always receives a complete fresh review from the
relevant reviewer set. No bracket starts another round after its cap. A formal round is
consumed only by a complete reviewer bracket. A halted operational attempt remains visible
but does not consume the cap. The specification round cap is 10 completed formal rounds
(default 10; expected closure is 2-3 rounds). The plan, configuration, and implementation
caps remain their configured values and defaults.

The current specification body is the only specification text in the task record. Keep task
metadata, packet identifiers, hashes, verdict counts, findings, convergence state, and body
size outside the hashed body. The body must define requirements, invariants, acceptance
criteria, red paths, and validation obligations. It must not contain review history or
reviewer output.

At every completed formal round, record the open P0-P2 count and the current body line and
byte size.
The body is at most 300 lines and 48,000 bytes. If round 3 does not reduce open P0-P2
findings, or the body grows without reducing them, the next Writer result is a compact,
complete restatement, not an additive patch. This does not reset the round count. At round
10, any remaining P0-P2 finding blocks implementation. An oversized Writer result is
incomplete and does not enter reviewer intake.

Convergence is explicit. Claims Reviewer and Spec Reviewer each return their complete
jurisdictional set on every round. The Orchestrator merges and freezes the ledger. A finding
first reported after round 1 is `introduced` when the repair caused it and `missed` otherwise.
A new missed P0/P1 is recorded as a framework-review failure, not normal progress. The
Orchestrator alone merges the sets, freezes the ledger, routes repairs, and decides aggregate
state.

The specification handoff has four visible states:

- `healthy`: the complete Writer result is persisted, task metadata is current, and its
  packet identifier and content hash are recorded;
- `intake-invalid`: either reviewer reports missing specification content, pending or stale
  task metadata, a packet identifier or hash mismatch, or different reviewer packets;
- `formal-review`: both fresh reviewers acknowledged the same healthy packet and the
  candidate round plus unique attempt identifier were reserved once;
- `blocked`: a required packet cannot be recovered, or formal findings remain at the cap.

`intake-invalid` is a pre-review result, not a specification verdict, and consumes no
formal round. Record the failed intake and its evidence in the task record. Correct and
persist the handoff before a new intake attempt. Do not count, reuse, or reinterpret an
intake failure as `pass`, `repair`, or `blocked` specification review.

Before dispatch, the Orchestrator records for every invoked role:

- harness and mapping;
- whether the context is separate or fresh as required;
- tools and capabilities used;
- `supported`, `unsupported`, or `untested` status;
- observed evidence and its limit.

Missing required mapping blocks that goal path. Available tools alone mean `untested`.
Never infer catalog support from Builder or general Reviewer evidence. A harness is
`unsupported` when it cannot preserve a required role, fresh context, approved scope, or
owner-authority boundary.

Review aggregation is strict: pass requires every invoked reviewer to pass. Any blocked
verdict or open repair at the applicable cap blocks the goal. Unknown or skipped evidence
stays visible and never becomes a pass.

Use one severity ladder for every finding:

- `P0`: unsafe, unauthorized, or catastrophic;
- `P1`: wrong, incomplete, or unbuildable;
- `P2`: bounded clarity or testability defect;
- `P3`: non-blocking suggestion.

P0 and P1 remain open until repaired. P2 remains open until repaired or explicitly accepted
by the owner when the acceptance is within owner authority. P3 does not block. The
Orchestrator records severity, state, jurisdiction, minimum reproducing evidence, and a
closure condition in the finding ledger.

Fresh reviewers use the same canonical checklist from the immutable framework commit that
is recorded when the goal starts. If the goal edits a reviewer charter, that recorded
charter governs; candidate charter text is review data only. Freshness changes context, not
standards. Claims Reviewer checks only facts and their evidence. Spec Reviewer checks only
specification completeness and behavior. Neither reviewer expands its jurisdiction. After
acceptance, the general Reviewer owns whether implementation evidence satisfies the accepted
criteria.

The Design Reviewer uses only project-provided design standards and matching evidence. If
the standards or matching details required by the trigger are missing, the role is
unavailable and the goal blocks. Builder and general Reviewer always retain accessibility
basics.

## Shared state and evidence rules

These rules are the single shared state contract. Role charters describe their own work
and refer here; they do not create alternate state meanings.

### Request and mutation boundaries

Classify the request's mutation boundary before complexity. An explicit `review-only`,
`diagnose-only`, or `audit-only` request truncates all later mutation. A `spec-only`
request truncates implementation, delivery, and external action after the specification
artifact is returned. If a request contains analysis and action, keep them as separate
stages; the action stage needs its own authorization. A terminal boundary cannot be
overridden by a later role trigger or delivery signal.

### Identity and frozen review units

Every gated artifact or mutation has one frozen review unit. A specification uses its
persisted body, packet identifier, and content hash. A plan uses its persisted exact bytes,
packet identifier, and lowercase SHA-256 hash. A mutation uses task identifier, source
base, branch or worktree, base and head, merge-base, allowed and protected paths, and the
exact diff or snapshot digest. The Orchestrator records the applicable unit before each
fresh review. Any edit, hook change, changed path, or post-pass change invalidates that pass
and requires a fresh review of the new exact unit. No role may treat its own claim that a
unit is unchanged as repository proof.

Role claims are not repository proof. Before each state transition, the Orchestrator
verifies role identity, packet identity, Git state, required checks, and the transition's
evidence. A role result cannot substitute for a command, file, or provider observation.

### Orchestrator aggregation boundary

The Orchestrator merges, counts, freezes, and routes the results that roles return. It
cannot invent a finding, reclassify a role's finding, resolve a finding, or produce a
finding on a role's behalf. A complete empty finding set is still a role result. Review
verdicts and operational outcomes remain separate records.

### Runtime, pending, and review outcomes

`halted` is an operational or runtime outcome, such as an unavailable role, failed
transport, tool that could not execute, or interrupted execution. It is separate from
findings and verdicts, consumes no completed review round, and cannot become `pass` through
aggregation. Preserve the attempt identifier, cause, partial output disposition, last
verified state, recovery owner, and safe retry condition. A check that executes and finds a
defect is not `halted`; the owning role returns its normal result or verdict.

If a halted review attempt produced findings before interruption, preserve them as
provisional evidence. A later fresh complete bracket must explicitly reproduce, withdraw,
or maintain each one. One automatic retry is permitted for the same frozen unit. A second
halt escalates or blocks instead of creating an unbounded operational loop.

`pending` means required work or evidence is not complete. Its cause classes are
writer-suppliable evidence, owner decision, environment or credentials, and unavailable
execution. Record every applicable cause separately with its owner, closure evidence, and
safe retry condition. Pending is never clean and resumes only after every required cause is
closed. Route writer-suppliable evidence to the owning writer, an owner decision to the
owner through the Orchestrator, environment or credentials to the owner or environment
gate, and unavailable execution to an honest `blocked`, `halted`, or `unsupported` outcome
as applicable. Do not silently substitute another role, command, context, or provider.

### Disputes and re-planning

For an unchanged artifact, allow one evidence-backed dispute round. A fresh reviewer
checks the same frozen unit and either withdraws or maintains the finding. A maintained
finding goes to the owner or the applicable escalation path; it does not receive an
unbounded argument loop. Any artifact edit starts a new frozen review unit instead.

Allow one re-plan when hidden complexity or a new trigger changes the accepted plan.
Record the new evidence and affected steps. A second stall at the same node escalates to
the owner or blocks the goal; it does not repeat the same re-plan.

### Skipped work and escaped findings

Record skipped or unrunnable work both at classification and at delivery, with the
reason, required capability, and consequence. A skipped role or check is never silently
substituted and never reported as passed.

An escaped external finding is recorded as evidence for a future framework-gap
assessment. It never mutates the active goal's rules, role catalog, authority, or
acceptance criteria in place. Any framework change follows the normal owner-approved
core-framework workflow.

## Release boundary

Release Agent owns only the provider-neutral release boundary. It has no file authority or
standing external authority. The Orchestrator owns task records, owner decisions, approval,
consumption, dispatch, aggregation, and every transition. A release action is never implied
by a local commit or by a role trigger.

### Preparation and execution handoffs

Release Agent has two separate handoffs. Preparation receives the following source fields in
this exact order:

| Field | Meaning |
| --- | --- |
| `goal-and-packet-identity` | Goal identifier and packet identity. |
| `reviewed-commit-and-review-evidence` | Full reviewed commit and complete review evidence. |
| `final-checks-and-current-git-state` | Final checks and current Git state. |
| `action-kind` | One distinct action kind. |
| `provider` | Provider identity. |
| `account-or-tenant` | Provider account or tenant. |
| `repository-or-service` | Repository or service identity. |
| `target` | Exact remote target. |
| `artifact-digest` | Artifact digest bytes, when the source semantics provide them. |
| `remote-object-identity` | Mandatory non-empty remote object identity. |
| `provider-request-bytes` | Exact provider request bytes. |
| `provider-options-bytes` | Complete material provider-options bytes, including defaults. |
| `concurrency-control-bytes` | Concurrency-control inputs and capability evidence. |
| `desired-post-state-bytes` | Exact desired post-state bytes. |
| `expires-at-source-value` | Expiry source value. |
| `read-back-method` | Authoritative read-back method. |
| `duplicate-materiality` | Whether concurrent duplication is material. |
| `residual-risk-evidence` | Evidence for remaining irreversible risk. |

Preparation contains source fields only. It does not contain a canonical block, canonical
digest, owner approval, consumption record, or execution attempt. Release Agent validates the
source fields, constructs the [canonical release request](#canonical-release-request), and
returns its digest, [owner rendering](#owner-rendering), pre-dispatch read-back,
duplicate-control decision, uncertainty, and `blocked`, `reconciled`, or `prepared`.

Push, tag creation, pull-request creation, merge, deploy, publish, and release are distinct
`action-kind` values. One provider action submission is one authenticated provider mutation
request intended to create or change the one approved remote object. Release Agent makes at
most one provider action submission for one valid execution handoff.

Execution receives these immutable fields in this exact order:

| Field | Meaning |
| --- | --- |
| `canonical-release-request` | The exact approved canonical request bytes. |
| `canonical-release-digest` | Lowercase SHA-256 of the complete canonical bytes. |
| `reviewed-commit-and-review-evidence` | Exact reviewed commit and review evidence. |
| `action-kind` | The approved distinct action kind. |
| `target` | The approved exact target. |
| `provider-capabilities` | Authenticated provider capability evidence. |
| `pre-submission-read-back` | Current authoritative pre-submission state. |
| `owner-approval-record` | Exact owner approval for digest, action, and target. |
| `clock-evidence` | First authenticated UTC sample plus the authenticated second-clock source and requirement for the immediate pre-submission sample. |
| `verified-consumption-record` | Verified one-use consumption before dispatch. |
| `execution-attempt-identity` | Unique attempt identity. |
| `duplicate-control-decision` | Provider control and race decision. |
| `action-ledger-state` | Ledger state for this approval and attempt. |
| `required-post-state-read-back` | Required post-submission state evidence. |

The Orchestrator creates the execution handoff only after exact owner approval and verified
one-use consumption. It copies the immutable approved block and digest. It never reconstructs
canonical bytes from source fields and never replays an execution handoff. Missing, stale,
changed, expired, or mismatched content blocks submission.

### Canonical release request

The canonical request is one inert block. Hash and present its exact UTF-8 bytes, including
both markers and exactly one final LF, in this field order:

```text
-----BEGIN OLYMPUS RELEASE REQUEST-----
schema: MQ
action-kind: <value>
provider: <value>
account-or-tenant: <value>
repository-or-service: <value>
target: <value>
reviewed-commit: <value>
artifact-digest: <value>
remote-object-identity: <value>
provider-request-bytes: <value>
provider-options-bytes: <value>
concurrency-control-bytes: <value>
desired-post-state-bytes: <value>
expires-at: <value>
-----END OLYMPUS RELEASE REQUEST-----
```

The block has exactly 16 lines. It uses UTF-8 bytes restricted to ASCII, LF line endings, no
byte-order mark, no CR, no blank line, no trailing space, one `: ` separator, and exactly one
LF after the end marker. `schema: MQ` is fixed and decodes to `1`. Every other value is the
exact source bytes encoded as unpadded RFC 4648 base64url. Only `artifact-digest`,
`provider-request-bytes`, and `concurrency-control-bytes` may use `-` or semantically valid
`~`; every other field, including the mandatory `remote-object-identity`, is non-empty.
The single invalid-base64url sentinel `~` denotes a present empty byte string, and `-` denotes
absence only for those three fields. Empty is valid only when the source-field semantics permit
it.

`remote-object-identity` is mandatory and non-empty. `artifact-digest`,
`provider-request-bytes`, and `concurrency-control-bytes` are each a non-empty encoded value,
`~` for a present empty byte string where empty is semantically valid, or `-` for absence. No
other canonical field permits either sentinel. The full reviewed commit, remote object identity,
complete provider-options bytes with every material option and default, desired post-state, and
UTC expiry remain part of the request identity.

Base64url and the sentinels keep raw newlines and marker text inert. Reject invalid alphabet,
padding, a disallowed sentinel, duplicate or reordered fields, extra bytes, missing final LF,
multiple markers, missing or extra canonical lines, or decoded data that does not match the
owner rendering. Any changed source byte, option or default, payload, commit, digest, target,
desired state, concurrency control, presence, absence, or expiry changes the canonical bytes
and lowercase SHA-256 digest. Identical blocks with `~` and `-` in the same optional field have
distinct bytes and distinct digests. Arbitrary source bytes, including invalid UTF-8 and
non-text bytes, are encoded as bytes and do not change these rules.

### Owner rendering

Decode each canonical value to its exact source bytes, then emit exactly 14 ASCII rendering
lines in the same field order, with one LF after every line and no other bytes:

```text
schema: hex:31
action-kind: hex:<lowercase hexadecimal>
provider: hex:<lowercase hexadecimal>
account-or-tenant: hex:<lowercase hexadecimal>
repository-or-service: hex:<lowercase hexadecimal>
target: hex:<lowercase hexadecimal>
reviewed-commit: hex:<lowercase hexadecimal>
artifact-digest: hex:<lowercase hexadecimal>
remote-object-identity: hex:<lowercase hexadecimal>
provider-request-bytes: hex:<lowercase hexadecimal>
provider-options-bytes: hex:<lowercase hexadecimal>
concurrency-control-bytes: hex:<lowercase hexadecimal>
desired-post-state-bytes: hex:<lowercase hexadecimal>
expires-at: hex:<lowercase hexadecimal>
```

For an exact canonical `~`, emit `<field-name>: hex:`. For optional `-`, emit
`<field-name>: absent`. Thus `hex:` round-trips only to present empty `~`, and `absent`
round-trips only to absent `-`. The two forms never round-trip to each other. Use exactly two
lowercase hex digits per source byte and no separator. Never emit raw decoded text. Reject
uppercase or odd hex, extra space, reordered, duplicate, missing, or extra rendering lines,
invalid `absent`, missing or extra final LF, or any rendering mismatch. The rendering cannot
emit raw C0 or C1 controls, DEL, NUL, bidirectional-control UTF-8, newlines, marker text,
invalid UTF-8, or other non-text bytes. Present the complete rendering adjacent to the exact
canonical block and digest. The block remains the approved and hashed authority.

### Phased release results

Apply each phase table in strict first-match order and stop at the first matching row. A
missing, unreadable, stale, internally inconsistent, or unauthenticated required evidence
item is an evidence defect. It overrides an exact-state claim.

| Phase | Order | Condition | Result |
| --- | --- | --- | --- |
| `pre-dispatch` | 1 | Any preparation or required read-back evidence defect. | `blocked` |
| `pre-dispatch` | 2 | Authoritative read-back proves the exact desired state. | `reconciled` |
| `pre-dispatch` | 3 | Authoritative read-back proves target identity absent and all preparation checks pass. | `prepared` |
| `pre-dispatch` | 4 | Target identity exists with any non-exact state, or no row above matches. | `blocked` |
| `dispatch/final-readback` | 1 | Any request, approval, clock, consumption, handoff, ledger, capability, or final-read-back evidence defect. | `blocked` |
| `dispatch/final-readback` | 2 | Authoritative final pre-submission read-back proves the exact desired state. | `reconciled`; approval stays consumed; submit nothing. |
| `dispatch/final-readback` | 3 | Authoritative read-back proves absence, required concurrency controls are ready, and all checks pass. | Make one provider action submission and enter `post-submission`; no terminal release state yet. |
| `dispatch/final-readback` | 4 | Target identity exists with non-exact state, or no row above matches. | `blocked` |
| `post-submission` | 1 | Any required response or post-state evidence defect. | `blocked`, even if another source claims exact state. |
| `post-submission` | 2 | Provider proves this attempt created the new action and exact read-back succeeds. | `released` |
| `post-submission` | 3 | Provider returns a conditional or precondition conflict that proves a concurrent creator won, and exact read-back succeeds. | `reconciled` |
| `post-submission` | 4 | Submission outcome is ambiguous and exact read-back succeeds. | `reconciled`; origin stays uncertain. |
| `post-submission` | 5 | Ordinary rejection, including rejection followed by exact state without provider proof of a winning conditional conflict. | `blocked` |
| `post-submission` | 6 | Conditional conflict with mismatched state, ambiguous mismatch, definite mismatch, or no row above matches. | `blocked` |

These are per-action release-result states, not goal states. Pre-dispatch reconciliation uses
only pre-submission evidence. Post-submission `reconciled` requires exact final state plus a
winning conditional-conflict proof or an exact read-back after an ambiguous outcome. Ordinary
rejection never reconciles. Definite created-action evidence plus exact read-back is the only
path to `released`; a conditional conflict with mismatch, an ambiguous mismatch, or unreadable
evidence is `blocked`.

### Approval, clocks, and duplicate control

One owner approval covers one canonical digest, one action kind, and one target. Record owner
identity, exact approval response or response identity, digest, action, target, observed
approval time, and one-use scope. `expires-at` decodes to valid UTC
`YYYY-MM-DDTHH:MM:SSZ`. Immediately before consumption, record the native host or provider
UTC clock source, raw output, and parsed first sample. Approval is valid only when
`observed < expires-at`; equality is expired. Verify unconsumed status, then record and
verify digest, approval identity, execution-attempt identity, and consumption time before
dispatch. After final read-back and all other dispatch gates pass, obtain and record the
authenticated second UTC clock sample immediately before the one provider action submission.
It must be earlier than expiry. Expiry or clock failure after consumption blocks submission and
does not restore approval. A valid time one second before expiry is allowed; equality and any
later time are expired. An invalid or failed first clock blocks consumption. An invalid or
failed second clock blocks submission. A consumed approval or a failed consumption record
blocks dispatch. Exact approval is required; bundled, missing, changed digest, changed action,
or changed target approval is not exact. The per-action result records the second sample's
authenticated source, raw output, and parsed time.

The Orchestrator records an action ledger for each approval and attempt. Before submission,
`submitted` or `ambiguous` for that attempt or consumed approval blocks a second submission.
An ambiguous ledger state is itself a blocking evidence state.
After any possible provider action submission, never submit again from that execution handoff.
Reconcile before submission and read back after it. Authenticated read-only clock,
capability, pre-submission, final, and post-submission calls are evidence calls; they are not
provider action submissions and do not consume the one-submission allowance.

An own second provider action submission is blocked. A `submitted` or `ambiguous` ledger state
is blocked before any retry. A retry with an old approval is invalid; a retry with new exact
approval still needs a new attempt and prior absence or safe-idempotency evidence.

When concurrent duplication is material, require a provider conditional-write or idempotency
primitive bound to the canonical digest. Without that control, block before submission. A
provider conditional conflict that proves a concurrent creator won is detected and contained
by stopping and reading back. Reconcile only an exact desired-state match. Block a mismatch.
Do not claim control over independent actors or provider defects. Record prevention, detection,
containment, recovery, and residual risk.

Every submitted or ambiguous attempt remains consumed. A retry requires a new canonical request
when any byte changes, new exact owner approval, a new attempt, and evidence that the prior
action is absent or the provider idempotency primitive makes the retry safe. Never retry an
unknown outcome blindly.

### Blocked recovery

Every `blocked` release result records cause, phase, last verified state, recovery owner,
exact closure evidence, safe retry condition, uncertainty, and irreversible residual risk.
There is no automatic rollback. Compensation is a new external action with its own source-only
preparation handoff, canonical request, exact owner approval, one-use consumption, and
immutable execution handoff. The owner retains irreversible residual risk.

## Owner-selected workflow

The owner can request one narrow role allowlist and one request boundary. The declarations are
plain text, not an invocation list or graph language:

```text
Custom workflow: <canonical role name>, ...
Request boundary: review-only|diagnose-only|audit-only|spec-only|mutation
```

Permit at most one `Custom workflow:` line and at most one `Request boundary:` line. Role
names must be unique canonical names in R1 order, and Orchestrator is required. No custom line
uses the default graph. Duplicate, conflicting, malformed, or ambiguous declarations are
`invalid`, dispatch no worker, and require a corrected owner request.

Zero custom declarations and zero boundary declarations use the default graph and boundary.
Zero custom workflow declarations with one valid boundary use the default graph constrained by
that boundary. One valid custom workflow declaration with zero boundary declarations uses the
selected allowlist under the request's default boundary. One valid declaration of each kind
uses the owner selection. Two workflow lines, two boundary lines, an unknown boundary, duplicate,
reordered, malformed, conflicting, or ambiguous role declaration is `invalid`. A selected but
untriggered role does not run. A missing paired verifier or reviewer is invalid. A later trigger
is handled only as `pending-expansion`.

The following five request boundaries are exhaustive. For a custom selection, an incompatible
role makes the selection invalid. For the default graph, routing truncates incompatible roles
before trigger evaluation.

| Boundary | Allowed effects | Terminal artifact | Required roles and checks | Incompatible roles |
| --- | --- | --- | --- | --- |
| `review-only` | Read frozen artifacts and evidence; no mutation, plan, release preparation, or external action | Complete review verdict or finding set, including empty | Applicable Claims Reviewer, Spec Reviewer, Reviewer, or Design Reviewer; frozen identity and read-only checks | System Configurer, Spec Writer, Plan Writer, Plan Verifier, Builder, Docs Writer, Release Agent |
| `diagnose-only` | Reproduce, trace, and explain; no proposal, plan, mutation, review verdict, advice, or external action | Cause, sink, expected behavior, smallest test boundary, evidence, and uncertainty | Explorer when repository evidence is material; read-only reproduction and trace checks | System Configurer, Spec Writer, Claims Reviewer, Spec Reviewer, Plan Writer, Plan Verifier, Builder, Docs Writer, Reviewer, Design Reviewer, Decision Council, Release Agent |
| `audit-only` | Enumerate and assess the stated population read-only; no proposal, plan, mutation, advice, or external action | Complete scoped findings, including explicit empty set and limits | Explorer; population or absence probes and exact source identity | System Configurer, Spec Writer, Claims Reviewer, Spec Reviewer, Plan Writer, Plan Verifier, Builder, Docs Writer, Reviewer, Design Reviewer, Decision Council, Release Agent |
| `spec-only` | Explore when blocked, write and review the specification; no plan, mutation, delivery, or external action | Accepted specification body and hash, or blocked specification | Spec Writer, fresh Claims Reviewer, fresh Spec Reviewer; intake, bounded review, and acceptance checks | System Configurer, Plan Writer, Plan Verifier, Builder, Docs Writer, Reviewer, Design Reviewer, Release Agent |
| `mutation` | Perform the approved local goal; release execution remains a separately owner-approved stage | Reviewed local mutation or commit, plus any separately authorized per-action release result | Every fixed trigger; accepted artifacts, implementation checks, fresh Reviewer, conditional Docs Writer and Design Reviewer, final Git checks | none by boundary; untriggered roles still do not run |

Selection is an allowlist. Invoke a selected role only when its fixed trigger holds. A valid
selection includes every initially triggered role and paired verifier or reviewer. Record
selected roles, boundary, ordered required handoffs, excluded roles, support evidence, and
completion evidence. A later unselected trigger is `pending-expansion`; stop before handoff.
The owner must approve one exact revised selection. Rejection makes the goal `blocked`, and
only explicit owner cancellation makes it `cancelled`.

No boundary or selection bypasses a fixed trigger, paired verifier, fresh mutation review,
Configurer double opt-in, exact owner approval and execution handoff, protected path,
bounded-loop cap, support gate, or sole-hub routing. The Orchestrator records declaration
bytes, selection, boundary, trigger closure, exclusions, handoffs, support, completion,
later-trigger evidence, and expansion decisions in the task record. It does not add a
PROJECT setting, preset registry, executable parser, runtime, or peer edge.

## 5. Bounded handoffs

Every packet contains only the information needed by the receiving role.

- Configurer receives the owner request, repository evidence, configuration template, and
  double-opt-in state.
- Explorer receives one question, path scope, revision, relevant documentation, and
  allowed read-only commands.
- Spec Writer receives the goal boundary, source/base revision, paths, evidence,
  validation obligations, source requirements, fixed controls, and owner or permission
  boundaries. On repair it also receives the current body and open finding ledger. It never
  receives earlier bodies or full reviewer reports. It returns the complete current
  specification body only to the Orchestrator.
- Claims Reviewer receives the complete persisted current specification body, packet
  identifier, content hash, current task metadata, current evidence, and the open finding
  ledger. It first acknowledges intake, then returns the complete facts-and-evidence finding
  set only to the Orchestrator. It does not assess design or acceptance structure.
- Spec Reviewer receives the same immutable current body, identifier, hash, task metadata,
  and open finding ledger. It first acknowledges intake, then returns the complete
  specification finding set only to the Orchestrator. It does not re-probe facts after shared
  intake.
- Plan Writer receives the accepted contract or specification verbatim plus boundary,
  evidence, and validation. It returns an ordered plan only to the Orchestrator.
- Plan Verifier receives that same contract plus the complete persisted plan, packet
  identifier, content hash, paths, interfaces, validation, and prior findings only for
  repair context.
- Builder receives the goal, accepted contract, accepted specification or plan, allowed
  paths, evidence, owner decisions, validation commands, and the accepted plan identifier
  and hash when a plan exists.
- Docs Writer receives the complete behavior diff, the accepted contract, approved docs,
  and relevant link-check commands.
- Reviewer receives the goal boundary, complete current mutation diff, role results,
  checks, project instructions, and prior findings only for repair context.
- Design Reviewer receives the complete relevant mutation diff, accepted criteria, project
  design standards, matching details, and validation evidence.
- Release Agent receives the source-only preparation handoff or the immutable execution
  handoff, never both as one packet. It returns only the release result to the Orchestrator.
- Decision Council receives one balanced question, viable options, constraints, evidence,
  and owner boundary. It returns advice only to the Orchestrator.
- Liaison receives the current task record, artifacts, Git evidence, and one human
  question. It returns an answer only to the Orchestrator.

Packets can narrow scope or add evidence. They cannot widen authority. The Orchestrator
records compact accepted results and ledger rows in the task record. Whole conversations,
earlier bodies, body diffs, reviewer transcripts, and full review history are not task state.
The specification and planning brackets add no new engine or peer edge.

## 6. Git and multiple goals

Use a clean current checkout or branch for one sequential goal when project policy
permits it. Use a worktree for concurrent work or when the current checkout contains
unrelated dirty state. A worktree starts from committed content. If dirty work is
relevant, the owner must first commit it or explicitly include it in the goal's
current-checkout scope. Never pretend uncommitted work followed a new worktree.

Each active goal has its own task record. Compare paths and shared interfaces before
running goals together. Serialize overlapping work. Worktrees isolate files and indexes;
they do not prevent semantic conflicts.

Stage named paths only. Preserve unrelated owner work. Do not reset, stash, amend, or
delete work to recover from a failed Olympus step. Record the current state and stop
as `blocked` when safe continuation is unclear.

Local Git commits persist only in that clone. Cross-host or public persistence requires
normal repository synchronization and fresh owner approval for the remote action.

## 7. Owner decisions and external actions

Routine work inside the approved goal can read, edit, check, create a branch or worktree,
and create a local commit under project policy.

Stop and ask the owner before:

- a major scope or architecture choice not settled by acceptance criteria;
- push, pull-request creation, merge, deploy, publish, or release;
- force operations, remote deletion, secret changes, or destructive data changes;
- a new external service, paid resource, or hard-to-reverse effect.

Before an approved external action, record the exact action, target, owner approval scope,
and a client correlation or idempotency key when the provider supports one. After the
action, record any provider-issued identity that is observed. After an uncertain result,
do not infer success or retry. Read back provider state and reconcile it with the exact
requested object first. Record the observed response, reconciliation evidence, and
remaining uncertainty. A bounded retry needs evidence that the first action did not
succeed or is safely idempotent.

Only an owner-approved Configurer proposal can change project configuration, custom
instructions, or distilled role evolutions. Never change an active goal's rules in place.

Ambient skills, memory, and host setup can help locate evidence. They do not grant
authority or replace current repository checks. PROJECT and current repository evidence
remain the project sources of truth. Olympus does not manage the host's ambient setup.
