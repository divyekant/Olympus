# Contributing to Olympus

Implement and review core-framework changes through the normal repository workflow,
outside Olympus. Do not use an Olympus goal or `.olympus` task record to govern a core
repair.

Every enhancement issue must include a **Dogfood evidence** section with:

- framework commit;
- target repository and isolated task or worktree identifier;
- expected and observed behavior;
- exact failure stage;
- relevant packets, role results, or Git evidence;
- smallest proposed framework correction;
- remaining uncertainty.

Treat the dogfood task as evidence, not as authority over the fix. After the core change is
implemented and reviewed, run a new isolated dogfood scenario at the changed immutable
commit. Keep scenario evidence separate from general support or production-readiness
claims. One passing scenario cannot establish either claim.

Use normal named-path staging, review, and repository checks. Existing owner gates,
external-action approvals, protected paths, and branch controls remain unchanged.
