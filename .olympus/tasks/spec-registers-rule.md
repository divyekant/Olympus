---
status: active
---

# Olympus task: `spec-registers-rule`

## Goal and scope

Fix goal 3 of 5 (issue #14). Deliverable: the registers rule for specification bodies —
populations defined by property, never bare enumeration; any true enumeration is a marked
register carrying its exact regeneration command, which the Spec Writer re-runs each round
together with the ID audit. Plus the owner-accepted residue from the spec-review-lenses
goal (same `references/PROTOCOL.md` section 4 region): SS-1..SS-4 (P2), SS-5..SS-9 (P3),
RL-1, RL-2 (the three falsified doc sentences and the C16 fixture gap - a docs-sync
change set inside this goal), all itemized on issue #14.

- Governing revision (dogfood exception): pinned v0.5.0
  `ae000769b7a66247d8e7425535362c5d9a48aee7`, clean checkout at
  `/private/tmp/claude-501/-Users-dk-projects-Olympus/b8bad8e1-f4ce-4413-86a9-12b9ef35fa24/scratchpad/framework-cache-4/Olympus`.
  Claims about the sizing-gate and lens/exit text refer to the MUTATION BASE.
- Mutation base: `main` at `e79baf4` (sizing gate + lens catalog + convergence exit merged).
- Isolation: worktree `/private/tmp/olympus-fix3-registers`, branch `claude/spec-registers-rule`.
- Orchestrator: Fable. All role sessions: fresh Opus; Spec Writer persistent per goal.

## Sizing check (merged-gate practice)

| Field | Value |
| --- | --- |
| deliverables | 3 (registers rule; SS/RL protocol+template residue repairs; RL-2 docs-sync) |
| basis | entry 1: registers rule (PROTOCOL section 4 + SPEC_WRITER touchpoint check), 8,000 bytes, 6 criteria; entry 2: SS/RL residue repairs in PROTOCOL/TASK, 4,000 bytes, 4 criteria; entry 3: docs-sync (WHITEPAPER:279, CONFORMANCE:161 + C16 fixture note, DECISIONS D010), 2,500 bytes, 2 criteria; overhead 4,000 bytes, 1 criterion |
| projected-bytes | 36,800 (re-recorded at round 4 - the digest reduction reclaimed 11KB from RG-4's verbatim rows while strengthening the reduction rule; covered by the recorded proceed-unsplit) |
| projected-criteria | 13 - EXCEEDS 12 |
| threshold results | deliverable test FAIL (3); byte test pass; criteria test FAIL |
| decision | proceed-unsplit |
| owner decision reference | Standing owner directive (2026-08-30, full-control; memory 71487) plus the recorded acceptance decisions folding the SS/RL residue into this goal (spec-review-lenses owner decision row 5; issue #14 comments). The residue and docs-sync land in the same section-4 region and the same review bracket; splitting would re-serialize three trivial change sets across three brackets for no isolation gain. Flagged here per the gate's rule; the owner may override. |

## Owner decisions

| # | Decision |
| --- | --- |
| 1 | Standing practices (fix goals 1-2): lean body; registers with re-run commands; ID audit; both-readings + interaction matrix + path walks; lens schedule per the MERGED catalog (this bracket runs the shipped six-lens rules as practice against the pin governor); writer persistent, reviewers fresh; rule pressure = owner gate. |
| 2 | Exit: the merged convergence exit applied as practice - coverage complete + qualifying round (zero new P0/P1, no open P0/P1, no blocked verdict, no later Writer result) + residue acceptance under the standing full-control directive (the Orchestrator accepts P2/P3 residue on the owner's behalf per memory 71487, recording each acceptance explicitly). Cap 10. |
| 3 | Docs-sync (RL-2) is in scope as change set 3 - the allowed path set for THIS goal includes docs/WHITEPAPER.md, docs/CONFORMANCE.md, docs/DECISIONS.md for the named sentences only. |
| 4 | VERSION bump and release excluded (issue #23). |
| 5 | Boundary decision (Orchestrator under the standing full-control directive, 2026-08-30): the edit set widens to FIVE files - templates/TASK.md joins (SREG-3: S1's carve-in otherwise falsifies the template's proposal-reference field; SREG-9's defect-kind collision resolves in the same edit). Recorded as owner-pre-approved per memory 71487. |

## Specification rounds

### Current specification body

| Field | Value |
| --- | --- |
| status | complete |
| packet identifier | REGISTERS-p6 |
| goal identifier | spec-registers-rule |
| source commit | ae000769b7a66247d8e7425535362c5d9a48aee7 (pin); mutation base e79baf4 |
| content hash | 9ee344954bdfda39f04a9e449905fad2260bccc2700db67b138704aeba6064b7 |

<!-- SPECIFICATION-BODY:BEGIN -->

# Problem

`references/PROTOCOL.md` section `## 4. Goal flow` fixes what a specification body must
define, but not how the body may state a population. The body-content rules require requirements,
invariants, acceptance criteria, red paths, and validation obligations, and cap the body at 300
lines and 48,000 bytes. No rule says whether a list in the body is complete, how a reader
regenerates it, or who owns a list that stops matching the repository. A bare list is therefore a
completeness claim that decays without a signal: the repository moves, the list stays, and the next
reviewer reads a stale claim as a fact.

The merged section 4 text carries six accepted residue defects: an unconditioned exception in the
proposal-reference rule together with an untouched re-send sentence, an unhandled key case in the
re-persist rule, a missing red path for a repeat append, an append rule that counts only two append
kinds, a lost narrowing prohibition in the lens scheduling sentence, and an ambiguous referent in
the unchanged-body sentence. Three tracked documentation sentences still state the pre-merge cap
rule.

Owner-supplied history, unverifiable in both sources, recorded under AS4: every bare enumeration in
two prior brackets diverged from the repository within one to two rounds, no rule-based population
did, and 7 of 10 and then 4 of 7 Claims packets returned zero findings after each enumeration
carried a re-runnable command.

# Requirements

An identifier reference carries the full weight of the clause it names. A reference is not a summary.

| ID | Requirement |
| --- | --- |
| R1 | Section 4 states that a specification body defines a population by a stated property. A bare list is not a population definition. |
| R2 | Section 4 states that a list of a population, meaning a list whose members are the whole of some population defined by a stated property under R1 and which the body relies on as complete, is a marked population register. A population register records the exact command that regenerates it, the recorded revision that command names, the location the command runs from, and that command's output, either verbatim or as a stated mechanical reduction that changes whenever the population changes. A digest of that output is the canonical such reduction, because any byte change anywhere in the population changes it. The recorded result carries output only: no interpretation, no conclusion, no claim about what the output means. The command filters on the stated property and names the recorded revision, so a re-run returns the same output after later edits. It runs as written under a stated neutral environment: the Git configuration `git --no-pager -c color.ui=false`, which each command carries, and the locale `LC_ALL=C`, which the runner sets so that a locale-sensitive filter sorts, collates, and matches the same way for every reader: one read-only Git read of the recorded revision, optionally piped to one text filter over that output, meaning a single `awk`, `sed`, `grep`, `tr`, `sort`, or `uniq` transform reading only that output, optionally followed by one final `shasum -a 256` digest stage. The digest stage adds no filtering: it digests exactly what the stage before it emitted. It starts no other program, changes no repository or environment state, makes no network request, and writes or removes no file. Default behavior of the Git read, its pager included, is not a defect. A list the body marks as examples is not a population register and licenses no universal or absence claim. |
| R3 | Section 4 states that Spec Writer re-runs every population register command at its recorded revision and runs an identifier audit before each return, and reports both under the return item the charter already requires for the complete Evidence register and traceability map. The report carries each command's observed output for that round, and the Orchestrator is its only recipient. The audit's subject is the body's own identifier series. It checks that every citation of a body-series identifier resolves to a definition in the body, and that each new identifier continues its series; an identifier belonging to a source document, such as a conformance, decision, or lens identifier, is out of range and is neither checked nor defined. A retired identifier leaves a recorded gap in its series, and a recorded gap is not a defect. An identifier an open frozen ledger row cites is retired only when the body records its successor, or when the retirement is the repair an open row requires and the body records the gap. A successor, where one exists, is recorded in the successor identifier's own clause. A body with no population register reports an explicit empty register set. The duty runs on every return, including a return that carries no repair. |
| R4 | Section 4 states that a population register whose re-run at its recorded revision differs from its recorded result is a defect in the specification body, not in the repository. The repair is the body, and the Orchestrator does not convert the divergence into a repository finding. Whether the population is still complete in the current tree is a separate question, closed by the validation obligations before acceptance, not by this check. |
| R5 | Section 4 states the charter boundary in the charter's own terms. The Spec Writer preflight duty to enumerate the full population for a universal or absence claim is satisfied, inside the body, by a population register. The charter's three exclusion sentences keep the Evidence register, findings, hashes, round records, reviewer text, and review state outside the body. A population register holds none of these: it records a command, its revision, its location, and that command's output, maps no claim to a fact, and licenses no fact. The `Assumptions` section stays body content, because the charter's stable body order requires it. |
| R6 | Section 4 restates the six sites S1, S2, S4, S5, S6, and S7 in the site table below, and inserts the new S3 text, which is four sentences. Each restatement keeps every other clause of its sentence unchanged, and the insertion changes no neighboring sentence. R1 to R5 enter one paragraph group of section 4: the body-content group that begins `The current specification body is the only specification text in the task record.` and ends `An oversized Writer result is incomplete and does not enter review.` In R6, R7, and R11 a quotation of framework text drops the source's inline code marks, which the amended file keeps on the same terms as the source. |
| R7 | The three sentences of register `RG-1` state the merged cap rule in place, each keeping its own section voice and subject. `docs/WHITEPAPER.md`, from `Open findings at a cap produce blocked, not another automatic loop.` to `Any open P0, P1, or P2 at a cap produces blocked, not another automatic loop. An open P3 does not block.` `docs/CONFORMANCE.md` C04, from `Open findings at the configured cap stop as blocked.` to `Any open P0, P1, or P2 at the configured cap stops as blocked. An open P3 does not block.` `docs/DECISIONS.md` D010, from `open findings at the cap stop the goal` to `any open P0, P1, or P2 at the cap stops the goal, and an open P3 does not block`. |
| R8 | `docs/CONFORMANCE.md` C17 records, in that section's own voice, that across C17, C18, and C19 no fixture row exercises the review-lens catalog, the lens schedule row, lens coverage, or the pre-cap accepted close, and links each named referent to `../references/PROTOCOL.md#4-goal-flow`, the section that states all four. The record is an evidence limit; it gates and waives nothing. Register `RG-4` is the row population the absence claim ranges over. |
| R9 | The change edits exactly five files: `references/PROTOCOL.md`, `templates/TASK.md`, and the three files of register `RG-1`. It edits no role charter and no other path, and adds no role, packet edge, authority, or owner gate. |
| R10 | No identifier this body defines appears in an amended file. |
| R11 | `templates/TASK.md` carries the three sites of the template table below, each phrased inside the structure the template already has, and its `Handoff defects` prose gains one sentence: one attempt counter serves each round, every append after that round's first append takes the next number from it, and a corrected re-persist also records the handoff-defect reference that caused it. |

| Site | Current text | Restated as, or inserted |
| --- | --- | --- |
| S1 | Two sentences of the sizing-gate paragraph. First: `then re-send the proposal once and reuse the proposal reference already appended when one exists.` Second: `or while the entry closed cancelled-with-goal before any permitted send.` | First: `then re-send the proposal once while the gate is still open, and reuse the proposal reference already appended when one exists.` Second: `or while a halted outcome was recorded for that entry and the entry then closed before any permitted send, a permitted send being a send that appended a proposal reference.` |
| S2 | A corrected re-persisted packet appends under the same round and its new packet key. | A corrected re-persisted packet appends under the same round and its new packet key. When the correction leaves the body unchanged, the key's hash component is unchanged; an append whose whole key is then unchanged keeps that key and is discriminated by the attempt number, exactly as the retry is. |
| S3 | (inserted after S2) | One attempt counter serves each round. The round's first append records no attempt number, the round's second append records attempt number 1, and each later append in that round records the next integer. That attempt number is the append's handoff-defect reference. A handoff-defect row references the corrective append that follows it, by that append's attempt number, and records none when no corrective append exists. An append after a round's first append with no recorded attempt number is itself a handoff defect. |
| S4 | and assign at most two lenses to one reviewer in a round. | and assign at most two lenses to one reviewer in a round. Scheduling never narrows or replaces a lens; it defers an unassigned lens to a later round, bounded by the round-3 assignment rule and the coverage-completion rule below. |
| S5 | and over such a ledger it also satisfies the compactness rule above | and over either such ledger it also satisfies the compactness rule above |
| S6 | Either append holds the same lens set and the same owning reviewers and retains the superseded row | A retry append and a corrected re-persisted append each hold the same lens set and the same owning reviewers and retain the superseded row |
| S7 | The permitted automatic retry over the same packet re-appends under the same round and packet key, discriminated by the attempt number already recorded in the handoff-defect table. | The permitted automatic retry over the same packet re-appends under the same round and packet key, discriminated by the attempt number that round's counter records in the handoff-defect table. |

| Template site | Current text | Restated as |
| --- | --- | --- |
| T1 | none only while that turn was interrupted before the reference was appended and no permitted send has appended it, or while the entry closed cancelled-with-goal before any permitted send; none on an all-pass entry | none only while that turn was interrupted before the reference was appended and no permitted send has appended it, or while a halted outcome was recorded for that entry and the entry then closed before any permitted send, a permitted send being a send that appended a proposal reference; none on an all-pass entry |
| T2 | <handoff-defect attempt number> | <attempt number from the one counter for this round, which is that append's handoff-defect reference; none only on the round's first append> |
| T3 | The `Attempt` cell of the `Handoff defects` table: <n> | <attempt number of the corrective append for this round; none when no corrective append exists> |

Population registers of this body. Each command is one read-only Git read of the mutation-base commit
under the neutral configuration R2 states, optionally piped to one text filter over that output and
optionally ending in one digest stage. Run each command from the repository root of a mutation-base
checkout, as written; add no option and change no character. `RG-1` and `RG-3` read
whitespace-normalized sentences: the filter drops the constant `<commit>:` prefix when the Git read
carries one, groups the rest by path in first-seen order, joins each path's text with single spaces,
collapses blank runs, splits on `. `, and prints `<path>: <sentence>.` for each matching sentence. The
recorded result is therefore byte-comparable, because the revision-bound form and the worktree form
are printed identically. `RG-2` reads lines and strips that same prefix in its own filter slot, so
its recorded result is verbatim command output. `RG-4` reads rows and records its digest line, which fixes the identity of every
byte in the population.

`RG-1` — whitespace-normalized sentences under `docs` that carry the cap-clause phrase family `at a
cap`, `at the cap`, or `at the configured cap`, or the P3 clause `open P3 does not block`. Command:
`git --no-pager -c color.ui=false grep -n -e '' e79baf4ec781304c492d17f3e353404a9b0b6c20 -- docs | awk '{if(substr($0,41,1)==":"&&substr($0,1,40)~/^[0-9a-f]+$/)$0=substr($0,42);i=index($0,":");p=substr($0,1,i-1);r=substr($0,i+1);k=index(r,":");if(!(p in t))o[++c]=p;t[p]=t[p] substr(r,k+1) " "}END{for(n=1;n<=c;n++){x=t[o[n]];gsub(/[ \t]+/," ",x);m=split(x,a,"\\. ");for(q=1;q<=m;q++)if(a[q]~/at (a|the|the configured) cap|open P3 does not block/)print o[n]": "a[q]"."}}'`

```
docs/CONFORMANCE.md: Open findings at the configured cap stop as `blocked`.
docs/DECISIONS.md: The cap is one to three rounds, default two; open findings at the cap stop the goal.
docs/WHITEPAPER.md: Open findings at a cap produce `blocked`, not another automatic loop.
```

`RG-2` — lines of `references/PROTOCOL.md` that carry the six lens and convergence rule anchors.
Command:
`git --no-pager -c color.ui=false grep -n -e "schedule this round's review lenses" -e 'Coverage is complete when every catalog' -e 'A lens disposition names its lens' -e 'row holds the assigned lenses' -e 'closes as accepted before its cap' -e 'is a re-grade' e79baf4ec781304c492d17f3e353404a9b0b6c20 -- references/PROTOCOL.md | sed 's/^e79baf4ec781304c492d17f3e353404a9b0b6c20://'`

```
references/PROTOCOL.md:310:   - before reviewer dispatch, schedule this round's review lenses from the fixed catalog
references/PROTOCOL.md:429:row holds the assigned lenses, their owning reviewers, and, once returns arrive, each
references/PROTOCOL.md:437:A lens disposition names its lens and gives either the findings the lens produced, by that
references/PROTOCOL.md:445:no preceding consumed round does not satisfy this. Coverage is complete when every catalog
references/PROTOCOL.md:457:The specification bracket closes as accepted before its cap when, and only when, all three
references/PROTOCOL.md:475:to an existing row is a re-grade and keeps that `First seen`, but only while the row's
```

`RG-3` — the same sentence property as `RG-1`, over the whole repository. Command:
`git --no-pager -c color.ui=false grep -n -e '' e79baf4ec781304c492d17f3e353404a9b0b6c20 | awk '{if(substr($0,41,1)==":"&&substr($0,1,40)~/^[0-9a-f]+$/)$0=substr($0,42);i=index($0,":");p=substr($0,1,i-1);r=substr($0,i+1);k=index(r,":");if(!(p in t))o[++c]=p;t[p]=t[p] substr(r,k+1) " "}END{for(n=1;n<=c;n++){x=t[o[n]];gsub(/[ \t]+/," ",x);m=split(x,a,"\\. ");for(q=1;q<=m;q++)if(a[q]~/at (a|the|the configured) cap|open P3 does not block/)print o[n]": "a[q]"."}}'`
Result: the three sentences recorded for `RG-1`, in that order, then:

```
references/PROTOCOL.md: At the cap the cap rule above governs unchanged: a frozen ledger holding no open P0, P1, or P2 at the cap is accepted, with any open P3 recorded to the owner.
```

`RG-4` — the data rows of every table of `docs/CONFORMANCE.md` whose header names `Observable pass
evidence`.
Command:
`git --no-pager -c color.ui=false show e79baf4ec781304c492d17f3e353404a9b0b6c20:docs/CONFORMANCE.md | awk '/Observable pass evidence/{t=1;next} /^\| --- /{next} !/^\|/{t=0} t' | shasum -a 256`

```
f1570a2e08cdebd23433c95dddc5a3499759b46c49f17befd63545e3cb27824c  -
```

# Approach

| Option | Cost | Result |
| --- | --- | --- |
| State the rule in the Spec Writer charter | The charter is a role duty surface; a reviewer reads the body against the protocol contract | Rejected |
| Separate the new artifact from the charter's registers by name alone | The charter's population duty sits inside its Evidence-register item, so a rename settles nothing | Rejected |
| Separate it by relation, in charter terms, under R5 | One sentence, testable by A4, and no charter edit | Accepted |
| Record register results against the working tree | Every unrelated edit moves a line number and forces a re-record | Rejected |
| Record results against a named revision, and check current-tree completeness in the obligations | A re-run is deterministic, and the two questions stay separate | Accepted |
| State the rule in the section 4 body-content rules, beside the size and content caps | One paragraph group, already read as the body contract | Accepted |
| Add a conformance fixture for the lens and exit machinery | New fixture design, outside this goal's owner boundary | Rejected; recorded under R8 |

Reading of the recorded results, kept out of the register text under R2. `RG-2` returns one line for
each of the six lens and convergence rules, so the completeness safeguard a reviewer might demand
for section 4 is already present, and the goal adds no criterion analog for it.
`RG-3` returns one sentence beyond `RG-1`, and that sentence already names P0, P1, and P2, so
`RG-1` is the complete population of stale documentation sentences. `RG-4` fixes a population of 39 rows by digest, drawn from the four tables
that carry the `Observable pass evidence` header, which are the tables of C17, C18, and C19; C14 is a
fifth fixture table in the same file and carries a different header, so the property excludes it. The
VO3 run of that command emits rows of which none names a lens, lens coverage, or the accepted close,
which is the evidence behind R8.

# Invariants

| ID | Invariant |
| --- | --- |
| I1 | A list of a population is either a population register with a command, a revision, a location, and a result, or a marked example set that claims no completeness, and for a list of a population no third state exists. A list that states no population, such as this body's own requirement, invariant, boundary, criterion, and obligation tables, is neither, and R1, R2, and B1 do not reach it. |
| I2 | A recorded register result is regenerable from its recorded command at its recorded revision, by any reader with read access to that revision, without side effect on the source. |
| I3 | A population register divergence at the recorded revision is repaired in the body and nowhere else. Completeness in the current tree is a separate question, closed by the validation obligations before acceptance. |
| I4 | A population register maps no claim to a fact and licenses no fact, and its recorded result carries output only. The Evidence register, review state, findings, hashes, round records, and reviewer text stay outside the body under the charter's three exclusion sentences. The `Assumptions` section is body content the charter's stable body order requires. |
| I5 | Every restatement in R6, R7, and R11 changes meaning only where its site names, and leaves every other clause of its sentence unchanged. R6 holds six restatements and the S3 insertion, and the insertion changes no neighboring sentence. |
| I6 | No amended file gains a role, a packet edge, an authority, an owner gate, or an identifier this body defines. |
| I7 | A retired identifier's recorded gap changes the body only. A frozen ledger row is Orchestrator-owned and evidence-matched, so no body edit removes it. |
| I8 | The re-run and audit report rides the charter's existing Evidence register and traceability map return item. Its only recipient is the Orchestrator, and no reviewer receives it. |

# Assumptions

| ID | Assumption | State | Evidence |
| --- | --- | --- | --- |
| AS1 | The Spec Writer charter needs no edit: R5 separates the artifacts by relation in the charter's own terms, and R3's report rides the charter's existing return item for the complete Evidence register and traceability map. Load-bearing: it carries the zero-charter-edit boundary | supported | `agents/SPEC_WRITER.md` is byte-identical in both sources. Method 4 and Method 7 place the assumption register in the body. The three exclusion sentences are Method 6, Method 10, and the self-check line naming `Evidence register or review state`. The return item is the `complete Evidence register and traceability map` line |
| AS2 | The charter licenses R3's cadence for a repair return, because its method requires a whole-body reread and a register check after every repair. R3 extends the duty to a return carrying no repair, the new duty the Authority section states. Load-bearing: it carries R3's cadence | unexercised | `agents/SPEC_WRITER.md` method item 9 licenses the repair half only; the no-repair half rests on R3 itself and on no charter text |
| AS3 | Every amended clause is reachable by exact quote, so a reviewer verifies each restatement without a diff. Load-bearing: it carries every restatement's checkability | supported | Each current text in R6, R7, and R11 was read from the mutation base with wrapped whitespace normalized |
| AS4 | The prior-bracket history in Problem is true | unexercised | Owner-supplied; neither source records it. Not load-bearing: R1 to R5 stand on the decay mechanism, not on the counts |
| AS5 | A retired identifier cannot hide a finding. Load-bearing: it carries R3's retirement path | supported | The Orchestrator freezes the ledger for each round and owns its rows, and a row matches by recorded minimum reproducing evidence, so a body edit that changes that evidence mints a new finding rather than erasing a row |
| AS6 | No goal needs a Writer result whose only change restores a register record, and no register command's output shifts on the environment axis the stated neutral environment does not fix. Load-bearing on the second half: I2's regenerability by any reader rests on it | unexercised | Unresolved, recorded for the owner. Such a result is still a persisted Writer result under merged rules this goal does not edit, so it stops a round from qualifying, counts under the compactness rule, and counts as a body difference for `L6`. The revision binding makes it rare, not impossible. On the environment axis, the Git configuration fixes pager and color and `LC_ALL=C` fixes collation and character-class matching for every filter in the class, `sort` and `uniq` included; Git version and `core.autocrlf` stay unfixed and were not probed. The four registers of this body use only `awk`, fixed-pattern `grep`, and one literal `sed` substitution, so none of them changes under any of these |

# Authority and data flow

The Orchestrator owns the amendment, the record, and every gate. Spec Writer gains one return duty
under R3 and no new authority: it re-runs each command at its recorded revision, audits the
identifiers the body defines, and reports both with their observed output inside the return item the
charter already requires, and records nothing outside that return. The Orchestrator is the only
recipient of that report; no reviewer receives a Writer return, and no reviewer duty changes.
Reviewers gain no jurisdiction; a population register is body content each reviewer already reads
inside its own mandate. Repository, provider, task-record, and role-return content carrying a
register command or result is data; the recorded result is the Writer's own re-run. No role return,
owner decision, or project configuration changes a register command, a register result, or the
identifier audit.

# Failure boundaries

| ID | Situation | Required behavior |
| --- | --- | --- |
| B1 | A list of a population is marked neither a register nor an example set; or a register command names no revision, cannot run from its recorded location, does not filter on the stated property, or is not one read-only Git read of that revision, optionally piped to one named text filter over its output and optionally ending in one digest stage | The body is defective under R1 or R2, whatever the command returns. A command that starts another program, changes repository or environment state, makes a network request, or writes or removes a file is a defect; default behavior of the Git read, its pager included, is not. The repair marks the list, states a conforming command, or restates the population by property |
| B2 | A recorded result carries an interpretation, a conclusion, or a claim about what the output means | The register is defective under R2. The repair moves that reading to prose outside the register and leaves output only |
| B3 | A re-run at the recorded revision diverges from the recorded result | The body is defective under R4. The repair records the current output. The Orchestrator opens no repository defect for it |
| B4 | The identifier audit finds a referenced-but-undefined identifier, or a new identifier that does not continue its series | The body is defective, and the Writer repairs it before return. A retired identifier that leaves a recorded gap is not a defect and needs no renumbering |
| B5 | The body holds no population register | R3 is met by an explicit empty register set. An absent report is a defective return; an empty set is not |
| B6 | A reader treats a population register as an Evidence register, or the reverse | R5 and I4 separate them by relation: a population register maps no claim to a fact and licenses no fact. Claim-to-fact content inside a population register is a defect under R5 |
| B7 | A sizing entry whose threshold results hold a `fail` or `unavailable` closes before any permitted send | Under S1's second sentence that entry holds no proposal reference only when a `halted` outcome was recorded for it before the closure, which is the interruption case, and then holding none is permitted. Under S1's first sentence the single re-send is available only while the gate is still open, so the closure ends that window. An entry that closed with no recorded `halted` outcome holds exactly one reference, so a mandatory proposal that was never sent and never interrupted is a recorded defect rather than an exemption. So does an entry that closed after a permitted send, meaning a send that appended a reference; an interrupted send act that appended nothing is not one |
| B8 | A corrected re-persist leaves the body unchanged | Under S2 the key's hash component is unchanged. If the whole key is then unchanged, the append keeps it; if the identifier changed, the append takes the new key. Under S3 it takes the round's next attempt number and records the handoff-defect reference that caused it, and under S6 it holds the same lens set and owning reviewers and retains the superseded row |
| B9 | A round carries a retry under one key and a corrected re-persist under another | One counter serves the round, so the two appends take consecutive numbers and stay distinguishable even where their keys collide. An append after the round's first with no recorded attempt number is itself a handoff defect: it consumes no round, stays recorded, and is corrected and re-persisted before a new dispatch |
| B10 | The Orchestrator leaves a catalog lens unassigned in a round | Under S4 that is deferral, not narrowing, and the round-3 assignment rule and the coverage-completion rule bound it. Any change to what a lens covers, or any substitution of one lens for another, is a defect |
| B11 | Coverage is incomplete and the frozen ledger holds no open finding at all | Under S5 the unchanged body satisfies the compactness rule over that ledger, as it does over a ledger holding only P3. Coverage still cannot complete while `L6` lacks two consumed rounds whose bodies differ, so the bracket ends at the cap |
| B12 | A body edit retires an identifier whose row is open in a frozen ledger | Under I7 and AS5 the row stands: the Orchestrator owns and freezes the ledger, a row matches by its recorded minimum reproducing evidence, and a retirement that changes that evidence mints a new finding instead of erasing the row. The recovery is to restore the cited identifier or record its successor under R3 |

# Acceptance criteria and red paths

A criterion that reads `Section 4 states Rn in full` is met only when section 4 carries every clause of
that requirement. The reference is not a summary, and a partial statement fails the criterion.

| ID | Criterion | Red path |
| --- | --- | --- |
| A1 | Section 4 states R1 and R2 in full | Any register part absent; a bare list allowed as a population definition; no recorded revision, or a result recorded against a moving tree; a result with no stated relation to its command; a reduction that can stay fixed while the population changes; interpretation allowed in a result; a bound stated as forbidden options rather than as one read-only Git read optionally piped to one named text filter and optionally ending in one digest stage; a digest stage that filters as well as digests; a command that starts another program, changes repository or environment state, makes a network request, or writes or removes a file; default Git-read behavior called a defect; an example set licensing a universal or absence claim |
| A2 | Section 4 states R3 in full | The re-run or audit stated as optional, conditional, or once per bracket; a re-run against the current tree instead of the recorded revision; either result unreported; observed output omitted; a new return item, recipient, or reviewer duty invented; the audit extended to source-document identifiers; the audit stated as contiguity, or renumbering required; a recorded gap called a defect; a cited identifier retired with no recorded successor and with no open row requiring that retirement; the duty limited to repair returns; no explicit empty set |
| A3 | Section 4 states R4 in full | The divergence assigned to the repository; the repair placed outside the body; the two questions merged, so a revision-bound register is read as evidence about the current tree; the rule silent on the defective artifact |
| A4 | Section 4 carries the R5 boundary sentence in full, in charter terms | The sentence absent; the boundary resting on a name rather than a relation; any claim that the assumption register belongs outside the body; fewer than three exclusion sentences, or review state omitted; claim-to-fact content in a register; a charter edit |
| A5 | S1's first sentence bounds the single re-send to a gate that is still open. S1's second sentence permits no proposal reference only for an entry that closed by any means before any permitted send and only after a `halted` outcome was recorded for that entry, defines a permitted send as one that appended a proposal reference, and otherwise requires exactly one. T1 carries that second clause in the same words, and neither adds a gate-open conjunct, because a closure of the entry is the closure of the gate under the section 4 sentence that lists the three closures | Either sentence left unrestated; a closure enumeration in place of any closure, so a closure kind outside the list leaves exactly-one unsatisfiable; the exemption granted without a recorded `halted` outcome, so an entry whose mandatory proposal was never sent and never interrupted holds no reference and the skip is untraceable; a case unconditioned on `before any permitted send`; `permitted send` left undefined, so an interrupted send act that appended nothing counts as one; a re-send permitted after the gate closes; T1 and S1 stating the clause in different words; the cardinality or all-pass rule changed |
| A6 | The S2 sentence derives the unchanged hash component from the unchanged body, states the whole-key case as a condition rather than an entailment, and gives the attempt number as the discriminator; the S6 sentence names the retry append and the corrected re-persisted append rather than counting them; and the S7 sentence draws the attempt number from that round's counter rather than presuming a record | The unchanged whole key asserted as a consequence of the unchanged body; identifier stability assumed without record; only the new-key case stated; discrimination by anything but the attempt number; S6 left with a referent that counts append kinds rather than naming the retry append and the corrected re-persisted append; S7 left reading `already recorded in the handoff-defect table`, which presumes the record it does not require |
| A7 | The S3 sentence gives one attempt counter per round, exempts the round's first append, starts the round's second append at attempt number 1 and each later append at the next integer, requires a corrected re-persist to record the handoff-defect reference that caused it, and makes a later append with no recorded attempt number a handoff defect | A counter keyed to anything but the round; the first append required to carry a number; a corrected re-persist exempted, or its originating reference omitted; two counters, or a counter serving one mechanism only; no red path for the missing record; the consequence stated as anything but a handoff defect |
| A8 | The S4 sentence says scheduling never narrows or replaces a lens, and defers an unassigned lens to a later round bounded by the round-3 assignment rule and the coverage-completion rule | The prohibition absent, or left only on external sources; deferral described as narrowing; either bound unnamed, or deferral left unbounded |
| A9 | The S5 sentence attaches the compactness result to both ledger cases | The referent still singular or ambiguous; the result attached to only one case |
| A10 | Each of the three `RG-1` sentences names P0, P1, and P2 as the blocking set at its cap and states that an open P3 does not block | Any of the three left unrestated; a restatement still reading `open findings`; a restatement that makes P3 block, or that changes its section's other claims |
| A11 | C17 records that across C17, C18, and C19 no fixture row exercises the lens catalog, the lens schedule row, lens coverage, or the pre-cap accepted close, links each referent to the protocol section that states all four, and reads as an evidence limit that gates and waives nothing; `RG-4` is the row population it ranges over, and the digest fixes that population's identity while the reviewer reads row content from the live command run VO3 mandates, not from the body | The record absent or left in C16; a scope narrower than the three sections; a referent unlinked; a fixture added; the record written as a gate, a waiver, or a deferral with a due condition; an absence claim with no register behind it |
| A12 | The change edits exactly the five files of R9; no charter or other path is edited; no role, packet edge, authority, or owner gate is added; no identifier this body defines appears in an amended file | Any sixth edited path, tracked or untracked; an edited charter; a new role, packet edge, widened authority, or new owner gate; any identifier this body defines present in an amended file |
| A13 | `templates/TASK.md` carries T1, T2, T3, and the one-counter sentence, each inside the template's existing structure and each matching the section 4 rule it records | Either site left unrestated; T1 stating the section 4 rule in other words; T2 or T3 keyed to anything other than the round; T3 with no none value, so a first-dispatch defect or an escalated or blocked disposition that produces no corrective append has no legal cell value; a template rule that states more or less than section 4; a new template table, column, or section |

# Validation obligations

Run every command from the repository root of the goal worktree. A command that names the
mutation-base commit reads that revision; a Git read that names no revision reads the worktree; and a
command that reads a file directly, with `cat`, reads the worktree copy of that file.

| ID | Obligation | Command |
| --- | --- | --- |
| VO1 | Read the amended text against A1 to A13. Run the unrestricted diff first for A12: it must return exactly the five paths of R9. Then run the porcelain status, which must name no untracked path, because an untracked sixth path does not appear in the diff. A path under `.olympus/tasks` is exempt from both reads, because the task record is the Orchestrator's own artifact and lives outside the goal worktree this change edits. Then read those five | `git diff --name-only e79baf4ec781304c492d17f3e353404a9b0b6c20` and `git status --porcelain` |
| VO2 | Regenerate `RG-1` and `RG-3` and compare each against its recorded result. Then run both again with the commit argument removed, so the Git read takes the worktree, and read every returned sentence against A10. For each of the three files the current-tree `RG-1` run must return exactly one sentence carrying the cap clause and exactly one carrying the P3 clause, and where a file states both clauses in one sentence that single sentence satisfies both. Before the edit each file therefore returns one sentence and no P3 sentence; after it `docs/CONFORMANCE.md` and `docs/WHITEPAPER.md` each return two and `docs/DECISIONS.md` returns one. Any other count is red for A10 | the `RG-1` and `RG-3` commands above, then each of them with `e79baf4ec781304c492d17f3e353404a9b0b6c20` removed |
| VO3 | Regenerate `RG-2` and `RG-4` and compare each against its recorded result. Then run `RG-2` again with the commit argument removed; it passes when the same six anchor lines return, and their line numbers are permitted to shift. Then run the `RG-4` filter alone over the worktree file, without the digest stage, so it emits rows, and read every emitted row against A11. That run must emit rows from every table whose header names `Observable pass evidence`; a table returning none is red for A11. The emitted rows carry no table marker, so map each row to its table by reading `docs/CONFORMANCE.md` beside the output | the `RG-2` and `RG-4` commands above, then `RG-2` with `e79baf4ec781304c492d17f3e353404a9b0b6c20` removed, and `cat docs/CONFORMANCE.md` piped to the `RG-4` filter |
| VO4 | Identifier containment for A12 and R10 over the five amended files. The pattern set covers only the series this body defines, because C, D, L, and P identifiers in those files are source identifiers this change does not introduce. It must return no hit | `git grep -nP -e '\bAS-?[0-9]+\b' -e '\bRG-[0-9]+\b' -e '\bVO[0-9]{1,2}\b' -e '\b[RIBAST][0-9]{1,2}\b' -- references/PROTOCOL.md templates/TASK.md docs/WHITEPAPER.md docs/CONFORMANCE.md docs/DECISIONS.md` |
| VO5 | Manual check on the first goal that runs an amended bracket: the Writer return holds a re-run result with observed output for every register and an identifier audit result, the Orchestrator is its only recipient, and any divergence was repaired in the body | none; manual |
| VO6 | Check internal link resolution after the edit, including the new C17 link | none; manual; no link checker is configured |

# Rollout/rollback

One local commit on a goal branch, over the five files of R9. The change is text only, and applies
to a goal that starts after it; an open bracket keeps the rules in force when its goal started.
Rollback is a revert of that commit. No record migration is needed: T1, T2, and T3 restate existing
template slots and add no field, and the one sentence R11 names is prose beside an existing table.

# Non-goals

Adding a conformance fixture for the lens or exit machinery. Editing a role charter. Changing the
round cap, the body-size caps, the restatement rule, the severity ladder, round accounting, or a
reviewer's jurisdiction. Changing what any reviewer receives. Adding a template table, column, or
section beyond T1, T2, and the one sentence R11 names. Adding a criterion analog for the
completeness subject `RG-2` covers. Repairing the criteria-count rule, whose row-and-item counting
the merged text already resolves. Repairing the previous bracket's specification-side form defects,
which did not ship. Verifying the Problem history.

# Provenance

Two sources, split by subject. Every claim about section 4's sizing gate, lens catalog, schedule
row, coverage, accepted close, re-grade rule, and finding-ledger row matching, every claim about the
three documentation sentences, C16, C17, C18, and C19, every claim about
`templates/TASK.md`, and every quoted current text in R6, R7, and R11 refers to the mutation
base, commit `e79baf4ec781304c492d17f3e353404a9b0b6c20`. Those ledger and re-grade sentences are
mutation-base text and are absent from the pin. Every other claim, including the body-content rules,
the severity ladder, and the Spec Writer charter, refers to the governing pin, Olympus v0.5.0,
commit `ae000769b7a66247d8e7425535362c5d9a48aee7`.
`agents/SPEC_WRITER.md` is byte-identical in both sources, so charter claims hold against
either. All quotes were verified with whitespace normalized. Probes ran on 2026-08-30. The Problem
history is owner-supplied and unverifiable, under AS4.

<!-- SPECIFICATION-BODY:END -->

### Specification review rounds

| Round | Packet identifier and hash | Claims verdict and finding count | Spec verdict and finding count | Open P0-P2 | Body lines | Body bytes | Lenses run | Aggregated state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REGISTERS-p1 7138f184...a01f | repair; 4 (1 P1, 2 P2, 1 P3) | repair; 18 (7 P1, 7 P2, 4 P3) | 17 | 216 | 19994 | L1 (Claims); L2 (Spec) | repair |
| 2 | REGISTERS-p2 a9ecf147...9e51 | repair; 4 (2 P1, 2 P2) | repair; 17 (7 P1, 8 P2, 2 P3) | 19 | 259 | 27373 | L5+L6 (Claims); L3+L4+L6 (Spec) - COVERAGE COMPLETE | repair - restatement for round 3 |
| 3 | REGISTERS-p3 3910438d...82a8 (compact restatement) | repair; 2 P2 | repair; 14 (6 P1, 5 P2, 3 P3) | 13 | 234 | 32311 | L6 attack primary (both) + full mandate | DOES NOT QUALIFY |
| 4 | REGISTERS-p4 e06d0c3f...b7eb (16 repairs + digest reduction) | repair; 1 P3 | repair; 11 (1 P1, 7 P2, 3 P3) | 8 | 246 | 36793 | L6 attack (both) + full mandate | DOES NOT QUALIFY - SRG4-1 P1 |
| 5 | REGISTERS-p5 9677c5dc...c58d (12 round-4 repairs incl. SRG4-1 any-closure fix) | 7 (4 P2, 3 P3) | 9 (2 P1, 3 P2, 4 P3) | 14 (2 P1, 5 P2, 7 P3) | 248 | 38540 | L6 attack (both) + full mandate - QUALIFYING CANDIDATE | DOES NOT QUALIFY - RS5-1, RS5-2 P1 |
| 6 | REGISTERS-p6 9ee34495...64b7 (12 round-5 repairs incl. halted-condition E2 rewrite) | 4 (1 P2, 3 P3) | 8 (3 P2, 5 P3) | 11 (3 P2, 8 P3) | 250 | 41563 | L6 attack (both) + full mandate - QUALIFYING CANDIDATE | QUALIFIES - accepted close |

### Finding ledger (Orchestrator-owned)

| ID | Jurisdiction | Severity | Finding | Closure condition | State | First seen | Last checked |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Evidence appendix (lean-body practice: transcripts live here)

Round-1 Writer probes: charter byte-identical across sources (zero charter edits safe);
the Method-6/10 "no registers in the body" collision resolved by content (population
register = command + location + result only, no probes/facts - R5/I4); every CS2 subject
verified against MERGED text - SS-2/SS-3/SS-5/RL-1/SS-6 confirmed live gaps, SS-1
ALREADY SATISFIED (register RG-2 proves all six section-4 rules shipped; dispositioned
in Non-goals with evidence), SS-8 already resolved by the merged counting rule, V1-form
nits spec-side only (dropped per goal boundary); three doc sentences byte-verified and
the stale population proven complete repo-wide (register RG-1); C16 gap recorded in
C16's own voice as an evidence limit that gates nothing. Self-test finding fixed during
drafting: a recorded command containing a pipe violates R2's own byte-runnable rule from
a table cell - all commands use repeated -e patterns. B-series renumbering slip caught
by the ID audit and fixed. Both registers re-run clean. Byte note: 19,994 of the 20,000
gate threshold - 6 bytes of margin; any addition crosses the projection (not the hard
cap; re-record the projection if it does).

Round-1 findings (merged, 22): KR-1 P1 (R5/I4/A4/B5 claim the charter keeps the ASSUMPTION
register outside the body - false: Method 7 mandates Assumptions IN the body; the body's own
AS table violates its own I4; strike the assumption-register halves, keep the
evidence-register halves). SREG-1 P1 (the Method-6/10 non-collision cannot rest on renaming
- Preflight 2's population enumeration lives INSIDE the Evidence-register item; state the
boundary in charter terms: the Preflight-2 population duty is satisfied in the body by the
population register; Methods 6/10 exclude probe-to-fact rows, which a population register
never holds; A4 tests it). SREG-2 P1 (R2 "recorded result" vs R5 "no observed output"
jointly unsatisfiable - exclude by RELATION: no claim-to-fact mapping, no fact licensed;
the register records a command, location, and that command's output). SREG-3 P1 (five-file
boundary - resolved by owner decision row 5). SREG-4 P1 (R2 needs the command-population
RELATION: the recorded result is the command's exact output or a stated reduction that
changes when the population changes, and the command filters on the stated property; fix
RG-1's command/population mismatch and record RG-2's actual lines). SREG-5 P1 (contiguity
forces renumbering which mints new findings via changed evidence; audit = no
referenced-but-undefined identifier + new identifiers continue the series + a retired
identifier leaves a RECORDED GAP which is not a defect; fix A2). SREG-6 P1 (bound register
commands: read-only, local to the recorded location, no network or write effects; B1 makes
any other command a body defect; A1 red path). SREG-7 P1 = KR-3 (the unchanged-key
entailment is underivable - the identifier is not body-bound; condition S2 on the HASH
component and drop the causal so-that; or record the identifier-stability assumption).
SREG-8 P2 (the untouched re-send sentence conflicts with both carve-ins - extend the S1
site: "re-send once while the gate is still open"). SREG-9 P2 (S3 scoped to appends
following a RECORDED handoff defect; ONE attempt counter per round+key covering both
mechanisms; the template edit from row 5 phrases the recording slot). SREG-10 P2 (R3's
return duty rides the charter's existing "expected evidence, skipped probes, and
uncertainty" item - state it; extend AS1 to the return surface). SREG-11 P2 (the C16 note
must link its referents or move to C17 where fixture coverage lives - move to C17).
SREG-12 P2 (R8's absence claim needs its own register - third register enumerating the
fixture population). SREG-13 P2 (register the unrestricted RG-1 variant or drop the
completeness conclusion - register it). SREG-14 P2 (R3's report carries the round's
OBSERVED OUTPUT so Claims/L5 can compare without new jurisdiction). KR-2 P2 (V4 regex
misses hyphen-less AS1..AS5 - \bAS-?[0-9]+\b). SREG-15..18 + KR-4 P3 (B10's L6 note;
V1-V4 run-location statement replacing <repo> placeholders; S4's cap-round referent and
named coverage rule; R6/I5 distinguish four restatements from one insertion; charter has
THREE exclusion sentences naming also review state). Open P0-P2: 17.

BUILD (2026-08-30): commit dea8e470386e7fc6a915c015cc809b9c111ed2b6 on
claude/spec-registers-rule, base e79baf4, five files, 98 insertions 21 deletions. All
sites landed with unique anchors; VO1-VO4, VO6 green (VO5 manual - no bracket has run
under the amended text yet); four registers byte-exact at base after edits. Builder
flagged six deviations (R1-R5 implemented per R6's placement group despite dispatch-brief
omission; "under R1" -> "as above" in R2's amended text per R10/VO4; meta-frame sentences
stripped; backtick conventions per source; five-sentence S3 cell implemented over R6's
stale count; convention re-wrapping). Fresh build review (rule-coverage method) judging
all six. Not pushed, not merged.

BUILD REVIEW (2026-08-30, fresh reviewer, rule-coverage method): PASS WITH RESIDUE.
16/16 sites landed exactly; R1-R11 all implemented; A1-A13 all pass; VO1-VO4, VO6 pass;
VO5 not exercisable by precondition (first amended-bracket goal has not run) and reported
honestly; four registers byte-exact at base; no hunk outside named sites and R6's
placement group. Deviation verdicts: D1 LICENSED (R6 is the placement rule; the dispatch
brief was wrong, not the Builder), D2 ACCEPTABLE-FORCED (R2-literal and R10/VO4 are
unsatisfiable together; "as above" is the minimal resolution -> BR-1), D3/D4/D5 LICENSED,
D6 ACCEPTABLE verified clean. Residue: BR-1 P3 (R2 contains body identifier "R1", which
R10 forbids in amended files - spec-internal conflict; future spec round phrases the
cross-reference identifier-free), BR-2 P3 (= RS6-1 stale four-sentence count), BR-3 P3
(A7 met by entailment). All residue spec-side, accepted under the standing directive.

ACCEPTED CLOSE - round 6 (2026-08-30). Convergence exit satisfied: lens coverage complete
since round 2; qualifying round with ZERO new P0/P1 in both packets; no open P0/P1 (both
round-5 P1 repairs re-attacked and held: E2 clause survives 13 orderings with no deadlock
and no silent skip - the never-sent/never-interrupted fail entry is now a recorded defect;
T3 gives every reachable defect row exactly one legal value); no blocked verdict; no later
Writer result. Both packets: hash MATCH, four registers byte-exact (LC_ALL=C invariance
verified under three locales), 27/27 quotes verbatim, ID audit clean, A5 gate-closure
entailment verified in the amended text, charter-interior check clean (population register
is a strict sub-structure of the Evidence register triple; Methods 6/10 not reached).
Residue accepted under the owner's standing full-control directive (2026-08-29); strict
convergence knob: off (default). Residue (merged, 11 distinct; RS6-1 = RC6-1):
P2 x3 - RS6-1/RC6-1 (R6 says the S3 text is four sentences; it is five - stale count from
the SRG5-1 repair; A7 independently binds all five behaviors, so no wrong text can ship);
RS6-2 (R3's audit sentence lacks the gap/successor carve-out its own retirement clause
needs; B4's second sentence provides the escape, so no path is globally blocked); RS6-3
(pre-existing S1/T1 first-exemption-clause divergence in the BASE text - protocol window
vs template appended-reference predicate diverge on ordering 13; not introduced by this
change; A13 literal red exposure noted for a future goal).
P3 x8 - RC6-2 (VO1/VO4 commands omit the neutral Git config R2 scopes to registers);
RC6-3 (RG-3 result partly by reference; byte-comparison passed); RC6-4 (S1/T1 current-text
cells are sentence fragments; all nine anchors unique in their files); RS6-4 (T3 forward
reference - cell transitions none->integer with no stated revisability rule); RS6-5 (R2
"It starts no other program" pronoun referent loose); RS6-6 (LC_ALL=C carried by no
recorded command - assigned to the runner; harmless for shipped registers); RS6-7 (R5
"three exclusion sentences" definite description; A4 red path is a floor not a ceiling);
RS6-8 (two RG-2 anchors sit in edited paragraphs; re-wrap exposure is a loud false red).
Convergence trace: 17 -> 19 -> 13 -> 8 -> 14 -> 0 new P0/P1. Rounds 6 of 10. Specification
frozen as REGISTERS-p6 9ee34495...64b7. Next: Builder.

Round-5 findings (merged, 14 distinct; RS5-1 subsumes RC5-3, RS5-2 subsumes RC5-2) -
binding for round 6 (surgical, hard freeze otherwise). Both packets: hash MATCH, all four
registers re-run byte-exact, 20/20 quotes verified, ID audit clean, SRG4-1 clause identical
in S1/T1, VO2 phased counts confirmed, VO4 green. Prescriptions:
SRG5-1 P1 (T3's Attempt cell has no legal value for a first-dispatch defect or an
escalated/blocked disposition - S3 states which append a handoff-defect row references:
the corrective append when one exists, none when no corrective append exists; T3 carries
the same none allowance in T2's pattern; A13 red path detects a missing none). SRG5-2 P1
(B7 sentence 3 contradicts shipped S1/E2 - ordering: fail recorded, no send, no
interruption, owner closes; S1/A5 permit zero references, B7 demands one, silent-skip
untraceable. Repair as ONE coherent clause set identical in S1 and T1: E2 gains the
condition that a halted outcome was recorded before the closure; "permitted send" defined
as a send whose reference was appended (reading ii, settles RS5-4 P2); the redundant
gate-closed conjunct dropped or justified (RC5-7 P3); S1/T1 restatements word-identical so
A5/A13 hold literally (RC5-4 P2); B7 rewritten to match the shipped text sentence by
sentence). SRG5-3 P2 (RG-4 heading drops the uncommanded "four fixture tables" count -
docs/CONFORMANCE.md holds FIVE fixture tables incl. C14; property-only phrasing; counts
live in Approach prose). SRG5-4 P2 (R2 trigger, I1, B1 scoped to population lists; I1's
no-third-state claim must not reach the body's own Requirements/Invariants/criteria
tables). SRG5-5 P2 (AS6 reclassified LOAD-BEARING for I2 any-reader regenerability;
locale-sensitive filters sort/uniq bound - run under LC_ALL=C stated next to the neutral
Git configuration, or excluded from the filter class; shipped registers use awk/grep only
and keep their recorded bytes). SRG5-6 P3 (rollout enumeration names T3 and R11). SRG5-7
P3 (R6 "the new sentence S3" -> the four-sentence S3 text). SRG5-8 P3 (VO3 states RG-2's
worktree pass condition: the six anchor lines return with numbers permitted to shift).
SRG5-9 P3 (VO1 records that task records live outside goal worktrees, or names the
exemption). SRG5-10 P3 (RG-2's out-of-band prefix strip moves in-command via its unused
filter slot so the recorded result is verbatim output). SRG5-11 P3 (VO3 table-coverage
decidability: reviewer maps rows to tables by reading the file alongside - state it).
SRG5-12 P3 (R3 audit range: subject = the body's own identifier series; the
referenced-but-undefined check ranges over body-series citations, source identifiers out
of range). Open P0-P2: 7. Round 6 = surgical; round-6 review is the next qualifying
candidate. Rounds 5 of 10.

Round-4 findings (merged, 12 distinct) - binding for round 5 (surgical, hard freeze):
SRG4-1 P1 (an owner-decision closure inside the halt window leaves exactly-one
unsatisfiable - S1's second sentence and T1 replace the closure enumeration with "or
while the entry closed before any permitted send"; A5 clause list matches). SRG4-2 P2
(the gate-open conjunct carries INTO S1's second sentence so template and protocol state
the same rule; settles B7's inference). SRG4-3 P2 (S7 joins R6's enumeration - six sites
+ the insertion; I5 count; A6 criterion text gains the S7 clause). SRG4-4 P2 (RG-4's
result = the command's output line ONLY; the row count moves to Approach prose). SRG4-5
P2 (VO3 gains the coverage bound: the worktree row run must emit rows from all four
fixture tables; a table returning none is red for A11). SRG4-6 P2 (RG-1's match extends
to the P3-sentence family so the register spans both halves of A10; VO2's per-file rule
becomes exactly one cap sentence AND exactly one P3 sentence per file). SRG4-7 P2 (R2's
Git reads run under a stated neutral configuration: git --no-pager -c color.ui=false;
AS6 names the environment axis). SRG4-8 P2 (R3 gains the delete-is-the-repair path: "or
when the retirement is the repair an open row requires, and the body records the gap";
successor recorded in the successor identifier's own clause - state it). KU-1 P3 (the
register preamble sentence gains the digest clause matching R2). SRG4-9 P3 (S3/T2: the
round's attempt number IS the handoff-defect reference - state it, dropping the
redundant also-records duty). SRG4-10 P3 (load-bearing classification added to AS1, AS2,
AS3, AS5, AS6). SRG4-11 P3 (preamble: "byte-comparable, because the two forms are
printed identically"). Open P0-P2: 8. Round 5 = surgical; round-5 review is the next
qualifying candidate. Rounds 4 of 10.

Round-3 findings (merged, 16 distinct; KT-2 and SRG3-5 same subject) - prescriptions
binding for round 4 (surgical, hard freeze otherwise): KT-1 P2 ("that line" -> "the
sentence that line continues" in Approach). SRG3-1 P1 (B6's last sentence scoped to the
REGISTER: "Claim-to-fact content inside a population register is a defect under R5").
SRG3-2 P1 (DELETE B12's three carve-outs - they amend rules this goal does not edit, one
an explicit Non-goal; keep only the recovery clause; the re-record residual returns as an
owner note in Residual risks, honestly stated as unresolved). SRG3-3 P1 (the retirement
guard ships: add to R3 "An identifier an open frozen ledger row cites is retired only
when the body records its successor"; A2 red path gains "a cited identifier retired with
no recorded successor" - this also settles the collective-reading deadlock). SRG3-4 P1
(positive command bound in R2/B1/A1: "one read-only Git read of the recorded revision,
optionally piped to a text filter over that output; starts no other program, changes no
repository or environment state, makes no network request, writes or removes no file").
SRG3-5 P1 + KT-2 (RG-4 recorded VERBATIM - 39 rows, fits caps; the count reduction dies;
A11's absence claim then ranges over recorded row content). SRG3-6 P1 (registers RG-1/
RG-3 defined over whitespace-normalized sentence reads - tr-newline pipe per the
positive bound; VO2 gains "the current-tree run must return exactly one matching
sentence for each of the three files; a missing file is red for A10"). SRG3-7 P2 (VO3's
HEAD -> worktree read - cat file | awk; preamble gains the worktree as third case).
SRG3-8 P2 (current-tree runs extend to RG-2 and RG-3 in VO2/VO3 - all four registers get
both runs; I3/R4 promise kept). SRG3-9 P2 (S6 names the set: "A retry append and a
corrected re-persisted append each hold..."; A6 red path re-aimed at the referent).
SRG3-10 P2 (S3 states the start: first append no number, second records 1, later appends
the next integer; the base "already recorded in the handoff-defect table" sentence
becomes a SEVENTH site restated to draw from the one round counter; T-series covers the
handoff Attempt cell binding). SRG3-11 P2 (VO1 gains git status --porcelain; A12 red
path gains an untracked sixth path - own recorded learning applied). SRG3-12 P3 (I8
"rides the charter's existing Evidence register and traceability map return item").
SRG3-13 P3 (AS2 split: charter licenses the cadence for repair returns; R3 extends to
no-repair returns as the new duty the Authority section states). SRG3-14 P3 (preamble
gains the de-framing sentence for A1-A4; R6 names the insertion site for R1-R5 by
paragraph group). Open P0-P2: 13. Round 4 = surgical repairs; round-4 review is the
next qualifying candidate.

Round-2 findings (merged, 21) - prescriptions binding for round 3 (compact restatement +
repairs): KS-1 P1 (git grep -E does not honor \b on this platform - V4 vacuous; use -nP).
KS-2 P1 (CONFORMANCE already carries V1..V12 headings colliding with the body's V series -
RENAME the body's validation series V -> VO everywhere; V4's claim binds only identifiers
this change INTRODUCES). SRG2-1 P1 (register result cells carry claim-to-fact content -
strip interpretive clauses; results are output or mechanical reductions only; the
completeness reasoning moves to Approach prose; R2 states the cell rule). SRG2-2 P1
(reviewers never receive the Writer return - the ORCHESTRATOR is the sole consumer of the
re-run/audit report; delete the reviewer-comparison clause). SRG2-3+SRG2-8 P1/P2 (the
attempt counter keys to the ROUND alone - derivable from the lens-schedule Round column;
corrected re-persists take the next number and record the originating defect reference;
T2 drops none-on-first-append for that path; template prose says "for that round").
SRG2-4 P1 (sixth R6 site: PROTOCOL:434 "Either append" -> "Each such append"; I5 = four
restatements + one insertion + this site; A6 red path). SRG2-5 P1 (RG-4 re-aimed at
fixture table DATA ROWS across C17/C18/C19 - property, command, and the C17 note's scope
"Across C17, C18, and C19" per SRG2-17). SRG2-6 P1 (RG-1/RG-2 record VERBATIM output
including line text - path:line reductions are blind to content edits). SRG2-7 P1
(registers bind to the RECORDED REVISION: every command runs as git grep ... <mutation-
base-commit> -- path so re-runs are stable across edits; V2/V3 state regeneration runs at
that revision; R4 evaluates divergence against it - this also simplifies SRG2-14). KS-3
P2 (subsumed by SRG2-5). KS-4 P2 (Provenance: the ledger row-matching/re-grade rules are
MUTATION-BASE, not pin). SRG2-9 P2 (T1 carries S1's gate-open bound: "while the sizing
gate is still open" in the interruption clause). SRG2-10 P2 (S4 bounded by the round-3
assignment rule AND the coverage-completion rule; A8 red path). SRG2-11 P2 (B4: an
identifier cited by an open frozen row is not retired; a dropped requirement records the
successor identifier; B11 names the recovery). SRG2-12 P2 (the bound is on the COMMAND
TEXT: "adds no option that opens a hook, pager, editor, or external filter" - default
pager behavior is not a defect; B1 and A1 mirror). SRG2-13 P2 (the audit ranges over THE
IDENTIFIERS THIS BODY DEFINES; source-document identifiers are references). SRG2-14 P2
(mostly dissolved by SRG2-7's revision binding: a register never diverges from working-
tree edits; state the residual: a re-record made solely to restore a register is
coverage-only for S5, not growth for compaction, not a body-difference for L6). SRG2-15
P2 (the report rides "complete Evidence register and traceability map"; AS1 evidence
cell + A2 updated). SRG2-16 P3 (lead sentence: "run as written; add no option and change
no character"). SRG2-17 P3 (folded into SRG2-5). Open P0-P2: 19. Round 3 = compact
restatement carrying all repairs; 13 criteria stays within the re-recorded projection.

Round-2 lens schedule (as run) -  (recorded pre-dispatch, Writer blind): L5+L6 Claims; L3+L4+L6 Spec
- coverage completes at round 2.

Round-1 lens schedule (as run) -  (recorded pre-dispatch, Writer blind; merged catalog as practice):
Claims - L1 claims/citations (dual-source); Spec - L2 charter-interior/governing-text.
Round 2 planned: L5+L6 Claims; L3+L4+L6 Spec.
