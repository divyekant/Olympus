---
record: olympus-task
schema: 1
status: planned
---

# Olympus task: `<goal-id>`

The Orchestrator is the sole owner of this record. Every role returns bounded results only
to it. This record stores facts and accepted results; the rules and state meanings live in
the pinned [runtime protocol](../references/PROTOCOL.md) and are not restated here.

## Goal and scope

| Field | Value |
| --- | --- |
| owner request | `<exact owner request bytes>` |
| created at | `<time>` |
| framework commit | `<full commit>` |
| PROJECT revision | `<revision>` |
| strict convergence | `<off or on; explicit or defaulted from omission; the value in force at goal start>` |
| writer reuse | `<reuse or fresh-per-round; explicit or defaulted from omission; the value in force at goal start>` |
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
| 4 | Spec Writer | `<substantial, ambiguous, architectural, cross-layer, or material frontend behavior goal>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 5 | Claims Reviewer | `<every persisted Spec Writer body>` | `<yes/no>` | `<yes/no>` | `<fresh mapping and evidence>` |
| 6 | Spec Reviewer | `<every persisted Spec Writer body>` | `<yes/no>` | `<yes/no>` | `<fresh mapping and evidence>` |
| 7 | Plan Writer | `<dependent or cross-layer steps or explicit need>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 8 | Plan Verifier | `<every Plan Writer result>` | `<yes/no>` | `<yes/no>` | `<fresh mapping and evidence>` |
| 9 | Builder | `<every non-configuration mutation>` | `<yes/no>` | `<yes/no>` | `<separate mapping and evidence>` |
| 10 | Docs Writer | `<false tracked docs or sync contract>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 11 | Reviewer | `<every project or configuration mutation>` | `<yes/no>` | `<yes/no>` | `<fresh mapping and evidence>` |
| 12 | Design Reviewer | `<material frontend behavior>` | `<yes/no>` | `<yes/no>` | `<fresh mapping and evidence>` |
| 13 | Release Agent | `<owner-requested release preparation, reconciliation, or external action>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 14 | Decision Council | `<unresolved material trade-off>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |
| 15 | Liaison | `<human status or explanation request>` | `<yes/no>` | `<yes/no>` | `<mapping and evidence>` |

Missing required mapping blocks dispatch. The Spec Writer row records that role's
mapping, context record, and support evidence; the per-attempt continuity log is the
`writer continuity` row. Use `supported`, `unsupported`, or `untested`.

## Shared state checkpoints

Record the fields below at the named transition. Apply the meanings in the [shared state
and evidence rules](../references/PROTOCOL.md#shared-state-and-evidence-rules); do not
replace them with role-specific labels.

| Checkpoint | Required record |
| --- | --- |
| request boundary | `<review-only, diagnose-only, audit-only, spec-only, or mutation; terminal boundary and truncated stages>` |
| frontend pre-bracket clean gate | `<material frontend only: source checkout path supplying the base and committed HEAD, exact approved Builder and Docs Writer allowed-path set, Git output before worktree creation, pass or stopped/new-goal result; worktree path and path/source recheck before Builder dispatch; protected Olympus task/config state and unrelated paths excluded>` |
| frontend commit and hook checkpoint | `<material frontend only: exact pre-commit Git state, named-path commit, exact post-hook Git state, pre-commit-working-bytes-to-post-hook-working-bytes delta, owning-role validation of hook-mutated paths, cumulative identity refreshed from committed bytes, and second-commit hook result or blocked outcome>` |
| frozen review unit | `<complete final mutation identity or artifact identity, as applicable; when accepted frontend scenarios exist, interaction-set identity (ordered stable scenario IDs plus the accepted specification packet identifier/hash that contains the complete scenario set, plus the accepted plan packet identifier/hash when a plan exists), verified frontend packet identifier/digest, implementation-bracket baseline, frontend commit and hook checkpoint reference, Builder round deltas with pre/post Git states and cumulative Builder-owned identity, Docs Writer round deltas with pre/post Git states and cumulative Docs Writer-owned identity (empty when Docs Writer did not run), and the disjoint union of both cumulative identities equaling the complete final mutation identity>` |
| transition evidence | `<role identity; packet identity; Git state; required checks; evidence verified by Orchestrator>` |
| halted outcome | `<operational/runtime cause; partial-output disposition; last verified state; recovery owner; safe retry; completed review rounds consumed: 0>` |
| pending outcome | `<every applicable cause; owner; closure evidence; safe retry; consequence; all required causes cleared: yes/no>` |
| dispute round | `<unchanged unit; evidence; fresh reviewer; withdraw/maintain result; owner/escalation if maintained>` |
| re-plan | `<hidden complexity or new trigger; affected steps; new evidence; attempt 1; second same-node stall escalation>` |
| skipped/unrunnable classification | `<role/check; reason; required capability; consequence; no substitution>` |
| skipped/unrunnable delivery | `<role/check; final reason; result omitted or blocked; user-visible consequence>` |
| escaped external finding | `<finding and evidence; future framework-gap assessment; active-goal rules unchanged>` |
| uncertain external action | `<exact action/target; approval; client key when supported; observed provider id when available; response; read-back and reconciliation; retry decision>` |

## Release boundary records

Use the [release boundary](../references/PROTOCOL.md#release-boundary). Release records
are per action and do not change goal state. Record one table per action:

| Field | Required record |
| --- | --- |
| `action-kind` | `<push, tag-creation, pull-request-creation, merge, deploy, publish, or release>` |
| `provider and account` | `<provider; account or tenant; repository or service>` |
| `target` | `<exact remote target>` |
| `reviewed commit` | `<full reviewed commit and review evidence>` |
| `desired post-state` | `<exact desired state>` |
| `owner approval` | `<owner identity; exact approved action and target; approval time; single-use>` |
| `goal state at dispatch` | `<active state confirmed immediately before execution; a terminal goal lapses the approval>` |
| `pre-submission read-back` | `<authoritative provider state before submission>` |
| `duplicate control` | `<provider conditional-write or idempotency primitive, or blocked when material and unavailable>` |
| `submission count` | `<zero or one; read-only evidence calls do not count>` |
| `post-submission read-back` | `<authoritative provider state after submission, or not applicable>` |
| `result` | `<blocked, reconciled, prepared, or released>` |
| `uncertainty` | `<exact unknown or none>` |
| `blocked recovery` | `<cause; last verified state; recovery owner; closure evidence; safe retry condition; residual risk — or not applicable>` |

## Custom workflow closure

Record only when the owner supplied a `Custom workflow:` or `Request boundary:`
declaration. The validity rules and the five boundaries live in the
[owner-selected workflow](../references/PROTOCOL.md#owner-selected-workflow).

| Field | Required record |
| --- | --- |
| `declaration-bytes` | `<exact custom workflow and boundary declaration bytes>` |
| `selected-roles` | `<unique role allowlist in catalog order>` |
| `boundary` | `<one of the five boundary values>` |
| `initially-triggered-roles` | `<fixed-trigger results before selection>` |
| `excluded-roles` | `<roles excluded by boundary or selection, with reason>` |
| `completion-evidence` | `<terminal artifact and fixed checks>` |
| `later-triggers` | `<new trigger and evidence, or none>` |
| `expansion-decision` | `<pending-expansion, exact owner-approved revision, rejected, or cancelled>` |
| `invalid-or-blocked-outcome` | `<cause, no-dispatch or stop evidence, and next action — or not applicable>` |

Acceptance criteria:

- `<measurable result>`

Accepted contract or specification after review:

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
| `<used or skipped>` | `<one material question or reason skipped>` | `<paths, commands, file:line; for the frontend question, the frontend source map covering philosophy, standards/tokens, components, exemplars, routes/states/fixtures, commands, freshness/conflicts/unknowns>` | `<answer or limit; evidence is not approval>` |

## Sizing check

Record this section whenever the goal is classified as requiring the specification bracket.
Omit it only while that classification does not hold, and record it as soon as the
classification holds.

| Field | Required record |
| --- | --- |
| `deliverables` | `<integer or unavailable>` |
| `projected-bytes` | `<integer or unavailable>` |
| `projected-criteria` | `<integer or unavailable>` |
| `basis` | `<each deliverable with its byte estimate, criteria count, and coupling reason when it merges change sets; the fixed-overhead byte estimate; the fixed-overhead criteria count; the counterfactual mark when it applies — or unavailable with its reason>` |
| `deliverable-test` | `<pass, fail, or unavailable>` |
| `byte-test` | `<pass, fail, or unavailable>` |
| `criteria-test` | `<pass, fail, or unavailable>` |
| `decision` | `<passed, partitioned, proceed-unsplit, cancelled-with-goal, or pending>` |
| `request-bytes` | `<exact bytes of the owner request field the check measured>` |
| `source-base` | `<full commit the check read>` |
| `proposal-reference` | `<exactly one reference whenever any threshold result is fail or unavailable; none only while that turn was interrupted before the reference was appended and no permitted send has appended it, or while a halted outcome was recorded for that entry and the entry then closed before any permitted send, a permitted send being a send that appended a proposal reference; none on an all-pass entry>` |
| `revision-reference` | `<one reference made in reply to a recorded owner clarification, or none>` |
| `clarification-reference` | `<at most one owner clarification, with the Orchestrator reply when it answered, or none>` |
| `owner-decision reference` | `<verbatim owner decision bytes and their position in the sequence below, or not applicable>` |
| `observed-at-round-1` | `<body bytes, criteria count, and deliverable count observed at round 1; empty until the first round completes, or not applicable>` |
| `cap-amendment` | `<proposal reference and its cause; latest frozen ledger state, including no-frozen-ledger before round 1; the exact current and proposed value of each cap named; the owner reply with its verbatim decision bytes; the path state, open, closed, or spent; each amended value and the next Writer result it governs, including a blocked result that is not persisted, or none>` |

The owner-exchange sequence is append-only. Only the Orchestrator appends, and positions
are assigned once and never renumbered.

| Position | Kind | Record |
| --- | --- | --- |
| `<n>` | `<proposal, clarification, revision, or owner turn>` | `<reference or exact bytes>` |

Record a member goal only when the owner's own request bytes name both the proposal
reference and that member's guidance position. Member rows are append-only; a correcting
append supersedes an earlier row and never replaces it.

| Guidance position | Stage position | Owner request bytes | Member goal identifier | Supersedes |
| --- | --- | --- | --- | --- |
| `<n>` | `<n for a staged sequence, or not applicable>` | `<exact bytes naming the proposal reference and the guidance position>` | `<goal-id>` | `<earlier row or none>` |

## Specification rounds

See the [goal-flow protocol](../references/PROTOCOL.md#4-goal-flow) for the Spec Writer trigger
and review rules. Record the complete current body and identity before reviewer dispatch. Keep
metadata and review state outside the body. For material frontend behavior, record the complete
accepted scenario set in the accepted body before Plan Writer or Builder receives it.

### Current specification body

| Field | Value |
| --- | --- |
| status | `<complete or exact incomplete state>` |
| packet identifier | `<identifier>` |
| goal identifier | `<goal-id>` |
| decision-value reference | `<sizing-check goal identifier and its recorded decision value>` |
| source commit | `<full commit>` |
| content hash | `<lowercase SHA-256 of the exact body between the markers below>` |

<!-- SPECIFICATION-BODY:BEGIN -->

`<complete current specification body only, persisted verbatim before reviewer dispatch>`

<!-- SPECIFICATION-BODY:END -->

### Handoff defects

Record a hash mismatch, missing content, or interrupted reviewer attempt here. A defect
consumes no review round; correct and re-persist the handoff before a new dispatch.
Preserve findings from an interrupted attempt as provisional evidence for the next
complete bracket. One attempt counter serves each round, every append after that round's
first append takes the next number from it, and a corrected re-persist also records the
handoff-defect reference that caused it.

| Attempt | Packet identifier | Defect or interruption | Provisional finding IDs | Disposition |
| --- | --- | --- | --- | --- |
| `<attempt number of the corrective append for this round; none when no corrective append exists>` | `<identifier>` | `<hash mismatch, missing content, or interrupted reviewer>` | `<IDs or none>` | `<corrected, retried with fresh reviewers, escalated, or blocked>` |

### Lens schedule

Append one row before each reviewer dispatch, keyed to the round and to that round's packet
key. Rows are append-only: a retry or a corrected re-persisted packet appends and retains
the superseded row, and a round's current row is the latest append for that round and key.
The catalog, the assignment rules, and the disposition rules live in the protocol. Never
record a lens assignment or a lens disposition in a Spec Writer packet record, in the
finding ledger, or in the specification body.

| Round | Packet identifier and hash | Attempt | Assigned lenses and owning reviewers | Recorded dispositions | Supersedes |
| --- | --- | --- | --- | --- | --- |
| `<n>` | `<identifier and hash>` | `<attempt number from the one counter for this round, which is that append's handoff-defect reference; none only on the round's first append>` | `<each lens with its owning reviewer; at most two lenses per reviewer>` | `<per lens: the lens, plus its findings by that reviewer's own references; for lenses other than L6, an explicit no-additional-finding; for L6, no-prior-repair only on a valid clean L6, or no-additional-finding only after attacking a repaired body; or not yet returned>` | `<earlier row or none>` |

### Specification review rounds

Verdicts are `pass`, `repair`, or `blocked`. This table contains completed reviewer
brackets only. Each reviewer returns its complete jurisdictional finding set in one
pass. The Orchestrator merges both sets and freezes the finding ledger for the round. At
the configured cap, any open P0, P1, or P2 blocks the goal.

| Round | Packet identifier and hash | Claims verdict and finding count | Spec verdict and finding count | Open P0-P2 | Body lines | Body bytes | Merged finding IDs | Aggregated state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<n>` | `<identifier and hash>` | `<pass/repair/blocked; count>` | `<pass/repair/blocked; count>` | `<count>` | `<count>` | `<count>` | `<ledger IDs or none>` | `<pass/repair/blocked>` |

### Finding ledger (Orchestrator-owned)

Keep one compact ledger for the whole specification bracket. Keep findings here, not in the
specification body. The Orchestrator assigns stable IDs, merges both complete reviewer sets,
freezes the rows for each round, routes repairs, and owns state.

| ID | Jurisdiction | Severity | Finding | Minimum evidence and closure condition | State | First seen | Last checked | Later classification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<F-001>` | `<Claims or Spec>` | `<P0/P1/P2/P3>` | `<short finding>` | `<evidence; exact condition that closes it>` | `<open/repaired/accepted/non-blocking>` | `<round>` | `<round>` | `<introduced/missed, or not applicable>` |

P0 and P1 remain open until repaired. P2 remains open until repaired or explicitly accepted
by the owner when the acceptance is within owner authority. P3 blocks neither the goal nor
the cap, and blocks only the pre-cap accepted close the protocol states for the
specification bracket.

### Convergence state

| Field | Value |
| --- | --- |
| current completed round | `<0-10>` |
| open P0-P2 count | `<count>` |
| new findings after round 1 | `<introduced/missed IDs, or none>` |
| framework-review failure | `<yes/no; new missed P0/P1 IDs>` |
| lens coverage | `<one entry per catalog lens: the lens, its owning reviewer, and either its consumed round or not run; two entries for L6, one per owning reviewer>` |
| writer continuity | `<one entry per dispatched Writer attempt, consumed or not: the round, the attempt, and either first dispatch, reused, fresh by configuration, or replaced with its cause>` |
| qualifying round | `<round, or none>` |
| coverage-only reason | `<reason recorded when an unchanged body is persisted while coverage is incomplete, or not applicable>` |
| next action | `<repair, accepted, blocked, or pending owner reply>` |

The round cap and body size caps live in the protocol. Record both body sizes in each round
summary.

## Plan rounds

Use this bracket only when the existing Plan Writer trigger holds. Frontend scenarios do not make
planning unconditional. See the [goal-flow protocol](../references/PROTOCOL.md#4-goal-flow) for
the plan contract and verification rules. Record the packet, body, verdict, and evidence below.

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

`<complete accepted plan body only, persisted verbatim before verification, including the frontend plan scenario contract and bidirectional scenario-ID-to-producing-step map when accepted frontend scenarios exist, or not required>`

<!-- PLAN-BODY:END -->

## Builder and review rounds

Builder rounds use a separate context:

| Round | Builder | Changed paths and result | Docs claims affected and trigger | Checks and results | Uncertainty |
| --- | --- | --- | --- | --- | --- |
| `<n>` | `<separate context>` | `<result; implementation pass explicitly records frontend evidence packet: not yet permitted; evidence-only candidate result references the Builder round delta and cumulative Builder-owned identity in the shared frozen review unit checkpoint>` | `<claims and Docs Writer yes/no>` | `<commands/results; with scenarios, candidate attempt number, packet identifier/digest only for the evidence-only pass after commit/hooks, disposition, replay result, required-artifact references and exact-byte digests, bounded console/page/network/command/output/exit summaries, and no raw artifact bytes; identity details are in the shared frozen review unit checkpoint>` | `<none or limit>` |

### Current verified frontend packet body

Use this one marker pair only when accepted frontend interaction scenarios exist. It contains only
the current verified `frontend packet body`; bytes between the markers are exact, at most 48,000
bytes, contain neither exact marker byte sequence, and its digest excludes the markers. It contains
bounded summaries plus references and exact-byte digests, never raw screenshots, traces, or full
logs. Record candidate attempts, dispositions, and prior identity/evidence in the Builder row;
replace this body only with a new verified packet. See the [goal-flow
protocol](../references/PROTOCOL.md#4-goal-flow) for verification and repair rules.

<!-- FRONTEND-PACKET-BODY:BEGIN -->

`<exact current verified frontend packet body only, persisted verbatim; at most 48,000 bytes; no marker byte sequence; present only with accepted scenarios>`

<!-- FRONTEND-PACKET-BODY:END -->

### Docs Writer results

Record only when its trigger holds.

| Round | Context | Approved docs changed | Claims and links checked | Result and uncertainty |
| --- | --- | --- | --- | --- |
| `<n>` | `<separate context>` | `<approved Docs Writer-only paths; reference to the Docs Writer round delta, cumulative Docs Writer-owned identity, and frontend commit and hook checkpoint in the shared frozen review unit checkpoint>` | `<claims, links, checks, and non-overlap result>` | `<result and limit>` |

Review rounds use a fresh context that did not build the change. Verdicts are `pass`,
`repair`, or `blocked`:

| Implementation round | Frontend review round | Frozen unit and frontend packet | Reviewer | Verdict | Acceptance checks, findings, and uncertainty |
| --- | --- | --- | --- | --- | --- |
| `<n>` | `<shared round identity, or not applicable>` | `<shared state checkpoint: frozen review unit; current verified frontend packet body is in the dedicated packet section; otherwise not applicable>` | `<fresh context>` | `<verdict>` | `<criterion results and findings>` |

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

Record only when the design trigger holds. See the [goal-flow protocol](../references/PROTOCOL.md#4-goal-flow)
for authority and paired-round rules.

| Implementation round | Frontend review round | Frozen unit and frontend packet | Context | Governing source and matching evidence | Verdict | Checks, findings, and uncertainty |
| --- | --- | --- | --- | --- | --- | --- |
| `<same implementation round as general Reviewer>` | `<same shared round identity as general Reviewer>` | `<shared state checkpoint: frozen review unit; current verified frontend packet body is in the dedicated packet section>` | `<fresh context>` | `<matching project standard first; task-specific owner decision only for an otherwise missing material aspect; evidence-backed empty component inventory valid; analogous screens are evidence only>` | `<pass, repair, or blocked>` | `<checks and evidence>` |

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
| goal closure | `<branch and disposition: merged, handed off, or retained with reason; worktree removed or retained>` |
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
