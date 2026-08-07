#!/usr/bin/env python3
"""Replay MapContextEnvelope → EvidenceDrawerPayload admission fixtures.

A passing run proves deterministic cross-object admission behavior and current
DecisionEnvelope schema conformance only. It does not resolve evidence, evaluate
policy, authenticate a caller or reviewer, establish release state, authorize
public use, or publish anything.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = ROOT / "packages/envelopes/src"
if str(PACKAGE_SRC) not in sys.path:
    sys.path.insert(0, str(PACKAGE_SRC))

from envelopes import (  # noqa: E402
    EnvelopeBuildError,
    build_map_context_evidence_drawer_admission_candidate,
)

FIXTURE_ROOT = ROOT / "fixtures/ui/map_context_evidence_drawer_admission"
MANIFEST = FIXTURE_ROOT / "cases.json"
DECISION_SCHEMA = ROOT / "schemas/contracts/v1/runtime/decision_envelope.schema.json"
MAX_JSON_BYTES = 512 * 1024
_CASE_ID_RE = re.compile(r"^[a-z][a-z0-9-]{0,79}$")


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise DuplicateKeyError
        output[key] = value
    return output


def _reject_constant(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _load_object(path: Path) -> dict[str, object]:
    if path.is_symlink() or not path.is_file():
        raise ValueError("input is not a regular file")
    if path.stat().st_size > MAX_JSON_BYTES:
        raise ValueError("input exceeds validation budget")
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except (
        OSError,
        UnicodeError,
        json.JSONDecodeError,
        DuplicateKeyError,
        NonFiniteNumberError,
        RecursionError,
        ValueError,
    ) as exc:
        raise ValueError("input could not be parsed safely") from exc
    if not isinstance(value, dict):
        raise ValueError("input root must be an object")
    return value


def _repo_path(value: object) -> Path:
    if not isinstance(value, str) or not value or "\\" in value or value.startswith("/"):
        raise ValueError("fixture path is not canonical")
    relative = PurePosixPath(value)
    if str(relative) != value or any(part in {".", ".."} for part in relative.parts):
        raise ValueError("fixture path is not canonical")
    if not value.startswith("fixtures/ui/"):
        raise ValueError("fixture path is outside admitted roots")
    candidate = ROOT.joinpath(*relative.parts)
    if candidate.is_symlink() or not candidate.is_file():
        raise ValueError("fixture path is not a regular file")
    candidate.resolve(strict=True).relative_to(ROOT.resolve(strict=True))
    return candidate


def _schema_validator() -> Draft202012Validator:
    schema = _load_object(DECISION_SCHEMA)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def run_cases() -> int:
    try:
        manifest = _load_object(MANIFEST)
        cases = manifest.get("cases")
        if not isinstance(cases, list) or not cases:
            raise ValueError("cases must be a nonempty array")
        schema_validator = _schema_validator()
    except ValueError:
        print("MAP_CONTEXT_DRAWER_ADMISSION_CASES_ERROR code=MANIFEST_INVALID")
        return 2

    failures: list[str] = []
    for raw_case in cases:
        try:
            if not isinstance(raw_case, dict):
                raise ValueError("case is not an object")
            case_id = raw_case.get("case_id")
            if not isinstance(case_id, str) or _CASE_ID_RE.fullmatch(case_id) is None:
                raise ValueError("case id is invalid")
            evaluated_at = raw_case.get("evaluated_at")
            allow_system_test = raw_case.get("allow_system_test")
            expected_outcome = raw_case.get("expected_outcome")
            expected_reason = raw_case.get("expected_reason_code")
            expected_refs = raw_case.get("expected_evidence_refs")
            if (
                not isinstance(evaluated_at, str)
                or not isinstance(allow_system_test, bool)
                or not isinstance(expected_outcome, str)
                or not isinstance(expected_reason, str)
                or not isinstance(expected_refs, list)
                or any(not isinstance(item, str) for item in expected_refs)
            ):
                raise ValueError("case expectation is invalid")

            candidate = build_map_context_evidence_drawer_admission_candidate(
                decision_id=f"decision:render:{case_id}",
                evaluated_at=evaluated_at,
                map_context=_load_object(_repo_path(raw_case.get("map_context"))),
                drawer_payload=_load_object(_repo_path(raw_case.get("drawer_payload"))),
                allow_system_test=allow_system_test,
            )
            schema_errors = list(schema_validator.iter_errors(candidate))
            matches = (
                candidate.get("outcome") == expected_outcome
                and candidate.get("decision") == expected_outcome
                and candidate.get("reason_code") == expected_reason
                and candidate.get("evidence_refs") == expected_refs
                and not schema_errors
            )
        except (ValueError, EnvelopeBuildError):
            case_id = (
                raw_case.get("case_id")
                if isinstance(raw_case, dict)
                and isinstance(raw_case.get("case_id"), str)
                else "invalid-case"
            )
            matches = False
            candidate = {}

        if not matches:
            failures.append(case_id)
        print(
            "MAP_CONTEXT_DRAWER_ADMISSION_CASE "
            f"case={case_id} outcome={candidate.get('outcome', 'ERROR')} "
            f"reason={candidate.get('reason_code', 'CASE_INVALID')} "
            f"match={'true' if matches else 'false'}"
        )

    if failures:
        for case_id in failures:
            print(f"MAP_CONTEXT_DRAWER_ADMISSION_MISMATCH case={case_id}")
        return 1

    print(
        "MAP_CONTEXT_DRAWER_ADMISSION_CASES_VALID "
        f"cases={len(cases)} no_network=true authority=candidate-only"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.cases:
        print("--cases is required", file=sys.stderr)
        return 2
    return run_cases()


if __name__ == "__main__":
    raise SystemExit(main())
