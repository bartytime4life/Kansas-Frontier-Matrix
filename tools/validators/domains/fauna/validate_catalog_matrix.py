#!/usr/bin/env python3
"""Bounded Fauna catalog-matrix validation.

The matrix validator does not create catalog authority. It only checks the shape,
finite states, and domain scoping of a declared Fauna catalog matrix.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (
    Finding,
    serialize_result,
    validate_fixture_file,
)

SCOPE = "fauna-catalog-matrix"
ALLOWED_DOMAINS = {"fauna"}
ALLOWED_STATUSES = {
    "active",
    "deny",
    "hold",
    "quarantine",
    "released",
    "review_required",
    "synthetic",
    "unknown",
    "withdrawn",
}


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code=code, path=path))


def validate_catalog_matrix(candidate: object) -> list[Finding]:
    """Return stable findings for a Fauna catalog matrix payload."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        _add(findings, "FAUNA_CATALOG_MATRIX_INVALID", "$")
        return sorted(findings)

    required_fields = {"id", "domain", "version"}
    for field in sorted(required_fields):
        if field not in candidate:
            _add(findings, "FAUNA_CATALOG_MATRIX_FIELD_MISSING", f"$.{field}")
    if "entries" not in candidate and "records" not in candidate:
        _add(findings, "FAUNA_CATALOG_MATRIX_FIELD_MISSING", "$.entries")

    domain = candidate.get("domain")
    if domain is not None and not isinstance(domain, str):
        _add(findings, "FAUNA_CATALOG_DOMAIN_TYPE_INVALID", "$.domain")
    elif isinstance(domain, str) and domain.casefold() not in {
        item.casefold() for item in ALLOWED_DOMAINS
    }:
        _add(findings, "FAUNA_CATALOG_DOMAIN_NOT_FAUNA", "$.domain")

    entries = candidate.get("entries", candidate.get("records"))
    if entries is not None and not isinstance(entries, list):
        _add(findings, "FAUNA_CATALOG_ENTRIES_TYPE_INVALID", "$.entries")
    if isinstance(entries, list):
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                _add(findings, "FAUNA_CATALOG_ENTRY_INVALID", f"$.entries[{index}]")
                continue
            for field in ("id", "kind", "status"):
                if field not in entry:
                    _add(findings, "FAUNA_CATALOG_ENTRY_FIELD_MISSING", f"$.entries[{index}].{field}")
            item_id = entry.get("id")
            if item_id is not None and not isinstance(item_id, str):
                _add(findings, "FAUNA_CATALOG_ENTRY_ID_TYPE_INVALID", f"$.entries[{index}].id")
            status = entry.get("status")
            if status is not None and not isinstance(status, str):
                _add(findings, "FAUNA_CATALOG_STATUS_TYPE_INVALID", f"$.entries[{index}].status")
            elif isinstance(status, str):
                normalized = status.casefold()
                if normalized not in {item.casefold() for item in ALLOWED_STATUSES}:
                    _add(findings, "FAUNA_CATALOG_STATUS_NOT_ALLOWED", f"$.entries[{index}].status")

    matrix_id = candidate.get("id")
    if matrix_id is not None and not isinstance(matrix_id, str):
        _add(findings, "FAUNA_CATALOG_ID_TYPE_INVALID", "$.id")
    elif isinstance(matrix_id, str) and not matrix_id.strip():
        _add(findings, "FAUNA_CATALOG_ID_EMPTY", "$.id")

    return sorted(findings)


def _validate_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_catalog_matrix)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a bounded Fauna catalog-matrix JSON file.")
    parser.add_argument("files", nargs="*", type=Path, help="JSON files to validate")
    args = parser.parse_args(argv)
    if not args.files:
        print("at least one catalog-matrix JSON file is required", file=sys.stderr)
        return 2

    any_failures = False
    for path in sorted(args.files, key=lambda item: str(item)):
        findings = _validate_file(path)
        any_failures = any_failures or bool(findings)
        print(serialize_result(SCOPE, path, findings))
    return 1 if any_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
