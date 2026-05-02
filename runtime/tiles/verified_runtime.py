from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone, timedelta
from typing import Any
from uuid import uuid5, NAMESPACE_URL

from runtime.tiles.pmtiles_reader import read_pmtiles_archive, read_tile_bytes, tile_exists
from runtime.tiles.policy_gate import evaluate_policy
from runtime.tiles.verify_signature_stub import verify_signature_bundle

SPEC_HASH = hashlib.sha256(b"VERIFIED_TILE_RUNTIME_LAYER_V1").hexdigest()


def _hash_obj(data: dict[str, Any]) -> str:
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _deterministic_timestamp(seed: str) -> str:
    seconds = int(hashlib.sha256(seed.encode("utf-8")).hexdigest()[:8], 16)
    instant = datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=seconds)
    return instant.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def process_tile_request(
    *,
    pmtiles_uri: str,
    release_manifest: dict[str, Any] | None,
    evidence_bundle: dict[str, Any] | None,
    decision_envelope: dict[str, Any] | None,
    signature_bundle: dict[str, Any] | None,
    request_tile: tuple[int, int, int],
    runtime_policy_profile: dict[str, Any] | None,
) -> dict[str, Any]:
    z, x, y = request_tile
    manifest_id = (release_manifest or {}).get("release_manifest_id", "")
    evidence_id = (evidence_bundle or {}).get("evidence_bundle_id", "")
    decision_ref = (decision_envelope or {}).get("decision_ref", "")

    verification = {
        "signature_checked": False,
        "signature_valid": False,
        "manifest_hash_match": False,
        "evidence_bundle_resolved": evidence_bundle is not None,
        "pmtiles_header_valid": False,
        "result": "fail",
    }

    def envelope(outcome: str, policy_result: str, verification_status: str, reason: str, tile_payload: bytes | None = None):
        verification["result"] = "pass" if (outcome == "ANSWER") else "fail"
        report_hash = _hash_obj(verification)
        response = {
            "object_type": "RuntimeResponseEnvelope",
            "outcome": outcome,
            "tile_ref": {"z": z, "x": x, "y": y},
            "release_manifest_id": manifest_id,
            "evidence_bundle_id": evidence_id,
            "decision_ref": decision_ref,
            "verification_status": verification_status,
            "policy_result": policy_result,
            "reason": reason,
            "spec_hash": SPEC_HASH,
        }
        request_id = str(uuid5(NAMESPACE_URL, f"{pmtiles_uri}:{z}/{x}/{y}:{manifest_id}"))
        access_log = {
            "request_id": request_id,
            "timestamp": _deterministic_timestamp(request_id),
            "tile": f"{z}/{x}/{y}",
            "outcome": outcome,
            "policy_reason": reason,
            "verification_ref": report_hash,
        }
        return {
            "runtime_response_envelope": response,
            "verification_report": verification,
            "access_decision_log": access_log,
            "tile_payload": tile_payload,
        }

    if release_manifest is None:
        return envelope("DENY", "deny", "failed", "missing_release_manifest")

    manifest_id = release_manifest.get("release_manifest_id", _hash_obj(release_manifest))
    manifest_hash = _hash_obj(release_manifest)

    checked, sig_valid, manifest_match = verify_signature_bundle(signature_bundle, manifest_hash)
    verification["signature_checked"] = checked
    verification["signature_valid"] = sig_valid
    verification["manifest_hash_match"] = manifest_match

    if signature_bundle is None:
        return envelope("ABSTAIN", "deny", "unknown", "missing_signature_bundle")
    if not sig_valid:
        return envelope("DENY", "deny", "failed", "invalid_signature")
    if not manifest_match:
        return envelope("DENY", "deny", "failed", "manifest_hash_mismatch")

    if evidence_bundle is None:
        return envelope("ABSTAIN", "deny", "unknown", "missing_evidence_bundle")

    if decision_envelope is None:
        return envelope("DENY", "deny", "failed", "missing_decision_envelope")

    allowed, policy_reason = evaluate_policy(
        decision_envelope=decision_envelope,
        release_manifest=release_manifest,
        policy_profile=runtime_policy_profile,
    )
    if not allowed:
        return envelope("DENY", "deny", "failed", policy_reason)

    archive = read_pmtiles_archive(pmtiles_uri)
    verification["pmtiles_header_valid"] = archive.header_valid
    if not archive.header_valid or not archive.directory_valid:
        return envelope("ERROR", "deny", "failed", "corrupt_pmtiles_archive")

    if not tile_exists(archive, z, x, y):
        return envelope("ERROR", "deny", "failed", "tile_not_found")

    payload = read_tile_bytes(archive, z, x, y)
    return envelope("ANSWER", "allow", "verified", "allow", payload)
