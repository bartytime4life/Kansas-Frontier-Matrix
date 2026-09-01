#!/usr/bin/env python3
"""Bounded Fauna source-descriptor validation.

This checker intentionally validates only the declared source metadata shape and
fail-closed safety posture. It does not admit any live source, authorize a crawl,
resolve rights, or approve publication.
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

SCOPE = "fauna-source-descriptor"
ALLOWED_SOURCE_TYPES = {
    "agency",
    "aggregator",
    "citizen_science",
    "synthetic",
    "survey",
    "telemetry",
    "unknown",
}
ALLOWED_SOURCE_FAMILIES = {
    "fauna",
    "aggregator",
    "agency",
    "synthetic",
    "unknown",
}
ALLOWED_ROLES = {
    "agency",
    "authority",
    "candidate",
    "observed",
    "observational",
    "regulated",
    "synthetic",
    "unknown",
}
ALLOWED_RIGHTS_STATES = {
    "approved",
    "abstain",
    "deny",
    "hold",
    "review_required",
    "unknown",
}
ALLOWED_SENSITIVITY_STATES = {
    "public_safe",
    "public_safe_after_withholding",
    "sensitive_withheld",
    "deny",
    "hold",
    "review_required",
    "unknown",
}


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code=code, path=path))


def validate_source_descriptor(candidate: object) -> list[Finding]:
    """Return stable, machine-comparable findings for a Fauna SourceDescriptor."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        _add(findings, "FAUNA_SOURCE_DESCRIPTOR_INVALID", "$")
        return sorted(findings)

    required_fields = {
        "id",
        "source_family",
        "source_type",
        "source_role",
        "rights_state",
        "sensitivity_state",
        "public_safe",
    }
    for field in sorted(required_fields):
        if field not in candidate:
            _add(findings, "FAUNA_SOURCE_DESCRIPTOR_FIELD_MISSING", f"$.{field}")

    source_family = candidate.get("source_family")
    if source_family is not None and not isinstance(source_family, str):
        _add(findings, "FAUNA_SOURCE_FAMILY_TYPE_INVALID", "$.source_family")
    elif isinstance(source_family, str) and source_family.casefold() not in {
        item.casefold() for item in ALLOWED_SOURCE_FAMILIES
    }:
        _add(findings, "FAUNA_SOURCE_FAMILY_NOT_ALLOWED", "$.source_family")

    source_type = candidate.get("source_type")
    if source_type is not None and not isinstance(source_type, str):
        _add(findings, "FAUNA_SOURCE_TYPE_TYPE_INVALID", "$.source_type")
    elif isinstance(source_type, str) and source_type.casefold() not in {
        item.casefold() for item in ALLOWED_SOURCE_TYPES
    }:
        _add(findings, "FAUNA_SOURCE_TYPE_NOT_ALLOWED", "$.source_type")

    source_role = candidate.get("source_role")
    if source_role is not None and not isinstance(source_role, str):
        _add(findings, "FAUNA_SOURCE_ROLE_TYPE_INVALID", "$.source_role")
    elif isinstance(source_role, str) and source_role.casefold() not in {
        item.casefold() for item in ALLOWED_ROLES
    }:
        _add(findings, "FAUNA_SOURCE_ROLE_NOT_ALLOWED", "$.source_role")

    rights_state = candidate.get("rights_state")
    if rights_state is not None and not isinstance(rights_state, str):
        _add(findings, "FAUNA_RIGHTS_STATE_TYPE_INVALID", "$.rights_state")
    elif isinstance(rights_state, str) and rights_state.casefold() not in {
        item.casefold() for item in ALLOWED_RIGHTS_STATES
    }:
        _add(findings, "FAUNA_RIGHTS_STATE_NOT_ALLOWED", "$.rights_state")

    sensitivity_state = candidate.get("sensitivity_state")
    if sensitivity_state is not None and not isinstance(sensitivity_state, str):
        _add(findings, "FAUNA_SENSITIVITY_STATE_TYPE_INVALID", "$.sensitivity_state")
    elif isinstance(sensitivity_state, str) and sensitivity_state.casefold() not in {
        item.casefold() for item in ALLOWED_SENSITIVITY_STATES
    }:
        _add(findings, "FAUNA_SENSITIVITY_STATE_NOT_ALLOWED", "$.sensitivity_state")

    public_safe = candidate.get("public_safe")
    if public_safe is not None and not isinstance(public_safe, bool):
        _add(findings, "FAUNA_PUBLIC_SAFE_TYPE_INVALID", "$.public_safe")
    elif isinstance(public_safe, bool):
        if public_safe and isinstance(sensitivity_state, str):
            allowed_public = {"public_safe", "public_safe_after_withholding"}
            if sensitivity_state.casefold() not in {item.casefold() for item in allowed_public}:
                _add(findings, "FAUNA_PUBLIC_SAFE_REQUIRES_PUBLIC_STATE", "$.public_safe")
        elif not public_safe and isinstance(sensitivity_state, str):
            if sensitivity_state.casefold() in {"public_safe", "public_safe_after_withholding"}:
                _add(findings, "FAUNA_PRIVATE_SOURCE_CANNOT_BE_PUBLIC_SAFE", "$.public_safe")

    descriptor_id = candidate.get("id")
    if descriptor_id is not None and not isinstance(descriptor_id, str):
        _add(findings, "FAUNA_SOURCE_ID_TYPE_INVALID", "$.id")
    elif isinstance(descriptor_id, str) and not descriptor_id.strip():
        _add(findings, "FAUNA_SOURCE_ID_EMPTY", "$.id")

    return sorted(findings)


def _validate_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_source_descriptor)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a bounded Fauna source descriptor JSON file.")
    parser.add_argument("files", nargs="*", type=Path, help="JSON files to validate")
    args = parser.parse_args(argv)
    if not args.files:
        print("at least one source descriptor JSON file is required", file=sys.stderr)
        return 2

    any_failures = False
    for path in sorted(args.files, key=lambda item: str(item)):
        findings = _validate_file(path)
        any_failures = any_failures or bool(findings)
        print(serialize_result(SCOPE, path, findings))
    return 1 if any_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
