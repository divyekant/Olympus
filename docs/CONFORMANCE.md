# Olympus conformance and dogfood evidence

Conformance checks whether a harness can use the fixed framework. It does not prove
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

1. `SKILL.md` has valid frontmatter, links to the protocol, and links to every local
   charter and template it names.
2. The protocol names one Orchestrator and the fixed ordered 14-role catalog with its
   triggers and authority.
3. PROJECT supports manual and project orchestration modes, exact role preferences,
   trigger floors, harness evidence, and design-standard matching details.
4. The skill supports manual, session, and project activation.
5. Every Spec Writer result receives fresh Claims Reviewer and Spec Reviewer checks.
6. Every Plan Writer result receives fresh Plan Verifier checks, when the plan trigger
   holds.
7. Every project or configuration mutation requires a fresh general Reviewer; Docs Writer
   and Design Reviewer triggers are conditional and cannot replace that review.
8. Configuration uses double opt-in, applies the exact approved unit uncommitted, reviews
   it fresh, and commits only after a pass; hook changes receive a fresh rereview.
9. Explorer, Council, Liaison, and worktree use are conditional; every invoked role has
   role-specific harness mapping and support evidence.
10. The runtime contains no manifest, transcript-provenance, custom Git-transaction, or
    exhaustive recovery requirement.
11. All internal Markdown links resolve.
12. The managed loader resolves the exact pin in a clean checkout or cache when the source
    working tree is at another commit.

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
applies the exact approved unit without a commit, receives a fresh Reviewer pass, and only
then stages and commits. Hook-changed content receives a fresh committed-content review.
It cannot change fixed roles or an active goal.

### C08 — Unsupported harness

If the host cannot or does not run a separate Builder and fresh Reviewer, or cannot or does
not preserve a required role, owner-approved scope, or owner-authority boundary, report `unsupported`. This is
classification, not enforcement. The framework does not add hashes, transcript analysis,
or Git plumbing to compensate.

### C09 — Fixed catalog and triggers

The Orchestrator records the ordered 14-role catalog, predicts the roles for the goal, and
invokes each role only when its trigger holds. PROJECT can make optional triggers more
eager but cannot suppress a framework trigger or add a role. Every invoked role has a
mapping, freshness, tools, support status, and observed evidence recorded.

### C10 — Specification and planning brackets

Every Spec Writer result goes to fresh Claims Reviewer and Spec Reviewer contexts over the
same complete packet. A triggered Plan Writer receives the accepted contract or
specification verbatim, and a fresh Plan Verifier receives that contract plus the whole
plan. Repairs use complete fresh reviews. Specification, plan, configuration, and
implementation caps apply independently.

### C11 — Documentation and design conditions

When Builder makes tracked documentation false or the contract requires synchronization,
Docs Writer changes approved documentation only and verifies touched links before fresh
general review. A material user-facing change invokes Design Reviewer when its trigger
holds and matching project design standards and evidence exist; missing required standards
block the goal, not the trigger. Design Reviewer cannot replace general review.
Accessibility basics remain in Builder and general Reviewer checks.

### C12 — Advisory and status roles

Decision Council answers one unresolved material trade-off question read-only and without
a gate. Liaison answers human status or explanation questions from current task and Git
evidence, without editing or creating a goal. Both return only to the Orchestrator.

## Current harness evidence

Results apply only to the framework commit named in each run. They are scenario-specific;
they do not establish general harness reliability.

| Scenario | Harness | Framework | Status |
| --- | --- | --- | --- |
| Simple conformance | Codex | `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` | `pass` |
| Fresh-clone installation | Codex | `e6a70e777213afb0935ac9c572e558d600624bb1` | `pass` |
| Large-codebase comparison | Codex | `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` | `fail` |
| Controlled Issue #750 A/B comparison | Codex | `3d67f064821c3e4a05b5e87118eeea19119a16e6` | `pass` |
| Unrelated-project mutation | Codex | `e6a70e777213afb0935ac9c572e558d600624bb1` | `pass` |
| Second-harness trial | Claude | `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9` | `unsupported` |
| Fixed conditional 14-role catalog | Codex | `3d67f064821c3e4a05b5e87118eeea19119a16e6` | `partial` |

At framework `5120ba5cb9ae911ac6a01ce0d753ffab6d3353b9`, Codex passed manual mutation;
session activation, deactivation, and question routing; project activation; repair-cap and
owner-gate dry-runs; and existing-loader preservation. At framework
`e6a70e777213afb0935ac9c572e558d600624bb1`, clean-cache and fresh-clone installation
passed. Loader ambiguity was observed and fixed at
`0d7705069a90ffea996a1de33a0eb52b023acb66`.

Issue #750 exercised the fixed catalog and its specification, build, and review path. Not
every conditional role ran. Do not infer support for an uninvoked role.

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
| structured Olympus arm | onboarding commit `60af43f233ef9e08536d7b36680140c20d34b014`; `1,128 seconds` after second opt-in or `1,385.6 seconds` including first onboarding; separate Explorer, Builder, and fresh Reviewer; checks passed |
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

### D05 — FPLGuru Issue #750 controlled A/B comparison pass

The experiment compared normal Codex with Codex using Olympus. Both arms started from
FPLGuru `1f1efd1`, used the same model, reasoning level, issue packet, and isolated
worktrees, and received the same external review process. Olympus used framework
`3d67f064821c3e4a05b5e87118eeea19119a16e6`.

Specification PRs
[#919](https://github.com/darshanpania/fplguru/pull/919) and
[#920](https://github.com/darshanpania/fplguru/pull/920) were approved at heads
`218d7314690b166b7150bb36b40d5386b4e98959` and
`ce1a429af9ea2ac5fe22363d07eefe06fceb31f5`. Implementation PRs
[#921](https://github.com/darshanpania/fplguru/pull/921) and
[#922](https://github.com/darshanpania/fplguru/pull/922) were reviewed at heads
`5fcbedba8ce2af6f4ac251b1f310f3d12b558e4f` and
`658b4057ac6eef4d44ae37d8fd69c29cbb098be2` against base
`6019c2005a4b3552d77928bc3905b69cb227a746`.

The external implementation reviews found no P0-P2 defect. Their GitHub status remained
`pending` because both pull requests were drafts and required checks were unavailable.
Normal Codex supplied two focused passing tests. Olympus supplied 21 focused passing tests
across the cache regression and direct consumers. Olympus also caught an order-dependent
combined-test problem before final implementation.

The correctness outcome was a tie. Normal Codex was leaner. Olympus produced stronger
evidence and review separation. This result supports experimental version `0.1.0` and
larger tests. It does not prove that Olympus produces better final code.
