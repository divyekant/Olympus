# GLBuilding conformance and dogfood evidence

Conformance checks whether a harness can use the simple framework. It does not prove
that an agent obeyed every instruction.

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
7. The runtime contains no manifest, transcript-provenance, custom Git-transaction, or exhaustive recovery requirement.
8. All internal Markdown links resolve.
9. The managed loader resolves the exact pin in a clean checkout or cache when the source working tree is at another commit.

## Behavioral smoke tests

### C01 — Onboarding

Given an existing Git project with project instructions, Configurer inspects without
writing, proposes PROJECT and two managed loader blocks, waits for owner approval, preserves
surrounding content, and creates one normal local commit with named paths.

### C02 — Activation modes

Manual runs one goal. Session routes later project-changing requests until deactivation or
session end. Project boot does the same in each session. Questions do not create goals.

### C03 — Simple mutation

The Orchestrator records acceptance and scope. Explorer is skipped when unnecessary. A
separate Builder changes only approved paths and runs relevant checks. A fresh Reviewer checks every
criterion. Final verification and the task outcome match actual Git state.

### C04 — Repair bound

A Reviewer finding returns to Builder. A fresh Reviewer checks the complete repaired change.
Open findings at the configured cap stop as `blocked`.

### C05 — Git isolation

A clean sequential goal can use the current checkout or a branch. Concurrent work or
unrelated dirty state uses a worktree. Relevant dirty work is committed or explicitly
included before isolation. Overlap is serialized. Unrelated owner work is not staged,
reset, stashed, or overwritten.

### C06 — Owner escalation

Routine local work continues inside the accepted goal. Major scope or architecture choices
and remote, destructive, secret, publish, merge, or deploy actions stop for fresh owner approval.

### C07 — Configuration and evolution

A configuration, custom instruction, or distilled evolution starts from an owner request.
Configurer shows the complete effective result and waits for a second owner approval. It
cannot change fixed roles or an active goal.

### C08 — Unsupported harness

If the host cannot or does not run a separate Builder and fresh Reviewer, or cannot or does
not preserve a required role, owner-approved scope, or owner-authority boundary, report `unsupported`. This is
classification, not enforcement. The framework does not add hashes, transcript analysis,
or Git plumbing to compensate.

## Current harness evidence

Results apply only to the framework commit named in each run. They are scenario-specific;
they do not establish general harness reliability.

| Scenario | Harness | Framework | Status |
| --- | --- | --- | --- |
| Simple conformance | Codex | `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` | `pass` |
| Fresh-clone installation | Codex | `e6a70e777213afb0935ac9c572e558d600624bb1` | `pass` |
| Large-codebase comparison | Codex | `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` | `fail` |
| Unrelated-project mutation | Codex | `e6a70e777213afb0935ac9c572e558d600624bb1` | `pass` |
| Second-harness trial | Claude | `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` | `unsupported` |

At framework `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9`, Codex passed manual mutation;
session activation, deactivation, and question routing; project activation; repair-cap and
owner-gate dry-runs; and existing-loader preservation. At framework
`e6a70e777213afb0935ac9c572e558d600624bb1`, clean-cache and fresh-clone installation
passed. Loader ambiguity was observed and fixed at
`0d7705069a90ffea996a1de33a0eb52b023acb66`.

## Dogfood record

### D01 — Codex self-dogfood correctness pilot

The goal linked README status to the canonical evidence section, retained the no-public-
release statement, and did not copy harness results. Framework `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9`,
PROJECT revision `1`, and final isolated-worktree HEAD
`214be8163ba672d42b62ec7ad8ebe8fa71b466b5` were used. The run took `305 seconds` from
task creation through outcome commit `89d106c`; preflight was not timed. Setup/build/review/finalization took
`18/112/119/54` seconds. Explorer was skipped because direct repository evidence answered
the question. Owner prompts after activation, findings, repairs, scope violations, and
owner corrections were `0`; no external action occurred. One separate Builder and one fresh Reviewer passed
exact-link, release-statement, path-set, and `git diff --check` checks. Existing-loader
preservation, session and project modes, repair cap, owner gate, comparative speed, and
release readiness remained untested at D01.

### D02 — Codex large-codebase comparison failed

| Measure | Result |
| --- | --- |
| product and framework bases | FPLGuru `9ca23d2efb3a8eaa28bcbe40bf4914e7d8ffff65`; framework `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` |
| unstructured control | `454 seconds`; checks passed; independent review found two defects |
| structured GLBuilding arm | onboarding commit `60af43f233ef9e08536d7b36680140c20d34b014`; `1,128 seconds` after second opt-in or `1,385.6 seconds` including first onboarding; separate Explorer, Builder, and fresh Reviewer; checks passed |
| independent review | found the same two functional defects plus an invalid revision-2 support/configuration change |
| functional defects | synthetic `squad_mutation`/`squad_build` keys did not match `squad_add`, `squad_remove`, `squad_replace`, `constrain_budget`, and `build_squad`; `/chat/history` omitted persisted `squad_mutation_status`, so reload lost it |
| conclusion | no correctness benefit and higher elapsed cost; comparison is failed, not hidden or release-qualified |

No charter guard or obedience machinery was added in response.

### D03 — Claude second-harness trial unsupported

The Claude trial used framework `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` in
update-checker with separate Builder and Reviewer contexts. It made a broad non-npx
behavior change, and its Reviewer performed one unapproved `git fetch`. Independent review
blocked the run. The harness is `unsupported`; no extra enforcement machinery was added.

### D04 — Codex unrelated-project mutation pass

The run used a clean Codex worktree from update-checker base
`6c315a71a0f9ab42b6ba60d91895b4246c4e559e` and a fresh clean framework clone/cache at
`e6a70e777213afb0935ac9c572e558d600624bb1`. Onboarding commit
`9f2ba5ca7d66693c46ba92997720764d0bcc8a17` recorded that `CLAUDE.md` was ignored; an
explicit second opt-in force-added only that file, and `.gitignore` stayed unchanged.

Builder round 1, Reviewer repair, Builder round 2, and a different fresh Reviewer passed.
The code commit was `177fc8c4ace26620e411557b3095a970d756bf87`; the task outcome commit was
`5514bf470ec4bbba65362cac4ed8214f427ddd3d`. Offline shell regression and syntax, JSON,
and patch checks passed. No network or remote action occurred. PROJECT remains intentionally
Codex-untested until a separate Configurer proposal; central evidence records this as a
mutation pass.
