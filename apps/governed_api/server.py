#!/usr/bin/env python3
"""
KFM Governed Ecology API.

Minimal FastAPI server for public-safe dry-run ecology artifacts.

Endpoints:
  GET /ecology/timeslices/{id}
  GET /ecology/evidence/{bundle_id}
  GET /ecology/catalog/stac

Default artifact root:
  data/published/ecology/dry-run

Run:
  uvicorn apps.governed_api.server:app --reload
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException


DEFAULT_ARTIFACT_ROOT = Path(
    os.environ.get("KFM_ECOLOGY_ARTIFACT_ROOT", "data/published/ecology/dry-run")
)

PUBLIC_DENY_FIELDS = {
    "raw_geometry",
    "exact_sensitive_geometry",
    "restricted_geometry",
    "internal_notes",
    "private_notes",
    "raw_source_payload",
}


app = FastAPI(
    title="KFM Governed Ecology API",
    version="0.1.0",
    description="Public-safe governed API for KFM Ecology publication artifacts.",
)


def artifact_path(name: str) -> Path:
    return DEFAULT_ARTIFACT_ROOT / name


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise HTTPException(
            status_code=404,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "ERROR",
                "message": f"Artifact not found: {path}",
            },
        )

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "ERROR",
                "message": f"Artifact is invalid JSON: {path}",
                "reasons": [str(exc)],
            },
        )


def redact_public(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: redact_public(item)
            for key, item in value.items()
            if key not in PUBLIC_DENY_FIELDS
        }

    if isinstance(value, list):
        return [redact_public(item) for item in value]

    return value


def require_public_safe_evidence(bundle: dict[str, Any]) -> None:
    if not bundle.get("resolved", False):
        raise HTTPException(
            status_code=451,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "DENY",
                "message": "EvidenceBundle is not resolved.",
                "reasons": ["unresolved_evidence_bundle"],
            },
        )

    if bundle.get("rights_status") == "unknown":
        raise HTTPException(
            status_code=451,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "DENY",
                "message": "EvidenceBundle rights are unknown.",
                "reasons": ["unknown_rights"],
            },
        )

    if bundle.get("sensitivity") == "restricted":
        raise HTTPException(
            status_code=451,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "DENY",
                "message": "Restricted EvidenceBundle cannot be returned publicly.",
                "reasons": ["restricted_evidence_bundle"],
            },
        )

    if bundle.get("exact_geometry_present") is True:
        raise HTTPException(
            status_code=451,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "DENY",
                "message": "Exact geometry is not public-safe.",
                "reasons": ["exact_geometry_present"],
            },
        )


def policy_summary(receipt: dict[str, Any]) -> dict[str, Any]:
    policy_results = receipt.get("policy_results", [])
    if not policy_results:
        return {
            "decision": "deny",
            "policy_ref": "policy/ecology/publication.rego",
            "reasons": ["missing_policy_results"],
        }

    first = policy_results[0]
    return {
        "decision": first.get("result", "deny"),
        "policy_ref": first.get("policy", "policy/ecology/publication.rego"),
        "reasons": first.get("reasons", []),
    }


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {
        "status": "ok",
        "artifact_root": str(DEFAULT_ARTIFACT_ROOT),
    }


@app.get("/ecology/timeslices/{id}")
def get_ecology_timeslice(id: str) -> dict[str, Any]:
    tileset_metadata = load_json(artifact_path("tileset_metadata.json"))
    promotion_decision = load_json(artifact_path("promotion_decision.json"))
    evidence_bundle = load_json(artifact_path("evidence_bundle.json"))
    run_receipt = load_json(artifact_path("run_receipt.json"))

    require_public_safe_evidence(evidence_bundle)

    decision = promotion_decision.get("decision")
    if decision != "PROMOTE":
        raise HTTPException(
            status_code=451,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "DENY",
                "message": "Time-slice is not promoted.",
                "reasons": [f"promotion_decision_{decision}"],
                "receipt_ref": run_receipt.get("receipt_ref"),
            },
        )

    response = {
        "schema_version": "v1",
        "object_type": "EcologyTimesliceResponse",
        "timeslice_id": f"kfm://tileset/ecology/{id}",
        "tileset_metadata": tileset_metadata,
        "promotion": {
            "decision_ref": promotion_decision.get("decision_id"),
            "decision": promotion_decision.get("decision"),
            "requires_steward": promotion_decision.get("requires_steward", False),
        },
        "evidence_bundle_ref": evidence_bundle.get("bundle_id"),
        "run_receipt_ref": run_receipt.get("receipt_ref"),
        "catalog": run_receipt.get("catalog", {}),
        "policy": policy_summary(run_receipt),
    }

    return redact_public(response)


@app.get("/ecology/evidence/{bundle_id}")
def get_ecology_evidence_bundle(bundle_id: str) -> dict[str, Any]:
    evidence_bundle = load_json(artifact_path("evidence_bundle.json"))

    expected_suffix = evidence_bundle.get("bundle_id", "").split("/")[-1]
    if bundle_id != expected_suffix and bundle_id != evidence_bundle.get("bundle_id"):
        raise HTTPException(
            status_code=404,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "ERROR",
                "message": "EvidenceBundle not found.",
            },
        )

    require_public_safe_evidence(evidence_bundle)
    return redact_public(evidence_bundle)


@app.get("/ecology/catalog/stac")
def get_ecology_stac_catalog() -> dict[str, Any]:
    catalog = load_json(artifact_path("stac_catalog.json"))
    return redact_public(catalog)
