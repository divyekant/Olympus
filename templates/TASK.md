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
| 13 | Decision Council | `<unresolved material trade-off>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 14 | Liaison | `<human status or explanation request>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |

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
| Builder, Docs Writer, Reviewer, and Design Reviewer | `<counts and verdicts>` |
| Configuration review | `<pass, blocked, or not used>` |
| Council and Liaison | `<results or not used>` |
| Review aggregation | `<pass only when every invoked reviewer passes>` |
| owner corrections | `<count and summary>` |
| remaining uncertainty | `<none or exact limit>` |

Do not mark a mutation `complete` without a fresh Reviewer `pass` and final relevant
verification. Read-only tasks do not need a mutation review.
