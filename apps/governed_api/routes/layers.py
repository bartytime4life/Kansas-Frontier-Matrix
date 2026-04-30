#!/usr/bin/env python3
"""
Governed ecology layer routes.

Endpoint:
  GET /ecology/layers/{id}

Returns a public-safe EcologyLayerManifest from the configured artifact root.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException


router = APIRouter(tags=["Ecology Layers"])


PUBLIC_DENY_FIELDS = {
    "raw_geometry",
    "exact_sensitive_geometry",
    "restricted_geometry",
    "internal_notes",
    "private_notes",
    "raw_source_payload",
}


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


def require_public_safe_layer(layer_manifest: dict[str, Any]) -> None:
    if layer_manifest.get("public_safe") is not True:
        raise HTTPException(
            status_code=451,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "DENY",
                "message": "Layer manifest is not marked public-safe.",
                "reasons": ["layer_not_public_safe"],
            },
        )

    if layer_manifest.get("sensitivity") not in {None, "public", "generalize"}:
        raise HTTPException(
            status_code=451,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "DENY",
                "message": "Layer sensitivity is not public-safe.",
                "reasons": ["layer_sensitivity_not_public_safe"],
            },
        )

    if layer_manifest.get("rights_status") not in {None, "public", "open"}:
        raise HTTPException(
            status_code=451,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "DENY",
                "message": "Layer rights are not public-safe.",
                "reasons": ["layer_rights_not_public_safe"],
            },
        )


@router.get("/ecology/layers/{id}")
def get_ecology_layer(id: str) -> dict[str, Any]:
    from apps.governed_api import server

    layer_manifest = load_json(
        Path(server.DEFAULT_ARTIFACT_ROOT) / "layer_manifest.json"
    )

    expected_suffix = layer_manifest.get("layer_id", "").split("/")[-1]

    if id != expected_suffix and id != layer_manifest.get("layer_id"):
        raise HTTPException(
            status_code=404,
            detail={
                "object_type": "ErrorEnvelope",
                "outcome": "ERROR",
                "message": "Ecology layer not found.",
            },
        )

    require_public_safe_layer(layer_manifest)
    return redact_public(layer_manifest)
