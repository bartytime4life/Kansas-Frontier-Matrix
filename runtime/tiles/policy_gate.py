from __future__ import annotations

from typing import Any


def evaluate_policy(
    *,
    decision_envelope: dict[str, Any],
    release_manifest: dict[str, Any],
    policy_profile: dict[str, Any] | None,
) -> tuple[bool, str]:
    if decision_envelope.get("decision") != "allow":
        return (False, "decision_envelope_denied")

    posture = (policy_profile or {}).get("posture", "unknown")
    if posture not in {"strict", "public_safe"}:
        return (False, "unknown_policy_posture")

    sensitive = bool(release_manifest.get("contains_sensitive_geometry", False))
    transformed = bool(release_manifest.get("sensitive_geometry_transformed", False))
    if sensitive and not transformed:
        return (False, "sensitive_geometry_without_transformation")

    return (True, "allow")
