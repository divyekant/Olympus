# Install and onboard GLBuilding

Give this guide to a Codex or Claude session in the target repository. Installation adds
Markdown configuration and loader blocks only. Use the [System Configurer charter](../agents/SYSTEM_CONFIGURER.md),
[PROJECT template](../templates/PROJECT.md), and [BOOTSTRAP template](../templates/BOOTSTRAP.md)
for the detailed role and loader contracts.

## Owner instruction

Replace the placeholders and send:

```text
Onboard this Git repository with GLBuilding from <repository-url> at exact commit
<full-commit>. Read docs/INSTALLATION.md from that version. Inspect and propose the
complete project configuration and file changes. Do not write until I approve that
proposal. Preserve existing project instructions. Do not start another orchestration
flow for this request.
```

Use a full commit, not a branch, tag, `main`, or `latest`.

## Preconditions

- The target is a Git repository with a committed base and no staged owner changes.
- Existing `AGENTS.md`, `CLAUDE.md`, and `.glbuilding/PROJECT.md` paths are clean relative
  to `HEAD`; absent paths are allowed and unrelated unstaged paths can remain.
- The owner supplied a framework repository URL and full commit.
- The agent can read both repositories and run Git.
- The harness has a role-specific mapping for every role the goal invokes, including a
  separate Builder and fresh Reviewer for mutation goals.
- Official configuration requires a System Configurer mapping and a fresh Reviewer
  mapping for the exact configuration unit.

## Onboarding

The owner request is the first opt-in. Approval of the complete proposal is the second.

1. Resolve the exact framework commit. Use a clean existing checkout only when its source and
   `HEAD` match the request. Otherwise fetch or clone that commit into a local cache.
   Stop if the commit is unavailable or unreadable. The pin identifies content, not trust.
2. Inspect existing `AGENTS.md`, `CLAUDE.md`, `.glbuilding/PROJECT.md`, project maps,
   validation commands, Git conventions, role-specific mappings, and design-standard
   sources. Derive the smallest useful Intent, Map, Validation, boundaries, exact role
   preferences, harness evidence, and matching details. Ask only unresolved questions
   about intent, boot mode, or authority.
3. Show the complete proposed PROJECT, exact managed loader changes, every changed path,
   conflicts, rejected custom settings, planned local commit, and no remote action.
4. Wait for explicit owner approval of that complete proposal. This is the second opt-in.
5. Recheck affected paths. Stop if they changed, or if markers are malformed, duplicate,
   nested, or incomplete. Apply only `.glbuilding/PROJECT.md` and the managed blocks in
   root `AGENTS.md` and `CLAUDE.md`; preserve all other content.
6. Validate the pin, boot mode, PROJECT, every invoked role mapping, both loader blocks,
   and surrounding content.

If the repository does not decide, use `manual` boot, review cap `2`, a current
checkout/branch for clean sequential work, and a worktree for concurrent or unrelated
dirty work. Commit or explicitly include relevant dirty work. Require fresh approval for
major or external actions. Use host-default models and tools.

## Persist locally

Use normal project Git commands:

1. Apply only the approved installation content without a commit.
2. Inspect the exact uncommitted `PROJECT.md` plus managed-loader unit.
3. Run a fresh Reviewer over that unit. Stop on `repair` or `blocked`.
4. After a passing review, stage only the approved installation paths.
5. Run normal project hooks and commit with `Configure GLBuilding` or
   `Update GLBuilding configuration`.
6. If a hook changed reviewed content, run a fresh review of the committed content.
7. Confirm the committed content matches the approved proposal and report the commit and
   remaining worktree state.

Do not reset, stash, bypass hooks, change Git identity, or include unrelated files. If
the commit fails, report the Git error and current state. A push, pull request, merge,
release, or other remote action needs fresh owner approval.

## Activation

Manual goal:

```text
Use GLBuilding for: <goal>
```

Session orchestration:

```text
Activate GLBuilding orchestration
```

Later project-changing requests become goals until session end or:

```text
Deactivate GLBuilding orchestration
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
