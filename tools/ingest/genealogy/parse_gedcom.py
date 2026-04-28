#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

GEDCOM_RE = re.compile(r"^(\d+)\s+(@[^@]+@\s+)?([A-Za-z0-9_]+)(?:\s+(.*))?$")
EVENT_TAGS = {"BIRT", "DEAT", "MARR", "RESI", "BURI", "CENS", "EMIG", "IMMI"}


def _line_record(line: str) -> tuple[int, str | None, str, str]:
    match = GEDCOM_RE.match(line.rstrip("\n"))
    if not match:
        raise ValueError(f"invalid GEDCOM line: {line!r}")
    level = int(match.group(1))
    xref = match.group(2).strip() if match.group(2) else None
    tag = match.group(3)
    rest = (match.group(4) or "").strip()
    return level, xref, tag, rest


def parse_gedcom(input_path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    current_person: str | None = None
    current_event: dict[str, Any] | None = None

    with input_path.open("r", encoding="utf-8") as handle:
        for line_no, raw in enumerate(handle, start=1):
            stripped = raw.strip()
            if not stripped:
                continue

            level, xref, tag, rest = _line_record(raw)

            if level == 0:
                current_event = None
                if tag == "INDI" and xref:
                    current_person = xref
                else:
                    current_person = None
                continue

            if current_person is None:
                continue

            if level == 1 and tag in EVENT_TAGS:
                current_event = {
                    "person_id": current_person,
                    "event_type": tag,
                    "event_date": None,
                    "place": None,
                    "source_value": rest or None,
                    "source_line": line_no,
                }
                rows.append(current_event)
                continue

            if current_event is None:
                continue

            if level == 2 and tag == "DATE":
                current_event["event_date"] = rest or None
            elif level == 2 and tag == "PLAC":
                current_event["place"] = rest or None

    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse GEDCOM into raw event NDJSON rows.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rows = parse_gedcom(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")
    print(f"WROTE: {len(rows)} rows -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
