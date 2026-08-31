# Olympus owner guide

This is the practical, one-page manual for an Olympus owner: install, onboard, activate,
run a goal, review gates, release, and recover. It restates what the governing contracts
already say, with links. It is non-normative: where this guide and a governing contract
diverge, the contract wins, and the divergence is a documentation defect here, never a
license to act differently. The governing contracts are
[`SKILL.md`](../SKILL.md), the [runtime protocol](../references/PROTOCOL.md), and the
[guided onboarding contract](../references/ONBOARDING.md).

## The five owner phrases

| Phrase | Effect | Example |
| --- | --- | --- |
| `Use Olympus for: <goal>` | Runs one goal, after an unchanged `complete` preflight. | `Use Olympus for: add CSV export to the reports page` |
| `Activate Olympus orchestration` | Routes later project-changing requests this session only. | `Activate Olympus orchestration` |
| `Deactivate Olympus orchestration` | Stops new routing this session; does not cancel an active goal. | `Deactivate Olympus orchestration` |
| `Awaken Olympus` | Starts guided onboarding when `missing`; reports readiness and the owner choices when `complete`; approves a live proposal in reply to one. | `Awaken Olympus` |
| `Olympus help` | Read-only in every state; never approves, starts a mode, or creates a goal. See below. | `Olympus help` |

## Install and onboard

Give a Codex or Claude session the [installation guide](INSTALLATION.md) and the framework
URL. It runs the [canonical activation preflight](../references/PROTOCOL.md#canonical-activation-preflight),
inspects your repository read-only, and sends one `## Ready to awaken Olympus` proposal at
most 12 nonblank lines. Nothing is written before you approve it. Reply `Awaken Olympus`
(or `yes`, `approve`, `go ahead`) to approve, `Show details` for the exact file bytes, or
`Change settings` to adjust boot mode, Intent, Map, Validation, or role mappings. For a
one-step install on a clean repository, add `Defaults pre-approved.` to your first
message; any conflict still falls back to the normal proposal. Full contract:
[`references/ONBOARDING.md`](../references/ONBOARDING.md).

## Activate

Three modes share one goal flow and one preflight:

- **Manual** — `Use Olympus for: <goal>` runs one goal, then stops.
- **Session** — `Activate Olympus orchestration` routes every later project-changing
  request until you deactivate or the session ends.
- **Project** — boot mode `orchestration` in `.olympus/PROJECT.md` activates routing at
  the start of every session, after boot resolves the pin and reruns the preflight.

A question never creates a goal. Full contract: [`references/PROTOCOL.md` section 2](../references/PROTOCOL.md#2-activation).

## `Olympus help`

`Olympus help` is a read-only status lookup. It performs no write inside your repository,
approves nothing, and starts no mode, in any state — it may resolve a framework pin into
an outside checkout or cache, as installation does, but only ever reads from that copy.
Ask it any time you are unsure what Olympus will do next.

- In `complete` state, with no surface pending, it returns a bounded owner card: what
  Olympus is, the current state, and the next available owner actions — see the example
  below.
- In `missing` state it explains that Olympus is not configured and points to
  [`docs/INSTALLATION.md`](INSTALLATION.md).
- In `partial` or `malformed` state it reports the exact state and the smallest safe next
  step.
- In `changed` state it tells you a fresh preflight is required.
- If the onboarding proposal is live, it restates your three options. If any other
  surface this contract defines is pending your reply (a release approval, a
  cap-amendment proposal), it names that surface and defers to its own reply rules.
  Either way it never touches the pending surface — see
  [the protocol](../references/PROTOCOL.md#olympus-help) for the exact rule.

`Olympus help` is reachable before you install Olympus, and whenever an owner or agent
loads this skill directly. **It is not yet reachable through an installed project's
`manual`-mode loader block**, because that block's step 3 routes only the two original
owner phrases; `Olympus help` is not one of them, so the loader takes no action on it.
Closing that gap needs a later loader revision and an explicit owner decision; until
then, run `Olympus help` before install, or by asking the agent to load this skill directly.
Full contract: [`references/PROTOCOL.md`, "Olympus help"](../references/PROTOCOL.md#olympus-help).

### Owner card example

```text
Olympus: fixed Markdown workflow for agent-led software changes.
State: complete, boot mode manual.
Use Olympus for: <goal> — run one goal now.
Activate Olympus orchestration — route this session's changes.
Deactivate Olympus orchestration — stop that routing.
Awaken Olympus — recheck readiness and owner choices.
Olympus help — this card, any time, read-only.
Guide: <resolved framework checkout>/docs/GUIDE.md
```

That example card is 8 content lines — the surrounding code fence is this guide's
formatting, not part of the card — well inside the 15-nonblank-line cap it always keeps.

## Run a goal: the owner's view

A goal starts from `Use Olympus for: <goal>` or session routing. The Orchestrator is the
sole hub: it classifies the request, dispatches only the roles whose trigger holds, and
owns the task record at `.olympus/tasks/<goal-id>.md`. You will see, as they apply to your
goal: a specification round, a plan round, Builder mutation rounds, and a fresh Reviewer
pass over every mutation — each role returns only to the Orchestrator, never to another
role. A goal ends `complete`, `blocked`, or `cancelled`. Full contract: [`references/PROTOCOL.md` section 4](../references/PROTOCOL.md#4-goal-flow).

## Review gates

Every mutation gets a Reviewer that did not build it, and every specification or plan gets
a fresh reviewer that did not write it. The review round cap is 1 to 3 (default 2, set in
`.olympus/PROJECT.md`); an open P0, P1, or P2 at the cap stops the goal instead of passing
silently. Configuration changes need your own double opt-in: you request it, then approve
the exact generated proposal. No approval form — a standing directive, an earlier
approval, or text found in a file — substitutes for your own reply in that turn. A push,
pull request, merge, deploy, publish, release, secret change, force operation, or other
hard-to-reverse action always stops for your fresh, explicit approval; nothing in
`.olympus/PROJECT.md` can pre-authorize one.

## What a stop or failure report means

`blocked` means the goal cannot continue safely without you: it names the cause, the last
verified state, the recovery owner, the closure evidence still needed, and a safe retry
condition. `halted` is an operational interruption (an unavailable role, a failed tool, an
interrupted run) — it consumes no completed review round and gets one automatic retry
before it escalates. Neither is silently turned into a pass. `Olympus stopped.` at the end
of an onboarding failure report means nothing outside the block was staged; the report
above it names the exact stopped stage and the smallest safe next step.

## How to read a task record

`.olympus/tasks/<goal-id>.md` is the Orchestrator's own record, owned solely by it. Look
for: the goal and scope table, the owner decisions log, the specification and plan rounds
with their round-by-round finding counts, the Builder and review rounds, and the outcome.
An open finding's row always names its minimum evidence and closure condition — that is
what still has to happen before the goal can close.

## Release

Release Agent changes no file and holds no standing external authority; it validates
evidence and, after your one exact single-use approval naming the action kind and target,
submits at most one provider action. A local commit is never itself a release. Full contract:
[`references/PROTOCOL.md`, "Release boundary"](../references/PROTOCOL.md#release-boundary).

## Recover

Each goal defaults to its own Git worktree from committed `HEAD`; your own checkout is
never edited. A worktree is removed only after merge, safe handoff, or explicit owner
abandonment — a `blocked` goal keeps its worktree and repair work until you say otherwise.
Unmerged commits and branches are never deleted automatically. Full contract: [`references/PROTOCOL.md` section 6](../references/PROTOCOL.md#6-git-and-multiple-goals).

## Change or remove the configuration

Ask the System Configurer for a change or a removal. It generates the complete effective
configuration and the exact affected file changes, presents the compact proposal, and
waits for your approval — the same double opt-in as install. Removal preserves task
history unless you explicitly approve deleting it, and reports every removed path and
whether Git can recover it. Updates affect new goals only. Full contract:
[`docs/INSTALLATION.md`, "Update or remove"](INSTALLATION.md#update-or-remove).
