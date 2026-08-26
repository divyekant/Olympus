# GLBuilding bootstrap template

The System Configurer inserts the same managed block in root `AGENTS.md` and
`CLAUDE.md`. Preserve all content outside the block. Keep one complete marker pair.

## Managed block

```markdown
<!-- GLBUILDING:BEGIN -->
## GLBuilding loader

1. Read `.glbuilding/PROJECT.md`.
2. In `manual` boot mode, load GLBuilding only for `Use GLBuilding for: <goal>` or
   `Activate GLBuilding orchestration`.
3. In `orchestration` boot mode, route project-changing requests through GLBuilding.
   Questions do not create goals.
4. Resolve the exact framework repository URL and full commit recorded in PROJECT in a
   clean checkout or cache. Do not read a newer source working tree.
5. Stop if the exact commit is unavailable or the resolved checkout is mismatched or dirty.
6. Read `SKILL.md` and `references/PROTOCOL.md` from that framework version.
7. Load only the charter required for the next role.
8. Existing host and project instructions still apply. Stop and report a conflict that
   prevents the fixed GLBuilding workflow.
<!-- GLBUILDING:END -->
```

## Validation

Confirm:

- PROJECT exists and records `manual` or `orchestration`;
- both loader files contain one complete marker pair;
- content outside the managed blocks is unchanged;
- the recorded source URL and full commit resolve to a clean, readable GLBuilding pack;
- the harness can run a separate Builder and fresh Reviewer.
