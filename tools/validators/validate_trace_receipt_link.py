#!/usr/bin/env python3
"""Validate fixture-first TraceReceiptLink records without network access.

A pass proves bounded local shape and linkage semantics only. It does not start
or verify an OpenTelemetry trace, authenticate a receipt, retrieve an OCI
object, verify a signature, close evidence, evaluate policy, promote, release,
or publish.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/telemetry/trace_receipt_link.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/telemetry/trace_receipt_link"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "trace-receipt-evidence-linkage-only"
CANONICAL_UTC_SECOND = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(
            item.code.startswith(
                ("FILE_", "JSON_", "INPUT_", "ROOT_", "SCHEMA_UNAVAILABLE")
            )
            for item in self.findings
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_nonfinite,
                parse_float=_finite_float,
            )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def canonical_link_id(candidate: Mapping[str, Any]) -> str:
    run = _mapping(candidate.get("run_anchor"))
    receipt = _mapping(candidate.get("run_receipt"))
    evidence = _mapping(candidate.get("evidence_bundle"))
    values = (
        run.get("run_id"),
        run.get("trace_id"),
        receipt.get("digest"),
        evidence.get("digest"),
    )
    if not all(isinstance(value, str) for value in values):
        raise ValueError("link identity anchors are incomplete")
    encoded = "\n".join(values).encode("utf-8")
    return "urn:kfm:trace-receipt-link:sha256:" + hashlib.sha256(encoded).hexdigest()


def _time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not CANONICAL_UTC_SECOND.fullmatch(value):
        return None
    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return None
    return parsed


def _digest_hex(value: Any) -> str | None:
    if not isinstance(value, str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", value):
        return None
    return value.removeprefix("sha256:")


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    run = _mapping(candidate.get("run_anchor"))
    receipt = _mapping(candidate.get("run_receipt"))
    evidence = _mapping(candidate.get("evidence_bundle"))
    assessment = _mapping(candidate.get("assessment"))
    governance = _mapping(candidate.get("governance"))

    try:
        if candidate.get("link_id") != canonical_link_id(candidate):
            findings.append(Finding("LINK_ID_MISMATCH", "/link_id"))
    except ValueError:
        findings.append(Finding("LINK_ID_UNVERIFIABLE", "/link_id"))

    for field, code in (
        ("run_id", "RUN_ID_MISMATCH"),
        ("spec_hash", "SPEC_HASH_MISMATCH"),
        ("trace_id", "TRACE_ID_MISMATCH"),
    ):
        if not (run.get(field) == receipt.get(field) == evidence.get(field)):
            findings.append(Finding(code, f"/{field}"))

    trace_id = run.get("trace_id")
    span_id = run.get("root_span_id")
    git_sha = run.get("git_sha")
    if isinstance(trace_id, str) and set(trace_id) == {"0"}:
        findings.append(Finding("TRACE_ID_ZERO_DENIED", "/run_anchor/trace_id"))
    if isinstance(span_id, str) and set(span_id) == {"0"}:
        findings.append(Finding("SPAN_ID_ZERO_DENIED", "/run_anchor/root_span_id"))
    if isinstance(git_sha, str) and set(git_sha) == {"0"}:
        findings.append(Finding("GIT_SHA_PLACEHOLDER_DENIED", "/run_anchor/git_sha"))

    start = _time(run.get("started_at"))
    end = _time(run.get("ended_at"))
    receipt_time = _time(receipt.get("emitted_at"))
    evidence_time = _time(evidence.get("recorded_at"))
    evaluated = _time(assessment.get("evaluated_at"))
    times = (start, end, receipt_time, evidence_time, evaluated)
    if any(value is None for value in times):
        findings.append(Finding("TIMESTAMP_CANONICALIZATION_REQUIRED", "/"))
    else:
        assert start and end and receipt_time and evidence_time and evaluated
        if not (
            start <= end
            and start <= receipt_time <= evaluated
            and start <= evidence_time <= evaluated
            and end <= evaluated
        ):
            findings.append(Finding("TIMESTAMP_ORDER_INVALID", "/"))
        receipt_delay = int((receipt_time - start).total_seconds())
        evidence_delay = int((evidence_time - start).total_seconds())
        if assessment.get("receipt_delay_seconds") != receipt_delay:
            findings.append(Finding("RECEIPT_DELAY_MISMATCH", "/assessment/receipt_delay_seconds"))
        if assessment.get("evidence_delay_seconds") != evidence_delay:
            findings.append(Finding("EVIDENCE_DELAY_MISMATCH", "/assessment/evidence_delay_seconds"))
        maximum = assessment.get("max_link_delay_seconds")
        if isinstance(maximum, int) and (receipt_delay > maximum or evidence_delay > maximum):
            findings.append(Finding("LINKAGE_DELAY_EXCEEDED", "/assessment/max_link_delay_seconds"))

    evidence_digest = _digest_hex(evidence.get("digest"))
    if evidence_digest is not None:
        expected_suffix = "@sha256:" + evidence_digest
        if not isinstance(evidence.get("oci_ref"), str) or not evidence["oci_ref"].endswith(expected_suffix):
            findings.append(Finding("EVIDENCE_REF_DIGEST_MISMATCH", "/evidence_bundle/oci_ref"))

    attestation_digests: set[str] = set()
    attestation_refs: set[str] = set()
    attestations = evidence.get("attestations")
    if isinstance(attestations, list):
        for index, item in enumerate(attestations):
            entry = _mapping(item)
            digest_hex = _digest_hex(entry.get("digest"))
            digest_value = entry.get("digest")
            ref = entry.get("ref")
            if entry.get("subject_digest") != evidence.get("digest"):
                findings.append(Finding("ATTESTATION_SUBJECT_MISMATCH", f"/evidence_bundle/attestations/{index}/subject_digest"))
            if digest_hex is not None and (not isinstance(ref, str) or not ref.endswith("@sha256:" + digest_hex)):
                findings.append(Finding("ATTESTATION_REF_DIGEST_MISMATCH", f"/evidence_bundle/attestations/{index}/ref"))
            if isinstance(digest_value, str):
                if digest_value in attestation_digests:
                    findings.append(Finding("ATTESTATION_DUPLICATE", f"/evidence_bundle/attestations/{index}/digest"))
                attestation_digests.add(digest_value)
            if isinstance(ref, str):
                if ref in attestation_refs:
                    findings.append(Finding("ATTESTATION_DUPLICATE", f"/evidence_bundle/attestations/{index}/ref"))
                attestation_refs.add(ref)

    if assessment.get("status") != "LINKED" or assessment.get("gate_disposition") != "PASS" or assessment.get("reason_codes") != ["TRACE_RECEIPT_EVIDENCE_LINKED"]:
        findings.append(Finding("LINKAGE_REASON_INVALID", "/assessment"))

    governed_flags = (
        "telemetry_truth_authority_created",
        "evidence_truth_authority_created",
        "promotion_authorized",
        "release_authorized",
        "publication_authorized",
        "public_route_created",
        "sensitive_payload_included",
    )
    if any(governance.get(name) is not False for name in governed_flags):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    return findings


def validate_link(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    schema_findings = _schema_findings(candidate)
    findings.extend(schema_findings)
    if not schema_findings:
        findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display(path),
            "findings": [
                {"code": item.code, "field": item.field}
                for item in result.findings
            ],
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _expected_manifest() -> dict[str, list[str]]:
    path = FIXTURE_ROOT / "invalid/expected_findings_manifest.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("expected findings manifest must be an object")
    return {
        str(name): sorted(str(code) for code in codes)
        for name, codes in value.items()
        if isinstance(name, str) and isinstance(codes, list)
    }


def validate_fixtures() -> int:
    valid_paths = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
    invalid_paths = sorted(
        path
        for path in (FIXTURE_ROOT / "invalid").glob("*.json")
        if path.name != "expected_findings_manifest.json"
    )
    try:
        expected = _expected_manifest()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        print("ERROR: expected findings manifest is unavailable or invalid.")
        return 1
    if not valid_paths or not invalid_paths or sorted(expected) != [path.name for path in invalid_paths]:
        print("ERROR: trace receipt link fixture inventory is incomplete or drifted.")
        return 1
    failed = False
    for path in valid_paths:
        result = validate_link(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    for path in invalid_paths:
        result = validate_link(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        failed = failed or result.ok or actual != expected[path.name]
    if failed:
        print("ERROR: trace receipt link fixture polarity failed.")
        return 1
    print(f"CONFIRMED: {len(valid_paths)} valid and {len(invalid_paths)} invalid trace receipt link fixtures passed exact polarity.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate proposed KFM TraceReceiptLink records.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return validate_fixtures()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_link(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
