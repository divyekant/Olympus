# GLBuilding runtime protocol

This is the shared contract for every GLBuilding goal. It is intentionally small.

## 1. Fixed system

GLBuilding has five roles:

| Role | Responsibility |
| --- | --- |
| Orchestrator | Owns routing, task records, Git isolation, and owner escalation. |
| System Configurer | Onboards the project and applies approved configuration changes. |
| Explorer | Answers one bounded repository question without edits. |
| Builder | Makes the approved project change and runs relevant checks. |
| Reviewer | Reviews the complete change in a fresh context. |

The Orchestrator is the hub. Worker roles receive bounded packets and return results to
it. They do not talk to each other, change the graph, or modify the framework revision
that governs the active goal.

For GLBuilding dogfood only, immutable revision A can govern a goal that edits a separate
target checkout for prospective revision B. The goal never reloads its own in-progress
changes as instructions.

Only the Configurer changes `.glbuilding/PROJECT.md` or the managed loader blocks. Only
the Orchestrator writes `.glbuilding/tasks/<goal-id>.md`. Only Builder changes approved
target-project paths.

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
Intent, Map, Validation, boundaries, role preferences, and approved custom instructions.

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
change protected paths, or grant standing authority for external actions.

Intent is owner direction. Map locates relevant code and documentation. Validation lists
commands and evidence sources. Map and Validation are hints until checked against current
code. Missing or stale documentation is a project risk, not a reason to invent facts.

Configuration uses double opt-in: the owner requests configuration, then approves the
complete effective configuration and exact loader changes. Apply only the approved paths
with normal project Git commands. Configuration changes affect new goals only.

## 4. Goal flow

For each goal, the Orchestrator creates one task record with:

- the request, acceptance criteria, non-goals, and allowed paths;
- framework commit, PROJECT revision, and source base;
- branch or worktree choice;
- owner decisions, role results, checks, and final status.

Use these states: `planned`, `active`, `reviewing`, `complete`, `blocked`, or `cancelled`.

Then:

1. Decide whether the goal is clear enough to build.
2. Use Explorer only for a material unresolved repository question.
3. Start a separate Builder with the bounded task packet.
4. Collect the Builder diff and check results.
5. Start a fresh Reviewer that did not build the change.
6. On `repair`, send only the findings and current task packet back to Builder.
7. Start a fresh final review after each repair. Stop at the configured round cap.
8. On `pass`, run the final relevant checks and record the result.
9. Use the project's normal local Git process when the goal includes a commit.
10. If commit hooks changed reviewed project content, run a fresh review of the committed
    result before completion.

A Reviewer `pass` must state how each acceptance criterion was checked. Unknown or
skipped evidence stays visible. It does not become a passing claim.

If a harness cannot start a separate Builder and fresh Reviewer, mark that harness
`unsupported`. Do not add hashes, transcript analysis, or other proof systems to
compensate for a host that ignores the contract.

## 5. Bounded handoffs

Every packet contains only the information needed by the receiving role.

- Configurer receives the owner request, project evidence, and configuration template.
- Explorer receives one question, path scope, revision, and relevant documentation.
- Builder receives the goal, acceptance criteria, allowed paths, accepted evidence, and
  validation commands.
- Reviewer receives the same goal boundary, complete diff, and Builder check results.

Packets can narrow scope or add evidence. They cannot widen authority. The Orchestrator
records accepted results in the task record. Whole conversations are not task state.

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
