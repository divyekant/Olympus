---
record: glbuilding-task
schema: 1
---

# GLBuilding Task Record

The repository-root Orchestrator is the sole semantic writer of this record.
Roles return packets. The Orchestrator accepts or rejects them here.

## Frozen identity

| Field | Frozen value |
| --- | --- |
| goal id | `<stable goal id>` |
| owner session principal | `<identity and binding limit>` |
| initial root Orchestrator | `<identity>` |
| attempt | `<positive integer>` |
| prior attempt record | `<none or terminal task-record path>` |
| created at | `<timestamp>` |
| framework URL and full commit | `<copied from PROJECT>` |
| PROJECT revision and SHA-256 | `<revision and digest>` |
| execution profile SHA-256 | `<digest or none>` |
| committed base | `<commit>` |
| branch and worktree | `<identity>` |
| delivery boundary | `<effective boundary>` |
| Git finalization capability | `<label and evidence, or not required>` |
| commit author and committer | `<exact disclosed name and email pairs, or not required>` |
| maximum capability envelope | `<semantic capabilities and labels>` |

No packet can widen these values.

## Goal and scope

- owner goal: `<exact request>`
- acceptance criteria:
  - `<criterion with measurable evidence>`
- non-goals:
  - `<explicit exclusion>`

| Field | Frozen value or evidence |
| --- | --- |
| allowed paths | `<exact paths>` |
| Builder-protected paths | `.glbuilding/`; `AGENTS.md`; `CLAUDE.md`; `<other>` |
| accepted Intent, Map, and Validation | `<PROJECT rows reverified at this base>` |
| relevant dirty state | `<none or exact owner-approved snapshot>` |
| overlap decision | `<paths, interfaces, migrations, validation resources>` |
| task-specific narrowing | `<none or exact scoped text>` |

## Append-only event log

Current state: `planned`

Valid states are `planned`, `exploring`, `building`, `reviewing`, `repairing`,
`complete`, `blocked`, `failed`, and `cancelled`. The last four are terminal.

Use this table for state changes, accepted packets, checkpoints, owner decisions,
external-action approvals, resume, and takeover. Record exact commands or effects.

| Time | Actor | Event or state change | Source/diff identity | Evidence, decision, or exact effect |
| --- | --- | --- | --- | --- |
| `<timestamp>` | `<actor>` | `created -> planned` | `<identity>` | `<freeze evidence>` |

## Accepted exploration evidence

Delete this section when Explorer is skipped and record the reason in the event log.

| Question | Scope and commands | Exact `file:line` evidence | Answer, uncertainty, acceptance |
| --- | --- | --- | --- |
| `<bounded question>` | `<paths/commands>` | `<evidence>` | `<answer and Orchestrator decision>` |

## Builder result

| Field | Accepted packet |
| --- | --- |
| summary against acceptance | `<result>` |
| exact diff identity and changed paths | `<hash, command, paths>` |
| checks and complete results | `<commands and results>` |
| remaining uncertainty or skipped check | `<none or exact detail>` |
| protected-path result | `<pass or finding>` |
| external action still requested | `<none or exact effect requiring fresh approval>` |

## Review rounds

Add one row only when a round occurs. Every recheck uses a fresh Reviewer and the
complete current review unit. Verdicts are `pass`, `repair`, or `blocked`.

| Round | Reviewer and freshness | Diff/base | Verdict | Criterion checks/results, findings, and uncertainty |
| --- | --- | --- | --- | --- |
| `<n>` | `<identity and fresh-context evidence>` | `<identity>` | `<verdict>` | `<criterion checks and results; commands with complete results or why none apply; findings with severity, file:line, criterion, and repair; remaining uncertainty>` |

Round cap: `<1, 2, or 3; default 2>`. A repair at the cap becomes `blocked`.
A bare `pass` or `no findings` is not a complete Reviewer packet and cannot finish a task.

## Final verification and terminal result

| Acceptance or check | Command or evidence | Result | Revision/diff |
| --- | --- | --- | --- |
| `<criterion>` | `<exact command/evidence>` | `<pass/fail>` | `<identity>` |

| Field | Record |
| --- | --- |
| terminal status | `<complete | blocked | failed | cancelled>` |
| reason | `<evidence-backed result>` |
| final source and diff identity | `<frozen base; reviewed diff identity if any; for a successful committed goal, the first goal-ref commit that introduces this task-record path; otherwise no delivery commit>` |
| remaining uncertainty | `<none or exact detail>` |
| recovery | `<none | resume | takeover | cancel; retry uses a linked new record>` |

For a committed goal, never put the record's own commit, tree, or blob hash here. Never
write `local commit to follow` in a terminal record. The verified transaction packet
returns the actual commit after its old-value ref update succeeds. A pre-delivery
terminal record states that no delivery commit exists.

Before interpreting `complete`, reconcile this record with its frozen goal ref. The old
ref means prepared but incomplete, even if an unreachable commit object exists; restore
`reviewing` and reverify. The verified new commit means `complete`. Any other ref or
commit mismatch is `blocked` and must be preserved.

Do not continue a verified terminal record. Resume requires the same freeze. Retry creates a
linked higher-attempt record after the cause is resolved and the owner permits it.
Takeover appends the new root identity after the prior root stops. Cancellation retains
all evidence and stops work.
