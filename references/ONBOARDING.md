# Guided Olympus onboarding

This is the canonical plain-Markdown contract for owner onboarding. The experience is
simple and a little magical: inspect quietly, show one small proposal, wait for one
phrase, then wake. The core keeps every value, gate, path, and result exact. Advanced
detail exists before approval but appears only on request. Onboarding adds no runtime,
terminal interface, package, service, installer, dependency, or user interface.

## Fixed controls

- Keep the framework URL and full immutable commit supplied by the owner. Resolve that
  exact pin in a clean checkout or cache. A pin identifies content; it does not
  authenticate the source. Do not read a newer source working tree.
- Every wake or activation request first follows the
  [canonical activation preflight](PROTOCOL.md#canonical-activation-preflight) against
  the target root. `missing` state routes to this guided flow. `partial`, `malformed`,
  or `changed` state stops with exact evidence. Only an unchanged `complete` state can
  activate.
- Keep the fixed ordered Pantheon and its protocol triggers, duties, and conditional
  use. The Orchestrator alone routes goals and owns records and gates. Roles return only
  to the Orchestrator.
- Only the System Configurer changes `.olympus/PROJECT.md` and the managed Olympus
  blocks in root `AGENTS.md` and `CLAUDE.md`. Preserve all other content and paths.
- Keep the owner's double opt-in, the fresh review of the exact uncommitted
  configuration unit, the named-path local commit, fresh review after hook changes, and
  fresh owner approval for push, pull request, merge, deploy, publish, release, secret,
  destructive, paid, or hard-to-reverse actions.

## The wake phrase

`Awaken Olympus` is the guided entry phrase. Trim surrounding whitespace and accept one
optional final period; both forms carry the same meaning. Context decides the effect:

- `missing` state: start this guided flow with a read-only inspection.
- an unchanged `## Ready to awaken Olympus` proposal: approve it as opt-in two.
- `complete` state: report verified readiness and the two canonical owner actions
  (`Use Olympus for: <goal>` and `Activate Olympus orchestration`) without starting a
  mode.

Any changed proposal requires a new second opt-in. The phrase is never a session
activation alias.

## Inspect first

The Configurer inspects read-only before it asks a question or proposes a write:

- the owner-supplied URL and full commit, resolved cleanly and exactly;
- repository root, branch or worktree, and staged and unstaged Git state;
- root `AGENTS.md`, `CLAUDE.md`, `.olympus/PROJECT.md`, loader markers, and surrounding
  content;
- project instructions, maps, validation commands, documentation, and matching design
  standards;
- role support, conflicts, stale evidence, and material unknowns.

Do not write during inspection. Do not dump raw discovery output. Keep the working
detail; the owner sees only what changes their decision.

## Ask one material question

If the framework URL or full commit is missing, ask one blocking question that names
only the missing value or values. Otherwise ask at most one unresolved material question
per turn, only about intent, boot mode, or authority. Do not ask for a resolved fact or
a documented default. Include a recommendation and exact effect:

```text
Question: <one missing URL, full commit, or unresolved intent, boot-mode, or authority question>
Recommendation: <recommended answer>
Effect: <one short statement naming the exact field, value, path, or authority result>
```

Safe defaults when the repository does not decide: `manual` boot mode, the
owner-supplied exact pin, repository-derived Map and Validation, review cap `2`, and
host-default role mappings with status `untested` unless a required role is unavailable.
A clean repository with both source values reaches the approval surface without a
question. If the owner changes an answer, regenerate the complete proposal; an earlier
approval does not apply to a changed proposal.

## Ready to awaken Olympus

When no material question remains, generate the complete proposal, then send one message
headed exactly `## Ready to awaken Olympus`. The approval surface is at most 12 nonblank
Markdown lines, excluding optional art, in this shape:

- What I found: `<one line: project type, Git state, and owner direction>`.
- Framework: `<version derived from the exact resolved pin> @ <short pin>`, resolved clean.
- Boot mode: `<manual or orchestration>` — `<one clause on what that means here>`.
- Validation: `<repository-derived commands or none found>`.
- Files: `.olympus/PROJECT.md` plus one small managed loader block in `AGENTS.md` and
  `CLAUDE.md`. Nothing else changes; content outside the markers is preserved.
- Boundary: local-only. No push, pull request, merge, deploy, publish, release, secret,
  paid, destructive, or hard-to-reverse action.

Reply `Awaken Olympus` to approve. `Show details` reveals the full configuration first.
`Change settings` adjusts the owner knobs. No write occurs before your reply.

Optional decorative art carries no meaning. Every required fact, gate, and action must
survive with art removed.

## Details on request

The complete proposal must exist before the approval surface is sent; disclosure is
progressive but generation is not. `Show details` reveals, without changing the
proposal:

- the complete exact `.olympus/PROJECT.md` bytes, following the
  [PROJECT template](../templates/PROJECT.md) with every placeholder replaced;
- the exact managed loader block from the
  [bootstrap template](../templates/BOOTSTRAP.md), inserted identically in root
  `AGENTS.md` and `CLAUDE.md`, as exact before-and-after bytes for both files;
- role support rows for at least System Configurer and the fresh Reviewer of the exact
  configuration unit, each with mapping, tools, `supported`, `unsupported`, or
  `untested` status, and evidence or limit;
- conflicts (`none` or each exact conflict and affected path) and rejected settings
  (`none` or each setting rejected because it changes a fixed role, trigger, duty, path,
  review, authority, or external-action gate);
- the named-path local commit plan: `git add -- .olympus/PROJECT.md AGENTS.md CLAUDE.md`,
  normal hooks, and the message `Configure Olympus` or `Update Olympus configuration`;
- external action: `none approved`.

A remaining placeholder makes the proposal incomplete. `Change settings` exposes only
boot mode, intent, Map or Validation, review cap, branch or worktree policy, role or
harness mappings, matching standards, and approved custom instructions. It cannot change
fixed roles, triggers, duties, protected paths, owner gates, or external authority.
After any change, regenerate the proposal and require a new second opt-in.

## Six stages

After opt-in two, run these six stages in this order and no other stage names:

1. `Recheck paths`
2. `Apply approved configuration`
3. `Validate configuration`
4. `Fresh review`
5. `Commit approved paths`
6. `Confirm committed result`

Each stage has exactly one status: `PENDING`, `ACTIVE`, `PASS`, or `STOPPED`. Only one
stage is `ACTIVE` at a time. Mark `PASS` only after its required evidence exists. When a
stage stops, keep every later stage `PENDING`. Stage status is separate from role
support status.

Report compactly: announce that the six stages are starting, then work without
per-transition tables. Send the complete six-stage table exactly once at the end — all
`PASS` in the success report, or the exact stopped state in the failure report. If the
owner asks for status mid-flow, show the current complete table.

### Stage evidence and gates

- Before dispatch, confirm mapping, freshness, tools, support state, and evidence for
  every required role. A missing or `unsupported` required mapping stops dispatch. An
  `untested` Configurer mapping may inspect, propose, apply, and validate, but the flow
  stops before staging unless exact-pin apply and validation make that behavior
  `supported`.
- `Recheck paths` compares affected paths and current Git state with the approved
  proposal. Stop on a changed path, new owner edit, unexpected staged content, missing
  or unsupported mapping, or a malformed, duplicate, nested, or incomplete loader
  marker.
- `Apply approved configuration` changes only `.olympus/PROJECT.md` and the two managed
  blocks. It preserves surrounding content and does not commit.
- `Validate configuration` checks the exact URL and full commit, PROJECT fields and
  revision, boot mode, role support and preference rows, loader equality and marker
  count, surrounding content, and named-path scope. Successful apply and validation at
  this exact pin are the observed Configurer support evidence; tools, a proposal,
  another role, or another commit are not evidence.
- `Fresh review` is an Orchestrator-controlled handoff. The Configurer returns the exact
  uncommitted PROJECT and both managed loader units only to the Orchestrator. The
  Orchestrator confirms a fresh Reviewer mapping for that exact unit, dispatches it, and
  continues only on a pass. An `untested` Reviewer mapping becomes `supported` only
  after observed passing behavior over that exact unit.
- `Commit approved paths` requires supported apply and validation plus the exact-unit
  fresh Reviewer pass. The Configurer stages only the three named paths, runs normal
  hooks, uses the approved commit message, and does not push. A repair or blocked review
  prevents staging and commit. Repair beyond the approved proposal requires a new
  complete proposal and second opt-in.
- `Confirm committed result` compares the commit with the approved proposal. If a hook
  changed reviewed content, the Orchestrator dispatches a fresh review of the exact
  committed unit first. Report any changed or untracked path.

### Truthful role support

- `supported` means the required mapping and behavior passed at the pinned commit.
- `unsupported` means the harness cannot preserve the required role, freshness,
  owner-approved scope, or owner-authority boundary.
- `untested` means a mapping or tool exists but required behavior has not passed at the
  pinned commit. Tool availability alone is `untested`.

Never infer one role's support from another role's result. Unknown, skipped, and
untested evidence stays visible.

## Success report

After all six stages pass, report every field below. The final line is exactly the
stated line, with no text after it:

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
`STOPPED` stage, or `pre-dispatch mapping gate` when no dispatch occurred. The final
line is exactly the stated line, with no text after it:

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
claim that Markdown itself is a security sandbox or that a written flow proves
execution.
