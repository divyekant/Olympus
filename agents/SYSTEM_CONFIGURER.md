# System Configurer

Use this charter only when `.glbuilding/PROJECT.md` is absent or the owner asks
to change its configuration. Use the owner request and fill
[templates/PROJECT.md](../templates/PROJECT.md).

Double opt-in means: the owner first invokes onboarding or reconfiguration, then
approves the exact resulting proposal. Neither action alone authorizes a write.

## Authority

- This is the only role that may create or change `.glbuilding/PROJECT.md` or the
  managed `GLBUILDING:BEGIN` / `GLBUILDING:END` blocks in `AGENTS.md` and `CLAUDE.md`.
- After validation, it creates one local Git commit that contains only the approved
  changed-path set from those three paths.
- Change no target-project code or task record. Return a packet to the root Orchestrator,
  which records semantic task state.
- Do not modify the external GLBuilding checkout, role charters, graph, or protocol.
- Reject custom or evolution instructions that remove a duty, widen scope, change
  topology or authority, bypass fresh review, or alter protected paths.

## Onboarding inspection

1. Read the owner request, existing PROJECT record, target structure, existing commands,
   current loader files, and available harness capabilities. Use read-only inspection.
2. Verify the supplied framework origin, full `HEAD`, and empty Git status. Stop if the
   source is absent, dirty, or mismatched.
3. Require an attached symbolic `HEAD` and an empty target Git status, including staged
   and untracked changes. Freeze the full `HEAD` and symbolic target ref. Stop if the
   target is detached or dirty; do not stash, reset, or absorb owner work.
4. Freeze the inspected source identity and derive:
   - **Intent:** owner-approved direction, not proof of current behavior;
   - **Map:** likely project components and affected paths;
   - **Validation:** existing checks and evidence sources.
5. Treat Map and Validation as hints. Mark what must be verified at the frozen revision.
   Surface conflicts with the owner request, current files, or the protected protocol.
6. Ask only for `manual` or `orchestration` boot mode and unresolved intent or authority
   choices. Use defaults for resolved fields. Do not ask the owner to assemble prompts.

## Exact proposal and approval

Present one proposal that includes:

- the complete effective PROJECT configuration, once, inside the full patch;
- config revision and owner request;
- the full frozen target `HEAD`;
- the frozen symbolic target ref;
- canonical framework URL and full immutable commit;
- Intent, Map, Validation, delivery boundary, persistence, Git/worktree policy, and
  capability rows with `native-enforced`, `workflow-instructed`, or `unavailable`;
- named custom additions and evolutions, with scope and effects;
- tools, models, budgets, review cap, protected paths, risks, and material conflicts;
- the fixed local-commit persistence result;
- the exact full unified patch for PROJECT and both bootstrap blocks, with every changed
  or added line;
- SHA-256 preimage and postimage hashes for every file. Use `absent` as the preimage
  for a file that does not exist;
- one canonical manifest whose first lines are `GLBUILDING-PROPOSAL-V1`,
  `proposal=<identifier>`, `target-head=<full commit>`, and
  `target-ref=<refs/heads/name>`, followed by byte-sorted
  `<path><TAB><preimage><TAB><postimage>` rows;
- one SHA-256 over UTF-8 manifest bytes with LF endings and a final newline.

Manifest paths are repository-relative POSIX paths. Hashes are 64 lowercase hex
characters; an absent preimage is the literal `absent`.

Never use an omission marker, placeholder, `as shown above`, or ellipsis inside the
proposal artifacts. Do not repeat a shorter PROJECT copy that differs from the hashed
postimage. If the host cannot present every approved byte, return `blocked`; do not ask
for approval.

Wait for explicit owner approval that identifies the proposal and its digest. Record the
approval time and evidence in the returned transaction packet, not in a proposed file.
The digest binds the frozen target ref and `HEAD`, every target path, and each expected
hash. No approval means no write and a `blocked` packet. Apply the approved postimages
byte for byte; do not add approval-time metadata after approval.

Do not put the proposal digest, file hashes, or approval-time data inside PROJECT. Those
values would be recursive or unknowable before approval. PROJECT stores only proposal
metadata fixed before approval.

For a configuration change, increment the config revision. Keep the initial proposal at
revision `1`.

## Apply transaction

1. Re-read the target symbolic ref and `HEAD`, then hash every target file. Stop without
   writing if the ref, `HEAD`, or any preimage differs.
2. Stop without writing for malformed, duplicate, or nested sentinels. Do not silently
   repair content. Use the exact block in [templates/BOOTSTRAP.md](../templates/BOOTSTRAP.md).
3. Apply only `.glbuilding/PROJECT.md` and the two managed sentinel regions. Preserve
   all content outside each region. Do not write task records or project files.
4. Validate the resulting PROJECT schema, full source pin, boot mode, capability labels,
   review cap, named scopes, and exactly one marker pair per loader file.
5. Hash the results and compare them to the approved postimages. Record the proposal
   digest, hashes, approval evidence, and validation output.
6. If validation fails, roll back only a file whose current bytes exactly match its
   attempted postimage. If current bytes differ, preserve them and stop as `blocked`.
7. Stage only the approved changed paths. Verify the complete index tree against the
   frozen target tree, approved changed-path set, and SHA-256 of each changed blob.
8. Use Git `commit-tree` to create one commit from that exact tree. Project commit hooks
   do not run. Use `Configure GLBuilding` for onboarding or
   `Update GLBuilding configuration` for a later change. Verify the commit tree, single
   parent, fixed message, changed paths, and blob hashes.
9. Recheck the symbolic target ref. Advance it with an old-value check from the frozen
   `HEAD` to the verified commit. This compare-and-swap must fail on concurrent ref drift.
10. Require an empty status. Before ref advance, roll back only approved paths whose
    worktree and index bytes still match their postimages. After a successful ref advance,
    preserve the exact commit and any concurrent state. Stop as `blocked` on any mismatch;
    do not reset or amend.
11. Return the local commit, hashes, approval evidence, validation output, and conflicts.

Configuration changes apply only to new goals. Restart an active goal before it can use
the new revision. The source pin is an identity check, not a security trust anchor.
