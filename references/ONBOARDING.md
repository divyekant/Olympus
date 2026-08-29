# Guided Olympus onboarding

This is the canonical plain-Markdown contract for owner onboarding. It uses Direction A:
a mythic shell with a practical core. The shell names the journey. The core keeps every
value, gate, path, and result exact. It adds no runtime, terminal interface, package,
service, installer, dependency, or user interface.

## Welcome

Welcome. I will inspect the target and the exact framework pin, show a compact proposal,
and wait for approval before any write. Optional art is decorative and carries no meaning.

## Fixed controls

Keep the framework URL and full immutable commit supplied by the owner. Resolve that
exact pin in a clean checkout or cache. A pin identifies content; it does not authenticate
the source. Do not read a newer source working tree.

Every wake or activation request first follows the [canonical activation preflight](PROTOCOL.md#canonical-activation-preflight)
against the target root, whether the target is Olympus or an unrelated repository. Missing
state routes to this guided flow. Partial or malformed state stops. Only an unchanged
complete state can activate. `Awaken Olympus` and `Awaken Olympus.` are guided entries;
in complete state they report verified readiness and the two canonical owner actions
without starting a mode. Only the exact no-period phrase approves an unchanged proposal.

Each preflight capture begins its before-and-after consistency bracket before the initial
PROJECT sample; it is not an atomic filesystem snapshot. Keep all target, checkout,
pinned-contract, canonical-loader, and checkout-status reads inside the bracket. An
unstable bracket or a difference between coherent captures is `changed` and requires fresh
preflight; stable invalid, unreadable, mismatched, or dirty evidence is `malformed` only
after the bracket and coherent final capture complete. Only internal instability or
differing coherent captures is `changed`. The final coherent capture and assignment form
one transition with no read, dispatch, or other action between them. A later repository change is next-entry
state, not a claim that this transition detected it. Project boot resolves the exact pin,
reads pinned `SKILL.md` and `references/PROTOCOL.md`, runs preflight and its final recheck,
then routes; boot mode never routes first.

A present loader needs a canonical comparison against valid PROJECT data or a complete
owner/request URL and full commit. Without source identity, the loader is unverifiable and
the state is `malformed`.

Keep the fixed ordered Pantheon: Orchestrator, System Configurer, Explorer, Spec Writer,
Claims Reviewer, Spec Reviewer, Plan Writer, Plan Verifier, Builder, Docs Writer,
Reviewer, Design Reviewer, Release Agent, Decision Council, and Liaison. Keep their
protocol triggers, duties, and conditional use. The Orchestrator alone routes goals, owns
records and gates, and communicates with roles. Roles return only to the Orchestrator.

Only the System Configurer changes `.olympus/PROJECT.md` and the managed Olympus blocks
in root `AGENTS.md` and `CLAUDE.md`. Preserve all other content and paths. Keep the
owner's double opt-in, the exact uncommitted configuration review, named-path local
commit, fresh review after hook changes, and fresh owner approval for push, pull request,
merge, deploy, publish, release, secret, destructive, paid, or hard-to-reverse actions.

## Inspect first

The Configurer performs read-only inspection before it asks a question or proposes a
write. Follow the canonical preflight above and inspect:

- the owner-supplied URL and full commit, resolved cleanly and exactly;
- repository root, branch or worktree, staged and unstaged Git state, and relevant
  owner edits;
- root `AGENTS.md`, `CLAUDE.md`, `.olympus/PROJECT.md`, loader markers, and surrounding
  content;
- project instructions, maps, validation commands, documentation, and matching design
  standards;
- role preferences, role-specific harness mappings, freshness, tools, support evidence,
  conflicts, stale evidence, and material unknowns.

Do not write during inspection. Complete the bracket and coherent final capture before
classifying stable unavailable, unreadable, mismatched, or dirty pin evidence as `malformed`
and stopping. Reserve `changed` for bracket instability or differing coherent captures.
After inspection, show only material configuration facts. Do not dump raw discovery output.
Use this compact shape:

## What I learned

- Target and intent: `<repository identity and owner direction>`.
- Framework and validation: `<version derived from the exact resolved pin> @ <short pin>`; `<exact URL, full-pin, and validation evidence>`.
- Project state: `<project type, derived map and validation, Git, loaders, PROJECT, and protected paths>`.
- Role support: `<required mappings, freshness, tools, status, evidence, and limits>`.
- Defaults and conflicts: `<safe defaults used; none or exact unresolved items>`.

## Ask one material question

If the framework URL or full commit is missing, ask one blocking question naming only the
missing value or values. Otherwise ask only one unresolved material question about intent,
boot mode, or authority. Ask after inspection, at most one question in a turn. Do not ask
for a resolved fact or a documented default. Include a recommendation and exact effect:

```text
Question: <one missing URL, full commit, or unresolved intent, boot-mode, or authority question>
Recommendation: <recommended answer>
Effect: <one short statement naming the exact field, value, path, or authority result>
```

If the owner changes an answer, regenerate the complete proposal. An earlier approval
does not apply to a changed proposal.

Use these safe defaults when the repository does not decide: `manual` boot mode, the
owner-supplied exact pin, repository-derived Map and Validation, review cap `2`, and
existing host-default model mappings unless a required role is unavailable. A clean
repository with both source values reaches the approval surface without a question.

## Ready to awaken Olympus

When no material question remains, send one message headed exactly `## Ready to awaken Olympus`.
The compact approval surface comes first and must fit within 25 nonblank Markdown lines,
excluding optional art:

- Boot mode: `<manual or orchestration>`.
- Framework: `<version derived from the exact resolved pin> @ <short pin>`; `<full commit and clean exact-pin evidence>`.
- Project and validation: `<detected project type>`; `<repository-derived map and validation>`.
- Role support: `<required mappings, freshness, tools, status, and evidence>`.
- Changed files: `.olympus/PROJECT.md`, `AGENTS.md`, and `CLAUDE.md` only.
- Approval effect: authorizes the unchanged six-stage configuration flow; no write occurs before this reply.
- Boundary: local-only; no push, pull request, merge, deploy, publish, release, secret, paid, destructive, or hard-to-reverse action.
- `Show full configuration`: inspect the exact PROJECT, loaders, mappings, paths, gates, and patch below; it does not change the proposal.
- `Change settings`: expose only boot mode, intent, map or validation, review cap, branch or worktree policy, role or harness mappings, matching standards, and approved custom instructions; regenerate the proposal after any change.

Reply exactly `Awaken Olympus` to approve this unchanged proposal as opt-in two. Do not
write before that reply. A changed proposal needs a new exact second opt-in.

## Full configuration before approval

`Show full configuration` means inspect the complete detail below. Plain Markdown keeps it
inline; a rich host may collapse it. Replace every placeholder with inspected values.
The detail remains complete and exact before approval. It includes the PROJECT, both
loader units, mappings, paths, preservation rules, gates, and patch.

### Complete exact `.olympus/PROJECT.md`

Include the complete file, with all placeholders replaced by approved values, in this
shape. Keep every field, role row, boundary, trigger floor, and support meaning:

```markdown
---
record: olympus-project
schema: 1
---

# Olympus project configuration

This file is the project source of truth. The System Configurer changes it only after
double opt-in.

## Project

| Field | Value |
| --- | --- |
| project name | `<name>` |
| repository root | `<path or repository-relative description>` |
| configuration revision | `1` |
| boot mode | `manual` or `orchestration` |
| configured at | `<date>` |

## Framework source pin

| Field | Value |
| --- | --- |
| repository URL | `<canonical URL>` |
| full immutable commit | `<full commit>` |

The pin identifies framework content. It does not authenticate the source or grant remote
authority.

## Project knowledge

### Intent

`<Owner-approved product direction and current priorities.>`

### Map and documentation

| Area | Paths or source | What it explains | Known gap or freshness limit |
| --- | --- | --- | --- |
| `<area>` | `<paths>` | `<purpose>` | `<none or limit>` |

### Validation

| Scope | Command or evidence | When to use it | Known limit |
| --- | --- | --- | --- |
| `<scope>` | `<command/source>` | `<condition>` | `<none or limit>` |

Map and Validation are hints. Check them against current code for each goal.

## Boundaries

| Setting | Approved value |
| --- | --- |
| protected paths | `.olympus/`; managed blocks in `AGENTS.md` and `CLAUDE.md`; `<other>` |
| allowed project areas | `<paths or all except protected paths>` |
| branch/worktree policy | `<current checkout or branch for clean sequential work; worktree for concurrent work or unrelated dirty state; commit or explicitly include relevant dirty work>` |
| review round cap | `2` (`1`, `2`, or `3`) |
| local commit policy | `<project convention>` |

The owner gates in the runtime protocol are fixed and not configurable in PROJECT.

## Harness and role support

Use `supported`, `unsupported`, or `untested`. Record one row for each harness-role pair
that a goal can invoke. A tool's availability alone is `untested`.

| Harness | Role | Status | Mapping and freshness | Tools or capabilities | Observed evidence and limit |
| --- | --- | --- | --- | --- | --- |
| `<harness>` | Orchestrator | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | System Configurer | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Explorer | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Spec Writer | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Claims Reviewer | `<status>` | `<mapping and fresh context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Spec Reviewer | `<status>` | `<mapping and fresh context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Plan Writer | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Plan Verifier | `<status>` | `<mapping and fresh context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Builder | `<status>` | `<mapping and separate context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Docs Writer | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Reviewer | `<status>` | `<mapping and fresh context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Design Reviewer | `<status>` | `<mapping and fresh context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Release Agent | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Decision Council | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Liaison | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |

Unsupported harnesses do not run goals that invoke unsupported roles through Olympus.

## Project design standards

Record the sources and matching details that Design Reviewer uses. Missing required
standards or matching evidence makes a triggered Design Reviewer unavailable.

| Source | Matching project area or component | Standard or rule | Status and evidence | Limit |
| --- | --- | --- | --- | --- |
| `<path or source>` | `<area or component>` | `<standard>` | `<supported, missing, or stale>` | `<limit>` |

## Role preferences

These settings select implementations inside fixed duties. They do not change the graph.

The trigger floor is immutable. PROJECT can make an optional trigger more eager, add
matching details, or identify standards and tools. It cannot suppress a trigger or add a
role.

| # | Role | Immutable trigger floor | When used | Model or capability | Tools | Limit |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Orchestrator | every routed request | `<when used>` | `<preference or host default>` | `<tools>` | `<limit>` |
| 2 | System Configurer | owner onboarding or configuration request, plus double opt-in | `<when used>` | `<preference>` | `<tools>` | `<limit>` |
| 3 | Explorer | fresh for material repository question blocking a required role, or explicit audit | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 4 | Spec Writer | substantial, ambiguous, architectural, or cross-layer goal | `<when used>` | `<preference>` | `<tools>` | `<limit>` |
| 5 | Claims Reviewer | every Spec Writer result; fresh and read-only | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 6 | Spec Reviewer | every Spec Writer result; fresh and read-only | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 7 | Plan Writer | accepted contract has dependent steps, cross-layer or interface sequencing, or explicit plan need | `<when used>` | `<preference>` | `<tools>` | `<limit>` |
| 8 | Plan Verifier | every Plan Writer result; fresh and read-only | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 9 | Builder | every non-configuration project mutation | `<when used>` | `<preference>` | `<tools>` | `<limit>` |
| 10 | Docs Writer | Builder makes tracked docs false, or contract requires synchronization | `<when used>` | `<preference>` | `<tools>` | `<limit>` |
| 11 | Reviewer | every project or configuration mutation; fresh and read-only | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 12 | Design Reviewer | material user-facing interface, interaction, visual design, or design-system change; fresh and read-only | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 13 | Release Agent | owner-requested release preparation, remote reconciliation, or one release-boundary external action; no standing authority | `<when used>` | `<preference>` | `<read-only provider evidence>` | `<limit>` |
| 14 | Decision Council | unresolved material decision with viable trade-offs; read-only advisory | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 15 | Liaison | human status or explanation request; read-only and no gate | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |

## Approved custom instructions and evolutions

Entries can add or narrow behavior. They cannot add roles, remove duties, change hub
communication, bypass review, alter protected paths, or widen external authority.

| Name | Kind | Scope | Instruction | Approval revision |
| --- | --- | --- | --- | --- |
| `<name>` | `custom` or `evolution` | `<role/path/goal>` | `<exact text>` | `<revision>` |
```

### Exact managed loader blocks

Place this complete, unchanged block in each named file. Content outside the markers is
preserved byte-for-byte. The two managed units are proposed together:

#### `AGENTS.md`

```markdown
<!-- OLYMPUS:BEGIN -->
## Olympus loader

1. Begin the first consistency bracket before the initial PROJECT sample.
2. Inside that open bracket, sample identities for `.olympus/PROJECT.md`, root `AGENTS.md`,
   and root `CLAUDE.md`. Read PROJECT or use a complete owner/request URL and full commit.
   Resolve the exact framework repository URL and full commit in a clean checkout or cache.
   Sample the resolved checkout path, commit, readability, and clean status. Read
   `SKILL.md` and `references/PROTOCOL.md` as pinned contracts from that framework
   version, then read both managed units, canonical loader bytes, and checkout evidence.
   Repeat the exact target and checkout samples. Record invalid pin evidence for unavailable,
   mismatched, or dirty pins and complete the bracket before classification.
3. Close the bracket only when all before and after samples match. An unstable capture
   returns `changed` and requires fresh preflight. Only a coherent first capture may
   classify. Stable invalid pin evidence is classified as `malformed` only after the
   coherent final capture.
4. Run the canonical activation preflight from the pinned protocol against the target
   repository root using the coherent first capture.
5. Run the immediate final recheck from that preflight. Perform the coherent final capture
   under the same bracket rules and bind its result.
6. Only after the final capture returns an unchanged `complete` state, route the requested
   entry: in `manual` boot mode, load Olympus only for `Use Olympus for: <goal>` or
   `Activate Olympus orchestration`; in `orchestration` boot mode, route project-changing
   requests through Olympus. Questions do not create goals. `missing`, `partial`,
   `malformed`, or `changed` results stop without activation.
7. Load only the charter required for the next role.
8. Before dispatch, confirm a role-specific harness mapping, freshness, tools, support
   status, and evidence for every invoked role. Missing mapping blocks the goal.
9. For configuration, require System Configurer support and a fresh Reviewer mapping for
   the exact uncommitted configuration unit before staging or commit.
10. Existing host and project instructions still apply. Stop and report a conflict that
    prevents the fixed Olympus workflow.
<!-- OLYMPUS:END -->
```

#### `CLAUDE.md`

Use this identical complete managed block. The path is different; the block and marker
pair are not. Reject malformed, duplicate, nested, or incomplete markers.

```markdown
<!-- OLYMPUS:BEGIN -->
## Olympus loader

1. Begin the first consistency bracket before the initial PROJECT sample.
2. Inside that open bracket, sample identities for `.olympus/PROJECT.md`, root `AGENTS.md`,
   and root `CLAUDE.md`. Read PROJECT or use a complete owner/request URL and full commit.
   Resolve the exact framework repository URL and full commit in a clean checkout or cache.
   Sample the resolved checkout path, commit, readability, and clean status. Read
   `SKILL.md` and `references/PROTOCOL.md` as pinned contracts from that framework
   version, then read both managed units, canonical loader bytes, and checkout evidence.
   Repeat the exact target and checkout samples. Record invalid pin evidence for unavailable,
   mismatched, or dirty pins and complete the bracket before classification.
3. Close the bracket only when all before and after samples match. An unstable capture
   returns `changed` and requires fresh preflight. Only a coherent first capture may
   classify. Stable invalid pin evidence is classified as `malformed` only after the
   coherent final capture.
4. Run the canonical activation preflight from the pinned protocol against the target
   repository root using the coherent first capture.
5. Run the immediate final recheck from that preflight. Perform the coherent final capture
   under the same bracket rules and bind its result.
6. Only after the final capture returns an unchanged `complete` state, route the requested
   entry: in `manual` boot mode, load Olympus only for `Use Olympus for: <goal>` or
   `Activate Olympus orchestration`; in `orchestration` boot mode, route project-changing
   requests through Olympus. Questions do not create goals. `missing`, `partial`,
   `malformed`, or `changed` results stop without activation.
7. Load only the charter required for the next role.
8. Before dispatch, confirm a role-specific harness mapping, freshness, tools, support
   status, and evidence for every invoked role. Missing mapping blocks the goal.
9. For configuration, require System Configurer support and a fresh Reviewer mapping for
   the exact uncommitted configuration unit before staging or commit.
10. Existing host and project instructions still apply. Stop and report a conflict that
    prevents the fixed Olympus workflow.
<!-- OLYMPUS:END -->
```

### Paths, preservation, conflicts, gates, and opt-in

The same readiness message lists:

- every created or changed path: `.olympus/PROJECT.md`, `AGENTS.md`, `CLAUDE.md`, and no
  other path unless the complete proposal names it;
- the preservation rule: all content outside each managed marker pair remains unchanged;
- conflicts: `<none or each exact conflict and affected path>`;
- rejected settings: `<none or each setting rejected because it changes a fixed role,
  trigger, duty, path, review, authority, or external-action gate>`;
- the named-path local commit: `git add -- .olympus/PROJECT.md AGENTS.md CLAUDE.md`, then
  the normal hooks and `Configure Olympus` or `Update Olympus configuration`;
- external action: `none approved`; do not push, create a pull request, merge, deploy,
  publish, release, change secrets, or perform a destructive, paid, or hard-to-reverse
  action.

### Exact patch

The readiness response must include the actual unapplied patch bytes for all three target
files. Prose about the operation is not sufficient. Replace every placeholder in the
following required fenced blocks with generated bytes before approval. A remaining
placeholder makes the proposal incomplete.

#### `.olympus/PROJECT.md` exact unapplied bytes

```markdown
<actual generated bytes for .olympus/PROJECT.md>
```

#### `AGENTS.md` exact before-and-after bytes

```diff
<actual exact before and after bytes for root AGENTS.md, including preserved surrounding content>
```

#### `CLAUDE.md` exact before-and-after bytes

```diff
<actual exact before and after bytes for root CLAUDE.md, including preserved surrounding content>
```

These bytes create or update `.olympus/PROJECT.md` and insert identical loader units in
root `AGENTS.md` and `CLAUDE.md`. They preserve content outside each marker pair, change
no other path, and remain unapplied until the exact second opt-in.

Before dispatch, record the current mapping, freshness, tools, support status, observed
evidence, and limit for every required role. For this configuration flow, include at
least these exact rows in the readiness message:

| Role | Mapping and freshness | Tools | Status | Evidence and limit |
| --- | --- | --- | --- | --- |
| System Configurer | `<explicit mapping; inspection context>` | `<tools>` | `untested`, `supported`, or `unsupported` | `<exact-pin evidence or limit>` |
| Reviewer | `<explicit fresh mapping for exact uncommitted unit>` | `<read-only tools>` | `untested`, `supported`, or `unsupported` | `<exact-unit evidence or limit>` |

The owner request is opt-in one. The owner must reply exactly `Awaken Olympus` to approve
this unchanged complete proposal as opt-in two. `Awaken Olympus.` is guided entry only and
does not approve the patch. Do not write before the exact reply. A changed proposal
requires a new exact second opt-in.

## Six stages

Use these six stages, in this order, and no other stage names:

1. `Recheck paths`
2. `Apply approved configuration`
3. `Validate configuration`
4. `Fresh review`
5. `Commit approved paths`
6. `Confirm committed result`

Each stage has exactly one of these four statuses: `PENDING`, `ACTIVE`, `PASS`, or
`STOPPED`. `PENDING` means not started. `ACTIVE` means in progress. `PASS` means the
required evidence exists. `STOPPED` means safe continuation is not allowed. Only one
stage can be `ACTIVE`. When a stage stops, keep later stages `PENDING`. Stage status is
separate from role support status.

Start the readiness message with all six stages as `PENDING`:

| # | Stage | Status |
| --- | --- | --- |
| 1 | Recheck paths | `PENDING` |
| 2 | Apply approved configuration | `PENDING` |
| 3 | Validate configuration | `PENDING` |
| 4 | Fresh review | `PENDING` |
| 5 | Commit approved paths | `PENDING` |
| 6 | Confirm committed result | `PENDING` |

Whenever any stage changes status, send the complete compact six-stage table again in
that same update. Send all six rows when a stage becomes `ACTIVE`, `PASS`, or `STOPPED`;
do not send only the changed row. Mark `PASS` only after its required evidence exists.
Keep only one `ACTIVE` stage. After a `STOPPED` stage, keep every later stage `PENDING`.

### Stage evidence and gates

- Before dispatch, confirm a role-specific mapping, freshness, tools, support state, and
  evidence for every required role. A missing or `unsupported` required mapping stops
  dispatch. An `untested` Configurer mapping may inspect, propose, apply, and validate,
  but the flow stops before staging unless exact-pin apply and validation then make that
  Configurer behavior `supported`.
- `Recheck paths` compares affected paths and current Git state with the approved
  proposal. Stop on a changed path, new owner edit, unexpected staged content, missing
  or unsupported mapping, or malformed, duplicate, nested, or incomplete loader marker.
- `Apply approved configuration` changes only `.olympus/PROJECT.md` and the two managed
  blocks. It preserves surrounding content and does not commit.
- `Validate configuration` checks the exact URL and full commit, PROJECT fields and
  revision, boot mode, fifteen role rows and trigger floors, role mappings and support
  evidence, loader equality and marker count, surrounding content, and named-path scope.
  Successful apply and validation at this exact pin are the observed Configurer support
  evidence; tools, a proposal, another role, or another commit are not evidence.
- `Fresh review` is an Orchestrator-controlled handoff. The Configurer returns the exact
  uncommitted PROJECT and both managed loader units only to the Orchestrator. The
  Configurer does not invoke or communicate with the Reviewer. The Orchestrator confirms
  a fresh Reviewer mapping for that exact unit, dispatches it, and continues only on a
  pass, then returns that verdict to the Configurer. An `untested` Reviewer mapping becomes
  `supported` only after observed passing behavior over that exact unit. A missing or
  `unsupported` mapping stops the stage.
- For `Commit approved paths`, the Configurer requires supported apply and validation plus
  the exact-unit fresh Reviewer pass returned by the Orchestrator. The Configurer stages
  only the three named paths, runs normal hooks, uses the approved commit message, does not
  push, and returns the exact committed unit, commit, and hook evidence only to the
  Orchestrator. A repair or blocked review prevents staging and commit. Repair beyond the
  approved proposal requires a new complete proposal and second opt-in.
- For `Confirm committed result`, the Configurer returns the exact committed unit and
  remaining Git state to the Orchestrator. If a hook changed reviewed content, the
  Orchestrator dispatches a fresh review of that exact committed unit and returns the
  verdict. After that pass, or when no hook changed content, the Configurer confirms the
  commit matches the approved proposal and returns the confirmation to the Orchestrator.
  Report any changed or untracked path.

### Truthful role support

Keep role support separate from stage status:

- `supported` means the required mapping and behavior passed at the pinned commit;
- `unsupported` means the harness cannot preserve the required role, freshness,
  owner-approved scope, or owner-authority boundary;
- `untested` means a mapping or tool exists but required behavior has not passed at the
  pinned commit. Tool availability alone is `untested`.

Never infer one role's support from another role's result. Missing or unsupported
required mappings block dispatch. Unknown, skipped, and untested evidence stays visible.

## Success report

After all six stages pass, report every field below. The final line is exactly the stated
line, with no text after it:

```text
## Success report
Stages: Recheck paths=PASS; Apply approved configuration=PASS; Validate configuration=PASS; Fresh review=PASS; Commit approved paths=PASS; Confirm committed result=PASS.
Configuration revision and boot mode: <exact values>.
Framework URL and full commit: <exact values>.
Changed paths: <exact named paths>.
Configurer support: <exact-pin apply and validation evidence>.
Fresh Reviewer: <fresh mapping, exact unit, verdict, and evidence>.
Local commit: <identifier and approved message>.
Hook rereview: <not required or exact committed-content review>.
Final Git state: <exact status and remaining paths>.
External action: none.
Remaining uncertainty: <none or exact limit>.
Olympus is awake.
```

## Failure report

If dispatch or a stage cannot continue, report every field below. Use the exact
`STOPPED` stage, or `pre-dispatch mapping gate` when no dispatch occurred. The final line
is exactly the stated line, with no text after it:

```text
## Failure report
Stopped stage: <exact stage name and STOPPED, or pre-dispatch mapping gate>.
Reason: <exact blocking reason>.
Mapping and support: <affected mapping, freshness, tools, status, evidence, and limit>.
Changed paths: <exact paths or none>.
Commit state: <identifier or no commit>.
Current Git state: <exact status and remaining paths>.
Smallest safe next step: <one action that does not widen approval>.
Olympus stopped.
```

Do not reset, stash, overwrite, amend, hide, or stage unrelated owner work. Do not turn
an untested, unsupported, blocked, or stopped result into a pass.

## Plain Markdown limitations

Plain Markdown carries the complete instructions, fields, order, and meanings. It does
not enforce inspection, context freshness, role separation, owner approval, path scope,
Git staging, hook behavior, or external-action boundaries. Host permissions, normal Git
review, branch protection, and a capable harness can add enforcement. Olympus does not
claim that Markdown itself is a security sandbox or that a written flow proves execution.
