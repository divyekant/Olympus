---
record: glbuilding-task
schema: 1
status: planned
---

# GLBuilding task: `<goal-id>`

The Orchestrator owns this record. Worker roles return bounded results to it.

## Goal

| Field | Value |
| --- | --- |
| owner request | `<request>` |
| created at | `<time>` |
| framework commit | `<full commit>` |
| PROJECT revision | `<revision>` |
| source base | `<commit>` |
| branch or worktree | `<current checkout, branch, or path>` |

Acceptance criteria:

- `<measurable result>`

Non-goals:

- `<explicit exclusion>`

| Scope | Value |
| --- | --- |
| allowed paths | `<paths>` |
| protected paths | `.glbuilding/`; managed loader blocks; `<other>` |
| relevant project instructions | `<paths or summary>` |
| validation commands | `<commands>` |

## Owner decisions

| Decision | Owner response | Effect |
| --- | --- | --- |
| `<major or external choice>` | `<approval, rejection, or pending>` | `<exact scope>` |

Delete this section when no owner decision was needed after goal activation.

## Explorer result

Delete this section when Explorer was skipped and state why in the outcome.

| Question | Evidence | Answer and uncertainty |
| --- | --- | --- |
| `<question>` | `<paths, commands, file:line>` | `<answer>` |

## Builder rounds

| Round | Builder | Summary and changed paths | Checks and results | Uncertainty |
| --- | --- | --- | --- | --- |
| `<n>` | `<separate context>` | `<result>` | `<commands/results>` | `<none or limit>` |

## Review rounds

Verdicts are `pass`, `repair`, or `blocked`. The final review must be fresh.

| Round | Reviewer | Verdict | Acceptance checks, findings, and uncertainty |
| --- | --- | --- | --- |
| `<n>` | `<fresh context>` | `<verdict>` | `<criterion results and findings>` |

Round cap: `<1, 2, or 3; default 2>`.

## Outcome

Set the frontmatter `status` to `complete`, `blocked`, or `cancelled`.

| Field | Result |
| --- | --- |
| final verification | `<commands and results>` |
| changed paths | `<paths>` |
| local commit | `<commit or none>` |
| Explorer | `<used or skipped with reason>` |
| Builder and review rounds | `<counts>` |
| owner corrections | `<count and summary>` |
| external action | `<none, pending approval, or approved action>` |
| remaining uncertainty | `<none or exact limit>` |

Do not mark `complete` without a fresh Reviewer `pass` and final relevant verification.
