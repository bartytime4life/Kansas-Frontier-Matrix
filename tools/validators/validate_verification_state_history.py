#!/usr/bin/env python3
"""Validate and replay the bounded VerificationStateHistory profile."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages/evidence-resolver/src"
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(PACKAGE_SRC))

from evidence_resolver.verification_history import (  # noqa: E402
    ReplayResult,
    canonical_spec_hash,
    replay_state,
    validate_history_semantics,
)

from tools.validators._common.jsonschema_runner import load_validator
from tools.validators._common.public_safe_fixture import (
    Finding,
    add_finding,
    run_cli,
    serialize_result,
    validate_fixture_file,
)


SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/evidence/verification_state_history.schema.json"
)
FIXTURES_ROOT = (
    REPO_ROOT / "fixtures/contracts/v1/evidence/verification_state_history"
)
SCOPE = "evidence.verification_state_history"
_SCHEMA_VALIDATOR = load_validator(SCHEMA_PATH)

def _json_path(error_path: Sequence[object]) -> str:
    result = "$"
    for part in error_path:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def validate_document(candidate: object) -> list[Finding]:
    """Validate shape, hash, append order, time axes, and transition chain."""

    findings: set[Finding] = set()
    schema_errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        add_finding(
            findings,
            "VERIFICATION_HISTORY_SCHEMA_INVALID",
            _json_path(tuple(error.absolute_path)),
        )
    if schema_errors or not isinstance(candidate, dict):
        return sorted(findings)

    for finding in validate_history_semantics(candidate):
        add_finding(findings, finding.code, finding.path)

    return sorted(findings)


def validate_history_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_document)


def _run_fixture_suite() -> int:
    ok = True
    for expected_valid, directory in (
        (True, FIXTURES_ROOT / "valid"),
        (False, FIXTURES_ROOT / "invalid"),
    ):
        files = sorted(directory.glob("*.json"))
        if not files:
            print(f"FAIL {directory}: no JSON fixtures found")
            ok = False
            continue
        for path in files:
            findings = validate_history_file(path)
            accepted = not findings
            if accepted == expected_valid:
                label = "OK" if expected_valid else "EXPECTED_FAIL"
                print(f"{label} {path}")
            else:
                print(serialize_result(SCOPE, path, findings))
                ok = False
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--fixtures"]:
        return _run_fixture_suite()
    if "--fixtures" in args:
        print("--fixtures cannot be combined with file arguments", file=sys.stderr)
        return 2
    return run_cli(
        argv=args,
        description="Validate bounded VerificationStateHistory fixtures.",
        scope=SCOPE,
        validator=validate_history_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
