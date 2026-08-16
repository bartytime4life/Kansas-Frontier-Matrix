"""Deterministic STAC/DCAT/PROV projection and closed-schema checks."""
from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker

from _synthetic_release_catalog_closure_common import (
    ERROR_CODES, Finding, Result, timestamp,
)
from hashing import CanonicalizationFailure, compute_spec_hash

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/data/synthetic_release_catalog_closure_profile.schema.json"
ID_PREFIX = "kfm:synthetic-release-catalog-closure:"
MAX_SCHEMA_FINDINGS = 50


def _projection_state(state: str) -> tuple[str, str, str]:
    if state == "CURRENT":
        return "APPROVED", "RELEASED", "CURRENT"
    if state == "CORRECTED":
        return "WITHDRAWN", "SUPERSEDED", "SUPERSEDED"
    return "WITHDRAWN", "WITHDRAWN", "WITHDRAWN"


def _record(profile: str, role: str, candidate: Mapping[str, Any]) -> dict[str, Any]:
    artifact = candidate["artifact"]
    transition = candidate["transition"]
    review_state, release_state, catalog_state = _projection_state(transition["state"])
    slug = role.lower().replace("_", "-")
    return {
        "profile": profile,
        "record_id": f"kfm:catalog:{profile.lower()}:{slug}:{candidate['release_id'].split(':')[-1]}",
        "release_id": candidate["release_id"],
        "artifact_id": artifact["artifact_id"],
        "digest": artifact["digest"],
        "bbox": artifact["bbox"],
        "interval": artifact["interval"],
        "source_role": artifact["source_role"],
        "license": artifact["license"],
        "sensitivity": artifact["sensitivity"],
        "public_safe": artifact["public_safe"] and catalog_state == "CURRENT",
        "review_state": review_state,
        "release_state": release_state,
        "catalog_state": catalog_state,
        "correction_ref": transition.get("correction_notice_ref") or candidate["correction_ref"],
        "rollback_ref": candidate["rollback_ref"],
        "authored_at": candidate["cataloged_at"],
        "public_url": None,
    }


def build_projections(candidate: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "stac_collection": _record("STAC", "COLLECTION", candidate),
        "stac_item": _record("STAC", "ITEM", candidate),
        "dcat_dataset": _record("DCAT", "DATASET", candidate),
        "dcat_distribution": _record("DCAT", "DISTRIBUTION", candidate),
        "prov_entity": _record("PROV", "ENTITY", candidate),
        "prov_activity": _record("PROV", "ACTIVITY", candidate),
        "prov_agent": _record("PROV", "AGENT", candidate),
    }


def projection_findings(expected: Mapping[str, Any], supplied: object) -> set[Finding]:
    if supplied is None:
        return set()
    if not isinstance(supplied, dict):
        return {Finding("HAND_AUTHORED_PROJECTION_INVALID", "/provided_projections")}
    findings: set[Finding] = set()
    dimensions = {
        "record_id": "PROJECTION_IDENTITY_MISMATCH",
        "release_id": "PROJECTION_RELEASE_MISMATCH",
        "artifact_id": "PROJECTION_IDENTITY_MISMATCH",
        "digest": "PROJECTION_DIGEST_MISMATCH",
        "bbox": "PROJECTION_EXTENT_MISMATCH",
        "interval": "PROJECTION_EXTENT_MISMATCH",
        "source_role": "PROJECTION_SOURCE_ROLE_MISMATCH",
        "license": "PROJECTION_RIGHTS_MISMATCH",
        "sensitivity": "PROJECTION_SENSITIVITY_MISMATCH",
        "public_safe": "PROJECTION_STATE_MISMATCH",
        "review_state": "PROJECTION_STATE_MISMATCH",
        "release_state": "PROJECTION_STATE_MISMATCH",
        "catalog_state": "PROJECTION_STATE_MISMATCH",
        "correction_ref": "PROJECTION_LINEAGE_MISMATCH",
        "rollback_ref": "PROJECTION_LINEAGE_MISMATCH",
        "public_url": "PROJECTION_PUBLIC_URL_DENIED",
    }
    for key, record in expected.items():
        actual = supplied.get(key)
        if not isinstance(actual, dict):
            findings.add(Finding("PROJECTION_RECORD_MISSING", f"/provided_projections/{key}"))
            continue
        for field, code in dimensions.items():
            if actual.get(field) != record.get(field):
                findings.add(Finding(code, f"/provided_projections/{key}/{field}"))
        authored = timestamp(actual.get("authored_at"))
        expected_authored = timestamp(record.get("authored_at"))
        if authored is None or expected_authored is None or authored < expected_authored:
            findings.add(Finding(
                "HAND_AUTHORED_PROJECTION_PRECEDES_RELEASE",
                f"/provided_projections/{key}/authored_at",
            ))
    if set(supplied) - set(expected):
        findings.add(Finding("PROJECTION_RECORD_UNEXPECTED", "/provided_projections"))
    return findings


def schema_findings(packet: Mapping[str, Any]) -> set[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(
                schema, format_checker=FormatChecker()
            ).iter_errors(packet),
            key=lambda error: (
                "/" + "/".join(str(item) for item in error.absolute_path),
                str(error.validator),
            ),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return {Finding("SCHEMA_UNAVAILABLE", "/")}
    return {
        Finding(
            "GENERATED_PACKET_SCHEMA_INVALID",
            "/" + "/".join(str(item) for item in error.absolute_path),
        )
        for error in errors[:MAX_SCHEMA_FINDINGS]
    }


def build_packet(candidate: Mapping[str, Any]) -> dict[str, Any]:
    semantic_subject = {
        "release_id": candidate["release_id"],
        "release_manifest_ref": candidate["release_manifest_ref"],
        "artifact": candidate["artifact"],
        "prerequisites": {
            "evidence_refs": candidate["evidence_refs"],
            "receipt_refs": candidate["receipt_refs"],
            "proof_refs": candidate["proof_refs"],
            "policy_decision_ref": candidate["policy_decision_ref"],
            "review_ref": candidate["review_ref"],
            "rollback_ref": candidate["rollback_ref"],
            "correction_ref": candidate["correction_ref"],
            "policy_state": candidate["policy_state"],
            "review_state": candidate["review_state"],
            "release_state": candidate["release_state"],
            "proof_state": candidate["proof_state"],
        },
        "projections": build_projections(candidate),
        "transition": copy.deepcopy(candidate["transition"]),
    }
    packet = {
        "object_type": "SyntheticReleaseCatalogClosurePacket",
        "profile_version": "kfm.synthetic-release-catalog-closure.v1",
        "packet_id": "",
        "spec_hash": "",
        **semantic_subject,
        "closure_report": {
            "outcome": "PASS",
            "reason_codes": [],
            "semantic_digest": compute_spec_hash(semantic_subject),
            "deterministic_replay": True,
            "history_preserved": True,
            "public_serving": False,
        },
        "authority": {
            "catalog_grants_evidence": False,
            "catalog_decides_policy": False,
            "catalog_approves_review": False,
            "catalog_authorizes_release": False,
            "catalog_publishes": False,
            "network_used": False,
            "lifecycle_written": False,
        },
    }
    subject = {key: value for key, value in packet.items() if key not in {"packet_id", "spec_hash"}}
    packet["spec_hash"] = compute_spec_hash(subject)
    packet["packet_id"] = ID_PREFIX + packet["spec_hash"].split(":", 1)[1][:24]
    return packet


def finish_validation(candidate: Mapping[str, Any]) -> Result:
    try:
        packet = build_packet(candidate)
    except (CanonicalizationFailure, KeyError, TypeError, ValueError):
        return Result("ERROR", (Finding("CANONICALIZATION_ERROR", "/"),))
    findings = projection_findings(
        packet["projections"], candidate.get("provided_projections")
    )
    expected_hash = candidate.get("expected_spec_hash")
    if expected_hash is not None and expected_hash != packet["spec_hash"]:
        findings.add(Finding("DETERMINISTIC_DIGEST_MISMATCH", "/expected_spec_hash"))
    findings |= schema_findings(packet)
    if findings:
        outcome = "ERROR" if any(item.code in ERROR_CODES for item in findings) else "DENY"
        return Result(outcome, tuple(sorted(findings)))
    return Result("PASS", (), packet)
