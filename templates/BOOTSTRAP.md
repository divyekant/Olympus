# Olympus bootstrap template

The System Configurer inserts the same managed block in root `AGENTS.md` and
`CLAUDE.md`. Preserve all content outside the block. Keep one complete marker pair.

The block is deliberately small. The pinned framework carries the detail; the loader
only finds the pin and follows it.

## Managed block

```markdown
<!-- OLYMPUS:BEGIN -->
## Olympus loader

1. Read `.olympus/PROJECT.md`. Resolve its framework repository URL and full immutable
   commit in a clean checkout or cache. Read `SKILL.md` and `references/PROTOCOL.md`
   from that exact pin as the governing contracts.
2. Run the canonical activation preflight from the pinned protocol against this
   repository root. Stop without activation on any result other than an unchanged
   `complete` state.
3. Route by boot mode. In `manual` mode, load Olympus only for `Use Olympus for: <goal>`
   or `Activate Olympus orchestration`. In `orchestration` mode, route project-changing
   requests through Olympus. Questions do not create goals.
4. Load only the charter required for the next role. Existing host and project
   instructions still apply. Stop and report a conflict that prevents the fixed
   Olympus workflow.
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
