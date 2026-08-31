---
record: olympus-project
schema: 1
---

# Olympus project configuration

This file is the project source of truth. The System Configurer changes it only after
double opt-in.

## Project

| Field | Value |
| --- | --- |
| project name | `Olympus` |
| repository root | `/Users/dk/projects/Olympus` |
| configuration revision | `1` |
| boot mode | `manual` |
| configured at | `2026-08-28` |

## Framework source pin

| Field | Value |
| --- | --- |
| repository URL | `git@github.com:divyekant/Olympus.git` |
| requested ref | `main` |
| full immutable commit | `8653b5409dec4ec7d9153c8b8e9ee30b3c5113f1` |

The pin identifies framework content. It does not authenticate the source or grant remote
authority.

## Project knowledge

### Intent

`Olympus is a private experimental Markdown-only build system for agent-led software
development. It defines one fixed orchestration graph, the fifteen-role Pantheon, bounded
review, and Git-backed handoffs, and it adds no runtime, service, or dependency. Current
priority is the 0.5.0 line: compact guided and express onboarding, the canonical
activation preflight, the release boundary, and the owner-selected workflow. This
repository is also the framework source, so the target and the framework pin stay
separate. Core-framework changes follow the normal repository workflow outside Olympus,
as CONTRIBUTING.md requires. Public visibility starts only with owner approval for
version 1.0.0.`

### Map and documentation

| Area | Paths or source | What it explains | Known gap or freshness limit |
| --- | --- | --- | --- |
| `framework contract` | `SKILL.md`, `references/PROTOCOL.md`, `references/ONBOARDING.md` | Activation, preflight, fixed roles, goal flow, owner gates, and the guided onboarding conversation | `none` |
| `role charters` | `agents/` | One charter for each Pantheon role | `none` |
| `templates` | `templates/PROJECT.md`, `templates/BOOTSTRAP.md`, `templates/TASK.md` | Project configuration, managed loader block, and task record shapes | `none` |
| `installation` | `docs/INSTALLATION.md` | Owner install, onboarding, wake, and activation procedure | `none` |
| `evidence and history` | `docs/CONFORMANCE.md`, `docs/DECISIONS.md`, `docs/DISTILLATION.md`, `CHANGELOG.md` | Dogfood results, decisions, distillation, and release history | `Conformance results are scenario-specific and do not prove general harness support` |
| `product direction` | `README.md`, `VISION.md`, `ROADMAP.md` | Purpose, scope limits, version status, and planned work | `none` |
| `contribution rule` | `CONTRIBUTING.md` | Core-framework changes run outside Olympus and need dogfood evidence | `none` |

### Validation

| Scope | Command or evidence | When to use it | Known limit |
| --- | --- | --- | --- |
| `automated tests and build` | `none found` | `not available` | `The repository has no build, test, or continuous integration configuration` |
| `static framework checks` | `docs/CONFORMANCE.md` static checks 1 to 28 | Before a framework or charter change is accepted | `Manual reading, not an executable suite` |
| `internal link resolution` | Manual check that every internal Markdown link resolves | After a documentation, charter, or template change | `Manual; no link checker is configured` |
| `repository state` | `git status --short`, `git diff`, `git log` | Before and after every mutation | `Shows files and history, not behavior` |

Map and Validation are hints. Check them against current code for each goal.

## Boundaries

| Setting | Approved value |
| --- | --- |
| protected paths | `.olympus/`; managed blocks in `AGENTS.md` and `CLAUDE.md` |
| allowed project areas | `all repository paths except the protected paths` |
| branch/worktree policy | `one worktree per goal with closure at goal end; commit or explicitly include relevant dirty work before a current-checkout goal` |
| review round cap | `2` |
| local commit policy | `stage only the named approved paths; keep each commit local; use Conventional Commit subjects for project work and the fixed onboarding message for configuration; a push, pull request, merge, or release needs fresh owner approval` |

The owner gates in the runtime protocol are fixed and not configurable in PROJECT.

## Harness and role support

Use `supported`, `unsupported`, or `untested`. A tool's availability alone is `untested`.

Default row: every role uses the host-default mapping and tools, in the context freshness
the protocol requires, with status `untested` until behavior is observed at the pinned
commit. Add one exception row for each harness-role pair that diverges from the default
or has observed evidence.

| Harness | Default mapping | Default status |
| --- | --- | --- |
| `Claude Code` | `host default; protocol freshness rules` | `untested` |

| Harness | Role | Status | Mapping and freshness | Tools or capabilities | Observed evidence and limit |
| --- | --- | --- | --- | --- | --- |
| `Claude Code` | `System Configurer` | `untested` | `main session under the pinned charter; separate from the Reviewer` | `file read and write, Git` | `No behavior observed at this pin when this revision was written` |
| `Claude Code` | `Reviewer` | `untested` | `fresh subagent context, read-only, never the Configurer` | `file read, Git read-only commands` | `No behavior observed at this pin when this revision was written` |

Unsupported harnesses do not run goals that invoke unsupported roles through Olympus.

## Project design standards

Record the sources and matching details that Design Reviewer uses, or `none recorded`.
Missing required standards or matching evidence makes a triggered Design Reviewer
unavailable.

| Source | Matching project area or component | Standard or rule | Status and evidence | Limit |
| --- | --- | --- | --- | --- |
| `none recorded` | `none` | `none` | `missing` | `The repository has no user-facing interface and no design standard` |

## Role preferences

These settings select implementations inside fixed duties. They do not change the graph.
The trigger floors live in the pinned framework's `references/PROTOCOL.md` and are
immutable. PROJECT can make an optional trigger more eager, add matching details, or
identify standards and tools. It cannot suppress a trigger or add a role.

Default row: every role uses the host-default model, capability, and tools. Add one
exception row per role that diverges.

| # | Role | When used | Model or capability | Tools | Limit |
| --- | --- | --- | --- | --- | --- |
| `1-15` | `all roles` | `when the fixed trigger holds` | `host default` | `host default` | `No role preference is recorded at revision 1` |

## Approved custom instructions and evolutions

Entries can add or narrow behavior. They cannot add roles, remove duties, change hub
communication, bypass review, alter protected paths, or widen external authority.

| Name | Kind | Scope | Instruction | Approval revision |
| --- | --- | --- | --- | --- |
| `none` | `custom` | `none` | `No custom instruction or evolution is approved at revision 1` | `1` |
