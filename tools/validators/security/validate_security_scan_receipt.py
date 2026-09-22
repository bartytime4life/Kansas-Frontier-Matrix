#!/usr/bin/env python3
"""Validate an imported security scanner receipt without granting authority."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = (
    ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "security"
    / "security_scan_receipt.schema.json"
)


class ReceiptError(ValueError):
    """A deterministic receipt validation failure."""


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ReceiptError(f"{path}: unreadable JSON: {exc}") from exc


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(
        timezone.utc
    )


def validate_receipt(document: Any, *, expected_commit: str | None = None) -> None:
    schema = load_json(SCHEMA_PATH)
    errors = sorted(
        Draft202012Validator(
            schema, format_checker=FormatChecker()
        ).iter_errors(document),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if errors:
        raise ReceiptError(
            "; ".join(
                f"{'/'.join(str(part) for part in error.absolute_path) or '<root>'}: "
                f"{error.message}"
                for error in errors
            )
        )

    if expected_commit and document["subject_commit"] != expected_commit:
        raise ReceiptError(
            f"SUBJECT_MISMATCH: {document['subject_commit']} != {expected_commit}"
        )

    started = parse_time(document["scan"]["started_at"])
    finished = parse_time(document["scan"]["finished_at"])
    if finished < started:
        raise ReceiptError("scan.finished_at precedes scan.started_at")

    now = datetime.now(timezone.utc)
    for suppression in document["suppressions"]:
        if parse_time(suppression["expires_at"]) <= now:
            raise ReceiptError(f"expired suppression: {suppression['identifier']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path)
    parser.add_argument("--expected-commit")
    args = parser.parse_args()
    try:
        validate_receipt(
            load_json(args.receipt), expected_commit=args.expected_commit
        )
    except ReceiptError as exc:
        print(f"SECURITY_SCAN_RECEIPT_INVALID: {exc}")
        return 2
    print("SECURITY_SCAN_RECEIPT_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
