#!/usr/bin/env python3
"""Validate fixture-only AirNow-to-AQS authority reconciliation candidates."""

from __future__ import annotations

import argparse
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
CANDIDATE_SCHEMA = REPO_ROOT / "schemas/contracts/v1/domains/atmosphere/airnow_aqs_reconciliation_candidate.schema.json"
PROFILE_ID = "kfm.airnow-aqs-reconciliation.synthetic.v1"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    report: dict[str, Any] | None

    @property
    def ok(self) -> bool:
        return not self.findings


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _canonical_blob(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode("utf-8")


def _sha256(value: object) -> str:
    return "sha256:" + hashlib.sha256(_canonical_blob(value)).hexdigest()


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(CANDIDATE_SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        errors = list(islice(_schema_validator().iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    ordered = sorted(errors, key=lambda error: (_pointer(error.absolute_path), str(error.validator)))[:MAX_SCHEMA_FINDINGS]
    findings = [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in ordered]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _monitor_key(record: Mapping[str, Any]) -> str:
    identity = record["identity"]
    return "-".join([
        identity["state_code"], identity["county_code"], identity["site_number"], identity["parameter_code"], str(identity["poc"])
    ])


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    airnow = candidate["airnow"]
    aqs = candidate["aqs"]

    if airnow["measurement_kind"] == "aqi_nowcast":
        if airnow["unit"] != "AQI" or airnow["nowcast"] is not True:
            findings.append(Finding("AIRNOW_NOWCAST_SHAPE_INVALID", "/airnow"))
    else:
        if airnow["unit"] == "AQI" or airnow["nowcast"] is not False:
            findings.append(Finding("AIRNOW_CONCENTRATION_SHAPE_INVALID", "/airnow"))

    if aqs is not None:
        if _monitor_key(airnow) != _monitor_key(aqs):
            findings.append(Finding("MONITOR_KEY_MISMATCH", "/aqs/identity"))
        if airnow["observed_at"] != aqs["observed_at"]:
            findings.append(Finding("OBSERVATION_TIME_MISMATCH", "/aqs/observed_at"))
        if airnow["measurement_kind"] == "concentration" and airnow["unit"] != aqs["unit"]:
            findings.append(Finding("CONCENTRATION_UNIT_MISMATCH", "/aqs/unit"))

    governance = candidate["governance"]
    if (
        governance["review_state"] != "fixture_only"
        or governance["release_state"] != "not_released"
        or governance["promotion_eligible"] is not False
        or governance["public_use_allowed"] is not False
    ):
        findings.append(Finding("GOVERNANCE_STATE_INVALID", "/governance"))
    return findings


def _decision(candidate: Mapping[str, Any]) -> tuple[str, str, bool]:
    airnow = candidate["airnow"]
    aqs = candidate["aqs"]
    requested_use = candidate["requested_use"]

    if airnow["measurement_kind"] == "aqi_nowcast":
        return "ABSTAIN", "AIRNOW_NOWCAST_DERIVED_ONLY", False
    if aqs is None:
        if requested_use == "regulatory_replacement":
            return "DENY", "AQS_AUTHORITATIVE_RECORD_MISSING", False
        return "ABSTAIN", "AIRNOW_PROVISIONAL_CONTEXT_ONLY", False
    if aqs["qa_state"] != "validated":
        return "ABSTAIN", "AQS_VALIDATION_PENDING", False
    if aqs["certification_state"] != "certified":
        return "ABSTAIN", "AQS_CERTIFICATION_PENDING", False
    return "PROPOSED_WORK_RECORD", "AQS_AUTHORITATIVE_REPLACEMENT_AVAILABLE", True


def validate_candidate(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic_findings(candidate))
    if findings:
        return ValidationResult(tuple(sorted(set(findings))), None)

    airnow = candidate["airnow"]
    aqs = candidate["aqs"]
    airnow_hash = _sha256(airnow)
    aqs_hash = _sha256(aqs) if aqs is not None else None
    outcome, reason_code, supersede = _decision(candidate)
    monitor_key = _monitor_key(airnow)
    report = {
        "object_type": "AirnowAqsReconciliationReport",
        "schema_version": "1.0.0",
        "profile_id": PROFILE_ID,
        "reconciliation_id": _sha256({
            "profile_id": PROFILE_ID,
            "evaluation_id": candidate["evaluation_id"],
            "requested_use": candidate["requested_use"],
            "monitor_key": monitor_key,
            "airnow_hash": airnow_hash,
            "aqs_hash": aqs_hash,
        }),
        "evaluation_id": candidate["evaluation_id"],
        "evaluated_at": candidate["evaluated_at"],
        "requested_use": candidate["requested_use"],
        "canonical_monitor_key": monitor_key,
        "source_state": {
            "airnow_record_hash": airnow_hash,
            "airnow_measurement_kind": airnow["measurement_kind"],
            "aqs_record_hash": aqs_hash,
            "aqs_qa_state": aqs["qa_state"] if aqs is not None else None,
            "aqs_certification_state": aqs["certification_state"] if aqs is not None else None,
        },
        "lineage": {
            "preserve_airnow_record": True,
            "superseding_source": "AQS" if supersede else None,
            "supersedes_record_hash": airnow_hash if supersede else None,
        },
        "decision": {"outcome": outcome, "reason_code": reason_code},
        "governance": {
            "steward_review_required": True,
            "promotion_allowed": False,
            "release_allowed": False,
            "publication": False,
        },
    }
    return ValidationResult((), report)


def _load(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, (Finding("INPUT_TOO_LARGE", "/"),)
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object, parse_constant=_reject_nonfinite)
    except UnicodeError:
        return None, (Finding("JSON_NOT_UTF8", "/"),)
    except DuplicateKeyError:
        return None, (Finding("JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("JSON_NONFINITE_NUMBER", "/"),)
    except json.JSONDecodeError:
        return None, (Finding("JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("INPUT_UNREADABLE", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ROOT_NOT_OBJECT", "/"),)
    return value, ()


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _load(path)
    if candidate is None:
        return ValidationResult(findings, None)
    return validate_candidate(candidate)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a fixture-only AirNow-to-AQS reconciliation candidate.")
    parser.add_argument("path", type=Path)
    args = parser.parse_args(argv)
    result = validate_file(args.path)
    output = {
        "ok": result.ok,
        "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        "report": result.report,
        "authority": {
            "source_admission": False,
            "regulatory_certification": False,
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
