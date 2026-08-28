"""Validate fixture-only KFM SourceEventEnvelope candidates without network access.

The profile uses CloudEvents-shaped core attributes to normalize source-edge
notifications, then binds the candidate to KFM SourceDescriptor references,
deterministic identity, finite routing, and explicit no-authority flags.

A passing result proves only the bounded local checks implemented here. It does
not authenticate the producer, establish CloudEvents conformance, activate a
source, write RAW, resolve evidence, evaluate policy, approve review, promote,
release, deploy, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import socket
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

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "source"
    / "source_event_envelope.schema.json"
)
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures"
    / "contracts"
    / "v1"
    / "source"
    / "source_event_envelope"
)
MANIFEST_PATH = FIXTURE_ROOT / "expected_findings_manifest.json"

MAX_FILE_BYTES = 1_000_000
MAX_JSON_DEPTH = 64
MAX_SCHEMA_FINDINGS = 100
SCOPE = "source.source_event_envelope_candidate"
NON_EFFECTS = (
    "no_network_or_queue_access",
    "no_source_activation",
    "no_raw_or_lifecycle_write",
    "no_evidence_resolution",
    "no_policy_evaluation",
    "no_human_approval_creation",
    "no_promotion_release_deployment_or_publication",
)


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
    event_id: str | None = None
    payload_spec_hash: str | None = None


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
            return None, [Finding("FILE_TOO_LARGE", "/")]
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


def _load_schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
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


def _identity_projection(candidate: Mapping[str, object]) -> dict[str, object]:
    subject = _mapping(candidate["subject"])
    payload = _mapping(candidate["payload"])
    return {
        "schema_version": candidate["schema_version"],
        "profile": candidate["profile"],
        "source_descriptor_ref": candidate["source_descriptor_ref"],
        "event_type": candidate["event_type"],
        "subject": {
            "subject_ref": subject["subject_ref"],
            "native_id": subject["native_id"],
            "content_digest": subject["content_digest"],
            "byte_count": subject["byte_count"],
            "etag": subject["etag"],
            "last_modified": subject["last_modified"],
        },
        "occurred_at": candidate["occurred_at"],
        "producer": candidate["producer"],
        "payload_spec_hash": payload["payload_spec_hash"],
    }


def _expected_event_id(candidate: Mapping[str, object]) -> str:
    return "kfm:source-event:" + compute_spec_hash(_identity_projection(candidate))


def _reference_order_findings(candidate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    governance = _mapping(candidate["governance"])
    routing = _mapping(candidate["routing"])
    for field in ("evidence_refs", "policy_refs"):
        values = _string_list(governance.get(field))
        if values != sorted(values):
            findings.add(Finding("REFERENCE_ORDER_INVALID", f"/governance/{field}"))
    reasons = _string_list(routing.get("reason_codes"))
    if reasons != sorted(reasons):
        findings.add(Finding("REASON_CODE_ORDER_INVALID", "/routing/reason_codes"))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> tuple[set[Finding], str | None, str | None]:
    findings: set[Finding] = set()
    subject = _mapping(candidate["subject"])
    payload = _mapping(candidate["payload"])
    routing = _mapping(candidate["routing"])
    governance = _mapping(candidate["governance"])

    source_ref = candidate["source_descriptor_ref"]
    source_role_ref = candidate["source_role_ref"]
    if source_role_ref != f"{source_ref}#/source_role":
        findings.add(Finding("SOURCE_ROLE_REF_UNBOUND", "/source_role_ref"))

    occurred_at = _parse_aware_datetime(candidate["occurred_at"])
    received_at = _parse_aware_datetime(candidate["received_at"])
    if occurred_at is not None and received_at is not None and occurred_at > received_at:
        findings.add(Finding("TIME_ORDER_INVALID", "/received_at"))

    last_modified = _parse_aware_datetime(subject.get("last_modified"))
    if (
        last_modified is not None
        and received_at is not None
        and last_modified > received_at
    ):
        findings.add(
            Finding("SOURCE_LAST_MODIFIED_AFTER_RECEIPT", "/subject/last_modified")
        )

    event_type = candidate["event_type"]
    content_digest = subject.get("content_digest")
    byte_count = subject.get("byte_count")
    if event_type == "OBJECT_DELETED":
        if content_digest is not None or byte_count != 0:
            findings.add(Finding("CONTENT_STATE_INVALID", "/subject"))
    elif content_digest is None or not isinstance(byte_count, int) or byte_count <= 0:
        findings.add(Finding("CONTENT_STATE_INVALID", "/subject"))

    try:
        actual_payload_hash = compute_spec_hash(payload["attributes"])
        actual_event_id = _expected_event_id(candidate)
    except (CanonicalizationFailure, KeyError, TypeError):
        findings.add(Finding("CANONICALIZATION_ERROR", "/"))
        return findings, None, None

    if payload["payload_spec_hash"] != actual_payload_hash:
        findings.add(Finding("PAYLOAD_SPEC_HASH_MISMATCH", "/payload/payload_spec_hash"))
    if candidate["event_id"] != actual_event_id:
        findings.add(Finding("EVENT_ID_MISMATCH", "/event_id"))

    findings.update(_reference_order_findings(candidate))

    disposition = routing["disposition"]
    reasons = set(_string_list(routing["reason_codes"]))
    review_required = routing["review_required"]
    rights_state = governance["rights_state"]
    sensitivity_state = governance["sensitivity_state"]
    evidence_refs = _string_list(governance["evidence_refs"])
    policy_refs = _string_list(governance["policy_refs"])

    unresolved_codes: set[str] = set()
    if rights_state != "KNOWN":
        unresolved_codes.add("RIGHTS_UNRESOLVED")
    if sensitivity_state != "KNOWN":
        unresolved_codes.add("SENSITIVITY_UNRESOLVED")

    if disposition == "PROPOSE_SOURCE_ADMISSION":
        if (
            rights_state != "KNOWN"
            or sensitivity_state != "KNOWN"
            or not evidence_refs
            or not policy_refs
        ):
            findings.add(
                Finding("ADMISSION_GOVERNANCE_INCOMPLETE", "/routing/disposition")
            )
        if "SOURCE_EVENT_READY_FOR_ADMISSION_REVIEW" not in reasons:
            findings.add(
                Finding("ADMISSION_REASON_INCOMPLETE", "/routing/reason_codes")
            )
        if review_required is not True:
            findings.add(Finding("ROUTING_REVIEW_MISMATCH", "/routing/review_required"))
    elif disposition == "PROPOSE_QUARANTINE":
        if unresolved_codes and not unresolved_codes.issubset(reasons):
            findings.add(
                Finding("QUARANTINE_REASON_INCOMPLETE", "/routing/reason_codes")
            )
        if review_required is not True:
            findings.add(Finding("ROUTING_REVIEW_MISMATCH", "/routing/review_required"))
    elif disposition == "NO_ACTION":
        if not reasons.intersection({"DUPLICATE_REDELIVERY", "NO_MATERIAL_CHANGE"}):
            findings.add(Finding("NO_ACTION_REASON_INVALID", "/routing/reason_codes"))
        if review_required is not False:
            findings.add(Finding("ROUTING_REVIEW_MISMATCH", "/routing/review_required"))

    if event_type == "MANUAL_REPLAY" and disposition != "NO_ACTION":
        findings.add(Finding("MANUAL_REPLAY_ROUTING_INVALID", "/routing/disposition"))

    return findings, actual_event_id, actual_payload_hash


def validate_document(candidate: object) -> ValidationResult:
    if not isinstance(candidate, Mapping):
        return ValidationResult("DENY", (Finding("ROOT_TYPE", "/"),))

    try:
        validator = _load_schema_validator()
    except (OSError, UnicodeError, ValueError):
        return ValidationResult("ERROR", (Finding("SCHEMA_UNAVAILABLE", "/"),))

    schema_findings = _schema_findings(validator, candidate)
    if schema_findings:
        return ValidationResult("DENY", tuple(sorted(set(schema_findings))))

    findings, event_id, payload_hash = _semantic_findings(candidate)
    return ValidationResult(
        "DENY" if findings else "PASS",
        tuple(sorted(findings)),
        event_id=event_id,
        payload_spec_hash=payload_hash,
    )


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _load_json_object(path)
    if candidate is None:
        return ValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_document(candidate)


def _serialize(path: Path | None, result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "event_id": result.event_id,
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path is not None else None,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": NON_EFFECTS,
            "outcome": result.outcome,
            "payload_spec_hash": result.payload_spec_hash,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _safe_fixture_path(relative: object) -> Path | None:
    if not isinstance(relative, str) or not relative:
        return None
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        return None
    resolved = (FIXTURE_ROOT / candidate).resolve()
    try:
        resolved.relative_to(FIXTURE_ROOT.resolve())
    except ValueError:
        return None
    return resolved


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    manifest, findings = _load_json_object(MANIFEST_PATH)
    if manifest is None:
        return False, {
            "authority": "NONE",
            "cases": 0,
            "execution_mode": "FIXTURE_ONLY",
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in findings
            ],
            "non_effects": NON_EFFECTS,
            "outcome": "ERROR",
            "scope": SCOPE,
        }

    cases = manifest.get("cases")
    if not isinstance(cases, list):
        cases = []

    suite_findings: list[dict[str, object]] = []
    for index, case in enumerate(cases):
        if not isinstance(case, Mapping):
            suite_findings.append(
                {
                    "case": index,
                    "code": "FIXTURE_CASE_INVALID",
                    "path": f"/cases/{index}",
                }
            )
            continue
        path = _safe_fixture_path(case.get("file"))
        if path is None:
            suite_findings.append(
                {
                    "case": case.get("case_id"),
                    "code": "FIXTURE_PATH_INVALID",
                    "path": f"/cases/{index}/file",
                }
            )
            continue

        result = validate_file(path)
        actual_findings = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        if result.outcome != case.get("expected_outcome"):
            suite_findings.append(
                {
                    "actual": result.outcome,
                    "case": case.get("case_id"),
                    "code": "FIXTURE_OUTCOME_MISMATCH",
                    "expected": case.get("expected_outcome"),
                }
            )
        if actual_findings != case.get("expected_findings"):
            suite_findings.append(
                {
                    "actual": actual_findings,
                    "case": case.get("case_id"),
                    "code": "FIXTURE_FINDINGS_MISMATCH",
                    "expected": case.get("expected_findings"),
                }
            )

    payload = {
        "authority": "NONE",
        "cases": len(cases),
        "execution_mode": "FIXTURE_ONLY",
        "findings": suite_findings,
        "non_effects": NON_EFFECTS,
        "outcome": "DENY" if suite_findings else "PASS",
        "scope": SCOPE,
    }
    return (not suite_findings, payload)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only KFM SourceEventEnvelope candidates."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1

    if not args.files:
        parser.error("provide one or more files or use --fixtures")

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_file(path)
        print(_serialize(path, result))
        failed = failed or result.outcome != "PASS"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
