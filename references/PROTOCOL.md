# Olympus runtime protocol

This is the shared contract for every Olympus goal. It stays small, conditional, and
Markdown-only.

## 1. Fixed catalog

The **Pantheon** is Olympus's fourteen fixed roles in this order. The Orchestrator is the
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
| 13 | Decision Council | unresolved material decision with viable trade-offs | Gives one read-only advisory recommendation. |
| 14 | Liaison | human status or explanation request | Rereads evidence and answers without changing the goal. |

Every role receives from and returns only to the Orchestrator. No role invokes or
communicates with another role. The Orchestrator decides which conditional roles run and
records each invoked role's result.

Only the System Configurer changes `.olympus/PROJECT.md` or managed loader blocks.
Only the Orchestrator writes `.olympus/tasks/<goal-id>.md`. Only the Builder changes
approved non-documentation project paths. Only the Docs Writer changes approved
documentation paths. Claims,
Spec, Plan, Design, and general Reviewers are read-only. Decision Council is
advisory and has no gate. Liaison is read-only and has no gate.

For Olympus dogfood only, an immutable earlier revision can govern a goal that edits a
separate target checkout for a prospective revision. The goal never reloads its own
in-progress edits as instructions.

## 2. Activation

- Manual mode: `Use Olympus for: <goal>` runs one goal.
- Session mode: `Activate Olympus orchestration` routes later project-changing
  requests until session end or deactivation.
- Project mode: PROJECT boot mode `orchestration` activates routing in each new session.
- `Deactivate Olympus orchestration` stops new session routing. It does not cancel an
  active goal or change PROJECT.
- Questions do not create goals. Explicit read-only audits use Explorer.

All three modes use the same goal flow.

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
   evidence. Missing mapping for any required role blocks that path before dispatch.
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
10. When a material decision has viable trade-offs that remain unresolved, the
    Orchestrator may ask Decision Council one balanced read-only question. Its advice is
    recorded but is not a gate and does not replace owner approval. For a high-stakes
    decision, the Orchestrator may use at most three fresh Council invocations for that
    same question. Record each packet separately and do not convert the set into a verdict
    or a new gate. Sequential or same-context execution is degraded independence.
11. For a human status or explanation request, Liaison rereads the current task record,
    artifacts, and Git evidence, answers first, cites evidence, and routes action requests
    back to the Orchestrator.
12. On passing invoked reviews, run final relevant checks and compare the result with
    actual Git state. Do not claim an untested role, harness, or execution as passed.

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
