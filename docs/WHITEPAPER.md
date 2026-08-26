# GLBuilding framework white paper

## Abstract

GLBuilding is a Markdown-only workflow for agent-led software development. It addresses
a common failure mode: one long session must discover a large codebase, choose scope,
edit it, and judge its own work. Context fills with old assumptions and self-review
inherits the Builder's blind spots.

GLBuilding keeps one small Orchestrator context and sends bounded work to four worker
roles. Git stores project configuration and task records. Codex or Claude supplies the
agents and tools. GLBuilding supplies no runtime. Its success criterion is product
delivery: administration that costs more than the change is a failure.

The [runtime protocol](../references/PROTOCOL.md) is the canonical operational contract.
This paper explains the design and its limits.

## Design thesis

The smallest useful graph is fixed. Every worker outcome returns to the Orchestrator:

```mermaid
flowchart TD
    O[Orchestrator] --> C[System Configurer<br/>onboarding or approved change]
    O --> E[Explorer<br/>only for unresolved questions]
    O --> B[Builder<br/>project mutation]
    O --> R[Fresh Reviewer<br/>every mutation]
    R -->|review packet| O
    O -->|repair below cap| B
    O -->|pass| V[Final verification]
    O -->|blocked or cap reached| H[Owner or blocked result]
```

Worker roles do not talk to each other. They return concise packets to the Orchestrator.
Only accepted results enter the goal record. This keeps:

1. discovery noise out of the Builder context;
2. Builder assumptions out of the Reviewer context;
3. owner attention on material decisions, not agent routing.

## System boundary

```mermaid
flowchart LR
    Owner --> Host[Codex or Claude]
    Host --> Loader[Project loader block]
    Loader --> Project[.glbuilding/PROJECT.md]
    Project --> Pack[External GLBuilding<br/>exact commit]
    Pack --> Flow[Fixed Markdown workflow]
    Flow --> Repo[Target Git repository]
    Repo --> Tasks[One task record per goal]
    Repo --> Trees[Branch or worktree when useful]
```

The framework does not call model APIs, schedule jobs, store conversations, or run a
service. The host uses its normal subagent and tool features. The target project contains
only loader blocks, `.glbuilding/PROJECT.md`, and `.glbuilding/tasks/<goal-id>.md` records.
The detailed framework stays outside the target repository at the pinned commit.

## Configuration boundary

The owner supplies a framework repository URL and full commit. The Configurer inspects
the target repository and derives a minimal configuration. It asks only questions that
change intent, boot mode, boundaries, or authority.

Configuration uses double opt-in:

```mermaid
sequenceDiagram
    participant Owner
    participant Configurer
    participant Git
    Owner->>Configurer: Request onboarding or change
    Configurer->>Configurer: Inspect repository and derive defaults
    Configurer->>Owner: Show complete configuration and file changes
    Owner->>Configurer: Approve that proposal
    Configurer->>Git: Apply, validate, and commit named paths
```

The owner can select models, tools, review rounds, boot mode, protected paths, and scoped
custom instructions. Fixed roles, hub communication, fresh review, and the external-action
gate remain unchanged.

## Project knowledge

GLBuilding records three kinds of project knowledge in PROJECT:

- **Intent:** owner-approved direction.
- **Map:** code, interfaces, and documentation that locate the work.
- **Validation:** commands and evidence that can disprove a result.

Map and Validation are hints until verified against current code. Good documentation
speeds work, but stale documentation can misroute it. The Configurer records missing or
stale sources. Explorer resolves only the material gaps needed for a goal.

Native host instructions, project instructions, skills, and memory can supply context.
They cannot change GLBuilding role duties or owner authority.

## Goal architecture

```mermaid
sequenceDiagram
    participant O as Orchestrator
    participant E as Explorer
    participant B as Builder
    participant R as Reviewer
    O->>O: Record goal, criteria, scope, and isolation
    opt Material repository question
        O->>E: One bounded question
        E-->>O: Evidence and uncertainty
    end
    O->>B: Goal, allowed paths, evidence, checks
    B-->>O: Diff, results, uncertainty
    O->>R: Goal, complete diff, results
    alt Pass
        R-->>O: Criterion checks and pass
        O->>O: Final verification and completion
    else Repair below cap
        R-->>O: Scoped findings
        O->>B: Findings and current task
    else Blocked
        R-->>O: Missing evidence or authority
    end
```

The task record contains outcomes, not whole conversations. Activation modes enter this
same flow; questions do not create goals.

## Why no runtime graph framework

Runtime graph systems can provide durable checkpoints, human interrupts, and long-term
stores. They also add code, serialization, storage, deployment, and operations.
GLBuilding does not need those components to test its first claim. Add a runtime only
after real goals show that Markdown, native agents, and Git cannot provide the result.

## External research

- The [Agent Skills specification](https://agentskills.io/specification) supports a
  portable `SKILL.md` entrypoint and progressive loading.
- OpenAI's [harness engineering report](https://openai.com/index/harness-engineering/)
  warns that one large `AGENTS.md` can crowd task and repository context.
- OpenAI's [agent-loop explanation](https://openai.com/index/unrolling-the-codex-agent-loop/)
  explains how project instructions and skills enter Codex context.
- Claude Code documents [version-controlled project instructions](https://code.claude.com/docs/en/memory)
  and [isolated subagents](https://code.claude.com/docs/en/sub-agents).
- Git documents how [worktrees](https://git-scm.com/docs/git-worktree.html) provide
  separate working trees while sharing repository state.
- [LangGraph](https://langchain-ai.github.io/langgraph/index.html) shows the runtime
  capabilities that GLBuilding deliberately defers.
- Microsoft's [AutoGen multi-agent debate pattern](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/multi-agent-debate.html)
  shows a peer graph. GLBuilding uses a hub because it needs handoffs, not open debate.

## Pitfalls and containment

### Ceremony cost

The main risk is that the framework becomes slower than the work. Configurer, Explorer,
and worktrees are conditional. Task records stay short. Dogfood measures setup, build,
review, and finalization separately.

### Stale project knowledge

Documentation can be wrong. Map and Validation remain hints. Agents verify material
claims in current code and state uncertainty instead of filling gaps.

### False fresh review

A Builder reviewing its own work preserves its assumptions. A supported harness uses a
different Reviewer context. A host that cannot do this is unsupported.

### Loop growth

Review rounds are capped at one to three, with two by default. Open findings at the cap
produce `blocked`, not another automatic loop.

### Partial installation

The Configurer shows the complete configuration and changed files, waits for approval,
rechecks affected paths, stages named files, and uses normal Git. A conflict stops the
install. The framework does not promise a database transaction. See the [installation
guide](INSTALLATION.md) and [System Configurer charter](../agents/SYSTEM_CONFIGURER.md).

### Dirty or concurrent work

Unrelated owner work is preserved and can be isolated with a worktree. Relevant dirty
work must be committed or explicitly included before isolation. Overlapping goals are
serialized because filesystem separation does not prevent design conflicts.

### False durability

A local commit survives only where that Git history survives. Remote persistence uses
the project's normal owner-approved Git flow.

### Harness variance

Codex and Claude can interpret the same Markdown differently. Test each harness on the
simple workflow. Record `supported`, `unsupported`, or `untested`; do not infer parity.
The framework does not add provenance machinery to force obedience.

## Evaluation

GLBuilding succeeds only when it improves delivery:

- fewer owner routing steps and corrections;
- equal or better acceptance coverage;
- one independent review before completion;
- no unbounded repair loop;
- lower elapsed time or owner attention than the prior unstructured process.

Dogfood records setup, build, review, finalization, owner input, findings, repairs, scope
escapes, and remaining uncertainty. One successful run is directional evidence, not
general proof.
