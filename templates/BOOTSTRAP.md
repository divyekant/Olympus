# GLBuilding Bootstrap Template

Copy the same managed block, byte for byte, into the target `AGENTS.md` and
`CLAUDE.md`. The System Configurer is the only role that inserts or changes it.
Keep the sentinel lines exact. Do not place one block inside another block or add
a second block to either file.

## Managed block

```markdown
<!-- GLBUILDING:BEGIN -->
## GLBuilding loader

1. Read `.glbuilding/PROJECT.md` and its boot mode. In `manual`, continue only when
   the owner invokes one GLBuilding goal or says `Activate GLBuilding orchestration`.
   Otherwise do not load GLBuilding. In `orchestration`, route project-changing
   requests automatically. Questions do not create goals. An invalid mode blocks.
2. Read the canonical framework source URL and full immutable commit from PROJECT.
   The pin identifies intended bytes; it is not a security trust anchor.
3. Find the host's cached GLBuilding checkout. Verify its origin URL and `HEAD` are
   exact matches for the recorded URL and full commit. Require an empty Git status,
   including staged and untracked changes. If the checkout is absent, dirty, or
   mismatched, fetch a clean checkout of that exact commit and verify again.
4. Never fetch or resolve `latest`, `main`, a floating tag, or a short commit. If Git,
   the source, the exact commit, the checkout, or this loader is unavailable or does
   not match, stop with task status `blocked`.
5. Load `SKILL.md` from the verified checkout. Load its protocol, then only the charter
   or template required for the current stage. A session deactivation is temporary;
   only an approved configuration change persists.
<!-- GLBUILDING:END -->
```

## Installation and validation

- Insert exactly one `GLBUILDING:BEGIN` and one `GLBUILDING:END` marker in each file.
- Preserve all content outside the managed block. Do not overwrite concurrent edits.
- Before writing, hash the complete file and show the exact insertion or replacement
  patch with its preimage and postimage SHA-256 values.
- After writing, verify the marker count, byte-for-byte block text, and loader references.
- If either file has malformed, duplicate, nested, or concurrently changed markers,
  stop and report `blocked`. Do not repair the file during onboarding.
- The source URL and commit remain only in `.glbuilding/PROJECT.md`; the loader does
  not copy or infer a floating source identity.

See the shared [runtime protocol](../references/PROTOCOL.md) for source, approval,
capability, Git, and recovery rules.
