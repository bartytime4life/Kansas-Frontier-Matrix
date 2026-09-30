"""Immutable, bounded snapshot carrier mechanics; no admission or activation.

Artifacts are preserved JSON text, so Python and Worker verification hashes the
same UTF-8 bytes without silently recanonicalizing measurement precision.
"""
from __future__ import annotations

import re
from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes, utc_time
from hashing import compute_spec_hash

MAX_PACKAGE_BYTES = 8 * 1024 * 1024
ARTIFACTS = ("candidate.json", "catalog.json", "evidence.json", "validation.json")
DIGEST = re.compile(r"^sha256:[a-f0-9]{64}$")
REVIEW_REQUIREMENTS = ["source_admission", "rights", "sensitivity", "policy", "independent_review", "release"]
MANIFEST_KEYS = {"profile", "package_id", "candidate_id", "source_id", "start", "end", "created_at", "artifacts", "review_requirements", "rollback_target"}


def prepare_snapshot(candidate: dict, catalog: dict, evidence: dict, validation: dict, *, rollback_target=None) -> dict:
    if rollback_target is not None and not DIGEST.fullmatch(rollback_target):
        raise ValueError("INVALID_ROLLBACK_TARGET")
    values = dict(zip(ARTIFACTS, (candidate, catalog, evidence, validation)))
    artifacts = {name: canonical_bytes(value).decode("utf-8") for name, value in values.items()}
    manifest = {"profile": "kfm.water-snapshot/v1", "candidate_id": candidate["candidate_id"],
                "source_id": "usgs-nwis", "start": candidate["start"], "end": candidate["end"],
                "created_at": candidate["retrieved_at"], "artifacts": {name: digest_bytes(text.encode()) for name, text in artifacts.items()},
                "review_requirements": REVIEW_REQUIREMENTS, "rollback_target": rollback_target}
    manifest["package_id"] = compute_spec_hash(manifest)
    snapshot = {"manifest": manifest, "artifacts": artifacts}
    validate_snapshot(canonical_bytes(snapshot))
    return snapshot


def validate_snapshot(raw: bytes) -> tuple[dict, dict]:
    snapshot = decode_object(raw, limit=MAX_PACKAGE_BYTES)
    if set(snapshot) != {"manifest", "artifacts"}:
        raise ValueError("SNAPSHOT_SHAPE_INVALID")
    manifest, texts = snapshot["manifest"], snapshot["artifacts"]
    if not isinstance(manifest, dict) or set(manifest) != MANIFEST_KEYS:
        raise ValueError("MANIFEST_SHAPE_INVALID")
    if (manifest["profile"] != "kfm.water-snapshot/v1" or manifest["source_id"] != "usgs-nwis"
            or manifest["review_requirements"] != REVIEW_REQUIREMENTS
            or manifest["rollback_target"] is not None and not DIGEST.fullmatch(manifest["rollback_target"])):
        raise ValueError("MANIFEST_PROFILE_INVALID")
    if manifest["package_id"] != compute_spec_hash({k: v for k, v in manifest.items() if k != "package_id"}):
        raise ValueError("PACKAGE_DIGEST_MISMATCH")
    if not 0 < (utc_time(manifest["end"]) - utc_time(manifest["start"])).total_seconds() <= 86400:
        raise ValueError("SNAPSHOT_INTERVAL_INVALID")
    utc_time(manifest["created_at"])
    if (not isinstance(texts, dict) or set(texts) != set(ARTIFACTS)
            or not isinstance(manifest["artifacts"], dict) or set(manifest["artifacts"]) != set(ARTIFACTS)):
        raise ValueError("ARTIFACT_CLOSURE_INVALID")
    values = {}
    for name in ARTIFACTS:
        if not isinstance(texts[name], str):
            raise ValueError("ARTIFACT_TEXT_REQUIRED")
        payload = texts[name].encode("utf-8")
        if digest_bytes(payload) != manifest["artifacts"][name]:
            raise ValueError("ARTIFACT_DIGEST_MISMATCH")
        values[name] = decode_object(payload, limit=MAX_PACKAGE_BYTES)
    candidate, catalog, evidence, validation = [values[name] for name in ARTIFACTS]
    if any(item.get("candidate_id") != manifest["candidate_id"] for item in (candidate, catalog, evidence, validation)):
        raise ValueError("CANDIDATE_BINDING_MISMATCH")
    if (digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "candidate_id"})) != manifest["candidate_id"]
            or candidate.get("start") != manifest["start"] or candidate.get("end") != manifest["end"]
            or candidate.get("retrieved_at") != manifest["created_at"]):
        raise ValueError("CANDIDATE_IDENTITY_MISMATCH")
    if (validation.get("outcome") != "PASS"
            or validation.get("receipt_digest") != digest_bytes(canonical_bytes({k: v for k, v in validation.items() if k != "receipt_digest"}))):
        raise ValueError("VALIDATION_RECEIPT_INVALID")
    # Authority is read separately from owner-controlled release metadata.
    if candidate.get("release_state") != "UNRELEASED" or catalog.get("authoritative") is not False:
        raise ValueError("CARRIER_CANNOT_SELF_APPROVE")
    if not isinstance(candidate.get("observations"), list) or len(candidate["observations"]) > 4000:
        raise ValueError("OBSERVATION_LIMIT")
    if not isinstance(evidence.get("entries"), list) or len(evidence["entries"]) != 2:
        raise ValueError("EVIDENCE_CLOSURE_INVALID")
    if {e["station_id"] for e in evidence["entries"]} != {s["id"] for s in candidate["stations"]}:
        raise ValueError("STATION_EVIDENCE_MISMATCH")
    stations = candidate["stations"]
    if len(stations) != 2 or {s["id"] for s in stations} != {"USGS-06892518", "USGS-07156900"}:
        raise ValueError("STATION_SCOPE_INVALID")
    for entry in evidence["entries"]:
        station = next(s for s in stations if s["id"] == entry["station_id"])
        records = [r for r in candidate["observations"] if r["station_id"] == station["id"]]
        bundle = entry["bundle"]
        ref = entry["evidence_ref"]
        expected_ref = "kfm://water/station/" + station["id"] + "/" + candidate["candidate_id"].split(":")[1]
        if ref != {"ref": expected_ref, "kind": "dataset", "bundle_ref": bundle["bundle_id"]}:
            raise ValueError("DATASET_EVIDENCE_MISMATCH")
        members = [ref] + [{"ref": r["evidence_ref"], "kind": "measurement", "bundle_ref": bundle["bundle_id"]} for r in records]
        if bundle["evidence_refs"] != members or len(members) > 128:
            raise ValueError("MEASUREMENT_EVIDENCE_MISMATCH")
        if bundle["checksums"] != {"candidate": candidate["candidate_id"], "validation": validation["receipt_digest"]}:
            raise ValueError("BUNDLE_CONTENT_BINDING_MISMATCH")
        if bundle["source_records"] != sorted({station["page_digest"], *[r["page_digest"] for r in records]}):
            raise ValueError("SOURCE_RECORD_BINDING_MISMATCH")
        if entry["verification_history"]["subject_ref"] != expected_ref:
            raise ValueError("HISTORY_SUBJECT_MISMATCH")
    return manifest, values
