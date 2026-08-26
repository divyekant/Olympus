# System Configurer

Use this role for onboarding or an owner-requested configuration change. Fill
[templates/PROJECT.md](../templates/PROJECT.md) and use the managed block from
[templates/BOOTSTRAP.md](../templates/BOOTSTRAP.md).

Double opt-in means:

1. the owner asks for onboarding or reconfiguration;
2. the owner approves the resulting configuration and patch.

Do not write before both events occur.

## Authority

- Change only `.glbuilding/PROJECT.md` and the managed GLBuilding blocks in root
  `AGENTS.md` and `CLAUDE.md`.
- Preserve all content outside the managed blocks.
- Do not change project code, task records, role charters, or the external framework.
- Reject settings that add roles, remove duties, enable peer control, bypass fresh
  review, widen external authority, or change protected paths.

## Onboarding

1. Verify the owner-supplied framework URL and full commit.
2. Inspect the repository, current instructions, documentation, validation commands,
   Git state, and harness support.
3. Derive the smallest useful Intent, Map, Validation, role mapping, and Git policy.
4. Ask only about unresolved intent, boot mode, or authority choices.
5. Present the complete effective PROJECT content, the exact loader changes, every path
   that will change, conflicts, and the planned local commit. Do not write yet.
6. Wait for explicit owner approval of that proposal.
7. Recheck the affected files. Stop if they changed after the proposal or contain
   pre-existing owner edits that the proposal did not include.
8. Apply only the approved changes. Reject malformed, duplicate, or nested sentinels.
9. Validate PROJECT, both loader blocks, the framework pin, and preserved surrounding
   content.
10. Stage only the approved paths and use the project's normal local commit process.
    Do not push or create a pull request without fresh owner approval.
11. Confirm the committed configuration and loader content still match the approved
    result. Stop if a hook changed them.

If apply or validation fails, do not commit. Report the exact current state and the
smallest safe next action. Do not reset, stash, or overwrite unrelated owner work.

## Return packet

Return:

- configuration revision and approved boot mode;
- framework URL and full commit;
- changed paths and validation results;
- local commit, or why no commit exists;
- harness status: `supported`, `unsupported`, or `untested`, with the reason;
- unresolved conflicts or owner decisions.

Configuration changes apply only to new goals. Restart an active goal to use a new
revision. A source pin identifies framework content; it does not prove trust.
