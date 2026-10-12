#!/usr/bin/env python3
"""Validate fixture-only AsynchronousTransferAssessment records."""
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
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/source/asynchronous_transfer_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/source/asynchronous_transfer_assessment/cases.json"
PREFIX = "kfm:async-transfer:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
TERMINAL_JOB_STATES = {"SUCCEEDED", "FAILED", "CANCELLED", "EXPIRED"}
ACTIVE_JOB_STATES = {"REQUESTED", "QUEUED", "RUNNING"}


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
            raise DuplicateKeyError
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
            return None, (Finding("ASYNC_TRANSFER_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("ASYNC_TRANSFER_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("ASYNC_TRANSFER_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("ASYNC_TRANSFER_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("ASYNC_TRANSFER_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("ASYNC_TRANSFER_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ASYNC_TRANSFER_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"assessment_id", "spec_hash"}
    }
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def recompute_decision(value: Mapping[str, Any]) -> dict[str, Any]:
    if value["assessment_state"] == "ERROR":
        state, reason = "ERROR", "ASSESSMENT_ERROR"
        retry_allowed = False
        ingest_candidate_allowed = False
    else:
        job_state = value["job"]["state"]
        transfer_state = value["transfer"]["state"]
        local_size = value["transfer"]["local_size_bytes"]
        if transfer_state == "QUARANTINED":
            state, reason = "QUARANTINED", "CHECKSUM_MISMATCH"
            retry_allowed = True
            ingest_candidate_allowed = False
        elif transfer_state == "COMPLETE":
            state, reason = "COMPLETE_CANDIDATE", "SIZE_AND_DIGEST_MATCH"
            retry_allowed = False
            ingest_candidate_allowed = True
        elif transfer_state == "PARTIAL":
            state, reason = "RESUME_ELIGIBLE", "PARTIAL_PREFIX_CHECKPOINTED"
            retry_allowed = True
            ingest_candidate_allowed = False
        elif job_state in {"FAILED", "CANCELLED", "EXPIRED"} and local_size == 0:
            state, reason = "TERMINAL_NO_ARTIFACT", "JOB_TERMINAL_WITHOUT_ARTIFACT"
            retry_allowed = True
            ingest_candidate_allowed = False
        elif job_state in ACTIVE_JOB_STATES and transfer_state == "NOT_STARTED":
            state, reason = "WAITING", "PROVIDER_JOB_ACTIVE"
            retry_allowed = True
            ingest_candidate_allowed = False
        else:
            state, reason = "ERROR", "ASSESSMENT_ERROR"
            retry_allowed = False
            ingest_candidate_allowed = False
    return {
        "state": state,
        "reason_codes": [reason],
        "review_required": True,
        "retry_allowed": retry_allowed,
        "ingest_candidate_allowed": ingest_candidate_allowed,
    }


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
                MAX_FINDINGS + 1,
            )
        )
    except Exception:
        return (Finding("ASYNC_TRANSFER_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("ASYNC_TRANSFER_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("ASYNC_TRANSFER_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _ranges_form_prefix(ranges: object, local_size: object) -> bool:
    if not isinstance(ranges, list) or not isinstance(local_size, int):
        return False
    cursor = 0
    for item in ranges:
        if (
            not isinstance(item, list)
            or len(item) != 2
            or not all(isinstance(value, int) for value in item)
            or item[0] != cursor
            or item[1] <= item[0]
        ):
            return False
        cursor = item[1]
    return cursor == local_size


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("ASYNC_TRANSFER_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("ASYNC_TRANSFER_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            findings.add(Finding("ASYNC_TRANSFER_ID_MISMATCH", "/assessment_id"))

    if value["source_descriptor_ref"] != f"kfm://source/{value['source_id']}":
        findings.add(Finding("ASYNC_TRANSFER_SOURCE_REF_MISMATCH", "/source_descriptor_ref"))

    job = value["job"]
    job_state = job["state"]
    requested = _time(job["requested_at"])
    last_observed = _time(job["last_observed_at"])
    completed = _time(job["completed_at"])
    expires = _time(job["archive_expires_at"])
    assessed = _time(value["assessed_at"])
    if requested is not None and last_observed is not None and requested > last_observed:
        findings.add(Finding("ASYNC_TRANSFER_JOB_TIME_ORDER_INVALID", "/job/last_observed_at"))
    if last_observed is not None and assessed is not None and last_observed > assessed:
        findings.add(Finding("ASYNC_TRANSFER_JOB_TIME_ORDER_INVALID", "/assessed_at"))
    if job_state in TERMINAL_JOB_STATES:
        if completed is None or (last_observed is not None and completed < last_observed):
            findings.add(Finding("ASYNC_TRANSFER_COMPLETION_TIME_INVALID", "/job/completed_at"))
    elif completed is not None:
        findings.add(Finding("ASYNC_TRANSFER_COMPLETION_TIME_INVALID", "/job/completed_at"))
    if expires is not None and completed is not None and expires <= completed:
        findings.add(Finding("ASYNC_TRANSFER_ARCHIVE_EXPIRY_INVALID", "/job/archive_expires_at"))
    if value["provider_request_id"] is None and job_state != "REQUESTED":
        findings.add(Finding("ASYNC_TRANSFER_PROVIDER_ID_REQUIRED", "/provider_request_id"))

    poll_history = value["poll_history"]
    expected_sequence = 1
    previous_time: datetime | None = None
    for index, poll in enumerate(poll_history):
        if poll["sequence"] != expected_sequence:
            findings.add(Finding("ASYNC_TRANSFER_POLL_SEQUENCE_INVALID", f"/poll_history/{index}/sequence"))
            break
        current_time = _time(poll["observed_at"])
        if previous_time is not None and current_time is not None and current_time <= previous_time:
            findings.add(Finding("ASYNC_TRANSFER_POLL_TIME_ORDER_INVALID", f"/poll_history/{index}/observed_at"))
            break
        previous_time = current_time
        expected_sequence += 1
    if poll_history[-1]["state"] != job_state or _time(poll_history[-1]["observed_at"]) != last_observed:
        findings.add(Finding("ASYNC_TRANSFER_POLL_SNAPSHOT_MISMATCH", "/poll_history"))

    transfer = value["transfer"]
    transfer_state = transfer["state"]
    expected_size = transfer["expected_size_bytes"]
    local_size = transfer["local_size_bytes"]
    if not _ranges_form_prefix(transfer["completed_ranges"], local_size):
        findings.add(Finding("ASYNC_TRANSFER_RANGES_INVALID", "/transfer/completed_ranges"))

    checkpoint = value["checkpoint"]
    if checkpoint["byte_offset"] != local_size:
        findings.add(Finding("ASYNC_TRANSFER_CHECKPOINT_OFFSET_MISMATCH", "/checkpoint/byte_offset"))
    if checkpoint["provider_job_state"] != job_state or checkpoint["transfer_state"] != transfer_state:
        findings.add(Finding("ASYNC_TRANSFER_CHECKPOINT_STATE_MISMATCH", "/checkpoint"))
    checkpoint_time = _time(checkpoint["observed_at"])
    if checkpoint_time is not None and assessed is not None and checkpoint_time > assessed:
        findings.add(Finding("ASYNC_TRANSFER_CHECKPOINT_TIME_INVALID", "/checkpoint/observed_at"))

    ingest = value["ingest"]
    if transfer_state == "NOT_STARTED":
        coherent = (
            local_size == 0
            and transfer["completed_ranges"] == []
            and transfer["partial_sha256"] is None
            and transfer["final_sha256"] is None
            and transfer["digest_match"] is None
            and transfer["resume_basis"] == "NONE"
            and ingest["state"] == "NOT_SEEN"
            and ingest["candidate_artifact_ref"] is None
        )
        if not coherent:
            findings.add(Finding("ASYNC_TRANSFER_NOT_STARTED_STATE_INVALID", "/transfer"))
    elif transfer_state == "PARTIAL":
        coherent = (
            isinstance(expected_size, int)
            and 0 < local_size < expected_size
            and transfer["partial_sha256"] is not None
            and transfer["final_sha256"] is None
            and transfer["digest_match"] is None
            and transfer["resume_supported"] is True
            and transfer["resume_basis"] == "BYTE_RANGE"
            and ingest["state"] == "NOT_SEEN"
            and ingest["candidate_artifact_ref"] is None
        )
        if not coherent:
            findings.add(Finding("ASYNC_TRANSFER_PARTIAL_STATE_INVALID", "/transfer"))
    elif transfer_state == "COMPLETE":
        coherent = (
            isinstance(expected_size, int)
            and local_size == expected_size
            and transfer["expected_sha256"] is not None
            and transfer["final_sha256"] == transfer["expected_sha256"]
            and transfer["partial_sha256"] is None
            and transfer["digest_match"] is True
            and job_state == "SUCCEEDED"
            and ingest["state"] == "QUARANTINE_CANDIDATE"
            and ingest["candidate_artifact_ref"] is not None
        )
        if not coherent:
            findings.add(Finding("ASYNC_TRANSFER_COMPLETE_STATE_INVALID", "/transfer"))
    elif transfer_state == "QUARANTINED":
        coherent = (
            isinstance(expected_size, int)
            and local_size == expected_size
            and transfer["expected_sha256"] is not None
            and transfer["final_sha256"] is not None
            and transfer["final_sha256"] != transfer["expected_sha256"]
            and transfer["partial_sha256"] is None
            and transfer["digest_match"] is False
            and ingest["state"] == "NOT_SEEN"
            and ingest["candidate_artifact_ref"] is None
        )
        if not coherent:
            findings.add(Finding("ASYNC_TRANSFER_QUARANTINE_STATE_INVALID", "/transfer"))

    if ingest["downstream_processed_incomplete_bytes"] is not False:
        findings.add(Finding("ASYNC_TRANSFER_INCOMPLETE_BYTES_EXPOSED", "/ingest/downstream_processed_incomplete_bytes"))
    retry = value["retry_lineage"]
    if (retry["previous_assessment_ref"] is None) != (retry["reason"] is None):
        findings.add(Finding("ASYNC_TRANSFER_RETRY_LINEAGE_INVALID", "/retry_lineage"))
    if value["retry_lineage"]["previous_assessment_ref"] == value["assessment_id"]:
        findings.add(Finding("ASYNC_TRANSFER_RETRY_SELF_REFERENCE", "/retry_lineage/previous_assessment_ref"))
    if value["decision"] != recompute_decision(value):
        findings.add(Finding("ASYNC_TRANSFER_DECISION_MISMATCH", "/decision"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    state = value["decision"]["state"]
    if state in {"WAITING", "RESUME_ELIGIBLE", "COMPLETE_CANDIDATE"}:
        return Result("PASS", ())
    if state in {"QUARANTINED", "TERMINAL_NO_ARTIFACT"}:
        return Result(
            "ABSTAIN",
            (Finding(value["decision"]["reason_codes"][0], "/decision/state"),),
        )
    return Result("ERROR", (Finding("ASSESSMENT_ERROR", "/decision/state"),))


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(replacement)
    else:
        target[key] = copy.deepcopy(replacement)


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    document["decision"] = copy.deepcopy(
        case.get("decision_override", recompute_decision(document))
    )
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["assessment_id"] = case.get("assessment_id_override", identifier)
    if case.get("self_retry"):
        document["retry_lineage"]["previous_assessment_ref"] = document["assessment_id"]
        digest, identifier = canonical_identity(document)
        document["spec_hash"] = digest
        document["assessment_id"] = identifier
        document["retry_lineage"]["previous_assessment_ref"] = identifier
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": [
                "no_network",
                "no_source_activation",
                "no_download",
                "no_raw_write",
                "no_ingest",
                "no_promotion",
                "no_release",
                "no_publication",
            ],
            "outcome": result.outcome,
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
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = Result("ERROR", findings) if value is None else validate_payload(value)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
