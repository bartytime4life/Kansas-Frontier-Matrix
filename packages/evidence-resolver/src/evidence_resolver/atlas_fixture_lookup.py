"""Fixed, read-only lookup of the existing synthetic Atlas fixture packet.

FOUND means byte/identity binding only. It never means resolver RESOLVED or a
public ANSWER. No policy, verification, review or release input is accepted.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import PurePosixPath
import re

from . import hydrology_fixture_adapter as _files
from .core import (
    BoundedJSONError,
    CandidateInputError,
    MAX_STRING_LENGTH,
    _validate_evidence_bundle,
    loads_bounded,
)


LOOKUP_PROFILE = "kfm/synthetic-atlas-fixture-lookup/v1alpha1"
CANDIDATE_ID = "atlas-candidate:synthetic-kansas-proof-v1"
SUBJECT_REF = "overlay:synthetic-kansas-promotion-proof"
EVIDENCE_REF = "evidence:synthetic:promotion-proof:v1"
FEATURE_ID = "synthetic-kansas-test-extent"
TIME_START = "2026-04-13T00:00:00Z"
TIME_END = "2026-04-13T01:00:00Z"
MAX_FIXTURE_BYTES = 32_768
_SELECTOR = re.compile(r"^[a-z][a-z0-9_:.-]*$")
_MANIFEST_PATH = PurePosixPath(
    "fixtures/packages/evidence_resolver/v1alpha1/repository/atlas_bundle_manifest.json"
)
# Code-owned allowlist: manifest edits alone cannot change paths or digest pins.
_ARTIFACTS = (
    ("carrier", "fixtures/release/promotion_verification_execution/artifacts/synthetic_atlas_carrier.geojson",
     "sha256:8ad3948994680b0e6a85a3eb4c82f69466d0c5c2baf4c15fb4e14e43c1acb26d"),
    ("reference", "fixtures/release/promotion_verification_execution/references/evidence.json",
     "sha256:79aa8c518fe95922cc3c29567a5edf067a866a5b0036eb0133a930b73a2748f6"),
    ("bundle", "fixtures/contracts/v1/evidence/evidence_bundle/valid/valid_3.json",
     "sha256:b84c2869e16f6c4050f1a5736fad57fd6fa3a9fb65bde5f4c709b0a8487c530f"),
)
_HOLD = "atlas-lookup/verification-subject-profile-incompatible"


@dataclass(frozen=True)
class AtlasFixturePacket:
    """Immutable internal bytes; never a public response or verification record."""

    candidate_id: str
    subject_ref: str
    evidence_ref: str
    feature_id: str
    time_start: str
    time_end: str
    carrier_bytes: bytes
    reference_bytes: bytes
    bundle_bytes: bytes


@dataclass(frozen=True)
class AtlasFixtureLookup:
    """Lookup diagnostics deliberately omit packet bytes and filesystem paths."""

    status: str
    packet: AtlasFixturePacket | None
    checks_performed: tuple[str, ...]
    issues: tuple[str, ...]

    def as_dict(self) -> dict[str, object]:
        return {
            "profile": LOOKUP_PROFILE,
            "status": self.status,
            "authoritative": False,
            "renderable": False,
            "checks_performed": list(self.checks_performed),
            "issues": list(self.issues),
            "resolution_hold": _HOLD if self.status == "FOUND" else None,
        }


def _manifest_contract() -> dict[str, object]:
    return {
        "adapter_profile": LOOKUP_PROFILE,
        "candidate_id": CANDIDATE_ID,
        "subject_ref": SUBJECT_REF,
        "evidence_ref": EVIDENCE_REF,
        "feature_id": FEATURE_ID,
        "temporal": {"start": TIME_START, "end": TIME_END},
        "artifacts": {
            role: {"path": path, "sha256": digest}
            for role, path, digest in _ARTIFACTS
        },
    }


def _read(relative: PurePosixPath, role: str, checks: list[str]) -> bytes:
    # Reuse the repaired package-internal descriptor reader. Do not widen the
    # Hydrology adapter's manifest/allowlist or fork its security-critical I/O.
    raw = _files._read_repository_file(
        relative, checks=checks, unreadable_code=f"atlas-lookup/{role}-unreadable"
    )
    if len(raw) > MAX_FIXTURE_BYTES:
        raise _files.FixtureAdapterError("atlas-lookup/fixture-too-large", tuple(checks))
    checks.append(f"atlas_{role}_bounded_read")
    return raw


def _binding_matches(carrier: object, reference: object, bundle: object) -> bool:
    """Cross-bind exact identities/time without inferring claim semantics."""
    if not all(isinstance(value, dict) for value in (carrier, reference, bundle)):
        return False
    try:
        _validate_evidence_bundle(bundle)
        return (
            carrier["type"] == "FeatureCollection"
            and carrier["kfm"]["candidate_id"] == SUBJECT_REF
            and carrier["kfm"]["fixture_only"] is True
            and carrier["kfm"]["lifecycle_state"] == "FIXTURE"
            and carrier["kfm"]["truth_posture"] == "SYNTHETIC"
            and carrier["kfm"]["temporal"] == {"start": TIME_START, "end": TIME_END}
            and len(carrier["features"]) == 1
            and carrier["features"][0]["id"] == FEATURE_ID
            and reference["object_type"] == "ResolvedPromotionReference"
            and reference["kind"] == "EVIDENCE_BUNDLE"
            and reference["ref_id"] == EVIDENCE_REF
            and reference["artifact_digest"] == _ARTIFACTS[0][2]
            and bundle["bundle_id"] == EVIDENCE_REF
            and bundle["spec_hash"]["value"] == reference["subject_spec_hash"]
            and bundle["checksums"]["carrier"] == _ARTIFACTS[0][2]
            and bundle["checksums"]["promotion_evidence_reference"] == _ARTIFACTS[1][2]
            and bundle["evidence_refs"] == [
                {"ref": SUBJECT_REF, "kind": "artifact", "bundle_ref": EVIDENCE_REF}
            ]
        )
    except (KeyError, TypeError, IndexError, CandidateInputError):
        return False


def lookup_atlas_fixture(candidate_id: str) -> AtlasFixtureLookup:
    """Look up one opaque selector; accept no path, bundle, URL or trust state.

    Unknown syntactically valid IDs return NOT_FOUND without filesystem reads.
    Every failure discards packet data. Successful lookup still has a mandatory
    verification-subject HOLD: overlay: identity cannot satisfy the current
    kfm://-only verification-history profile without an explicit contract change.
    """
    checks: list[str] = []
    if (
        not isinstance(candidate_id, str)
        or len(candidate_id) > MAX_STRING_LENGTH
        or not _SELECTOR.fullmatch(candidate_id)
    ):
        return AtlasFixtureLookup("ERROR", None, (), ("atlas-lookup/selector-invalid",))
    checks.append("atlas_selector_shape")
    if candidate_id != CANDIDATE_ID:
        return AtlasFixtureLookup("NOT_FOUND", None, tuple(checks), ("atlas-lookup/not-found",))
    try:
        manifest = loads_bounded(_read(_MANIFEST_PATH, "manifest", checks))
        if manifest != _manifest_contract():
            raise _files.FixtureAdapterError("atlas-lookup/manifest-binding-invalid", tuple(checks))
        checks.append("atlas_manifest_closed_binding")
        payloads: dict[str, bytes] = {}
        parsed: dict[str, object] = {}
        for role, path, digest in _ARTIFACTS:
            raw = _read(PurePosixPath(path), role, checks)
            if f"sha256:{hashlib.sha256(raw).hexdigest()}" != digest:
                raise _files.FixtureAdapterError("atlas-lookup/digest-mismatch", tuple(checks))
            checks.append(f"atlas_{role}_byte_digest")
            parsed[role] = loads_bounded(raw)
            payloads[role] = raw
        if not _binding_matches(parsed["carrier"], parsed["reference"], parsed["bundle"]):
            raise _files.FixtureAdapterError("atlas-lookup/packet-binding-invalid", tuple(checks))
        checks.append("atlas_identity_scope_time_binding")
    except _files.FixtureAdapterError as exc:
        return AtlasFixtureLookup("ERROR", None, tuple(checks), (exc.code,))
    except BoundedJSONError:
        return AtlasFixtureLookup("ERROR", None, tuple(checks), ("atlas-lookup/json-invalid",))
    packet = AtlasFixturePacket(
        CANDIDATE_ID, SUBJECT_REF, EVIDENCE_REF, FEATURE_ID, TIME_START, TIME_END,
        payloads["carrier"], payloads["reference"], payloads["bundle"],
    )
    return AtlasFixtureLookup("FOUND", packet, tuple(checks), ())
