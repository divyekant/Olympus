# Install and onboard Olympus

Give this guide to a Codex or Claude session in the target repository. Installation adds
Markdown configuration and loader blocks only. Use the [guided onboarding contract](../references/ONBOARDING.md)
for the complete owner conversation, exact proposal, stage evidence, and reports. The
[System Configurer charter](../agents/SYSTEM_CONFIGURER.md), [PROJECT template](../templates/PROJECT.md),
and [BOOTSTRAP template](../templates/BOOTSTRAP.md) retain the role, project, and loader
contracts.

## Owner instruction

Replace the placeholders and send:

```text
Onboard this Git repository with Olympus from <repository-url> at exact commit
<full-commit>. Read docs/INSTALLATION.md from that version. Inspect and propose the
complete project configuration and file changes. Do not write until I approve that
proposal. Preserve existing project instructions. Do not start another orchestration
flow for this request.
```

Use a full commit, not a branch, tag, `main`, or `latest`.

## Preconditions

- The target is a Git repository with a committed base and no staged owner changes.
- Existing `AGENTS.md`, `CLAUDE.md`, and `.olympus/PROJECT.md` paths are clean relative
  to `HEAD`; absent paths are allowed and unrelated unstaged paths can remain.
- The owner supplied a framework repository URL and full commit.
- The agent can read both repositories and run Git.
- The harness has a role-specific mapping for every role the goal invokes, including a
  separate Builder and fresh Reviewer for mutation goals.
- Official configuration requires a System Configurer mapping and a fresh Reviewer
  mapping for the exact configuration unit.

## Onboarding

The owner request is opt-in one. Follow the guided onboarding contract after inspection:

1. Resolve the exact URL and full commit in a clean checkout or cache. Stop if it is
   unavailable, unreadable, mismatched, or dirty.
2. Inspect the target and show the concise, exact `## What I learned` summary. Do not
   ask a question before inspection.
3. Ask at most one unresolved material question per turn. Each question has a
   `Recommendation:` and a short exact `Effect:`. Apply documented defaults when they
   decide the choice.
4. When no material question remains, send one `## Ready to awaken Olympus` message with
   the complete exact PROJECT, both loader blocks, paths, preservation rule, conflicts,
   rejected settings, named-path commit, stages, mappings, evidence, and no remote action.
5. Wait for explicit approval of that complete current proposal. This is opt-in two.
6. Run the six stages in the canonical contract. Do not write before opt-in two. Stop on
   a changed path, unsupported mapping, failed evidence, review repair, or blocked gate.

## Defaults

If the repository does not decide, use `manual` boot, review cap `2`, a current
checkout/branch for clean sequential work, and a worktree for concurrent or unrelated
dirty work. Commit or explicitly include relevant dirty work. Require fresh approval for
major or external actions. Use host-default models and tools. Tools alone are `untested`;
record `supported` only after the required mapping and behavior pass at the pinned commit.

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

## Activation

Manual goal:

```text
Use Olympus for: <goal>
```

Session orchestration:

```text
Activate Olympus orchestration
```

Later project-changing requests become goals until session end or:

```text
Deactivate Olympus orchestration
```

Project orchestration sets PROJECT boot mode to `orchestration` through an approved
Configurer change. Questions do not create goals.

## Update or remove

Use the System Configurer. It must show the complete effective configuration and exact
affected loader changes, then wait for owner approval. Updates affect new goals only.
For removal, preserve task history unless the owner explicitly approves deletion, and
report every removed path and whether Git can recover it.

## Persistence limit

Git-tracked configuration survives only where repository history is available. Do not
claim cross-host continuity until the project uses its normal approved remote flow.
