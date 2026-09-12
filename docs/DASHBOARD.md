# Task dashboard

The dashboard is an optional, read-only view of existing Olympus task records. It uses
Python 3's standard library and generates one self-contained HTML file. It adds no
scheduler, database, project dependency, or agent authority.

The generator requires Python 3.10 or later on macOS or Linux. It uses Unix file-opening
flags to reject symlink records. Windows is not supported by this version.

From the framework checkout, generate a snapshot:

```sh
python3 scripts/dashboard.py --root /path/to/project --output /path/to/status.html
```

Open the generated file in a browser. No web server is required. The output directory
must be separate from the task records. The generator refuses to replace existing files
unless they carry its generated-file marker.

The HTML includes full original task records and the local source path. Keep it local
unless that content is suitable for sharing.

To rebuild after records change, keep this command running in a terminal:

```sh
python3 scripts/dashboard.py --root /path/to/project --output /path/to/status.html --watch 2
```

This foreground process checks for changes every two seconds. Stop it with Ctrl+C.
Refresh the browser to load the latest generated snapshot. The page displays its generation
time and source directory. There is no automatic host registration or background service.
Alternatively, run the one-shot command after an Orchestrator checkpoint.

## Source and interpretation

The generator reads only `.olympus/tasks/*.md` under the explicit source root. Use the
checkout that actually holds the task records. A goal worktree does not necessarily hold
records maintained in the main checkout. The generator does not scan other worktrees,
follow links, or collect data from other projects.

- Each record supplies one card. Explicit member-goal links can include related records
  when a goal is selected. Free-form plans do not become invented subtasks.
- Canonical frontmatter status is displayed as recorded. Unknown and legacy status values
  remain visible, with the original text in task details.
- Stage is shown only when an explicit frontmatter `stage` names `Prepare`, `Build`, or
  `Verify`. Existing templates do not require this field. Records without it appear under
  **Stage unknown**. Historical sections never prove a task's current stage.
- **Needs you** comes from a structured owner-decision row with a pending owner response.
  A later response for the same decision replaces the earlier pending response for this
  display. Completed and cancelled tasks do not receive this highlight.
- Role participation comes from recorded Actual values. It does not prove that an agent
  is running now. Missing participation remains unknown.
- The details panel includes the source path, file modification time, and original record
  as plain text. Modification time is not a heartbeat or a verified completion time.

The records remain the source of truth. The dashboard never changes them, approves a
request, starts an agent, or changes a goal. Unsupported or malformed data produces a
visible warning instead of a guessed success state. Historical statements in the source
are not refreshed against GitHub, Git, or an agent host.

## Limits and validation

This is a best-effort filesystem snapshot. It detects files that change during a read,
but it does not establish a transaction across several independently changing records.
Watch mode can reflect the next completed write. Symlink records are not followed.

The HTML template is `templates/DASHBOARD.html`. Record text is embedded as escaped JSON
and displayed as text, not executed as HTML or Markdown instructions.

Run the focused checks from the framework checkout:

```sh
python3 -m unittest discover -s tests -p 'test_dashboard.py'
```

Release preparation on 2026-09-12 passed all 14 tests on macOS with Python 3.14.4.
An isolated sample build verified watch updates from Active to Reviewing to Complete.
Browser checks at 1440px and 390px covered search, attention and status filters, task
details, Escape focus handling, and horizontal overflow. Independent review found an
indented-code parsing defect; the fix passed regression tests and focused re-review.
This validates the local dashboard flow, not live swarm execution or Windows support.
