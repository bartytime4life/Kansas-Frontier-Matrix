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
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    validate_fixture_file,
)
from tools.validators.domains.atmosphere.validate_observed_modeled_separation import (  # noqa: E402
    ValidationResult,
    outcome_for_findings,
    validate_candidate as validate_profile_candidate,
)


SCOPE = "atmosphere-air-observation"


def validate_candidate(candidate: object) -> list[Finding]:
    """Validate only AirObservation objects through the canonical profile."""

    if not isinstance(candidate, dict):
        return validate_profile_candidate(candidate)
    if candidate.get("object_type") != "AirObservation":
        return [Finding("AIR_OBSERVATION_REQUIRED", "$.object_type")]
    return validate_profile_candidate(candidate)


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
