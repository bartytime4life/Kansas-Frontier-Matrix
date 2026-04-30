#!/usr/bin/env python3
"""
KFM Governed Ecology API.

Minimal FastAPI server for public-safe dry-run ecology publication artifacts.

Endpoints:
  GET /healthz
  GET /ecology/timeslices/{id}
  GET /ecology/evidence/{bundle_id}
  GET /ecology/catalog/stac

Default artifact root:
  data/published/ecology/dry-run

Run:
  uvicorn apps.governed_api.server:app --reload

Governance posture:
  - Public endpoints fail closed on unresolved evidence, unknown rights,
    restricted sensitivity, exact geometry, missing promotion, or denied policy.
  - The API returns redacted derived/publication artifacts only.
  - Filesystem paths are not exposed in public error envelopes.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path as FsPath
from typing import Any, Final

from fastapi import FastAPI, HTTPException, Path as ApiPath


DEFAULT_ARTIFACT_ROOT: Final[FsPath] = FsPath(
    os.environ.get("KFM_ECOLOGY_ARTIFACT_ROOT", "data/published/ecology/dry-run")
)

PUBLIC_DENY_FIELDS: Final[frozenset[str]] = frozenset(
    {
        "raw_geometry",
        "exact_sensitive_geometry",
        "restricted_geometry",
        "internal_notes",
        "private_notes",
        "raw_source_payload",
    }
)

PUBLIC_RIGHTS_ALLOW_VALUES: Final[frozenset[str]] = frozenset(
    {
        "approved",
        "cc-by",
        "cc0",
        "clear",
        "cleared",
        "government_public_domain",
        "known",
        "open",
        "open_data",
        "permissive",
        "public",
        "public_domain",
        "released",
        "us_public_domain",
    }
)

PUBLIC_SENSITIVITY_ALLOW_VALUES: Final[frozenset[str]] = frozenset(
    {
        "coarse",
        "generalized",
        "low",
        "masked",
        "non_sensitive",
        "normal",
        "none",
        "not_sensitive",
        "public",
        "redacted",
    }
)

POLICY_ALLOW_VALUES: Final[frozenset[str]] = frozenset(
    {
        "allow",
        "allowed",
        "approve",
        "approved",
        "pass",
        "passed",
        "permit",
        "permitted",
        "promote",
        "promoted",
    }
)


app = FastAPI(
    title="KFM Governed Ecology API",
    version="0.1.1",
    description="Public-safe governed API for KFM Ecology publication artifacts.",
)


@dataclass(frozen=True)
class PublicationArtifacts:
    tileset_metadata: dict[str, Any]
    promotion_decision: dict[str, Any]
    evidence_bundle: dict[str, Any]
    run_receipt: dict[str, Any]


def normalize_token(value: Any) -> str:
    return str(value).strip().lower() if value is not None else ""


def error_envelope(
    *,
    status_code: int,
    outcome: str,
    message: str,
    reasons: list[str] | None = None,
    **extra: Any,
) -> None:
    detail: dict[str, Any] = {
        "object_type": "ErrorEnvelope",
        "outcome": outcome,
        "message": message,
    }
    if reasons:
        detail["reasons"] = reasons
    detail.update(extra)
    raise HTTPException(status_code=status_code, detail=detail)


def artifact_path(name: str) -> FsPath:
    return DEFAULT_ARTIFACT_ROOT / name


def load_json_artifact(name: str) -> dict[str, Any]:
    path = artifact_path(name)

    if not path.exists():
        error_envelope(
            status_code=404,
            outcome="ERROR",
            message=f"Required artifact is missing: {name}",
            reasons=["missing_artifact"],
            artifact_name=name,
        )

    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        error_envelope(
            status_code=500,
            outcome="ERROR",
            message=f"Artifact is invalid JSON: {name}",
            reasons=["invalid_json", str(exc)],
            artifact_name=name,
        )

    if not isinstance(loaded, dict):
        error_envelope(
            status_code=500,
            outcome="ERROR",
            message=f"Artifact must be a JSON object: {name}",
            reasons=["json_artifact_not_object"],
            artifact_name=name,
        )

    return loaded


def load_publication_artifacts() -> PublicationArtifacts:
    return PublicationArtifacts(
        tileset_metadata=load_json_artifact("tileset_metadata.json"),
        promotion_decision=load_json_artifact("promotion_decision.json"),
        evidence_bundle=load_json_artifact("evidence_bundle.json"),
        run_receipt=load_json_artifact("run_receipt.json"),
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


def policy_summary(receipt: dict[str, Any]) -> dict[str, Any]:
    policy_results = receipt.get("policy_results", [])
    if not isinstance(policy_results, list) or not policy_results:
        return {
            "decision": "deny",
            "policy_ref": "policy/ecology/publication.rego",
            "reasons": ["missing_policy_results"],
        }

    first = policy_results[0]
    if not isinstance(first, dict):
        return {
            "decision": "deny",
            "policy_ref": "policy/ecology/publication.rego",
            "reasons": ["malformed_policy_result"],
        }

    return {
        "decision": first.get("result", "deny"),
        "policy_ref": first.get("policy", "policy/ecology/publication.rego"),
        "reasons": first.get("reasons", []),
    }


def require_public_safe_evidence(bundle: dict[str, Any]) -> None:
    if bundle.get("resolved") is not True:
        error_envelope(
            status_code=451,
            outcome="DENY",
            message="EvidenceBundle is not resolved.",
            reasons=["unresolved_evidence_bundle"],
        )

    rights_status = normalize_token(bundle.get("rights_status"))
    if rights_status not in PUBLIC_RIGHTS_ALLOW_VALUES:
        error_envelope(
            status_code=451,
            outcome="DENY",
            message="EvidenceBundle rights are not public-release cleared.",
            reasons=[f"rights_status_{rights_status or 'missing'}"],
        )

    sensitivity = normalize_token(bundle.get("sensitivity"))
    if sensitivity not in PUBLIC_SENSITIVITY_ALLOW_VALUES:
        error_envelope(
            status_code=451,
            outcome="DENY",
            message="EvidenceBundle sensitivity is not public-safe.",
            reasons=[f"sensitivity_{sensitivity or 'missing'}"],
        )

    if bundle.get("public_release_allowed") is False:
        error_envelope(
            status_code=451,
            outcome="DENY",
            message="EvidenceBundle is not approved for public release.",
            reasons=["public_release_not_allowed"],
        )

    if bundle.get("exact_geometry_present") is not False:
        reason = (
            "exact_geometry_present"
            if bundle.get("exact_geometry_present") is True
            else "exact_geometry_not_explicitly_absent"
        )
        error_envelope(
            status_code=451,
            outcome="DENY",
            message="Exact geometry has not been ruled out for this EvidenceBundle.",
            reasons=[reason],
        )


def require_promoted(promotion_decision: dict[str, Any], run_receipt: dict[str, Any]) -> None:
    decision = normalize_token(promotion_decision.get("decision"))
    if decision != "promote":
        error_envelope(
            status_code=451,
            outcome="DENY",
            message="Artifact is not promoted for public release.",
            reasons=[f"promotion_decision_{decision or 'missing'}"],
            receipt_ref=run_receipt.get("receipt_ref"),
        )


def require_policy_allows_public_release(run_receipt: dict[str, Any]) -> dict[str, Any]:
    summary = policy_summary(run_receipt)
    decision = normalize_token(summary.get("decision"))
    if decision not in POLICY_ALLOW_VALUES:
        reasons = summary.get("reasons")
        if not isinstance(reasons, list) or not reasons:
            reasons = [f"policy_decision_{decision or 'missing'}"]
        error_envelope(
            status_code=451,
            outcome="DENY",
            message="Policy did not allow public release.",
            reasons=[str(reason) for reason in reasons],
            policy_ref=summary.get("policy_ref"),
        )
    return summary


def require_publication_allowed(artifacts: PublicationArtifacts) -> dict[str, Any]:
    require_public_safe_evidence(artifacts.evidence_bundle)
    require_promoted(artifacts.promotion_decision, artifacts.run_receipt)
    return require_policy_allows_public_release(artifacts.run_receipt)


def require_timeslice_match(requested_id: str, tileset_metadata: dict[str, Any]) -> None:
    """Deny accidental wildcard behavior when metadata declares an ID.

    Dry-run artifact shapes may vary. If no ID-like field is present, the endpoint
    keeps compatibility with the original single-artifact behavior. If an ID is
    present, the requested path value must match either the full ID or its suffix.
    """

    candidate_ids: set[str] = set()
    for key in ("id", "timeslice_id", "tileset_id", "collection_id"):
        value = tileset_metadata.get(key)
        if value:
            text = str(value)
            candidate_ids.add(text)
            candidate_ids.add(text.rstrip("/").split("/")[-1])

    requested_full = f"kfm://tileset/ecology/{requested_id}"
    if candidate_ids and requested_id not in candidate_ids and requested_full not in candidate_ids:
        error_envelope(
            status_code=404,
            outcome="ERROR",
            message="Ecology time-slice not found.",
            reasons=["timeslice_id_mismatch"],
        )


def bundle_id_matches(requested_bundle_id: str, evidence_bundle: dict[str, Any]) -> bool:
    expected = str(evidence_bundle.get("bundle_id", ""))
    if not expected:
        return False

    expected_suffix = expected.rstrip("/").split("/")[-1]
    return requested_bundle_id in {expected, expected_suffix}


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ecology/timeslices/{id}")
def get_ecology_timeslice(
    id: str = ApiPath(
        min_length=1,
        max_length=128,
        pattern=r"^[A-Za-z0-9._:-]+$",
        description="Ecology time-slice ID or suffix.",
    ),
) -> dict[str, Any]:
    artifacts = load_publication_artifacts()
    policy = require_publication_allowed(artifacts)
    require_timeslice_match(id, artifacts.tileset_metadata)

    response = {
        "schema_version": "v1",
        "object_type": "EcologyTimesliceResponse",
        "timeslice_id": f"kfm://tileset/ecology/{id}",
        "tileset_metadata": artifacts.tileset_metadata,
        "promotion": {
            "decision_ref": artifacts.promotion_decision.get("decision_id"),
            "decision": artifacts.promotion_decision.get("decision"),
            "requires_steward": artifacts.promotion_decision.get("requires_steward", False),
        },
        "evidence_bundle_ref": artifacts.evidence_bundle.get("bundle_id"),
        "run_receipt_ref": artifacts.run_receipt.get("receipt_ref"),
        "catalog": artifacts.run_receipt.get("catalog", {}),
        "policy": policy,
    }

    return redact_public(response)


@app.get("/ecology/evidence/{bundle_id:path}")
def get_ecology_evidence_bundle(bundle_id: str) -> dict[str, Any]:
    artifacts = load_publication_artifacts()
    require_publication_allowed(artifacts)

    if not bundle_id_matches(bundle_id, artifacts.evidence_bundle):
        error_envelope(
            status_code=404,
            outcome="ERROR",
            message="EvidenceBundle not found.",
            reasons=["evidence_bundle_id_mismatch"],
        )

    return redact_public(artifacts.evidence_bundle)


@app.get("/ecology/catalog/stac")
def get_ecology_stac_catalog() -> dict[str, Any]:
    artifacts = load_publication_artifacts()
    require_publication_allowed(artifacts)

    catalog = load_json_artifact("stac_catalog.json")
    return redact_public(catalog)
