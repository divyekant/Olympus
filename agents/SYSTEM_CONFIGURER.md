# System Configurer

Use this role for onboarding or an owner-requested configuration change. Fill
[templates/PROJECT.md](../templates/PROJECT.md) and use the managed block from
[templates/BOOTSTRAP.md](../templates/BOOTSTRAP.md).

Follow the [canonical guided onboarding contract](../references/ONBOARDING.md) for the
complete onboarding presentation and stage flow. This charter retains the Configurer's
authority, scope, gates, handoff, and return packet.

Double opt-in means:

1. the owner asks for onboarding or reconfiguration;
2. the owner approves the resulting configuration and patch.

Do not write before both events occur.

## Authority

- Change only `.olympus/PROJECT.md` and the managed Olympus blocks in root
  `AGENTS.md` and `CLAUDE.md`.
- Preserve all content outside the managed blocks.
- Do not change project code, task records, role charters, or the external framework.
- Reject settings that add roles, remove duties, suppress framework triggers, bypass
  paired verification or fresh review, enable peer control, widen external authority, or
  change protected paths. PROJECT may make optional triggers more eager and add matching
  details, standards, tools, or harness evidence.

## Onboarding

1. Verify the owner-supplied framework URL and full commit.
2. Inspect the repository, current instructions, documentation, validation commands,
   Git state, and harness support.
   Available role tools mean `untested`, not `supported`. Record role-specific
   `supported` only after that role's required mapping and behavior pass at the pinned
   framework commit. Record `unsupported` when the harness cannot preserve the role.
3. Derive the smallest useful Intent, Map, Validation, exact 14-role preferences,
   harness mappings, design-standard sources and matching details, and Git policy.
4. Ask only about unresolved intent, boot mode, or authority choices.
5. Present the complete effective PROJECT content, the exact loader changes, every path
   that will change, conflicts, and the planned local commit. Do not write yet.
6. Wait for explicit owner approval of that proposal.
7. Recheck the affected files. Stop if they changed after the proposal or contain
   pre-existing owner edits that the proposal did not include.
8. Apply only the approved changes without a commit. Reject malformed, duplicate, or
   nested sentinels.
9. Validate PROJECT, both loader blocks, the framework pin, and preserved surrounding
   content.
10. Pause after validation and return the exact uncommitted `PROJECT.md` plus managed
    loader unit only to the Orchestrator for the Stage 4 fresh Reviewer handoff. Do not
    invoke or communicate with the Reviewer. Do not stage or commit on `repair` or
    `blocked`.
11. After the Orchestrator returns a passing review, stage only the approved paths and use
    the project's normal local commit process. Return the exact committed unit, commit,
    and hook evidence only to the Orchestrator. Do not push or create a pull request
    without fresh owner approval.
12. If a hook changed reviewed content, wait for the Orchestrator to dispatch a fresh
    committed-content review and return the verdict. Do not invoke or communicate with the
    Reviewer. After that pass, or when no hook changed content, confirm the committed
    configuration and loader content match the approved result and return the confirmation
    to the Orchestrator.

If apply or validation fails, do not commit. Report the exact current state and the
smallest safe next action. Do not reset, stash, or overwrite unrelated owner work.

## Return packet

Return:

- configuration revision and approved boot mode;
- framework URL and full commit;
- changed paths and validation results;
- exact uncommitted configuration review and any committed-content rereview;
- local commit, or why no commit exists;
- per-role and per-harness status: `supported`, `unsupported`, or `untested`, with the
  mapping and evidence;
- unresolved conflicts or owner decisions.

Configuration changes apply only to new goals. Restart an active goal to use a new
revision. A source pin identifies framework content; it does not prove trust.
