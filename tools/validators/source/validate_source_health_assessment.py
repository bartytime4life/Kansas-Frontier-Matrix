#!/usr/bin/env python3
"""Validate one offline SourceHealthAssessment without creating authority."""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/source/source_health_assessment.schema.json"
MAX_BYTES = 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
FAILED_RESULTS = frozenset({"TIMEOUT", "HTTP_ERROR", "PARSE_ERROR", "AUTH_ERROR"})
SCOPE = "source.health_assessment.offline.v1"
NON_EFFECTS = (
    "no_network_request",
    "no_source_activation",
    "no_source_truth_or_scientific_conclusion",
    "no_raw_or_lifecycle_write",
    "no_policy_review_or_candidate_authority",
    "no_promotion_release_deployment_or_publication",
)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised for NaN or infinity tokens, including overflowed floats."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _compact(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None and parsed.utcoffset() is not None else None


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("SOURCE_HEALTH_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("SOURCE_HEALTH_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("SOURCE_HEALTH_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("SOURCE_HEALTH_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("SOURCE_HEALTH_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("SOURCE_HEALTH_JSON_INVALID", "/"),)
    except (OSError, RecursionError, ValueError):
        return None, (Finding("SOURCE_HEALTH_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("SOURCE_HEALTH_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema,
                    format_checker=FormatChecker(),
                ).iter_errors(value),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return (Finding("SOURCE_HEALTH_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("SOURCE_HEALTH_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SOURCE_HEALTH_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    result_class = value.get("result_class")
    health_outcome = value.get("health_outcome")
    reasons_value = value.get("reasons")
    reasons = set(reasons_value) if isinstance(reasons_value, list) else set()

    if result_class in FAILED_RESULTS and health_outcome == "HEALTHY":
        findings.add(Finding("SOURCE_HEALTH_FAILED_AS_HEALTHY", "/health_outcome"))
    if health_outcome == "UNAVAILABLE" and result_class not in FAILED_RESULTS:
        findings.add(
            Finding("SOURCE_HEALTH_UNAVAILABLE_WITHOUT_FAILURE", "/result_class")
        )
    if result_class in FAILED_RESULTS and "RETRIEVAL_FAILED" not in reasons:
        findings.add(Finding("SOURCE_HEALTH_RETRIEVAL_REASON_REQUIRED", "/reasons"))
    if result_class == "PARSE_ERROR" and "SCHEMA_OR_PARSE_FAILURE" not in reasons:
        findings.add(Finding("SOURCE_HEALTH_PARSE_REASON_REQUIRED", "/reasons"))
    if result_class == "AUTH_ERROR" and "AUTH_FAILURE" not in reasons:
        findings.add(Finding("SOURCE_HEALTH_AUTH_REASON_REQUIRED", "/reasons"))
    if result_class == "EMPTY":
        if health_outcome == "HEALTHY":
            findings.add(Finding("SOURCE_HEALTH_EMPTY_AS_HEALTHY", "/health_outcome"))
        if "EMPTY_NOT_CLEAR" not in reasons:
            findings.add(Finding("SOURCE_HEALTH_EMPTY_REASON_REQUIRED", "/reasons"))
    if result_class == "NOT_PROBED":
        if health_outcome != "UNKNOWN":
            findings.add(Finding("SOURCE_HEALTH_NOT_PROBED_OUTCOME_INVALID", "/health_outcome"))
        if "NOT_PROBED" not in reasons:
            findings.add(Finding("SOURCE_HEALTH_NOT_PROBED_REASON_REQUIRED", "/reasons"))

    material_change = value.get("material_change")
    if material_change is True and "MATERIAL_CHANGE" not in reasons:
        findings.add(Finding("SOURCE_HEALTH_MATERIAL_REASON_REQUIRED", "/reasons"))
    if material_change is False and "MATERIAL_CHANGE" in reasons:
        findings.add(Finding("SOURCE_HEALTH_MATERIAL_REASON_FORBIDDEN", "/reasons"))

    probed_at = _parse_time(value.get("probed_at"))
    last_success_at = _parse_time(value.get("last_success_at"))
    freshness_deadline = _parse_time(value.get("freshness_deadline"))
    if probed_at is not None and last_success_at is not None and last_success_at > probed_at:
        findings.add(Finding("SOURCE_HEALTH_LAST_SUCCESS_AFTER_PROBE", "/last_success_at"))
    if probed_at is not None and freshness_deadline is not None:
        expired = probed_at > freshness_deadline
        if expired and health_outcome == "HEALTHY":
            findings.add(Finding("SOURCE_HEALTH_EXPIRED_AS_HEALTHY", "/health_outcome"))
        if expired and "FRESHNESS_EXPIRED" not in reasons:
            findings.add(Finding("SOURCE_HEALTH_EXPIRED_REASON_REQUIRED", "/reasons"))
        if not expired and "FRESHNESS_EXPIRED" in reasons:
            findings.add(Finding("SOURCE_HEALTH_EXPIRED_REASON_CONFLICT", "/reasons"))
    if health_outcome == "HEALTHY" and "WITHIN_FRESHNESS" not in reasons:
        findings.add(Finding("SOURCE_HEALTH_FRESH_REASON_REQUIRED", "/reasons"))

    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema = _schema_findings(value)
    if schema:
        return Result("DENY", schema)
    semantic = _semantic_findings(value)
    if semantic:
        return Result("DENY", semantic)
    if value.get("health_outcome") == "UNKNOWN" or value.get("result_class") == "NOT_PROBED":
        return Result(
            "ABSTAIN",
            (Finding("SOURCE_HEALTH_UNKNOWN_REQUIRES_REVIEW", "/health_outcome"),),
        )
    return Result("PASS", ())


def validate_doc(value: Mapping[str, Any]) -> list[str]:
    """Compatibility wrapper returning finite codes for denial/error findings."""
    result = validate_payload(value)
    return [finding.code for finding in result.findings] if result.outcome in {"DENY", "ERROR"} else []


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    return Result("ERROR", findings) if value is None else validate_payload(value)


def _serialize(path: Path | None, result: Result) -> str:
    return _compact(
        {
            "authority": "NONE",
            "execution_mode": "OFFLINE_VALIDATION",
            "file": path.as_posix() if path else None,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": NON_EFFECTS,
            "outcome": result.outcome,
            "scope": SCOPE,
        }
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args(argv)
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
