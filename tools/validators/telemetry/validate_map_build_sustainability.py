"""Validate inactive fixture-only map-build sustainability telemetry.

The validator reads bounded local JSON, validates a closed candidate shape,
checks UTC window ordering, percentage bounds, and energy-to-carbon arithmetic,
and emits finite PASS/ABSTAIN/DENY/ERROR results. It performs no measurement,
network access, policy decision, release action, or repository mutation.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import re
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/telemetry/map_build_sustainability.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/telemetry/map_build_sustainability/cases.json"
PROFILE = "kfm.telemetry.map-build-sustainability.fixture.v1"
SCOPE = "telemetry.map_build_sustainability.fixture"
MAX_JSON_BYTES = 1_048_576
CASE_ID = re.compile(r"^[a-z][a-z0-9_]{2,79}$")
OUTCOMES = {"PASS", "ABSTAIN", "DENY"}
MAX_ROUNDING_TOLERANCE = Decimal("0.001")


class DuplicateKeyError(ValueError):
    """Raised when JSON repeats a mapping key."""


class InputError(ValueError):
    """Raised when bounded local input cannot be evaluated safely."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _json_pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _nonfinite(_value: str) -> object:
    raise InputError("non-finite JSON number")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise InputError("non-finite JSON number")
    return parsed


def _contains_surrogate(value: object, active: set[int] | None = None) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(char) <= 0xDFFF for char in value)
    if not isinstance(value, (Mapping, list)):
        return False
    active = set() if active is None else active
    identity = id(value)
    if identity in active:
        raise InputError("recursive input")
    active.add(identity)
    try:
        if isinstance(value, Mapping):
            return any(
                _contains_surrogate(key, active) or _contains_surrogate(item, active)
                for key, item in value.items()
            )
        return any(_contains_surrogate(item, active) for item in value)
    finally:
        active.remove(identity)


def _read_bounded(path: Path) -> str:
    try:
        if path.is_symlink() or not path.is_file():
            raise InputError("input is not a regular file")
        if path.stat().st_size > MAX_JSON_BYTES:
            raise InputError("input exceeds byte limit")
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise InputError("input cannot be read safely") from exc


def load_json(path: Path) -> tuple[object | None, tuple[Finding, ...]]:
    try:
        value = json.loads(
            _read_bounded(path),
            object_pairs_hook=_json_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
        if _contains_surrogate(value):
            return None, (Finding("JSON_UNPAIRED_SURROGATE", "$"),)
    except DuplicateKeyError:
        return None, (Finding("JSON_DUPLICATE_KEY", "$"),)
    except (InputError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("JSON_INPUT_INVALID", "$"),)
    return value, ()


def _json_path(parts: Sequence[object]) -> str:
    return "$" + "".join(
        f"[{part}]" if isinstance(part, int) else f".{part}" for part in parts
    )


def _load_schema() -> dict[str, Any]:
    value, findings = load_json(SCHEMA_PATH)
    if findings or not isinstance(value, dict):
        raise InputError("canonical schema is unavailable")
    Draft202012Validator.check_schema(value)
    return value


def _schema_findings(candidate: object) -> set[Finding]:
    try:
        validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
        errors = sorted(
            validator.iter_errors(candidate),
            key=lambda error: (list(error.absolute_path), str(error.validator)),
        )
    except (InputError, OSError, RecursionError, SchemaError, ValueError):
        return {Finding("SCHEMA_UNAVAILABLE", "$")}
    return {
        Finding("SCHEMA_INVALID", _json_path(list(error.absolute_path)))
        for error in errors[:100]
    }


def _utc(value: str) -> datetime:
    if not value.endswith("Z"):
        raise ValueError("timestamp is not UTC Z form")
    return datetime.fromisoformat(value[:-1] + "+00:00")


def _decimal(value: object) -> Decimal:
    if not isinstance(value, str):
        raise InvalidOperation
    parsed = Decimal(value)
    if not parsed.is_finite():
        raise InvalidOperation
    return parsed


def validate_candidate(candidate: object) -> ValidationResult:
    findings = _schema_findings(candidate)
    if findings or not isinstance(candidate, dict):
        outcome = (
            "ERROR"
            if any(item.code == "SCHEMA_UNAVAILABLE" for item in findings)
            else "DENY"
        )
        return ValidationResult(outcome, tuple(sorted(findings)))

    binding = candidate["build_binding"]
    energy = candidate["energy"]
    carbon = candidate["carbon"]

    try:
        if _utc(binding["started_at"]) >= _utc(binding["ended_at"]):
            findings.add(Finding("MEASUREMENT_WINDOW_INVALID", "$.build_binding"))
    except (TypeError, ValueError):
        findings.add(Finding("MEASUREMENT_WINDOW_INVALID", "$.build_binding"))

    for name, value in (
        ("energy", energy.get("relative_uncertainty_percent")),
        ("carbon", carbon.get("relative_uncertainty_percent")),
    ):
        if value is None:
            continue
        try:
            if _decimal(value) > Decimal("100"):
                findings.add(
                    Finding(
                        "UNCERTAINTY_PERCENT_OUT_OF_RANGE",
                        f"$.{name}.relative_uncertainty_percent",
                    )
                )
        except InvalidOperation:
            findings.add(
                Finding(
                    "DECIMAL_INVALID",
                    f"$.{name}.relative_uncertainty_percent",
                )
            )

    energy_available = energy["state"] == "AVAILABLE"
    carbon_available = carbon["state"] == "AVAILABLE"

    if not energy_available and carbon_available:
        findings.add(Finding("CARBON_REQUIRES_ENERGY", "$.carbon"))
    elif not energy_available and carbon.get("reason_code") != "ENERGY_UNAVAILABLE":
        findings.add(
            Finding(
                "CARBON_ABSTENTION_REASON_INCONSISTENT",
                "$.carbon.reason_code",
            )
        )

    if energy_available and carbon_available:
        try:
            joules = _decimal(energy["joules"])
            factor = _decimal(carbon["factor_grams_co2e_per_kwh"])
            actual = _decimal(carbon["grams_co2e"])
            tolerance = _decimal(carbon["rounding_tolerance_grams_co2e"])
            if tolerance > MAX_ROUNDING_TOLERANCE:
                findings.add(
                    Finding(
                        "ROUNDING_TOLERANCE_OUT_OF_RANGE",
                        "$.carbon.rounding_tolerance_grams_co2e",
                    )
                )
            with localcontext() as context:
                context.prec = 80
                expected = (joules / Decimal("3600000")) * factor
            if abs(actual - expected) > tolerance:
                findings.add(
                    Finding(
                        "CARBON_CALCULATION_MISMATCH",
                        "$.carbon.grams_co2e",
                    )
                )
        except (InvalidOperation, KeyError):
            findings.add(Finding("DECIMAL_INVALID", "$.carbon"))

    if findings:
        return ValidationResult("DENY", tuple(sorted(findings)))
    if not energy_available or not carbon_available:
        return ValidationResult("ABSTAIN", ())
    return ValidationResult("PASS", ())


def _set_patch_path(candidate: dict[str, Any], dotted: str, value: object) -> None:
    parts = dotted.split(".")
    target: dict[str, Any] = candidate
    for part in parts[:-1]:
        next_value = target.get(part)
        if not isinstance(next_value, dict):
            raise InputError("fixture patch path is invalid")
        target = next_value
    target[parts[-1]] = value


def _materialize_cases(entries: object) -> list[dict[str, Any]]:
    if not isinstance(entries, list) or not entries:
        raise InputError("fixture cases are invalid")
    materialized: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            raise InputError("fixture entry is invalid")
        case_id = entry.get("case_id")
        expected = entry.get("expected")
        if (
            not isinstance(case_id, str)
            or CASE_ID.fullmatch(case_id) is None
            or case_id in by_id
        ):
            raise InputError("fixture case id is invalid")
        if (
            not isinstance(expected, dict)
            or set(expected) != {"outcome", "finding_codes"}
            or expected.get("outcome") not in OUTCOMES
            or not isinstance(expected.get("finding_codes"), list)
            or expected["finding_codes"] != sorted(set(expected["finding_codes"]))
            or any(not isinstance(code, str) for code in expected["finding_codes"])
        ):
            raise InputError("fixture expected result is invalid")

        if "candidate" in entry:
            if set(entry) != {"case_id", "candidate", "expected"} or not isinstance(
                entry["candidate"], dict
            ):
                raise InputError("inline fixture candidate is invalid")
            candidate = copy.deepcopy(entry["candidate"])
        else:
            if set(entry) != {"case_id", "candidate_from", "patch", "expected"}:
                raise InputError("derived fixture entry is invalid")
            source = by_id.get(entry.get("candidate_from"))
            patch = entry.get("patch")
            if source is None or not isinstance(patch, dict) or not patch:
                raise InputError("derived fixture source or patch is invalid")
            candidate = copy.deepcopy(source)
            for path, value in patch.items():
                if not isinstance(path, str):
                    raise InputError("fixture patch path is invalid")
                if "." in path:
                    _set_patch_path(candidate, path, copy.deepcopy(value))
                else:
                    candidate[path] = copy.deepcopy(value)

        by_id[case_id] = candidate
        materialized.append(
            {"case_id": case_id, "candidate": candidate, "expected": expected}
        )
    return materialized


def run_fixture_suite(path: Path = FIXTURE_PATH) -> tuple[bool, dict[str, object]]:
    suite, load_findings = load_json(path)
    if load_findings or not isinstance(suite, dict):
        return False, {
            "authority": "NONE",
            "cases": [],
            "findings": [finding.code for finding in load_findings]
            or ["FIXTURE_SUITE_INVALID"],
            "ok": False,
            "outcome": "ERROR",
            "scope": SCOPE,
        }
    if set(suite) != {"profile", "cases"} or suite.get("profile") != PROFILE:
        return False, {
            "authority": "NONE",
            "cases": [],
            "findings": ["FIXTURE_SUITE_INVALID"],
            "ok": False,
            "outcome": "ERROR",
            "scope": SCOPE,
        }
    try:
        cases = _materialize_cases(suite["cases"])
    except InputError:
        return False, {
            "authority": "NONE",
            "cases": [],
            "findings": ["FIXTURE_SUITE_INVALID"],
            "ok": False,
            "outcome": "ERROR",
            "scope": SCOPE,
        }

    replay: list[dict[str, object]] = []
    ok = True
    for entry in cases:
        result = validate_candidate(entry["candidate"])
        expected = entry["expected"]
        case_ok = (
            result.outcome == expected["outcome"]
            and result.codes == expected["finding_codes"]
        )
        ok = ok and case_ok
        replay.append(
            {
                "actual_findings": result.codes,
                "actual_outcome": result.outcome,
                "case_id": entry["case_id"],
                "expected_findings": expected["finding_codes"],
                "expected_outcome": expected["outcome"],
                "ok": case_ok,
            }
        )
    return ok, {
        "authority": "NONE",
        "cases": replay,
        "findings": [] if ok else ["FIXTURE_REPLAY_MISMATCH"],
        "ok": ok,
        "outcome": "PASS" if ok else "DENY",
        "scope": SCOPE,
    }


def _emit(value: Mapping[str, object]) -> None:
    print(json.dumps(value, ensure_ascii=True, separators=(",", ":"), sort_keys=True))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--candidate", type=Path)
    args = parser.parse_args(argv)

    if args.fixtures:
        ok, report = run_fixture_suite()
        _emit(report)
        return 0 if ok else 1

    candidate, findings = load_json(args.candidate)
    if findings:
        _emit(
            {
                "authority": "NONE",
                "findings": sorted({finding.code for finding in findings}),
                "outcome": "ERROR",
                "scope": SCOPE,
            }
        )
        return 1
    result = validate_candidate(candidate)
    _emit(
        {
            "authority": "NONE",
            "findings": result.codes,
            "outcome": result.outcome,
            "scope": SCOPE,
        }
    )
    return 0 if result.outcome in {"PASS", "ABSTAIN"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
