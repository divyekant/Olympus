# Goal: spec-writer-config

## Goal and scope

Fifth and final process-fix goal from the v060-agents retrospective. Issue #16. Two
coupled change sets:

1. Writer-reuse configuration knob. A specification bracket keeps one persistent Spec
   Writer across rounds by default. Reviewers are always fresh. The owner can set the
   knob to fresh-writer-per-round. The default is reuse. Rationale: the validated
   asymmetry from three closed brackets - a persistent Writer carries repair context
   and self-test discipline; fresh reviewers supply the independence.
2. Writer self-test duties for every new or modified rule clause, before handoff:
   the both-readings test (escape AND deadlock; distributive AND collective readings),
   the clause-interaction matrix over every touched pair, and a full path re-walk.
   Evidence: 4 of 6 round-6 P1s in the sizing-gate bracket were contradictions between
   isolated repairs; the matrix caught 2 P1-class contradictions pre-handoff after
   adoption and collapsed the introduced-defect rate.

Out of scope: VERSION bump and release (issue #23). Charter file edits only if the
duties cannot ride existing charter text - prefer protocol-level statement; if a
charter edit is unavoidable this is a conflict to report, not to resolve silently.

## Governance

| item | value |
| --- | --- |
| governing pin | 58bb19288ad6f60974110e57ad894e033323c1a8 (post fix-4 repin) |
| governor checkout | /private/tmp/olympus-governor-58bb192 |
| mutation base | /private/tmp/olympus-fix5-writerconfig, branch claude/spec-writer-config, base 58bb192 |
| pinned machinery in force | sizing gate (fix 1), six-lens catalog (fix 2), population registers rule (fix 3), lean-body rule + cap-amendment path (fix 4) |

The body of this goal's specification must comply with the registers rule AND the
lean-body three-case rule now in force at the pin.

## Sizing check (pinned gate)

| field | value |
| --- | --- |
| deliverables | 2 coupled change sets |
| projected bytes | 30,000 |
| projected criteria | 10 |
| result | fail (projected bytes exceed 20,000) |
| proposal reference | owner standing full-control directive of 2026-08-29, applied as the partition proposal send |
| owner decision | proceed-unsplit (standing directive; both change sets amend the same Writer-bracket machinery and partitioning would split one rule family) |

## Owner decisions

| # | decision |
| --- | --- |
| 1 | Proceed-unsplit per the sizing entry above. |
| 2 | VERSION bump and release excluded (issue #23). |
| 3 | Rolling repin policy: this goal governs under 58bb192. |

## Specification rounds

| field | value |
| --- | --- |
| packet identifier | WRITERCFG-p6 |
| content hash | 46d4348746472a8b7e96577d86f90a661ed7e31e611cf238277f004a7278e947 |

<!-- SPECIFICATION-BODY:BEGIN -->

## Problem

The specification bracket fixes reviewer freshness but says nothing about the Spec Writer's own
context. Of register G-4's 13 members, eight bind freshness to a reviewer or verifier, D024's
among them; four are template evidence cells or the D018 history row; the one naming a Writer
context is a goal record. Register G-5 adds nothing: two of its four members are that goal
record, one persists an artifact, one is history. G-3 is empty, so no setting exists. The
bracket runs an undeclared convention with no rule, no owner control, and no record, and
nothing states what such a context may carry. Second, repairs authored one at a time contradict
each other: in the sizing-gate bracket 4 of 6 round-6 P1 findings were contradictions between
repairs each correct alone, while a matrix run before handoff caught 2 P1-class contradictions.
That practice is undeclared, and a question with no consequence is not a duty.

## Requirements

| ID | Requirement | Source |
| --- | --- | --- |
| R-1 | The protocol declares an owner-configurable setting for the Spec Writer context, values `reuse` and `fresh-per-round`, default `reuse`, following the precedent slot for a PROJECT boundary setting, states the reason each reviewer stays fresh under both values, and puts context selection in the Orchestrator's dispatch step before the send, that step carrying Orchestrator acts only. | goal set 1 |
| R-3 | A standing Writer duty states, in receipt and use terms, what a retained context may hold, what it must not receive anew or reconstruct, and what is authority for a repair, and the section-5 packet bullet records the same boundary. | goal set 1 |
| R-4 | The protocol defines the Writer replacement path, its input, and its effect on the remaining dispatches. | goal set 1 |
| R-5 | The role-context record admits a retained context; under `reuse` a harness that cannot preserve one degrades visibly, on a bound, and to the owner. | goal set 1 |
| R-6 | The task record holds the value in force at goal start and one continuity entry per dispatched Writer attempt. | goal set 1 |
| R-7 | Before every return the Writer runs the both-readings test, the clause-interaction matrix over a stated universe, and the gate and state-machine path re-walk, over a defined subject set. | goal set 2 |
| R-8 | The Writer tests, repairs, and re-tests once; that last pass bounds the duty. An adverse self-test result is a defect in the body, repaired before the return. After a cap-blocked residue with no restatement yet produced in the bracket, the next Writer result is a compact complete restatement. A residue the Writer states instead is recorded by the Orchestrator and barred from silence by the owner's residue acceptance at the pre-cap accepted close. The results are Writer evidence under the existing return item, not body content, and the duty is reconciled with the charter. | goal set 2, lean-body rule |
| R-10 | The duties land in protocol text. No role charter file changes. The conformance and decision records carry both change sets. | task record, convention |

## Approach

The setting follows one precedent, `strict convergence`: register G-1's four members are three
declaration sites plus one use, as A-5 records. The duties follow a second precedent in the
same section: the standing Writer duty stating the register re-run and the identifier audit,
reporting both under the return item the charter requires, and reconciling with the charter
rather than editing it; its defect sentence, making a divergent register a body defect, is
R-8's shape. Form differs between settings: G-6 shows `review round cap` as task-template
prose, not a goal-scope row, so no universal over settings is claimed. A stated residue routes
through the owner's residue acceptance and the cap-close report, because the Orchestrator
cannot originate a finding and the ledger alone would leave it ungated.

### Site set

Five files are amended. Four are in register G-2, the 13 files naming the role;
`templates/PROJECT.md` is in G-1 only. G-2's other nine are out of scope: two history files
excluded by the task record, four carrying no rule this changes, three charters by R-10.

Each edit names file, kind, anchor, and probe. The anchor is the shortest tail unique in that
file before the edits. The probe is a fixed string on one payload line absent from that file at
the governing revision, counted by V-2. An insert places its bytes after the anchor's line,
with a blank line before a paragraph and none before a row; a replace substitutes them.

**E-1** `references/PROTOCOL.md`, insert a paragraph after the sibling setting paragraph; anchor `section.`; probe `one role carries each property`:
```
`writer reuse` is a PROJECT boundary setting with values `reuse` and `fresh-per-round`,
default `reuse`. It changes only through the [section 3](#3-project-configuration)
configuration flow, the goal uses the value in force at goal start, and the Orchestrator
records that value with the goal. It governs the Spec Writer context only. Each reviewer is
fresh at each of its own dispatches under both values, because reviewer independence needs a
context that has not seen the body before and Writer repair needs one holding its own
authoring history; one role carries each property. The setting never makes a reviewer
persistent, never changes a packet, never lowers a bar, and never suppresses a trigger, a
lens, the coverage rule, an owner gate, or any other requirement of this protocol.
```
**E-2** `references/PROTOCOL.md`, replace the opening of the Writer dispatch sub-item; anchor `send the bounded packet to Spec Writer;`; probe `select the round's Spec Writer context`:
```
select the round's Spec Writer context under the `writer reuse` value in force, record
     that dispatch, and send the bounded packet to that
     Writer;
```
**E-3** `references/PROTOCOL.md`, insert three paragraphs after the standing Writer duty; anchor `no repair.`; probe `may hold what it lawfully`:
```
A dispatch is one send of a Writer packet to a selected context; a re-send after an
interruption reusing that packet is the same dispatch; an attempt is a dispatch. The
Orchestrator selects each dispatch's context under the `writer reuse` value: under `reuse`,
the most recent context to return a Writer result in this bracket; under `fresh-per-round`,
one that has not served this bracket. On a first dispatch none has returned a result, so both
values select one that has not served this bracket. When the serving Writer is interrupted,
unavailable, or replaced for any cause, including a harness that cannot retain a context, the
Orchestrator selects one that has not served this bracket, sends it that same packet and
nothing else, and records the dispatch as a replacement with its cause; under `reuse` it then
serves the remaining dispatches. Selection changes no packet.

A context serving more than one dispatch of a bracket may hold what it lawfully received or
authored, judged by the packet contract in force at that time. It must not receive anew, and
must not reconstruct, any of the following, each item on its own: a body that the packet's
persisted current body superseded; a body diff; a reviewer transcript; review history; a lens
assignment; a lens disposition. Only the packet's persisted current body and open finding
ledger are authority for a repair; material retained from an earlier dispatch, or received in
breach, is never authority however obtained, and the Orchestrator records it.

Spec Writer runs three self-tests before each return. The subject set is every rule clause of
the returned body that is new, or whose bytes differ from the corresponding clause of the
packet's persisted current body; it is empty when the returned body is byte-identical to that
body; and it is every rule clause on a bracket's first return and on a compact complete
restatement of a changed body. A rule clause states an obligation, permission, prohibition,
or condition, and when the body amends framework files its rule clauses include those of its
edit payloads. The both-readings test asks of each subject clause whether a reading escapes
it or deadlocks the goal, and, where the clause quantifies over a set, asks the distributive
and collective reading. The clause-interaction matrix pairs each subject clause with every
other subject clause and with every untouched rule clause of each file an edit lands in,
keeps the pairs sharing a named artifact, actor, identifier, or backtick-quoted string, the
first three read as judgment, any uncoverable class routed to residue, reports each kept pair
as consistent, jointly unsatisfiable, or an ordering conflict, the dropped pairs as one class
with that reason, and reports any pair class it could not cover as residue below. The path
re-walk covers each gate or state machine a subject clause touches, walking every path from
entry to each terminal outcome and naming it. When a return deletes a rule clause, the matrix
runs over the pairs it keeps under the same filter, computed from the packet's persisted
current body before the deletion; the path re-walk is required when the deletion touches a
gate or state machine; and both results are reported under the deleted clause's identifier.
An adverse result, meaning an escape, a deadlock, a jointly unsatisfiable pair, or a broken
path, is a defect in the body, not the packet, and the Writer repairs it before the return.
The Writer then re-tests the repaired clauses once; that re-test is the last pass. An adverse
result present at the last pass is stated in the return for the clause it concerns, and so is
one whose repair would exceed a cap in force. The return is lawful with such a residue, which
is not review material: the Orchestrator records it in the task record verbatim, marks it
superseded when a later Writer return reports repairing or deleting the clause the residue
names, which is recording on the Writer's report, not origination, and reports every standing
residue to the owner, whose acceptance at the pre-cap accepted close and whose report at the
cap read it. After a return states a cap-blocked residue, and no compact complete restatement
has been produced in this bracket, the next Writer result is a compact complete restatement.
The duties run on every return, which states each subject clause's result or an explicit
empty set. These results are the Writer's evidence, not body content, and go only to the
Orchestrator, riding the return item the charter requires for the Evidence register and
traceability map: that map binds each requirement to its validation, and this report does so
at rule-clause grain. It holds no finding, hash, round record, reviewer text, or review
state, so the charter's three exclusions are unaffected.
```
**E-4** `references/PROTOCOL.md`, replace the end of the section-5 Spec Writer bullet; anchor `body only to the Orchestrator.`; probe `adds no input to this bullet`:
```
body only to the Orchestrator. Writer continuity adds no input to this bullet
  and removes none: a context that serves more than one dispatch is never authority for an
  input this bullet names, and never supplies an input this bullet excludes.
```
**E-5** `references/PROTOCOL.md`, replace the role-context record bullet; anchor `separate or fresh as required;`; probe `retained as configured`:
```
separate, fresh as required, or retained as configured;
```
**E-6** `references/PROTOCOL.md`, replace the end of the harness-support paragraph; anchor `owner-authority boundary.`; probe `for that reason alone`:
```
owner-authority boundary. Under `reuse`, a harness that cannot preserve a Spec Writer context
across dispatches is not `unsupported` for that reason alone, because it violates no
freshness requirement: the Orchestrator selects a context that has not served the bracket at
each dispatch, recording each as a replacement caused by that limit, so the degradation is
recorded, not silent. On the second such replacement in adjacent continuity entries, a first
dispatch being no replacement, the Orchestrator records the limit and reports it to the owner
in the goal's next owner exchange, no later than the completion report; the goal continues
under fresh dispatch. Under `fresh-per-round` this paragraph does not apply.
```
**E-7** `references/PROTOCOL.md`, replace the end of the pre-cap accepted-close condition; anchor `P3.`; probe `marked superseded`:
```
P3, and no standing
   Writer-stated residue is recorded for this goal. That same acceptance covers every residue
   a Spec Writer stated in a return for this goal, as recorded and not marked superseded, and
   an unaccepted standing residue bars this close.
```
**E-16** `references/PROTOCOL.md`, replace the end of the cap-close sentence; anchor `to the owner.`; probe `at the same time`:
```
to the owner. Every standing residue a Spec
Writer stated in a return for this goal is reported to the owner
at the same time.
```
**E-8** `templates/PROJECT.md`, insert a row after the Boundaries row for the sibling setting; anchor `convergence`; probe `fresh-per-round`:
```
| writer reuse | `reuse` (`reuse` or `fresh-per-round`) |
```
**E-9** `templates/TASK.md`, insert a row after the goal-scope row for the sibling setting; anchor `strict convergence`; probe `fresh-per-round`:
```
| writer reuse | `<reuse or fresh-per-round; the value in force at goal start>` |
```
**E-10** `templates/TASK.md`, replace mid-line in the role-population note, keeping the sentence that follows; anchor `blocks dispatch.`; probe `per-attempt continuity log`:
```
blocks dispatch. The Spec Writer row records that role's
mapping, context record, and support evidence; the per-attempt continuity log is the
`writer continuity` row.
```
**E-11** `templates/TASK.md`, insert a row after the `lens coverage` convergence-state row; anchor `lens coverage`; probe `one entry per dispatched Writer attempt`:
```
| writer continuity | `<one entry per dispatched Writer attempt, consumed or not: the round, the attempt, and either first dispatch, reused, fresh by configuration, or replaced with its cause>` |
```
**E-12** `templates/TASK.md`, replace inside the residue-acceptance row; anchor `in that frozen ledger, or none>`; probe `every standing Writer-stated residue`:
```
in that frozen ledger and every standing Writer-stated residue recorded for the goal, or none when neither exists>
```
**E-13** `docs/CONFORMANCE.md`, replace the end of static check 5; anchor `facts.`; probe `edit payloads included`:
```
facts. Every Spec Writer return reports the
   three self-tests the protocol requires over its subject set of new and modified rule
   clauses, edit payloads included, or every rule clause on a first return or restatement:
   both readings, the clause-interaction matrix, and the gate and state-machine path re-walk.
   It states each subject clause's result, or an explicit empty subject set. An adverse result
   is a body defect repaired before the return; a residue stated instead is recorded, every
   standing one reaches the owner's residue acceptance and a superseded one is excluded, and
   after a cap-blocked residue with no restatement yet in the bracket the next result is a
   compact complete restatement.
```
**E-14** `docs/CONFORMANCE.md`, replace the end of static check 6; anchor `markers.`; probe `in adjacent entries`:
```
markers. Each reviewer is fresh at each
   dispatch. The Spec Writer context follows the `writer reuse` setting, default `reuse`:
   selection changes no packet, a retained context is never authority for a repair, a
   replacement receives the same packet and nothing else, and under `reuse` a harness that
   cannot retain a context records a replacement per dispatch, escalating to the owner on
   the second in adjacent entries, instead of becoming `unsupported`.
```
**E-15** `docs/DECISIONS.md`, insert a row after the last decision row; anchor `own authority.`; probe `Persistent Spec Writer, fresh reviewers`:
```
| D033 | Persistent Spec Writer, fresh reviewers | A specification bracket keeps one Spec Writer context across dispatches by default, and each Claims and Spec Reviewer is fresh at each of its own dispatches. The asymmetry is the point: independence needs a context that has not seen the body, and repair needs a context that holds its own authoring history. The owner may set the `writer reuse` PROJECT boundary setting to `fresh-per-round`; no value makes a reviewer persistent or changes a packet. A retained context may hold what it lawfully received or authored, must not receive anew or reconstruct a superseded body, a body diff, a reviewer transcript, review history, or lens data, and is never authority for a repair. Before each return the Writer runs three self-tests over its new and modified rule clauses, edit payloads included, or every rule clause on a first return or a compact complete restatement: both readings, the clause-interaction matrix, and the gate and state-machine path re-walk. An adverse result is a body defect repaired before the return; a residue stated in its place is recorded, every standing residue reaches the owner's residue acceptance and the cap-close report while a superseded one is recorded and excluded, and after a cap-blocked residue with no restatement yet produced in the bracket the next Writer result is a compact complete restatement. |
```

## Invariants

| ID | Invariant |
| --- | --- |
| I-1 | No value of the setting makes any reviewer persistent or changes any reviewer's freshness at any of its dispatches, and no lens assignment and no lens disposition reaches the Writer, by packet or by retained context; that bar is protocol text in the goal-flow section, not a charter sentence. |
| I-2 | The Spec Writer packet contract is identical under both values. The section-5 exclusion stands unchanged: "It never receives earlier bodies or full reviewer reports." The source soft-wraps that sentence across two lines, so the quotation is sentence-exact, not byte-exact. |
| I-4 | Only the packet's persisted current body and current open finding ledger are authority for a repair, under either value. |
| I-5 | No file under `agents/` changes. The duties are protocol text riding the charter method that already requires a whole-specification reread and self-refutation after every repair. |
| I-6 | Every anchor occurs exactly once in its file at the governing revision, and after all sixteen edits none occurs more than once: twelve still occur once, and E-2's, E-5's, E-7's, and E-12's occur zero times because their replacement payloads do not reproduce them. The edit bytes carry no identifier of this specification's series, and the `docs/DECISIONS.md` payload carries no em dash, matching that file's existing punctuation. |

## Assumptions

| ID | Assumption | State | Evidence | Load-bearing |
| --- | --- | --- | --- | --- |
| A-1 | No framework file at the governing revision states a Spec Writer context-continuity rule. | supported, with a stated limit | registers G-4 and G-5; a paraphrase using none of G-5's continuity words would escape both, so the claim is licensed for that lexical population only. Register G-3 is empty, so the setting name and its hyphenated value are new | yes |
| A-3 | The bracket-history counts in `Problem` are owner-supplied packet evidence, not a probe of the governing revision. | unexercised | packet and task record | motivation only; no requirement depends on them |
| A-4 | The nine out-of-scope members of register G-2 need no edit. | supported | the task record's scope for the history files and R-10 for the charters; `.olympus/tasks/spec-registers-rule.md` does state a continuity convention and the self-test practice, so its operative reason is scope, not silence | yes |
| A-5 | The `strict convergence` precedent this specification follows is declared at three sites; register G-1's four members are those three declarations plus one use of the setting. No universal over PROJECT boundary settings is claimed: register G-6's three members show `review round cap` declared as task-template prose, not a goal-scope row, so the contrast is form, not count. | supported | registers G-1 and G-6 | yes |
| A-6 | Item 1 of the retention bar is bracket-scoped where the charter's exclusion of earlier bodies is unqualified. | unexercised | the narrower scope binds only inside a bracket, and no packet contract licenses an out-of-bracket body either way, so the two never disagree on an admissible input | no; the bar is a superset of the charter's inside a bracket and adds nothing outside one |
| A-7 | The design leans on `fresh`, which the pin uses without defining. | unexercised | `fresh` keeps the meaning the reviewer charters and the goal-flow section already give it: a context that has not seen the body before | yes, if a later goal defines `fresh` differently |

## Authority and data flow

Only the owner sets the value, and only the System Configurer writes it into PROJECT. The
Orchestrator records the value in force at goal start, selects each dispatch's context under
it, records every dispatch, and records each stated residue. The Writer returns only to it.

## Failure boundaries

Each failure and disposition sits in its criterion's red path: Writer interruption,
replacement, and retained material as authority in C-3; an unretainable context in C-5; an
adverse result, a surviving residue, a cap-blocked repair, an uncoverable class, and a
byte-identical body in C-9; a mid-goal change and a missing row in C-1. Recorded gaps,
retirements not citations: R-2, R-9, I-3, A-2, C-2, C-4, C-11, V-4, and the B series. A stated
residue has no owner-authority bound: it is P3-kin, never blocks the cap, and fresh review each
round is the severity leg.

## Acceptance criteria and red paths

| ID | Criterion | Red path |
| --- | --- | --- |
| C-1 | `references/PROTOCOL.md` declares `writer reuse` with both values and default `reuse`, beside the sibling setting, states per-dispatch reviewer freshness with the reason for the asymmetry, and puts context selection in the dispatch sub-item before the send, that sub-item carrying Orchestrator acts only. | The setting has no protocol hit, the default is not `reuse`, the asymmetry or its reason is absent, selection follows the send, the sub-item carries a Writer obligation, or a mid-goal change or a missing PROJECT row has no stated disposition. |
| C-3 | A standing Writer duty states retention in receipt and use terms, lists all six excluded items with a distributive marker, names the two authorities for a repair, and defines the replacement path: a context that has not served the bracket, the same packet and nothing else, recorded with its cause, serving the remaining dispatches under `reuse`. | Any excluded item is missing, the rule's prohibitions use a possession predicate, no authority sentence exists, there is no replacement path, the replacement's input is unstated, or an interrupted or replaced Writer has no disposition. |
| C-5 | The role-context record admits a retained context, recording the configured intent from the first dispatch; under `reuse` the harness paragraph makes an unretainable context a recorded per-dispatch replacement rather than `unsupported`, escalated to the owner on the second in adjacent entries within a stated bound. | The record admits only separate or fresh, the harness limit yields `unsupported`, the escalation has no time bound or no record, the paragraph binds `fresh-per-round`, or the escalation counts dispatches rather than replacements. |
| C-6 | `templates/PROJECT.md` and `templates/TASK.md` each hold exactly one `writer reuse` row; `templates/TASK.md` holds exactly one `writer continuity` row keyed per dispatched attempt with a `first dispatch` value; the role-population note says which record holds the mapping and which the per-attempt log. | Any row is absent or duplicated, the continuity row is keyed per consumed round, or the note is absent. |
| C-7 | The protocol defines the subject set against the packet's persisted current body, one designator, and states the byte-identical, first-return, and restatement cases explicitly. | A second designator names that body, or any of the three cases is unstated. |
| C-8 | The matrix clause states that edit payloads' rule clauses are subject clauses, gives the pairing universe, defines the shared-term filter by backtick quotation, and states the deletion rule computably. | Any of the four is absent, or the deletion rule names a historical artifact a replacement Writer cannot reach. |
| C-9 | An adverse self-test result is a body defect repaired before the return; a residue stated in its place is recorded by the Orchestrator, and after a return states a cap-blocked residue with no compact complete restatement yet produced in the bracket, the next Writer result is a compact complete restatement. The duty places the results under the existing return item, keeps them out of the body, and states the charter reconciliation. | The duty states no consequence, the two-pass bound that triggers a residue is unstated, a cap-blocked repair yields no residue or no restatement ordering, the residue reaches no record or is not recorded verbatim, supersession has no reported trigger or no recording-not-origination sentence, an uncoverable pair class or a byte-identical body has no disposition, any self-test result is body content, or no reconciliation sentence exists. |
| C-10 | The pre-cap accepted close accepts every standing Writer-stated residue in the same owner step as open P2 and P3, its `none` branch requires that no residue is recorded, the cap close reports standing residues beside the open P3s, and the task record's residue-acceptance row names them. | The close omits stated residue, the `none` branch stays satisfiable while a residue stands, the cap close omits residues, the row is unchanged, or an unaccepted standing residue does not bar the pre-cap close. |
| C-12 | `docs/CONFORMANCE.md` checks 5 and 6 carry both change sets including the residue rule, `docs/DECISIONS.md` gains one decision row whose body carries the same rules and no em dash, no file under `agents/` differs, and the changed-path set is exactly the five files the edits name. | Either check is unchanged or unqualified, the row is absent, title-only, or contains an em dash, a charter file differs, or a sixth path changed. |

## Validation obligations

| ID | Obligation |
| --- | --- |
| V-1 | Re-run each `Provenance` register command at its recorded revision from the repository root; each digest and member count matches. |
| V-2 | Count each edit's anchor as a fixed string in its file at the governing revision; every count is 1. Repeat in the amended tree; the counts for E-2, E-5, E-7, and E-12 are 0 because their replacement payloads do not reproduce their anchors, every other count is 1, and no count exceeds 1. Count each edit's stated probe the same way in that edit's file: 0 at the governing revision, 1 after the build. The probe list enumerates this body's own payloads, which are body content, so it is a self-reference rather than a repository population and is not a population register. |
| V-3 | List changed paths after the build: exactly the five files the edits name, none under `agents/`. Count table rows, meaning lines beginning with a pipe, matching `writer reuse` in `templates/PROJECT.md` and in `templates/TASK.md`, and matching `writer continuity` in `templates/TASK.md`; each count is 1. Prose mentioning a row name is not a row. |
| V-5 | Check every internal Markdown link in the five amended files: each resolves to an existing file, and each anchor link to a heading in the file it names. Check that each amended table keeps its original column count. Run `grep -nEw '[RIABCVEG]-[0-9]+'` over those files; the result is empty. Count em dashes in `docs/DECISIONS.md` before and after; both counts are 0. |

## Rollout/rollback

Markdown only. It takes effect for goals started after the amended revision is pinned; an open
goal keeps its start value. Rollback reverts the sixteen edits; no migration exists.

## Non-goals

- The VERSION bump and the release, which issue #23 owns; any charter edit under `agents/`; any per-round Orchestrator discretion over context; and any change to reviewer freshness, the lens catalog, the sizing gate, the registers rule, the lean-body rule, the round cap, or the body size caps.

## Provenance

Governing revision `58bb19288ad6f60974110e57ad894e033323c1a8`, mutation base
`claude/spec-writer-config`. Commands run from the repository root; the runner sets `LC_ALL=C`.

```
git --no-pager -c color.ui=false grep -nP 'strict convergence' 58bb19288ad6f60974110e57ad894e033323c1a8 -- . | shasum -a 256
git --no-pager -c color.ui=false grep -lP 'Spec Writer' 58bb19288ad6f60974110e57ad894e033323c1a8 -- . | shasum -a 256
git --no-pager -c color.ui=false grep -lP 'writer reuse|fresh-per-round' 58bb19288ad6f60974110e57ad894e033323c1a8 -- . | shasum -a 256
git --no-pager -c color.ui=false grep -nP '^(?=.*\bfresh)(?=.*Writer).*$' 58bb19288ad6f60974110e57ad894e033323c1a8 -- . | shasum -a 256
git --no-pager -c color.ui=false grep -niP '^(?=.*Writer)(?=.*(persistent|persists|retain|reus|same context)).*$' 58bb19288ad6f60974110e57ad894e033323c1a8 -- . | shasum -a 256
git --no-pager -c color.ui=false grep -nP 'review round cap|Round cap' 58bb19288ad6f60974110e57ad894e033323c1a8 -- . | shasum -a 256
```

| ID | Population | Members | Recorded result |
| --- | --- | --- | --- |
| G-1 | every line naming the sibling setting | 4 | `7450655460a1563c8897aa6a19ca60b12cf5dec8a66ef1b653b3d45e7e97bd02` |
| G-2 | every file naming the Spec Writer role | 13 | `132aaf313aa9203eb47212866e851a20f0d03ebc210aabe05609c053b599ae01` |
| G-3 | every file naming the new setting or its hyphenated value | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| G-4 | every line carrying both `fresh` and `Writer`, case-sensitive, `fresh` on a word boundary | 13 | `af39085b5d2d60a6f374800fe6c8e8cbfd59248f2ba361f3c0952f855a9e6509` |
| G-5 | every line carrying `Writer` with a continuity word, case-insensitive, no word boundary, so `reus` matches `reused` | 4 | `a98a6df86eccd2740dcd4e1bfc25c3764f42d325a3de3550b39c4533359a8795` |
| G-6 | every line naming the review round cap | 3 | `d40ad67f9e0c84673b61d0f3b9fe9ad01522f6edc85b9c41c56b36e52285ae41` |

Self-test results, anchor and probe counts, and register outputs are in the return.

<!-- SPECIFICATION-BODY:END -->

## Round table

| round | packet | Claims packet | Spec packet | merged distinct | lines | bytes | lenses | result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | WRITERCFG-p1 79eca47c...bacc (first draft; 10 edits, 5 files) | 16 (6 P1, 5 P2, 5 P3) | 20 (7 P1, 7 P2, 6 P3) | ~27 distinct (8 P1 clusters, ~10 P2, ~9 P3) | 290 | 21693 | Claims L1+L5; Spec L2+L3 | DOES NOT QUALIFY - 8 P1 clusters |
| 2 | WRITERCFG-p2 ba707f63...da4d (compact complete restatement; round-1 full repair; 13 edits; receipt+use retention; 6 registers) | 8 (3 P2, 5 P3) | 11 (2 P1, 8 P2, 1 P3) | 13 (2 P1, ~11 P2 XS2-10=XC2-8, ~6 P3) | 300 | 26414 | Claims L1+L6; Spec L4+L6 | DOES NOT QUALIFY - XS2-1, XS2-2 P1 |
| 3 | WRITERCFG-p3 20bde46d...9b31 (surgical round-2 full repair; per-edit probes; bounded two-pass rule) | 12 (3 P2, 9 P3) | 7 (1 P1, 5 P2, 1 P3) | 19 (1 P1, 8 P2, 10 P3) | 300 | 28736 | full mandate + L6 attack (both) - QUALIFYING CANDIDATE | DOES NOT QUALIFY - YS3-1 P1 |
| 4 | WRITERCFG-p4 3551c450...a16b (second restatement; residue routed to owner acceptance; 14 edits; 7 id retirements with gaps) | 9 (1 P1, 4 P2, 4 P3) | 11 (3 P1, 6 P2, 2 P3) | 16 (3 P1, 7 P2, ~6 P3; ZC4-1=ZS4-3, ZC4-4=ZS4-5, ZC4-3=ZS4-10 adj) | 300 | 30423 | full mandate + L6 attack (both) - QUALIFYING CANDIDATE | DOES NOT QUALIFY - ZS4-1/2, E-14 probe |
| 5 | WRITERCFG-p5 b378ccf6...fcd8 (surgical round-4 full repair; cap-close residue report; none-disjunct; 16 edits; B folded) | 6 (3 P2, 3 P3) | 7 (1 P1, 4 P2, 2 P3) | ~10 (1 P1, ~5 P2, ~5 P3; QC5-1~QS5-2, QC5-2~QS5-3, QC5-6~QS5-4) | 300 | 29993 | full mandate + L6 attack (both) - QUALIFYING CANDIDATE | DOES NOT QUALIFY - QS5-1 P1 |
| 6 | WRITERCFG-p6 46d43487...e947 (surgical round-5 full repair; result-bound restatement rule; supersession chain reconciled) | 2 (2 P3) | 6 (3 P2, 3 P3) | 8 (3 P2, 5 P3) | 300 | 30507 | full mandate + L6 attack (both) - QUALIFYING CANDIDATE | QUALIFIES - accepted close |

## Round-1 findings (merged) - binding for round 2

Dedup: WC1=WS1+WS2 (retention cluster, incl. WS12/WS13); WC6=WS9+WS7 (continuity-row
cluster); WC2 joins WS4 (subject-set cluster); WS6=WC5 (role-context cluster); WS11 folds
into WC3; WS17=WC11; WS15=WC15. Mechanical layer clean: 4/4 register digests reproduce
inside the command-shape bound; 10/10 anchors unique pre AND post edit; ID series clean;
lean-body sweep clean except two over-long anchors; the one quotation byte-exact.
P1 x8 (clusters):
1. RETENTION BOUNDARY (WS1+WS2+WC1): "may not hold" is a state predicate a reused context
   cannot satisfy - the context that returned the previous body holds it by construction,
   and lawfully received earlier ledgers are review history in substance. The charter
   uses ACTION verbs only (receive, reconstruct). REPAIR: drop the hold-predicate; the
   rule becomes receipt+use: a retained context may hold what it lawfully received or
   authored; it must not receive anew or reconstruct superseded bodies, diffs, reviewer
   transcripts, review history, or lens data; and only the packet's persisted current
   body and current open ledger are authority. Distributive marker stated (WS12); E-4's
   "item" sense fixed (WS13).
2. SUBJECT SET (WS4+WC2): "corresponding clause of the immediately preceding persisted
   body" undefined after a restatement, and the body uses two designators for one
   artifact. REPAIR: one designator - the packet's persisted current body; subject set =
   clauses of the returned body new or byte-different vs that body; after a compact
   complete restatement (and on a bracket's first return) the subject set is every rule
   clause of the returned body - stated explicitly.
3. MATRIX UNIVERSE (WS5): unstated whether edit payloads are in the matrix; on the
   body-only reading the matrix cannot catch the class WS1 shipped. REPAIR: for a
   framework-amending body the subject clauses INCLUDE the edit payloads' rule clauses,
   paired against each other and against the amended files' untouched rules under the
   shared-term filter; "defined term" given a decidable definition.
4. SELF-TEST CONSEQUENCE (WS3): duty discharged by asking; no consequence; no verifier.
   REPAIR per the register-duty precedent: an adverse result (escape, deadlock, jointly
   unsatisfiable pair, broken path) is a defect in the specification body and the repair
   is the body, before return; the return states each subject clause's result.
5. ROLE-CONTEXT RECORD (WS6+WC5): PROTOCOL:612-623 admits only separate/fresh; reuse has
   no truthful value; harness inability untreated. REPAIR: site at the role-context
   record admitting "retained as configured"; harness that cannot preserve a persistent
   context dispatches fresh WITH a recorded replacement per round (visible degradation,
   not unsupported, not silent); TASK.md:35 role row reconciled (WS18).
6. CONTINUITY ROW (WS7+WS9+WC6): no truthful round-1 value under reuse; replacements in
   unconsumed attempts have no record site. REPAIR: enumeration gains "first dispatch";
   keyed one entry per dispatched Writer attempt (consumed or not); round vocabulary
   unified - E-2 dispatches the context that returned the packet's persisted current
   body (fixes WS10).
7. A-5 FALSIFIED (WC3+WS11): "complete declaration pattern" universal falsified by
   review-round-cap (two sites, no TASK row); Approach's "adds nothing" contradicted by
   E-8/9/10. REPAIR: rescope A-5 to the strict-convergence precedent followed; Approach
   states the conformance/decision rows as the second, separate convention.
8. A-1 EVIDENCE (WC4): true claim, wrong license - G-4's population cannot contain the
   fact denied. REPAIR: supplementary register over the claimed population (stated
   lexically, honestly), disclosure of limits.
P2 (binding): WS8 (return-item schema - add the explicit reconciliation the registers
duty carries at PROTOCOL:465-471; state how analytic results ride the traceability-map
half); WC9 (lens-bar attributed to protocol text, not the charter); WC10 (anchor
minimality: E-5 shortened; E-1's length justified in-body by post-edit uniqueness - the
payload mirrors the sibling text, which is what "the edit requires" covers - STATE it);
WC11/WS17 (E-2 placed before the send sub-item, or value selection folded into it);
WS14 (Writer-context duties move to a standalone Writer-duty paragraph per the
PROTOCOL:443-457 precedent; the dispatch sub-item keeps Orchestrator acts only); WC7
(Problem sentence corrected - 4 of G-4's 13 members bind fresh to evidence cells or
history rows, not actor contexts); WC8 (A-4 rescoped - spec-registers-rule.md states
both a continuity convention and self-test practice; the Site set's out-of-scope reason
is the correct one).
P3: WS15/WC15 (E-1 tail rationale stated); WS16 (freshness scope aligned E-1/E-9);
WS19+WC13 (V set gains row-count obligations and V-6's exact grep pattern); WS20 (line
headroom); WC12 (E-7 position text names the lens coverage row); WC14 (G-4 property
states case sensitivity and word boundary); WC16 (no em dashes in the DECISIONS row).
Positives settled: 4/4 digests; 10/10 anchors pre/post; site-set arithmetic; D033 next;
I-2 quotation; I-6 containment; charter facts verified; walks P-12..P-18 clean.
Round 2 lenses: Claims L1+L6; Spec L4+L6 (coverage complete at round 2). Line budget:
290/300 - compaction reserve first if repairs push past 300 (Site set + rejected
alternatives ~7 lines), restatement if needed. Rounds 1 of 10.

## Round-2 findings (merged, 13 distinct; XS2-10=XC2-8) - binding for round 3

Coverage complete (all six lenses run). Round-1 repairs re-attacked and held: receipt+use
retention cannot launder at the pin (no packet contract licenses a transcript); E-2
restructure drops nothing; anchor consumption legal under lean-body case two; 6/6
register digests reproduce; 13/13 anchors pre; post 11 at 1 + 2 consumed exactly as
I-6 states; V-3/V-4 fixed methods verified working; reproduction sweep zero unlicensed.
P1 x2 (both from the executed build walk):
1. XS2-1 BUILD GATE BLIND: dropping any of 7 of 13 edits (incl. E-3, the substance)
   passes V-1..V-4 - proven by 13 one-edit-dropped rebuilds. REPAIR: V set gains one
   fixed-string presence count per edit payload (a stated distinctive substring from
   each of the 13 payloads, expected count per file stated).
2. XS2-2 ADVERSE-RESULT LOOP HAS NO TERMINAL: fixpoint reading never returns (no round
   consumed, blocked never fires); one-pass reading never re-tests repaired bytes; at
   the size cap a growth repair has no lawful return. REPAIR: bounded two-pass rule -
   test, repair, re-test once; an adverse result that survives the re-test is stated
   per clause in the return, and the return is lawful with that residue (the stall
   routes to normal review; rounds consume; the cap-composition deadlock dissolves).
P2 (binding): XS2-3 (deletion repairs escape the subject set - the duties cover
deletions: matrix re-runs over the deleted clause's former kept pairs; path re-walk
mandatory when a deletion touches a gate); XS2-4 (selection designator not unique when
a coverage-only round persists an unchanged body - name the MOST RECENT context to
return a result in this bracket); XS2-5 (dangling "it" in E-3 P1 and E-6 - the
Orchestrator selects, named explicitly); XS2-6 (E-9 header says end-of-note, anchor
sits mid-line with 46 trailing bytes - one deterministic reading, re-anchored or header
corrected, and gated by the new presence checks); XS2-7 (A-5 "three sites" vs G-1's
four lines - state three declarations + one use; Approach aligned with what G-6 shows:
the contrast is form, prose vs row); XS2-8 (dispatch defined once: one send of a Writer
packet to a selected context; a re-send after interruption reusing the same packet is
the SAME dispatch - mirrors the sizing gate's reuse-the-reference precedent); XS2-9
(unbounded silent harness degradation diverges from PROTOCOL:333's
escalate-on-second convention - the second consecutive harness-caused replacement is
reported to the owner in the Orchestrator's next owner-facing reply; goal continues
under fresh dispatch, not blocked); XS2-10/XC2-8 ("definition sentence" undecidable -
defined term = backtick-declared only); XC2-1 (E-4 has no criterion, no obligation, no
requirement trace - gains all three; the presence check covers detection); XC2-2 (C-3
red path self-trips on the conforming "may hold" - reworded: the rule's PROHIBITIONS
use a possession predicate); XC2-3 (E-11/E-13 glosses omit the restatement case - both
gain "or every rule clause on a first return or a compact complete restatement").
P3: XC2-4 (six-item bar names its breach disposition: material received in breach is
never authority and the breach is recorded); XC2-5 (bracket-scope of item 1 and the
undefined "fresh" leaned on - disclosed in an assumption); XC2-6 ("that Writer" names
the Spec Writer once in E-2's payload); XC2-7 (E-10 gains the either/or choice marker
of its sibling row); XS2-11 (E-5 slot records configured intent - stated); V-4's link
clause gains a pass condition.
LINE BUDGET: 300/300 - every repair line must be paid by compaction (identified
reserve: Problem/Approach prose ~4, Requirements table fold ~6); a further compact
complete restatement is authorized if needed, with clause-preservation checklist.
Convergence: 27 -> 13. Round 3 = surgical (or restatement); round-3 review is the
QUALIFYING CANDIDATE. Rounds 2 of 10.

## Round-3 findings (merged, 19 distinct) - binding for round 4

Claims packet clean (0 P1); dropped-edit attack now caught 13/13 by V-5 alone; E-9
single-reading verified; two-pass partition exhaustive; escalation decidable in the
intended case. The one P1 is the bar-lowering hole the qualifying calibration exists
to catch.
P1 x1 - YS3-1: a Writer-stated residue reaches no ledger, no reviewer, and no owner
gate (return goes only to the Orchestrator, who cannot originate findings; accepted
close reads the frozen ledger only), so a bracket can close ACCEPTED carrying a defect
its own author declared; "which is review material" is false as shipped; the
cannot-repair-inside-caps disjunct names no judge and bypasses the restatement remedy
and the owner cap authority; E-11/E-13/C-9 state the rule unqualified so the exception
is invisible to conformance readers. REPAIR: (a) the Orchestrator records each stated
residue item in the task record, and the pre-cap accepted close gains the condition
that every Writer-stated residue is accepted by the owner in the same residue-
acceptance step as open P2/P3; (b) the caps disjunct is gated: it applies only after a
compact complete restatement has been produced in the bracket - before that, the
restatement is the required path; (c) E-11, E-13, and C-9 gain the residue rule so no
gloss is unqualified; (d) drop or fix the false "review material" predicate.
P2 x8: YS3-2 (matrix incomplete-test disposition: uncovered pair classes stated in the
return through the same residue channel; a persisted body byte-identical to the
packet's current body has an EMPTY subject set - the coverage-only return is not a
restatement in substance); YS3-3 (escalation timed - the goal's next owner exchange
and no later than the completion report - and recorded in the task record; C-5 red
path gains its absence); YS3-4 (E-6 scoped to reuse: under fresh-per-round the harness
limit is inert and rows read fresh by configuration; no escalation fires); YS3-5
(former kept pairs -> computable form: the pairs the deleted clause keeps under the
current filter, computed from the packet's persisted current body before the deletion);
YS3-6+YC3 residue (defined term = any backticked string, full stop - over-inclusive is
acknowledged and safe, it only keeps more pairs); YC3-1 (blank line at body:217 drops
A-6 out of the assumptions table - restore, and split per YC3-12); YC3-2 (unescaped
pipe splits V-4's command cell - escape or fence); YC3-3 (E-1/E-11/E-12 anchors exceed
the pinned minimality bound - shorten to minimal unique suffixes; E-2/E-5 licensed by
the replaced-extent conjunct).
P3 x10: YC3-4 (V-5 before V-4 ordering); YC3-5 (I-2 quotation sentence-exact not
byte-exact - licensed, note it); YC3-6 (E-13 probe is the D033 title - C-11 red path
gains body coverage); YC3-7 (state the any-present-at-last-pass reading of
"surviving"); YC3-8 (consecutive = adjacent continuity entries); YC3-9 (deletion
re-run results reported under the deleted clause's identifier); YC3-10 (I-3 names
section 4 Goal flow); YC3-11 (G-4 bucket wording - D024 assignment stated); YC3-12
(A-6 split so each disclosure has its own load-bearing answer); YS3-7 (attempt =
dispatch, stated once).
LINE BUDGET: 300/300; remaining reserve ~5 lines (site-set file list -> G-2 pointer);
a compact complete restatement is authorized if the set cannot fit, with checklist.
Convergence: 27 -> 13 -> 19 raw but 1 open P0-P1. Round 4 = surgical (or restatement);
round-4 review is the QUALIFYING CANDIDATE. Rounds 3 of 10.

## Round-4 findings (merged, 16 distinct) - binding for round 5

ORCHESTRATOR AUDIT DISCHARGE (retirement guard): no open ledger row cites a retired
identifier - every round-3 finding was repaired in round 4, so the ten retirements are
lawful under the repair limb; B-5's trailing gap (B series ends at 4) is hereby recorded
in this task record per the guard. 9/10 merge targets verified strict supersets; B-5's
Failure half was lost (ZC4-3) and is a round-5 repair.
P1 x3:
1. ZS4-1 CAP TERMINAL: the residue channel's only owner gate is the pre-cap close; at
   the cap a residue is not a ledger row, blocks nothing, and is not among the P3s
   recorded to the owner - the escape is selected FOR by long brackets. REPAIR: the cap
   close's owner report gains stated residues alongside the open P3s (disclosure parity;
   fresh review each round remains the severity leg).
2. ZS4-2 NONE-DISJUNCT: condition 3's none branch stays satisfiable by its own reason
   while a residue stands, and the TASK residue-acceptance row still describes a
   P2/P3-only test. REPAIR: the none disjunct gains "and no Writer-stated residue is
   recorded for the goal"; the TASK row's template text names stated residues; "That
   step" referent fixed.
3. ZS4-3/ZC4-1 E-14 PROBE: spans a payload line break - V-2 fails on a CORRECT build
   and a dropped E-14 is undetectable. REPAIR: single-line probe (e.g. "in adjacent
   entries").
P2 x7: ZS4-4 (caps-gate undecidable for a replacement Writer - move the ordering to the
actor who can decide it: the Writer states a caps-blocked residue whenever the repair
exceeds a cap in force; the ORCHESTRATOR, who holds bracket history, dispatches the
restatement first when none has been produced); ZS4-5/ZC4-4 (fidelity: the Orchestrator
records the residue in the Writer's stated words - verbatim); ZS4-6 (staleness: a
residue is superseded when a later persisted body repairs the clause it names; the
Orchestrator marks it superseded and the owner accepts standing residues only); ZS4-7
(Approach rationale sentence updated - the close now reads the recorded residues too);
ZS4-8 (the two-pass/last-pass bound is load-bearing and untraced - R-7 or R-8 names it,
C-9's red path gains it); ZC4-2 (I-6 arithmetic: twelve still occur once, not thirteen);
ZC4-3/ZS4-10 (B-4's Failure cell gains the missing-row/mid-goal-change failure its
surviving disposition answers).
P3 x6: ZS4-11 (E-2 payload short lines); ZC4-6 (residue acceptance carries no authority
bound - note the P3-kinship reasoning in-body); ZC4-7 (E-6 vs E-3/E-11: escalation
counts replacements, so it fires at dispatch 3 under a never-retaining harness - state
it); ZC4-8 (E-7 anchor shortened to the minimal unique tail); ZC4-9 (filter's first
three disjuncts are judgment - acknowledged, uncoverable classes route to residue);
quotation/lean-body notes carried.
LINE BUDGET: 300/300, reserve exhausted. AUTHORIZED: fold the Failure boundaries table
into the criteria red paths (~9 lines) if needed - the charter's failure-boundary
section carried through red-path text. NO cap amendment.
Convergence: 27 -> 13 -> 19 -> 16 raw; open P0-P1 3. Round 5 = surgical (or third
restatement); round-5 review is the QUALIFYING CANDIDATE. Rounds 4 of 10.

## Round-5 findings (merged, ~10 distinct) - binding for round 6

Verified held: 16/16 anchors and probes (single-line check clean); 6/6 registers;
dropped-edit attack 7/7 with the four consumed anchors double-covered; B-retirement
PASS; E-7 grammar and satisfiability PASS (genuinely-empty goals close); E-16 preserves
automatic cap acceptance; the residue design's two-leg coherence verified END TO END in
protocol text; fold adequate at 8 of 9 items.
P1 x1 - QS5-1: the round-5 caps-ordering repair exists only in E-3's payload. C-9's
criterion still states the round-4 design ("the caps disjunct applies only after a
compact complete restatement"), contradicting the built text; C-9's red path has no
cap-blocked-repair detector (the fold's location claim is false for that one item,
QC5-4); the Orchestrator's restatement-first duty traces to no requirement and is
carried by neither E-13 nor E-15 (R-10 unmet for the clause). REPAIR, folding QS5-5:
bind the RESULT per the framework's own precedent - the next Writer result after a
cap-blocked residue, when no restatement has been produced in the bracket, is a compact
complete restatement (a result rule needs no channel and is decidable regardless of
which context serves); C-9's criterion updated to the round-5 design and its red path
gains the detector; R-8 gains the ordering sentence; E-13 and E-15 carry it.
P2: QS5-2/QC5-1 (one word - "no STANDING Writer-stated residue is recorded"; aligns
E-7 with E-12 and C-10; kills the superseded-only forced owner turn and the ambiguous
none record); QS5-3/QC5-2 (supersession decidable + reconciled: the Orchestrator marks
superseded only on the Writer's reported repair of the named clause in a later return -
marking on the Writer's report is recording, not origination - state the reconciliation
sentence per the identifier-mapping precedent); QS5-4/QC5-6 (E-16 pronoun: "is reported
to the owner at the same time"); QC5-3 (E-13/E-15 glosses gain the standing/superseded
qualifier).
P3: QS5-6 (supersession trigger gains "or deletes" so a deleted clause's residue does
not stand forever); QS5-7 (E-16 adopts E-7's "a Spec Writer stated in a return for this
goal"); QC5-4 (fold location claim corrected - cap-blocked repair sits in C-9's
criterion, or moves to the red path per the P1 repair); QC5-5 (one line enumerating all
recorded gaps: R-2, R-9, I-3, A-2, C-2, C-4, C-11, V-4, and the B series in full).
LINE BUDGET: 300/300 - repairs must be line-neutral via prose compaction; a third
restatement is authorized if not. NO cap amendment.
Convergence: 27 -> 13 -> 19 -> 16 -> 10. Round 6 = surgical; round-6 review is the
QUALIFYING CANDIDATE. Rounds 5 of 10.

## ACCEPTED CLOSE - round 6 (2026-08-30)

Convergence exit satisfied: lens coverage complete since round 2; qualifying round with
ZERO new P0/P1 in both packets; no open P0/P1 (QS5-1 repaired - the result-bound rule's
carriage chain verified verbatim-consistent across E-3/R-8/C-9/E-13/E-15, detector in
the red path, fold claim now true); no blocked verdict; no later Writer result. Both
packets: hash MATCH, 6/6 registers, 16/16 anchors and probes (single-line clean, E-15
one-row integrity held), dropped-edit attack 8/8 with double coverage, gap enumeration
exact, ID audit clean, lean-body self-compliant, four L6 attacks pressed and none
landed (result-rule enforcement inherits the pin's own model; supersession lands on
existing return content; none-disjunct aligned on standing; no consumed-anchor
regression). Case P closes on the none branch; E-16 unconditional at zero P3s.
Residue accepted under the owner's standing full-control directive (2026-08-29);
strict convergence knob: off (default). Residue (merged, 8 distinct):
P2 x3 - RS6-1 (the result-bound rule's antecedent is knowable only to the context that
stated the residue - under fresh-per-round or after replacement the receiving Writer
cannot evaluate it; SAME property as the pinned round-3 restatement rule at
PROTOCOL:474-476, inherited by following the precedent shape; worst case is the pinned
visible block; default reuse keeps it performable); RS6-2 (supersession trigger rides
a Writer repair report no charter return item requires - strict reading over-reports,
residues stand and the owner sees more, the safe direction); RS6-3 (a coverage-only
unchanged body is a complete restatement at the pin and discharges the forcing while
freeing no headroom - jointly satisfiable, no deadlock, residue still bars/reports).
P3 x5 - RS6-4 (C-10 keeps the retired beside-the-P3s phrasing; timing at a cap block
left to inference); RS6-5 (E-13 omits the cap-report leg E-15 carries); RS6-6 (deleted
payload clauses have no stated reporting handle); RC6-1 (C-10 criterion ellipsis lacks
standing); RC6-2 (standing homonym - E-16 reads without the superseded contrast; the
defining paragraph is 180 lines earlier in the same file).
Convergence trace: 27 -> 13 -> 19 -> 16 -> 10 -> 0 new P0/P1. Rounds 6 of 10.
Specification frozen as WRITERCFG-p6 46d43487...e947. Next: Builder.

## BUILD AND BUILD REVIEW (2026-08-30)

Build: commit 95fedce95d56afbcf2e3648f43b565b57f22f055 on claude/spec-writer-config,
base 58bb192, five files, 111 insertions 10 deletions, 16/16 payloads byte-identical.
One forced item (payload-mandated line widths) flagged.
Build review (fresh reviewer, rule-coverage): PASS - zero findings at any severity,
zero residue. All five built files RECONSTRUCT BYTE-FOR-BYTE from the base tree under
the body's own edit semantics (placement proven, not sampled); all live requirements,
criteria, and obligations re-run clean; hard freeze proven; the forced item judged
LICENSED (no column-width rule exists at the pin). One out-of-jurisdiction observation
(OBS-1, a likely-redundant bar in E-7's payload, jointly satisfiable) recorded against
the spec body for any future goal. First zero-residue build of the five fix goals.
