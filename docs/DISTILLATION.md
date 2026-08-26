# Skill-to-charter distillation

## Purpose

GLBuilding role charters are self-contained. They are distilled from selected skills and
prior FPLGuru charter work; those sources are not loaded at runtime.

Distillation means:

1. inspect the complete source;
2. extract behavior needed by a fixed role;
3. remove source-specific commands, hosts, and workflow machinery;
4. write the behavior directly into the charter;
5. record source identity and exclusions;
6. test the charter through conformance scenarios.

A source update changes nothing automatically. An owner-approved re-mine creates a
versioned charter change for new goals.

## Source influences

The FPLGuru pattern at `d77b93ba` supplied separate mutation and review contexts, one
loop owner, and one canonical charter copy. GLBuilding keeps that pattern for the fixed
14-role catalog. It does not copy project-specific roles, review history, service delivery
paths, or unbounded review pressure.

## Source ledger

Local source paths record what was inspected. They are design provenance, not runtime
requirements.

| Source | Extracted behavior | Destination |
| --- | --- | --- |
| `conductor/SKILL.md` | task classification, one routing owner, phase boundaries | Orchestrator protocol and entrypoint |
| `shaping/SKILL.md` | separate requirements from mechanisms, surface unknowns, consistent docs | Configurer, Explorer |
| `brainstorming/SKILL.md` | inspect first, ask material questions, present design before edits | System Configurer |
| `ponytail/SKILL.md` | simplicity ladder, reuse before addition, smallest useful check | Builder, Reviewer, Orchestrator |
| `resilience/SKILL.md` | material hazard, blast radius, degraded behavior, fail-closed unknowns | All fixed roles |
| `systematic-debugging/SKILL.md` | reproduce, gather evidence, trace cause, test one hypothesis | Explorer, Builder |
| `test-driven-development/SKILL.md` | prove material behavior can fail before relying on a check | Builder |
| `using-git-worktrees/SKILL.md` | conditional isolation, dirty-state safety, baseline verification | Orchestrator protocol |
| `verification-before-completion/SKILL.md` | current command evidence before completion claims | Builder, Reviewer, Orchestrator |
| `requesting-code-review/SKILL.md` | exact review unit, independent feedback, evidence-backed response | Reviewer, Orchestrator |
| `council/SKILL.md` | adversarial option comparison, challenge resolution, and pre-mortem | Decision Council advisory role |
| `skill-creator/SKILL.md` | valid metadata and progressive loading | Pack structure and conformance |

## Historical charter sources for C roles

These seven historical charter sources informed the added generic roles. They are design
provenance only. They are not loaded or invoked at runtime.

| Historical source | Retained generic behavior | Excluded behavior |
| --- | --- | --- |
| Claims Reviewer charter | Grade material claims from current evidence; attack universals, history, and counts. | Product packs, digests, and service-specific commands. |
| Plan Writer charter | Turn an accepted contract into ordered, independently verifiable steps with red checks. | Task artifacts, commits, and delivery. |
| Plan Verifier charter | Verify paths, interfaces, dependency order, criteria, scope, and red checks. | Edits, implementation, and plan authority. |
| Docs Writer charter | Synchronize false tracked documentation, keep one canonical home, and verify links. | Code, configuration, and task edits. |
| Design Reviewer charter | Check accessibility, interaction, responsive behavior, themes, and component reuse against supplied standards. | Assumed tokens, breakpoints, frameworks, or services. |
| Decision Council charter | Compare viable options, recommend, challenge, pre-mortem, and state dissent. | Gates, owner decisions, and role routing. |
| Liaison charter | Answer human status and explanation questions from current task and Git evidence. | Goal creation, edits, and action execution. |

The source charters remain historical inputs. The seven new charters retain only this
generic behavior and remain untested in a 14-role dogfood run.

## Deliberate exclusions

- Source skill names and invocation commands are not runtime dependencies.
- Source model names are not copied; projects choose capability tiers or explicit models inside fixed slots.
- Full test-driven development ceremony is not universal. Nontrivial behavior leaves the smallest check that can fail.
- FPLGuru labels, branches, continuous-integration providers, declarations, and review lanes are not copied.
- Decision Council is a runtime advisory role with no gate. Material owner decisions still
  go to the owner.
- No source skill can automatically modify a charter.

## Owner-approved evolution

1. Record the changed source path and version.
2. State the observed GLBuilding escape or material new behavior.
3. Propose the smallest charter delta and exact effective result.
4. Run the System Configurer conflict check and obtain owner approval.
5. Publish a new immutable revision only after conformance.
6. Apply it to new goals. Restart an active goal only with explicit owner approval.

If no GLBuilding behavior needs to change, record no charter delta.
