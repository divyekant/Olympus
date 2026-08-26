---
record: glbuilding-project
schema: 1
---

# GLBuilding Project Configuration

The System Configurer writes this record only after double opt-in. Fixed behavior
comes from the pinned GLBuilding protocol. This file stores project values and
approved overrides only.

## Project

| Field | Approved value |
| --- | --- |
| project name | `<name>` |
| repository root marker | `.` or `<stable repository-relative marker>` |
| outcome | `<one measurable project outcome>` |
| config revision | `<integer starting at 1>` |
| boot mode | `manual` or `orchestration` |

Activation commands are fixed: `Use GLBuilding for: <goal>`,
`Activate GLBuilding orchestration`, and `Deactivate GLBuilding orchestration`.

## Framework source

This is the only canonical source identity. Each task copies the commit that governs it.

| Field | Approved value |
| --- | --- |
| canonical repository URL | `<exact owner-approved URL>` |
| full immutable commit | `<full commit; no branch, tag, or short SHA>` |
| verification | `<origin, HEAD, and empty-status commands and results>` |

The pin identifies content. It is not a security trust anchor.

## Proposal metadata

| Field | Record |
| --- | --- |
| proposal identifier | `<stable identifier>` |
| proposed at | `<timestamp fixed before approval>` |
| requested by | `<current session principal>` |
| principal binding limit | `<native control or workflow-only>` |
| conflicts | `<none or exact rejected conflict>` |

## Project knowledge

### Intent

`<owner-approved direction; not proof of current behavior>`

### Map

| Component or boundary | Likely paths | Why it matters | Frozen evidence |
| --- | --- | --- | --- |
| `<component>` | `<paths>` | `<impact>` | `<revision and file:line>` |

### Validation

| Check or evidence | Command or path | Read/write | Verified at revision |
| --- | --- | --- | --- |
| `<check>` | `<command or path>` | `<read-only or mutation>` | `<revision and result>` |

Map and Validation are hints. Reverify them for each frozen goal.

## Project commands and boundaries

| Field | Approved value |
| --- | --- |
| stack | `<language, platform, existing libraries, or none>` |
| check | `<existing command or none>` |
| test | `<existing command or none>` |
| lint or format | `<existing command or none>` |
| build | `<existing command or none>` |
| default allowed paths | `<paths or task-specific>` |
| protected paths | `.glbuilding/`; `AGENTS.md`; `CLAUDE.md`; `<other>` |
| default delivery boundary | `<verified local change or committed goal branch>` |
| cross-host resume | `off` or `<tested persistent-workspace/checkpoint contract>` |
| v1 external-action policy | `fresh owner approval for each external effect` |

## Harness capabilities

Use one label: `native-enforced`, `workflow-instructed`, or `unavailable`.

| Boundary | Semantic capability | Label | Host evidence |
| --- | --- | --- | --- |
| Orchestrator | task-record write and active-root scan | `<label>` | `<control>` |
| Orchestrator | branch and worktree setup | `<label>` | `<control>` |
| Git finalization | exact `commit-tree` and old-value `update-ref`; hooks or signing not required | `<label>` | `<control or limit>` |
| System Configurer | PROJECT and sentinel-only write | `<label>` | `<control>` |
| Explorer | fresh read-only inspection | `<label>` | `<control>` |
| Builder | approved-path edit and checks | `<label>` | `<control>` |
| Reviewer | fresh independent read-only review | `<label>` | `<control>` |
| Harness | current-session owner-principal binding | `<label>` | `<control or limit>` |
| Harness | fresh approval capture for external effects | `<label>` | `<control>` |

## Optional execution profile

`none` is valid. Limits use explicit units. Provider mappings cannot change role duties.

| Role | Semantic tool scope | Codex mapping | Claude mapping | Model or tier | Limit |
| --- | --- | --- | --- | --- | --- |
| Configurer | `<scope or none>` | `<mapping>` | `<mapping>` | `<value>` | `<turns/minutes or none>` |
| Explorer | `<scope or none>` | `<mapping>` | `<mapping>` | `<value>` | `<turns/minutes or none>` |
| Builder | `<scope or none>` | `<mapping>` | `<mapping>` | `<value>` | `<turns/minutes or none>` |
| Reviewer | `<scope or none>` | `<mapping>` | `<mapping>` | `<value>` | `<turns/minutes or none>` |

| Other bounded setting | Approved value |
| --- | --- |
| review rounds | `2` (allowed: `1`, `2`, or `3`) |
| maximum concurrent non-overlapping goals | `<integer or host default>` |

Execution profile SHA-256: `<digest of the effective table and settings>`

## Named custom additions and evolutions

Entries can add or narrow instructions. They cannot remove duties or change topology,
authority, protected paths, action policy, or independent review.

| Name | Kind | Scope | Exact addition or narrowing | Approval and revision |
| --- | --- | --- | --- | --- |
| `<name>` | `custom` or `evolution` | `<role/path/goal>` | `<exact text>` | `<approval/revision>` |
