# Install and onboard Olympus

Give this guide to a Codex or Claude session in the target repository. Installation adds
Markdown configuration and loader blocks only. Use the [guided onboarding contract](../references/ONBOARDING.md)
for the complete owner conversation, exact proposal, stage evidence, and reports. The
[canonical activation preflight](../references/PROTOCOL.md#canonical-activation-preflight)
owns wake and activation classification, target identity captures, and the immediate recheck. The
[System Configurer charter](../agents/SYSTEM_CONFIGURER.md), [PROJECT template](../templates/PROJECT.md),
and [BOOTSTRAP template](../templates/BOOTSTRAP.md) retain the role, project, and loader
contracts.

The preflight classifies the target as `missing`, `partial`, `malformed`, or `complete`,
and re-reads the target immediately before any activation. A difference between the two
reads is `changed`: discard the result and run a fresh preflight. A changed result does
not route Configurer or report a candidate state.

## Owner instruction

Replace the placeholders and send:

```text
Onboard this Git repository with Olympus from <repository-url> at exact commit
<full-commit>. Read docs/INSTALLATION.md from that version. Inspect and propose the
complete project configuration and file changes. Do not write until I approve that
proposal. Preserve existing project instructions. Do not start another orchestration
flow for this request. For an unchanged proposal, reply exactly `Awaken Olympus` for the
second opt-in.
```

Use a full commit, not a branch, tag, `main`, or `latest`.

## Preconditions

- The target is a Git repository with a committed base and no staged owner changes.
- Existing `AGENTS.md`, `CLAUDE.md`, and `.olympus/PROJECT.md` paths are clean relative
  to `HEAD`; absent paths are allowed and unrelated unstaged paths can remain.
- The request supplies a framework repository URL and full commit, or identifies the
  missing source value that the guided flow must request.
- The agent can read both repositories and run Git.
- The harness has a role-specific mapping for every role the goal invokes, including a
  separate Builder and fresh Reviewer for mutation goals.
- Official configuration requires a System Configurer mapping and a fresh Reviewer
  mapping for the exact configuration unit.

## Onboarding

The owner request is opt-in one. Follow this order and the guided onboarding contract:

1. Run the [canonical activation preflight](../references/PROTOCOL.md#canonical-activation-preflight)
   first. Resolve and record the exact URL and full commit. An unresolvable, mismatched,
   unreadable, or dirty pin is `malformed`: stop with the exact evidence.
2. Inspect read-only. Do not ask before inspection and do not dump raw discovery
   output.
3. Use documented safe defaults when they decide the choice. Ask at most one unresolved
   material question per turn, with `Recommendation:` and exact `Effect:`. If the URL or
   full commit is missing, ask only for the missing source value or values.
4. When no material question remains, generate the complete proposal, then send one
   `## Ready to awaken Olympus` message with the compact approval surface of at most 12
   nonblank Markdown lines. It names what was found, framework version and short pin,
   boot mode, validation, changed files, and the local-only/no-remote boundary.
5. Offer `Show details` for the exact PROJECT bytes, both loader diffs, mappings, paths,
   gates, conflicts, and commit plan. Offer `Change settings` only for real
   owner-configurable settings.
6. Reply `Awaken Olympus` to approve that unchanged complete proposal. This is opt-in
   two. A changed proposal needs a new second opt-in.
7. Run the six stages in the canonical contract. Do not write before opt-in two. Stop on
   a changed path, unsupported mapping, failed evidence, review repair, or blocked gate.

## Defaults

If the repository does not decide, use `manual` boot, the exact owner-supplied pin,
repository-derived Map and Validation, review cap `2`, a current checkout/branch for
clean sequential work, and a worktree for concurrent or unrelated dirty work. Commit or
explicitly include relevant dirty work. Require fresh approval for major or external
actions. Use existing host-default models and tools unless a required role is unavailable.
Tools alone are `untested`; record `supported` only after the required mapping and behavior
pass at the pinned commit. A clean repository with both source values reaches the approval
surface without a question.

## Persist locally

Use normal project Git commands:

1. Apply only the approved installation content without a commit.
2. Inspect the exact uncommitted `PROJECT.md` plus managed-loader unit.
3. The Configurer returns that unit only to the Orchestrator. The Orchestrator runs a fresh
   Reviewer over it and stops on `repair` or `blocked`.
4. The Orchestrator returns a passing verdict to the Configurer.
5. The Configurer stages only the approved installation paths.
6. The Configurer runs normal project hooks and commits with `Configure Olympus` or
   `Update Olympus configuration`.
7. The Configurer returns the exact committed unit, commit, and hook evidence only to the
   Orchestrator. If a hook changed reviewed content, the Orchestrator runs a fresh review
   of that exact committed unit.
8. The Configurer confirms the committed content matches the approved proposal and returns
   the commit and remaining worktree state to the Orchestrator.

Do not reset, stash, bypass hooks, change Git identity, or include unrelated files. If
the commit fails, report the Git error and current state. A push, pull request, merge,
release, or other remote action needs fresh owner approval.

## Wake and activation preflight

Before `Use Olympus for: <goal>`, `Activate Olympus orchestration`, project boot, or a
guided wake, run the read-only [canonical activation preflight](../references/PROTOCOL.md#canonical-activation-preflight)
against the target repository root. It owns the ordered state classifier and the final
recheck; this guide does not duplicate those rules. No goal, session route, project
route, or active claim starts before a `complete` state and its recheck authorize it.
Missing state enters guided onboarding. Partial or malformed state stops with exact
evidence. A repository change after the recheck is next-entry state.

Project boot order is exact pin resolution, pinned `SKILL.md` and `references/PROTOCOL.md`
reads, preflight, immediate final recheck, then route. Boot mode never routes first.

`Awaken Olympus`, with or without a final period, is a guided entry, never a
session-activation alias. Missing state starts inspection; complete state reports
verified readiness and owner choices; an unchanged proposal accepts the phrase as opt-in
two. See the
[focused Issue #8 fixtures](CONFORMANCE.md#c19--issue-8-activation-preflight-and-progressive-onboarding) for
bounded static and behavioral coverage. These fixtures are not runtime harness results.

## Activation

Manual goal:

```text
Use Olympus for: <goal>
```

The preflight must return an unchanged complete state before this starts one goal.

Session orchestration:

```text
Activate Olympus orchestration
```

The preflight must return an unchanged complete state before this starts session routing.

Later project-changing requests become goals until session end or:

```text
Deactivate Olympus orchestration
```

Project orchestration sets PROJECT boot mode to `orchestration` through an approved
Configurer change. The preflight must return an unchanged complete state before each
session starts project routing. Questions do not create goals.

## Update or remove

Use the System Configurer. It must show the complete effective configuration and exact
affected loader changes, then wait for owner approval. Updates affect new goals only.
For removal, preserve task history unless the owner explicitly approves deletion, and
report every removed path and whether Git can recover it.

## Persistence limit

Git-tracked configuration survives only where repository history is available. Do not
claim cross-host continuity until the project uses its normal approved remote flow.
