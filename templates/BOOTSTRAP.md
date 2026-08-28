# Olympus bootstrap template

The System Configurer inserts the same managed block in root `AGENTS.md` and
`CLAUDE.md`. Preserve all content outside the block. Keep one complete marker pair.

## Managed block

```markdown
<!-- OLYMPUS:BEGIN -->
## Olympus loader

1. Begin the first consistency bracket before the initial PROJECT sample.
2. Inside that open bracket, sample identities for `.olympus/PROJECT.md`, root `AGENTS.md`,
   and root `CLAUDE.md`. Read PROJECT or use a complete owner/request URL and full commit.
   Resolve the exact framework repository URL and full commit in a clean checkout or cache.
   Sample the resolved checkout path, commit, readability, and clean status. Read
   `SKILL.md` and `references/PROTOCOL.md` as pinned contracts from that framework
   version, then read both managed units, canonical loader bytes, and checkout evidence.
   Repeat the exact target and checkout samples. Record invalid pin evidence for unavailable,
   mismatched, or dirty pins and complete the bracket before classification.
3. Close the bracket only when all before and after samples match. An unstable capture
   returns `changed` and requires fresh preflight. Only a coherent first capture may
   classify. Stable invalid pin evidence is classified as `malformed` only after the
   coherent final capture.
4. Run the canonical activation preflight from the pinned protocol against the target
   repository root using the coherent first capture.
5. Run the immediate final recheck from that preflight. Perform the coherent final capture
   under the same bracket rules and bind its result.
6. Only after the final capture returns an unchanged `complete` state, route the requested
   entry: in `manual` boot mode, load Olympus only for `Use Olympus for: <goal>` or
   `Activate Olympus orchestration`; in `orchestration` boot mode, route project-changing
   requests through Olympus. Questions do not create goals. `missing`, `partial`,
   `malformed`, or `changed` results stop without activation.
7. Load only the charter required for the next role.
8. Before dispatch, confirm a role-specific harness mapping, freshness, tools, support
   status, and evidence for every invoked role. Missing mapping blocks the goal.
9. For configuration, require System Configurer support and a fresh Reviewer mapping for
   the exact uncommitted configuration unit before staging or commit.
10. Existing host and project instructions still apply. Stop and report a conflict that
    prevents the fixed Olympus workflow.
<!-- OLYMPUS:END -->
```

## Validation

Confirm:

- PROJECT exists and records `manual` or `orchestration`;
- both loader files contain one complete marker pair;
- content outside the managed blocks is unchanged;
- the recorded source URL and full commit resolve to a clean, readable Olympus pack;
- the harness has role-specific support for every invoked role;
- mutation goals have a separate Builder and fresh Reviewer;
- configuration goals have a System Configurer and fresh Reviewer for the exact unit.
