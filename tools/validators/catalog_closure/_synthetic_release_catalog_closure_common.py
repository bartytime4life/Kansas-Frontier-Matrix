"""Shared no-network input and prerequisite checks for synthetic catalog closure."""
from __future__ import annotations

import json
import math
import os
import stat
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

MAX_BYTES = 768 * 1024
KNOWN_LICENSES = {"CC0-1.0", "CC-BY-4.0", "US-PUBLIC-DOMAIN"}
ALLOWED_SOURCE_ROLES = {"AUTHORITATIVE", "OBSERVED", "DERIVED"}
DENIED_REF_PREFIXES = ("raw:", "work:", "quarantine:", "internal:", "canonical:", "model:")
ERROR_CODES = {
    "INPUT_NOT_FILE",
    "INPUT_READ_ERROR",
    "INPUT_TOO_LARGE",
    "INPUT_SYMLINK_DENIED",
    "JSON_INVALID",
    "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER",
    "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
    "CANONICALIZATION_ERROR",
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]
    packet: dict[str, Any] | None = None

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def read_object(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    descriptor: int | None = None
    try:
        if path.is_symlink():
            return None, (Finding("INPUT_SYMLINK_DENIED", "/"),)
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode):
            return None, (Finding("INPUT_NOT_FILE", "/"),)
        if info.st_size > MAX_BYTES:
            return None, (Finding("INPUT_TOO_LARGE", "/"),)
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = None
            raw = stream.read(MAX_BYTES + 1)
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except FileNotFoundError:
        return None, (Finding("INPUT_NOT_FILE", "/"),)
    except DuplicateKeyError:
        return None, (Finding("JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("JSON_NONFINITE_NUMBER", "/"),)
    except (json.JSONDecodeError, UnicodeError):
        return None, (Finding("JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("INPUT_READ_ERROR", "/"),)
    finally:
        if descriptor is not None:
            os.close(descriptor)
    if not isinstance(value, dict):
        return None, (Finding("ROOT_NOT_OBJECT", "/"),)
    return value, ()


def timestamp(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def safe_ref(value: object) -> bool:
    return (
        isinstance(value, str)
        and 3 <= len(value) <= 320
        and not value.casefold().startswith(DENIED_REF_PREFIXES)
        and not value.startswith(("http://", "https://"))
    )


def canonical_refs(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(safe_ref(item) for item in value)
        and value == sorted(set(value))
    )


def full_digest(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 71
        and value.startswith("sha256:")
        and all(ch in "0123456789abcdef" for ch in value[7:])
    )


def bbox_valid(value: object) -> bool:
    return (
        isinstance(value, list)
        and len(value) == 4
        and all(isinstance(item, (int, float)) and math.isfinite(item) for item in value)
        and -180 <= value[0] < value[2] <= 180
        and -90 <= value[1] < value[3] <= 90
    )


def interval_valid(value: object) -> bool:
    return (
        isinstance(value, list)
        and len(value) == 2
        and timestamp(value[0]) is not None
        and timestamp(value[1]) is not None
        and timestamp(value[0]) <= timestamp(value[1])
    )


def _required(value: Mapping[str, Any], names: Iterable[str]) -> set[Finding]:
    return {
        Finding("REQUIRED_FIELD_MISSING", f"/{name}")
        for name in names
        if name not in value
    }


def candidate_findings(candidate: Mapping[str, Any]) -> set[Finding]:
    findings = _required(
        candidate,
        (
            "profile_version", "release_id", "release_manifest_ref",
            "release_manifest_artifact_digest", "assembled_at", "cataloged_at",
            "artifact", "source_descriptor_role", "evidence_refs", "receipt_refs",
            "proof_refs", "policy_decision_ref", "review_ref", "rollback_ref",
            "correction_ref", "policy_state", "review_state", "release_state",
            "proof_state", "transition",
        ),
    )
    if findings:
        return findings
    if candidate.get("profile_version") != "kfm.synthetic-release-catalog-closure-candidate.v1":
        findings.add(Finding("PROFILE_VERSION_UNSUPPORTED", "/profile_version"))
    for name in (
        "release_id", "release_manifest_ref", "policy_decision_ref",
        "review_ref", "rollback_ref", "correction_ref",
    ):
        if not safe_ref(candidate.get(name)):
            findings.add(Finding("REFERENCE_INVALID", f"/{name}"))
    for name in ("evidence_refs", "receipt_refs", "proof_refs"):
        if not canonical_refs(candidate.get(name)):
            findings.add(Finding("REFERENCE_SET_NOT_CANONICAL", f"/{name}"))

    artifact = candidate.get("artifact")
    if not isinstance(artifact, dict):
        findings.add(Finding("ARTIFACT_INVALID", "/artifact"))
        return findings
    for name in (
        "artifact_id", "digest", "locator", "media_type", "source_role", "bbox",
        "interval", "rights_state", "license", "sensitivity", "public_safe",
    ):
        if name not in artifact:
            findings.add(Finding("REQUIRED_FIELD_MISSING", f"/artifact/{name}"))
    digest = artifact.get("digest")
    if not full_digest(digest):
        findings.add(Finding("ARTIFACT_DIGEST_INVALID", "/artifact/digest"))
    if candidate.get("release_manifest_artifact_digest") != digest:
        findings.add(Finding("RELEASE_MANIFEST_DIGEST_MISMATCH", "/release_manifest_artifact_digest"))
    locator = artifact.get("locator")
    if not isinstance(locator, str) or not locator.startswith("urn:kfm:synthetic:"):
        findings.add(Finding("PUBLIC_OR_NETWORK_LOCATOR_DENIED", "/artifact/locator"))
    elif isinstance(digest, str) and not locator.endswith("@" + digest):
        findings.add(Finding("LOCATOR_DIGEST_MISMATCH", "/artifact/locator"))
    if artifact.get("source_role") not in ALLOWED_SOURCE_ROLES:
        findings.add(Finding("SOURCE_ROLE_UNSUPPORTED", "/artifact/source_role"))
    if candidate.get("source_descriptor_role") != artifact.get("source_role"):
        findings.add(Finding("SOURCE_ROLE_UPCAST_OR_MISMATCH", "/source_descriptor_role"))
    if not bbox_valid(artifact.get("bbox")):
        findings.add(Finding("SPATIAL_EXTENT_INVALID", "/artifact/bbox"))
    if not interval_valid(artifact.get("interval")):
        findings.add(Finding("TEMPORAL_EXTENT_INVALID", "/artifact/interval"))
    if artifact.get("rights_state") != "KNOWN" or artifact.get("license") not in KNOWN_LICENSES:
        findings.add(Finding("RIGHTS_OR_LICENSE_UNRESOLVED", "/artifact/license"))
    if artifact.get("sensitivity") != "PUBLIC" or artifact.get("public_safe") is not True:
        findings.add(Finding("SENSITIVITY_PUBLIC_SAFE_MISMATCH", "/artifact"))
    if candidate.get("policy_state") != "ALLOW":
        findings.add(Finding("POLICY_NOT_ALLOW", "/policy_state"))
    if candidate.get("review_state") != "APPROVED":
        findings.add(Finding("REVIEW_NOT_APPROVED", "/review_state"))
    if candidate.get("release_state") != "RELEASED":
        findings.add(Finding("RELEASE_NOT_CURRENT", "/release_state"))
    if candidate.get("proof_state") != "PASS":
        findings.add(Finding("PROOF_CLOSURE_MISSING", "/proof_state"))

    assembled = timestamp(candidate.get("assembled_at"))
    cataloged = timestamp(candidate.get("cataloged_at"))
    if assembled is None or cataloged is None or cataloged < assembled:
        findings.add(Finding("CATALOG_TIME_PRECEDES_RELEASE", "/cataloged_at"))

    transition = candidate.get("transition")
    if not isinstance(transition, dict):
        findings.add(Finding("TRANSITION_INVALID", "/transition"))
        return findings
    state = transition.get("state")
    if state not in {"CURRENT", "CORRECTED", "WITHDRAWN"}:
        findings.add(Finding("TRANSITION_STATE_UNSUPPORTED", "/transition/state"))
    effective = timestamp(transition.get("effective_at"))
    if effective is None or (cataloged is not None and effective > cataloged):
        findings.add(Finding("TRANSITION_TIME_INVALID", "/transition/effective_at"))
    predecessor = transition.get("predecessor_packet_ref")
    notice = transition.get("correction_notice_ref")
    if state == "CURRENT":
        if predecessor is not None or notice is not None:
            findings.add(Finding("CURRENT_TRANSITION_HAS_LINEAGE", "/transition"))
    elif not safe_ref(predecessor) or not safe_ref(notice):
        findings.add(Finding("CORRECTION_LINEAGE_MISSING", "/transition"))
    return findings
