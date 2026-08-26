# Role bootstrap design

Status: approved design. This document defines the controlled path from the current
framework revision A to later dogfood of a complete role catalog.

## Revision boundaries

Revision A is the current immutable revision. It has five fixed roles:

- Orchestrator
- System Configurer
- Explorer
- Builder
- Reviewer

Revision A governs the goal that creates revision B. That goal does not load or invoke
the roles that B introduces.

Revision B adds only `Spec Writer`, `Spec Reviewer`, and the minimum invocation plumbing
needed to route them. B must not use those roles during its own creation. After the B
change is committed, immutable B governs a new goal.

The B-governed goal uses Spec Writer and a fresh Spec Reviewer to specify the remaining
historical FPLGuru-derived roles for prospective revision C. The current Builder and a
fresh Reviewer then implement and review C. The goal never reloads prospective C as its
governing instructions.

After C is committed, immutable C governs later dogfood of the complete catalog. A role
is recorded as tested only when its activation condition actually occurs. Declaring a
charter, adding invocation text, or mentioning a role is not a test.

This bootstrap does not reverse the failed D02 large-codebase result and does not unblock
Phase 6. Those remain their recorded status until separate evidence changes them.

## Exact revision-B boundary

B changes only these framework files:

- new `agents/SPEC_WRITER.md`
- new `agents/SPEC_REVIEWER.md`
- modify `references/PROTOCOL.md`
- modify `SKILL.md`
- modify `templates/TASK.md`

The B goal must leave PROJECT preferences unchanged. Those preferences are deferred until
B is promoted beyond dogfood because host defaults suffice. B contains no remaining role
charters and no placeholder slots.

The existing Orchestrator remains the hub. The plumbing adds conditional routing for the
specification bracket and records its result in the existing task flow. It does not add a
loop engine. The same configured review-round cap applies to the specification and
implementation brackets. Each repair gets a fresh reviewer. An open finding at the cap
stops the bracket as `blocked`.

## B-governed specification and C implementation

1. The Orchestrator starts a new goal under immutable B and applies the spec activation
   condition.
2. For substantial, ambiguous, architectural, or cross-layer work, it invokes Spec
   Writer. The writer returns a bounded specification packet to the Orchestrator.
3. A fresh, read-only Spec Reviewer reads the full specification and relevant repository
   evidence. It returns `pass`, `repair`, or `blocked` with evidence and uncertainty.
4. On `repair`, the Orchestrator sends the bounded findings to Spec Writer and starts a
   fresh Spec Reviewer for the complete repaired specification. The configured cap applies.
5. After a passing specification bracket and any required owner decisions, the current
   Builder implements prospective C. A fresh Reviewer reviews the complete C change. The
   implementation bracket uses the same cap and fresh-review rule.
6. The goal records C only after the applicable checks and fresh review pass. C is then an
   immutable governing revision for later complete-catalog dogfood; it is never loaded
   during its own creation.

Spec Writer and Spec Reviewer return to the Orchestrator. They do not talk to each other,
edit project code, edit project configuration, edit task records, change the graph, or
direct another role.

## Role contracts

### Spec Writer

Invoke Spec Writer for substantial, ambiguous, architectural, or cross-layer work. The
writer is evidence-first and must:

- separate requirements from mechanism;
- verify material claims or mark them unknown;
- compare two or three approaches only when a real choice exists;
- state the selected approach and assumptions;
- state measurable acceptance criteria, including red paths;
- state validation, non-goals, and owner decisions;
- return a bounded packet to the Orchestrator.

Spec Writer does not edit project code, project configuration, or task records.

### Spec Reviewer

Spec Reviewer is always fresh and read-only. It reads the full specification and relevant
repository evidence. It tries to falsify assumptions, mechanisms, interfaces, scope,
acceptance criteria, owner and permission boundaries, and material failure paths.

It returns `pass`, `repair`, or `blocked` with evidence and uncertainty. It never edits
files or directs roles. A repair always receives a fresh Spec Reviewer, up to the shared
configured cap.

## Architecture and owner boundary

The architecture remains Markdown-only, hub-routed, conditional, and fixed by the
framework. It has no editable graph and no runtime. The owner can configure allowed knobs,
such as models, tools, limits, and project instructions inside fixed slots. The owner
cannot reorder stages, change hub ownership, add placeholder roles, or bypass fresh review.

Long-term catalog provenance is the historical FPLGuru snapshot `d77b93ba`, which has 12
role charters plus `README` and `EVOLUTION`. GLBuilding has two native roles, System
Configurer and Explorer, so the prospective catalog can reach 14 roles. Names and
activation conditions for roles beyond the seed pair are decisions for the B-governed
specification, not this bootstrap design.

## Non-goals

- No remaining role charters in B.
- Placeholder role slots.
- Pipeline YAML.
- A CLI, service, or database.
- Cryptographic proof or transcript-provenance machinery.
- Hostile-harness machinery or obedience enforcement.
- A release, release candidate, or public release claim.

## Acceptance criteria

### A to B

- The creation goal is governed by immutable A and records the A five-role boundary.
- Only the five named B files change; B adds only Spec Writer, Spec Reviewer, and
  minimum invocation plumbing.
- The A Builder implements B and a fresh A Reviewer reviews B under the existing review
  cap. Neither new role is invoked during B creation.
- B is committed as an immutable revision for the next goal. PROJECT preferences remain
  deferred until B is promoted beyond dogfood.

### B to C

- A new goal reads immutable B and invokes Spec Writer when the goal is substantial,
  ambiguous, architectural, or cross-layer.
- Spec Writer returns the required bounded, evidence-first packet without editing project
  code, configuration, or task records.
- A fresh read-only Spec Reviewer checks the full packet and relevant evidence, returns a
  supported verdict, and receives a fresh context after every repair.
- After the spec bracket passes, the current Builder implements C and a fresh Reviewer
  reviews C under the same cap. The goal never reloads prospective C as instructions.
- The B-governed specification selects names and activation conditions for roles beyond
  the seed pair. B itself contains no remaining charters or placeholders.
- A committed C can govern later dogfood of the complete catalog.

### Evidence truthfulness

- A role is marked tested only when its activation condition occurs in a recorded goal;
  unactivated roles remain `not run` or equivalent.
- Every pass claim names the applicable revision, goal, activation, acceptance checks,
  validation results, and uncertainty. Unknown evidence remains visible.
- The bootstrap leaves D02 as a failed large-codebase comparison, leaves Phase 6 blocked,
  and makes no release claim.
