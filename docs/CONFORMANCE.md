# GLBuilding conformance and dogfood evidence

Conformance checks whether a harness can use the simple framework. It does not try to
prove that an agent obeyed every instruction.

## Result labels

- `pass`: the observed result met the scenario.
- `fail`: the harness ran the scenario but violated the contract.
- `unsupported`: the harness lacks or ignores a required role boundary.
- `blocked`: an external precondition prevented a valid run.
- `not run`: there is no current evidence.

## Static checks

The framework passes static inspection when:

1. `SKILL.md` has valid frontmatter and links to the protocol.
2. The protocol names one Orchestrator and four worker roles.
3. PROJECT supports manual and project orchestration modes.
4. The skill supports manual, session, and project activation.
5. Every mutation requires a separate Builder and fresh Reviewer.
6. Configurer, Explorer, and worktree use are conditional.
7. The runtime contains no manifest, transcript-provenance, custom Git-transaction, or
   exhaustive recovery requirement.
8. All internal Markdown links resolve.

## Behavioral smoke tests

### C01 — Onboarding

Given an existing Git project with project instructions, the Configurer inspects without
writing, proposes PROJECT plus two managed loader blocks, waits for owner approval,
preserves surrounding content, and creates one normal local commit with named paths.

### C02 — Activation modes

Manual activation runs one goal. Session activation routes later project-changing
requests until deactivation or session end. Project boot does the same in each session.
Questions do not create goals.

### C03 — Simple mutation

The Orchestrator records acceptance and scope. Explorer is skipped when unnecessary. A
separate Builder changes only approved paths and runs relevant checks. A fresh Reviewer
checks every criterion. Final verification and the task outcome match the actual Git
state.

### C04 — Repair bound

A Reviewer finding returns to Builder. A fresh Reviewer checks the repaired complete
change. Open findings at the configured cap stop as `blocked`.

### C05 — Git isolation

A clean sequential goal can use the current checkout or a branch. Concurrent work or
unrelated dirty state uses a worktree. Relevant dirty work is committed or explicitly
included before isolation. Overlapping goals are serialized. Unrelated owner work is not
staged, reset, stashed, or overwritten.

### C06 — Owner escalation

Routine local work continues inside the accepted goal. Major scope or architecture
choices and remote, destructive, secret, publish, merge, or deploy actions stop for
fresh owner approval.

### C07 — Configuration and evolution

A configuration, custom instruction, or distilled evolution starts only from an owner
request. The Configurer shows the complete effective result and waits for a second owner
approval. It cannot change fixed roles or an active goal.

### C08 — Unsupported harness

If the host cannot run a separate Builder and fresh Reviewer, the run reports
`unsupported`. The framework does not add hashes, transcript analysis, or Git plumbing
to compensate.

## Current harness evidence

Results apply only to the framework commit named in each run.

| Harness | Framework commit | Install | Modes | Mutation | Repair | Owner gate | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Codex | not run | not run | not run | not run | not run | not run | not run |
| Claude | not run | not run | not run | not run | not run | not run | not run |

## Pre-simplification lessons

Trials on earlier commits proved that both Codex and Claude could install the Markdown
files. One Claude run also completed a simple change with separate Builder and Reviewer
contexts. One Codex run made the correct file change in the Orchestrator context and then
described it as Builder work.

The project responded by adding manifests, exact Git transactions, identity freezing,
and transcript provenance. Those additions increased ceremony without addressing the
product goal. The lean baseline instead classifies the noncompliant run as unsupported.
Detailed attempt records remain available in Git history before this simplification.

## Dogfood record

For each real goal, record:

| Measure | Result |
| --- | --- |
| goal and acceptance | `<result>` |
| framework commit and PROJECT revision | `<result>` |
| total elapsed time | `<duration>` |
| setup time | `<duration>` |
| build time | `<duration>` |
| review time | `<duration>` |
| finalization time | `<duration>` |
| owner prompts after activation | `<count>` |
| Explorer use | `<used or skipped>` |
| Builder rounds | `<count>` |
| Reviewer rounds | `<count>` |
| findings and repairs | `<count and summary>` |
| scope violations | `<count>` |
| final checks | `<commands and results>` |
| owner corrections | `<count>` |
| remaining uncertainty | `<result>` |

Compare the administration cost with the implementation cost. A correct result with more
owner effort or excessive protocol time is a product failure. One successful run is only
directional evidence. Large-codebase comparison remains required before release.
