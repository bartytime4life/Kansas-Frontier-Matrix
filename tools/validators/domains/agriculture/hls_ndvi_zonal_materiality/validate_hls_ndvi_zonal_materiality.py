#!/usr/bin/env python3
"""Validate fixture-only HLS NDVI zonal materiality assessments."""

from __future__ import annotations

import argparse
from datetime import datetime
from decimal import Decimal
import hashlib
import json
import math
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[5]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/agriculture/"
    "hls_ndvi_zonal_materiality_assessment.schema.json"
)
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
COUNT_KEYS = (
    "valid",
    "cloud",
    "shadow",
    "adjacent_cloud",
    "high_aerosol",
    "snow",
    "water",
    "other_invalid",
)


class DuplicateKeyError(ValueError):
    """Raised when an object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised for NaN or Infinity tokens."""


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


def canonical_spec_hash(payload: Mapping[str, Any]) -> str:
    """Return the deterministic hash excluding the top-level spec_hash."""

    body = {key: value for key, value in payload.items() if key != "spec_hash"}
    encoded = json.dumps(
        body,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def derive_computed(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Derive materiality fields from a valid-shape payload."""

    prior = payload["prior"]
    current = payload["current"]
    thresholds = payload["thresholds"]

    source_changed = any(
        prior[field] != current[field]
        for field in (
            "stac_updated",
            "collection_version",
            "asset_digest",
            "source_spec_hash",
        )
    )
    prior_mean = Decimal(str(prior["statistics"]["mean_ndvi"]))
    current_mean = Decimal(str(current["statistics"]["mean_ndvi"]))
    absolute_change_decimal = abs(current_mean - prior_mean)
    relative_change_decimal = (
        None
        if prior_mean == 0
        else absolute_change_decimal / abs(prior_mean)
    )
    signal_changed = (
        absolute_change_decimal
        > Decimal(str(thresholds["min_absolute_change"]))
        or (
            relative_change_decimal is not None
            and relative_change_decimal
            > Decimal(str(thresholds["min_relative_change"]))
        )
    )
    counts = current["pixel_counts"]
    current_valid_fraction_decimal = (
        Decimal(int(counts["valid"])) / Decimal(int(counts["total"]))
    )
    return {
        "source_changed": source_changed,
        "absolute_change": float(absolute_change_decimal),
        "relative_change": (
            None
            if relative_change_decimal is None
            else float(relative_change_decimal)
        ),
        "signal_changed": signal_changed,
        "current_valid_fraction": float(current_valid_fraction_decimal),
    }


def expected_reasons(payload: Mapping[str, Any]) -> list[str]:
    computed = derive_computed(payload)
    reasons: set[str] = set()
    if computed["current_valid_fraction"] < float(
        payload["thresholds"]["min_valid_fraction"]
    ):
        reasons.add("VALID_FRACTION_BELOW_MINIMUM")
    if not computed["source_changed"]:
        reasons.add("SOURCE_UNCHANGED")
    if not computed["signal_changed"]:
        reasons.add("SIGNAL_BELOW_THRESHOLD")
    return sorted(reasons)


def expected_outcome(payload: Mapping[str, Any]) -> str:
    computed = derive_computed(payload)
    if computed["current_valid_fraction"] < float(
        payload["thresholds"]["min_valid_fraction"]
    ):
        return "HOLD"
    if computed["source_changed"] and computed["signal_changed"]:
        return "MATERIAL_CHANGE_CANDIDATE"
    return "NO_MATERIAL_CHANGE"


def _float_equal(actual: object, expected: float | None) -> bool:
    if expected is None:
        return actual is None
    return isinstance(actual, (int, float)) and math.isclose(
        float(actual), expected, rel_tol=0.0, abs_tol=1e-12
    )


def _semantic_findings(payload: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    support = payload["support"]
    support_id = support["id"]
    if support["kind"] == "county" and len(support_id) != 5:
        findings.append(Finding("COUNTY_ID_INVALID", "/support/id"))
    if support["kind"] == "huc12" and len(support_id) != 12:
        findings.append(Finding("HUC12_ID_INVALID", "/support/id"))

    for name in ("prior", "current"):
        snapshot = payload[name]
        counts = snapshot["pixel_counts"]
        if sum(int(counts[key]) for key in COUNT_KEYS) != int(counts["total"]):
            findings.append(
                Finding("PIXEL_COUNT_CLOSURE_INVALID", f"/{name}/pixel_counts")
            )
        stats = snapshot["statistics"]
        if float(stats["median_ndvi"]) > float(stats["p95_ndvi"]):
            findings.append(
                Finding("SUMMARY_STAT_ORDER_INVALID", f"/{name}/statistics")
            )
        if _parse_time(snapshot["window_start"]) >= _parse_time(snapshot["window_end"]):
            findings.append(
                Finding("WINDOW_ORDER_INVALID", f"/{name}")
            )

    derived = derive_computed(payload)
    computed = payload["computed"]
    for field in ("source_changed", "signal_changed"):
        if computed[field] is not derived[field]:
            findings.append(
                Finding("COMPUTED_FIELD_MISMATCH", f"/computed/{field}")
            )
    for field in ("absolute_change", "relative_change", "current_valid_fraction"):
        if not _float_equal(computed[field], derived[field]):
            findings.append(
                Finding("COMPUTED_FIELD_MISMATCH", f"/computed/{field}")
            )

    reasons = expected_reasons(payload)
    decision = payload["decision"]
    if decision["reasons"] != reasons:
        findings.append(Finding("DECISION_REASONS_MISMATCH", "/decision/reasons"))
    if decision["outcome"] != expected_outcome(payload):
        findings.append(Finding("DECISION_OUTCOME_MISMATCH", "/decision/outcome"))

    if payload["spec_hash"] != canonical_spec_hash(payload):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    return findings


def validate_payload(payload: Mapping[str, Any]) -> ValidationResult:
    """Validate a parsed zonal materiality assessment."""

    findings = _schema_findings(payload)
    if not findings:
        findings.extend(_semantic_findings(payload))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_file(path: Path) -> ValidationResult:
    payload, findings = _load_payload(path)
    if payload is None:
        return ValidationResult(tuple(sorted(findings)))
    return validate_payload(payload)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a fixture-only HLS NDVI zonal materiality assessment."
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
        "scope": "fixture-only-hls-ndvi-zonal-materiality",
        "authority": {
            "source_access": False,
            "raster_processing": False,
            "alerting": False,
            "promotion": False,
            "release": False,
            "publication": False,
        },
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
