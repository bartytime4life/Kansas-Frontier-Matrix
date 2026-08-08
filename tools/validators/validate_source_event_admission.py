#!/usr/bin/env python3
"""Validate fixture-only SourceEvent prefilter and run-receipt candidates.

This validator extends the existing SourceEventEnvelopeCandidate profile with a
bounded deterministic prefilter output and a fixture-only signed-shape
EventRunReceipt candidate.

A passing result proves only local schema, deterministic identity, cross-file
reference, finite-disposition, and fixture-attestation checks. It does not
authenticate a producer, verify a production signature, resolve evidence,
evaluate policy, activate a source, write RAW or another lifecycle lane,
approve review, promote, release, deploy, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import os
import stat
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages" / "hashing" / "src"
for path in (REPO_ROOT, PACKAGE_SRC):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA_ROOT = REPO_ROOT / "schemas" / "contracts" / "v1" / "source"
PREFILTER_SCHEMA_PATH = SCHEMA_ROOT / "source_event_prefilter_output.schema.json"
RECEIPT_SCHEMA_PATH = SCHEMA_ROOT / "source_event_run_receipt.schema.json"
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures"
    / "contracts"
    / "v1"
    / "source"
    / "source_event_admission"
)
EVENT_FIXTURE_ROOT = FIXTURE_ROOT.parent / "source_event_envelope" / "valid"
MANIFEST_PATH = FIXTURE_ROOT / "fixture_manifest.json"

MAX_FILE_BYTES = 1_000_000
MAX_JSON_DEPTH = 64
MAX_SCHEMA_FINDINGS = 100
SCOPE = "source.source_event_admission_candidates"
NON_EFFECTS = (
    "no_network_or_queue_access",
    "no_hidden_reasoning_capture",
    "no_production_signature_verification",
    "no_source_activation",
    "no_raw_or_lifecycle_write",
    "no_evidence_or_proof_creation",
    "no_policy_or_review_authority",
    "no_promotion_release_deployment_or_publication",
)

PREFILTER_DESTINATION = {
    "MATERIAL_CHANGE": "RAW_REVIEW",
    "NON_MATERIAL_CHANGE": "NO_ACTION",
    "REVIEW_REQUIRED": "WORK_REVIEW",
    "RIGHTS_UNRESOLVED": "QUARANTINE_REVIEW",
    "SENSITIVITY_UNRESOLVED": "QUARANTINE_REVIEW",
    "DUPLICATE_REPLAY": "NO_ACTION",
}
DECISION_TARGET = {
    "ALLOW": "RAW",
    "HOLD": "WORK",
    "QUARANTINE": "QUARANTINE",
    "REJECT": "NONE",
    "NO_ACTION": "NONE",
}
DECISION_POLICY = {
    "ALLOW": "ALLOW",
    "HOLD": "HOLD",
    "QUARANTINE": "HOLD",
    "REJECT": "DENY",
    "NO_ACTION": "NOT_EVALUATED",
}
DECISION_REVIEW_REQUIRED = {
    "ALLOW": True,
    "HOLD": True,
    "QUARANTINE": True,
    "REJECT": True,
    "NO_ACTION": False,
}
ERROR_CODES = {
    "READ_ERROR",
    "UNSAFE_FILE",
    "FILE_TOO_LARGE",
    "DUPLICATE_KEY",
    "NONFINITE_NUMBER",
    "INVALID_JSON",
    "JSON_COMPLEXITY_LIMIT",
    "ROOT_TYPE",
    "SCHEMA_UNAVAILABLE",
    "SCHEMA_EVALUATION_LIMIT",
    "UNKNOWN_OBJECT_TYPE",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard or overflowing number."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    object_id: str | None = None
    spec_hash: str | None = None


def _object_no_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite_number(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _json_depth_exceeded(value: str) -> bool:
    depth = 0
    in_string = False
    escaped = False
    for character in value:
        if in_string:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_string = False
            continue
        if character == '"':
            in_string = True
        elif character in "[{":
            depth += 1
            if depth > MAX_JSON_DEPTH:
                return True
        elif character in "]}":
            depth -= 1
    return False


def _has_symlink_component(path: Path) -> bool:
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current /= part
        if current.is_symlink():
            return True
    return False


def _read_bounded_regular_file(path: Path) -> tuple[str | None, list[Finding]]:
    if _has_symlink_component(path):
        return None, [Finding("UNSAFE_FILE", "/")]

    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    descriptor: int | None = None
    try:
        descriptor = os.open(path, flags)
        file_stat = os.fstat(descriptor)
        if not stat.S_ISREG(file_stat.st_mode):
            return None, [Finding("UNSAFE_FILE", "/")]
        if file_stat.st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]

        chunks: list[bytes] = []
        remaining = MAX_FILE_BYTES + 1
        while remaining:
            block = os.read(descriptor, min(64 * 1024, remaining))
            if not block:
                break
            chunks.append(block)
            remaining -= len(block)
        encoded = b"".join(chunks)
        if len(encoded) > MAX_FILE_BYTES:
            return None, [Finding("FILE_LOO_LARGE", "/")]
        return encoded.decode("utf-8"), []
    except (OSError, UnicodeError):
        return None, [Finding("READ_ERROR", "/")]
    finally:
        if descriptor is not None:
            os.close(descriptor)


def _load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    text, findings = _read_bounded_regular_file(path)
    if text is None:
        return None, findings
    if _json_depth_exceeded(text):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]

    try:
        value = json.loads(
            text,
            object_pairs_hook=_object_no_duplicates,
            parse_constant=_reject_nonfinite_number,
            parse_float=_parse_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("INVALID_JSON", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]

    if not isinstance(value, dict):
        return None, [Finding("ROOT_TYPE", "/")]
    return value, []


def _schema_validator(path: Path) -> Draft202012Validator:
    schema = json.loads(path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _json_pointer(parts: Sequence[object]) -> str:
    if not parts:
        return "/"
    escaped = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(escaped)


def _schema_findings(
    validator: Draft202012Validator,
    candidate: Mapping[str, object],
) -> list[Finding]:
    try:
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (RecursionError, ValueError):
        return [Finding("SCHEMA_EVALUATION_LIMIT", "/")]

    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(
        errors[:MAX_SCHEMA_FINDINGS],
        key=lambda error: (
            _json_pointer(tuple(error.absolute_path)),
            str(error.validator or "schema"),
        ),
    )
    findings = [
        Finding("SCHEMA_INVALID", _json_pointer(tuple(error.absolute_path)))
        for error in errors
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _string_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str)]


def _parse_aware_datetime(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed


def _canonical_order_findings(
    candidate: Mapping[str, object],
    fields: Sequence[tuple[str, object]],
) -> set[Finding]:
    findings: set[Finding] = set()
    for path, value in fields:
        strings = _string_list(value)
        if strings != sorted(strings):
            findings.add(Finding("CANONICAL_ORDER_INVALID", path))
    return findings


def _prefilter_identity_projection(candidate: Mapping[str, object]) -> dict[str, object]:
    return {
        "schema_version": candidate["schema_version"],
        "profile": candidate["profile"],
        "event_ref": candidate["event_ref"],
        "event_payload_spec_hash": candidate["event_payload_spec_hash"],
        "evaluator": candidate["evaluator"],
        "classification": candidate["classification"],
        "significance_score": candidate["significance_score"],
        "uncertainty": candidate["uncertainty"],
        "explanation_digest": candidate["explanation_digest"],
        "candidate_destination": candidate["candidate_destination"],
    }


def _prefilter_spec_subject(candidate: Mapping[str, object]) -> dict[str, object]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("spec_hash", None)
    return subject


def _expected_prefilter_id(candidate: Mapping[str, object]) -> str:
    return "kfm:source-prefilter:" + compute_spec_hash(
        _prefilter_identity_projection(candidate)
    )


def _expected_prefilter_spec_hash(candidate: Mapping[str, object]) -> str:
    return compute_spec_hash(_prefilter_spec_subject(candidate))


def _receipt_identity_projection(candidate: Mapping[str, object]) -> dict[str, object]:
    return {
        "schema_version": candidate["schema_version"],
        "profile": candidate["profile"],
        "receipt_type": candidate["receipt_type"],
        "event_ref": candidate["event_ref"],
        "event_payload_spec_hash": candidate["event_payload_spec_hash"],
        "prefilter_ref": candidate["prefilter_ref"],
        "prefilter_spec_hash": candidate["prefilter_spec_hash"],
        "recorded_at": candidate["recorded_at"],
        "decision": candidate["decision"],
        "target_lane": candidate["target_lane"],
        "policy_summary": candidate["policy_summary"],
        "review_required": candidate["review_required"],
        "reason_codes": candidate["reason_codes"],
    }


def _receipt_spec_subject(candidate: Mapping[str, object]) -> dict[str, object]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("spec_hash", None)
    subject.pop("signature", None)
    return subject


def _expected_receipt_id(candidate: Mapping[str, object]) -> str:
    return "kfm:event-run-receipt:" + compute_spec_hash(
        _receipt_identity_projection(candidate)
    )


def _expected_receipt_spec_hash(candidate: Mapping[str, object]) -> str:
    return compute_spec_hash(_receipt_spec_subject(candidate))


def _expected_fixture_signature(candidate: Mapping[str, object]) -> str:
    signature = _mapping(candidate["signature"])
    return compute_spec_hash(
        {
            "profile": signature["profile"],
            "signer_ref": signature["signer_ref"],
            "signed_spec_hash": signature["signed_spec_hash"],
        }
    )


def _event_binding_findings(
    candidate: Mapping[str, object],
    event: Mapping[str, object] | None,
) -> set[Finding]:
    findings: set[Finding] = set()
    if event is None:
        return findings

    if candidate["event_ref"] != event.get("event_id"):
        findings.add(Finding("EVENT_REFERENCE_MISMATCH", "/event_ref"))

    payload = _mapping(event.get("payload"))
    if candidate["event_payload_spec_hash"] != payload.get("payload_spec_hash"):
        findings.add(
            Finding("EVENT_PAYLOAD_SPEC_HASH_MISMATCH", "/event_payload_spec_hash")
        )
    return findings


def _prefilter_semantic_findings(
    candidate: Mapping[str, object],
    event: Mapping[str, object] | None,
) -> set[Finding]:
    findings = _event_binding_findings(candidate, event)
    evaluator = _mapping(candidate["evaluator"])

    try:
        expected_id = _expected_prefilter_id(candidate)
        expected_hash = _expected_prefilter_spec_hash(candidate)
    except (CanonicalizationFailure, KeyError, TypeError):
        findings.add(Finding("CANONICALIZATION_ERROR", "/"))
        return findings

    if candidate["prefilter_id"] != expected_id:
        findings.add(Finding("PREFILTER_ID_MISMATCH", "/prefilter_id"))
    if candidate["spec_hash"] != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    kind = evaluator["kind"]
    if kind == "RULE_SET":
        if evaluator["temperature"] is not None or evaluator["seed"] is not None:
            findings.add(
                Finding("RULE_SET_CONFIGURATION_INVALID", "/evaluator")
            )
    elif kind == "MODEL":
        if evaluator["temperature"] != 0 or not isinstance(evaluator["seed"], int):
            findings.add(
                Finding("MODEL_CONFIGURATION_NOT_DETERMINISTIC", "/evaluator")
            )

    expected_destination = PREFILTER_DESTINATION[candidate["classification"]]
    if candidate["candidate_destination"] != expected_destination:
        findings.add(
            Finding("PREFILTER_DESTINATION_MISMATCH", "/candidate_destination")
        )

    findings.update(
        _canonical_order_findings(
            candidate,
            (("/reason_codes", candidate["reason_codes"]),),
        )
    )

    if event is not None:
        evaluated_at = _parse_aware_datetime(candidate["evaluated_at"])
        received_at = _parse_aware_datetime(event.get("received_at"))
        if (
            evaluated_at is not None
            and received_at is not None
            and evaluated_at < received_at
        ):
            findings.add(Finding("PREFILTER_TIME_ORDER_INVALID", "/evaluated_at"))
    return findings


def _receipt_semantic_findings(
    candidate: Mapping[str, object],
    event: Mapping[str, object] | None,
    prefilter: Mapping[str, object] | None,
) -> set[Finding]:
    findings = _event_binding_findings(candidate, event)
    policy = _mapping(candidate["policy_summary"])
    signature = _mapping(candidate["signature"])

    try:
        expected_id = _expected_receipt_id(candidate)
        expected_hash = _expected_receipt_spec_hash(candidate)
        expected_signature = _expected_fixture_signature(candidate)
    except (CanonicalizationFailure, KeyError, TypeError):
        findings.add(Finding("CANONICALIZATION_ERROR", "/"))
        return findings

    if candidate["receipt_id"] != expected_id:
        findings.add(Finding("RECEIPT_ID_MISMATCH", "/receipt_id"))
    if candidate["spec_hash"] != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if signature["signed_spec_hash"] != candidate["spec_hash"]:
        findings.add(
            Finding("SIGNATURE_SUBJECT_MISMATCH", "/signature/signed_spec_hash")
        )
    if signature["signature_value"] != expected_signature:
        findings.add(
            Finding("FIXTURE_SIGNATURE_MISMATCH", "/signature/signature_value")
        )

    if prefilter is not None:
        if candidate["prefilter_ref"] != prefilter.get("prefilter_id"):
            findings.add(
                Finding("PREFILTER_REFERENCE_MISMATCH", "/prefilter_ref")
            )
        if candidate["prefilter_spec_hash"] != prefilter.get("spec_hash"):
            findings.add(
                Finding("PREFILTER_SPEC_HASH_MISMATCH", "/prefilter_spec_hash")
            )

    decision = candidate["decision"]
    if candidate["target_lane"] != DECISION_TARGET[decision]:
        findings.add(Finding("DECISION_TARGET_MISMATCH", "/target_lane"))
    if policy["outcome"] != DECISION_POLICY[decision]:
        findings.add(Finding("DECISION_POLICY_MISMATCH", "/policy_summary/outcome"))
    if candidate["review_required"] is not DECISION_REVIEW_REQUIRED[decision]:
        findings.add(Finding("DECISION_REVIEW_MISMATCH", "/review_required"))

    rights = policy["rights_state"]
    sensitivity = policy["sensitivity_state"]
    if decision == "ALLOW" and (rights != "KNOWN" or sensitivity != "KNOWN"):
        findings.add(Finding("ALLOW_GOVERNANCE_INCOMPLETE", "/policy_summary"))
    if decision == "QUARANTINE" and rights == "KNOWN" and sensitivity == "KNOWN":
        findings.add(Finding("QUARANTINE_REASON_UNSUPPORTED", "/policy_summary"))
    if decision == "NO_ACTION" and _string_list(policy["policy_refs"]):
        findings.add(Finding("NO_ACTION_POLICY_REFS_INVALID", "/policy_summary/policy_refs"))

    findings.update(
        _canonical_order_findings(
            candidate,
            (
                ("/reason_codes", candidate["reason_codes"]),
                ("/policy_summary/policy_refs", policy["policy_refs"]),
            ),
        )
    )

    if event is not None:
        recorded_at = _parse_aware_datetime(candidate["recorded_at"])
        received_at = _parse_aware_datetime(event.get("received_at"))
        if recorded_at is not None and received_at is not None and recorded_at < received_at:
            findings.add(Finding("RECEIPT_TIME_ORDER_INVALID", "/recorded_at"))

    if prefilter is not None:
        recorded_at = _parse_aware_datetime(candidate["recorded_at"])
        evaluated_at = _parse_aware_datetime(prefilter.get("evaluated_at"))
        if (
            recorded_at is not None
            and evaluated_at is not None
            and recorded_at < evaluated_at
        ):
            findings.add(Finding("RECEIPT_TIME_ORDER_INVALID", "/recorded_at"))

    return findings


def _derive_outcome(
    findings: Sequence[Finding],
    schema_findings: Sequence[Finding],
) -> str:
    if any(item.code in ERROR_CODES for item in findings):
        return "ERROR"
    if schema_findings:
        return "FAIL"
    if findings:
        return "DENY"
    return "PASS"


def validate_file(
    path: Path,
    *,
    event_path: Path | None = None,
    prefilter_path: Path | None = None,
) -> ValidationResult:
    candidate, findings = _load_json_object(path)
    if candidate is None:
        ordered = tuple(sorted(set(findings)))
        return ValidationResult(_derive_outcome(ordered, ()), ordered)

    object_type = candidate.get("object_type")
    try:
        if object_type == "SourceEventPrefilterOutputCandidate":
            schema_validator = _schema_validator(PREFILTER_SCHEMA_PATH)
        elif object_type == "SourceEventRunReceiptCandidate":
            schema_validator = _schema_validator(RECEIPT_SCHEMA_PATH)
        else:
            ordered = (Finding("UNKNOWN_OBJECT_TYPE", "/object_type"),)
            return ValidationResult("ERROR", ordered)
    except (OSError, UnicodeErroq, json.JSONDecodeError, ValueError):
        ordered = (Finding("SCHEMA_UNAVAILABLE", "/"),)
        return ValidationResult("ERROR", ordered)

    schema_findings = _schema_findings(schema_validator, candidate)
    findings.extend(schema_findings)
    if schema_findings:
        ordered = tuple(sorted(set(findings)))
        return ValidationResult(_derive_outcome(ordered, schema_findings), ordered)

    event: Mapping[str, object] | None = None
    if event_path is not None:
        event_value, event_findings = _load_json_object(event_path)
        if event_value is None:
            findings.extend(
                Finding(f"EVENT_{item.code}", item.path) for item in event_findings
            )
        else:
            event = event_value

    prefilter: Mapping[str, object] | None = None
    if prefilter_path is not None:
        prefilter_value, prefilter_findings = _load_json_object(prefilter_path)
        if prefilter_value is None:
            findings.extend(
                Finding(f"PREFILTER_{item.code}", item.path)
                for item in prefilter_findings
            )
        else:
            prefilter = prefilter_value

    if object_type == "SourceEventPrefilterOutputCandidate":
        findings.extend(_prefilter_semantic_findings(candidate, event))
        object_id = (
            candidate["prefilter_id"]
            if isinstance(candidate.get("prefilter_id"), str)
            else None
        )
    else:
        findings.extend(_receipt_semantic_findings(candidate, event, prefilter))
        object_id = (
            candidate["receipt_id"]
            if isinstance(candidate.get("receipt_id"), str)
            else None
        )

    ordered = tuple(sorted(set(findings)))
    spec_hash = (
        candidate["spec_hash"] if isinstance(candidate.get("spec_hash"), str) else None
    )
    return ValidationResult(
        _derive_outcome(ordered, schema_findings),
        ordered,
        object_id,
        spec_hash,
    )


def _safe_display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> dict[str, object]:
    return {
        "file": _safe_display_path(path),
        "outcome": result.outcome,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "scope": SCOPE,
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "non_effects": list(NON_EFFECTS),
    }


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    manifest, manifest_findings = _load_json_object(MANIFEST_PATH)
    if manifest is None:
        return False, {
            "outcome": "ERROR",
            "findings": [
                {"code": item.code, "path": item.path}
                for item in manifest_findings
            ],
            "scope": SCOPE,
            "authority": "NONE",
        }

    cases = manifest.get("cases")
    if not isinstance(cases, list) or not cases:
        return False, {
            "outcome": "ERROR",
            "findings": [{"code": "FIXTURE_MANIFEST_INVALID", "path": "/cases"}],
            "scope": SCOPE,
            "authority": "NONE",
        }

    passed = True
    reports: list[dict[str, object]] = []
    for case in cases:
        if not isinstance(case, Mapping):
            passed = False
            continue
        file_path = FIXTURE_ROOT / str(case["file"])
        event_path = EVENT_FIXTURE_ROOT / str(case["event_file"])
        prefilter_path = (
            FIXTURE_ROOT / str(case["prefilter_file"])
            if isinstance(case.get("prefilter_file"), str)
            else None
        )
        result = validate_file(
            file_path,
            event_path=event_path,
            prefilter_path=prefilter_path,
        )
        actual_findings = [
            {"code": item.code, "path": item.path}
            for item in result.findings
        ]
        expected_findings = case["expected_findings"]
        expected_outcome = case["expected_outcome"]
        case_ok = (
            result.outcome == expected_outcome
            and actual_findings == expected_findings
        )
        passed = passed and case_ok
        reports.append(
            {
                "case_id": case["case_id"],
                "file": str(case["file"]),
                "outcome": result.outcome,
                "findings": actual_findings,
                "matches_manifest": case_ok,
            }
        )

    payload = {
        "outcome": "PASS" if passed else "FIXTURE_POLARITY_ERROR",
        "cases": len(reports),
        "reports": reports,
        "scope": SCOPE,
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "non_effects": list(NON_EFFECTS),
    }
    return passed, payload


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only SourceEvent prefilter and receipt candidates."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--event", type=Path)
    parser.add_argument("--prefilter", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures:
        if args.files or args.event or args.prefilter:
            print("--fixtures cannot be combined with file arguments", file=sys.stderr)
            return 2
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1

    if not args.files:
        print("at least one file or --fixtures is required", file=sys.stderr)
        return 2

    exit_code = 0
    for path in args.files:
        result = validate_file(
            path,
            event_path=args.event,
            prefilter_path=args.prefilter,
        )
        print(
            json.dumps(
                _serialize(path, result),
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        if result.outcome == "ERROR":
            exit_code = max(exit_code, 2)
        elif result.outcome != "PASS":
            exit_code = max(exit_code, 1)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
