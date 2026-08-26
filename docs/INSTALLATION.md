# Install and onboard GLBuilding

Give this guide to a Codex or Claude session in the target repository. Installation adds
Markdown configuration and loader blocks only.

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

- The target is a Git repository with a committed base.
- The Git index has no staged owner changes.
- Existing `AGENTS.md`, `CLAUDE.md`, and `.glbuilding/PROJECT.md` paths are clean relative
  to `HEAD`. Absent paths are allowed. Unrelated unstaged paths can remain.
- The owner supplied a framework repository URL and full commit.
- The agent can read both repositories and run Git.
- The harness can run a separate Builder and fresh Reviewer for mutation goals.

## Onboarding flow

### 1. Resolve the framework

Use a clean existing checkout only when its source and `HEAD` match the owner request.
Otherwise fetch or clone the exact commit into a local cache. Stop if it cannot be read.

The commit identifies the intended framework content. It does not prove that the source
is trusted.

### 2. Inspect the project

Use the System Configurer. Read:

- existing root `AGENTS.md` and `CLAUDE.md`;
- existing `.glbuilding/PROJECT.md`, if present;
- project documentation and codebase maps;
- build, test, lint, and validation commands;
- Git state and branch or worktree conventions;
- available Codex and Claude role mappings.

Derive the smallest useful Intent, Map, Validation, boundaries, and role preferences.
Do not ask the owner for facts that the repository already supplies. Record missing or
stale documentation as a limit.

### 3. Ask only material questions

Ask about:

1. boot mode when it is not known: `manual` or `orchestration`;
2. unresolved project intent or protected areas;
3. a major local Git policy choice that project instructions do not settle;

Use these defaults when the repository does not decide them:

- boot mode: `manual`;
- review round cap: `2`;
- current checkout for one clean goal;
- branch for clean sequential work; worktree for concurrent work, unrelated dirty state,
  or policy isolation;
- commit relevant dirty work first, or explicitly include it in the current-checkout goal;
- fresh owner approval for every major or external action;
- host-default models and tools.

### 4. Present one proposal

Show:

- the complete proposed `.glbuilding/PROJECT.md`;
- the exact managed block changes for root `AGENTS.md` and `CLAUDE.md`;
- every path that will change;
- existing instruction conflicts and rejected custom settings;
- the planned local commit and the fact that no remote action is included.

Do not write yet. This is the first opt-in result.

### 5. Obtain approval

Wait for the owner to approve the displayed configuration and changes. A summary-only
approval does not cover hidden changes. No approval means no write.

### 6. Apply and validate

Recheck the affected paths. Stop if they changed after the proposal.

Create or update only:

- `.glbuilding/PROJECT.md`;
- the managed GLBuilding block in root `AGENTS.md`;
- the managed GLBuilding block in root `CLAUDE.md`.

Preserve all content outside the managed blocks. Stop on malformed, duplicate, nested,
or incomplete markers.

Confirm that PROJECT uses the approved source, commit, boot mode, boundaries, and role
settings. Confirm both loaders have one complete block and resolve that source version.

### 7. Persist locally

Use normal project Git commands:

1. stage only the changed installation paths;
2. inspect the complete staged diff and path list;
3. run applicable project hooks through the normal commit process;
4. commit with `Configure GLBuilding` or `Update GLBuilding configuration`;
5. confirm the committed installation content still matches the approved result;
6. report the commit and remaining working-tree state.

Do not bypass project hooks or change Git identity settings. If the commit fails, report
the normal Git error and current state. Do not reset, stash, or include unrelated files.

The local commit persists in that clone. A push, pull request, merge, or release needs
fresh owner approval.

## Activation

### Manual goal

```text
Use GLBuilding for: <goal>
```

### Session orchestration

```text
Activate GLBuilding orchestration
```

Later project-changing requests become goals until session end or:

```text
Deactivate GLBuilding orchestration
```

### Project orchestration

Set PROJECT boot mode to `orchestration` through an approved Configurer change.

## Update or remove

Use the System Configurer. It must show the complete new configuration and exact affected
loader changes, then wait for owner approval. An update affects new goals only.

For removal, preserve task history unless the owner explicitly approves its deletion.
Report every removed path and whether Git can recover it.

## Persistence limit

Git-tracked configuration survives only where the repository history is available. Do
not claim cross-host continuity until the project uses its normal approved remote flow.
