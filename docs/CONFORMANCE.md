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

## Behavioral scenarios

### C01 — New installation

Given a clean Git repository without project instruction files, the owner-supplied URL
and commit load only the installation guide and Configurer. The Configurer presents an
exact three-file proposal and writes nothing before approval.

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

A clear goal in a clean checkout can skip Explorer and worktree creation. Builder changes approved paths. A fresh Reviewer receives the exact review unit before completion.

### C10 — Concurrent goals

Two non-overlapping goals receive separate records, branches, and worktrees under one root Orchestrator. No record or changed path crosses goals.

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

An unavailable required check produces Reviewer `blocked`, never `pass`.

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

## Harness evidence

| Harness | Static | Install | Activation | Mutation review | Concurrency | Recovery | Status |
|---|---|---|---|---|---|---|---|
| Codex | not run | not run | not run | not run | not run | not run | not run |
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
