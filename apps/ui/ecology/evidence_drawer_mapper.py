```python
from __future__ import annotations

from typing import Any


def map_evidence_bundle_to_drawer(
    response: dict[str, Any],
) -> dict[str, Any]:
    data = response.get("data", {}) or {}

    if not isinstance(data, dict):
        return abstain_drawer(
            candidate_id="unknown",
            status="unresolved",
            reason="invalid_response_shape",
            error_code="ECO_DRAWER_INVALID_RESPONSE",
            summary="KFM abstained because the ecology EvidenceBundle response was malformed.",
        )

    candidate_id = str(data.get("candidate_id") or "unknown")
    decision = str(data.get("decision") or "abstain")
    status = str(data.get("status") or "unresolved")

    if decision != "cite":
        return abstain_drawer(
            candidate_id=candidate_id,
            status=status,
            reason=data.get("reason"),
            error_code=data.get("error_code"),
            summary=data.get(
                "claim_text",
                "KFM abstained because the ecological proof pack could not be resolved.",
            ),
        )

    evidence = data.get("evidence", {}) or {}
    if not isinstance(evidence, dict):
        evidence = {}

    receipts = evidence.get("receipts", []) or []
    catalog_refs = evidence.get("catalog_refs", {}) or {}
    uncertainty = data.get("uncertainty", {}) or {}

    return {
        "drawer_id": f"kfm.drawer.ecology.{candidate_id}",
        "candidate_id": candidate_id,
        "decision": "cite",
        "status": status,
        "title": "Ecology evidence",
        "summary": "Evidence resolved from ecology proof pack.",
        "proof_pack": {
            "ref": data.get("proof_pack_ref"),
            "spec_hash": data.get("spec_hash"),
        },
        "sections": [
            {
                "section_id": "receipts",
                "title": "Validation receipts",
                "items": receipts,
            },
            {
                "section_id": "catalog_refs",
                "title": "Catalog references",
                "items": catalog_refs,
            },
            {
                "section_id": "uncertainty",
                "title": "Uncertainty",
                "items": uncertainty,
            },
        ],
        "actions": {
            "copy_citation": True,
            "open_catalog": True,
            "open_provenance": True,
        },
    }


def abstain_drawer(
    *,
    candidate_id: str,
    status: str,
    reason: Any,
    error_code: Any,
    summary: Any,
) -> dict[str, Any]:
    return {
        "drawer_id": f"kfm.drawer.ecology.{candidate_id}",
        "candidate_id": candidate_id,
        "decision": "abstain",
        "status": status,
        "title": "Ecology evidence unavailable",
        "summary": str(summary),
        "failure": {
            "reason": reason,
            "error_code": error_code,
        },
        "sections": [
            {
                "section_id": "failure",
                "title": "Why KFM abstained",
                "items": [
                    {
                        "label": "Reason",
                        "value": reason,
                    }
                ],
            }
        ],
        "actions": {
            "copy_citation": False,
            "open_catalog": False,
            "open_provenance": False,
        },
    }
```
