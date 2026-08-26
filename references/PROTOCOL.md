# GLBuilding Runtime Protocol

This is the Orchestrator contract for the fixed Markdown pack. Fresh roles receive only
their charter and a bounded packet.

## 1. Fixed control plane

- GLBuilding is an external, versioned Markdown pack. The target repository receives
  only owner-approved control records, bootstrap loader blocks, and ordinary goal changes.
- One active repository-root **Orchestrator** is the hub and the only role that
  writes semantic state to `.glbuilding/tasks/<goal-id>.md`.
- The Orchestrator may inspect Git and create the approved goal branch or worktree.
  It does not edit target-project paths; only the Builder does that.
- The fixed roles are **System Configurer**, **Explorer**, **Builder**, and **Reviewer**.
  The Orchestrator invokes them in fresh, bounded sessions.
- Roles do not talk peer-to-peer, spawn agents, edit task records, change the graph,
  or modify the external GLBuilding pack. They return scoped packets to the Orchestrator.
- The System Configurer is the only role that changes `.glbuilding/PROJECT.md` or
  the managed bootstrap blocks in `AGENTS.md` and `CLAUDE.md`.
- The Builder may change approved target-project paths, including goal-required scripts,
  dependencies, CLIs, and tests. Those are target work, not GLBuilding machinery.

## 2. Activation and graph ownership

- `boot mode` is exactly `manual` or `orchestration`.
- In `manual`, activate one goal with one explicit owner invocation.
- In any session, the owner command `Activate GLBuilding orchestration` temporarily
  activates routing until owner deactivation or session end.
- In `orchestration`, routing starts automatically for project-changing requests in
  every session. Session deactivation does not change the persisted boot mode.
- `Deactivate GLBuilding orchestration` stops routing new goals in that session. It
  does not cancel an active goal. A persistent mode change uses the Configurer.
- In an active orchestration session, a project-changing goal creates a bounded child
  graph under the root Orchestrator. A casual question creates no graph.
- An explicit read-only audit may invoke Explorer or Reviewer without mutation authority.
- There is one active root Orchestrator per repository. It may own child graphs for
  different goals, but a role never becomes a second root.
- Same-goal concurrent ownership is unsupported. If ownership, intent, or authority is
  ambiguous, stop as `blocked` until the owner explicitly takes over.

Before accepting a goal, scan all non-terminal task records. A different active root
identity blocks the goal. This is workflow coordination, not a distributed lock. If two
sessions can race and the host has no exclusive-create control, report that limit.

Before starting concurrent goals or integrating their results, compare their paths,
interfaces, migrations, and validation resources. Serialize any overlap. Worktrees
isolate files; they do not isolate orchestration ownership or approval state.

## 3. Framework source pin and bootstrap

- The canonical, owner-approved framework repository URL and its full immutable commit
  exist only in `.glbuilding/PROJECT.md`.
- Initial onboarding is the only exception. The owner's installation command supplies
  the exact URL and commit out of band. Verify that checkout, then load only the
  installation guide and System Configurer before PROJECT and loader files exist.
- A full immutable commit is a complete commit identifier, not a branch, tag, or short SHA.
- A loader reads that URL and commit, then checks a cached checkout's exact origin,
  `HEAD`, and clean status. The status must show no tracked, staged, or untracked change.
  If the cache is absent or mismatched, fetch that exact commit from the exact URL. Never
  fetch `latest`, `main`, or another floating reference.
- If Git, the source, the exact commit, the external pack, or the required loader block
  is unavailable or mismatched, stop as `blocked` before role work or project mutation.
- The source pin identifies the intended bytes but is not a security trust anchor. Host
  authentication, transport, and filesystem controls remain separate requirements.
- Use the exact managed sentinel block in [templates/BOOTSTRAP.md](../templates/BOOTSTRAP.md)
  in both target loader files. Stop on malformed, duplicate, or nested sentinels.

## 4. Project knowledge and instruction order

The Configurer derives these fields and records the evidence used:

- **Intent** is owner-approved direction. It is not proof of current behavior.
- **Map** is a structural map of the project and likely affected paths.
- **Validation** is a set of existing checks and likely evidence sources.
- Map and Validation are hints. Verify them at the frozen source revision before use.
- Memory and ambient skills are optional evidence. They are never authority. Surface any
  material conflict with the owner request, current files, or the frozen configuration.

Native host instruction precedence always applies. If a higher-priority or more-specific
host instruction conflicts with the fixed GLBuilding contract, block instead of claiming
that GLBuilding overrides it. Inside the GLBuilding configuration layer, resolve:

1. protected base rules in this protocol and the fixed role boundaries;
2. versioned GLBuilding defaults;
3. owner-approved, named custom additions or narrowing;
4. owner-approved, named evolutions;
5. task-specific narrowing in the goal record.

Custom and evolution fields must name their scope. They cannot remove role duties or
change topology, ownership, authority, review independence, or protected paths. Show the
complete effective result before owner approval. Configuration and evolution changes
apply only to new goals; restart an active goal to use them.

## 5. Goal record and stage packets

For each goal, the Orchestrator creates `.glbuilding/tasks/<goal-id>.md` from
[templates/TASK.md](../templates/TASK.md). Before any role runs, the record freezes:

- framework URL and full commit;
- project configuration revision;
- committed base identity and dirty-base decision;
- goal identity, acceptance criteria, scope, and non-goals;
- maximum capability envelope and harness enforcement labels;
- branch and worktree identity;
- attempt number and root Orchestrator identity;
- delivery boundary and required owner approvals.

A stage packet may only narrow the frozen authority or add accepted evidence and findings.
It cannot widen scope, capabilities, delivery authority, topology, or protected-path rules.
The Orchestrator alone merges accepted packets into the task record.

Every capability uses one label: `native-enforced`, `workflow-instructed`, or
`unavailable`. The first is host-enforced. The second is a behavioral instruction. The
third blocks only a path that requires it. Fresh means no parent or Builder task
conversation is supplied; higher-priority ambient host context can remain.

## 6. States, verdicts, and recovery

Valid task states are:

`planned`, `exploring`, `building`, `reviewing`, `repairing`, `complete`, `blocked`,
`failed`, and `cancelled`.

Only `complete`, `blocked`, `failed`, and `cancelled` are terminal. Record every state
change with its actor, time, reason, source identity, and checkpoint. Do not continue a
terminal task.

- `planned -> exploring` is optional and is used only when a question needs Explorer.
- `planned -> reviewing` is allowed for an explicit read-only review.
- `exploring -> complete` is allowed for a read-only evidence goal after final verification.
- `exploring -> reviewing` is allowed when a read-only audit needs independent review.
- `exploring -> building` requires accepted evidence. A simple goal may go directly
  from `planned` to `building`.
- `building -> reviewing` requires the Builder diff and verification packet.
- `reviewing -> complete` requires a fresh Reviewer `pass` and final verification.
- `reviewing -> repairing` requires a fresh Reviewer `repair` finding.
- `repairing -> reviewing` requires a Builder repair packet and a new fresh Reviewer.
- `failed` and `cancelled` can be reached from any non-terminal state.
- Any unavailable capability, missing approval, scope conflict, stale identity, or
  unsafe recovery is `blocked`; an execution error that prevents a safe result is `failed`.

Reviewer verdicts are exactly `pass`, `repair`, or `blocked`. `unknown` never passes.
The review/repair cap defaults to `2`; allowed values are `1`, `2`, or `3`. A repair at
the cap becomes `blocked`. Every recheck starts fresh and reviews the whole current unit.

- **Resume:** after interruption, resume a non-terminal goal only after re-reading its
  record and confirming the same frozen source, base, branch, worktree, attempt, and
  capability envelope. Do not resume across configuration or evolution changes.
- **Retry:** after a failed or blocked goal, retry only after the recorded cause is
  resolved and the owner permits it. Keep the terminal record unchanged. Create a new
  `<goal-id>-attempt-<n>.md` record that links to it, increments `attempt`, and freezes
  the current base and capabilities.
- **Takeover:** for a non-terminal goal, the owner may explicitly assign a new root
  Orchestrator. Preserve the initial root identity and history, append the new active
  root identity, stop concurrent ownership, and revalidate the same-goal freeze.
- **Cancel:** the owner may set `cancelled`. Stop role work and mutation, retain evidence,
  and do not silently restart it.

## 7. Persistence and Git isolation

- Tracked local Git records are local persistence only. They do not promise cloud resume.
- Cross-host resume is off unless `PROJECT.md` explicitly says `harness-persistent workspace`
  or contains an owner-approved remote checkpoint contract.
- A simple, single goal may use the current clean checkout.
- Concurrent goals or relevant dirty state require separate worktrees based on a committed
  base. Relevant dirty state requires an exact named snapshot approved by the owner;
  otherwise block.
- Freeze branch, worktree path or identity, committed base, and snapshot name in the task.
- Check for concurrent drift before mutation, review, integration, and recovery. Do not
  merge or integrate overlapping work until the Orchestrator serializes it.

## 8. Delivery and action boundary

The v1 action boundary permits routine in-scope read, edit, check, worktree setup, and
local commit after the goal freeze. This baseline applies unless a later owner-approved
framework revision changes it. Project instructions cannot widen it.

Every push, pull request creation, merge, deploy, publish, force operation, secret change,
remote deletion, or other hard-to-reverse external effect requires fresh owner approval
at the point of action. Record the exact command or effect, target, owner, timestamp, and
approval in the task. A custom instruction cannot preauthorize these effects.
