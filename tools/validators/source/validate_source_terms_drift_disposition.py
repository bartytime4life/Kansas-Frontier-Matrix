#!/usr/bin/env python3
"""Validate fixture-only source-terms drift dispositions without legal effects."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/source/source_terms_drift_disposition.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/source/source_terms_drift_disposition/cases.json"
MAX_BYTES = 1024 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:source-terms-drift:"

CHANGED_FIELD_ORDER = (
    "TERMS_CONTENT",
    "LICENSE_ID",
    "SCOPE",
    "ATTRIBUTION",
    "REDISTRIBUTION",
    "COMMERCIAL_USE",
    "DERIVATIVE_USE",
    "RETENTION",
    "ACCESS",
    "EXPIRY",
)
POSTURE_FIELDS = {
    "ATTRIBUTION": "attribution",
    "REDISTRIBUTION": "redistribution",
    "COMMERCIAL_USE": "commercial_use",
    "DERIVATIVE_USE": "derivative_use",
    "RETENTION": "retention",
    "ACCESS": "access",
}
REASON_ORDER = (
    "NO_TERMS_CHANGE",
    "TERMS_CHANGE_REQUIRES_REASSESSMENT",
    "RESTRICTIVE_TERMS_CHANGE",
    "TERMS_EVIDENCE_UNRESOLVED",
    "RIGHTS_SCOPE_MISMATCH",
    "TERMS_EXPIRED",
    "DOWNSTREAM_OBLIGATION_UNPROPAGATED",
    "ASSESSMENT_ERROR",
)
RANKS = {
    "attribution": {"NOT_REQUIRED": 0, "REQUIRED": 1, "UNKNOWN": 2},
    "redistribution": {"ALLOWED": 0, "RESTRICTED": 1, "PROHIBITED": 2, "UNKNOWN": 3},
    "commercial_use": {"ALLOWED": 0, "RESTRICTED": 1, "PROHIBITED": 2, "UNKNOWN": 3},
    "derivative_use": {"ALLOWED": 0, "RESTRICTED": 1, "PROHIBITED": 2, "UNKNOWN": 3},
    "retention": {"ALLOWED": 0, "RESTRICTED": 1, "PROHIBITED": 2, "UNKNOWN": 3},
    "access": {"PUBLIC": 0, "KEYED": 1, "AGREEMENT_REQUIRED": 2, "RESTRICTED": 3, "UNKNOWN": 4},
}


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
    state: str | None
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


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("TERMS_DRIFT_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("TERMS_DRIFT_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("TERMS_DRIFT_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("TERMS_DRIFT_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("TERMS_DRIFT_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("TERMS_DRIFT_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("TERMS_DRIFT_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("TERMS_DRIFT_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def _dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def snapshot_hash(snapshot: Mapping[str, Any]) -> str:
    subject = {
        key: item
        for key, item in snapshot.items()
        if key not in {"snapshot_ref", "snapshot_hash"}
    }
    return compute_spec_hash(subject)


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"assessment_id", "spec_hash"}
    }
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("TERMS_DRIFT_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("TERMS_DRIFT_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("TERMS_DRIFT_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def changed_fields(prior: Mapping[str, Any], current: Mapping[str, Any]) -> list[str]:
    changed: set[str] = set()
    if prior["terms_content_hash"] != current["terms_content_hash"]:
        changed.add("TERMS_CONTENT")
    if prior["license_id"] != current["license_id"]:
        changed.add("LICENSE_ID")
    if prior["scope_hash"] != current["scope_hash"]:
        changed.add("SCOPE")
    for label, key in POSTURE_FIELDS.items():
        if prior["use_posture"][key] != current["use_posture"][key]:
            changed.add(label)
    if prior["expires_at"] != current["expires_at"]:
        changed.add("EXPIRY")
    return [item for item in CHANGED_FIELD_ORDER if item in changed]


def _expired(current: Mapping[str, Any], assessed_at: datetime) -> bool:
    expires_at = current["expires_at"]
    return expires_at is not None and _dt(expires_at) <= assessed_at


def _became_more_restrictive(
    prior: Mapping[str, Any],
    current: Mapping[str, Any],
) -> bool:
    for key, ranks in RANKS.items():
        if ranks[current["use_posture"][key]] > ranks[prior["use_posture"][key]]:
            return True
    prior_expiry = prior["expires_at"]
    current_expiry = current["expires_at"]
    if current_expiry is not None and (
        prior_expiry is None or _dt(current_expiry) < _dt(prior_expiry)
    ):
        return True
    return False


def expected_classification(value: Mapping[str, Any]) -> str:
    prior = value["prior_snapshot"]
    current = value["current_snapshot"]
    if value["assessment_state"] == "ERROR":
        return "UNRESOLVED"
    if (
        prior["verification_state"] != "VERIFIED"
        or current["verification_state"] != "VERIFIED"
        or prior["scope_hash"] != current["scope_hash"]
    ):
        return "UNRESOLVED"
    if _expired(current, _dt(value["assessed_at"])):
        return "RESTRICTIVE_CHANGE"
    changes = changed_fields(prior, current)
    if not changes:
        return "NO_CHANGE"
    if _became_more_restrictive(prior, current):
        return "RESTRICTIVE_CHANGE"
    return "NON_RESTRICTIVE_CHANGE"


def _expected_action(classification: str, dependency_kind: str) -> str:
    if classification == "NO_CHANGE":
        return "NO_ACTION"
    if classification == "NON_RESTRICTIVE_CHANGE":
        return "REASSESS"
    if classification == "UNRESOLVED":
        return "HOLD"
    if dependency_kind in {"RELEASE", "PUBLIC_ARTIFACT"}:
        return "WITHDRAWAL_REVIEW"
    if dependency_kind == "CACHE":
        return "RECOMPUTE_REVIEW"
    return "HOLD"


def _expected_disposition(
    value: Mapping[str, Any],
    classification: str,
    propagation_missing: bool,
) -> tuple[str, list[str]]:
    if value["assessment_state"] == "ERROR":
        return "ERROR", ["ASSESSMENT_ERROR"]
    if classification == "NO_CHANGE":
        status, reasons = "NO_ACTION", ["NO_TERMS_CHANGE"]
    elif classification == "NON_RESTRICTIVE_CHANGE":
        status, reasons = "REASSESS", ["TERMS_CHANGE_REQUIRES_REASSESSMENT"]
    elif classification == "RESTRICTIVE_CHANGE":
        status, reasons = "HOLD", ["RESTRICTIVE_TERMS_CHANGE"]
        if _expired(value["current_snapshot"], _dt(value["assessed_at"])):
            reasons.append("TERMS_EXPIRED")
    else:
        status, reasons = "HOLD", []
        snapshots = (value["prior_snapshot"], value["current_snapshot"])
        if any(item["verification_state"] != "VERIFIED" for item in snapshots):
            reasons.append("TERMS_EVIDENCE_UNRESOLVED")
        if snapshots[0]["scope_hash"] != snapshots[1]["scope_hash"]:
            reasons.append("RIGHTS_SCOPE_MISMATCH")
    if propagation_missing:
        status = "HOLD"
        reasons.append("DOWNSTREAM_OBLIGATION_UNPROPAGATED")
    ordered = [reason for reason in REASON_ORDER if reason in set(reasons)]
    return status, ordered


def _semantic_findings(value: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    prior = value["prior_snapshot"]
    current = value["current_snapshot"]
    assessed_at = _dt(value["assessed_at"])

    if _dt(prior["captured_at"]) > _dt(current["captured_at"]):
        findings.add(Finding("TERMS_DRIFT_CAPTURE_ORDER_INVALID", "/current_snapshot/captured_at"))
    if _dt(current["captured_at"]) > assessed_at:
        findings.add(Finding("TERMS_DRIFT_ASSESSMENT_BEFORE_CAPTURE", "/assessed_at"))
    for name, snapshot in (("prior_snapshot", prior), ("current_snapshot", current)):
        if _dt(snapshot["effective_from"]) > _dt(snapshot["captured_at"]):
            findings.add(Finding("TERMS_DRIFT_EFFECTIVE_TIME_INVALID", f"/{name}/effective_from"))
        expires_at = snapshot["expires_at"]
        if expires_at is not None and _dt(expires_at) <= _dt(snapshot["effective_from"]):
            findings.add(Finding("TERMS_DRIFT_EXPIRY_INVALID", f"/{name}/expires_at"))
        try:
            expected_snapshot_hash = snapshot_hash(snapshot)
        except CanonicalizationFailure:
            findings.add(Finding("TERMS_DRIFT_SNAPSHOT_CANONICALIZATION_ERROR", f"/{name}"))
        else:
            if snapshot["snapshot_hash"] != expected_snapshot_hash:
                findings.add(Finding("TERMS_DRIFT_SNAPSHOT_HASH_MISMATCH", f"/{name}/snapshot_hash"))
        refs = snapshot["obligation_refs"]
        if refs != sorted(refs):
            findings.add(Finding("TERMS_DRIFT_OBLIGATION_ORDER_INVALID", f"/{name}/obligation_refs"))

    expected_changed = changed_fields(prior, current)
    if value["drift"]["changed_fields"] != expected_changed:
        findings.add(Finding("TERMS_DRIFT_CHANGED_FIELDS_MISMATCH", "/drift/changed_fields"))
    expected_scope_match = prior["scope_hash"] == current["scope_hash"]
    if value["drift"]["scope_match"] is not expected_scope_match:
        findings.add(Finding("TERMS_DRIFT_SCOPE_MATCH_MISMATCH", "/drift/scope_match"))
    expected_evidence = (
        value["assessment_state"] == "COMPLETE"
        and prior["verification_state"] == "VERIFIED"
        and current["verification_state"] == "VERIFIED"
    )
    if value["drift"]["evidence_complete"] is not expected_evidence:
        findings.add(Finding("TERMS_DRIFT_EVIDENCE_COMPLETENESS_MISMATCH", "/drift/evidence_complete"))

    classification = expected_classification(value)
    if value["drift"]["classification"] != classification:
        findings.add(Finding("TERMS_DRIFT_CLASSIFICATION_MISMATCH", "/drift/classification"))

    dependencies = value["downstream_dependencies"]
    refs = [item["dependency_ref"] for item in dependencies]
    if refs != sorted(refs) or len(refs) != len(set(refs)):
        findings.add(Finding("TERMS_DRIFT_DEPENDENCY_ORDER_INVALID", "/downstream_dependencies"))
    propagation_missing = False
    for index, dependency in enumerate(dependencies):
        if not dependency["obligation_propagated"]:
            propagation_missing = True
            findings.add(
                Finding(
                    "TERMS_DRIFT_DOWNSTREAM_OBLIGATION_UNPROPAGATED",
                    f"/downstream_dependencies/{index}/obligation_propagated",
                )
            )
        expected_action = _expected_action(classification, dependency["dependency_kind"])
        if dependency["proposed_action"] != expected_action:
            findings.add(
                Finding(
                    "TERMS_DRIFT_DOWNSTREAM_ACTION_MISMATCH",
                    f"/downstream_dependencies/{index}/proposed_action",
                )
            )

    expected_status, expected_reasons = _expected_disposition(
        value, classification, propagation_missing
    )
    if value["disposition"]["status"] != expected_status:
        findings.add(Finding("TERMS_DRIFT_DISPOSITION_MISMATCH", "/disposition/status"))
    if value["disposition"]["reason_codes"] != expected_reasons:
        findings.add(Finding("TERMS_DRIFT_REASON_CODES_MISMATCH", "/disposition/reason_codes"))
    return findings


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", None, schema_findings)
    try:
        findings = _semantic_findings(value)
        expected_hash, expected_id = canonical_identity(value)
    except (CanonicalizationFailure, ValueError, TypeError, OverflowError):
        return Result(
            "DENY",
            None,
            (Finding("TERMS_DRIFT_CANONICALIZATION_OR_TIME_ERROR", "/"),),
        )
    if value["spec_hash"] != expected_hash:
        findings.add(Finding("TERMS_DRIFT_SPEC_HASH_MISMATCH", "/spec_hash"))
    if value["assessment_id"] != expected_id:
        findings.add(Finding("TERMS_DRIFT_ID_MISMATCH", "/assessment_id"))
    if findings:
        return Result("DENY", None, tuple(sorted(findings)))
    return Result("PASS", value["disposition"]["status"], ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if value is None:
        return Result("ERROR", None, findings)
    return validate_payload(value)


def _set_pointer(document: dict[str, Any], pointer: str, replacement: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
    ]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    last = parts[-1]
    if isinstance(cursor, list):
        cursor[int(last)] = replacement
    else:
        cursor[last] = replacement


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    for name in ("prior_snapshot", "current_snapshot"):
        document[name]["snapshot_hash"] = snapshot_hash(document[name])
    document["spec_hash"], document["assessment_id"] = canonical_identity(document)
    for override, pointer in (
        ("prior_snapshot_hash_override", "/prior_snapshot/snapshot_hash"),
        ("current_snapshot_hash_override", "/current_snapshot/snapshot_hash"),
        ("spec_hash_override", "/spec_hash"),
        ("assessment_id_override", "/assessment_id"),
    ):
        if override in case:
            _set_pointer(document, pointer, case[override])
    return document


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    if not isinstance(value, dict):
        raise ValueError("fixture root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if (
            result.outcome != case["expected_outcome"]
            or result.state != case["expected_state"]
            or actual != case["expected_findings"]
        ):
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_state": case["expected_state"],
                    "actual_state": result.state,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def _serialize(path: Path, result: Result) -> str:
    return json.dumps(
        {
            "authority": {
                "legal_determination": False,
                "source_activation": False,
                "lifecycle_write": False,
                "hold_execution": False,
                "recomputation": False,
                "withdrawal": False,
                "release": False,
                "publication": False,
            },
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix(),
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "outcome": result.outcome,
            "state": result.state,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.input is None:
        raise SystemExit("input is required unless --fixtures is used")
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
