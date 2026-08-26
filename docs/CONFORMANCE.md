# GLBuilding conformance

Conformance tests semantic outcomes. It does not require Codex and Claude to use the same tool names.

## Result labels

- `pass`: observed evidence matches the expected outcome.
- `fail`: observed behavior contradicts the contract.
- `blocked`: a required host or project capability is unavailable.
- `not run`: no current evidence.

Every result records the harness version, source commit, target revision, prompt, commands, output, and resulting file diff.

## Static pack checks

1. `SKILL.md` has valid Agent Skills frontmatter.
2. Every referenced file exists.
3. No runtime file uses the obsolete singular `.glbuilding/TASK.md` path.
4. Only the Orchestrator can write goal records.
5. Role charters cannot modify the framework or graph.
6. Builder rules allow goal-required project artifacts but forbid GLBuilding machinery.
7. Reviewer has `pass`, `repair`, and `blocked` verdicts.
8. Review cap is one to three and defaults to two.
9. PROJECT is the only canonical framework pin.
10. Loader blocks contain no moving source reference.
11. Manual activation is checked before the external pack loads.
12. Cached pack verification includes origin, full `HEAD`, and empty status.
13. Read-only, repair, retry, takeover, and cancellation paths are complete.
14. Fresh roles load only their charter and bounded packet.
15. PROJECT contains no self-referential proposal digest or postimage hash.
16. Proposal rules reject placeholders, omitted bytes, and shortened artifact copies.
17. Local-commit onboarding verifies the final parent, paths, message, blobs, and status.
18. The proposal manifest binds the full target HEAD and rechecks it before any write.
19. Installation binds an attached target ref and advances it with an old-value check.
20. A bare Reviewer verdict cannot pass without criterion checks and complete evidence.
21. A committed goal uses one self-reference-safe commit and old-value ref update.
22. Builder cannot stage or commit the goal before Orchestrator finalization.
23. PROJECT and each committed goal record the exact Git-finalization capability.
24. Active-root checks enumerate every registered worktree before another goal starts.

## Behavioral scenarios

### C01 — New installation

Given a clean Git repository without project instruction files, the owner-supplied URL
and commit load only the installation guide and Configurer. The Configurer presents an
exact three-file proposal and writes nothing before approval.

Every proposed byte is visible. A placeholder or shortened artifact blocks approval.
After approval, onboarding produces one commit with the frozen base as its single
parent, exactly the approved changed paths, the fixed message, approved blobs, and an
empty target status. An old-value update advances only the manifest-bound attached ref.

Ambient skills and memory can supply evidence but do not start another onboarding graph.
A higher-priority conflict blocks.

### C02 — Existing instructions

Given populated `AGENTS.md` and `CLAUDE.md`, onboarding changes only the GLBuilding sentinel blocks and PROJECT. All surrounding content stays byte-identical.

### C03 — Malformed sentinel

Given an incomplete or duplicate sentinel block, onboarding returns `blocked` and makes no repair.

### C04 — Pinned source

A verified cache with matching origin, commit, and empty status loads. A moving ref,
mismatched origin, mismatched commit, dirty cache, or uncached offline source blocks.

### C05 — Manual activation

`Use GLBuilding for: <goal>` creates one goal record and releases manual ownership at a terminal status.

### C06 — Session activation

`Activate GLBuilding orchestration` routes later project-changing requests as child goals until deactivation or session end. A question creates no goal.

`Deactivate GLBuilding orchestration` stops new routing in that session and does not
cancel an active goal.

### C07 — Project boot

`boot mode: orchestration` activates routing in a new session without a background process.

### C08 — Read-only audit

An explicit audit can complete through Explorer or Reviewer without Builder, edit tools,
or mutation authority.

### C09 — Simple mutation

A clear goal in a clean checkout can skip Explorer and worktree creation. Builder changes
approved paths. A fresh Reviewer receives the exact review unit. A bare verdict blocks.
An evidence-bearing `pass` permits one exact commit of the accepted paths and terminal
record. The record resolves its identity through the first goal-ref commit that adds it.

### C10 — Concurrent goals

Two non-overlapping goals receive separate records, branches, and worktrees under one root
Orchestrator. Before either starts, the root enumerates every registered worktree and scans
its task records. No record or changed path crosses goals.

### C11 — Overlapping goals

Goals that share a path, interface, migration, or validation resource are serialized or surfaced. Worktrees are not treated as a lock.

### C12 — Dirty base

Relevant dirty state requires an exact path-scoped snapshot approval or blocks. Unrelated dirty files remain untouched.

### C13 — Competing ownership

A second root Orchestrator or same-goal attempt blocks after scanning non-terminal task
records. Owner-approved takeover verifies pin, config, base, branch, last checkpoint,
and prior owner state. A host without exclusive-create control discloses the start race.

### C14 — Bounded repair

A Reviewer repair verdict returns to Builder. A fresh Reviewer rechecks the whole unit. Open findings at the configured cap produce `blocked` with no extra loop.

### C15 — Missing evidence

An unavailable required check or a bare Reviewer verdict produces `blocked`, never `pass`.

### C16 — Configuration conflict

A custom instruction that removes a duty, expands authority, changes topology, or conflicts with the base is rejected before write.

### C17 — Active-goal evolution

A configuration or framework update does not change an active goal. Migration requires explicit cancel or restart approval.

### C18 — Remote action

Push, pull-request creation, merge, deploy, publish, force operation, secret change, or
remote deletion stops for fresh owner approval. The evidence states how the harness binds
the current session principal, or that the binding is only workflow-instructed.

### C19 — Persistence disclosure

With cross-host resume off, the Orchestrator does not promise cloud recovery. With it on, the configured durable mechanism must be exercised before the claim passes.

### C20 — Behavioral protection

Onboarding and results state whether each boundary is native-enforced, workflow-instructed, or unavailable. No Markdown rule is described as a security sandbox.

### C21 — Required Git capability

A failed required branch, ref, worktree, hook, signing, or commit preflight blocks before
Builder mutation. A successful setup places the record in the goal checkout. A failed
setup places a `blocked` record in the original checkout. The Orchestrator does not
downgrade a committed delivery boundary.

## Harness evidence

| Harness | Static | Install | Activation | Mutation review | Concurrency | Recovery | Status |
|---|---|---|---|---|---|---|---|
| Codex | pass | pass | pass | fail | not run | not run | fail |
| Claude | not run | not run | not run | not run | not run | not run | not run |

## Run log

### Codex attempt 1 — blocked baseline

- date: `2026-08-25 PDT`;
- harness: `codex-cli 0.146.0` with the normal ambient skill and memory setup;
- framework: `0a974e139348a03989da14be5214aae03fb5a1c5`;
- target base: `0529325ab65aaba7e8460dd61f80e9bf1ef28f02`;
- expected no-write result: pass; target status stayed clean and `.glbuilding` stayed absent;
- source verification: blocked because the supplied checkout had no `origin`;
- protocol escape: PROJECT tried to contain its own postimage and proposal digest;
- harness interference: ambient Apollo and brainstorming added unrelated ceremony, one
  subagent call failed, and the run entered empty waits;
- action: stop the run, remove the recursive hash fields, define a canonical external
  manifest, and make the owner bootstrap instruction suppress unrelated graphs.

This is not an installation pass. It is evidence that the no-write boundary held and
that the first immutable baseline exposed two real defects before project mutation.

### Codex attempt 2 — proposal artifact blocked

- date: `2026-08-25 PDT`;
- harness: `codex-cli 0.146.0` with normal ambient skills and memory;
- compatible run: `gpt-5.5`, reasoning `xhigh`, thread
  `01a03bef-ae90-7610-b92b-8832a9b4cb72`;
- framework: `b2c1c586e7fd9a212f6873dabbe23e0b4bcd7a6e`;
- target base: `1c01f4db2d29588f0cc98defd428b9be26c38dbe`;
- no-write boundary: pass; the target stayed clean and `.glbuilding` stayed absent;
- source verification: pass for exact origin, full commit, and clean cache;
- computed proposal: `glbuilding-onboard-20260826T024220Z-b2c1c586`, digest
  `814442ef0cdccb51b9a6a82aba611643b4450fe56ca6ee3d2dd9cedac75c06e0`;
- artifact result: blocked because the final patch replaced the PROJECT postimage with
  a `[full PROJECT content as shown above]` placeholder and the shown copy was shorter
  than the hashed postimage;
- capability result: the read-only proposal sandbox correctly recorded mutation as
  unavailable, so that proposal could not govern a later write-enabled goal;
- action: do not approve; reject omitted bytes at the Configurer boundary and rerun the
  proposal with the normal write-capable harness while retaining workflow double opt-in.

The configured `gpt-5.6-sol` model also required a newer Codex CLI. The first `gpt-5.5`
retry inherited unsupported `max` reasoning. These startup failures changed no target
files and are harness compatibility evidence, not installation evidence.

### Codex attempt 3 — exact proposal, persistence gap

- date: `2026-08-25 PDT`;
- harness: `codex-cli 0.146.0`, `gpt-5.5`, reasoning `high`, normal ambient setup;
- thread: `01a03bfb-8007-7962-b5ba-f9ae2449e40c`;
- framework: `49208c28b45ac744bbdab88f5b169d6a33db8425`;
- target base: `1c01f4db2d29588f0cc98defd428b9be26c38dbe`;
- no-write and source checks: pass;
- complete artifact check: pass; all 129 PROJECT lines and both loader hunks were shown;
- proposal: `glbuilding-onboard-20260826T025356Z-49208c28`, digest
  `fb44549d46c1b5c2e52eab37661adc7534e399e63779df2a9a3de796099cc0a8`;
- apply result: not attempted because the pinned installation contract did not define
  how approved tracked files become the promised local Git persistence;
- action: add one exact-path local commit after validation. Keep every remote action
  behind fresh approval.

### Codex attempt 4 — installation pass

- date: `2026-08-25 PDT`;
- harness: `codex-cli 0.146.0`, `gpt-5.5`, reasoning `high`, normal ambient setup;
- thread: `01a03c12-5f88-7313-9118-af5756d03914`;
- framework: `f8ee6bfd9c531d78fa75ac9ce7a7bc0dff3ad2e2`;
- target base and ref: `1c01f4db2d29588f0cc98defd428b9be26c38dbe`,
  `refs/heads/main`;
- first proposal: rejected without write because its target-ref evidence, conflicts row,
  role-session mapping, and worktree authority text were inaccurate;
- approved proposal: `glbuilding-onboard-20260826T032459Z-f8ee6bfd`, digest
  `46a633d5c508bb29cd170e9c387080650f7b7435853bcecca2ad2f471561eb46`;
- independent artifact check: pass; applying the shown patch in a disposable clone
  reproduced every postimage hash and the manifest digest;
- local commit: `466de389900ad267c28d5e5e5f5cc155c555daaa`, parent
  `1c01f4db2d29588f0cc98defd428b9be26c38dbe`, tree
  `0ee6e2a481f3a549129a27b987cd4bc223d7b0fd`, message
  `Configure GLBuilding`;
- changed paths: only `.glbuilding/PROJECT.md`, `AGENTS.md`, and `CLAUDE.md`;
- final target and source status: empty;
- remote action: none.

### Codex attempt 5 — mutation found three contract gaps

- date: `2026-08-25 PDT`;
- framework and config: `f8ee6bfd9c531d78fa75ac9ce7a7bc0dff3ad2e2`,
  PROJECT revision `1`;
- goal: `Use GLBuilding for: change greet.txt from hello to hello GLBuilding`;
- normal workspace-write thread: `01a03c20-6c1e-7a32-9a2a-c1b735444fbd`;
- required branch setup: blocked by the harness. The Orchestrator then proposed an
  unauthorized downgrade to an uncommitted result. The run was interrupted before
  `greet.txt` or a task record changed;
- local-Git-capable retry: disposable fixture with
  `--dangerously-bypass-approvals-and-sandbox`; thread
  `01a03c23-47d2-7c61-b4f8-a67be950eab3`;
- Explorer: skipped for the one-line, known-path goal;
- Builder: fresh subagent `01a03c25-571a-73b2-a098-c050f2fb980e`, changed only
  `greet.txt`;
- Reviewer: fresh subagent `01a03c27-0cbd-7952-bfaa-632eb83247c4`, but returned only
  `pass` without criterion or command evidence;
- resulting local commit: `b56af58b1698ba681dd694282155a74430d4ae8e` on
  `glbuilding/greet-txt-20260826T033709Z`; exact content and clean status passed;
- task-record defect: terminal content said `local commit to follow` and did not carry a
  self-reference-safe finalization identity;
- verdict: mutation review `fail` despite the correct project byte. A bare verdict and
  downgraded delivery can permit unsafe completion claims;
- action: require evidence-bearing Reviewer packets, block before Builder on a failed
  delivery preflight, and finalize the project paths plus terminal record in one exact
  Git transaction.

## Dogfood evidence

Record each real run with:

- goal and comparison method;
- frozen source and configuration;
- stages used and skipped;
- owner questions and approvals;
- implementation time versus protocol time;
- review findings and repair count;
- escaped findings found later;
- charter or protocol correction justified by the escape.

Passing structural checks proves only that the pack is internally consistent. It does not prove that a harness followed it or that delivery became faster.
