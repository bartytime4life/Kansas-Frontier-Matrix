#!/usr/bin/env python3
"""Validate fixture-only eBird/GBIF occurrence retrieval snapshots."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Sequence

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    run_cli,
    serialize_result,
    validate_fixture_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/occurrence_retrieval_snapshot.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/occurrence_retrieval_snapshot"
SCOPE = "source.occurrence_retrieval_snapshot"

FORBIDDEN_GEOMETRY_KEYS = frozenset(
    {"coordinate", "coordinates", "decimallatitude", "decimallongitude", "geometry", "geom", "latitude", "longitude", "wkt"}
)
FORBIDDEN_SECRET_KEYS = frozenset(
    {"api_key", "api_token", "credential", "credentials", "email", "notification_address", "notification_addresses", "password", "secret", "token", "username"}
)
INTERNAL_LIFECYCLE_MARKERS = (
    "/data/raw/", "/data/work/", "/data/quarantine/", "data/raw/", "data/work/", "data/quarantine/"
)
EXPECTED_HOLDS = ["CURRENT_SOURCE_TERMS_UNVERIFIED", "SENSITIVE_OCCURRENCE_REVIEW_PENDING"]
EXPECTED_EFFORT_FIELDS = ["distance_km", "duration_minutes", "party_size", "protocol_type"]
TERMINAL_STATES = frozenset({"SUCCEEDED", "FAILED", "CANCELLED", "EXPIRED"})
FAILURE_STATES = frozenset({"FAILED", "CANCELLED", "EXPIRED"})
ALLOWED_TRANSITIONS = {
    "NOT_SUBMITTED": {"SUBMITTED"},
    "SUBMITTED": {"QUEUED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"},
    "QUEUED": {"RUNNING", "SUCCEEDED", "FAILED", "CANCELLED", "EXPIRED"},
    "RUNNING": {"SUCCEEDED", "FAILED", "CANCELLED", "EXPIRED"},
    "SUCCEEDED": set(),
    "FAILED": set(),
    "CANCELLED": set(),
    "EXPIRED": set(),
}

_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA)


def canonical_query_hash(query_snapshot: dict[str, object]) -> str:
    identity = {key: value for key, value in query_snapshot.items() if key != "query_hash"}
    canonical = json.dumps(identity, ensure_ascii=True, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def canonical_spec_hash(document: dict[str, object]) -> str:
    identity = {key: value for key, value in document.items() if key != "spec_hash"}
    canonical = json.dumps(identity, ensure_ascii=True, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _scan_payload(value: object) -> list[Finding]:
    findings: set[Finding] = set()
    pending: list[tuple[object, str]] = [(value, "$")]
    while pending:
        current, path = pending.pop()
        if isinstance(current, dict):
            for key, item in current.items():
                child_path = f"{path}.{key}"
                normalized_key = key.lower()
                if normalized_key in FORBIDDEN_GEOMETRY_KEYS:
                    add_finding(findings, "OCCURRENCE_RETRIEVAL_EXACT_GEOMETRY_DENIED", child_path)
                if normalized_key in FORBIDDEN_SECRET_KEYS:
                    add_finding(findings, "OCCURRENCE_RETRIEVAL_SECRET_FIELD_DENIED", child_path)
                pending.append((item, child_path))
        elif isinstance(current, list):
            pending.extend((item, f"{path}[{index}]") for index, item in enumerate(current))
        elif isinstance(current, str):
            normalized = current.lower()
            if any(marker in normalized for marker in INTERNAL_LIFECYCLE_MARKERS):
                add_finding(findings, "OCCURRENCE_RETRIEVAL_INTERNAL_LIFECYCLE_REF_DENIED", path)
    return sorted(findings)


def _parse_date(value: object) -> date | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        return None
    return parsed if parsed.isoformat() == value else None


def _parse_instant(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _canonical_predicate(predicate: object) -> str:
    return json.dumps(predicate, ensure_ascii=True, allow_nan=False, sort_keys=True, separators=(",", ":"))


def _has_predicate(predicates: list[object], field: str, operator: str, value: object) -> bool:
    return any(
        isinstance(item, dict)
        and item.get("field") == field
        and item.get("operator") == operator
        and item.get("value") == value
        for item in predicates
    )


def validate_document(candidate: object) -> list[Finding]:
    findings: set[Finding] = set(_scan_payload(candidate))
    schema_errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_SCHEMA_INVALID", _json_path(tuple(error.absolute_path)))
    if schema_errors or not isinstance(candidate, dict):
        return sorted(findings)

    family = candidate["source_family"]
    query = candidate["query_snapshot"]
    intent = candidate["retrieval_intent"]
    support = candidate["sampling_support"]
    transfer = candidate["transfer"]
    governance = candidate["governance"]
    assert isinstance(family, str)
    assert isinstance(query, dict)
    assert isinstance(intent, dict)
    assert isinstance(support, dict)
    assert isinstance(transfer, dict)
    assert isinstance(governance, dict)

    if query["query_hash"] != canonical_query_hash(query):
        add_finding(findings, "OCCURRENCE_RETRIEVAL_QUERY_HASH_MISMATCH", "$.query_snapshot.query_hash")
    query_hash = query["query_hash"]
    assert isinstance(query_hash, str)
    query_hex = query_hash.removeprefix("sha256:")
    expected_retrieval_id = f"kfm://candidate/source/occurrence-retrieval/{family}/{query_hex}"
    if candidate["retrieval_id"] != expected_retrieval_id:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_ID_MISMATCH", "$.retrieval_id")

    history = transfer["state_history"]
    assert isinstance(history, list)
    expected_revision = len(history)
    if candidate["revision"] != expected_revision:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_REVISION_MISMATCH", "$.revision")
    expected_snapshot_id = f"{expected_retrieval_id}/revision/{candidate['revision']}"
    if candidate["snapshot_id"] != expected_snapshot_id:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_SNAPSHOT_ID_MISMATCH", "$.snapshot_id")
    expected_previous = None if candidate["revision"] == 1 else f"{expected_retrieval_id}/revision/{candidate['revision'] - 1}"
    if candidate["previous_snapshot_ref"] != expected_previous:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_PREVIOUS_SNAPSHOT_MISMATCH", "$.previous_snapshot_ref")

    if candidate["spec_hash"] != canonical_spec_hash(candidate):
        add_finding(findings, "OCCURRENCE_RETRIEVAL_SPEC_HASH_MISMATCH", "$.spec_hash")

    expected_role = "citizen_science_observation" if family == "ebird" else "aggregated_occurrence"
    if candidate["source_role"] != expected_role:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_SOURCE_ROLE_MISMATCH", "$.source_role")
    descriptor = candidate["source_descriptor_ref"]
    assert isinstance(descriptor, str)
    if f"/{family}@" not in descriptor:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_SOURCE_DESCRIPTOR_MISMATCH", "$.source_descriptor_ref")

    date_range = query["date_range"]
    assert isinstance(date_range, dict)
    start = _parse_date(date_range["start"])
    end = _parse_date(date_range["end"])
    if start is None or end is None or start > end:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_DATE_RANGE_INVALID", "$.query_snapshot.date_range")

    for field_name in ("county_fips", "taxon_keys"):
        values = query[field_name]
        assert isinstance(values, list)
        if values != sorted(values):
            add_finding(findings, "OCCURRENCE_RETRIEVAL_SELECTOR_ORDER_INVALID", f"$.query_snapshot.{field_name}")

    predicates = query["predicates"]
    assert isinstance(predicates, list)
    predicate_keys = [_canonical_predicate(item) for item in predicates]
    if predicate_keys != sorted(predicate_keys):
        add_finding(findings, "OCCURRENCE_RETRIEVAL_PREDICATE_ORDER_INVALID", "$.query_snapshot.predicates")
    if len(set(predicate_keys)) != len(predicate_keys):
        add_finding(findings, "OCCURRENCE_RETRIEVAL_PREDICATE_DUPLICATE", "$.query_snapshot.predicates")

    if intent["exact_coordinates_requested"] is not False:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_EXACT_COORDINATES_REQUESTED", "$.retrieval_intent.exact_coordinates_requested")
    if intent["absence_claim_requested"] is not False or support["absence_claim_supported"] is not False:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_ABSENCE_CLAIM_DENIED", "$.sampling_support.absence_claim_supported")

    pair = support["ebd_sed_pair"]
    effort_fields = support["required_effort_fields"]
    assert isinstance(effort_fields, list)
    result_artifacts = transfer["result_artifact_refs"]
    assert isinstance(result_artifacts, list)

    if family == "ebird":
        if transfer["mode"] != "bulk_file":
            add_finding(findings, "OCCURRENCE_RETRIEVAL_TRANSFER_MODE_MISMATCH", "$.transfer.mode")
        if transfer["native_job_key_digest"] is not None:
            add_finding(findings, "OCCURRENCE_RETRIEVAL_BULK_JOB_DIGEST_DENIED", "$.transfer.native_job_key_digest")
        if support["support_type"] == "COMPLETE_CHECKLIST_EBD_SED":
            if intent["requested_claim_support"] != "checklist_non_detection":
                add_finding(findings, "OCCURRENCE_RETRIEVAL_CLAIM_SUPPORT_MISMATCH", "$.retrieval_intent.requested_claim_support")
            if support["non_detection_supported"] is not True:
                add_finding(findings, "OCCURRENCE_RETRIEVAL_NON_DETECTION_UNSUPPORTED", "$.sampling_support.non_detection_supported")
            if support["complete_checklists_only"] is not True:
                add_finding(findings, "OCCURRENCE_RETRIEVAL_COMPLETE_CHECKLIST_REQUIRED", "$.sampling_support.complete_checklists_only")
            if effort_fields != EXPECTED_EFFORT_FIELDS:
                add_finding(findings, "OCCURRENCE_RETRIEVAL_EFFORT_SUPPORT_INCOMPLETE", "$.sampling_support.required_effort_fields")
            if not _has_predicate(predicates, "all_species_reported", "equals", True):
                add_finding(findings, "OCCURRENCE_RETRIEVAL_REQUIRED_PREDICATE_MISSING", "$.query_snapshot.predicates")
            if not isinstance(pair, dict) or pair.get("pairing_confirmed") is not True:
                add_finding(findings, "OCCURRENCE_RETRIEVAL_EBD_SED_PAIR_REQUIRED", "$.sampling_support.ebd_sed_pair")
            else:
                pair_refs = [pair.get("ebd_artifact_ref"), pair.get("sed_artifact_ref")]
                if pair_refs[0] == pair_refs[1] or any(ref not in result_artifacts for ref in pair_refs):
                    add_finding(findings, "OCCURRENCE_RETRIEVAL_EBD_SED_PAIR_ARTIFACT_MISMATCH", "$.sampling_support.ebd_sed_pair")
        else:
            if intent["requested_claim_support"] != "presence_only" or support["non_detection_supported"] is not False:
                add_finding(findings, "OCCURRENCE_RETRIEVAL_CLAIM_SUPPORT_MISMATCH", "$.sampling_support")
            if pair is not None or effort_fields:
                add_finding(findings, "OCCURRENCE_RETRIEVAL_SOURCE_FAMILY_SUPPORT_MISMATCH", "$.sampling_support")
    else:
        if transfer["mode"] != "async_job":
            add_finding(findings, "OCCURRENCE_RETRIEVAL_TRANSFER_MODE_MISMATCH", "$.transfer.mode")
        if support["support_type"] != "PRESENCE_ONLY_OCCURRENCE" or intent["requested_claim_support"] != "presence_only":
            add_finding(findings, "OCCURRENCE_RETRIEVAL_SOURCE_FAMILY_SUPPORT_MISMATCH", "$.sampling_support.support_type")
        if support["non_detection_supported"] is not False or support["complete_checklists_only"] is not False or pair is not None or effort_fields:
            add_finding(findings, "OCCURRENCE_RETRIEVAL_SOURCE_FAMILY_SUPPORT_MISMATCH", "$.sampling_support")
        if not _has_predicate(predicates, "has_coordinate", "equals", True) or not _has_predicate(predicates, "has_geospatial_issue", "equals", False):
            add_finding(findings, "OCCURRENCE_RETRIEVAL_REQUIRED_PREDICATE_MISSING", "$.query_snapshot.predicates")

    instants: list[datetime | None] = []
    states: list[str] = []
    for item in history:
        assert isinstance(item, dict)
        states.append(item["state"])
        instants.append(_parse_instant(item["occurred_at"]))
    if any(item is None for item in instants) or any(
        current is not None and previous is not None and current <= previous
        for previous, current in zip(instants, instants[1:])
    ):
        add_finding(findings, "OCCURRENCE_RETRIEVAL_TRANSFER_TIME_ORDER_INVALID", "$.transfer.state_history")
    for previous, current in zip(states, states[1:]):
        if current not in ALLOWED_TRANSITIONS.get(previous, set()):
            add_finding(findings, "OCCURRENCE_RETRIEVAL_TRANSFER_TRANSITION_INVALID", "$.transfer.state_history")
    if transfer["current_state"] != states[-1]:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_TRANSFER_STATE_MISMATCH", "$.transfer.current_state")

    current_state = transfer["current_state"]
    job_digest = transfer["native_job_key_digest"]
    if family == "gbif" and current_state != "NOT_SUBMITTED" and job_digest is None:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_ASYNC_JOB_DIGEST_REQUIRED", "$.transfer.native_job_key_digest")

    citation_refs = transfer["citation_refs"]
    assert isinstance(citation_refs, list)
    for field_name, values in (("result_artifact_refs", result_artifacts), ("citation_refs", citation_refs)):
        if values != sorted(values):
            add_finding(findings, "OCCURRENCE_RETRIEVAL_REFERENCE_ORDER_INVALID", f"$.transfer.{field_name}")

    record_count = transfer["record_count"]
    interpretation = transfer["result_interpretation"]
    reason = transfer["failure_reason_code"]
    if current_state == "SUCCEEDED":
        if not result_artifacts:
            add_finding(findings, "OCCURRENCE_RETRIEVAL_SUCCEEDED_ARTIFACT_REQUIRED", "$.transfer.result_artifact_refs")
        if not isinstance(record_count, int):
            add_finding(findings, "OCCURRENCE_RETRIEVAL_SUCCEEDED_RECORD_COUNT_REQUIRED", "$.transfer.record_count")
        else:
            expected_interpretation = "candidate_records_available" if record_count > 0 else "zero_records_no_claim"
            if interpretation != expected_interpretation:
                add_finding(findings, "OCCURRENCE_RETRIEVAL_RESULT_INTERPRETATION_MISMATCH", "$.transfer.result_interpretation")
        if reason is not None:
            add_finding(findings, "OCCURRENCE_RETRIEVAL_FAILURE_REASON_UNEXPECTED", "$.transfer.failure_reason_code")
        if family == "gbif" and not citation_refs:
            add_finding(findings, "OCCURRENCE_RETRIEVAL_GBIF_CITATION_REQUIRED", "$.transfer.citation_refs")
    else:
        if result_artifacts or citation_refs or record_count is not None:
            add_finding(findings, "OCCURRENCE_RETRIEVAL_NONTERMINAL_RESULT_DENIED", "$.transfer")
        if interpretation != "not_evaluated":
            add_finding(findings, "OCCURRENCE_RETRIEVAL_RESULT_INTERPRETATION_MISMATCH", "$.transfer.result_interpretation")
        if current_state in FAILURE_STATES and not isinstance(reason, str):
            add_finding(findings, "OCCURRENCE_RETRIEVAL_FAILURE_REASON_REQUIRED", "$.transfer.failure_reason_code")
        if current_state not in FAILURE_STATES and reason is not None:
            add_finding(findings, "OCCURRENCE_RETRIEVAL_FAILURE_REASON_UNEXPECTED", "$.transfer.failure_reason_code")

    if governance["holds"] != EXPECTED_HOLDS:
        add_finding(findings, "OCCURRENCE_RETRIEVAL_GOVERNANCE_HOLD_REQUIRED", "$.governance.holds")

    return sorted(findings)


def validate_snapshot_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_document)


def _manifest(directory: Path) -> dict[str, list[str]]:
    try:
        value = json.loads((directory / "expected_findings_manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def _validate_lane(directory: Path, prefix: str, expect_valid: bool) -> tuple[bool, int]:
    files = sorted(directory.glob(f"{prefix}*.json"))
    if not files:
        print(f"FAIL {directory}: no fixtures found")
        return False, 0
    expected = _manifest(directory)
    ok = True
    for path in files:
        findings = validate_snapshot_file(path)
        if expect_valid:
            if findings:
                print(serialize_result(SCOPE, path, findings))
                ok = False
            else:
                print(f"OK {path}")
            continue
        actual_codes = sorted({finding.code for finding in findings})
        expected_codes = sorted(expected.get(path.name, []))
        if not findings or not expected_codes or actual_codes != expected_codes:
            print(serialize_result(SCOPE, path, findings))
            print(json.dumps({"actual": actual_codes, "expected": expected_codes, "file": str(path), "outcome": "FIXTURE_POLARITY_ERROR"}, sort_keys=True, separators=(",", ":")))
            ok = False
        else:
            print(f"EXPECTED_FAIL {path}")
    return ok, len(files)


def _run_fixture_suite() -> int:
    valid_ok, valid_count = _validate_lane(FIXTURES_ROOT / "valid", "valid_", True)
    semantic_ok, semantic_count = _validate_lane(FIXTURES_ROOT / "semantic_invalid", "semantic_invalid_", False)
    schema_ok, schema_count = _validate_lane(FIXTURES_ROOT / "schema_invalid", "invalid_", False)
    ok = valid_ok and semantic_ok and schema_ok
    if ok:
        print(
            "OCCURRENCE_RETRIEVAL_FIXTURES_VALID "
            f"valid={valid_count} semantic_invalid={semantic_count} schema_invalid={schema_count} "
            "no_network=true non_publisher=true"
        )
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--fixtures"]:
        return _run_fixture_suite()
    if "--fixtures" in args:
        print("--fixtures cannot be combined with file arguments", file=sys.stderr)
        return 2
    return run_cli(
        argv=args,
        description="Validate fixture-only occurrence retrieval snapshots.",
        scope=SCOPE,
        validator=validate_snapshot_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
