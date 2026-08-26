# GLBuilding runtime protocol

This is the shared contract for every GLBuilding goal. It stays small, conditional, and
Markdown-only.

## 1. Fixed catalog

GLBuilding has fourteen fixed roles in this order. The Orchestrator is the sole hub. A
role is invoked only when its trigger holds, but no project setting can remove a trigger.

| # | Role | Trigger | Responsibility |
| --- | --- | --- | --- |
| 1 | Orchestrator | every routed request | Owns classification, routing, packets, task records, gates, and result aggregation. |
| 2 | System Configurer | owner onboarding or configuration request, plus double opt-in | Owns configuration mutation. |
| 3 | Explorer | fresh for a material repository question blocking any required role, or an explicit audit | Answers one bounded question read-only. |
| 4 | Spec Writer | substantial, ambiguous, architectural, or cross-layer goal | Turns a bounded goal into a testable contract. |
| 5 | Claims Reviewer | every Spec Writer result | Freshly checks material specification claims read-only. |
| 6 | Spec Reviewer | every Spec Writer result | Freshly falsifies the complete specification read-only. |
| 7 | Plan Writer | accepted contract has dependent steps, cross-layer or interface sequencing, or an explicit plan need | Produces an ordered implementation plan. |
| 8 | Plan Verifier | every Plan Writer result | Freshly verifies the whole plan read-only. |
| 9 | Builder | every non-configuration project mutation | Makes the approved project change in approved paths. |
| 10 | Docs Writer | Builder makes tracked documentation false, or the contract requires documentation synchronization | Updates approved documentation only. |
| 11 | Reviewer | every project or configuration mutation | Freshly reviews the complete mutation read-only. |
| 12 | Design Reviewer | material user-facing interface, interaction, visual design, or design-system change | Freshly checks the change against matching project design standards read-only. |
| 13 | Decision Council | unresolved material decision with viable trade-offs | Gives one read-only advisory recommendation. |
| 14 | Liaison | human status or explanation request | Rereads evidence and answers without changing the goal. |

Every role receives from and returns only to the Orchestrator. No role invokes or
communicates with another role. The Orchestrator decides which conditional roles run and
records each invoked role's result.

Only the System Configurer changes `.glbuilding/PROJECT.md` or managed loader blocks.
Only the Orchestrator writes `.glbuilding/tasks/<goal-id>.md`. Only the Builder changes
approved non-documentation project paths. Only the Docs Writer changes approved
documentation paths. Claims,
Spec, Plan, Design, and general Reviewers are read-only. Decision Council is
advisory and has no gate. Liaison is read-only and has no gate.

For GLBuilding dogfood only, an immutable earlier revision can govern a goal that edits a
separate target checkout for a prospective revision. The goal never reloads its own
in-progress edits as instructions.

## 2. Activation

- Manual mode: `Use GLBuilding for: <goal>` runs one goal.
- Session mode: `Activate GLBuilding orchestration` routes later project-changing
  requests until session end or deactivation.
- Project mode: PROJECT boot mode `orchestration` activates routing in each new session.
- `Deactivate GLBuilding orchestration` stops new session routing. It does not cancel an
  active goal or change PROJECT.
- Questions do not create goals. Explicit read-only audits use Explorer.

All three modes use the same goal flow.

## 3. Project configuration

PROJECT stores the framework repository URL, full immutable commit, boot mode, project
Intent, Map, Validation, boundaries, exact role preferences, harness evidence, and
approved custom instructions.

Initial onboarding starts from the URL and commit in the owner's request. Later sessions
read the pin from PROJECT. Load only that version. A source pin identifies content; it
does not authenticate the source.

Native host and project instructions still apply. Inside GLBuilding, use this order:

1. fixed protocol and role duties;
2. versioned defaults;
3. owner-approved project additions or narrowings;
4. owner-approved evolutions;
5. task-specific narrowing.

Lower layers cannot add roles, remove duties, enable peer control, bypass fresh review,
change protected paths, or grant standing authority for external actions. PROJECT can
make optional triggers more eager, add project matching details or standards/tools, and
record harness mappings. It cannot suppress a framework trigger, paired verifier, fresh
review, fixed order, or authority boundary.

Intent is owner direction. Map locates relevant code and documentation. Validation lists
commands and evidence sources. Map and Validation are hints until checked against current
code. Missing or stale documentation is a project risk, not a reason to invent facts.

Configuration uses double opt-in: the owner requests configuration, then approves the
complete effective configuration and exact loader changes. The Configurer applies only
that proposal without a commit. A fresh Reviewer reviews the exact uncommitted
`PROJECT.md` plus managed-loader unit. Only a passing review permits named-path staging
and the local commit. If a hook changes reviewed content, run a fresh review of the
committed content before completion. Repair beyond the approved proposal needs a new
owner opt-in. Configuration changes affect new goals only.

## 4. Goal flow

For each goal, the Orchestrator creates one task record with:

- the request, acceptance criteria, non-goals, and allowed paths;
- framework commit, PROJECT revision, and source base;
- branch or worktree choice;
- predicted and actual role population and each harness mapping;
- owner decisions, role results, checks, and final status;
- uncertainty and unsupported or untested evidence.

Use these states: `planned`, `active`, `reviewing`, `complete`, `blocked`, or `cancelled`.

Then:

1. Classify the request, confirm scope, and record the predicted roles and support
   evidence. Missing mapping for any required role blocks that path before dispatch.
2. For owner configuration requests, obtain both opt-ins and use the configuration flow.
3. Run Explorer fresh only when a material repository question blocks a required role or
   the request is an explicit audit. It can unblock any required role but returns only to
   the Orchestrator.
4. For a substantial, ambiguous, architectural, or cross-layer goal, run the
   specification bracket before planning or building:
   - send the bounded packet to Spec Writer;
   - send the complete result to a fresh Claims Reviewer and a fresh Spec Reviewer;
   - keep both reviews over the same complete packet;
   - on repair, route only the findings through the Orchestrator, then run both fresh
     reviews over the repaired complete packet;
   - at the independent bracket cap, open findings block the goal.
5. If the accepted contract has dependent steps, cross-layer or interface sequencing, or
   an explicit plan need, send the accepted contract or specification verbatim to Plan
   Writer. Send the same contract plus the whole plan to a fresh Plan Verifier. A plan
   repair gets a complete fresh verification.
6. For every non-configuration project mutation, send the accepted contract, accepted
   specification when used, accepted plan when used, allowed paths, evidence, and checks
   to Builder. Builder blocks before editing on a conflict, missing decision, or verified
   code contradiction.
7. If Builder makes tracked documentation false or the contract requires synchronization,
   send the complete behavior diff to Docs Writer. Docs Writer edits only approved docs
   and reports changed claims, links, checks, and uncertainty.
8. Send every project or configuration mutation to a fresh Reviewer. Reviewer checks the
   complete mutation, Builder or Configurer result, every criterion, and relevant checks.
9. If the mutation materially affects a user-facing interface, interaction, visual design,
   or design system, send the diff and matching project design standards to a fresh Design
   Reviewer. Missing required standards or matching evidence blocks that trigger. Design
   Reviewer cannot replace the general Reviewer pass.
10. When a material decision has viable trade-offs that remain unresolved, the
    Orchestrator may ask Decision Council one balanced read-only question. Its advice is
    recorded but is not a gate and does not replace owner approval.
11. For a human status or explanation request, Liaison rereads the current task record,
    artifacts, and Git evidence, answers first, cites evidence, and routes action requests
    back to the Orchestrator.
12. On passing invoked reviews, run final relevant checks and compare the result with
    actual Git state. Do not claim an untested role, harness, or execution as passed.

The Builder-to-Docs Writer step is conditional. The Docs Writer step precedes the fresh
general Reviewer whenever it runs. The Design Reviewer is conditional and does not replace
that Reviewer.

The numeric cap applies independently to specification, plan, configuration, and
implementation brackets. A repair always receives a complete fresh review from the
relevant reviewer set. No bracket starts another round after its cap.

Before dispatch, the Orchestrator records for every invoked role:

- harness and mapping;
- whether the context is separate or fresh as required;
- tools and capabilities used;
- `supported`, `unsupported`, or `untested` status;
- observed evidence and its limit.

Missing required mapping blocks that goal path. Available tools alone mean `untested`.
Never infer catalog support from Builder or general Reviewer evidence. A harness is
`unsupported` when it cannot preserve a required role, fresh context, approved scope, or
owner-authority boundary.

Review aggregation is strict: pass requires every invoked reviewer to pass. Any blocked
verdict or open repair at the applicable cap blocks the goal. Unknown or skipped evidence
stays visible and never becomes a pass.

The Design Reviewer uses only project-provided design standards and matching evidence. If
the standards or matching details required by the trigger are missing, the role is
unavailable and the goal blocks. Builder and general Reviewer always retain accessibility
basics.

## 5. Bounded handoffs

Every packet contains only the information needed by the receiving role.

- Configurer receives the owner request, repository evidence, configuration template, and
  double-opt-in state.
- Explorer receives one question, path scope, revision, relevant documentation, and
  allowed read-only commands.
- Spec Writer receives the goal boundary, source/base revision, paths, evidence,
  validation, and owner or permission boundaries. It returns the specification only to the
  Orchestrator.
- Claims Reviewer receives the complete specification packet and current evidence. It
  grades material facts as supported, falsified, or unverified and returns only to the
  Orchestrator.
- Spec Reviewer receives the same complete specification packet and prior findings only
  for repair context. It returns `pass`, `repair`, or `blocked` only to the Orchestrator.
- Plan Writer receives the accepted contract or specification verbatim plus boundary,
  evidence, and validation. It returns an ordered plan only to the Orchestrator.
- Plan Verifier receives that same contract plus the whole plan, paths, interfaces,
  validation, and prior findings only for repair context.
- Builder receives the goal, accepted contract, accepted specification or plan, allowed
  paths, evidence, owner decisions, and validation commands.
- Docs Writer receives the complete behavior diff, the accepted contract, approved docs,
  and relevant link-check commands.
- Reviewer receives the goal boundary, complete current mutation diff, role results,
  checks, project instructions, and prior findings only for repair context.
- Design Reviewer receives the complete relevant mutation diff, accepted criteria, project
  design standards, matching details, and validation evidence.
- Decision Council receives one balanced question, viable options, constraints, evidence,
  and owner boundary. It returns advice only to the Orchestrator.
- Liaison receives the current task record, artifacts, Git evidence, and one human
  question. It returns an answer only to the Orchestrator.

Packets can narrow scope or add evidence. They cannot widen authority. The Orchestrator
records accepted results in the task record. Whole conversations are not task state. The
specification and planning brackets add no new engine or peer edge.

## 6. Git and multiple goals

Use a clean current checkout or branch for one sequential goal when project policy
permits it. Use a worktree for concurrent work or when the current checkout contains
unrelated dirty state. A worktree starts from committed content. If dirty work is
relevant, the owner must first commit it or explicitly include it in the goal's
current-checkout scope. Never pretend uncommitted work followed a new worktree.

Each active goal has its own task record. Compare paths and shared interfaces before
running goals together. Serialize overlapping work. Worktrees isolate files and indexes;
they do not prevent semantic conflicts.

Stage named paths only. Preserve unrelated owner work. Do not reset, stash, amend, or
delete work to recover from a failed GLBuilding step. Record the current state and stop
as `blocked` when safe continuation is unclear.

Local Git commits persist only in that clone. Cross-host or public persistence requires
normal repository synchronization and fresh owner approval for the remote action.

## 7. Owner decisions and external actions

Routine work inside the approved goal can read, edit, check, create a branch or worktree,
and create a local commit under project policy.

Stop and ask the owner before:

- a major scope or architecture choice not settled by acceptance criteria;
- push, pull-request creation, merge, deploy, publish, or release;
- force operations, remote deletion, secret changes, or destructive data changes;
- a new external service, paid resource, or hard-to-reverse effect.

Only an owner-approved Configurer proposal can change project configuration, custom
instructions, or distilled role evolutions. Never change an active goal's rules in place.

Ambient skills, memory, and host setup can help locate evidence. They do not grant
authority or replace current repository checks. PROJECT and current repository evidence
remain the project sources of truth. GLBuilding does not manage the host's ambient setup.
