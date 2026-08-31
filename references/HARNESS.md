# Harness adapter notes

This file is non-normative. It maps the fixed role classes to host harness mechanics and
records what has actually been observed. Neither this file nor `docs/GUIDE.md` can change a
role duty, trigger, authority, gate, or path: the [runtime protocol](PROTOCOL.md) and the
role charters in `agents/` win over both, and a statement here that contradicts either is a
documentation defect, not a rule.

`.olympus/PROJECT.md` holds the approved per-project harness mapping. This file is
background for writing that mapping, not a substitute for it.

## Vocabulary

Use exactly `supported`, `unsupported`, or `untested`, matching `templates/PROJECT.md`:

- `supported` — the required mapping and behavior passed at a recorded commit.
- `unsupported` — the harness cannot preserve the required role separation, freshness,
  owner-approved scope, or owner-authority boundary.
- `untested` — a mapping or tool may exist, but the required behavior has not passed at a
  recorded commit. **Tool or session availability alone is `untested`.**

A role-class row reads `supported` only when every member role in it has its own recorded
`supported` observation. One unobserved or `untested` member makes the whole class row
`untested`, even when other members passed. The sole observation register for this file is
`docs/CONFORMANCE.md`'s "Current harness evidence" table and its dogfood (`D01`-`D08`)
records; a status not traceable to a row or record there is not recorded here, and reads
`untested` by default.

## Role classes

The sixteen fixed roles group into eight classes for adapter purposes. This grouping is a
mapping convenience; the [fixed catalog](PROTOCOL.md#1-fixed-catalog) is still the
canonical role list and order.

| Class | Member roles |
| --- | --- |
| Hub | Orchestrator |
| Configuration mutator | System Configurer |
| Read-only investigator | Explorer |
| Writer | Spec Writer, Plan Writer |
| Fresh reviewer | Claims Reviewer, Spec Reviewer, Plan Verifier, Reviewer, Design Reviewer |
| Project mutator | Builder, Docs Writer |
| Test author | Tester |
| Advisory, status, and release boundary | Decision Council, Liaison, Release Agent |

Tester gets its own class rather than joining Project mutator: it writes and runs tests
only in Tester-owned test paths, never product code, and never repairs a defect or issues
a verdict — an authority shape distinct from Builder and Docs Writer.

## Claude Code mapping

A Claude Code session plays the Orchestrator hub directly; a role with its own fresh
context is a separate subagent session invoked by that hub and returning only to it. The
hub never edits the target repository as any other role, and a fresh-review role never
reuses the hub's own context.

| Class | Claude Code status | Evidence |
| --- | --- | --- |
| Hub | `supported` | Orchestrator: `supported`. A hub session ran the guided-onboarding dogfood in `docs/CONFORMANCE.md` D08 (three runs, Configurer and Reviewer dispatch and aggregation) and the D03 bounded mutation-path pass (Builder and Reviewer dispatch and aggregation). |
| Configuration mutator | `supported` | System Configurer: `supported`, per D08. Three fresh-repository onboarding runs; one found a template defect and stopped clean at `Fresh review=STOPPED` with nothing staged, the other two completed all six stages and matched the approved proposal byte for byte. |
| Read-only investigator | `untested` | Explorer: `untested`. No Claude Code scenario in `docs/CONFORMANCE.md` records an Explorer dispatch. |
| Writer | `untested` | Spec Writer: `untested`; Plan Writer: `untested`. No Claude Code scenario records either dispatch. |
| Fresh reviewer | `untested` | Reviewer: `supported`, per D08 (fresh review of the exact uncommitted configuration unit) and D03 (fresh review of the exact Builder mutation). Claims Reviewer, Spec Reviewer, Plan Verifier, and Design Reviewer: `untested`, no recorded dispatch. The class stays `untested` because four of five members are unobserved. |
| Project mutator | `untested` | Builder: `supported, bounded`, per D03 — one observed mutation path only; the earlier `unsupported` classification for a different, broader Claude trial is superseded for that exact path only, and general Claude support is not established. Docs Writer: `untested`, no recorded dispatch. The class stays `untested`. |
| Test author | `untested` | Tester: `untested`. The role was only just added to the catalog; `docs/CONFORMANCE.md` records no Claude Code Tester dispatch at all. |
| Advisory, status, and release boundary | `untested` | Decision Council, Liaison, Release Agent: `untested`, no recorded Claude Code dispatch for any of the three. |

## Codex mapping

Codex plays the same hub-and-subagent shape through its own session and task mechanics.
Freshness for a fresh-review or fresh-Writer role means a separate Codex context that did
not produce the artifact it reviews.

| Class | Codex status | Evidence |
| --- | --- | --- |
| Hub | `supported` | Orchestrator: `supported`. Multiple complete goal runs in `docs/CONFORMANCE.md` (D01, D04, and the "Simple conformance" and "Fresh-clone installation" rows) show routing, task records, and result aggregation through to a passing outcome. |
| Configuration mutator | `supported` | System Configurer: `supported`, per D04 (onboarding commit, an explicit second opt-in, and a passing installation) and the "Fresh-clone installation" row. |
| Read-only investigator | `untested` | Explorer: `untested`. D01 records that Explorer was explicitly skipped because direct repository evidence answered the question; no other row records a Codex Explorer dispatch. |
| Writer | `untested` | Spec Writer: `untested`; Plan Writer: `untested`. D06 ran ten formal specification rounds through Spec Writer and its reviewers, but the bracket never converged — the final packet still carried one open P1, and `docs/CONFORMANCE.md` records that this "demonstrates the specification convergence failure only. It does not establish general harness quality." That is not pass evidence for Spec Writer, and no row records a Plan Writer dispatch. |
| Fresh reviewer | `untested` | Reviewer: `supported`, per D01 and D04 (each a passing fresh review of a live Builder mutation dispatched through Olympus). The "Role craft and shared state static validation" row is not cited here even though it also reads `pass`: it shares D07's commit and D07's own text says that change "used the normal repository workflow outside Olympus" with "[f]resh contract and resilience reviews," not a live Olympus Reviewer dispatch, and that it "does not prove ... general harness support" — citing it for this role would overclaim. Claims Reviewer and Spec Reviewer ran repeatedly inside D06 but never reached an accepted body, so their pass-evidence claim is withheld for the same reason as Spec Writer above. Plan Verifier and Design Reviewer: `untested`, no recorded dispatch. The class stays `untested`. |
| Project mutator | `untested` | Builder: `supported`, per D01, D04, and the "Simple conformance" row. Docs Writer: `untested`, no recorded dispatch — `docs/CONFORMANCE.md` D07 is a core-framework change made through the normal repository workflow outside Olympus, not a Docs Writer dispatch, and its own text says it "does not prove general harness support." The class stays `untested`. |
| Test author | `untested` | Tester: `untested`. The role was only just added to the catalog; `docs/CONFORMANCE.md` records no Codex Tester dispatch at all. |
| Advisory, status, and release boundary | `untested` | Release Agent: `untested`. D06 is a Release Agent scenario, but it failed at the specification stage before implementation started, so it is not pass evidence for the Release Agent role's own boundary behavior either. Decision Council and Liaison: `untested`, no recorded dispatch. |

## Reading this file

- Every status above is `untested` unless the evidence column names a specific passing
  `docs/CONFORMANCE.md` row or `D`-numbered record. A blank or generic citation is not
  sufficient to write `supported` here.
- A `supported` row is scenario-specific, exactly as `docs/CONFORMANCE.md` states for its
  own evidence: it does not generalize to an unobserved role, an unobserved harness
  version, or production readiness.
- Before running a goal on a harness, check `.olympus/PROJECT.md` for the project's own
  approved mapping. This file only informs that mapping; it does not replace it.
