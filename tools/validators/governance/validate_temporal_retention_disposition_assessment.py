#!/usr/bin/env python3
"""Validate fixture-only temporal retention disposition assessments."""

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

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash  # noqa: E402

SCHEMA = (
    ROOT
    / "schemas/contracts/v1/governance/temporal_retention_disposition_assessment.schema.json"
)
FIXTURES = (
    ROOT
    / "fixtures/contracts/v1/governance/temporal_retention_disposition_assessment/cases.json"
)
PREFIX = "kfm:temporal-retention:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
EXPECTED_LIMITATIONS = [
    "fixture_only",
    "no_disposition_execution",
    "no_evidence_or_history_deletion",
    "no_policy_or_erasure_authority",
    "no_release_or_publication_authority",
]


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("RETENTION_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("RETENTION_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("RETENTION_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("RETENTION_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("RETENTION_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("RETENTION_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("RETENTION_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"assessment_id", "spec_hash"}
    }
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def _decision(
    outcome: str, recommendation: str, *reason_codes: str
) -> dict[str, Any]:
    return {
        "outcome": outcome,
        "recommendation": recommendation,
        "reason_codes": sorted(reason_codes),
        "review_required": True,
        "execution_authorized": False,
    }


def _coherent_retain(value: Mapping[str, Any]) -> bool:
    subject = value["subject"]
    controls = value["retention_controls"]
    return (
        subject["resulting_record_count"] == subject["input_record_count"]
        and subject["history_preserved"] is True
        and subject["reversible"] is True
        and controls["archive_ref"] is None
        and controls["disposition_receipt_ref"] is None
        and controls["tombstone_ref"] is None
        and controls["proof_preservation"] == "FULL"
    )


def _coherent_archive(value: Mapping[str, Any]) -> bool:
    subject = value["subject"]
    controls = value["retention_controls"]
    dependencies = value["dependencies"]
    return (
        subject["effective_at"] is not None
        and subject["resulting_record_count"] == subject["input_record_count"]
        and subject["history_preserved"] is True
        and subject["reversible"] is True
        and controls["archive_ref"] is not None
        and controls["disposition_receipt_ref"] is not None
        and controls["tombstone_ref"] is None
        and controls["proof_preservation"] == "FULL"
        and dependencies["rollback_target_ref"] is not None
    )


def _coherent_compact(value: Mapping[str, Any]) -> bool:
    subject = value["subject"]
    controls = value["retention_controls"]
    dependencies = value["dependencies"]
    return (
        subject["effective_at"] is not None
        and 0 < subject["resulting_record_count"] < subject["input_record_count"]
        and subject["history_preserved"] is True
        and subject["reversible"] is True
        and controls["archive_ref"] is not None
        and controls["disposition_receipt_ref"] is not None
        and controls["tombstone_ref"] is not None
        and controls["proof_preservation"] in {"FULL", "DIGEST_ONLY"}
        and dependencies["rollback_target_ref"] is not None
    )


def _coherent_erase(value: Mapping[str, Any]) -> bool:
    subject = value["subject"]
    controls = value["retention_controls"]
    dependencies = value["dependencies"]
    return (
        subject["effective_at"] is not None
        and subject["resulting_record_count"] == 0
        and subject["history_preserved"] is False
        and subject["reversible"] is False
        and controls["archive_ref"] is None
        and controls["disposition_receipt_ref"] is None
        and controls["tombstone_ref"] is not None
        and controls["proof_preservation"] == "DIGEST_ONLY"
        and dependencies["rollback_target_ref"] is None
    )


def recompute_decision(value: Mapping[str, Any]) -> dict[str, Any]:
    if value["assessment_state"] == "ERROR":
        return _decision("ERROR", "VALIDATOR_ERROR", "VALIDATOR_ERROR")

    subject = value["subject"]
    dependencies = value["dependencies"]
    controls = value["retention_controls"]
    disposition = subject["disposition"]

    if controls["policy_state"] == "DENIED" or controls["legal_basis_state"] == "DENIED":
        return _decision("DENY", "REJECT", "POLICY_OR_LEGAL_BASIS_DENIED")

    coherent = {
        "RETAIN": _coherent_retain,
        "ARCHIVE": _coherent_archive,
        "COMPACT": _coherent_compact,
        "ERASE": _coherent_erase,
    }[disposition](value)
    if not coherent:
        code = {
            "RETAIN": "RETENTION_STATE_INCOHERENT",
            "ARCHIVE": "ARCHIVE_CONTROLS_INCOMPLETE",
            "COMPACT": "COMPACTION_CONTROLS_INCOMPLETE",
            "ERASE": "ERASURE_STATE_INCOHERENT",
        }[disposition]
        return _decision("DENY", "REJECT", code)

    if disposition == "ERASE":
        if dependencies["release_state"] == "ACTIVE":
            return _decision("DENY", "REJECT", "ACTIVE_RELEASE_BLOCKS_ERASURE")
        if controls["erasure_obligation"] == "NONE":
            return _decision("DENY", "REJECT", "ERASURE_WITHOUT_OBLIGATION")
        if controls["erasure_obligation"] == "UNRESOLVED":
            return _decision(
                "ABSTAIN", "HOLD_FOR_POLICY", "ERASURE_OBLIGATION_UNRESOLVED"
            )
        if (
            controls["policy_state"] != "VERIFIED"
            or controls["legal_basis_state"] != "VERIFIED"
            or dependencies["release_state"] == "UNKNOWN"
            or dependencies["evidence_state"] == "UNRESOLVED"
            or dependencies["correction_state"] == "UNRESOLVED"
        ):
            return _decision(
                "ABSTAIN", "HOLD_FOR_POLICY", "DEPENDENCY_CLOSURE_UNRESOLVED"
            )
        return _decision(
            "ABSTAIN", "HOLD_FOR_POLICY", "ERASURE_REQUIRES_SEPARATE_AUTHORITY"
        )

    if controls["erasure_obligation"] != "NONE" or controls["minimization_required"]:
        return _decision(
            "ABSTAIN", "HOLD_FOR_POLICY", "CONFLICTING_ERASURE_OBLIGATION"
        )
    if controls["policy_state"] != "VERIFIED" or controls["legal_basis_state"] == "UNKNOWN":
        return _decision(
            "ABSTAIN", "HOLD_FOR_POLICY", "RETENTION_POLICY_UNRESOLVED"
        )
    if (
        dependencies["evidence_state"] == "UNRESOLVED"
        or dependencies["correction_state"] == "UNRESOLVED"
        or dependencies["release_state"] == "UNKNOWN"
    ):
        return _decision(
            "ABSTAIN", "HOLD_FOR_POLICY", "DEPENDENCY_CLOSURE_UNRESOLVED"
        )
    if disposition == "COMPACT" and dependencies["release_state"] == "ACTIVE":
        return _decision(
            "ABSTAIN", "HOLD_FOR_POLICY", "ACTIVE_RELEASE_REQUIRES_HANDOFF"
        )

    code = {
        "RETAIN": "RETENTION_CONTROLS_COHERENT",
        "ARCHIVE": "ARCHIVE_CONTROLS_COHERENT",
        "COMPACT": "COMPACTION_CONTROLS_COHERENT",
    }[disposition]
    return _decision("PASS", "READY_FOR_REVIEW", code)


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema, format_checker=FormatChecker()
                ).iter_errors(value),
                MAX_FINDINGS + 1,
            )
        )
    except Exception:
        return (Finding("RETENTION_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("RETENTION_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("RETENTION_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _state_refs_match(state: str, refs: Sequence[str]) -> bool:
    if state == "NONE":
        return not refs
    if state == "RESOLVED":
        return bool(refs)
    return True


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("RETENTION_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("RETENTION_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            findings.add(Finding("RETENTION_ID_MISMATCH", "/assessment_id"))

    if value["limitations"] != EXPECTED_LIMITATIONS:
        findings.add(Finding("RETENTION_LIMITATIONS_INVALID", "/limitations"))

    subject = value["subject"]
    proposed = _time(subject["proposed_at"])
    effective = _time(subject["effective_at"])
    if proposed is not None and effective is not None and effective < proposed:
        findings.add(Finding("RETENTION_TIME_ORDER_INVALID", "/subject/effective_at"))

    dependencies = value["dependencies"]
    for state_key, refs_key in (
        ("evidence_state", "evidence_refs"),
        ("correction_state", "correction_refs"),
    ):
        if not _state_refs_match(dependencies[state_key], dependencies[refs_key]):
            findings.add(
                Finding("RETENTION_REFERENCE_STATE_MISMATCH", f"/dependencies/{refs_key}")
            )
    release_state = dependencies["release_state"]
    if (release_state == "NONE") != (not dependencies["release_refs"]):
        findings.add(
            Finding("RETENTION_REFERENCE_STATE_MISMATCH", "/dependencies/release_refs")
        )

    controls = value["retention_controls"]
    policy_ref_required = controls["policy_state"] in {"VERIFIED", "DENIED"}
    if policy_ref_required != (controls["policy_ref"] is not None):
        findings.add(
            Finding("RETENTION_REFERENCE_STATE_MISMATCH", "/retention_controls/policy_ref")
        )
    legal_ref_required = controls["legal_basis_state"] in {"VERIFIED", "DENIED"}
    if legal_ref_required != (controls["legal_basis_ref"] is not None):
        findings.add(
            Finding(
                "RETENTION_REFERENCE_STATE_MISMATCH",
                "/retention_controls/legal_basis_ref",
            )
        )

    if value["decision"] != recompute_decision(value):
        findings.add(Finding("RETENTION_DECISION_MISMATCH", "/decision"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    decision = recompute_decision(value)
    findings: tuple[Finding, ...] = ()
    if decision["outcome"] in {"ABSTAIN", "DENY", "ERROR"}:
        findings = tuple(
            Finding(code, "/decision/reason_codes") for code in decision["reason_codes"]
        )
    return Result(decision["outcome"], findings)


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if value is None:
        return Result("ERROR", findings)
    return validate_payload(value)


def validate_fixtures(path: Path = FIXTURES) -> int:
    value, findings = _read(path)
    if value is None:
        print(json.dumps({"outcome": "ERROR", "findings": [item.code for item in findings]}))
        return 2
    cases = value.get("cases")
    if not isinstance(cases, list) or not cases:
        print(json.dumps({"outcome": "ERROR", "findings": ["RETENTION_CASES_INVALID"]}))
        return 2
    failures: list[dict[str, Any]] = []
    for case in cases:
        if not isinstance(case, dict) or not isinstance(case.get("candidate"), dict):
            failures.append({"case_id": "UNKNOWN", "error": "case shape invalid"})
            continue
        result = validate_payload(case["candidate"])
        actual_codes = [item.code for item in result.findings]
        if (
            result.outcome != case.get("expected_outcome")
            or actual_codes != case.get("expected_findings")
        ):
            failures.append(
                {
                    "case_id": case.get("case_id"),
                    "expected_outcome": case.get("expected_outcome"),
                    "actual_outcome": result.outcome,
                    "expected_findings": case.get("expected_findings"),
                    "actual_findings": actual_codes,
                }
            )
    if failures:
        print(json.dumps({"outcome": "ERROR", "failures": failures}, indent=2))
        return 2
    print(
        json.dumps(
            {
                "outcome": "PASS",
                "case_count": len(cases),
                "profile": "kfm.governance.temporal-retention-disposition.fixture.v1",
            },
            sort_keys=True,
        )
    )
    return 0


def _result_json(result: Result) -> dict[str, Any]:
    return {
        "outcome": result.outcome,
        "findings": [
            {"code": finding.code, "path": finding.path} for finding in result.findings
        ],
        "boundary": [
            "fixture-only assessment",
            "no retention policy or erasure authority",
            "no mutation, deletion, release, or publication authority",
        ],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only temporal retention disposition assessments."
    )
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return validate_fixtures()
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    result = validate_file(args.path)
    print(json.dumps(_result_json(result), indent=2, sort_keys=True))
    return {"PASS": 0, "ABSTAIN": 3, "DENY": 4, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
