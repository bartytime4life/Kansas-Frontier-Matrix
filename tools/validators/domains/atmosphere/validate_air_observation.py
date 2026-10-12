#!/usr/bin/env python3
"""Validate AirObservation carriers through the governed domain profile.

This compatibility entrypoint narrows the existing observed-versus-modeled
validator to AirObservation inputs. It does not define independent parameter,
unit, source, evidence, policy, release, alerting, or life-safety authority.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Iterable, Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    validate_fixture_file,
)
from tools.validators._common.jsonschema_runner import load_validator  # noqa: E402
from tools.validators.domains.atmosphere.validate_observed_modeled_separation import (  # noqa: E402
    ValidationResult,
    outcome_for_findings,
    validate_candidate as validate_profile_candidate,
)


SCOPE = "atmosphere-air-observation"
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "domains"
    / "atmosphere"
    / "air_observation.schema.json"
)
_SCHEMA_VALIDATOR = load_validator(SCHEMA_PATH, check_formats=True)
_MAX_SCHEMA_FINDINGS = 50


def _json_path(parts: Iterable[object]) -> str:
    path = "$"
    for part in parts:
        if isinstance(part, int):
            path += f"[{part}]"
        else:
            path += f".{part}"
    return path


def _schema_findings(candidate: dict[str, object]) -> list[Finding]:
    errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), error.validator or ""),
    )
    findings = {
        Finding("AIR_OBSERVATION_SCHEMA_INVALID", _json_path(error.absolute_path))
        for error in errors[:_MAX_SCHEMA_FINDINGS]
    }
    if len(errors) > _MAX_SCHEMA_FINDINGS:
        findings.add(Finding("SCHEMA_FINDINGS_TRUNCATED", "$"))
    return sorted(findings)


def validate_candidate(candidate: object) -> list[Finding]:
    """Validate only AirObservation objects through the canonical profile."""

    if not isinstance(candidate, dict):
        return validate_profile_candidate(candidate)
    if candidate.get("object_type") != "AirObservation":
        return [Finding("AIR_OBSERVATION_REQUIRED", "$.object_type")]

    findings = _schema_findings(candidate)
    findings.extend(validate_profile_candidate(candidate))
    return sorted(set(findings))


def validate_file(path: Path | str) -> ValidationResult:
    """Decode one bounded JSON file and retain the profile's finite outcomes."""

    findings = tuple(validate_fixture_file(path, validate_candidate))
    return ValidationResult(outcome_for_findings(findings), findings)


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": str(path),
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "scope": SCOPE,
            "status": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate bounded Atmosphere AirObservation carriers."
    )
    parser.add_argument("files", nargs="*", type=Path)
    args = parser.parse_args(argv)
    if not args.files:
        print("at least one AirObservation file is required", file=sys.stderr)
        return 2

    failed = False
    for path in sorted(args.files, key=lambda item: str(item)):
        result = validate_file(path)
        failed = failed or result.outcome in {"DENY", "ERROR"}
        print(_serialize(path, result))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
