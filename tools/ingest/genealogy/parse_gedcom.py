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
    current_family: str | None = None
    family_spouses: dict[str, set[str]] = {}
    current_event: dict[str, Any] | None = None
    current_family_event: dict[str, Any] | None = None

    def flush_family_event() -> None:
        nonlocal current_family_event
        if current_family is None or current_family_event is None:
            return
        for spouse in sorted(family_spouses.get(current_family, set())):
            rows.append(
                {
                    "person_id": spouse,
                    "event_type": current_family_event["event_type"],
                    "event_date": current_family_event["event_date"],
                    "place": current_family_event["place"],
                    "source_value": current_family_event["source_value"],
                    "source_line": current_family_event["source_line"],
                    "family_id": current_family,
                }
            )
        current_family_event = None

    with input_path.open("r", encoding="utf-8") as handle:
        for line_no, raw in enumerate(handle, start=1):
            stripped = raw.strip()
            if not stripped:
                continue

            level, xref, tag, rest = _line_record(raw)

            if level == 0:
                flush_family_event()
                current_event = None
                current_family_event = None
                if tag == "INDI" and xref:
                    current_person = xref
                    current_family = None
                elif tag == "FAM" and xref:
                    current_family = xref
                    current_person = None
                    family_spouses.setdefault(current_family, set())
                else:
                    current_person = None
                    current_family = None
                continue

            if level == 1 and current_person and tag in EVENT_TAGS:
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

            if level == 1 and current_family and tag in EVENT_TAGS:
                current_family_event = {
                    "family_id": current_family,
                    "event_type": tag,
                    "event_date": None,
                    "place": None,
                    "source_value": rest or None,
                    "source_line": line_no,
                }
                continue

            if level == 1 and current_family and tag in {"HUSB", "WIFE"} and rest:
                family_spouses[current_family].add(rest)
                continue

            if level == 2 and current_event is not None:
                if tag == "DATE":
                    current_event["event_date"] = rest or None
                elif tag == "PLAC":
                    current_event["place"] = rest or None
                continue

            if level == 2 and current_family_event is not None:
                if tag == "DATE":
                    current_family_event["event_date"] = rest or None
                elif tag == "PLAC":
                    current_family_event["place"] = rest or None

                if tag in {"DATE", "PLAC"}:
                    continue

            if level == 1 and current_family and current_family_event is not None and tag not in {"DATE", "PLAC"}:
                flush_family_event()

    flush_family_event()

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
