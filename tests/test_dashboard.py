import json
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

    def test_pending_latest_decision_drives_attention(self):
        text = CANONICAL.replace("| profile fields | resolved | Form may continue |", "| profile fields | pending | Form paused again |")
        self.write("pending.md", text)
        record = dashboard.collect(self.root)["records"][0]
        self.assertTrue(record["needs"])
        self.assertEqual(record["decisions"][-1]["response"], "pending")

    def test_html_serialization_escapes_script_payload_and_preserves_source(self):
        source = self.write("xss.md", "# Olympus task: `xss`\n\n## Goal and scope\n<img src=x onerror=alert(1)> </script>\n")
        template = self.root / "DASHBOARD.html"
        template.write_text('<html><script id="olympus-data" type="application/json">{}</script></html>', encoding="utf-8")
        output = self.root / "out.html"
        before = source.read_bytes()
        dashboard.write_dashboard(self.root, output, template)
        rendered = output.read_text(encoding="utf-8")
        self.assertIn("<!-- OLYMPUS-DASHBOARD:GENERATED -->", rendered)
        embedded = re.search(r'type="application/json">(.*?)</script>', rendered, re.S).group(1)
        self.assertNotIn("<", embedded)
        self.assertEqual(json.loads(embedded)["records"][0]["raw"], before.decode())
        self.assertEqual(before, source.read_bytes())

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
        template.write_text('<script id="olympus-data" type="application/json">{}</script>', encoding="utf-8")
        with self.assertRaises(ValueError):
            dashboard.write_dashboard(self.root, self.tasks / "out.html", template)
        output = self.root / "out.html"
        output.write_text("existing", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            dashboard.write_dashboard(self.root, output, template)

    def test_template_placeholders_and_quoted_status(self):
        text = CANONICAL.replace("status: active", 'status: "active"').replace("Owner request: Choose the required profile fields.", "| Field | Value |\n| --- | --- |\n| owner request | `<exact owner request bytes>` |")
        self.write("template.md", text)
        record = dashboard.collect(self.root)["records"][0]
        self.assertEqual(record["status"], "Active")
        self.assertEqual(record["request"], "")

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
        template.write_text('<script id="olympus-data" type="application/json">{}</script>')
        target = self.root / "existing.html"
        target.write_text("<p>"+dashboard.SIGNATURE+"</p>")
        with self.assertRaises(FileExistsError):
            dashboard.write_dashboard(self.root, target, template)


if __name__ == "__main__":
    unittest.main()
