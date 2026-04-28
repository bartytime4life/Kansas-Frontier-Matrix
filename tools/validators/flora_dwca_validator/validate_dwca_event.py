#!/usr/bin/env python3
"""Minimal fail-closed DwC-A event row validator for flora ingestion."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

REQUIRED_COLUMNS = (
    "eventID",
    "occurrenceID",
    "scientificName",
    "eventDate",
    "decimalLatitude",
    "decimalLongitude",
    "basisOfRecord",
)

ALLOWED_BASIS = {"HumanObservation", "PreservedSpecimen", "MachineObservation"}


def fail(message: str) -> None:
    print(f"DENY: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_dwca_event.py <events.csv>")

    path = Path(sys.argv[1])
    if not path.exists():
        fail(f"missing DwC-A events CSV: {path}")

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)

        if reader.fieldnames is None:
            fail("events CSV is missing header row")

        for column in REQUIRED_COLUMNS:
            if column not in reader.fieldnames:
                fail(f"missing required column: {column}")

        rows = 0
        for idx, row in enumerate(reader, start=2):
            rows += 1
            for column in REQUIRED_COLUMNS:
                if not row.get(column):
                    fail(f"row {idx} missing required value for {column}")

            if row["basisOfRecord"] not in ALLOWED_BASIS:
                fail(f"row {idx} basisOfRecord must be one of {sorted(ALLOWED_BASIS)}")

        if rows == 0:
            fail("events CSV has no data rows")

    print(f"ALLOW: valid DwC-A events CSV: {path}")


if __name__ == "__main__":
    main()
