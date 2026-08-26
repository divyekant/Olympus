# Install and onboard GLBuilding

This guide is designed to be given to a Codex or Claude session. It installs Markdown records and loader blocks only.

## Owner instruction

Replace the placeholders and send this from the target repository root:

```text
Onboard this Git repository with GLBuilding from <canonical-repository-url>
at exact commit <full-immutable-commit>. Read docs/INSTALLATION.md from that
exact commit. Inspect and propose only. Do not write until I approve the exact
effective configuration and exact patch.
```

Do not use a branch, tag, release name, `main`, or `latest` as the source identity.

## Preconditions

- The target is a Git repository.
- The target has a resolvable committed base.
- The agent can read the repository and run Git.
- The agent can reach the source or verify an existing local checkout.
- The owner supplied the canonical source URL and full commit.

If a precondition is missing, return `blocked`. Do not create a package dependency or installer script.

The owner instruction is the initial bootstrap. Before PROJECT and loader blocks exist,
it authorizes only verification of the supplied source, reading this guide, and running
the System Configurer. Normal loader rules apply after installation.

## Onboarding flow

### 1. Verify the framework source

Use an existing checkout only when its canonical origin and checked-out commit match the
owner instruction and Git status is empty, including staged and untracked changes.
Otherwise fetch a clean copy of the exact commit into a host cache. Never resolve a
moving reference.

If no verified checkout exists and the network is unavailable, return `blocked`. An exact commit proves content identity. It does not prove that the repository is trustworthy.

### 2. Inspect without edits

Read existing `AGENTS.md`, `CLAUDE.md`, `.glbuilding/PROJECT.md`, project documentation, build files, Git state, and current commands.

Derive the smallest useful Map and Validation proposal. Do not ask the owner to repeat facts available in the repository.

### 3. Ask only material questions

Ask about:

1. boot mode when the owner has not chosen it: `manual` or `orchestration`;
2. unresolved project intent that can change the configuration;
3. the proposed default delivery boundary when repository conventions do not settle it;
4. cross-host resume only when cloud continuity is required.

Use safe defaults in the proposal:

- review and repair cap: `2`;
- cross-host resume: `off`;
- remote and destructive actions: fresh approval for each action;
- advanced model, tool, budget, and evolution choices: unchanged or omitted;
- worktree: only for concurrency, relevant dirty state, or project policy.

### 4. Present one exact proposal

Show:

- the complete proposed `.glbuilding/PROJECT.md`;
- the exact `AGENTS.md` loader block;
- the exact `CLAUDE.md` loader block;
- existing file preimage hashes and expected postimage hashes;
- one proposal SHA-256 that binds the complete proposal, patch, paths, and file hashes;
- every path that will change;
- rejected custom instructions and the protected rule they conflict with;
- persistence and behavioral-enforcement limits;
- the config revision and owner approval text that will be recorded.

Do not write yet.

### 5. Obtain exact approval

The owner must approve the proposal identifier and its SHA-256. Approval of a summary,
an earlier revision, or a different digest is not approval.

No approval means no write.

### 6. Apply the approved patch

Recheck each preimage immediately before its write. Stop if any file changed.

Create or update only:

- `.glbuilding/PROJECT.md`;
- the GLBuilding sentinel block in root `AGENTS.md`;
- the GLBuilding sentinel block in root `CLAUDE.md`.

Preserve all content outside the sentinels. Reject duplicate, nested, incomplete, or malformed sentinels. Do not guess a repair.

### 7. Validate or recover

Confirm:

- both loaders find `.glbuilding/PROJECT.md`;
- PROJECT contains the approved canonical URL and full commit;
- the resolved framework checkout has that origin and commit;
- the effective instruction order has no protected conflict;
- the selected boot mode is valid;
- `.glbuilding/tasks/` can be created when the first goal starts;
- repository content outside the approved patch is unchanged.

If validation fails, restore a preimage only when the current file still matches the attempted postimage. If it changed again, preserve it and return `blocked` with the conflict. Never use a broad Git reset.

## Existing project instructions

The loader blocks are additive. They do not replace project instructions. Higher-priority host policies and existing project rules still apply.

If a project rule conflicts with the protected GLBuilding base, onboarding stops and identifies the exact conflict. The Configurer cannot silently choose a winner.

## Activation after onboarding

### Manual goal

```text
Use GLBuilding for: <goal>
```

Ownership ends when that goal reaches a terminal status.

### Session orchestration

```text
Activate GLBuilding orchestration
```

The agent acknowledges activation. Later project-changing requests become child goals. Completion of one goal does not deactivate routing.

```text
Deactivate GLBuilding orchestration
```

Deactivation stops routing new goals in this session. It does not cancel an active goal.

### Project orchestration

Set `boot mode: orchestration` through the System Configurer. Each new session loads
routing authority from PROJECT. Session deactivation lasts only for that session.

## Update

Ask the System Configurer to propose an update to a new canonical URL or commit. The proposal must show the source change, compatibility effect, exact PROJECT patch, full effective instructions, and new config revision.

An update never changes an active goal. Cancel or explicitly restart that goal if it must use the new revision.

## Remove

Ask the System Configurer to propose removal. After exact approval, remove only the two sentinel blocks and the named `.glbuilding` records. Preserve goal history if the owner wants an audit trail. Report exactly what was removed and whether Git can recover it.

## Cloud limit

Committed local state does not guarantee cross-host resume. Do not claim cloud continuity unless an approved checkpoint destination or tested persistent workspace is recorded in PROJECT.
