#!/usr/bin/env python3
"""Fail-closed living-person screen for KFM's bounded synthetic historical profile.

This entrypoint deliberately reuses the existing
``validate_historical_person_place_event_resolution`` contract/schema/fixture
validator. It does not infer whether a real person is living, establish consent,
or create release authority. Candidates outside that validated synthetic,
historical-only profile fail closed.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

VALIDATOR_DIR = Path(__file__).resolve().parents[1]
if str(VALIDATOR_DIR) not in sys.path:
    sys.path.insert(0, str(VALIDATOR_DIR))

from validate_historical_person_place_event_resolution import (  # noqa: E402
    FIXTURE_ROOT,
    Finding,
    validate_file,
)


def screen_file(path: Path) -> tuple[bool, str, list[Finding]]:
    """Return whether *path* clears the bounded living-person safety screen."""
    candidate, findings = validate_file(path)
    if candidate is None:
        return False, "INPUT_INVALID", findings

    codes = {finding.code for finding in findings}
    if "LIVING_PERSON_DENIED" in codes:
        return False, "LIVING_PERSON_DENIED", findings
    if findings:
        return False, "CANDIDATE_INVALID", findings

    scope = candidate.get("candidate_scope")
    if not isinstance(scope, dict):
        return False, "CANDIDATE_SCOPE_INVALID", findings
    if scope.get("synthetic_fixture") is not True or scope.get("historical_only") is not True:
        return False, "SYNTHETIC_HISTORICAL_SCOPE_REQUIRED", findings
    if scope.get("living_person") is not False:
        return False, "LIVING_PERSON_DENIED", findings

    return True, "HISTORICAL_SYNTHETIC_SCOPE_CONFIRMED", findings


def run_fixtures() -> int:
    historical = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
    living = FIXTURE_ROOT / "invalid" / "living_person_denied.json"
    failures: list[str] = []

    if not historical or not living.is_file():
        print("LIVING_PERSON_SCREEN_FIXTURES_ERROR required fixture profile is incomplete")
        return 2

    for path in historical:
        allowed, _reason, _findings = screen_file(path)
        if not allowed:
            failures.append(f"historical/{path.name}")

    allowed, reason, _findings = screen_file(living)
    if allowed or reason != "LIVING_PERSON_DENIED":
        failures.append(f"living/{living.name}")

    if failures:
        for item in failures:
            print(f"LIVING_PERSON_SCREEN_FIXTURE_POLARITY_FAIL file={item}")
        return 1

    print(
        "LIVING_PERSON_SCREEN_FIXTURES_VALID "
        f"historical_allowed={len(historical)} living_denied=1"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument(
        "--fixtures",
        action="store_true",
        help="replay the existing synthetic historical/living-person fixture polarity",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        if args.paths:
            raise SystemExit("--fixtures cannot be combined with paths")
        return run_fixtures()
    if not args.paths:
        raise SystemExit("at least one path is required unless --fixtures is used")

    failed = False
    for path in args.paths:
        allowed, reason, findings = screen_file(path)
        if allowed:
            print(
                "LIVING_PERSON_SCREEN_ALLOWED "
                f"file={path.name} scope=historical_synthetic"
            )
            continue

        failed = True
        codes = ",".join(sorted({finding.code for finding in findings})) or reason
        print(
            "LIVING_PERSON_SCREEN_DENIED "
            f"file={path.name} reason={reason} findings={codes}"
        )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
