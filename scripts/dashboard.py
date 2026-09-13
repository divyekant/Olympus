#!/usr/bin/env python3
"""Build a read-only HTML dashboard from Olympus task records."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import stat
import sys
import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable


SIGNATURE = "<!-- OLYMPUS-DASHBOARD:GENERATED -->"
CANONICAL_STATUS = {
    "planned": "Planned",
    "active": "Active",
    "reviewing": "Reviewing",
    "complete": "Complete",
    "blocked": "Blocked",
    "cancelled": "Cancelled",
}
CANONICAL_STAGE = {"Prepare", "Build", "Verify"}
PRODUCT_PHASES = {"discovery", "decision", "execution", "awaiting evidence", "evaluation", "closed"}
PLACEHOLDERS = {"", "-", "—", "–", "none", "n/a", "na", "tbd", "placeholder"}


def _utc(timestamp: float | None = None) -> str:
    value = datetime.now(timezone.utc) if timestamp is None else datetime.fromtimestamp(timestamp, timezone.utc)
    return value.isoformat(timespec="seconds").replace("+00:00", "Z")


def _clean(value: str) -> str:
    value = re.sub(r"<!--.*?-->", "", value, flags=re.S)
    value = value.replace("\\|", "|")
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "`\"'":
        value = value[1:-1].strip()
    value = value.replace("`", "")
    return value


def _placeholder(value: str) -> bool:
    cleaned = _clean(value).lower()
    return cleaned in PLACEHOLDERS or "placeholder" in cleaned or bool(re.fullmatch(r"<[^>]+>", cleaned))


def _split_pipe(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in line:
        if char == "|" and not escaped:
            cells.append("".join(current).strip())
            current = []
            continue
        if char == "\\" and not escaped:
            escaped = True
            current.append(char)
            continue
        escaped = False
        current.append(char)
    cells.append("".join(current).strip())
    return cells


def _separator(row: list[str]) -> bool:
    return bool(row) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in row)


def _tables(lines: list[str]) -> Iterable[tuple[list[str], list[list[str]]]]:
    index = 0
    while index < len(lines):
        if "|" not in lines[index]:
            index += 1
            continue
        rows: list[list[str]] = []
        while index < len(lines) and "|" in lines[index] and lines[index].strip():
            row = _split_pipe(lines[index])
            if len(row) < 2:
                index += 1
                break
            rows.append(row)
            index += 1
        if len(rows) >= 2 and _separator(rows[1]):
            headers = [_clean(cell).lower() for cell in rows[0]]
            yield headers, rows[2:]
        if not rows:
            index += 1


def _heading(line: str) -> tuple[int, str] | None:
    match = re.match(r"^\s*(#{1,6})\s+(.+?)\s*$", line)
    return (len(match.group(1)), match.group(2).strip()) if match else None


def _section(lines: list[str], pattern: str) -> list[str]:
    wanted = re.compile(pattern, re.I)
    for index, line in enumerate(lines):
        heading = _heading(line)
        if not heading or not wanted.search(heading[1]):
            continue
        end = len(lines)
        for next_index in range(index + 1, len(lines)):
            if _heading(lines[next_index]):
                end = next_index
                break
        return lines[index + 1 : end]
    return []


def _sections(lines: list[str], pattern: str) -> list[list[str]]:
    wanted = re.compile(pattern, re.I)
    found: list[list[str]] = []
    for index, line in enumerate(lines):
        heading = _heading(line)
        if not heading or not wanted.search(heading[1]):
            continue
        end = len(lines)
        for next_index in range(index + 1, len(lines)):
            if _heading(lines[next_index]):
                end = next_index
                break
        found.append(lines[index + 1 : end])
    return found


def _metadata_text(body: str) -> str:
    lines, fence = [], None
    for line in body.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            continue
        if line.expandtabs(4).startswith("    "):
            lines.append("")
            continue
        if match:
            fence = match[1]
            continue
        lines.append(line)
    body = "\n".join(lines)
    for name in ("SPECIFICATION-BODY", "PLAN-BODY", "FRONTEND-PACKET-BODY"):
        body = re.sub(rf"<!--\s*{name}:BEGIN\s*-->.*?(?:<!--\s*{name}:END\s*-->|\Z)", "", body, flags=re.S | re.I)
    return re.sub(r"<!--.*?(?:-->|\Z)", "", body, flags=re.S)

def _frontmatter(text: str) -> tuple[dict[str, str], str, bool]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, False
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {"_invalid": "unclosed frontmatter"}, "", True
    values: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z][\w-]*)\s*:\s*(.*?)\s*$", line)
        if match:
            key = match[1].lower()
            if key in values:
                values["_invalid"] = "duplicate frontmatter key: " + key
            values[key] = match[2]
            if re.fullmatch(r"[|>][0-9+-]*", match[2]):
                values["_unsupported"] = "multiline header values are not supported"
        elif line.strip() and not line.lstrip().startswith("#"):
            values["_unsupported"] = "header fields must be top-level single-line values"
    return values, "\n".join(lines[end + 1:]), True

def _humanize_id(identifier: str) -> str:
    value = re.sub(r"^\d{4}-\d{2}-\d{2}-?", "", identifier)
    value = re.sub(r"[-_]+", " ", value)
    return re.sub(r"\s+", " ", value).strip() or identifier


def _title(lines: list[str], fallback: str) -> str:
    for line in lines:
        match = re.match(r"^# Olympus task:\s*(.*?)\s*$", line, re.I)
        if match and not _placeholder(match[1]):
            value = _clean(match[1])
            return _humanize_id(fallback) if value == fallback and re.match(r"^\d{4}-\d{2}-\d{2}-", fallback) else value
        match = re.match(r"^# Goal\s+`([^`]+)`(?:\s+[—-]\s*(.*?))?\s*$", line, re.I)
        if not match:
            match = re.match(r"^# Goal\s+([^\s—-]+)(?:\s+[—-]\s*(.*?))?\s*$", line, re.I)
        if match:
            description = _clean(match[2] or "")
            return description or _humanize_id(_clean(match[1]))
    return fallback


def _legacy_status(lines: list[str]) -> str:
    for line in lines[:40]:
        match = re.match(r"^\s*Status:\s*(\S.*)$", line)
        if match:
            return match[1].strip()
    return ""


def _schema2_stem(value: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", value)) and not _placeholder(value)


def _schema2_timestamp(value: str) -> bool:
    try:
        timestamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return timestamp.tzinfo is not None and timestamp.utcoffset() == timedelta(0)


def _schema2_record(record: dict, front: dict[str, str], lines: list[str], warnings: list[str], source: str) -> dict:
    errors: list[str] = []
    record["_schema2"] = True
    if front.get("_unsupported"):
        errors.append(front["_unsupported"])
    record["statusRaw"] = _clean(front.get("status", ""))
    filesystem_modified = record.get("modifiedAt")
    if _clean(front.get("record", "")) != "olympus-task":
        errors.append("record must be olympus-task")
    if not _schema2_stem(record["id"]):
        errors.append("filename stem is not a valid task id")
    title = _clean(front.get("title", ""))
    if (
        "title" not in front
        or not title.strip()
        or "\n" in title
        or "\r" in title
        or re.fullmatch(r"[|>][+-]?", title.strip())
        or _placeholder(title)
    ):
        errors.append("title must be a nonplaceholder single-line value")
    else:
        record["title"] = title.strip()
    status = _clean(front.get("status", ""))
    if status not in CANONICAL_STATUS:
        errors.append("status is not canonical")
    else:
        record["status"] = CANONICAL_STATUS[status]
    kind_value = _clean(front.get("kind", ""))
    if kind_value not in {"delivery", "product"}:
        errors.append("kind must be delivery or product")
    else:
        record["kind"] = kind_value
    parent = _clean(front.get("parent", ""))
    if parent != "none" and not _schema2_stem(parent):
        errors.append("parent must be none or a task stem")
    record["parent"] = parent
    linked_raw = front.get("linked-tasks", "")
    try:
        linked = json.loads(linked_raw)
    except (TypeError, json.JSONDecodeError):
        linked = []
        errors.append("linked-tasks must be a JSON array")
    if not isinstance(linked, list) or any(not isinstance(value, str) or not _schema2_stem(value) for value in linked):
        errors.append("linked-tasks must contain valid task stems")
        linked = [value for value in linked if isinstance(value, str)] if isinstance(linked, list) else []
    if len(linked) != len(set(linked)):
        errors.append("linked-tasks must not contain duplicates")
    record["links"] = list(linked)
    owner_action = _clean(front.get("owner-action", ""))
    if owner_action not in {"none", "pending"}:
        errors.append("owner-action must be none or pending")
    product_phase = _clean(front.get("product-phase", ""))
    if kind_value == "delivery" and product_phase != "none":
        errors.append("delivery product-phase must be none")
    if kind_value == "product" and product_phase not in PRODUCT_PHASES:
        errors.append("product product-phase must be canonical")
    record["productPhase"] = product_phase if product_phase else "Unknown"
    stage = _clean(front.get("stage", "")) if "stage" in front else None
    if stage is not None and stage not in CANONICAL_STAGE:
        errors.append("stage is not canonical")
    record["stage"] = stage or "Unknown"
    updated_at = _clean(front.get("updated-at", ""))
    if not _schema2_timestamp(updated_at):
        errors.append("updated-at must be a UTC ISO timestamp")
    else:
        record["updatedAt"] = updated_at
    record["request"] = _request(lines)
    record["agents"] = _agents(lines)
    record["product"] = _product(lines) if kind_value == "product" else {}
    record["decisions"], table_needs, table_known = _decisions(lines)
    record["attentionKnown"] = table_known or owner_action == "none"
    if owner_action == "pending" and not (table_known and table_needs):
        errors.append("pending owner-action requires a supported pending decision")
    if owner_action == "none" and table_needs:
        errors.append("owner-action none contradicts a pending decision")
    if record.get("status") in {"Complete", "Cancelled"} and owner_action != "none":
        errors.append("terminal status requires owner-action none")
    record["needs"] = (
        record["status"] not in {"Complete", "Cancelled"}
        and owner_action == "pending"
        and record["attentionKnown"]
        and table_needs
    )
    if errors:
        record["_schema2_errors"] = errors
        record["status"] = "Unknown"
        record["stage"] = "Unknown"
        record["kind"] = "Unknown"
        record["productPhase"] = "Unknown"
        record["product"] = {}
        record["links"] = []
        record["needs"] = False
        record["attentionKnown"] = False
        record.pop("updatedAt", None)
        if filesystem_modified is not None:
            record["modifiedAt"] = filesystem_modified
        for error in errors:
            warnings.append(f"{source}: schema2 {error}")
    return record


def _mark_schema2_invalid(record: dict, error: str, warnings: list[str]) -> None:
    errors = record.setdefault("_schema2_errors", [])
    if error not in errors:
        errors.append(error)
        warnings.append(f"{record['source']}: schema2 {error}")
    record["status"] = "Unknown"
    record["stage"] = "Unknown"
    record["kind"] = "Unknown"
    record["productPhase"] = "Unknown"
    record["product"] = {}
    record["links"] = []
    record["needs"] = False
    record["attentionKnown"] = False
    record.pop("updatedAt", None)


def _validate_schema2(records: list[dict], warnings: list[str]) -> list[str]:
    schema2 = [record for record in records if record.get("_schema2")]
    by_id: dict[str, list[dict]] = {}
    all_by_id: dict[str, list[dict]] = {}
    for record in records:
        all_by_id.setdefault(record["id"], []).append(record)
    all_ids = set(all_by_id)
    for record in schema2:
        by_id.setdefault(record["id"], []).append(record)
    for identifier, matches in all_by_id.items():
        if len(matches) > 1:
            for record in matches:
                if not record.get("_schema2"):
                    continue
                _mark_schema2_invalid(record, f"duplicate task id {identifier}", warnings)
    for record in schema2:
        identifier = record["id"]
        if record.get("_schema2_errors"):
            continue
        parent = record.get("parent", "none")
        if parent != "none":
            if parent == identifier:
                _mark_schema2_invalid(record, "parent cannot reference itself", warnings)
            elif parent not in all_ids:
                _mark_schema2_invalid(record, f"parent task is missing: {parent}", warnings)
            elif len(all_by_id[parent]) != 1:
                _mark_schema2_invalid(record, f"parent task id is ambiguous: {parent}", warnings)
        for linked in record.get("links", []):
            if linked == identifier:
                _mark_schema2_invalid(record, "linked-tasks cannot reference itself", warnings)
            elif linked not in all_ids:
                _mark_schema2_invalid(record, f"linked task is missing: {linked}", warnings)
            elif len(all_by_id[linked]) != 1:
                _mark_schema2_invalid(record, f"linked task id is ambiguous: {linked}", warnings)
    parent_map = {
        record["id"]: record.get("parent", "none")
        for record in schema2
        if not record.get("_schema2_errors")
        and record.get("parent", "none") != "none"
        and len(by_id.get(record["id"], [])) == 1
        and record.get("parent") in by_id
        and not by_id[record["parent"]][0].get("_schema2_errors")
    }
    visited: set[str] = set()
    for start in parent_map:
        if start in visited:
            continue
        trail: list[str] = []
        positions: dict[str, int] = {}
        current = start
        while current in parent_map and current not in visited:
            if current in positions:
                for cycle_id in trail[positions[current] :]:
                    _mark_schema2_invalid(by_id[cycle_id][0], "parent relationships contain a cycle", warnings)
                break
            positions[current] = len(trail)
            trail.append(current)
            current = parent_map[current]
        visited.update(trail)
    # Represent each valid schema 2 parent as an explicit member link on that parent.
    by_single_id = {identifier: matches[0] for identifier, matches in all_by_id.items() if len(matches) == 1}
    for record in schema2:
        if record.get("_schema2_errors"):
            continue
        parent = record.get("parent", "none")
        target = by_single_id.get(parent) if parent != "none" else None
        if target is None or target.get("_schema2_errors"):
            continue
        if record["id"] not in target["links"]:
            target["links"].append(record["id"])
    return [
        f"{record['id']}: {error}"
        for record in schema2
        for error in record.get("_schema2_errors", [])
    ]

def _request(lines: list[str]) -> str:
    section = _section(lines, r"\bgoal\s*(?:and|&)\s*scope\b")
    intro: list[str] = []
    for line in lines:
        heading = _heading(line)
        if heading and heading[0] >= 2:
            break
        intro.append(line)
    candidates = [section] if section else [intro]
    for candidate in candidates:
      for headers, rows in _tables(candidate):
        names = {header: index for index, header in enumerate(headers)}
        owner_index = names.get("owner request")
        if owner_index is not None:
            for row in rows:
              if owner_index < len(row) and not _placeholder(row[owner_index]):
                  return _clean(row[owner_index])
        field_index = names.get("field")
        if field_index is not None:
            for row in rows:
              if field_index < len(row) and _clean(row[field_index]).lower() == "owner request":
                  values = [cell for cell in row[field_index + 1 :] if not _placeholder(cell)]
                  return _clean(" ".join(values))
    plain: list[str] = []
    for line in section or intro:
        value = re.sub(r"^\s*[-*+]\s+", "", line).strip()
        if not value or "|" in value:
            continue
        scope = re.match(r"^(?:scope|owner request)\s*:\s*(.+)$", value, re.I)
        if scope:
            return _clean(scope[1])
        if not section and _heading(line) and not re.match(r"^# Goal\s+", line, re.I):
            break
        value = re.sub(r"^owner request\s*:\s*", "", value, flags=re.I)
        plain.append(value)
    return _clean(" ".join(plain)) if section else ""


def _decisions(lines: list[str]) -> tuple[list[dict[str, str]], bool, bool]:
    decisions: list[dict[str, str]] = []
    latest: dict[str, str] = {}
    known = False
    for section in _sections(lines, r"^owner\s+decisions?$"):
      for headers, rows in _tables(section):
        indices = {header: index for index, header in enumerate(headers)}
        response_index = indices.get("response", indices.get("owner response"))
        if "decision" not in indices or response_index is None or "effect" not in indices:
            continue
        known = True
        for row in rows:
          decision = _clean(row[indices["decision"]]) if indices["decision"] < len(row) else ""
          response = _clean(row[response_index]) if response_index < len(row) else ""
          effect = _clean(row[indices["effect"]]) if indices["effect"] < len(row) else ""
          if _placeholder(decision):
              continue
          item = {"decision": decision, "response": response, "effect": effect}
          decisions.append(item)
          latest[decision.casefold()] = response
    needs = any(response.casefold() in {"pending", "awaiting owner reply"} for response in latest.values())
    return decisions, needs, known


def _agents(lines: list[str]) -> list[list[str]]:
    section = _section(lines, r"role\s+population|agent\s+assignments?")
    result: list[list[str]] = []
    for headers, rows in _tables(section):
        indices = {header: index for index, header in enumerate(headers)}
        if "role" not in indices or "actual" not in indices:
            continue
        for row in rows:
            role = _clean(row[indices["role"]]) if indices["role"] < len(row) else ""
            actual = _clean(row[indices["actual"]]) if indices["actual"] < len(row) else ""
            if _placeholder(role):
                continue
            status = {
                "invoked": "Invoked (recorded)",
                "yes": "Invoked (recorded)",
                "pending": "Pending (recorded)",
                "not invoked": "Not invoked (recorded)",
                "no": "Not invoked (recorded)",
            }.get(actual.casefold(), "Unknown (not recorded)" if _placeholder(actual) else actual)
            result.append([role, status])
    return result


def _product(lines: list[str]) -> dict[str, str]:
    product: dict[str, str] = {}
    for section in _sections(lines, r"^(?:product(?:\s+field)?(?:\s+checkpoints?)?|shared\s+state\s+checkpoints)$"):
        for headers, rows in _tables(section):
            if "product field" not in headers or "record" not in headers:
                continue
            key_index = headers.index("product field")
            value_index = headers.index("record")
            for row in rows:
                if key_index >= len(row) or value_index >= len(row):
                    continue
                key = _clean(row[key_index])
                value = _clean(row[value_index])
                if not _placeholder(key) and not _placeholder(value):
                    product[key] = value
            if product:
                return product
    return product


def _product_phase(product: dict[str, str]) -> str:
    for key, raw in product.items():
        normalized_key = key.casefold()
        if normalized_key != "phase and trigger":
            continue
        value = raw.split(";", 1)[0].strip().casefold()
        if value in PRODUCT_PHASES:
            return value
    return "Unknown"


LINK_COLUMNS = (
    "member goal identifier",
    "goal identifier",
    "linked task",
    "related task",
    "task id",
    "task",
    "member",
)


def _explicit_task_id(value: str) -> str:
    value = _clean(value)
    if _placeholder(value):
        return ""
    return value if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", value) else ""


def _links(lines: list[str], warnings: list[str], source: str) -> list[str]:
    links: list[str] = []
    found_heading = False
    for section in _sections(lines, r"^(?:sizing\s+check|linked\s+work|related\s+work|members?|shared\s+state\s+checkpoints)"):
        found_heading = True
        for headers, rows in _tables(section):
            index = next((headers.index(name) for name in LINK_COLUMNS if name in headers), None)
            if index is None and "product field" in headers and "record" in headers:
                product_index, record_index = headers.index("product field"), headers.index("record")
                for row in rows:
                    if product_index < len(row) and _clean(row[product_index]).casefold() == "linked work" and record_index < len(row):
                        link = _explicit_task_id(row[record_index].split(";", 1)[0])
                        if link and link not in links:
                            links.append(link)
                continue
            if index is None:
                continue
            supersedes = headers.index("supersedes") if "supersedes" in headers else None
            for row in rows:
                if supersedes is not None and supersedes < len(row) and not _placeholder(row[supersedes]):
                    warnings.append(f"{source}: superseded member rows require source inspection; links omitted")
                    return []
                member = _explicit_task_id(row[index]) if index < len(row) else ""
                if member and member not in links:
                    links.append(member)
            break
    if found_heading and not links:
        # A heading alone is not enough evidence to invent a relationship.
        return []
    return links


def _references(metadata: str, known_ids: set[str], own_id: str, links: list[str]) -> list[str]:
    candidates = sorted((value for value in known_ids if value != own_id), key=len, reverse=True)
    if not candidates:
        return []
    pattern = re.compile(r"(?<![A-Za-z0-9_.-])(?:" + "|".join(re.escape(value) for value in candidates) + r")(?![A-Za-z0-9_.-])")
    found: list[str] = []
    for match in pattern.finditer(metadata):
        value = match.group(0)
        if value not in links and value not in found:
            found.append(value)
    return found

def _base_record(root: Path, path: Path, raw: str, modified: str) -> dict:
    relative = path.relative_to(root).as_posix()
    task_relative = path.relative_to(root / ".olympus" / "tasks").with_suffix("").as_posix()
    return {
        "id": task_relative,
        "title": path.stem,
        "status": "Unknown",
        "statusRaw": "",
        "parent": "none",
        "stage": "Unknown",
        "request": "",
        "needs": False,
        "attentionKnown": False,
        "decisions": [],
        "agents": [],
        "kind": "delivery",
        "productPhase": "Unknown",
        "product": {},
        "source": relative,
        "modifiedAt": modified,
        "raw": raw,
        "links": [],
        "references": [],
    }


def _record(root: Path, path: Path, warnings: list[str], known_ids: set[str] | None = None) -> dict:
    record = _base_record(root, path, "", None)
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW)
        with os.fdopen(fd, "rb") as handle:
            before = os.fstat(handle.fileno())
            if not stat.S_ISREG(before.st_mode):
                raise OSError("non-regular record rejected")
            record["modifiedAt"] = _utc(before.st_mtime)
            data = handle.read()
            after_fd = os.fstat(handle.fileno())
        record["raw"] = data.decode("utf-8", errors="replace")
        after = path.lstat()
    except OSError as exc:
        warnings.append(f"{path}: unreadable or changed record ({exc})")
        record["_validation_error"] = f"unreadable or changed record ({exc})"
        return record
    identity = lambda st: (st.st_dev, st.st_ino, st.st_mtime_ns, st.st_size)
    if identity(before) != identity(after_fd) or identity(before) != identity(after):
        warnings.append(f"{path}: changed during read; metadata unavailable")
        record["_validation_error"] = "changed during read; metadata unavailable"
        return record
    try:
        raw = data.decode("utf-8")
    except UnicodeDecodeError:
        warnings.append(f"{path}: invalid UTF-8; metadata unavailable")
        record["_validation_error"] = "invalid UTF-8; metadata unavailable"
        return record
    front, body, has_frontmatter = _frontmatter(raw)
    lines = _metadata_text(body).splitlines()
    record["title"] = _title(lines, record["id"])
    record["statusRaw"] = front.get("status", "") or _legacy_status(lines)
    # Keep malformed schema 2 files in the schema 2 validation set.
    raw_lines = raw.splitlines()
    header: list[str] = []
    if raw_lines and raw_lines[0].strip() == "---":
        for line in raw_lines[1:]:
            if line.strip() == "---":
                break
            header.append(line)
    schema2_hint = _clean(front.get("schema", "")) == "2" or any(
        re.match(r"^\s*schema\s*:\s*['\"`]?2['\"`]?\s*$", line) for line in header
    )
    if schema2_hint and "_invalid" in front:
        record["_schema2"] = True
        _mark_schema2_invalid(record, front["_invalid"], warnings)
        return record
    if "_invalid" in front:
        warnings.append(f"{path}: {front['_invalid']}; metadata unavailable")
        return record
    front_record = _clean(front.get("record", ""))
    front_schema = _clean(front.get("schema", ""))
    if schema2_hint:
        result = _schema2_record(record, front, lines, warnings, str(path))
        if known_ids is not None:
            result["references"] = _references("\n".join(lines), known_ids, record["id"], result["links"])
        return result
    if front_record and front_record != "olympus-task":
        warnings.append(f"{path}: unsupported record/schema; metadata unavailable")
        return record
    if front_schema and front_schema != "1":
        warnings.append(f"{path}: unsupported record/schema; metadata unavailable")
        return record
    if not has_frontmatter or "record" not in front or "schema" not in front:
        warnings.append(f"{path}: legacy record missing record/schema")
        if not any(re.match(r"^# (?:Olympus task:|Goal\s+)", line, re.I) for line in lines):
            return record
    raw_status = _clean(front.get("status", "")) if "status" in front else ""
    record["status"] = CANONICAL_STATUS.get(raw_status, "Unknown")
    if record["status"] == "Unknown" and (raw_status or record["statusRaw"]):
        warnings.append(f"{path}: status is missing or noncanonical; shown as Unknown")
    raw_stage = _clean(front.get("stage", ""))
    if raw_stage in CANONICAL_STAGE:
        record["stage"] = raw_stage
    record["request"] = _request(lines)
    record["decisions"], record["needs"], record["attentionKnown"] = _decisions(lines)
    record["agents"] = _agents(lines)
    record["links"] = _links(lines, warnings, str(path))
    record["product"] = _product(lines)
    record["kind"] = "product" if record["product"] else "delivery"
    record["productPhase"] = _product_phase(record["product"])
    if known_ids is not None:
        record["references"] = _references("\n".join(lines), known_ids, record["id"], record["links"])
    if record["status"] in {"Complete", "Cancelled"}:
        record["needs"] = False
    return record

def _task_files(root: Path, warnings: list[str], excluded_count: list[int] | None = None) -> list[Path]:
    task_dir = root / ".olympus" / "tasks"
    try:
        for directory in (root / ".olympus", task_dir):
            info = directory.lstat()
            if stat.S_ISLNK(info.st_mode):
                warnings.append(f"{directory}: symlink directory rejected")
                return []
            if not stat.S_ISDIR(info.st_mode):
                warnings.append(f"{directory}: not a directory")
                return []
        candidates = sorted(task_dir.iterdir())
    except OSError as exc:
        warnings.append(f"{task_dir}: task directory unavailable ({exc})")
        return []
    paths = []
    for path in candidates:
        if path.suffix.lower() != ".md":
            continue
        try:
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode) or not stat.S_ISREG(mode):
                warnings.append(f"{path}: symlink or non-regular record rejected")
                continue
        except OSError as exc:
            warnings.append(f"{path}: unavailable record ({exc})")
            continue
        if path.name.casefold().endswith((".spec.md", ".plan.md")):
            if excluded_count is not None:
                excluded_count[0] += 1
            continue
        paths.append(path)
    return paths

def collect(root: Path) -> dict:
    root = Path(root).resolve()
    warnings: list[str] = []
    excluded_count = [0]
    discovery_warning_count = len(warnings)
    paths = _task_files(root, warnings, excluded_count)
    discovery_warnings = warnings[discovery_warning_count:]
    known_ids = {path.relative_to(root / ".olympus" / "tasks").with_suffix("").as_posix() for path in paths}
    records = [_record(root, path, warnings, known_ids) for path in paths]
    validation_errors = [f"discovery: {warning}" for warning in discovery_warnings]
    validation_errors.extend(_validate_schema2(records, warnings))
    for record in records:
        if record.get("_validation_error"):
            validation_errors.append(f"{record['id']}: {record['_validation_error']}")
            warnings.append(f"{record['source']}: validation failed ({record['_validation_error']})")
    legacy_count = sum(1 for record in records if not record.get("_schema2") and not record.get("_validation_error"))
    for record in records:
        record.pop("_schema2", None)
        record.pop("_schema2_errors", None)
        record.pop("_validation_error", None)
    return {
        "project": root.name,
        "root": str(root),
        "generatedAt": _utc(),
        "records": records,
        "warnings": warnings,
        "validationErrors": validation_errors,
        "legacyCount": legacy_count,
        "excludedCount": excluded_count[0],
    }


def _json_payload(payload: dict) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    for char in "<>&\u2028\u2029":
        encoded = encoded.replace(char, f"\\u{ord(char):04x}")
    return encoded


def _inside(path: Path, directory: Path) -> bool:
    try:
        path.relative_to(directory)
        return True
    except ValueError:
        return False


DATA_SIGNATURE = "// OLYMPUS-DASHBOARD:GENERATED\n"


def _has_symlink_component(path: Path, stop: Path | None = None) -> bool:
    current = path
    while True:
        try:
            if current.is_symlink():
                return True
        except OSError:
            pass
        if stop is not None and current == stop:
            return False
        if current.parent == current:
            return False
        current = current.parent


def _protected_destination(root: Path, path: Path, template: Path) -> None:
    if path.is_symlink():
        raise ValueError(f"symlink destination rejected: {path}")
    if path == template or _inside(path, root / ".olympus" / "tasks"):
        raise ValueError("dashboard output is inside a protected Olympus path")
    try:
        olympus_relative = path.relative_to(root / ".olympus")
    except ValueError:
        olympus_relative = None
    if olympus_relative and olympus_relative.parts and olympus_relative.parts[0].casefold().startswith("project"):
        raise ValueError("dashboard output would overwrite a protected Olympus project file")


def _read_existing(path: Path, signature: bytes, label: str) -> bytes | None:
    if not path.exists() and not path.is_symlink():
        return None
    if path.is_symlink():
        raise ValueError(f"symlink {label} rejected: {path}")
    if not path.is_file():
        raise FileExistsError(f"refusing to overwrite non-file {label}: {path}")
    existing = path.read_bytes()
    if not existing.startswith(signature):
        raise FileExistsError(f"refusing to overwrite unsigned {label}: {path}")
    return existing


def _prepare_bundle(root: Path, output: Path, template: Path | None) -> tuple[Path, Path, bytes, bytes | None, bytes | None]:
    root_input = Path(root).absolute()
    root = root_input.resolve()
    output = Path(output).absolute()
    if output.suffix.lower() != ".html" or output.name.casefold() != "index.html":
        raise ValueError("dashboard output must use the index.html filename")
    if _has_symlink_component(output, root_input):
        raise ValueError(f"symlink destination rejected: {output}")
    output = output.resolve()
    template_path = (Path(template) if template else Path(__file__).resolve().parent.parent / "templates" / "DASHBOARD.html").absolute()
    if _inside(template_path, root_input) and _has_symlink_component(template_path, root_input):
        raise ValueError(f"symlink template rejected: {template_path}")
    if template_path.is_symlink():
        raise ValueError(f"symlink template rejected: {template_path}")
    template_path = template_path.resolve()
    if not template_path.is_file():
        raise FileNotFoundError(template_path)
    data_path = output.parent / "tasks-data.js"
    _protected_destination(root, output, template_path)
    _protected_destination(root, data_path, template_path)
    if data_path == template_path:
        raise ValueError("template cannot be the tasks-data.js destination")
    html_bytes = template_path.read_bytes()
    signature = SIGNATURE.encode("utf-8")
    if html_bytes.startswith(signature):
        if not html_bytes.startswith(signature + b"\n"):
            html_bytes = signature + b"\n" + html_bytes[len(signature) :]
    else:
        html_bytes = signature + b"\n" + html_bytes
    existing_html = _read_existing(output, signature + b"\n", "HTML output")
    existing_data = _read_existing(data_path, DATA_SIGNATURE.encode("utf-8"), "data output")
    return output, data_path, html_bytes, existing_html, existing_data


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: str | None = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp", delete=False) as handle:
            temporary = handle.name
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)


def _bundle_data(payload: dict) -> bytes:
    return (DATA_SIGNATURE + "window.olympusSnapshot = " + _json_payload(payload) + ";\n").encode("utf-8")


def write_dashboard(root: Path, output: Path, template: Path | None = None) -> dict:
    output_path, data_path, html_bytes, existing_html, existing_data = _prepare_bundle(root, output, template)
    payload = collect(root)
    data_bytes = _bundle_data(payload)
    if existing_html != html_bytes:
        _atomic_write(output_path, html_bytes)
    if existing_data != data_bytes:
        _atomic_write(data_path, data_bytes)
    return payload


def write_data(root: Path, output: Path, template: Path | None = None) -> dict:
    _output_path, data_path, _html_bytes, existing_html, existing_data = _prepare_bundle(root, output, template)
    if existing_html is None:
        raise FileNotFoundError(f"dashboard HTML output does not exist: {output}")
    payload = collect(root)
    data_bytes = _bundle_data(payload)
    if existing_data != data_bytes:
        _atomic_write(data_path, data_bytes)
    return payload


def _snapshot(root: Path) -> tuple:
    warnings: list[str] = []
    signatures = []
    for path in _task_files(root, warnings):
        try:
            info = path.lstat()
            signatures.append((str(path), info.st_ino, info.st_mtime_ns, info.st_size))
        except OSError as exc:
            warnings.append(f"{path}: {exc}")
    return tuple(signatures), tuple(warnings)

def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a read-only Olympus task dashboard.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Olympus project root (default: current directory)")
    parser.add_argument("--output", type=Path, help="HTML output path (must be named index.html)")
    parser.add_argument("--template", type=Path, help="Dashboard HTML template")
    parser.add_argument("--watch", type=float, help="Regenerate on task changes, in seconds (minimum 1)")
    parser.add_argument("--validate-only", action="store_true", help="Validate schema 2 records without writing HTML")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    if args.validate_only and args.output is not None:
        parser.error("--validate-only cannot be combined with --output")
    if args.validate_only and args.watch is not None:
        parser.error("--validate-only cannot be combined with --watch")
    if not args.validate_only and args.output is None:
        parser.error("--output is required unless --validate-only is used")
    if args.watch is not None and (not math.isfinite(args.watch) or args.watch < 1):
        parser.error("--watch must be at least 1 second")
    try:
        if args.validate_only:
            payload = collect(args.root)
            print(f"Skipped legacy records: {payload['legacyCount']}")
            for error in payload["validationErrors"]:
                print(error, file=sys.stderr)
            return 1 if payload["validationErrors"] else 0
        previous = _snapshot(Path(args.root).resolve())
        payload = write_dashboard(args.root, args.output, args.template)
        print(f"Wrote {args.output} ({len(payload['records'])} records)")
        if args.watch is not None:
            while True:
                time.sleep(args.watch)
                current = _snapshot(Path(args.root).resolve())
                if current != previous:
                    try:
                        payload = write_data(args.root, args.output, args.template)
                    except (OSError, ValueError) as exc:
                        print(f"Watch update failed: {exc}", file=sys.stderr)
                    else:
                        print(f"Updated {args.output.parent / 'tasks-data.js'} ({len(payload['records'])} records)")
                        previous = current
    except KeyboardInterrupt:
        return 0
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
