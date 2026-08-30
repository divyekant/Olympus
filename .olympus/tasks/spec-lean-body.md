# Goal: spec-lean-body

## Goal and scope

Fourth process-fix goal from the v060-agents retrospective. Issue #15. Two coupled
change sets:

1. Lean-body rule. The specification body carries claims and pointers. Evidence
   transcripts live in the task record. Reviewers re-probe every claim themselves.
   Embedded evidence was byte-waste in the v060-agents bracket and drove the body
   toward the cap.
2. Cap-amendment owner path. A legal, owner-gated, never-expected backstop for
   amending a body cap during a goal. This is the missing valve behind
   framework-review failure record 3: the Orchestrator raised a pinned cap by fiat
   and fresh review caught it (SJ-1).

Out of scope: VERSION bump and release (issue #23). Charter edits (fixed roles).

## Governance

| item | value |
| --- | --- |
| governing pin | d4244229ffe12a67d6efd94fbefbeaa446cef98e (post fix-3 repin) |
| governor checkout | /private/tmp/olympus-governor-d424422 |
| mutation base | /private/tmp/olympus-fix4-leanbody, branch claude/spec-lean-body, base d424422 |
| pinned machinery in force | sizing gate (fix 1), six-lens catalog (fix 2), population registers rule (fix 3) |

The body of this goal's specification must itself comply with the registers rule:
every enumeration the body relies on as complete is a marked population register.

## Sizing check (pinned gate)

| field | value |
| --- | --- |
| deliverables | 2 coupled change sets |
| projected bytes | 28,000 |
| projected criteria | 11 |
| result | fail (projected bytes exceed 20,000) |
| proposal reference | owner standing full-control directive of 2026-08-29, applied as the partition proposal send; decision requested: partition or proceed-unsplit |
| owner decision | proceed-unsplit (standing directive; the two change sets share the body-cap subject and partitioning them would split one rule family across two brackets) |

## Owner decisions

| # | decision |
| --- | --- |
| 1 | Proceed-unsplit per the sizing entry above. |
| 2 | VERSION bump and release excluded (issue #23). |
| 3 | Rolling repin policy: this goal governs under d424422; the pin rolls forward after every merge; a running goal keeps its creation-time governor. |

## Specification rounds

| field | value |
| --- | --- |
| packet identifier | LEANBODY-p5 |
| content hash | ccbd99fced796e19df719bf162dd9a917bb66aa40f2cee83752bac719e38a444 |

<!-- SPECIFICATION-BODY:BEGIN -->

## Problem

The specification body has two size caps: 300 lines and 48,000 bytes. In the `v060-agents`
bracket the body carried probe output, command output, and quoted file regions inside itself.
That reproduced text consumed the byte budget, the body reached a cap, and the Orchestrator
raised the cap on its own authority. The raise was illegal and fresh review caught it. That
goal is closed and its body is not preserved, so the byte history is not re-probeable; this
paragraph rests on its task record and on framework-review failure record 3.

Two defects produced that outcome. First, the governing text does not exclude reproduced
evidence from the body. Three Spec Writer charter sentences, which the protocol names, keep
six categories out of the body: the Evidence register, findings, hashes, round records,
reviewer text, and review state. None of the six covers probe output pasted into a
requirement, a command transcript pasted into an approach paragraph, or a file region pasted
into an assumption. Reviewers do not take a body's reproduced text as proof either: Claims
Reviewer re-runs every load-bearing evidence probe, samples the remaining register, and
traces each claim to an evidence-register entry or an inline probe, and Spec Reviewer does not
re-probe factual claims inside that jurisdiction. Reproduced text therefore buys no assurance
and costs bytes. Second, there is no legal way to amend a cap; the only recorded exits are a
compact complete restatement and a blocked goal, and that gap is what the illegal raise
filled. This specification adds the lean-body rule, which is the fix, and one owner-gated
cap-amendment path, which is a backstop expected never to run.

## Requirements

| ID | Requirement | Criteria |
| --- | --- | --- |
| REQ-1 | The protocol states that the body carries claims and pointers only, and defines the cases in which reproduced text is body content, each with a bound. | `AC-1`, `AC-2` |
| REQ-2 | The rule keeps a population register's recorded result inside the body and bounds what that result may hold. | `AC-1`, `AC-8` |
| REQ-3 | The rule denies reproduced text any evidentiary force without adding a reviewer duty or crossing a jurisdiction, and routes an evidence transcript to the return item the Writer charter already requires. | `AC-1`, `AC-9` |
| REQ-4 | The protocol carries one owner-only cap-amendment path with a recorded proposal, a stated cause, an exact new value, a stated path state, and a terminal state; the protocol names the amendment record in the reviewer handoff and in the sizing-entry enumeration. | `AC-3` |
| REQ-5 | The path states that it is expected never to run, and that an Orchestrator raising a cap on its own authority stays illegal. | `AC-3`, `AC-6` |
| REQ-6 | templates/TASK.md adds evidence transcripts to its body exclusions and holds the amendment record beside the sizing entry; docs/CONFORMANCE.md makes both rules checkable; docs/DECISIONS.md records the decision. | `AC-2`, `AC-4`, `AC-5`, `AC-6`, `AC-7` |
| REQ-7 | The change touches only the enumerated sites, and every other `BND-1`-normalized byte of the repository is unchanged. Backtick placement is outside that comparison and is covered by review, not by a command. | `AC-10` |

## Approach

The change is text only. It amends four files at ten sites, and adds no role, setting, state
value, gate, reviewer duty, or return item. The lean-body rule goes into the protocol
paragraph that already governs body content, which sits immediately before the
population-registers paragraph, so `the population-register rules below` resolves to that rule.

| ID | Boundary |
| --- | --- |
| BND-1 | `BND-1` is a comparison rule only. To compare two texts, delete every backtick character and collapse every run of whitespace to one space, on both sides. Bytes written into a file are not transformed: they keep the backticks and the wrapping that file already uses, and backtick placement is therefore invisible to every `BND-1` comparison. `reproduced` means text copied from a pre-existing source; a command the body composes is authored, not reproduced. |
| BND-2 | An edit replaces the anchored string only. Where the replacement changes a prose paragraph's length, the builder re-wraps that paragraph following the wrapping convention the file already uses. No wrap width is mandated, because no single width reproduces the touched paragraphs. A table row is one line at any length and is never wrapped; `VO-8` checks that, because normalization cannot. |
| BND-3 | Outside the anchored strings, the `BND-1`-normalized content of each amended file is unchanged, and no other file changes. Backtick placement and whitespace are outside this comparison; `VO-7` and `VO-8` carry the two facts that depend on them. |
| BND-4 | Charter files are not edited. Three charters carry register hits: two hold packet-input exclusions only, and the Spec Writer charter holds both a packet-input exclusion and a method sentence that is a body-content rule. This goal changes none of them; the Writer method sentence keeps its wording and the protocol rule governs the body. |

### Population registers

Both registers run from the root of a clean checkout of commit
`d4244229ffe12a67d6efd94fbefbeaa446cef98e`, with `LC_ALL=C` set by the runner and a `grep`
that supports PCRE. In the block below, a `register` line names the register, the line after
`command` is its command, and the lines after `output` are that command's output. Each
property is lexical and line-scoped, because `git grep` matches within one line. `PR-2` does
not use the token `reviewer transcript`, because that token also matches a plan-review
exclusion and adds only a charter file, which `BND-4` excludes.

```text
register PR-1 a tracked Markdown file that has a line containing 48,000, 48000, 300 lines, or body size cap
command
git --no-pager -c color.ui=false grep -lP '48,000|48000|300 lines|body size cap' d4244229ffe12a67d6efd94fbefbeaa446cef98e -- '*.md' | sort
output
d4244229ffe12a67d6efd94fbefbeaa446cef98e:docs/CONFORMANCE.md
d4244229ffe12a67d6efd94fbefbeaa446cef98e:references/PROTOCOL.md
d4244229ffe12a67d6efd94fbefbeaa446cef98e:templates/TASK.md
register PR-2 a tracked Markdown file that has a line containing review history, defensive annotation, or body diff
command
git --no-pager -c color.ui=false grep -lP 'review history|defensive annotation|body diff' d4244229ffe12a67d6efd94fbefbeaa446cef98e -- '*.md' | sort
output
d4244229ffe12a67d6efd94fbefbeaa446cef98e:agents/CLAIMS_REVIEWER.md
d4244229ffe12a67d6efd94fbefbeaa446cef98e:agents/SPEC_REVIEWER.md
d4244229ffe12a67d6efd94fbefbeaa446cef98e:agents/SPEC_WRITER.md
d4244229ffe12a67d6efd94fbefbeaa446cef98e:docs/CONFORMANCE.md
d4244229ffe12a67d6efd94fbefbeaa446cef98e:docs/DISTILLATION.md
d4244229ffe12a67d6efd94fbefbeaa446cef98e:references/PROTOCOL.md
d4244229ffe12a67d6efd94fbefbeaa446cef98e:templates/TASK.md
```

The site set is the union of both registers, less the hits `ASM-1` excludes, plus
`docs/DECISIONS.md` and the two sites `ASM-7` records. Neither register hits
`docs/WHITEPAPER.md`, which is therefore not amended, or `docs/DECISIONS.md`, which gains one
new row rather than an amendment to existing text.

### Exact strings

In the block below, a `site` line names the site and its location and delimits sites; a
field's text is every line between its `current` or `restated` label and the next label; a
blank line inside a text is a required paragraph break; and a label line is never written.
`SITE-5` is retired and leaves a recorded gap; its successor is `SITE-10`.

```text
site SITE-1 references/PROTOCOL.md, last sentence of the body-content paragraph
current
It must not contain review history or reviewer output.
restated
It must not contain review history or reviewer output. It carries claims and pointers only. Reproduced text, meaning text copied from a pre-existing source, is body content in exactly three cases: a recorded result licensed by the population-register rules below, whose command filters on the stated property; exact bytes that must appear in, or that an edit replaces in, an artifact the body requires, where output an obligation merely re-reads is not such bytes and where an anchor is no longer than uniqueness within its file and the edit require; and a quotation that one claim, one edit, or one acceptance criterion names, limited to the sentences of prose that carry the cited point and to at most three of them. Every other reproduction of text from a pre-existing source is an evidence transcript, and the body carries none. A register's recorded result is body content for that register's own completeness claim only, and when the population's members are regions of a file that recorded result is a digest of the command's output, optionally with the member count, because a digest changes whenever the population changes. Spec Writer reports an evidence transcript to the Orchestrator under the return item the charter already requires for the complete Evidence register and traceability map, and the body's claim points to that report. Reproduced text in the body carries no evidentiary force. Each reviewer verifies the claims in its own jurisdiction by that reviewer's own charter method, and text the body reproduces neither reduces nor replaces that method. A body that carries an evidence transcript is a specification defect, and the repair is the body.
site SITE-2 references/PROTOCOL.md, the persist step's body-content exclusion list
current
contains no earlier body, body diff, reviewer transcript, review history, or defensive annotation;
restated
contains no earlier body, body diff, reviewer transcript, review history, evidence transcript, or defensive annotation;
site SITE-3 references/PROTOCOL.md, last sentence of the cap paragraph
current
An oversized Writer result is incomplete and does not enter review.
restated
An oversized Writer result is incomplete and does not enter review.

The owner alone amends a body size cap, and only through this path. An Orchestrator raising a cap on its own authority is illegal, and this path does not change that. An amendment during an open specification bracket is expected never to happen: the rule that the body carries claims and pointers only is the fix for a body that approaches a cap, and the compact complete restatement is the standing remedy. The Orchestrator sends at most one cap-amendment proposal per goal. One proposal names one cap or both. It states the cause, the exact current value and the exact proposed value of each cap it names, and the frozen ledger's recorded state at the latest frozen round, which shows whether an open finding concerns reproduced text; the Orchestrator records that state and originates no determination. The path closes or is spent only on the owner's own reply turn. A grant is the owner's verbatim decision bytes naming an exact new value for each cap the reply amends. The owner may name a value the proposal did not propose, and that owner-named value is the amended value, because the proposal is a request and the owner is the authority; a scalar counter-value is determinate and therefore a decision, unlike a counter-boundary in the sizing gate, which changes the goal's scope and leaves that gate open. A reply naming values for only some proposed caps grants the named caps and leaves the others unamended. A reply that omits a value, a question, a conditional reply, and a settings change are not grants, and a reply that names a value and also asks a question or states a condition is not a grant; each leaves the path open. If the turn is interrupted after the proposal is recorded and before it reaches the owner, record a `halted` outcome, then re-send the proposal once while the path is open, and reuse the recorded proposal reference. The path is open until a proposal is refused, which closes it, or a grant is recorded, which spends it. A proposal by itself stops no round and blocks no goal, and no proposal changes another rule: the round cap, the restatement duty, and the rule that an oversized result does not enter review stay as stated. While the path is open the goal continues under the values in force, and its exits are the compact complete restatement, the proposal the Orchestrator may still send, and the standing duty to record the current state and stop as `blocked` when safe continuation is unclear. The Orchestrator records the proposal, the reply, and each amended value in the task record beside the sizing entry's `observed-at-round-1` record, because an amendment shows that entry's projection was low. An amended value replaces the stated value for that goal only, and governs from the first Writer result persisted after the grant; a result persisted before that is measured against the value in force when it was persisted. At most one amendment takes effect in a goal. The goal blocks when a Writer result exceeds a cap in force, a compact complete restatement has not brought the body under that cap, and the path is closed or spent, in any order.
site SITE-4 templates/TASK.md, last sentence of the specification-rounds preamble
current
Never put earlier bodies, body diffs, reviewer transcripts, review history, or defensive annotations in the body.
restated
Never put earlier bodies, body diffs, reviewer transcripts, review history, evidence transcripts, or defensive annotations in the body. The body carries claims and pointers only, under the protocol rule for reproduced text.
site SITE-6 docs/CONFORMANCE.md, last sentence of item 20
current
Earlier bodies, body diffs, reviewer transcripts, review history, round records, and defensive annotations are not embedded in it.
restated
Earlier bodies, body diffs, reviewer transcripts, review history, round records, evidence transcripts, and defensive annotations are not embedded in it. The body carries claims and pointers only. Reproduced text is body content only in the three cases the protocol rule for reproduced text states, each under the bound that rule sets: a licensed register result; exact bytes that must appear in, or that an edit replaces in, an artifact the body requires; and a bounded quotation a claim, an edit, or a criterion names. Reproduced text carries no evidentiary force, and each reviewer verifies the claims in its own jurisdiction by that reviewer's own charter method.
site SITE-7 docs/CONFORMANCE.md, second-to-last sentence of item 23
current
An oversized result cannot enter review.
restated
An oversized result cannot enter review. Only the owner amends a body size cap, through at most one Orchestrator proposal per goal that names one cap or both, states the cause and the exact current and proposed value of each cap named, and is granted in the owner's own reply turn by verbatim decision bytes naming an exact new value, which the owner may set to a value the proposal did not propose. The Orchestrator records the proposal, the reply, the path state, and each amended value in the task record beside the sizing entry. An amended value governs that goal only, from the first Writer result persisted after the grant. The goal blocks when a result exceeds a cap in force, a restatement has not brought the body under that cap, and the path is closed or spent. An Orchestrator that raises a cap on its own authority fails this item.
site SITE-8 docs/DECISIONS.md, last row of the accepted-decisions table
current
Byte-exact approval phrasing was dropped as ceremony without a defect it prevented. |
restated
Byte-exact approval phrasing was dropped as ceremony without a defect it prevented. |
| D032 | Lean specification body with an owner-only cap amendment | The body carries claims and pointers only. Reproduced text is body content only in the three cases the protocol rule for reproduced text states, each under the bound that rule sets: a licensed register result; exact bytes that must appear in, or that an edit replaces in, an artifact the body requires; and a bounded quotation a claim, an edit, or a criterion names. Reproduced text carries no evidentiary force, and each reviewer verifies the claims in its own jurisdiction by that reviewer's own charter method. Only the owner amends a body size cap, through at most one recorded proposal per goal, granted in the owner's own reply turn at a value the owner names, and effective from the first Writer result persisted after the grant. The amendment is a never-expected backstop; an Orchestrator still cannot raise a cap on its own authority. |
site SITE-9 references/PROTOCOL.md, the Claims Reviewer bounded-handoff sentence
current
current task metadata, current evidence, and the open finding ledger.
restated
current task metadata including the cap-amendment record when the task record holds one, current evidence, and the open finding ledger.
site SITE-10 templates/TASK.md, the sizing-check row whose first cell is observed-at-round-1
current
| `observed-at-round-1` | `<body bytes, criteria count, and deliverable count observed at round 1, or not applicable>` |
restated
| `observed-at-round-1` | `<body bytes, criteria count, and deliverable count observed at round 1, or not applicable>` |
| `cap-amendment` | `<proposal reference and its cause; the exact current and proposed value of each cap named; the owner reply with its verbatim decision bytes; the path state, open, closed, or spent; each amended value and the first persisted Writer result it governs, or none>` |
site SITE-11 references/PROTOCOL.md, the closing item of the sizing-entry field enumeration
current
the `decision-value reference` that every Spec Writer packet record carries, and `observed-at-round-1` once the goal completes specification round 1;
restated
the `decision-value reference` that every Spec Writer packet record carries, `observed-at-round-1` once the goal completes specification round 1, and the cap-amendment record once the task record holds one;
```

`SITE-10` is the successor of the retired `SITE-5`, which anchored the convergence-state table
before the amendment record moved to its single home in the sizing-check section. This
sentence is `SITE-10`'s own clause for the purpose of the successor rule.

## Invariants

| ID | Invariant |
| --- | --- |
| INV-1 | A population register's recorded result is body content for that register's own completeness claim. The lean-body rule never removes it. |
| INV-2 | Exact bytes that must appear in an artifact the body requires, and exact bytes that an edit replaces in one, are both body content, so a deletion edit stays specifiable. |
| INV-3 | Only the owner amends a cap, and the owner sets the value. An Orchestrator cap raise is illegal at every point in a goal, whether or not a proposal is open. |
| INV-4 | A cap amendment is scoped to one goal. It changes no round cap, restatement duty, oversize rule, acceptance condition, or reviewer jurisdiction. |
| INV-5 | The change adds no reviewer duty and moves no check across a jurisdiction. It removes evidentiary force from reproduced text and leaves each charter method as written. |

## Assumptions

| ID | Assumption | State | Evidence or probe | Load-bearing |
| --- | --- | --- | --- | --- |
| ASM-1 | The four amended files are the complete site set for the two token classes at the pin. | supported | `PR-1` and `PR-2`, less these excluded hits: three charters under `BND-4`; docs/DISTILLATION.md, whose hit lists what Olympus did not copy from its source influences; the protocol lens sentence about a packet body that differs between rounds, a substring hit stating no exclusion; the protocol sentence on what is not task state, which governs task state and which this specification does not touch; and the templates/TASK.md sentence saying the body size caps live in the protocol, a pointer the protocol edits reach. | yes |
| ASM-2 | No file at the pin states a cap or a body-content exclusion that the two registers miss and that this change should amend. | unexercised | Both registers are lexical and line-scoped, so a paraphrase carrying none of the seven tokens is missed, and so is a token wrapped across two lines. agents/DOCS_WRITER.md is one such wrapped miss, carrying `review history` across a line break; it is a charter under `BND-4`, and its sentence tells Docs Writer to remove review history from documentation, which is not a body-content rule. Six of the ten anchors carry no token themselves and are reached through their files. | yes |
| ASM-3 | Each current text occurs exactly once in its file at the pin. | supported | `VO-2` | yes |
| ASM-4 | The amendment record reaches each specification reviewer without a new packet field or return item. | supported | `SITE-9` names the record inside the Claims Reviewer handoff, and the Spec Reviewer handoff receives the same task metadata by reference. The record's single home is the sizing-check section. The protocol and the reviewer charters already differ on how widely `task metadata` reaches; this change adds no new divergence and relies only on the protocol handoff sentence it amends. | yes |
| ASM-5 | Detecting an evidence transcript, and judging an anchor against the minimality bound, are reviewer judgements rather than mechanical counts, so the rule creates no Orchestrator gate. | supported | the protocol Orchestrator aggregation boundary | yes |
| ASM-6 | Whitespace, list indentation, and backtick placement inside an amended file are invisible to `VO-5`, which compares `BND-1`-normalized text. | supported | `BND-1` erases all three by construction. Four facts depend on them: the `SITE-3` paragraph break, covered by `VO-7`; the single-line form of the two inserted table rows, covered by `VO-8`; `SITE-2`'s three-space list indent; and `SITE-6`'s four-space continuation indent. The last two and backtick placement are left to review. | yes |
| ASM-7 | Two sites are not reachable from any register, because no register covers where a task-record field is enumerated. | supported | `SITE-9` and `SITE-11` were found by reading the protocol's handoff and sizing-entry enumerations. A register over that class would need a property no token expresses, so this specification states the gap rather than claiming register coverage it does not have. | yes |

## Authority and data flow

The Orchestrator writes the proposal and records the owner's reply verbatim, each amended
value, the path state, and the frozen ledger's state the proposal cites; it originates no
determination, grants no amendment, sets no value, and raises no cap. The owner grants or
refuses on the owner's own reply turn and names the value that takes effect. Each
specification reviewer receives the amendment record as task metadata and reports inside its
own jurisdiction under its own charter method, gaining no new duty and no return item. Spec
Writer reports an evidence transcript under the return item its charter already requires, and
never sends or learns of a proposal, which is task-record state.

## Failure boundaries

Both readings of every new or changed clause follow: escape asks whether a clause can be
abused, deadlock whether it can stall work.

| Reading | Question | Result |
| --- | --- | --- |
| escape | Can the amendment path become a routine valve? | No. One proposal per goal; a refusal closes it; a grant needs the owner's verbatim bytes naming an exact value, and the path closes or is spent only on the owner's own reply turn, so no standing pre-authorization, settings change, or mixed reply grants it. |
| escape | Can a new goal reset the counter? | Yes, and that is the intended cost. A new goal identifier brings a new sizing check, a new bracket, and no carry-over of the earlier body, so re-minting a goal costs more than a restatement. |
| escape | Does the owner counter-value rule let the Orchestrator steer the cap? | No. The Orchestrator proposes and records; the owner names the value. A scalar value is determinate, so it decides, while a sizing-gate counter-boundary changes scope and decides nothing. |
| escape | Can a grant legalize a body already persisted oversize, or can an oversized body enter review while a proposal is open? | No to both. The oversize rule holds until a grant is recorded, and an amended value governs only from the first Writer result persisted after the grant. |
| escape | Can a transcript ride the quotation case, or a 200-line anchor ride case two? | No. The quotation case admits at most three sentences of prose, each named by one claim, edit, or criterion, and command output is not prose. Case two now bounds an anchor to what uniqueness and the edit require, so a long anchor with a one-word edit is not licensed. |
| escape | Is the re-read escape still closed after case two widened? | Yes. Case two covers bytes an edit replaces as well as bytes it requires, and still excludes output an obligation merely re-reads. |
| escape | Can a Writer keep a transcript by copying from a source that is not a file? | No. The residual covers text copied from any pre-existing source, so an owner message, a role return, a log, and a web page are covered, and intent is not tested. |
| escape | Does the proposal make the Orchestrator judge lean-body conformance? | No. It cites the frozen ledger's recorded state, which is recording. |
| deadlock | Does the repaired disclaimer let a refused goal escape blocking? | No. The disclaimer now scopes to the proposal itself. A refusal closes the path, and a closed path is the block clause's third conjunct, so the earlier reading that left a refused, oversize, failed-restatement goal with no terminal state is gone. |
| deadlock | Does dropping the word refused from that disclaimer create pressure to grant? | No. A refusal blocks only in combination with a result over a cap in force and a failed restatement. A refusal on a healthy body still stops nothing. |
| deadlock | Nothing obliges the Orchestrator to propose. Does an unproposed goal have an exit? | Yes, three, and the clause names them: the compact complete restatement, the proposal that stays available while the path is open, and the standing duty to record the state and stop as blocked when safe continuation is unclear. |
| deadlock | Does the owner naming a different or partial value waste the single proposal? | No. Such a reply grants the named caps at the owner's values and leaves unnamed caps as stated. |
| deadlock | Does the block clause over-fire on a healthy body, or under-fire after a grant? | Neither. It requires a result exceeding a cap in force, so a findings-stagnation restatement under both caps triggers nothing; and a recorded grant spends the path, which satisfies the third conjunct exactly as a refusal does. |
| deadlock | Can a deletion edit, a cited quotation, and a universal claim still be specified? | Yes. Case two covers bytes an edit replaces, case three covers a bounded quotation a claim names, and a population register covers a universal or absence claim. |
| deadlock | Does removing evidentiary force break the Claims claim-to-evidence trace or its quote claim class? | No. The trace reads the Evidence register, which stays a return item, and a claim with no entry grades `unverified`. Case three keeps a cited quotation in the body, so the quote class still has a subject. |
| deadlock | Does the normalized freeze forbid the re-wrap that `BND-2` requires? | No. `BND-3` and `VO-5` compare normalized text, in which wrapping does not exist. `VO-7` and `VO-8` carry the two whitespace facts that matter; `ASM-6` records the rest. |

### Clause-interaction matrix

| Pair | Shared site | Interaction |
| --- | --- | --- |
| `BND-1`, `BND-2`, `BND-3`, `VO-5`, `VO-7`, `VO-8`, and `AC-10` | comparison space | One design. Every anchor match and every freeze happens in `BND-1`-normalized space, where wrapping and backticks do not exist; `BND-2` leaves wrapping to the builder because no width reproduces the touched paragraphs. `ASM-6` names what normalization cannot see, and `VO-7` and `VO-8` cover the two facts that depend on it. |
| the three-case rule and its three bounds | the carve-out | One design. Case one is bounded by the digest rule, which engages only when the members are regions of a file; a population of commits or refs falls to the residual instead. Case two is bounded by the re-read exclusion for kind and the anchor-minimality clause for quantity. Case three is bounded by the three-sentence prose limit. Widening any one voids the residual, so they move together. |
| lean-body rule, the population-registers rule, and the Writer charter's three exclusion sentences at method 6, method 10, and the self-check bullet | body content | Complementary and generalising. The register result is named as body content, so both rules hold at once, and the lean-body rule sits immediately above the register rule and names it. The charter's three sentences exclude six categories; the rule excludes reproduced text in any shape and any section, and routes it to the same return item the charter already requires. |
| lean-body rule, the Claims inline-probe wording, and the rule on what is not task state | claim tracing and destination | Narrowed domain, no conflict. An inline probe in the body is now a register result, prescribed bytes, or a bounded quotation, and the Evidence register carries the rest. The destination is a Writer return item, not task state. No charter text changes. |
| the amendment record, `SITE-9`, `SITE-11`, and the sizing-check section | delivery | One home, three mentions. The record lives beside `observed-at-round-1`; `SITE-11` adds it to the protocol's enumeration of that entry's fields, and `SITE-9` names it in the handoff, so a reviewer receives it as task metadata rather than as convergence state, which the protocol lists as a separate class. |
| the path state, the block clause, the open-path exits, the restatement duty, and the pre-cap accepted close | termination | One design. The path state supplies the third conjunct, so the block is order-independent and cannot fire on a healthy body; the open-path exits keep an unproposed goal terminating; an amendment excuses no restatement; and a proposal is not a finding and persists no Writer result, so it neither creates nor removes a qualifying round. |
| cap-amendment path and the Orchestrator aggregation boundary | recording | The Orchestrator records the owner's decision bytes, the path state, and the ledger's state, and originates none of them. |

### Path walks

| Walk | Sequence | End state |
| --- | --- | --- |
| W-1 | Proposal with cause, exact values, and ledger state; owner grants with verbatim bytes, or names a value the proposal did not propose, or names only some proposed caps. | Grant at the owner's values; unnamed caps stay as stated; the path is spent. |
| W-2 | A result exceeds a cap in force and a restatement does not bring it under; the proposal is refused, in either order relative to that restatement. | Goal blocks. |
| W-3 | A grant is recorded; a later result still exceeds the amended cap after a failed restatement. | Goal blocks. A spent path satisfies the same conjunct as a refusal. |
| W-4 | A proposal is refused, then findings stagnation triggers a restatement on a body well under both caps. | No block. The first conjunct is false. |
| W-5 | No proposal is ever sent and a restatement does not bring the body under the cap. | The path stays open, so this clause does not block. The exits are a further restatement, the available proposal, and the standing stop-as-blocked duty. |
| W-6 | The turn is interrupted after the proposal is recorded and before it reaches the owner. | `halted` recorded; one re-send while the path is open, reusing the recorded proposal reference. |
| W-7 | An oversized result is rejected and a grant follows, or a round's packet is frozen and a grant follows during that round. | The amended value governs the restatement that rejection triggered, and governs no earlier-frozen round; the metadata those reviewers received is correct as of dispatch. |

## Acceptance criteria and red paths

| ID | Criterion | Red path |
| --- | --- | --- |
| AC-1 | In references/PROTOCOL.md the `SITE-1` restated text occurs exactly once under `BND-1`, and it carries the three-case rule, the command-filters clause, the digest bound, case two covering bytes that must appear and bytes an edit replaces with both the re-read exclusion and the anchor-minimality bound, the bounded quotation case, the return-item destination, and the no-evidentiary-force clause. | Any one is absent; the residual is narrower than text copied from any pre-existing source; case two omits replaced bytes, which would make a deletion edit unspecifiable, or omits the minimality bound, which would license a long anchor for a one-word edit; the quotation case carries no length bound; or the rule regains a purpose qualifier such as offered in support of a claim. |
| AC-2 | The `SITE-2`, `SITE-4`, and `SITE-6` restated texts each occur exactly once in their files under `BND-1`, and each of those three current texts occurs zero times. | Any of the three exclusion lists still omits evidence transcripts. |
| AC-3 | In references/PROTOCOL.md the `SITE-3`, `SITE-9`, and `SITE-11` restated texts each occur exactly once under `BND-1`, and `SITE-3` carries owner-only authority, the one-proposal limit, one-cap-or-both scope, the stated cause, each exact value, the ledger-state citation, the restrictive owner-reply-turn operator, the counter-value clause with its sizing-gate distinction, the partial-grant clause, the non-grant list including a mixed reply, the interruption clause, the open-closed-spent path state, the proposal-scoped disclaimer, the three named open-path exits, the sizing-entry record, the goal-scoped effect from the first result persisted after the grant, the three-conjunct order-independent block clause, and the never-expected statement. | Any one is absent; the disclaimer again covers a refused proposal, which would leave a refused, oversize, failed-restatement goal with no terminal state; the block clause omits the cap-in-force conjunct and fires on a healthy body; the block clause omits the spent state; or the handoff or the sizing enumeration does not name the record. |
| AC-4 | In templates/TASK.md the `SITE-10` restated text occurs exactly once under `BND-1`, the cap-amendment row follows the observed-at-round-1 row inside the sizing-check table, and each row is one line. | The row is missing, wrapped across lines, placed in the convergence-state table, or omits the cause, each exact value, the verbatim owner bytes, the path state, or the first persisted result it governs. |
| AC-5 | In docs/CONFORMANCE.md item 20 carries the lean-body rule, names each of the three cases, and points to the protocol rule for reproduced text for the bound on each. | Item 20 states the exclusion without the rule, omits a case, or uses the term population register, which does not occur in that file. |
| AC-6 | In docs/CONFORMANCE.md the `SITE-7` restated text occurs exactly once under `BND-1`, and item 23's final sentence about completed round 10 is unchanged. | Item 23 does not make an Orchestrator cap raise a conformance failure, omits the block condition, or the edit displaced the final sentence. |
| AC-7 | In docs/DECISIONS.md the accepted-decisions table carries exactly one row whose first cell is `D032`, that row follows the `D031` row, and it points to the protocol rule rather than naming a term that file does not define. | The row is absent, duplicated, renumbers an existing decision, or uses the term population register. |
| AC-8 | The amended references/PROTOCOL.md names a population register's recorded result as body content, so the population-registers rule and the lean-body rule are jointly satisfiable, and this body itself satisfies both. | A body that satisfies one rule breaks the other. |
| AC-9 | No amended file states or implies a reviewer duty to re-probe every claim, and no amended file moves a check across the Claims and Spec jurisdictions. | An amended file contradicts the Spec Reviewer boundary against re-probing inside the Claims jurisdiction, or restates the Claims checklist as re-probe every claim. |
| AC-10 | The name-only diff from the base commit lists exactly references/PROTOCOL.md, templates/TASK.md, docs/CONFORMANCE.md, and docs/DECISIONS.md, and each file's `BND-1`-normalized content equals its base version's normalized content with only that file's substitutions applied. | Any other file changes, or an amended file's normalized content differs from its base version anywhere outside its anchored strings. |

## Validation obligations

| ID | Obligation |
| --- | --- |
| VO-1 | Re-run the `PR-1` and `PR-2` commands at the recorded commit from a clean checkout root with `LC_ALL=C` set. Each output equals its recorded output. |
| VO-2 | For each site, normalize the file at the recorded commit under `BND-1`, then count occurrences of the normalized current text with `grep -o -F` piped to `wc -l`, because normalization puts the file on one line and a line count would be structurally wrong. Each count is exactly 1. |
| VO-3 | After the edits, repeat the `VO-2` procedure on the working tree for every current text and every restated text. Each restated-text count is 1. The current-text counts are, in `SITE-1`, `SITE-2`, `SITE-3`, `SITE-4`, `SITE-6`, `SITE-7`, `SITE-8`, `SITE-9`, `SITE-10`, `SITE-11` order, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0; a count of 1 occurs exactly where the restated text contains the current text unchanged, and each such count is 1 and not more. |
| VO-4 | Run the name-only diff from the base commit to the goal head. The output lists exactly the four amended files. |
| VO-5 | For each amended file, normalize the base-commit copy under `BND-1`, apply that file's substitutions in normalized space, normalize the working-tree file under `BND-1`, and compare the two normalized strings. Each comparison reports equality. This closes `BND-3` and `AC-10`. It does not close `BND-2`, because normalization erases wrapping; `VO-7` and `VO-8` close what it cannot. |
| VO-6 | Run the identifier command below. Empty output shows that no amended file cites an identifier that only this body defines. |
| VO-7 | Run the paragraph-break command below. It prints `1`, which shows that exactly one occurrence of the amendment paragraph's opening line is preceded by an empty line. A count of `0` means that opening was merged into the sentence above it. `VO-3` closes duplication, so a count above 1 cannot arise from this change. |
| VO-8 | Run the two single-line commands below. Each prints `1`, which shows that the inserted row begins and ends on one line. A wrapped row prints `0`. |

The `BND-1` transform is `tr -d` on the backtick character, then `tr -s '[:space:]' ' '`. All
four commands below read the working tree, and the first needs a `grep` that supports PCRE,
because `git grep -E` does not honour `\b` in this environment.

```text
git --no-pager -c color.ui=false grep -nP '\b(REQ|INV|BND|ASM|PR|SITE|AC|VO|W)-[0-9]' -- references/PROTOCOL.md templates/TASK.md docs/CONFORMANCE.md docs/DECISIONS.md
awk 'p=="" && /^The owner alone amends a body size cap/{n++} {p=$0} END{print n+0}' references/PROTOCOL.md
awk '/^\| .cap-amendment. \|.*\| *$/{n++} END{print n+0}' templates/TASK.md
awk '/^\| D032 \|.*\| *$/{n++} END{print n+0}' docs/DECISIONS.md
```

## Rollout/rollback

Rollout is the merge of the goal branch; rollback is a revert of that commit, and no state,
migration, or configuration depends on it. An amendment already granted stays recorded in its
task record, a revert removes the path for later goals only, and no accepted body becomes
invalid, because the rule creates a finding class rather than a retroactive gate.

## Non-goals

| Item | Reason |
| --- | --- |
| Charter file edits, and any new reviewer duty, return item, or packet field | Fixed roles, and an owner scope decision. `BND-4`, `ASM-4`, and `INV-5`. The amendment record is named inside existing protocol sentences, and an evidence transcript rides the Writer return item the charter already requires. |
| A mechanical Orchestrator check for evidence transcripts or anchor minimality | `ASM-5`. A mechanical gate would let the Orchestrator originate a finding. |
| VERSION bump and release | Excluded by owner decision and tracked separately. |
| A cap reduction, an amendment outside the specification bracket, or a PROJECT setting for cap values | The path is designed for a raise and states no direction, so an owner-named lower value is operable but untested and unintended. A setting would make the amendment standing authority, and a settings change is named as not a grant. |

## Provenance

| Field | Value |
| --- | --- |
| governing pin | d4244229ffe12a67d6efd94fbefbeaa446cef98e |
| source base | d4244229ffe12a67d6efd94fbefbeaa446cef98e |
| task record | .olympus/tasks/spec-lean-body.md |
| evidence location | the Spec Writer return item for the Evidence register and traceability map |
| owner decisions applied | proceed-unsplit; release excluded; rolling repin |

<!-- SPECIFICATION-BODY:END -->

## Round table

| round | packet | Claims packet | Spec packet | merged distinct | lines | bytes | lenses | result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LEANBODY-p1 382eb371...4823 (first draft) | 14 (5 P1, 5 P2, 4 P3) | 26 (1 P0, 9 P1, 11 P2, 5 P3) | ~33 distinct (1 P0, 11 P1, ~15 P2, ~6 P3) | 290 | 24026 | Claims L1+L5; Spec L2+L3 | DOES NOT QUALIFY - LS1 P0 |
| 2 | LEANBODY-p2 55256e8e...b2a4 (round-1 full repair; 8 sites; PR-2 replaced per LS7 deviation) | 13 (5 P2, 8 P3) | 14 (6 P1, 6 P2, 2 P3) | 25 (5 P1 clustered, ~11 P2, ~9 P3) | 293 | 31431 | Claims L1+L6; Spec L4+L6 | DOES NOT QUALIFY - LSP2-1..6 P1 |
| 3 | LEANBODY-p3 3855ba1f...5c28 (round-2 full repair; 9 sites; normalized-freeze trio; owner counter-value grant) | 6 (2 P1, 4 P2) | 11 (3 P1, 5 P2, 3 P3) | 14 (4 P1, 7 P2, 3 P3; QS3-1=QC3-2) | 299 | 35418 | full mandate + L6 attack (both) - QUALIFYING CANDIDATE | DOES NOT QUALIFY - 4 P1 |
| 4 | LEANBODY-p4 7874d914...ff9d (round-3 full repair; three-case rule; path-state machine; SITE-5 retired with gap) | 6 (2 P2, 4 P3) | 10 (1 P1, 4 P2, 4 P3, 1 handoff) | 10 (1 P1, 5 P2, ~8 P3; FS4-1=FC4-1, FS4-7=FC4-2) | 297 | 39173 | full mandate + L6 attack (both) - QUALIFYING CANDIDATE | DOES NOT QUALIFY - FS4-1 P1 |
| 5 | LEANBODY-p5 ccbd99fc...a444 (compact complete restatement; round-4 full repair; SITE-11; minimality bound shipped) | 4 (4 P3) | 8 (2 P2, 6 P3) | 10 (2 P2, ~8 P3; GS5-8=GC5-2, GS5-1 subject = GC5-3) | 298 | 41127 | full mandate + L6 attack (both) - QUALIFYING CANDIDATE | QUALIFIES - accepted close |

## Round-1 findings (merged) - binding for round 2

Full packets in orchestration transcript. Dedup: LC5=LS2, LC9=LS16, LC6=LS25,
LC1+LC2 subsumed by LS7, LC11=LS23, LS18 repairs jointly with LS4.
P0: LS1 (enacted re-probe duty contradicts SPEC_REVIEWER charter jurisdiction bound and
raises CLAIMS_REVIEWER above load-bearing+sample; rescope to per-jurisdiction,
charter-accurate wording in ALL THREE enacted strings).
P1 x11: LS2/LC5 (AC-1/AC-6 zero-counts unsatisfiable - correct to 1); LS3 (load-bearing
narrowings not enacted, esp. prescribed-bytes = only bytes an implementer must match or
write; required-output escape); LS4+LS18 (PROTOCOL weaker than CONFORMANCE - adopt the
strong only-two-cases form in PROTOCOL, drop the offered-in-support loophole from the
operative rule); LS5 (evidence destination has no actor, host, or AC - route via existing
Writer return items as the registers rule did; reconcile with PROTOCOL:828-829); LS6
(Claims Reviewer amendment-reporting duty rides no return item - drop it; Orchestrator
records, reviewers receive as metadata, conformance binds the record); LS7 (register
properties do not select the concepts; BND-4 false - honest re-gloss, PR-1 pattern gains
body size caps, third register for exclusion-list sites incl. DISTILLATION.md:27 check);
LS8 (proposal cites frozen ledger state, Orchestrator originates no determination); LS9
(INV-4 one-number vs SITE-2 each-cap - unify on named-caps-per-goal); LS10 (BND-3 has no
VO - add normalized-equality obligation closing BND-2+BND-3); LC3 (PROTOCOL:307-309 third
exclusion list unamended - new site; check :449-450); LC4 (VO-2 tr recipe returns 0 -
correct transform tr -d backtick, tr -s [:space:] to one space).
P2 (prescribed): LS11 (question/conditional-reply not-a-grant clause per sibling gates);
LS12 (refusal branch terminal is blocked - state honestly; remove unreachable sizing-gate
exits); LS13 (walk O2/O3: grant-after-oversize governs the restatement dispatch;
grant-after-freeze governs no earlier round, absence report is as-of-dispatch metadata);
LS14 (interruption halted/re-send clause per sizing gate); LS15 (anti-retroactivity unit
unified: first Writer result persisted after the grant, all three sites); LS16/LC9 (REQ-6
docs trio undefined - name the files); LS17 (register-relabel escape - recorded result is
body content for the register's own completeness claim only; identity-only output for
file-region members); LS19 (BND-2 table carve-out - a table row stays one line); LS20
(VO-3 enumerates the seven expected counts); LS21 (granted amendment recorded beside
observed-at-round-1 - sizing feedback link); LC6/LS25 (body-size-cap class defined);
LC7 (SITE-6 anchor descriptor); LC8 (SITE-4 written bytes keep source backticks); LC10
(Problem claims gain a pointer or honest unverifiable note).
P3: LS22 (binds-every-role overclaim); LS23/LC11 (AC-10 orphan); LS24 (rules-below
referent); LS26 (load-bearing+sample premise); LC12 (dead body-cap disjunct); LC13
(register command/output machine-separable delimiting); LC14 (line headroom 290/300 -
restructure for headroom).
Positives settled (do not re-litigate): registers reproduce; 7/7 anchors unique; site-set
arithmetic; ASM-3 input side; paragraph adjacency; INV-2 self-consistency; sites cover
REQs; Orchestrator-as-proposer inside aggregation boundary. Round 2 lenses: Claims L1+L6;
Spec L4+L6 (coverage complete at round 2). Rounds 1 of 10.

## Round-2 findings (merged) - binding for round 3

Dedup: LSP2-1+LSP2-2+LC2-5 one cluster; LSP2-9=LC2-1; LC2-4 folds into LSP2-5.
Coverage complete (all six lenses have run). LS7 deviation VERIFIED SOUND by old-command
reconstruction. Round-1 repairs largely held; new P1s are build-mechanics (L4, first run)
and gate escapes the repairs created.
P1 x5 (clustered):
1. VO-5/BND-2/AC-10 executability cluster (LSP2-1, LSP2-2, LC2-5): five of eight anchors
   are not byte-contiguous in base; no wrap width reproduces the touched paragraphs;
   BND-2's mandatory re-wrap trips AC-10's red path at three sites by construction.
   REPAIR: move the freeze and the check into BND-1 normalized space - BND-3 becomes a
   normalized-content freeze outside the anchored strings, wrap is builder discretion
   per file convention, VO-5 = normalize base, substitute in normalized space, normalize
   tree, compare equality; AC-10 red path normalized identically.
2. LSP2-3: "changes a value" non-grant clause caps the owner's own authority (a reply
   naming a different exact value can never take effect). REPAIR: an owner reply naming
   a different exact new value in the owner's own reply turn IS a grant of that value;
   non-grant list = omits a value, question, conditional, settings change.
3. LSP2-4: refusal-first then restatement-fails has no terminal. REPAIR: block clause
   made order-independent - the goal blocks when the path is closed and a compact
   complete restatement has failed, in either order.
4. LSP2-5 (+LC2-4): amendment record placed in convergence state, which bounded handoffs
   do not send; SITE-3 vs SITE-5 disagree on location. REPAIR: record lives in the
   sizing-check section beside observed-at-round-1 (one location, all sites agree), and
   the reviewer-handoff enumeration is amended to name the cap-amendment record (new
   site if needed).
5. LSP2-6: case two "match or write" admits any transcript via a re-read obligation
   (VO-1 shape). REPAIR: the narrowing ships in ALL THREE restated texts - output an
   obligation merely re-reads is not prescribed.
P2 (binding): LSP2-7 (region-population reductions: digests only - names have no
referent for regions, counts miss in-place edits; member count optional alongside);
LSP2-8 (state the counting command: grep -oF piped to wc -l); LSP2-9/LC2-1 (PR-1
sentence hedged lexical-only like PR-2); LSP2-10 (CONFORMANCE/DECISIONS restated texts
point to the protocol rule, as SITE-4 does); LSP2-11 (answer the new-goal reset row
plainly; walk proposal-cancelled-new-goal); LSP2-12 (residual made universal: every
other reproduction of text from any pre-existing source); LC2-2 (SPEC_WRITER carries
two PR-2 hits; :66 IS a body-content rule - fix table and BND-4); LC2-3 (Problem states
the charter's three exclusion sentences and six categories accurately).
P3: LC2-6 (SITE-3 backticks on halted, observed-at-round-1); LC2-7 (cell convention
", or none"; round->result); LC2-8 (paragraph-break undetectable in normalized space -
record as known limit of the normalized check); LC2-9 (reviewer-transcript token note);
LC2-10 (define reproduced: text copied from a pre-existing source; authored commands
are not reproduced); LC2-11 (back-pointer from the registers paragraph to the bounds
above, or record why not); LC2-12 (Problem sentence qualified: load-bearing + sample +
inline-probe trace); LC2-13/LSP2-14 (REQ-6 wording honest about what each file
carries); LSP2-13 (PCRE stated in the environment note).
Structural: 293/300 lines - make the flagged structural cut (fold excluded-hit table
into ASM-1 evidence) BEFORE adding repair text.
Positives settled: registers reproduce; 8/8 anchors unique; VO-3 vector correct;
interruption clause mirrors pin; W-8/W-9 hold; LS5 return-item route fits the charter;
table insertions parse (D032 3 cells correct); VO-6 clean.
Round 3 = full mandate + L6 attack (both) - QUALIFYING CANDIDATE. Rounds 2 of 10.

## Round-3 findings (merged, 14 distinct; QS3-1=QC3-2 same clause) - binding for round 4

All four P1s were introduced by round-3's own repairs. Registers byte-exact; 9/9 anchors
unique incl. new SITE-4; VO-3 vector confirmed; VO-5 proven executable end to end and
order-independent; 12/12 quotes; excluded-hit dispositions all correct; no missing site
beyond the P1s below.
P1 x4:
1. Case-two cluster (QC3-2 + QS3-1): "must appear in a produced artifact" strips the
   license for REPLACED anchors - four of this body's own current texts (post-edit count
   0) become evidence transcripts under its own rule; INV-2's rescue clause never ships;
   the widened residual ("text from a pre-existing source") also catches ordinary source
   quotation, contradicting the Claims charter's quotes claim class. REPAIR: widen case
   two in the SHIPPED text (bytes that must appear in, or that an edit replaces in, a
   produced artifact; re-read exclusion kept) and license claim-cited quotation at
   sentence scale, bounded so transcripts cannot ride it. Both-readings mandatory.
2. QS3-2 block over-fires: no conjunct requires the body to be over a cap in force -
   a findings-stagnation restatement (size-independent per PROTOCOL:456-458) on a
   healthy under-cap goal satisfies "restatement has not brought the body under the
   cap" vacuously. REPAIR: block requires a result exceeding a cap in force.
3. QS3-3 block under-fires: "closed" defined only for refusal; a granted-then-still-
   oversize goal reaches no terminal and consumes no round; "unused path is not closed"
   lives only in body prose. REPAIR: ship the full path-state machine - open (unused:
   failed restatement leaves the proposal available, no block), pending, spent (grant
   recorded), closed (refusal); block fires when result exceeds cap in force AND
   restatement failed AND path refused or spent, any order.
4. QC3-1 SITE series renumbered mid-bracket: round-2 SITE-5 retired with NO recorded
   gap, identifier reused, two sites inserted mid-series, five identifiers silently
   re-pointed - violates the pinned retirement guard (PROTOCOL:429-437, merged in fix
   3). REPAIR: restore round-2 numbering for stable subjects (SITE-1..4, 6..8 as in
   round 2), record the SITE-5 gap with the successor clause on its successor, new
   subjects continue the series as SITE-9 (Claims handoff) and SITE-10 (sizing row,
   successor of SITE-5).
P2 x7: QS3-4 (VO-5 closure claim false for BND-2's single-line-row mandate - normalized
space erases wrapping; add a single-line check for the two inserted rows; correct the
claim); QS3-5+QC3-5 (VO-7 is a no-op - line anchor is not a paragraph anchor and grep -c
prints one line per file regardless of count; replace with a check that actually
distinguishes blank-line presence); QS3-6+QC3-6 (mixed replies: value+question / value+
condition explicitly not a grant, path stays open; partial value = grant for the named
caps, others unamended - ship both sentences); QS3-7 (register property says "text
contains" but grep is line-based - wrapped token in agents/DOCS_WRITER.md:50-51 is a
live missed member, BND-4-excluded by luck; property re-stated line-scoped and the wrap
blind spot disclosed in ASM-2); QS3-8 (counter-value grant contradicts the sizing gate's
counter-boundary rule with no stated distinction - ship the reason: a scalar counter is
determinate, a counter-boundary changes scope); QC3-3 (ASM-6 "no other site depends on
whitespace" false - AC-4 does); QC3-4 (matrix cites methods 6/7/10 as the three
exclusion sentences - the third is the self-check bullet, not method 7).
P3 x3: QS3-9 (task-metadata term absent from charters - pre-existing, noted); QS3-10
(Non-goals "lowering a cap" falsified by the counter-value path - reword honestly);
QS3-11 (BND-3/REQ-7 disclose backtick blindness of the normalized check).
STRUCTURAL: body is 299/300 lines and repairs add text. Cuts FIRST (path-walk fold ~6
lines, BND prose ~3); target under 295 before adding. Convergence: 33 -> 25 -> 14.
Round 4 = surgical; round-4 review is the next qualifying candidate. Rounds 3 of 10.

## Round-4 findings (merged, 10 distinct; FS4-1=FC4-1 graded P1 by consequence,
FS4-7=FC4-2) - binding for round 5

All four round-3 P1 repairs verified held (retirement guard SATISFIED; three-case rule
self-compliant; path-state machine ships with spent in the block clause; VO-7/VO-8
discriminate against forced negatives). Registers byte-exact; 9/9 anchors at true
locations; VO-3 vector exact; 31/31 quotes; simulated build passes VO-1..VO-8; no
orphaned citation after the 14-line cut; no repair thinned.
P1 x1 - FS4-1/FC4-1: "An absent, open, or refused proposal stops no round and blocks no
goal" vs the block clause whose third conjunct IS the refusal-closed path; same paragraph
defines refused as the closure event. Literal reading leaves a refused+oversize+failed-
restatement goal with NO terminal (oversized result enters no review, no round consumed,
round cap never bites). Aggravating: nothing obliges a proposal, so the never-proposed
path has the same no-pressure gap (PROTOCOL:854 catch-all is the only backstop). REPAIR:
scope the disclaimer to the proposal itself ("A proposal by itself stops no round and
blocks no goal") or drop refused from the list; reconcile W-3; state the open-path exits
honestly (restatement, proposal, and the protocol catch-all).
P2 x5: FS4-2 (case two has no minimality bound and the matrix claims it does - a
200-line anchor with a one-word edit reproduces the v060 dump legally; ship an
anchor-minimality clause - an anchor no longer than uniqueness and the edit require - or
correct the matrix claim and route quantity to reviewer judgment via ASM-5); FS4-3 ("the
gate closes in the owner's own reply turn" - undefined term colliding with the sizing
gate, assertive reading breaks the machine; use path vocabulary with the restrictive
operator: the path closes or is spent only on the owner's own reply turn); FS4-4 (missed
site: PROTOCOL:209-219 sizing-entry enumeration is a closed and-terminated 14-field list
mirroring the template 1:1 - SITE-10 adds a 15th template field; add SITE-11 amending the
enumeration; disclose the register-class gap - no register covers where task-record
fields are enumerated); FS4-5 (AC-5 not executable: SITE-6's mandated bytes omit case
one's and case three's bounds while AC-5's red path fails on a dropped bound - soften
AC-5 to names-each-case-and-points-to-the-protocol-rule, the subordination SITE-6 already
carries); FS4-7/FC4-2 (case two shipped in two non-identical formulations - one wording
verbatim at all three sites; AC-1 red path updated).
P3 x8: FC4-3/FS4-9 (VO-6 names its tree; "last three commands" count wrong); FC4-4 (VO-7
claim wording - prints 1 shows one blank-line-preceded occurrence, duplication closed by
VO-3 instead - say so); FC4-5 (ASM-6 adds the two list-indent facts at SITE-2/SITE-6);
FC4-6 (vocabulary: "a licensed register result" - keep, noted); FS4-6 (matrix "case one
bounded by the digest rule" is unconditional but the bound engages only for file-region
members - qualify; commits/refs residual disclosed); FS4-8 (successor clause satisfied
under reading A - record the reading or add a note label to the SITE-10 block); ASM-2
count claim (says two token-free anchors, five exist: SITE-3/7/8/9/10 - recount; the
completeness conclusion is unaffected); vocabulary drift removes-vs-replaces folded into
FS4-7 repair.
LINE BUDGET: 297/300 with a new site to add. If the repair set cannot land under 300,
perform the compact complete restatement (the body's own named remedy) - re-plan the
layout, keep every binding clause, same rule content, and record it as the restatement
the protocol names, not a silent rewrite.
Convergence: 33 -> 25 -> 14 -> 10. Round 5 = surgical (or restatement); round-5 review
is the next qualifying candidate. Rounds 4 of 10.

## ACCEPTED CLOSE - round 5 (2026-08-30)

Convergence exit satisfied: lens coverage complete since round 2; qualifying round with
ZERO new P0/P1 in both packets; no open P0/P1 (FS4-1 repaired - the block clause fires
on every ordering of refused/oversize/failed-restatement and the disclaimer no longer
neuters it under either reading; verified by both packets); no blocked verdict; no later
Writer result. The compact complete restatement preserved every binding clause (verified
by full-series sampling and the eighteen AC-3 clause families). Both packets: hash MATCH,
registers byte-exact, 10/10 anchors unique at claimed locations, VO-3 vector exact, all
eight VOs executable and discriminating on a simulated build (forced negatives fail
correctly), retirement guard satisfied (SITE-5 gap + successor clause survive), body
self-compliant under its own three-case rule, 38/38 quotes with one P3 imprecision.
Residue accepted under the owner's standing full-control directive (2026-08-29); strict
convergence knob: off (default). Residue (merged, ~10 distinct):
P2 x2 - GS5-1 (anchor-minimality bound has two readings: objective reading makes four
of the body's own anchors over-long, site-unit reading per GC5-3 makes all ten comply
but weakens the 200-line-anchor closure to ASM-5 reviewer judgment; the shipped protocol
text is unaffected - the fork lives in how a reviewer applies the bound); GS5-2 (matrix
row's commits-or-refs-fall-to-the-residual reading contradicts the correct shipped rule;
explanatory row only, no artifact defect).
P3 x8 - GS5-3 (both-readings preamble overstates coverage); GS5-4 (proposal's ledger-
state field has no referent before the first frozen round - exits list over-broad in one
state, catch-all covers); GS5-5 (spend moment: recorded-vs-owner-turn charitable reading;
recovery unconditional); GS5-6 (grant scope axis unstated for unproposed caps); GS5-7
(block conjunct's no-restatement-attempted reading; both readings terminate safely);
GS5-8/GC5-2 (SITE-11 circular trigger - enumerative only, duty lives in SITE-3); GC5-1
(ASM-6 SITE-2 indent figure 3 vs measured 5); GC5-4 (ASM-1 audit-aid list misses two
live hits inside anchored units - file-level claim holds).
Convergence trace: 33 -> 25 -> 14 -> 10 -> 0 new P0/P1. Rounds 5 of 10. Specification
frozen as LEANBODY-p5 ccbd99fc...a444. Next: Builder.

## BUILD AND BUILD REVIEW (2026-08-30)

Build: commit 4e53bad2c85906be5c564b9615f5cafa0203d434 on claude/spec-lean-body, base
d424422, four files, 89 insertions 14 deletions, ten hunks mapping 1:1 to the ten sites.
Builder reported zero deviations.
Build review (fresh reviewer, rule-coverage): PASS WITH RESIDUE. 10/10 sites landed
character-for-character including backtick placement (zero-deviation claim verified by
sampling); REQ-1..7 implemented; AC-1..10 all pass; VO-1..VO-8 all re-run and pass
(VO-5 normalized equality EQUAL on all four files); item 23's round-10 sentence
byte-unchanged; SITE-11 punctuation intact; freeze check clean (no hunk outside sites;
re-wrap BND-1-invisible). Residue: LBR-1, LBR-2 - two P3 cosmetic wrapping observations,
no repair required. Accepted under the standing directive.
