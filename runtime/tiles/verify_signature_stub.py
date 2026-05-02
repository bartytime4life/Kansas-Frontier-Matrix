from __future__ import annotations

from typing import Any


def verify_signature_bundle(signature_bundle: dict[str, Any] | None, manifest_hash: str) -> tuple[bool, bool, bool]:
    """Deterministic Cosign/Sigstore-compatible stub.

    Returns (signature_checked, signature_valid, manifest_hash_match).
    """
    if signature_bundle is None:
        return (False, False, False)

    checked = True
    status = signature_bundle.get("status")
    signature_valid = status == "valid"
    manifest_hash_match = signature_bundle.get("manifest_hash") == manifest_hash
    return (checked, signature_valid, manifest_hash_match)
