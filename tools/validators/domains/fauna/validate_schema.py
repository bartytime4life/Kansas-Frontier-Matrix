#!/usr/bin/env python3
"""Bounded JSON schema validation for Fauna data and profiles.

This is intentionally fail-closed and non-authoritative: it validates the declared
shape of a candidate JSON document, but does not admit a source, prove a release,
approve public delivery, or authorize a live workflow.
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

SCOPE = "fauna-schema"
ALLOWED_JSON_TYPES = {
    "array",
    "boolean",
    "integer",
    "null",
    "number",
    "object",
    "string",
}


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code=code, path=path))


def validate_schema(candidate: object) -> list[Finding]:
    """Return stable, deterministic findings for a Fauna schema-bearing JSON candidate."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        _add(findings, "FAUNA_SCHEMA_INVALID", "$")
        return sorted(findings)

    if "$schema" in candidate and not isinstance(candidate["$schema"], str):
        _add(findings, "FAUNA_SCHEMA_URI_TYPE_INVALID", '$."$schema"')
    if "type" in candidate and not isinstance(candidate["type"], str):
        _add(findings, "FAUNA_SCHEMA_TYPE_EXPECTED_STRING", "$.type")
    elif isinstance(candidate.get("type"), str):
        if candidate["type"] not in ALLOWED_JSON_TYPES:
            _add(findings, "FAUNA_SCHEMA_TYPE_NOT_ALLOWED", "$.type")

    if "properties" in candidate and not isinstance(candidate["properties"], dict):
        _add(findings, "FAUNA_SCHEMA_PROPERTIES_TYPE_INVALID", "$.properties")
    if "required" in candidate and not isinstance(candidate["required"], list):
        _add(findings, "FAUNA_SCHEMA_REQUIRED_TYPE_INVALID", "$.required")
    if "items" in candidate and not isinstance(candidate["items"], (dict, list)):
        _add(findings, "FAUNA_SCHEMA_ITEMS_TYPE_INVALID", "$.items")

    return sorted(findings)


def _validate_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_schema)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a bounded Fauna schema JSON file.")
    parser.add_argument("files", nargs="*", type=Path, help="JSON files to validate")
    args = parser.parse_args(argv)
    if not args.files:
        print("at least one schema JSON file is required", file=sys.stderr)
        return 2

    any_failures = False
    for path in sorted(args.files, key=lambda item: str(item)):
        findings = _validate_file(path)
        any_failures = any_failures or bool(findings)
        print(serialize_result(SCOPE, path, findings))
    return 1 if any_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
