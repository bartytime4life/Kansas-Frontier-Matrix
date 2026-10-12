#!/usr/bin/env python3
"""Validate smoke-aware NDVI readiness sidecars without network access."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[5]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/agriculture/ndvi_readiness.schema.json"
)
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100


class DuplicateKeyError(ValueError):
    """Raised when an object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised for non-standard NaN or Infinity tokens."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_payload(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
        )
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_UNREADABLE", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(payload: Mapping[str, Any]) -> list[Finding]:
    try:
        errors = list(
            islice(_schema_validator().iter_errors(payload), MAX_SCHEMA_FINDINGS + 1)
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    ordered = sorted(
        errors,
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )[:MAX_SCHEMA_FINDINGS]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in ordered
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _readiness_level(score: float) -> int:
    if score < 0.30:
        return 0
    if score < 0.60:
        return 1
    if score < 0.80:
        return 2
    return 3


def _expected_reasons(payload: Mapping[str, Any]) -> list[str]:
    thresholds = payload["thresholds"]
    summary = payload["tile_summary"]
    critical = payload["critical_aoi_summary"]
    inputs = payload["inputs"]

    reasons: set[str] = set()
    if float(summary["readiness_score"]) < float(
        thresholds["min_mask_health_emit"]
    ):
        reasons.add("LOW_MASK_HEALTH")
    if float(summary["fraction_ready"]) < float(
        thresholds["min_area_fraction_emit"]
    ):
        reasons.add("LOW_READY_AREA")
    if (
        thresholds["no_heavy_smoke_in_aois"] is True
        and int(critical["heavy_smoke_overlap_count"]) > 0
    ):
        reasons.add("HEAVY_SMOKE_AOI")
    if any(item["receipt_state"] != "RESOLVED" for item in inputs):
        reasons.add("INPUT_RECEIPT_UNRESOLVED")
    return sorted(reasons)


def _semantic_findings(payload: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    summary = payload["tile_summary"]
    decision = payload["emit_decision"]

    score = float(summary["readiness_score"])
    if int(summary["level"]) != _readiness_level(score):
        findings.append(Finding("READINESS_LEVEL_MISMATCH", "/tile_summary/level"))

    counties = payload["county_readiness"]
    fips_values = [county["fips"] for county in counties]
    if fips_values != sorted(fips_values) or len(fips_values) != len(
        set(fips_values)
    ):
        findings.append(
            Finding("COUNTY_READINESS_NOT_CANONICAL", "/county_readiness")
        )

    sources = [item["source"] for item in payload["inputs"]]
    if sources != sorted(sources) or len(sources) != len(set(sources)):
        findings.append(Finding("INPUTS_NOT_CANONICAL", "/inputs"))

    expected = _expected_reasons(payload)
    if decision["reasons"] != expected:
        findings.append(
            Finding("DECISION_REASONS_MISMATCH", "/emit_decision/reasons")
        )

    expected_outcome = "EMIT_CANDIDATE" if not expected else "HOLD"
    if decision["outcome"] != expected_outcome:
        findings.append(
            Finding("DECISION_OUTCOME_MISMATCH", "/emit_decision/outcome")
        )

    blocker = summary["primary_blocker"]
    if not expected and blocker is not None:
        findings.append(
            Finding("PRIMARY_BLOCKER_UNEXPECTED", "/tile_summary/primary_blocker")
        )
    if expected and blocker not in expected:
        findings.append(
            Finding("PRIMARY_BLOCKER_MISMATCH", "/tile_summary/primary_blocker")
        )

    governance = payload["governance"]
    if (
        governance["promotion_eligible"] is not False
        or governance["public_use_allowed"] is not False
        or governance["release_state"] != "not_released"
        or governance["review_state"] != "fixture_only"
    ):
        findings.append(Finding("GOVERNANCE_STATE_INVALID", "/governance"))
    return findings


def validate_payload(payload: Mapping[str, Any]) -> ValidationResult:
    """Validate a parsed sidecar against shape and semantic closure."""

    findings = _schema_findings(payload)
    if not findings:
        findings.extend(_semantic_findings(payload))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_file(path: Path) -> ValidationResult:
    """Read and validate one bounded JSON file."""

    payload, findings = _load_payload(path)
    if payload is None:
        return ValidationResult(tuple(sorted(findings)))
    return validate_payload(payload)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a fixture-only smoke-aware NDVI readiness sidecar."
    )
    parser.add_argument("path", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    result = validate_file(args.path)
    output = {
        "ok": result.ok,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "scope": "fixture-only-ndvi-readiness-sidecar",
        "authority": {
            "emission": False,
            "promotion": False,
            "release": False,
            "publication": False,
        },
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
