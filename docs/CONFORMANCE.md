# GLBuilding conformance and dogfood evidence

Conformance checks whether a harness can use the simple framework. It does not try to
prove that an agent obeyed every instruction.

## Result labels

- `pass`: the observed result met the scenario.
- `partial`: some required parts passed, but the scenario or harness gate is incomplete.
- `fail`: the harness ran the scenario but violated the contract.
- `unsupported`: the harness cannot or does not preserve a required role, owner-approved
  scope, or owner-authority boundary.
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
9. The managed loader resolves the exact pin in a clean checkout or cache when the source
   working tree is at another commit.

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

If the host cannot run a separate Builder and fresh Reviewer, or cannot or does not preserve
a required role, owner-approved scope, or owner-authority boundary, the run reports
`unsupported`. This is classification, not enforcement. The framework does not add hashes,
transcript analysis, or Git plumbing to compensate.

## Current harness evidence

Results apply only to the framework commit named in each run.

These results are scenario-specific. They do not establish general harness reliability.

| Scenario | Harness | Framework | Status |
| --- | --- | --- | --- |
| Simple conformance | Codex | `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` | `pass` |
| Fresh-clone installation | Codex | `e6a70e777213afb0935ac9c572e558d600624bb1` | `pass` |
| Large-codebase comparison | Codex | `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` | `fail` |
| Unrelated-project mutation | Codex | `e6a70e777213afb0935ac9c572e558d600624bb1` | `pass` |
| Second-harness trial | Claude | `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` | `unsupported` |

At framework `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9`, Codex simple conformance passed:
manual mutation; session activation, deactivation, and question routing; project activation;
repair-cap and owner-gate dry-runs; and existing-loader preservation.

At framework `e6a70e777213afb0935ac9c572e558d600624bb1`, clean-cache and fresh-clone
installation passed. Loader ambiguity was observed and fixed at
`0d7705069a90ffea996a1de33a0eb52b023acb66`.

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

### D01 — Codex self-dogfood correctness pilot

| Measure | Result |
| --- | --- |
| goal and acceptance | Link README status to the canonical evidence section, do not copy harness results, and retain the no-public-release statement. |
| framework commit and PROJECT revision | `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9`; revision `1` |
| final evidence HEAD | `214be8163ba672d42b62ec7ad8ebe8fa71b466b5` in an isolated worktree |
| total elapsed time | `305 seconds` from task record creation through the initial outcome; preflight was not timed |
| setup, build, review, finalization | `18`, `112`, `119`, and `54` seconds |
| owner prompts after activation | `0` |
| Explorer use | skipped; direct repository evidence answered the bounded question |
| Builder and Reviewer rounds | `1` separate Builder; `1` fresh Reviewer |
| findings and repairs | `0` |
| scope violations | `0` |
| final checks | exact README link and target; retained release statement; no copied results; expected path set; `git diff --check`; all passed |
| owner corrections | `0` |
| external action | none |
| remaining uncertainty at D01 | Existing-loader preservation, session and project modes, repair cap, owner gate, comparative speed, and release readiness were not tested. |

Measure administration cost on representative larger goals. This small smoke test checks
correctness and role separation, not speed. At that time, large-codebase comparison remained
required before release.

### D02 — Codex large-codebase comparison failed

| Measure | Result |
| --- | --- |
| product and framework bases | FPLGuru frozen product base `9ca23d2efb3a8eaa28bcbe40bf4914e7d8ffff65`; framework `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` |
| unstructured control | `454 seconds`; checks passed; independent review found two defects |
| structured GLBuilding arm | onboarding commit `60af43f233ef9e08536d7b36680140c20d34b014`; `1,128 seconds` after second opt-in, or `1,385.6 seconds` including the first onboarding turn; separate Explorer, Builder, and fresh Reviewer; checks passed |
| independent review | found the same two functional defects plus an invalid revision-2 support/configuration change |
| functional defects | synthetic `squad_mutation`/`squad_build` keys do not match real engine keys `squad_add`, `squad_remove`, `squad_replace`, `constrain_budget`, and `build_squad`; `/chat/history` omits persisted `squad_mutation_status`, so reload loses it |
| conclusion | no correctness benefit and higher elapsed cost; comparison is failed, not hidden or release-qualified |

No charter guard or other obedience machinery was added in response.

### D03 — Claude second-harness trial unsupported

The Claude trial used framework `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` in update-checker
with separate Builder and Reviewer contexts. It made a broad non-npx behavior change, and
its Reviewer performed one unapproved `git fetch`. Independent review blocked the run.
The harness is `unsupported`; no extra enforcement machinery was added.

### D04 — Codex unrelated-project mutation pass

The run used a clean Codex worktree from update-checker base
`6c315a71a0f9ab42b6ba60d91895b4246c4e559e` and a fresh clean framework clone/cache at
`e6a70e777213afb0935ac9c572e558d600624bb1`. Onboarding commit
`9f2ba5ca7d66693c46ba92997720764d0bcc8a17` recorded that `CLAUDE.md` was ignored; an
explicit second opt-in force-added only that file, and `.gitignore` stayed unchanged.

Builder round 1, Reviewer repair, Builder round 2, and a different fresh Reviewer passed.
The code commit was `177fc8c4ace26620e411557b3095a970d756bf87`; the task outcome commit was
`5514bf470ec4bbba65362cac4ed8214f427ddd3d`. Offline shell regression and syntax, JSON, and
patch checks passed. No network or remote action occurred. `PROJECT` remains intentionally
Codex-untested until a separate Configurer proposal; central evidence records this as a
mutation pass.
