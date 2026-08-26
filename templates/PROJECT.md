---
record: glbuilding-project
schema: 1
---

# GLBuilding project configuration

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
| protected paths | `.glbuilding/`; managed blocks in `AGENTS.md` and `CLAUDE.md`; `<other>` |
| allowed project areas | `<paths or all except protected paths>` |
| branch/worktree policy | `<current checkout or branch for clean sequential work; worktree for concurrent work or unrelated dirty state; commit or explicitly include relevant dirty work>` |
| review round cap | `2` (`1`, `2`, or `3`) |
| local commit policy | `<project convention>` |

The owner gates in the runtime protocol are fixed and not configurable in PROJECT.

## Harness support

Use `supported`, `unsupported`, or `untested`.

| Harness | Status | Builder mapping | Reviewer mapping | Notes |
| --- | --- | --- | --- | --- |
| Codex | `<status>` | `<native subagent or equivalent>` | `<fresh review context>` | `<limit>` |
| Claude | `<status>` | `<native subagent or equivalent>` | `<fresh review context>` | `<limit>` |

Unsupported harnesses do not run mutation goals through GLBuilding.

## Role preferences

These settings select implementations inside fixed duties. They do not change the graph.

| Role | When used | Model or capability | Tools | Limit |
| --- | --- | --- | --- | --- |
| Orchestrator | every goal | `<preference or host default>` | `<tools>` | `<limit>` |
| System Configurer | onboarding or approved change | `<preference>` | `<tools>` | `<limit>` |
| Explorer | only for unresolved questions | `<preference>` | `<read-only tools>` | `<limit>` |
| Builder | every mutation | `<preference>` | `<tools>` | `<limit>` |
| Reviewer | every mutation | `<preference>` | `<read-only tools>` | `<limit>` |

## Approved custom instructions and evolutions

Entries can add or narrow behavior. They cannot add roles, remove duties, change hub
communication, bypass review, alter protected paths, or widen external authority.

| Name | Kind | Scope | Instruction | Approval revision |
| --- | --- | --- | --- | --- |
| `<name>` | `custom` or `evolution` | `<role/path/goal>` | `<exact text>` | `<revision>` |
