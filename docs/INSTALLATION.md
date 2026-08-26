# Install and onboard GLBuilding

This guide is designed to be given to a Codex or Claude session. It installs Markdown records and loader blocks only.

## Owner instruction

Replace the placeholders and send this from the target repository root:

```text
Onboard this Git repository with GLBuilding from <canonical-repository-url>
at exact commit <full-immutable-commit>. Read docs/INSTALLATION.md from that
exact commit. Inspect and propose only. Do not write until I approve the exact
effective configuration and exact patch. Do not activate another onboarding,
design, or orchestration framework for this request. Ambient skills and memory
may supply evidence only. If a higher-priority host rule conflicts, stop and report it.
```

Do not use a branch, tag, release name, `main`, or `latest` as the source identity.

## Preconditions

- The target is a Git repository.
- The target has a resolvable committed base.
- The target `HEAD` is attached to a symbolic branch ref.
- The target Git status is empty, including staged and untracked changes.
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
- onboarding persistence: one local commit containing only the approved install paths;
- committed-goal persistence: one exact Git transaction; project hooks do not run;
- advanced model, tool, budget, and evolution choices: unchanged or omitted;
- worktree: only for concurrency, relevant dirty state, or project policy.

### 4. Present one exact proposal

Show:

- the complete proposed `.glbuilding/PROJECT.md` once, inside the full unified patch;
- the exact full unified patch for PROJECT and both loader blocks, with every changed
  or added line;
- existing file preimage hashes and expected postimage hashes;
- one canonical manifest starting with `GLBUILDING-PROPOSAL-V1`,
  `proposal=<identifier>`, `target-head=<full commit>`, and
  `target-ref=<refs/heads/name>`, then byte-sorted
  `<path><TAB><preimage><TAB><postimage>` rows;
- one SHA-256 over the UTF-8 manifest with LF endings and one final newline;
- every path that will change;
- rejected custom instructions and the protected rule they conflict with;
- persistence and behavioral-enforcement limits;
- the fixed `Configure GLBuilding` local commit result;
- the config revision and proposal metadata that will be recorded.

Do not write yet.

If the owner selects a committed goal branch, disclose that its exact finalization uses
Git plumbing without project commit hooks. If project rules require hooks or commit
signing, that delivery boundary is unavailable in version one.

Never abbreviate an artifact. Do not use a placeholder, omission marker, `as shown
above`, or ellipsis. If the host cannot present every approved byte, return `blocked`.
Do not ask for approval of an incomplete proposal.

Manifest paths are repository-relative POSIX paths. Hashes use 64 lowercase hex
characters. Use the literal `absent` for a missing preimage.

Do not put the digest, file hashes, or approval-time data inside PROJECT. PROJECT stores
only proposal metadata fixed before approval: identifier, proposal time, request
principal, binding limit, and conflicts. Keep later approval evidence in the returned
transaction packet.

### 5. Obtain exact approval

The owner must approve the proposal identifier and its SHA-256. Approval of a summary,
an earlier revision, a different digest, or an incomplete artifact is not approval.

No approval means no write.

### 6. Apply the approved patch

Recheck the target symbolic ref, full `HEAD`, and each preimage immediately before any
write. Stop if the ref, `HEAD`, or any file changed.

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

### 8. Persist the installation

Onboarding always creates one local configuration commit:

1. stage only the approved changed paths;
2. verify the complete index tree against the frozen target tree, changed-path set, and
   SHA-256 of each changed blob;
3. use Git `commit-tree` to create a commit from that exact tree with the fixed message
   `Configure GLBuilding`; project commit hooks do not run;
4. verify its tree, single parent, complete changed-path set, message, and blob hashes;
5. recheck the symbolic target ref;
6. advance that ref with an old-value check from the frozen `HEAD` to the verified commit;
7. check the target Git status; empty is expected.

Before ref advance, roll back only approved paths whose worktree and index bytes still
match their postimages. After a successful ref advance, preserve the exact commit and
any concurrent state. New dirty state then blocks activation but does not revoke the
configuration commit. Return `blocked` on any earlier mismatch. Do not reset or amend.
A later configuration commit uses the fixed message `Update GLBuilding configuration`.

If project rules require commit hooks for this metadata-only commit, return `blocked`
before the proposal. Do not silently bypass a higher-priority rule.

A local commit persists on that Git clone. It does not persist across an ephemeral host.
Push or pull-request creation still requires fresh owner approval.

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
