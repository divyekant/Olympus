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
| project name | `<name>` |
| repository root | `<path or repository-relative description>` |
| configuration revision | `1` |
| boot mode | `manual` or `orchestration` |
| configured at | `<date>` |

## Framework source pin

| Field | Value |
| --- | --- |
| repository URL | `<canonical URL>` |
| full immutable commit | `<full commit>` |

The pin identifies framework content. It does not authenticate the source or grant remote
authority.

## Project knowledge

### Intent

`<Owner-approved product direction and current priorities.>`

### Map and documentation

| Area | Paths or source | What it explains | Known gap or freshness limit |
| --- | --- | --- | --- |
| `<area>` | `<paths>` | `<purpose>` | `<none or limit>` |

### Validation

| Scope | Command or evidence | When to use it | Known limit |
| --- | --- | --- | --- |
| `<scope>` | `<command/source>` | `<condition>` | `<none or limit>` |

Map and Validation are hints. Check them against current code for each goal.

## Boundaries

| Setting | Approved value |
| --- | --- |
| protected paths | `.olympus/`; managed blocks in `AGENTS.md` and `CLAUDE.md`; `<other>` |
| allowed project areas | `<paths or all except protected paths>` |
| branch/worktree policy | `<current checkout or branch for clean sequential work; worktree for concurrent work or unrelated dirty state; commit or explicitly include relevant dirty work>` |
| review round cap | `2` (`1`, `2`, or `3`) |
| local commit policy | `<project convention>` |

The owner gates in the runtime protocol are fixed and not configurable in PROJECT.

## Harness and role support

Use `supported`, `unsupported`, or `untested`. Record one row for each harness-role pair
that a goal can invoke. A tool's availability alone is `untested`.

| Harness | Role | Status | Mapping and freshness | Tools or capabilities | Observed evidence and limit |
| --- | --- | --- | --- | --- | --- |
| `<harness>` | Orchestrator | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | System Configurer | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Explorer | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Spec Writer | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Claims Reviewer | `<status>` | `<mapping and fresh context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Spec Reviewer | `<status>` | `<mapping and fresh context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Plan Writer | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Plan Verifier | `<status>` | `<mapping and fresh context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Builder | `<status>` | `<mapping and separate context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Docs Writer | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Reviewer | `<status>` | `<mapping and fresh context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Design Reviewer | `<status>` | `<mapping and fresh context>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Release Agent | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Decision Council | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |
| `<harness>` | Liaison | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |

Unsupported harnesses do not run goals that invoke unsupported roles through Olympus.

## Project design standards

Record the sources and matching details that Design Reviewer uses. Missing required
standards or matching evidence makes a triggered Design Reviewer unavailable.

| Source | Matching project area or component | Standard or rule | Status and evidence | Limit |
| --- | --- | --- | --- | --- |
| `<path or source>` | `<area or component>` | `<standard>` | `<supported, missing, or stale>` | `<limit>` |

## Role preferences

These settings select implementations inside fixed duties. They do not change the graph.

The trigger floor is immutable. PROJECT can make an optional trigger more eager, add
matching details, or identify standards and tools. It cannot suppress a trigger or add a
role.

| # | Role | Immutable trigger floor | When used | Model or capability | Tools | Limit |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Orchestrator | every routed request | `<when used>` | `<preference or host default>` | `<tools>` | `<limit>` |
| 2 | System Configurer | owner onboarding or configuration request, plus double opt-in | `<when used>` | `<preference>` | `<tools>` | `<limit>` |
| 3 | Explorer | fresh for material repository question blocking a required role, or explicit audit | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 4 | Spec Writer | substantial, ambiguous, architectural, or cross-layer goal | `<when used>` | `<preference>` | `<tools>` | `<limit>` |
| 5 | Claims Reviewer | every Spec Writer result; fresh and read-only | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 6 | Spec Reviewer | every Spec Writer result; fresh and read-only | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 7 | Plan Writer | accepted contract has dependent steps, cross-layer or interface sequencing, or explicit plan need | `<when used>` | `<preference>` | `<tools>` | `<limit>` |
| 8 | Plan Verifier | every Plan Writer result; fresh and read-only | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 9 | Builder | every non-configuration project mutation | `<when used>` | `<preference>` | `<tools>` | `<limit>` |
| 10 | Docs Writer | Builder makes tracked docs false, or contract requires synchronization | `<when used>` | `<preference>` | `<tools>` | `<limit>` |
| 11 | Reviewer | every project or configuration mutation; fresh and read-only | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 12 | Design Reviewer | material user-facing interface, interaction, visual design, or design-system change; fresh and read-only | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 13 | Release Agent | owner-requested release preparation, remote reconciliation, or one release-boundary external action; no standing authority | `<when used>` | `<preference>` | `<read-only provider evidence>` | `<limit>` |
| 14 | Decision Council | unresolved material decision with viable trade-offs; read-only advisory | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |
| 15 | Liaison | human status or explanation request; read-only and no gate | `<when used>` | `<preference>` | `<read-only tools>` | `<limit>` |

## Approved custom instructions and evolutions

Entries can add or narrow behavior. They cannot add roles, remove duties, change hub
communication, bypass review, alter protected paths, or widen external authority.

| Name | Kind | Scope | Instruction | Approval revision |
| --- | --- | --- | --- | --- |
| `<name>` | `custom` or `evolution` | `<role/path/goal>` | `<exact text>` | `<revision>` |
