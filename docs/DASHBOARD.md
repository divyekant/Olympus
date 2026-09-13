# Task dashboard

The dashboard is fixed HTML, CSS, and JavaScript. Open `index.html` directly in desktop
Chrome. It loads a sibling `tasks-data.js` file as a classic script. No web server,
folder picker, framework, or model call is needed to display or refresh the view.

The data file is a disposable export of existing `.olympus/tasks/*.md` records. Python
reads those records; it does not maintain another task list or control agents. Task
record instructions and validation are defined in the
[task-record contract](../references/PROTOCOL.md#task-record-contract).

## Start once

From the framework checkout, run:

```sh
python3 scripts/dashboard.py --root /path/to/project --output /path/to/dashboard/index.html --watch 2
```

Then open the output `index.html` in Chrome. The exporter creates the HTML and its data
file together. It changes HTML only when the framework template changes. Watch mode
checks source files every two seconds and exports data after a change. The open page
checks that data file every two seconds and updates its view without a full page reload.
Allow roughly four seconds after a completed record write. Checks pause while the tab
is hidden and resume when it becomes visible.

There is no per-turn user command. Keep this foreground exporter running during work;
Ctrl+C stops it. Without `--watch`, the command exports one snapshot. This is not an
installed background service or an automatic host integration. If the exporter stops,
the dashboard retains its last export time; it cannot prove that an agent is still running.
A missing or unreadable data file shows a warning and retains the last loaded snapshot.

The exporter requires Python 3.10 or later on macOS or Linux. Windows export is not
supported by this version. The browser view uses no network fetch or module import.
The HTML and data file must remain together. Never edit the exported JavaScript by hand;
it contains serialized data and a fixed assignment, not agent-generated code.

Both files contain or expose task information, including full source records and local
paths. Keep them local unless that information is suitable for sharing. The exporter
refuses unsigned existing output files, symlinks, and protected record paths.

## Validate task records

```sh
python3 scripts/dashboard.py --root /path/to/project --validate-only
```

This read-only check reports invalid schema 2 fields, contradictory owner-action state,
unresolved task references, and invalid parent relationships. It does not rewrite files.
Schema 1 and legacy records are reported as skipped. Passing structure checks does not
prove that an agent's claims, timestamps, external state, or approvals are true.

## What the view means

- Each task supplies one card. Supporting `.spec.md` and `.plan.md` files are excluded.
- Schema 2 frontmatter supplies the current title, status, parent, related tasks, owner
  action, checkpoint time, and product phase. Children are derived from parent IDs.
  The original evidence and history remain available in task details.
- Legacy formats remain readable, including observed Claude `# Goal` headings and
  top-level owner-request tables. Missing and unsupported state remains Unclassified.
  The dashboard never infers completion from prose or old pull-request references.
- Delivery defaults to status. Optional stage grouping requires explicit `Prepare`,
  `Build`, or `Verify` values. No recorded stages means no stage grouping.
- Product phases are discovery, decision, execution, awaiting evidence, evaluation, and
  closed. Product phase is separate from delivery status. Legacy product checkpoint
  tables remain supported. A completed build does not prove a product outcome.
- Pending owner actions are highlighted. Missing legacy decision data shows incomplete
  coverage rather than an implied absence of owner actions.
- The rail shows seven recent goals, omitting known completed work. Search and the goal
  selector retain access to all tasks. Completed work and long columns are collapsible.
- Explicit related-task links and exact narrative task references are navigable. Narrative
  references never establish ownership. Role participation never claims live activity.

Choose the checkout holding the records. A running Claude session or a task worktree may
have none. The exporter does not discover sessions, combine worktrees, follow source
symlinks, or collect data from other projects. Its snapshot detects individual files
changing during reads, but is not a transaction across several task records.

## Verification

```sh
python3 -m unittest discover -s tests -p 'test_dashboard.py'
```

Initial synthetic checks missed real-record compatibility defects. Corrected historical
Claude validation yielded 45 task records, excluded 21 supporting documents, recovered
33 descriptions, and exposed exact references in eight records. That source still has
20 unsupported or missing status values and no supported role or owner-decision tables.
It is historical evidence, not live swarm validation. Do not rewrite historical source
records merely to improve their appearance in the dashboard.
