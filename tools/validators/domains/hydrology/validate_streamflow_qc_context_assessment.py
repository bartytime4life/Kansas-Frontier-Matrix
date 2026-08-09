#!/usr/bin/env python3
"""Validate fixture-only streamflow QC context assessments."""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/domains/hydrology/streamflow_qc_context_assessment.schema.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:streamflow-qc-context:"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


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
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


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
            return None, (Finding("STREAMFLOW_QC_CONTEXT_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("STREAMFLOW_QC_CONTEXT_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("STREAMFLOW_QC_CONTEXT_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("STREAMFLOW_QC_CONTEXT_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("STREAMFLOW_QC_CONTEXT_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("STREAMFLOW_QC_CONTEXT_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("STREAMFLOW_QC_CONTEXT_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("STREAMFLOW_QC_CONTEXT_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"assessment_id", "spec_hash"}}
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("STREAMFLOW_QC_CONTEXT_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [Finding("STREAMFLOW_QC_CONTEXT_SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:MAX_SCHEMA_FINDINGS]]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("STREAMFLOW_QC_CONTEXT_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def expected_assessment(value: Mapping[str, Any]) -> dict[str, Any]:
    subject = value["subject"]
    regional = value["regional_context"]
    integrity = value["integrity_context"]
    current = value["assessment"]
    if current["outcome"] == "ERROR" and subject["flow_state"] == "UNKNOWN" and regional["corroboration"] == "INSUFFICIENT" and regional["drought_context"] == "UNKNOWN" and all(item == "UNKNOWN" for item in integrity.values()):
        return {"outcome": "ERROR", "priority": "NONE", "reason_codes": ["ASSESSMENT_ERROR"]}
    if subject["flow_state"] == "UNKNOWN" or regional["corroboration"] == "INSUFFICIENT" and subject["flow_state"] != "NOT_LOW" or regional["drought_context"] == "UNKNOWN" and subject["flow_state"] != "NOT_LOW" or "UNKNOWN" in integrity.values():
        return {"outcome": "HOLD", "priority": "NONE", "reason_codes": ["CONTEXT_INSUFFICIENT"]}
    if subject["flow_state"] == "NOT_LOW" and all((integrity["ingest_state"] == "CLEAN", integrity["unit_state"] == "COMPATIBLE", integrity["cadence_state"] == "ON_TIME")):
        return {"outcome": "NO_QC_ESCALATION", "priority": "ROUTINE", "reason_codes": ["NO_LOW_FLOW_SIGNAL"]}
    integrity_concern = integrity["ingest_state"] != "CLEAN" or integrity["unit_state"] != "COMPATIBLE" or integrity["cadence_state"] != "ON_TIME"
    if subject["flow_state"] == "LOW_PERCENTILE" and integrity_concern:
        return {"outcome": "LOCAL_SIGNAL_REVIEW", "priority": "HIGH", "reason_codes": ["INTEGRITY_CONCERN", "LOW_FLOW_SIGNAL"]}
    if subject["flow_state"] == "LOW_PERCENTILE" and regional["corroboration"] == "DOES_NOT_CORROBORATE":
        return {"outcome": "LOCAL_SIGNAL_REVIEW", "priority": "ELEVATED", "reason_codes": ["ADJACENT_GAUGES_DO_NOT_CORROBORATE", "LOW_FLOW_SIGNAL"]}
    if subject["flow_state"] == "LOW_PERCENTILE" and regional["corroboration"] == "CORROBORATES_LOW_FLOW" and regional["drought_context"] == "SUPPORTS_LOW_FLOW":
        return {"outcome": "REGIONAL_LOW_FLOW_CONTEXT", "priority": "ROUTINE", "reason_codes": ["ADJACENT_GAUGES_CORROBORATE", "DROUGHT_CONTEXT_SUPPORTS", "LOW_FLOW_SIGNAL"]}
    return {"outcome": "HOLD", "priority": "NONE", "reason_codes": ["CONTEXT_INSUFFICIENT"]}


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    out: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        out.add(Finding("STREAMFLOW_QC_CONTEXT_CANONICALIZATION_ERROR", "/"))
    else:
        if value.get("spec_hash") != expected_hash:
            out.add(Finding("STREAMFLOW_QC_CONTEXT_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value.get("assessment_id") != expected_id:
            out.add(Finding("STREAMFLOW_QC_CONTEXT_ID_MISMATCH", "/assessment_id"))

    subject = value["subject"]
    regional = value["regional_context"]
    if subject["observation_source_ref"] == subject["percentile_context_ref"]:
        out.add(Finding("STREAMFLOW_QC_CONTEXT_SOURCE_ROLE_COLLAPSE", "/subject/percentile_context_ref"))
    observed = _parse_time(subject["observed_at"])
    retrieved = _parse_time(subject["retrieved_at"])
    if observed is None or retrieved is None or retrieved < observed:
        out.add(Finding("STREAMFLOW_QC_CONTEXT_TIME_ORDER_INVALID", "/subject/retrieved_at"))
    if regional["corroboration"] == "CORROBORATES_LOW_FLOW":
        if regional["adjacent_gauge_count"] < 2:
            out.add(Finding("STREAMFLOW_QC_CONTEXT_ADJACENT_GAUGES_INSUFFICIENT", "/regional_context/adjacent_gauge_count"))
        if len(regional["context_evidence_refs"]) < 2:
            out.add(Finding("STREAMFLOW_QC_CONTEXT_REGIONAL_EVIDENCE_INSUFFICIENT", "/regional_context/context_evidence_refs"))
    if set(subject["evidence_refs"]) & set(regional["context_evidence_refs"]):
        out.add(Finding("STREAMFLOW_QC_CONTEXT_EVIDENCE_ROLE_COLLAPSE", "/regional_context/context_evidence_refs"))
    if value["assessment"] != expected_assessment(value):
        out.add(Finding("STREAMFLOW_QC_CONTEXT_ASSESSMENT_MISMATCH", "/assessment"))
    return tuple(sorted(out))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema = _schema_findings(value)
    if schema:
        return Result("DENY", schema)
    semantic = _semantic_findings(value)
    if semantic:
        return Result("DENY", semantic)
    packet_outcome = value["assessment"]["outcome"]
    if packet_outcome == "HOLD":
        return Result("ABSTAIN", (Finding("STREAMFLOW_QC_CONTEXT_HELD", "/assessment/outcome"),))
    if packet_outcome == "ERROR":
        return Result("ERROR", (Finding("STREAMFLOW_QC_CONTEXT_UPSTREAM_ERROR", "/assessment/outcome"),))
    return Result("PASS", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    return Result("ERROR", findings) if value is None else validate_payload(value)


def _serialize(path: Path, result: Result) -> str:
    return json.dumps({
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "file": path.as_posix(),
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
        "non_effects": ["no_network", "no_percentile_computation", "no_sensor_invalidation", "no_event_declaration", "no_detector_mutation", "no_policy_review_release_or_publication"],
        "outcome": result.outcome,
    }, sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args(argv)
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
