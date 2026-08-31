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
| repository root | `<absolute path of the repository root>` |
| configuration revision | `1` |
| boot mode | `manual` or `orchestration` |
| configured at | `<date>` |

## Framework source pin

| Field | Value |
| --- | --- |
| repository URL | `<canonical URL, or a local path for a private framework copy>` |
| requested ref | `<branch, tag, or commit from the owner request; default main>` |
| full immutable commit | `<the resolved full commit; the pin sessions load>` |

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
| branch/worktree policy | `<one worktree per goal with closure at goal end (default); current checkout or branch when the owner permits it for simple sequential work; commit or explicitly include relevant dirty work>` |
| review round cap | `2` (`1`, `2`, or `3`) |
| strict convergence | `off` (`off` or `on`) |
| writer reuse | `reuse` (`reuse` or `fresh-per-round`) |
| local commit policy | `<project convention>` |

The owner gates in the runtime protocol are fixed and not configurable in PROJECT.

## Harness and role support

Use `supported`, `unsupported`, or `untested`. A tool's availability alone is `untested`.

Default row: every role uses the host-default mapping and tools, in the context freshness
the protocol requires, with status `untested` until behavior is observed at the pinned
commit. Add one exception row for each harness-role pair that diverges from the default
or has observed evidence.

Explorer's reproduction-execution authority is one such row, recorded with role value
`Explorer (reproduction execution)`. Only `supported` opens that gate, and only when the
observed evidence covers exactly four limits enforced by the environment itself, not by
Explorer's own command list: no network access, no credential access, no write outside
the one disposable reproduction copy, and no access to the target repository or its Git
administration beyond the read that creates the copy. A sandbox's mere availability,
without that evidence, stays `untested` and leaves the gate closed; Explorer then stays
observation-only for a diagnose-only dispatch.

| Harness | Default mapping | Default status |
| --- | --- | --- |
| `<harness>` | `host default; protocol freshness rules` | `untested` |

| Harness | Role | Status | Mapping and freshness | Tools or capabilities | Observed evidence and limit |
| --- | --- | --- | --- | --- | --- |
| `<harness>` | `<role>` | `<status>` | `<mapping>` | `<tools>` | `<evidence or limit>` |

Unsupported harnesses do not run goals that invoke unsupported roles through Olympus.

## Project design standards

Record the sources and matching details that Design Reviewer uses, or `none recorded`.
Missing required standards or matching evidence makes a triggered Design Reviewer
unavailable.

| Source | Matching project area or component | Standard or rule | Status and evidence | Limit |
| --- | --- | --- | --- | --- |
| `<path or source, or none recorded>` | `<area or component>` | `<standard>` | `<supported, missing, or stale>` | `<limit>` |

## Role preferences

These settings select implementations inside fixed duties. They do not change the graph.
The trigger floors live in the pinned framework's `references/PROTOCOL.md` and are
immutable. PROJECT can make an optional trigger more eager, add matching details, or
identify standards and tools. It cannot suppress a trigger or add a role.

Default row: every role uses the host-default model, capability, and tools. Add one
exception row per role that diverges.

| # | Role | When used | Model or capability | Tools | Limit |
| --- | --- | --- | --- | --- | --- |
| `<#>` | `<role, or all roles>` | `<when used>` | `<preference or host default>` | `<tools>` | `<limit>` |

## Approved custom instructions and evolutions

Entries can add or narrow behavior. They cannot add roles, remove duties, change hub
communication, bypass review, alter protected paths, or widen external authority.

| Name | Kind | Scope | Instruction | Approval revision |
| --- | --- | --- | --- | --- |
| `<name>` | `custom` or `evolution` | `<role/path/goal>` | `<exact text>` | `<revision>` |
