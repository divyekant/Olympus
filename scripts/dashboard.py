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
from datetime import datetime, timezone
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
    return values, "\n".join(lines[end + 1:]), True

def _title(lines: list[str], fallback: str) -> str:
    for line in lines:
        match = re.match(r"^# Olympus task:\s*(.*?)\s*$", line, re.I)
        if match and not _placeholder(match[1]):
            return _clean(match[1])
    return fallback

def _request(lines: list[str]) -> str:
    section = _section(lines, r"\bgoal\s*(?:and|&)\s*scope\b")
    if not section:
        return ""
    for headers, rows in _tables(section):
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
    for line in section:
        value = re.sub(r"^\s*[-*+]\s+", "", line).strip()
        if not value or "|" in value:
            continue
        value = re.sub(r"^owner request\s*:\s*", "", value, flags=re.I)
        plain.append(value)
    return _clean(" ".join(plain))


def _decisions(lines: list[str]) -> tuple[list[dict[str, str]], bool]:
    decisions: list[dict[str, str]] = []
    latest: dict[str, str] = {}
    for headers, rows in _tables(_section(lines, r"^owner\s+decisions?$")):
        indices = {header: index for index, header in enumerate(headers)}
        response_index = indices.get("response", indices.get("owner response"))
        if "decision" not in indices or response_index is None or "effect" not in indices:
            continue
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
    return decisions, needs


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


def _links(lines: list[str], warnings: list[str], source: str) -> list[str]:
    links = []
    for headers, rows in _tables(_section(lines, r"^sizing\s+check(?:\s*\(|$)")):
        if "member goal identifier" not in headers:
            continue
        index = headers.index("member goal identifier")
        supersedes = headers.index("supersedes") if "supersedes" in headers else None
        for row in rows:
            if supersedes is not None and supersedes < len(row) and not _placeholder(row[supersedes]):
                warnings.append(f"{source}: corrected member rows require source inspection; links omitted")
                return []
            if index < len(row) and not _placeholder(row[index]):
                link = _clean(row[index])
                if link not in links:
                    links.append(link)
    return links

def _base_record(root: Path, path: Path, raw: str, modified: str) -> dict:
    relative = path.relative_to(root).as_posix()
    task_relative = path.relative_to(root / ".olympus" / "tasks").with_suffix("").as_posix()
    return {
        "id": task_relative,
        "title": path.stem,
        "status": "Unknown",
        "statusRaw": "",
        "stage": "Unknown",
        "request": "",
        "needs": False,
        "decisions": [],
        "agents": [],
        "source": relative,
        "modifiedAt": modified,
        "raw": raw,
        "links": [],
    }


def _record(root: Path, path: Path, warnings: list[str]) -> dict:
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
        return record
    identity = lambda st: (st.st_dev, st.st_ino, st.st_mtime_ns, st.st_size)
    if identity(before) != identity(after_fd) or identity(before) != identity(after):
        warnings.append(f"{path}: changed during read; metadata unavailable")
        return record
    try:
        raw = data.decode("utf-8")
    except UnicodeDecodeError:
        warnings.append(f"{path}: invalid UTF-8; metadata unavailable")
        return record
    front, body, has_frontmatter = _frontmatter(raw)
    lines = _metadata_text(body).splitlines()
    record["title"] = _title(lines, path.stem)
    record["statusRaw"] = front.get("status", "")
    if "_invalid" in front:
        warnings.append(f"{path}: {front['_invalid']}; metadata unavailable")
        return record
    if ("record" in front and _clean(front["record"]) != "olympus-task") or ("schema" in front and _clean(front["schema"]) != "1"):
        warnings.append(f"{path}: unsupported record/schema; metadata unavailable")
        return record
    if not has_frontmatter or "record" not in front or "schema" not in front:
        warnings.append(f"{path}: legacy record missing record/schema")
        if not any(re.match(r"^# Olympus task:", line, re.I) for line in lines):
            return record
    raw_status = _clean(front.get("status", ""))
    record["status"] = CANONICAL_STATUS.get(raw_status, "Unknown")
    if record["status"] == "Unknown":
        warnings.append(f"{path}: status is missing or noncanonical; shown as Unknown")
    raw_stage = _clean(front.get("stage", ""))
    if raw_stage in CANONICAL_STAGE:
        record["stage"] = raw_stage
    record["request"] = _request(lines)
    record["decisions"], record["needs"] = _decisions(lines)
    record["agents"] = _agents(lines)
    record["links"] = _links(lines, warnings, str(path))
    if record["status"] in {"Complete", "Cancelled"}:
        record["needs"] = False
    return record

def _task_files(root: Path, warnings: list[str]) -> list[Path]:
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
        paths.append(path)
    return paths

def collect(root: Path) -> dict:
    root = Path(root).resolve()
    warnings: list[str] = []
    records = [_record(root, path, warnings) for path in _task_files(root, warnings)]
    return {"project": root.name, "root": str(root), "generatedAt": _utc(), "records": records, "warnings": warnings}


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


def write_dashboard(root: Path, output: Path, template: Path | None = None) -> dict:
    root = Path(root).resolve()
    output = Path(output).absolute()
    if output.is_symlink():
        raise ValueError("symlink output rejected")
    output = output.resolve()
    template = (Path(template) if template else Path(__file__).resolve().parent.parent / "templates" / "DASHBOARD.html").resolve()
    if output.suffix.lower() != ".html":
        raise ValueError("dashboard output must use the .html extension")
    if output == template or _inside(output, root / ".olympus" / "tasks"):
        raise ValueError("dashboard output is inside a protected Olympus path")
    try:
        olympus_relative = output.relative_to(root / ".olympus")
    except ValueError:
        olympus_relative = None
    if olympus_relative and olympus_relative.parts and olympus_relative.parts[0].casefold().startswith("project"):
        raise ValueError("dashboard output would overwrite a protected Olympus project file")
    if not template.is_file():
        raise FileNotFoundError(template)
    if output.exists():
        existing = output.read_text(encoding="utf-8")
        if not existing.startswith(SIGNATURE + "\n"):
            raise FileExistsError(f"refusing to overwrite unsigned output: {output}")
    template_text = template.read_text(encoding="utf-8")
    pattern = re.compile(r'(<script\s+id=["\']olympus-data["\']\s+type=["\']application/json["\']\s*>)(.*?)(</script>)', re.S)
    matches = list(pattern.finditer(template_text))
    if len(matches) != 1:
        raise ValueError("template must contain exactly one olympus-data JSON script")
    payload = collect(root)
    match = matches[0]
    rendered = template_text[: match.start()] + match.group(1) + _json_payload(payload) + match.group(3) + template_text[match.end() :]
    if not rendered.startswith(SIGNATURE):
        rendered = SIGNATURE + "\n" + rendered
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary: str | None = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=output.parent, prefix=f".{output.name}.", suffix=".tmp", delete=False) as handle:
            temporary = handle.name
            handle.write(rendered)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, output)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)
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
    parser.add_argument("--output", type=Path, required=True, help="HTML output path")
    parser.add_argument("--template", type=Path, help="Dashboard HTML template")
    parser.add_argument("--watch", type=float, help="Regenerate on task changes, in seconds (minimum 1)")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    if args.watch is not None and (not math.isfinite(args.watch) or args.watch < 1):
        parser.error("--watch must be at least 1 second")
    try:
        previous = _snapshot(Path(args.root).resolve())
        payload = write_dashboard(args.root, args.output, args.template)
        print(f"Wrote {args.output} ({len(payload['records'])} records)")
        if args.watch is not None:
            while True:
                time.sleep(args.watch)
                current = _snapshot(Path(args.root).resolve())
                if current != previous:
                    payload = write_dashboard(args.root, args.output, args.template)
                    print(f"Updated {args.output} ({len(payload['records'])} records)")
                    previous = current
    except KeyboardInterrupt:
        return 0
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
