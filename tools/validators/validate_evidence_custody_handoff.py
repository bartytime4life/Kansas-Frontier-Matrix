#!/usr/bin/env python3
"""Validate fixture-only evidence custody handoff and reconciliation records."""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    run_cli,
    serialize_result,
    validate_fixture_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/evidence_custody_handoff.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/contracts/v1/evidence/evidence_custody_handoff"
SCOPE = "evidence.evidence_custody_handoff"

FORBIDDEN_GEOMETRY_KEYS = frozenset(
    {"coordinate", "coordinates", "decimallatitude", "decimallongitude", "geometry", "geom", "latitude", "longitude", "wkt"}
)
FORBIDDEN_SECRET_KEYS = frozenset(
    {"api_key", "api_token", "credential", "credentials", "email", "password", "secret", "token", "username"}
)
INTERNAL_PATH_MARKERS = (
    "/data/raw/", "/data/work/", "/data/quarantine/", "/data/published/",
    "data/raw/", "data/work/", "data/quarantine/", "data/published/",
)

_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())


def _canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=True, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def canonical_digest(value: object) -> str:
    return f"sha256:{hashlib.sha256(_canonical(value)).hexdigest()}"


def canonical_spec_hash(document: dict[str, object]) -> str:
    return canonical_digest({key: value for key, value in document.items() if key != "spec_hash"})


def canonical_handoff_id(document: dict[str, object]) -> str:
    sender = document["sender"]
    receiver = document["receiver"]
    assert isinstance(sender, dict) and isinstance(receiver, dict)
    identity_digest = canonical_digest(
        {
            "sender_boundary_id": sender["boundary_id"],
            "receiver_boundary_id": receiver["boundary_id"],
            "manifest_digest": sender["manifest_digest"],
        }
    )
    return f"kfm://candidate/evidence-custody/{identity_digest.removeprefix('sha256:')}"


def _json_path(parts: Sequence[object]) -> str:
    value = "$"
    for part in parts:
        value += f"[{part}]" if isinstance(part, int) else f".{part}"
    return value


def _parse_instant(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


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
                    add_finding(findings, "CUSTODY_EXACT_GEOMETRY_DENIED", child_path)
                if normalized_key in FORBIDDEN_SECRET_KEYS:
                    add_finding(findings, "CUSTODY_SECRET_FIELD_DENIED", child_path)
                pending.append((item, child_path))
        elif isinstance(current, list):
            pending.extend((item, f"{path}[{index}]") for index, item in enumerate(current))
        elif isinstance(current, str):
            normalized = current.lower()
            if any(marker in normalized for marker in INTERNAL_PATH_MARKERS):
                add_finding(findings, "CUSTODY_INTERNAL_LIFECYCLE_PATH_DENIED", path)
    return sorted(findings)


def validate_document(candidate: object) -> list[Finding]:
    findings: set[Finding] = set(_scan_payload(candidate))
    schema_errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        add_finding(findings, "CUSTODY_SCHEMA_INVALID", _json_path(tuple(error.absolute_path)))
    if schema_errors or not isinstance(candidate, dict):
        return sorted(findings)

    sender = candidate["sender"]
    receiver = candidate["receiver"]
    transfer = candidate["transfer"]
    items = candidate["items"]
    dispositions = candidate["receiver_dispositions"]
    summary = candidate["summary"]
    assert isinstance(sender, dict) and isinstance(receiver, dict) and isinstance(transfer, dict)
    assert isinstance(items, list) and isinstance(dispositions, list) and isinstance(summary, dict)

    if sender["manifest_digest"] != canonical_digest(items):
        add_finding(findings, "CUSTODY_MANIFEST_DIGEST_MISMATCH", "$.sender.manifest_digest")
    if receiver["reconciliation_digest"] != canonical_digest(dispositions):
        add_finding(findings, "CUSTODY_RECONCILIATION_DIGEST_MISMATCH", "$.receiver.reconciliation_digest")

    expected_handoff_id = canonical_handoff_id(candidate)
    if candidate["handoff_id"] != expected_handoff_id:
        add_finding(findings, "CUSTODY_HANDOFF_ID_MISMATCH", "$.handoff_id")
    expected_transfer_id = f"{expected_handoff_id}/transfer/{candidate['revision']}"
    if transfer["transfer_id"] != expected_transfer_id:
        add_finding(findings, "CUSTODY_TRANSFER_ID_MISMATCH", "$.transfer.transfer_id")
    expected_previous = None if candidate["revision"] == 1 else f"{expected_handoff_id}/revision/{candidate['revision'] - 1}"
    if candidate["previous_handoff_ref"] != expected_previous:
        add_finding(findings, "CUSTODY_PREVIOUS_HANDOFF_MISMATCH", "$.previous_handoff_ref")
    if candidate["spec_hash"] != canonical_spec_hash(candidate):
        add_finding(findings, "CUSTODY_SPEC_HASH_MISMATCH", "$.spec_hash")

    if sender["boundary_id"] == receiver["boundary_id"]:
        add_finding(findings, "CUSTODY_BOUNDARY_NOT_DISTINCT", "$.receiver.boundary_id")
    if receiver["lifecycle_stage"] not in {sender["lifecycle_stage"], "QUARANTINE"}:
        add_finding(findings, "CUSTODY_STAGE_ESCALATION_DENIED", "$.receiver.lifecycle_stage")

    sent_at = _parse_instant(sender["sent_at"])
    received_at = _parse_instant(receiver["received_at"])
    if sent_at is None or received_at is None or received_at < sent_at:
        add_finding(findings, "CUSTODY_TIME_ORDER_INVALID", "$.receiver.received_at")

    item_ids = [item["item_id"] for item in items if isinstance(item, dict)]
    if item_ids != sorted(item_ids):
        add_finding(findings, "CUSTODY_ITEM_ORDER_INVALID", "$.items")
    if len(set(item_ids)) != len(item_ids):
        add_finding(findings, "CUSTODY_ITEM_ID_DUPLICATE", "$.items")

    disposition_ids = [entry["item_id"] for entry in dispositions if isinstance(entry, dict)]
    if disposition_ids != sorted(disposition_ids):
        add_finding(findings, "CUSTODY_DISPOSITION_ORDER_INVALID", "$.receiver_dispositions")
    if len(set(disposition_ids)) != len(disposition_ids):
        add_finding(findings, "CUSTODY_DISPOSITION_DUPLICATE", "$.receiver_dispositions")

    item_by_id = {item["item_id"]: item for item in items if isinstance(item, dict)}
    disposition_by_id = {entry["item_id"]: entry for entry in dispositions if isinstance(entry, dict)}
    for item_id in sorted(set(item_by_id) - set(disposition_by_id)):
        add_finding(findings, "CUSTODY_ITEM_UNACCOUNTED", "$.receiver_dispositions")
    for item_id in sorted(set(disposition_by_id) - set(item_by_id)):
        add_finding(findings, "CUSTODY_UNKNOWN_ITEM_DISPOSITION", "$.receiver_dispositions")

    recorded_instants: list[datetime | None] = []
    for index, entry in enumerate(dispositions):
        assert isinstance(entry, dict)
        recorded = _parse_instant(entry["recorded_at"])
        recorded_instants.append(recorded)
        if recorded is None or received_at is None or recorded < received_at:
            add_finding(findings, "CUSTODY_TIME_ORDER_INVALID", f"$.receiver_dispositions[{index}].recorded_at")
        item = item_by_id.get(entry["item_id"])
        if not isinstance(item, dict):
            continue

        kind = entry["disposition"]
        reason_codes = entry["reason_codes"]
        assert isinstance(reason_codes, list)
        if reason_codes != sorted(reason_codes):
            add_finding(findings, "CUSTODY_REASON_CODE_ORDER_INVALID", f"$.receiver_dispositions[{index}].reason_codes")

        if kind == "ACCEPTED":
            if entry["receiver_digest"] != item["sender_digest"]:
                add_finding(findings, "CUSTODY_ACCEPTED_DIGEST_MISMATCH", f"$.receiver_dispositions[{index}].receiver_digest")
            if entry["receiver_size_bytes"] != item["sender_size_bytes"]:
                add_finding(findings, "CUSTODY_ACCEPTED_SIZE_MISMATCH", f"$.receiver_dispositions[{index}].receiver_size_bytes")
            if entry["existing_item_ref"] is not None:
                add_finding(findings, "CUSTODY_ACCEPTED_EXISTING_REF_DENIED", f"$.receiver_dispositions[{index}].existing_item_ref")
            if reason_codes != ["ACCEPTED_INTACT"]:
                add_finding(findings, "CUSTODY_ACCEPTED_REASON_INVALID", f"$.receiver_dispositions[{index}].reason_codes")
        elif kind == "DUPLICATE":
            if entry["receiver_digest"] != item["sender_digest"]:
                add_finding(findings, "CUSTODY_DUPLICATE_DIGEST_MISMATCH", f"$.receiver_dispositions[{index}].receiver_digest")
            if entry["receiver_size_bytes"] != item["sender_size_bytes"]:
                add_finding(findings, "CUSTODY_DUPLICATE_SIZE_MISMATCH", f"$.receiver_dispositions[{index}].receiver_size_bytes")
            if entry["existing_item_ref"] is None:
                add_finding(findings, "CUSTODY_DUPLICATE_EXISTING_REF_REQUIRED", f"$.receiver_dispositions[{index}].existing_item_ref")
            if reason_codes != ["IDENTICAL_CONTENT_ALREADY_PRESENT"]:
                add_finding(findings, "CUSTODY_DUPLICATE_REASON_INVALID", f"$.receiver_dispositions[{index}].reason_codes")
        elif kind == "REJECTED":
            if entry["receiver_digest"] is not None or entry["receiver_size_bytes"] is not None or entry["existing_item_ref"] is not None:
                add_finding(findings, "CUSTODY_REJECTED_RECEIVER_ARTIFACT_DENIED", f"$.receiver_dispositions[{index}]")
        elif kind == "UNRESOLVED":
            if entry["existing_item_ref"] is not None:
                add_finding(findings, "CUSTODY_UNRESOLVED_EXISTING_REF_DENIED", f"$.receiver_dispositions[{index}].existing_item_ref")

        if item["classification"] == "PUBLIC_SAFE" and item["sensitivity_state"] != "PUBLIC_SAFE":
            add_finding(findings, "CUSTODY_CLASSIFICATION_MISMATCH", f"$.items[{item_ids.index(item['item_id'])}].classification")
        unknown_posture = item["rights_state"] == "UNKNOWN" or item["sensitivity_state"] == "UNKNOWN"
        if unknown_posture and (kind != "UNRESOLVED" or receiver["lifecycle_stage"] != "QUARANTINE"):
            add_finding(findings, "CUSTODY_UNKNOWN_POSTURE_NOT_QUARANTINED", f"$.receiver_dispositions[{index}].disposition")

    counts = {"ACCEPTED": 0, "REJECTED": 0, "DUPLICATE": 0, "UNRESOLVED": 0}
    for entry in dispositions:
        assert isinstance(entry, dict)
        counts[entry["disposition"]] += 1
    expected_summary = {
        "sent": len(items),
        "accepted": counts["ACCEPTED"],
        "rejected": counts["REJECTED"],
        "duplicate": counts["DUPLICATE"],
        "unresolved": counts["UNRESOLVED"],
        "accounted": len(dispositions),
        "closure_status": "OPEN" if counts["UNRESOLVED"] else "CLOSED",
    }
    for field, expected in expected_summary.items():
        if summary[field] != expected:
            code = "CUSTODY_CLOSURE_STATUS_MISMATCH" if field == "closure_status" else "CUSTODY_SUMMARY_MISMATCH"
            add_finding(findings, code, f"$.summary.{field}")

    return sorted(findings)


def validate_handoff_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_document)


def _fixture_codes(path: Path) -> list[str]:
    return sorted({finding.code for finding in validate_handoff_file(path)})


def validate_fixture_suite() -> int:
    valid_files = sorted((FIXTURES_ROOT / "valid").glob("valid_*.json"))
    semantic_files = sorted((FIXTURES_ROOT / "semantic_invalid").glob("semantic_invalid_*.json"))
    schema_files = sorted((FIXTURES_ROOT / "invalid").glob("invalid_*.json"))
    semantic_expected = json.loads((FIXTURES_ROOT / "semantic_invalid/expected_findings_manifest.json").read_text(encoding="utf-8"))
    schema_expected = json.loads((FIXTURES_ROOT / "invalid/expected_findings_manifest.json").read_text(encoding="utf-8"))

    ok = bool(valid_files and semantic_files and schema_files)
    ok = ok and {path.name for path in semantic_files} == set(semantic_expected)
    ok = ok and {path.name for path in schema_files} == set(schema_expected)
    for path in valid_files:
        findings = validate_handoff_file(path)
        print(serialize_result(SCOPE, path, findings))
        ok = ok and not findings
    for path in semantic_files:
        findings = validate_handoff_file(path)
        print(serialize_result(SCOPE, path, findings))
        ok = ok and _fixture_codes(path) == sorted(semantic_expected[path.name])
    for path in schema_files:
        findings = validate_handoff_file(path)
        print(serialize_result(SCOPE, path, findings))
        ok = ok and _fixture_codes(path) == sorted(schema_expected[path.name])

    if ok:
        print(
            f"EVIDENCE_CUSTODY_FIXTURES_VALID valid={len(valid_files)} "
            f"semantic_invalid={len(semantic_files)} schema_invalid={len(schema_files)} "
            "no_network=true release_authority=false"
        )
        return 0
    print("EVIDENCE_CUSTODY_FIXTURES_INVALID", file=sys.stderr)
    return 1


def main(argv: Sequence[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--fixtures"]:
        return validate_fixture_suite()
    if "--fixtures" in args:
        print("--fixtures cannot be combined with file arguments", file=sys.stderr)
        return 2
    return run_cli(
        argv=args,
        description="Validate fixture-only evidence custody handoffs",
        scope=SCOPE,
        validator=validate_handoff_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
