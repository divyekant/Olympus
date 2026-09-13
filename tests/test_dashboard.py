import json
import contextlib
import io
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import dashboard


CANONICAL = """---
record: olympus-task
schema: 1
status: active
stage: Build
---
# Olympus task: `ACC-01`

## Goal and scope
Owner request: Choose the required profile fields.

## Owner decisions
| Decision | Owner response | Effect |
| --- | --- | --- |
| `profile fields` | pending | Form paused |
| profile fields | resolved | Form may continue |

### Role population and support
| Role | Support | Actual |
| --- | --- | --- |
| Builder | build | yes |
| Reviewer | review | Pending |
| <!-- placeholder --> | — | — |

## Sizing check
| Member goal identifier | Supersedes |
| --- | --- |
| account | none |

<!-- SPECIFICATION-BODY:BEGIN -->
## Owner decisions
| Decision | Owner response | Effect |
| spoof | pending | Never parse this |
<!-- SPECIFICATION-BODY:END -->
"""


class DashboardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.tasks = self.root / ".olympus" / "tasks"
        self.tasks.mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, text):
        path = self.tasks / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_collects_canonical_fields_and_ignores_body_tables(self):
        self.write("ACC-01.md", CANONICAL)
        payload = dashboard.collect(self.root)
        record = payload["records"][0]
        self.assertEqual(record["id"], "ACC-01")
        self.assertEqual(record["title"], "ACC-01")
        self.assertEqual(record["statusRaw"], "active")
        self.assertEqual(record["status"], "Active")
        self.assertEqual(record["stage"], "Build")
        self.assertEqual(record["request"], "Choose the required profile fields.")
        self.assertFalse(record["needs"])
        self.assertEqual(record["agents"], [["Builder", "Invoked (recorded)"], ["Reviewer", "Pending (recorded)"]])
        self.assertEqual(record["links"], ["account"])
        self.assertNotIn("spoof", json.dumps(record["decisions"]))
        self.assertTrue(record["raw"].startswith("---\n"))

    def test_unknown_status_preserves_raw_value_and_defaults_stage(self):
        self.write("legacy.md", "---\nrecord: olympus-task\nschema: 1\nstatus: done-ish\n---\n# Legacy\n")
        record = dashboard.collect(self.root)["records"][0]
        self.assertEqual(record["status"], "Unknown")
        self.assertEqual(record["statusRaw"], "done-ish")
        self.assertEqual(record["stage"], "Unknown")

    def test_schema2_contract_and_parent_member_links(self):
        self.write("parent.md", "---\n"
                   "record: olympus-task\nschema: 2\ntitle: Parent task\n"
                   "status: active\nkind: delivery\nparent: none\nlinked-tasks: []\n"
                   "owner-action: none\nupdated-at: 2026-09-13T10:00:00Z\n"
                   "product-phase: none\nstage: Build\n---\n")
        self.write("child.md", "---\n"
                   "record: olympus-task\nschema: 2\ntitle: Child task\n"
                   "status: active\nkind: delivery\nparent: parent\nlinked-tasks: [\"parent\"]\n"
                   "owner-action: pending\nupdated-at: 2026-09-13T10:01:00Z\n"
                   "product-phase: none\nstage: Verify\n---\n"
                   "## Goal and scope\nOwner request: Confirm the child scope.\n\n"
                   "## Owner decisions\n"
                   "| Decision | Owner response | Effect |\n| --- | --- | --- |\n"
                   "| choose scope | pending | Hold build |\n\n"
                   "### Role population and support\n"
                   "| Role | Support | Actual |\n| --- | --- | --- |\n"
                   "| Builder | build | yes |\n")
        payload = dashboard.collect(self.root)
        records = {record["id"]: record for record in payload["records"]}
        self.assertEqual(records["child"]["title"], "Child task")
        self.assertEqual(records["child"]["status"], "Active")
        self.assertEqual(records["child"]["parent"], "parent")
        self.assertEqual(records["child"]["updatedAt"], "2026-09-13T10:01:00Z")
        self.assertNotEqual(records["child"]["modifiedAt"], records["child"]["updatedAt"])
        self.assertEqual(records["child"]["request"], "Confirm the child scope.")
        self.assertEqual(records["child"]["agents"], [["Builder", "Invoked (recorded)"]])
        self.assertTrue(records["child"]["needs"])
        self.assertTrue(records["child"]["attentionKnown"])
        self.assertEqual(records["parent"]["links"], ["child"])
        self.assertEqual(payload["validationErrors"], [])

    def test_schema2_invalid_references_cycles_and_malformed_records_stay_unknown(self):
        self.write("a.md", "---\n"
                   "record: olympus-task\nschema: 2\ntitle: A\nstatus: active\n"
                   "kind: delivery\nparent: b\nlinked-tasks: []\nowner-action: none\n"
                   "updated-at: 2026-09-13T10:00:00Z\nproduct-phase: none\n---\n")
        self.write("b.md", "---\n"
                   "record: olympus-task\nschema: 2\ntitle: B\nstatus: active\n"
                   "kind: delivery\nparent: a\nlinked-tasks: []\nowner-action: none\n"
                   "updated-at: 2026-09-13T10:00:00Z\nproduct-phase: none\n---\n")
        self.write("missing-ref.md", "---\n"
                   "record: olympus-task\nschema: 2\ntitle: Missing reference\nstatus: active\n"
                   "kind: delivery\nparent: none\nlinked-tasks: [\"missing\"]\nowner-action: none\n"
                   "updated-at: 2026-09-13T10:00:00Z\nproduct-phase: none\n---\n")
        self.write("malformed.md", "---\nrecord: olympus-task\nschema: 2\ntitle: Broken\nstatus: active\n")
        payload = dashboard.collect(self.root)
        records = {record["id"]: record for record in payload["records"]}
        self.assertEqual(records["a"]["status"], "Unknown")
        self.assertEqual(records["b"]["status"], "Unknown")
        self.assertEqual(records["malformed"]["status"], "Unknown")
        self.assertFalse(records["a"]["attentionKnown"])
        self.assertFalse(records["b"]["needs"])
        self.assertEqual(payload["legacyCount"], 0)
        self.assertTrue(payload["validationErrors"])
        self.assertTrue(any("missing" in error for error in payload["validationErrors"]))
        self.assertTrue(any("unclosed frontmatter" in error for error in payload["validationErrors"]))

    def test_schema2_product_and_terminal_owner_action_rules(self):
        self.write("product.md", "---\n"
                   "record: olympus-task\nschema: 2\ntitle: Product checkpoint\n"
                   "status: active\nkind: product\nparent: none\nlinked-tasks: []\n"
                   "owner-action: none\nupdated-at: 2026-09-13T10:00:00Z\n"
                   "product-phase: awaiting evidence\n---\n"
                   "## Shared state checkpoints\n| Product field | Record |\n| --- | --- |\n"
                   "| phase and trigger | awaiting evidence; collect proof |\n"
                   "| audience | Operators |\n")
        self.write("terminal.md", "---\n"
                   "record: olympus-task\nschema: 2\ntitle: Terminal checkpoint\n"
                   "status: complete\nkind: delivery\nparent: none\nlinked-tasks: []\n"
                   "owner-action: pending\nupdated-at: 2026-09-13T10:00:00Z\n"
                   "product-phase: none\n---\n## Owner decisions\n"
                   "| Decision | Owner response | Effect |\n| --- | --- | --- |\n"
                   "| close | pending | Wait |\n")
        records = {record["id"]: record for record in dashboard.collect(self.root)["records"]}
        self.assertEqual(records["product"]["kind"], "product")
        self.assertEqual(records["product"]["productPhase"], "awaiting evidence")
        self.assertEqual(records["product"]["product"]["audience"], "Operators")
        self.assertTrue(records["product"]["attentionKnown"])
        self.assertEqual(records["terminal"]["status"], "Unknown")
        self.assertFalse(records["terminal"]["attentionKnown"])

    def test_validate_only_reports_schema2_errors_and_skips_legacy(self):
        self.write("legacy.md", "# Goal `legacy` — Legacy\n")
        self.write("bad.md", "---\n"
                   "record: olympus-task\nschema: 2\ntitle: Bad\nstatus: active\n"
                   "kind: delivery\nparent: missing\nlinked-tasks: []\nowner-action: none\n"
                   "updated-at: 2026-09-13T10:00:00Z\nproduct-phase: none\n---\n")
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            result = dashboard.main(["--root", str(self.root), "--validate-only"])
        self.assertEqual(result, 1)
        self.assertIn("Skipped legacy records: 1", stdout.getvalue())
        self.assertIn("parent task is missing", stderr.getvalue())
        self.assertFalse((self.root / "index.html").exists())

    def test_validate_only_reports_missing_task_directory(self):
        missing_root = self.root / "missing-project"
        missing_root.mkdir()
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            result = dashboard.main(["--root", str(missing_root), "--validate-only"])
        self.assertEqual(result, 1)
        self.assertIn("Skipped legacy records: 0", stdout.getvalue())
        self.assertIn("task directory unavailable", stderr.getvalue())

    def test_pending_latest_decision_drives_attention(self):
        text = CANONICAL.replace("| profile fields | resolved | Form may continue |", "| profile fields | pending | Form paused again |")
        self.write("pending.md", text)
        record = dashboard.collect(self.root)["records"][0]
        self.assertTrue(record["needs"])
        self.assertEqual(record["decisions"][-1]["response"], "pending")

    def test_bundle_export_escapes_data_payload_and_preserves_source(self):
        source = self.write("xss.md", "# Olympus task: `xss`\n\n## Goal and scope\n<img src=x onerror=alert(1)> </script>\n")
        template = self.root / "DASHBOARD.html"
        template.write_text("<html><main>fixed template</main></html>", encoding="utf-8")
        output = self.root / "index.html"
        before = source.read_bytes()
        dashboard.write_dashboard(self.root, output, template)
        rendered = output.read_text(encoding="utf-8")
        self.assertIn("<!-- OLYMPUS-DASHBOARD:GENERATED -->", rendered)
        self.assertEqual(rendered, dashboard.SIGNATURE + "\n" + template.read_text(encoding="utf-8"))
        data = (self.root / "tasks-data.js").read_text(encoding="utf-8")
        self.assertTrue(data.startswith(dashboard.DATA_SIGNATURE + "window.olympusSnapshot = "))
        self.assertNotIn("<", data)
        payload = json.loads(data[len(dashboard.DATA_SIGNATURE + "window.olympusSnapshot = ") : -2])
        self.assertEqual(payload["records"][0]["raw"], before.decode())
        self.assertEqual(before, source.read_bytes())

    def test_data_refresh_keeps_fixed_index_stable(self):
        source = self.write("task.md", "# Goal `task` — First\n")
        template = self.root / "DASHBOARD.html"
        template.write_text("<html><main>fixed template</main></html>", encoding="utf-8")
        output = self.root / "index.html"
        dashboard.write_dashboard(self.root, output, template)
        first_index = output.read_bytes()
        first_index_mtime = output.stat().st_mtime_ns
        first_data = (self.root / "tasks-data.js").read_bytes()
        source.write_text("# Goal `task` — Changed\n", encoding="utf-8")
        dashboard.write_dashboard(self.root, output, template)
        self.assertEqual(output.read_bytes(), first_index)
        self.assertEqual(output.stat().st_mtime_ns, first_index_mtime)
        self.assertNotEqual((self.root / "tasks-data.js").read_bytes(), first_data)

    def test_unsigned_data_destination_blocks_bundle_before_index_write(self):
        self.write("task.md", "# Goal `task` — Task\n")
        template = self.root / "DASHBOARD.html"
        template.write_text("<html></html>", encoding="utf-8")
        (self.root / "tasks-data.js").write_text("window.olympusSnapshot = {}", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            dashboard.write_dashboard(self.root, self.root / "index.html", template)
        self.assertFalse((self.root / "index.html").exists())

    def test_missing_and_malformed_records_are_visible_with_warnings(self):
        self.write("empty.md", "")
        (self.tasks / "bad.md").write_bytes(b"\xff\xfe")
        payload = dashboard.collect(self.root)
        self.assertEqual(len(payload["records"]), 2)
        self.assertTrue(payload["warnings"])
        self.assertTrue(all(r["status"] == "Unknown" for r in payload["records"]))

    def test_symlink_record_is_skipped(self):
        target = self.root / "outside.md"
        target.write_text("# outside", encoding="utf-8")
        (self.tasks / "link.md").symlink_to(target)
        payload = dashboard.collect(self.root)
        self.assertEqual(payload["records"], [])
        self.assertTrue(any("symlink" in warning.lower() for warning in payload["warnings"]))

    def test_output_safety_rejects_task_dir_and_unsigned_existing_file(self):
        template = self.root / "DASHBOARD.html"
        template.write_text("<html></html>", encoding="utf-8")
        with self.assertRaises(ValueError):
            dashboard.write_dashboard(self.root, self.tasks / "index.html", template)
        output = self.root / "index.html"
        output.write_text("existing", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            dashboard.write_dashboard(self.root, output, template)

    def test_template_placeholders_and_quoted_status(self):
        text = CANONICAL.replace("status: active", 'status: "active"').replace("Owner request: Choose the required profile fields.", "| Field | Value |\n| --- | --- |\n| owner request | `<exact owner request bytes>` |")
        self.write("template.md", text)
        record = dashboard.collect(self.root)["records"][0]
        self.assertEqual(record["status"], "Active")
        self.assertEqual(record["request"], "")

    def test_schema2_rejects_yaml_multiline_title_marker(self):
        for value in ("|", "|2", ">-", "Plain title"):
            with self.subTest(value=value):
                self.write("multiline.md", "---\n"
                           f"record: olympus-task\nschema: 2\ntitle: {value}\n"
                           "  This title is multiline\nstatus: active\nkind: delivery\n"
                           "parent: none\nlinked-tasks: []\nowner-action: none\n"
                           "updated-at: 2026-09-13T10:00:00Z\nproduct-phase: none\n---\n")
                payload = dashboard.collect(self.root)
                self.assertEqual(payload["records"][0]["status"], "Unknown")
                self.assertTrue(any("header" in error for error in payload["validationErrors"]))

    def test_hidden_owner_tables_do_not_override_actual_record(self):
        fake = "## Owner decisions\n| Decision | Owner response | Effect |\n| --- | --- | --- |\n| fake | pending | spoof |\n"
        for indent in ("    ", "\t"):
            example = "\n" + "\n".join(indent + line for line in fake.splitlines()) + "\n\n"
            self.write("hidden.md", CANONICAL.replace("## Owner decisions", example + "## Owner decisions", 1))
            self.assertFalse(dashboard.collect(self.root)["records"][0]["needs"])
        for wrapper in ["~~~markdown\n{}~~~\n", "<!--\n{}-->\n", "<!-- FRONTEND-PACKET-BODY:BEGIN -->\n{}<!-- FRONTEND-PACKET-BODY:END -->\n"]:
            self.write("hidden.md", CANONICAL.replace("## Owner decisions", wrapper.format(fake)+"## Owner decisions",1))
            record = dashboard.collect(self.root)["records"][0]
            self.assertFalse(record["needs"])
            self.assertNotIn("fake", str(record["decisions"]))

    def test_unsupported_partial_schema_cannot_raise_attention(self):
        self.write("foreign.md", CANONICAL.replace("schema: 1\n", "").replace("record: olympus-task", "record: foreign").replace("| profile fields | resolved | Form may continue |", ""))
        record = dashboard.collect(self.root)["records"][0]
        self.assertEqual(record["status"], "Unknown")
        self.assertFalse(record["needs"])

    def test_symlink_ancestor_fifo_and_nested_sources_rejected(self):
        nested = self.tasks / "nested"
        nested.mkdir()
        (nested / "hidden.md").write_text(CANONICAL)
        os.mkfifo(self.tasks / "stuck.md")
        self.assertEqual(dashboard.collect(self.root)["records"], [])
        (self.root / ".olympus").rename(self.root / "real-state")
        (self.root / ".olympus").symlink_to(self.root / "real-state")
        result = dashboard.collect(self.root)
        self.assertEqual(result["records"], [])
        self.assertTrue(any("symlink" in w for w in result["warnings"]))

    def test_literal_frontmatter_cannot_override_status(self):
        self.write("literal.md", CANONICAL.replace("status: active", "status: active\nnotes: |\n  status: complete"))
        self.assertEqual(dashboard.collect(self.root)["records"][0]["status"], "Active")

    def test_conflicting_frontmatter_fails_closed(self):
        self.write("conflict.md", CANONICAL.replace("status: active", "status: blocked\nstatus: complete"))
        self.assertEqual(dashboard.collect(self.root)["records"][0]["status"], "Unknown")

    def test_signed_marker_in_body_is_not_overwrite_permission(self):
        template = self.root / "template.html"
        template.write_text("<html></html>")
        target = self.root / "index.html"
        target.write_text("<p>"+dashboard.SIGNATURE+"</p>")
        with self.assertRaises(FileExistsError):
            dashboard.write_dashboard(self.root, target, template)

    def test_legacy_goal_product_fields_and_explicit_links(self):
        self.write("2026-09-05-product.md", """# Goal `2026-09-05-product` — Product onboarding checkpoint

Status: Waiting for owner response; do not infer Complete from this prose.
Scope: Confirm the first useful product slice.

## Shared state checkpoints
| Product field | Record |
| --- | --- |
| phase and trigger | execution; builder is ready |
| audience | New users |
| linked work | delivery-trial; complete; workflow accepted; human acceptance pending |

## Owner decisions
| Decision | Owner response | Effect |
| --- | --- | --- |
| first slice | pending | Hold implementation |

""")
        self.write("delivery-trial.md", "# Goal `delivery-trial` — Delivery trial\n")
        record = dashboard.collect(self.root)["records"][0]
        self.assertEqual(record["title"], "Product onboarding checkpoint")
        self.assertEqual(record["status"], "Unknown")
        self.assertIn("Waiting for owner response", record["statusRaw"])
        self.assertEqual(record["request"], "Confirm the first useful product slice.")
        self.assertEqual(record["kind"], "product")
        self.assertEqual(record["productPhase"], "execution")
        self.assertEqual(record["product"]["audience"], "New users")
        self.assertEqual(record["product"]["phase and trigger"], "execution; builder is ready")
        self.assertTrue(record["attentionKnown"])
        self.assertTrue(record["needs"])
        self.assertEqual(record["links"], ["delivery-trial"])

    def test_id_only_title_is_humanized_and_product_word_does_not_make_product_kind(self):
        self.write("2026-09-05-delivery-child.md", """# Goal `2026-09-05-delivery-child`

Product work is mentioned in the scope.

## Shared state checkpoints
| Field | Value |
| --- | --- |
| phase and trigger | execution; this is a generic checkpoint |
""")
        record = dashboard.collect(self.root)["records"][0]
        self.assertEqual(record["title"], "delivery child")
        self.assertEqual(record["kind"], "delivery")
        self.assertEqual(record["productPhase"], "Unknown")
        self.assertEqual(record["product"], {})
        self.assertFalse(record["attentionKnown"])
        self.assertFalse(record["needs"])

    def test_empty_owner_decisions_table_is_known_but_not_needy(self):
        self.write("empty-decisions.md", """# Goal `empty-decisions` — Empty decision register

## Owner decisions
| Decision | Owner response | Effect |
| --- | --- | --- |
""")
        record = dashboard.collect(self.root)["records"][0]
        self.assertTrue(record["attentionKnown"])
        self.assertFalse(record["needs"])
        self.assertEqual(record["decisions"], [])

    def test_supporting_artifacts_are_excluded_and_counted(self):
        self.write("real.md", "# Goal `real` — Real task\n")
        self.write("support.spec.md", "# spec\n")
        self.write("support.plan.md", "# plan\n")
        self.write("support.txt", "# ignored\n")
        payload = dashboard.collect(self.root)
        self.assertEqual([record["id"] for record in payload["records"]], ["real"])
        self.assertEqual(payload["excludedCount"], 2)

    def test_top_level_owner_request_wins_over_later_tables(self):
        self.write("intro.md", """# Olympus task: `intro`

| Field | Value |
| --- | --- |
| owner request | Keep this request. |

## Shared state checkpoints
| Field | Value |
| --- | --- |
| owner request | Do not use this later prose. |
""")
        record = dashboard.collect(self.root)["records"][0]
        self.assertEqual(record["request"], "Keep this request.")

    def test_references_are_exact_bounded_and_ignore_hidden_regions(self):
        self.write("delivery-trial.md", "# Goal `delivery-trial` — Trial\n")
        self.write("delivery-trial-long.md", "# Goal `delivery-trial-long` — Long trial\n")
        self.write("refs.md", """# Goal `refs` — References

See delivery-trial-long and delivery-trial in this recorded note.

```text
delivery-trial-long
```

<!-- SPECIFICATION-BODY:BEGIN -->
delivery-trial
<!-- SPECIFICATION-BODY:END -->
""")
        records = {record["id"]: record for record in dashboard.collect(self.root)["records"]}
        self.assertEqual(records["refs"]["references"], ["delivery-trial-long", "delivery-trial"])

    def test_actual_task_product_placeholders_stay_delivery_unknown(self):
        self.write("placeholder-product.md", """# Goal `placeholder-product` — Placeholder checkpoint

## Shared state checkpoints
| Product field | Record |
| --- | --- |
| phase and trigger | <not recorded> |
| linked work | <none> |
""")
        record = dashboard.collect(self.root)["records"][0]
        self.assertEqual(record["kind"], "delivery")
        self.assertEqual(record["product"], {})
        self.assertEqual(record["productPhase"], "Unknown")


if __name__ == "__main__":
    unittest.main()
