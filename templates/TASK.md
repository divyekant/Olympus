---
record: olympus-task
schema: 1
status: planned
---

# Olympus task: `<goal-id>`

The Orchestrator is the sole owner of this record. Every role returns bounded results only
to it.

## Goal and scope

| Field | Value |
| --- | --- |
| owner request | `<request>` |
| created at | `<time>` |
| framework commit | `<full commit>` |
| PROJECT revision | `<revision>` |
| source base | `<commit>` |
| isolation | `<current checkout, branch, or worktree path>` |

### Role population and support

Record the predicted and actual roles in fixed catalog order. Record one mapping for every
invoked role before dispatch.

| # | Role | Trigger result | Predicted | Actual | Harness mapping, freshness, tools, support, and evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Orchestrator | every routed request | `<yes>` | `<yes>` | `<mapping and evidence>` |
| 2 | System Configurer | `<owner config request and double-opt-in flow>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 3 | Explorer | `<material question or explicit audit>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 4 | Spec Writer | `<substantial or other trigger>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 5 | Claims Reviewer | `<every Spec Writer result>` | `<yes/no>` | `<yes/no>` | `<fresh mapping and evidence>` |
| 6 | Spec Reviewer | `<every Spec Writer result>` | `<yes/no>` | `<yes/no>` | `<fresh mapping and evidence>` |
| 7 | Plan Writer | `<dependent or cross-layer steps or explicit need>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 8 | Plan Verifier | `<every Plan Writer result>` | `<yes/no>` | `<yes/no>` | `<fresh mapping and evidence>` |
| 9 | Builder | `<every non-configuration mutation>` | `<yes/no>` | `<yes/no>` | `<separate mapping and evidence>` |
| 10 | Docs Writer | `<false tracked docs or sync contract>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 11 | Reviewer | `<every project or configuration mutation>` | `<yes/no>` | `<yes/no>` | `<fresh mapping and evidence>` |
| 12 | Design Reviewer | `<material user-facing change>` | `<yes/no>` | `<yes/no>` | `<fresh mapping and evidence>` |
| 13 | Release Agent | `<owner-requested release preparation, reconciliation, or external action>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 14 | Decision Council | `<unresolved material trade-off>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 15 | Liaison | `<human status or explanation request>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |

Missing required mapping blocks dispatch. Use `supported`, `unsupported`, or `untested`.

## Shared state checkpoints

Record the fields below at the named transition. Apply the meanings in the [shared state
and evidence rules](../references/PROTOCOL.md#shared-state-and-evidence-rules); do not
replace them with role-specific labels.

| Checkpoint | Required record |
| --- | --- |
| request boundary | `<review-only, diagnose-only, audit-only, spec-only, or mutation; terminal boundary and truncated stages>` |
| frozen review unit | `<spec body id/hash, plan id/hash, or mutation task/base/branch/worktree/base/head/merge-base/paths/diff digest, as applicable>` |
| transition evidence | `<role identity; packet identity; Git state; required checks; evidence verified by Orchestrator>` |
| halted outcome | `<attempt id; operational/runtime cause; partial-output disposition; last verified state; recovery owner; safe retry; completed review rounds consumed: 0>` |
| pending outcome | `<every applicable cause; owner; closure evidence; safe retry; consequence; all required causes cleared: yes/no>` |
| dispute round | `<unchanged unit; evidence; fresh reviewer; withdraw/maintain result; owner/escalation if maintained>` |
| re-plan | `<hidden complexity or new trigger; affected steps; new evidence; attempt 1; second same-node stall escalation>` |
| skipped/unrunnable classification | `<role/check; reason; required capability; consequence; no substitution>` |
| skipped/unrunnable delivery | `<role/check; final reason; result omitted or blocked; user-visible consequence>` |
| escaped external finding | `<finding and evidence; future framework-gap assessment; active-goal rules unchanged>` |
| uncertain external action | `<exact action/target; approval; client key when supported; observed provider id when available; response; read-back and reconciliation; retry decision>` |

## Release boundary records

Use the [canonical release boundary](../references/PROTOCOL.md#release-boundary). Release
records are per action and do not change goal state. Preparation and execution are separate
handoffs. The Orchestrator owns approval, consumption, dispatch, aggregation, and this record.

### Preparation handoff

Record only source fields in this exact order. Do not reconstruct or accept a canonical block,
digest, approval, consumption record, or execution attempt in this handoff.

| Field | Required record |
| --- | --- |
| `goal-and-packet-identity` | <goal identifier and packet identity> |
| `reviewed-commit-and-review-evidence` | <full reviewed commit and complete review evidence> |
| `final-checks-and-current-git-state` | <final checks and current Git state> |
| `action-kind` | <push, tag-creation, pull-request-creation, merge, deploy, publish, or release> |
| `provider` | <provider identity> |
| `account-or-tenant` | <account or tenant> |
| `repository-or-service` | <repository or service> |
| `target` | <exact remote target> |
| `artifact-digest` | <exact digest bytes; non-empty, `~`, or `-` as source semantics permit> |
| `remote-object-identity` | <mandatory non-empty remote object identity> |
| `provider-request-bytes` | <exact provider request bytes; non-empty, `~`, or `-` as source semantics permit> |
| `provider-options-bytes` | <complete non-empty material options and defaults> |
| `concurrency-control-bytes` | <control inputs and capability evidence; non-empty, `~`, or `-` as source semantics permit> |
| `desired-post-state-bytes` | <exact non-empty desired post-state bytes> |
| `expires-at-source-value` | <expiry source value> |
| `read-back-method` | <authoritative read-back method> |
| `duplicate-materiality` | <whether concurrent duplication is material> |
| `residual-risk-evidence` | <remaining irreversible risk evidence> |

### Execution handoff

Record an execution handoff only after exact owner approval and verified one-use consumption.
Copy the immutable approved block and digest without reconstruction. The handoff never
reconstructs canonical bytes from source fields and never replays an execution handoff. Missing, stale,
changed, expired, or mismatched content blocks submission. Record these immutable fields in
this exact order:

| Field | Required record |
| --- | --- |
| `canonical-release-request` | <exact approved canonical request bytes> |
| `canonical-release-digest` | <lowercase SHA-256 of complete canonical bytes> |
| `reviewed-commit-and-review-evidence` | <exact reviewed commit and review evidence> |
| `action-kind` | <approved distinct action kind> |
| `target` | <approved exact target> |
| `provider-capabilities` | <authenticated provider capability evidence> |
| `pre-submission-read-back` | <current authoritative pre-submission state> |
| `owner-approval-record` | <owner, exact response or identity, digest, action, target, time, one-use scope> |
| `clock-evidence` | <authenticated first-clock source, raw output, parsed first sample, and authenticated second-clock source and requirement for the immediate pre-submission sample> |
| `verified-consumption-record` | <unconsumed check, digest, approval identity, attempt identity, and consumption time> |
| `execution-attempt-identity` | <unique attempt identity> |
| `duplicate-control-decision` | <conditional-write or idempotency support and race decision> |
| `action-ledger-state` | <approval and attempt ledger state> |
| `required-post-state-read-back` | <required post-submission state evidence> |

### Canonical request and owner rendering

Hash and present the exact 16-line canonical block, including both markers and exactly one
final LF. Every value after `schema: MQ` is exact source bytes encoded as unpadded RFC 4648
base64url. Only `artifact-digest`, `provider-request-bytes`, and `concurrency-control-bytes`
may use `-` or semantically valid `~`; every other field, including the mandatory
`remote-object-identity`, is non-empty.

`remote-object-identity` is mandatory and non-empty. `artifact-digest`,
`provider-request-bytes`, and `concurrency-control-bytes` are each a non-empty encoded value,
`~` for a present empty byte string where empty is semantically valid, or `-` for absence. No
other canonical field permits either sentinel. Keep the full reviewed commit, remote object
identity, complete provider-options bytes with every material option and default, desired
post-state, and UTC expiry in the request identity.

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

The bytes are ASCII UTF-8 with LF endings, no byte-order mark, no CR, no blank line, no trailing
space, extra bytes, duplicate or reordered fields, missing or extra canonical lines, multiple
markers, padding, or invalid base64url. The lowercase SHA-256 covers the complete block bytes.
Reject invalid alphabet, a disallowed sentinel, and any changed source byte. Identical blocks
with `~` and `-` in the same optional field have distinct bytes and distinct digests. Arbitrary
source bytes, including invalid UTF-8 and non-text bytes, are encoded as bytes.

Present the exact block and digest adjacent to this 14-line ASCII hexadecimal rendering:

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

Render `~` as `hex:` and `-` as `absent`. Use two lowercase hex digits per source byte.
Never emit raw decoded text. Reject unsafe bytes, uppercase or odd hex, invalid `absent`,
reordered, duplicate, missing, or extra rendering lines, extra space, missing or extra final
LF, or any rendering mismatch. Reject CR and trailing space. The rendering cannot emit raw C0
or C1 controls, DEL, NUL, bidirectional-control UTF-8, newlines, marker text, invalid UTF-8,
or other non-text bytes.

### Approval, phase, and result records

One owner approval covers one canonical digest, one action kind, and one target. Approval is
valid only when the first authenticated UTC sample satisfies `observed < expires-at`.
Equality is expired. Record the first sample before consumption and, after final read-back and
all other dispatch gates pass, obtain and record the authenticated second UTC sample immediately
before the one provider action submission. If either clock fails or expiry occurs after
consumption, block and keep the approval consumed. A valid time one second before expiry is
allowed; equality and any later time are expired. An invalid or failed first clock blocks
consumption. An invalid or failed second clock blocks submission. A consumed approval or a
failed consumption record blocks dispatch. Exact approval is required; bundled, missing,
changed digest, changed action, or changed target approval is not exact. The result record
includes the second sample's authenticated source, raw output, and parsed time.

| Field | Required record |
| --- | --- |
| `phase` | <pre-dispatch, dispatch/final-readback, or post-submission> |
| `last-verified-state` | <exact provider and local state before this result> |
| `duplicate-control-decision` | <prevention, detection, containment, provider control, or block> |
| `action-ledger-state` | <unsubmitted, submitted, ambiguous, or reconciled state with attempt identity> |
| `provider-action-submission-count` | <zero or one; read-only evidence calls do not count> |
| `result` | <blocked, reconciled, prepared, or released> |
| `uncertainty` | <exact unknown or none> |
| `irreversible-residual-risk` | <owner-retained risk> |
| `recovery-owner` | <owner or named recovery owner> |
| `closure-evidence` | <exact evidence needed to close the block> |
| `safe-retry-condition` | <new approval, new attempt, absence or safe idempotency evidence> |

Apply the phase rows in strict first-match order. An evidence defect overrides an exact-state
claim in every phase:

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

Definite created-action evidence plus exact read-back is the only path to `released`. Ordinary
rejection never reconciles. A conditional conflict with mismatch, an ambiguous mismatch, or
unreadable evidence is `blocked`.

### Duplicate and recovery record

Authenticated read-only clock, capability, pre-submission, final, and post-submission calls
are evidence calls. They are not provider action submissions and do not consume the one
submission allowance. A submitted or ambiguous ledger state blocks a second submission from
the handoff. When concurrent duplication is material, absence of a provider conditional-write
or idempotency primitive blocks submission. Every submitted or ambiguous attempt remains
consumed. A retry needs new exact approval, a new attempt, and prior absence or safe
idempotency evidence.

An own second provider action submission is blocked. A `submitted` or `ambiguous` ledger state
is blocked before any retry. A retry with an old approval is invalid; a retry with new exact
approval still needs a new attempt and prior absence or safe-idempotency evidence.

Without that control, a material concurrent race blocks before submission. Unreadable,
conflicting, or mismatched evidence is also `blocked` by phase precedence.

Every `blocked` result records cause, phase, last verified state, recovery owner, closure
evidence, safe retry condition, uncertainty, and irreversible residual risk. There is no
automatic rollback.
Compensation is a new external action with a new preparation handoff, canonical request,
approval, consumption, and execution handoff. The owner retains irreversible residual risk.

## Custom workflow closure

An owner may provide at most one exact declaration of each kind:

```text
Custom workflow: <canonical role name>, ...
Request boundary: review-only|diagnose-only|audit-only|spec-only|mutation
```

Role names are unique, canonical R1 names in fixed order, and Orchestrator is required. No
custom declaration selects the default graph. Duplicate, conflicting, malformed, or ambiguous
declarations are `invalid`, dispatch no worker, and require a corrected owner request.

Zero custom declarations and zero boundary declarations use the default graph and boundary.
Zero custom workflow declarations with one valid boundary use the default graph constrained by
that boundary. One valid custom workflow declaration with zero boundary declarations uses the
selected allowlist under the request's default boundary. One valid declaration of each kind
uses the owner selection. Two workflow lines, two boundary lines, an unknown boundary, duplicate,
reordered, malformed, conflicting, or ambiguous role declaration is `invalid`. A selected but
untriggered role does not run. A missing paired verifier or reviewer is invalid. A later trigger
is handled only as `pending-expansion`.

| Field | Required record |
| --- | --- |
| `declaration-bytes` | <exact custom workflow and boundary declaration bytes> |
| `selected-roles` | <unique R1-ordered role allowlist> |
| `boundary` | <one of the five exhaustive boundary values> |
| `initially-triggered-roles` | <fixed-trigger results before selection> |
| `ordered-required-handoffs` | <required packets and receiving roles in order> |
| `excluded-roles` | <roles excluded by boundary or selection, with reason> |
| `support-evidence` | <mapping, freshness, tools, status, and evidence for every invoked role> |
| `completion-evidence` | <terminal artifact and fixed checks> |
| `later-triggers` | <new trigger and evidence, or none> |
| `expansion-decision` | <pending-expansion, exact owner-approved revision, rejected, or cancelled> |
| `invalid-or-blocked-outcome` | <cause, no-dispatch or stop evidence, and next action> |

The five request boundaries are exhaustive. Incompatible roles make a custom selection
`invalid`; default routing truncates those roles before trigger evaluation:

| Boundary | Allowed effects | Terminal artifact | Required roles and checks | Incompatible roles |
| --- | --- | --- | --- | --- |
| `review-only` | Read frozen artifacts and evidence; no mutation, plan, release preparation, or external action | Complete review verdict or finding set, including empty | Applicable Claims Reviewer, Spec Reviewer, Reviewer, or Design Reviewer; frozen identity and read-only checks | System Configurer, Spec Writer, Plan Writer, Plan Verifier, Builder, Docs Writer, Release Agent |
| `diagnose-only` | Reproduce, trace, and explain; no proposal, plan, mutation, review verdict, advice, or external action | Cause, sink, expected behavior, smallest test boundary, evidence, and uncertainty | Explorer when repository evidence is material; read-only reproduction and trace checks | System Configurer, Spec Writer, Claims Reviewer, Spec Reviewer, Plan Writer, Plan Verifier, Builder, Docs Writer, Reviewer, Design Reviewer, Decision Council, Release Agent |
| `audit-only` | Enumerate and assess the stated population read-only; no proposal, plan, mutation, advice, or external action | Complete scoped findings, including explicit empty set and limits | Explorer; population or absence probes and exact source identity | System Configurer, Spec Writer, Claims Reviewer, Spec Reviewer, Plan Writer, Plan Verifier, Builder, Docs Writer, Reviewer, Design Reviewer, Decision Council, Release Agent |
| `spec-only` | Explore when blocked, write and review the specification; no plan, mutation, delivery, or external action | Accepted specification body and hash, or blocked specification | Spec Writer, fresh Claims Reviewer, fresh Spec Reviewer; intake, bounded review, and acceptance checks | System Configurer, Plan Writer, Plan Verifier, Builder, Docs Writer, Reviewer, Design Reviewer, Release Agent |
| `mutation` | Perform the approved local goal; release execution remains a separately owner-approved stage | Reviewed local mutation or commit, plus any separately authorized per-action release result | Every fixed trigger; accepted artifacts, implementation checks, fresh Reviewer, conditional Docs Writer and Design Reviewer, final Git checks | none by boundary; untriggered roles still do not run |

Selection is an allowlist, not an invocation list or graph. Invoke a selected role only when
its fixed trigger holds. A valid selection includes every initially triggered role and paired
verifier or reviewer. A later unselected trigger records `pending-expansion` and stops before
handoff. The owner must approve one exact revised selection. Rejection makes the goal
`blocked`; only explicit owner cancellation makes it `cancelled`. No selection bypasses
support, review, Configurer, owner, protected-path, bounded-loop, or sole-hub gates.

Acceptance criteria:

- `<measurable result>`

Accepted contract or specification after formal review:

- `current specification body in the section below` (or `not required`)

Non-goals:

- `<explicit exclusion>`

| Scope item | Value |
| --- | --- |
| allowed paths | `<paths>` |
| protected paths | `.olympus/`; managed loader blocks; `<other>` |
| relevant project instructions | `<paths or summary>` |
| validation commands | `<commands>` |

## Owner decisions

| Decision | Owner response | Effect |
| --- | --- | --- |
| `<major or external choice>` | `<approval, rejection, or pending>` | `<exact scope>` |

Delete this section when no owner decision was needed after activation.

## Explorer

| Status | Question | Evidence | Answer and uncertainty |
| --- | --- | --- | --- |
| `<used or skipped>` | `<one material question or reason skipped>` | `<paths, commands, file:line>` | `<answer or limit>` |

## Specification rounds

Use this bracket only for substantial, ambiguous, architectural, or cross-layer goals.
Persist the complete current Writer result and update task metadata before reviewer dispatch.
The body between the markers is the only specification body in this record. It must contain
requirements, invariants, acceptance criteria, red paths, and validation obligations. Keep
metadata, packet identifiers, hashes, verdict counts, findings, convergence state, and body
size outside the hashed body. Never put earlier bodies, body diffs, reviewer transcripts,
review history, round records, or defensive annotations in the body.

### Current specification body

| Field | Value |
| --- | --- |
| status | `<complete or exact incomplete state>` |
| packet identifier | `<identifier>` |
| goal identifier | `<goal-id>` |
| source commit | `<full commit>` |
| content hash | `<lowercase SHA-256 of the exact body between the markers below>` |

<!-- SPECIFICATION-BODY:BEGIN -->

`<complete current specification body only, persisted verbatim before reviewer dispatch>`

<!-- SPECIFICATION-BODY:END -->

### Specification intake

| Attempt | Packet identifier | Content hash | Metadata state | Claims acknowledgement | Spec acknowledgement | Handoff state and evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `<n>` | `<identifier>` | `<lowercase SHA-256>` | `<current and persisted, or exact defect>` | `<matching identifier/recomputed hash and required sections, or defect>` | `<matching identifier/recomputed hash and required sections, or defect>` | `<healthy, intake-invalid, formal-review, or blocked; evidence>` |

`intake-invalid` is preserved here as a pre-review result and consumes no round. Start and
reserve a formal round only after both fresh reviewers acknowledge the same immutable
healthy packet. Each reviewer stops after acknowledgement. Record the `formal-review`
authorization, candidate round number, and unique attempt identifier for that exact packet
before either reviewer starts formal work. Consume the round only after both complete
reviewer packets return. Correct and persist an invalid handoff before a new intake attempt.

### Formal review attempts

Record every authorized attempt. A halted attempt remains visible, uses a new identifier
on retry, and consumes no completed formal round. Preserve provisional findings for the
next complete bracket. Permit one automatic retry for the same packet; a second halt
escalates or blocks.

| Attempt identifier | Candidate round | Packet identifier and hash | Claims completion or halted state | Spec completion or halted state | Provisional finding IDs | Operational outcome and recovery | Completed round consumed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `<identifier>` | `<n>` | `<identifier and hash>` | `<complete or halted>` | `<complete or halted>` | `<IDs or none; next-attempt disposition>` | `<none, or cause, partial-output disposition, owner, and safe retry>` | `<yes/no>` |

### Formal specification review

Formal verdicts are `pass`, `repair`, or `blocked`. This table contains completed reviewer
brackets only and is the compact round summary.
Each reviewer returns its complete
jurisdictional finding set in one pass. The Orchestrator merges both sets and freezes the
finding ledger for the round. At the configured cap, open findings block the goal. The
numeric cap applies independently to specification, plan, configuration, and implementation
brackets.

| Round | Packet identifier and hash | Writer result | Claims verdict and finding count | Spec verdict and finding count | Open P0-P2 | Body lines | Body bytes | Merged finding IDs | Aggregated state | Restatement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<n>` | `<identifier and hash>` | `<current body persisted; separate context; no body copy>` | `<pass/repair/blocked; count>` | `<pass/repair/blocked; count>` | `<count>` | `<count>` | `<count>` | `<ledger IDs or none>` | `<pass/repair/blocked>` | `<yes/no; reason>` |

### Finding ledger (Orchestrator-owned)

Keep one compact ledger for the whole specification bracket. Keep findings here, not in the
specification body. The Orchestrator assigns stable IDs, merges both complete reviewer sets,
freezes the rows for each round, routes repairs, and owns state.

| ID | Jurisdiction | Severity | Finding | Minimum evidence and closure condition | State | First seen | Last checked | Later classification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<F-001>` | `<Claims or Spec>` | `<P0/P1/P2/P3>` | `<short finding>` | `<evidence; exact condition that closes it>` | `<open/repaired/accepted/non-blocking>` | `<round>` | `<round>` | `<introduced/missed, or not applicable>` |

P0 and P1 remain open until repaired. P2 remains open until repaired or explicitly accepted
by the owner when the acceptance is within owner authority. P3 is non-blocking. Review
findings can cite the current snapshot by `file:line`; the specification body does not need
self-referential line citations.

### Convergence state

| Field | Value |
| --- | --- |
| current completed formal round | `<0-10>` |
| complete Claims set returned | `<yes/no; count>` |
| complete Spec set returned | `<yes/no; count>` |
| merged ledger frozen | `<yes/no; round>` |
| open P0-P2 count | `<count>` |
| new findings after round 1 | `<introduced/missed IDs, or none>` |
| framework-review failure | `<yes/no; new missed P0/P1 IDs>` |
| next action | `<repair, compact complete restatement, accepted, or blocked>` |

Specification round cap: `10` completed formal rounds (default 10; expected closure is 2-3
rounds).
The current specification body cap is 300 lines and 48,000 bytes. Record both sizes in each
round summary. If round 3 does not reduce open P0-P2 findings, or body size grows without
reducing them, the next Writer result must be a compact complete restatement, not an additive
patch. This does not reset the round count. At completed round 10, remaining P0-P2 findings block
implementation. An oversized Writer result is incomplete and does not enter reviewer intake.

## Plan rounds

Use this bracket only when the accepted contract has dependent steps, cross-layer or
interface sequencing, or an explicit plan need. Plan Writer receives the accepted contract
or specification verbatim. Plan Verifier receives that contract plus the whole plan.

| Round | Plan packet identifier and hash | Plan Writer context | Fresh Plan Verifier context | Verdict | Accepted plan or findings/evidence | Uncertainty |
| --- | --- | --- | --- | --- | --- | --- |
| `<n>` | `<identifier and lowercase SHA-256>` | `<separate context>` | `<fresh context>` | `<verdict>` | `<accepted plan or findings and exact evidence>` | `<none or limit>` |

Plan round cap: `<1, 2, or 3; default 2>`.

Accepted plan:

| Field | Value |
| --- | --- |
| status | `<accepted, incomplete, or not required>` |
| packet identifier | `<identifier or not required>` |
| content hash | `<lowercase SHA-256 of the exact plan body or not required>` |

<!-- PLAN-BODY:BEGIN -->

`<complete accepted plan body only, persisted verbatim before verification, or not required>`

<!-- PLAN-BODY:END -->

## Builder and review rounds

Builder rounds use a separate context:

| Round | Builder | Changed paths and result | Docs claims affected and trigger | Checks and results | Uncertainty |
| --- | --- | --- | --- | --- | --- |
| `<n>` | `<separate context>` | `<result and paths>` | `<claims and Docs Writer yes/no>` | `<commands/results>` | `<none or limit>` |

### Docs Writer results

Record only when its trigger holds.

| Round | Context | Approved docs changed | Claims and links checked | Result and uncertainty |
| --- | --- | --- | --- | --- |
| `<n>` | `<separate context>` | `<paths>` | `<checks/results>` | `<result and limit>` |

Review rounds use a fresh context that did not build the change. Verdicts are `pass`,
`repair`, or `blocked`:

| Round | Reviewer | Verdict | Acceptance checks, findings, and uncertainty |
| --- | --- | --- | --- |
| `<n>` | `<fresh context>` | `<verdict>` | `<criterion results and findings>` |

Round cap: `<1, 2, or 3; default 2>`.

### Configuration review

Record only for a configuration mutation. The Configurer applies the approved unit
uncommitted. Fresh Reviewer pass is required before staging and commit. Hook-changed
content receives a fresh committed-content review.

| Stage | Context | Exact unit and paths | Verdict | Checks, findings, and uncertainty |
| --- | --- | --- | --- | --- |
| uncommitted review | `<fresh context>` | `<PROJECT.md plus managed-loader unit>` | `<pass, repair, or blocked>` | `<checks and evidence>` |
| committed-content rereview | `<fresh context or not required>` | `<hook-changed paths or not required>` | `<pass or not required>` | `<checks and evidence>` |

### Design review

Record whenever the material user-facing design trigger holds. Missing required project
standards or matching evidence produce `blocked`, not `not used`.

| Context | Standards and matching evidence | Verdict | Checks, findings, and uncertainty |
| --- | --- | --- | --- |
| `<fresh context>` | `<sources and paths>` | `<pass, repair, or blocked>` | `<checks and evidence>` |

### Decision Council and Liaison

Record these results only when used. Council advice is not a gate. Liaison is read-only.

| Role | Invocation identity, source revision, and freshness | Question | Result and evidence | Uncertainty |
| --- | --- | --- | --- | --- |
| Decision Council | `<packet id; revision; fresh or degraded context>` | `<one balanced question>` | `<recommendation or not used>` | `<limit>` |
| Liaison | `<packet id; revision; read-only context>` | `<human question>` | `<answer or not used>` | `<limit>` |

## Outcome

Set frontmatter `status` to `complete`, `blocked`, or `cancelled`.

| Field | Result |
| --- | --- |
| final verification | `<commands and results>` |
| changed paths | `<paths>` |
| local commit | `<commit or none>` |
| external action | `<none, pending approval, or approved action>` |
| Explorer | `<used or skipped with reason>` |
| Invoked roles and support evidence | `<predicted/actual mapping summary>` |
| Specification and plan rounds | `<counts and verdicts>` |
| Builder, Docs Writer, Reviewer, Design Reviewer, and Release Agent | `<counts and verdicts>` |
| Configuration review | `<pass, blocked, or not used>` |
| Council and Liaison | `<results or not used>` |
| Review aggregation | `<pass only when every invoked reviewer passes>` |
| owner corrections | `<count and summary>` |
| remaining uncertainty | `<none or exact limit>` |

Do not mark a mutation `complete` without a fresh Reviewer `pass` and final relevant
verification. Read-only tasks do not need a mutation review.
