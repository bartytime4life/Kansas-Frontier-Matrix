#!/usr/bin/env python3
"""Validate the frozen synthetic consent-safe genealogy-overlay profile.

This fixture-only validator proves bounded consent, revocation, evidence,
privacy, deterministic-hash, and non-release behavior. It never validates real
people, DNA, consent, rights, policy approval, release, or publication.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    find_undeclared_fields,
    is_nonempty_string,
    serialize_result,
    validate_fixture_file,
)

PROFILE_ID = "kfm-people-dna-land-consent-overlay-fixture-v1"
REVOCATION_PROFILE_ID = "kfm-people-dna-land-genealogy-overlay-revocation-manifest-v1"
OBJECT_FAMILY = "ConsentedGenealogyOverlayCandidate"
SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
FIXTURE_RE = re.compile(r"^fixture://[a-z0-9][a-z0-9._~:/-]*$")
FIPS_RE = re.compile(r"^[0-9]{5}$")

TOP_FIELDS = frozenset({
    "fixture_id", "profile_id", "object_family", "overlay_id", "spec_hash",
    "evaluation_time", "material_kind", "subject_posture", "source_role",
    "kit_hash", "kit_salt_version", "consent", "revocation_root", "events",
    "evidence_refs", "disclosure_level", "governance", "limitations",
})
CONSENT_FIELDS = frozenset({
    "status", "token_hash", "issued_at", "expires_at", "revocation_ref",
    "scope", "audience",
})
EVENT_FIELDS = frozenset({
    "event_type", "time_bucket", "place_bucket",
    "non_identifying_match_score", "evidence_refs",
})
TIME_FIELDS = frozenset({"start", "end"})
PLACE_FIELDS = frozenset({"county_fips", "precision"})
GOV_FIELDS = frozenset({
    "rights_state", "sensitivity_state", "review_state", "release_state",
    "promotion_eligible", "public_exposure", "rollback_state",
})
MANIFEST_FIELDS = frozenset({
    "profile_id", "manifest_id", "spec_hash", "revocation_root",
    "generated_at", "revoked_overlay_ids", "source_posture", "release_state",
})
EXPECTED_GOV = {
    "rights_state": "fixture_only",
    "sensitivity_state": "restricted_fixture",
    "review_state": "fixture_only",
    "release_state": "not_released",
    "promotion_eligible": False,
    "public_exposure": False,
    "rollback_state": "fixture_only",
}
EXPECTED_LIMITATIONS = frozenset({
    "no_identity_proof", "no_kinship_proof", "no_person_parcel_link",
    "no_raw_genomic_material", "not_released", "synthetic_fixture_only",
})
SCOPES = frozenset({
    "derived_match_summary", "historical_context",
    "restricted_genealogy_overlay",
})
EVENT_TYPES = frozenset({
    "match_hint", "shared_ancestor", "lineage_cluster", "tree_link",
})
RAW_KEYS = frozenset({
    "dna_segments", "genotype", "raw_dna", "raw_genotype", "sequence",
    "triangulation",
})
LOCATION_KEYS = frozenset({
    "address", "coordinates", "lat", "latitude", "lon", "longitude",
    "street_address",
})
KIT_KEYS = frozenset({"kit_id", "vendor_kit_id"})
IDENTIFYING_KEYS = frozenset({
    "birth_date", "death_date", "email", "full_name", "name", "parcel_id",
    "person_id", "person_name", "phone", "ssn",
})


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")


def overlay_spec_hash(candidate: Mapping[str, Any]) -> str:
    payload = {k: v for k, v in candidate.items() if k != "spec_hash"}
    return "sha256:" + hashlib.sha256(_canonical_json(payload)).hexdigest()


def revocation_manifest_spec_hash(candidate: Mapping[str, Any]) -> str:
    payload = {k: v for k, v in candidate.items() if k != "spec_hash"}
    return "sha256:" + hashlib.sha256(_canonical_json(payload)).hexdigest()


def _sha(value: object) -> bool:
    return isinstance(value, str) and SHA256_RE.fullmatch(value) is not None


def _fixture(value: object) -> bool:
    return isinstance(value, str) and FIXTURE_RE.fullmatch(value) is not None


def _datetime(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed.astimezone(timezone.utc) if parsed.tzinfo else None


def _date(value: object) -> date | None:
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _refs(value: object, maximum: int = 32) -> bool:
    return (
        isinstance(value, list) and bool(value) and len(value) <= maximum
        and all(_fixture(item) for item in value)
        and len(value) == len(set(value))
    )


def _scan(value: object, path: str, findings: set[Finding]) -> None:
    if isinstance(value, dict):
        for key in sorted(value, key=lambda item: (type(item).__name__, repr(item))):
            child = f"{path}.{key}"
            if isinstance(key, str):
                normalized = key.casefold()
                if normalized in RAW_KEYS:
                    add_finding(findings, "RAW_GENOMIC_MATERIAL_DENIED", child)
                elif normalized in LOCATION_KEYS:
                    add_finding(findings, "SENSITIVE_LOCATION_DENIED", child)
                elif normalized in KIT_KEYS:
                    add_finding(findings, "IDENTIFYING_KIT_FIELD_DENIED", child)
                elif normalized in IDENTIFYING_KEYS:
                    add_finding(findings, "IDENTIFYING_FIELD_DENIED", child)
            _scan(value[key], child, findings)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _scan(item, f"{path}[{index}]", findings)


def _consent(candidate: Mapping[str, Any], evaluation: datetime | None, findings: set[Finding]) -> None:
    consent = candidate.get("consent")
    if not isinstance(consent, dict):
        add_finding(findings, "CONSENT_INVALID", "$.consent")
        return
    find_undeclared_fields(findings, consent, CONSENT_FIELDS, "UNDECLARED_CONSENT_FIELD", "$.consent")
    status = consent.get("status")
    subject = candidate.get("subject_posture")
    material = candidate.get("material_kind")
    if status not in {"active", "revoked", "expired", "not_required"}:
        add_finding(findings, "CONSENT_STATUS_INVALID", "$.consent.status")
        return
    if subject == "living_person" and status != "active":
        add_finding(findings, "CONSENT_REQUIRED_FOR_LIVING_PERSON", "$.consent.status")
    if material == "dna_derived_summary" and status != "active":
        add_finding(findings, "CONSENT_REQUIRED_FOR_DNA_DERIVATIVE", "$.consent.status")
    if status == "not_required" and not (
        subject == "deceased_or_historical" and material == "documentary_genealogy_context"
    ):
        add_finding(findings, "CONSENT_NOT_REQUIRED_INVALID", "$.consent.status")
    scope = consent.get("scope")
    if not (
        isinstance(scope, list) and bool(scope) and len(scope) <= 8
        and all(item in SCOPES for item in scope) and len(scope) == len(set(scope))
    ):
        add_finding(findings, "CONSENT_SCOPE_INVALID", "$.consent.scope")
    if consent.get("audience") != "restricted_steward":
        add_finding(findings, "CONSENT_AUDIENCE_INVALID", "$.consent.audience")
    if status == "active":
        issued = _datetime(consent.get("issued_at"))
        expires = _datetime(consent.get("expires_at"))
        if not _sha(consent.get("token_hash")):
            add_finding(findings, "CONSENT_TOKEN_HASH_INVALID", "$.consent.token_hash")
        if issued is None:
            add_finding(findings, "CONSENT_ISSUED_AT_INVALID", "$.consent.issued_at")
        if expires is None:
            add_finding(findings, "CONSENT_EXPIRES_AT_INVALID", "$.consent.expires_at")
        if issued and expires and issued >= expires:
            add_finding(findings, "CONSENT_INTERVAL_INVALID", "$.consent")
        if evaluation and issued and evaluation < issued:
            add_finding(findings, "CONSENT_NOT_YET_ACTIVE", "$.consent.issued_at")
        if evaluation and expires and evaluation >= expires:
            add_finding(findings, "CONSENT_EXPIRED", "$.consent.expires_at")
    elif status == "revoked":
        add_finding(findings, "REVOCATION_ACTIVE", "$.consent.status")
    elif status == "expired":
        add_finding(findings, "CONSENT_EXPIRED", "$.consent.status")


def _events(value: object, findings: set[Finding]) -> None:
    if not isinstance(value, list) or not value or len(value) > 16:
        add_finding(findings, "EVENTS_INVALID", "$.events")
        return
    for index, event in enumerate(value):
        base = f"$.events[{index}]"
        if not isinstance(event, dict):
            add_finding(findings, "EVENT_INVALID", base)
            continue
        find_undeclared_fields(findings, event, EVENT_FIELDS, "UNDECLARED_EVENT_FIELD", base)
        if event.get("event_type") not in EVENT_TYPES:
            add_finding(findings, "EVENT_TYPE_INVALID", f"{base}.event_type")
        refs = event.get("evidence_refs")
        if not _refs(refs):
            add_finding(findings, "EVIDENCE_REFS_INVALID", f"{base}.evidence_refs")
        score = event.get("non_identifying_match_score")
        if not isinstance(score, (int, float)) or isinstance(score, bool) or not 0 <= score <= 1:
            add_finding(findings, "MATCH_SCORE_INVALID", f"{base}.non_identifying_match_score")
        elif score >= 0.9 and (not isinstance(refs, list) or len(refs) < 2):
            add_finding(findings, "HIGH_CONFIDENCE_EVIDENCE_INSUFFICIENT", f"{base}.evidence_refs")
        time_bucket = event.get("time_bucket")
        if not isinstance(time_bucket, dict):
            add_finding(findings, "TIME_BUCKET_INVALID", f"{base}.time_bucket")
        else:
            find_undeclared_fields(findings, time_bucket, TIME_FIELDS, "UNDECLARED_TIME_FIELD", f"{base}.time_bucket")
            start, end = _date(time_bucket.get("start")), _date(time_bucket.get("end"))
            if start is None or end is None or start > end:
                add_finding(findings, "TIME_BUCKET_INVALID", f"{base}.time_bucket")
            elif end.year >= 1900 and (end - start).days < 3652:
                add_finding(findings, "RECENT_TIME_BUCKET_TOO_PRECISE", f"{base}.time_bucket")
        place = event.get("place_bucket")
        if not isinstance(place, dict):
            add_finding(findings, "PLACE_BUCKET_INVALID", f"{base}.place_bucket")
        else:
            find_undeclared_fields(findings, place, PLACE_FIELDS, "UNDECLARED_PLACE_FIELD", f"{base}.place_bucket")
            if place.get("precision") not in {"coarse", "county", "state"}:
                add_finding(findings, "PLACE_PRECISION_INVALID", f"{base}.place_bucket.precision")
            county = place.get("county_fips")
            if not isinstance(county, str) or FIPS_RE.fullmatch(county) is None:
                add_finding(findings, "COUNTY_FIPS_INVALID", f"{base}.place_bucket.county_fips")
            elif county != "99999":
                add_finding(findings, "NON_SYNTHETIC_COUNTY_DENIED", f"{base}.place_bucket.county_fips")


def validate_revocation_manifest(candidate: object) -> list[Finding]:
    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("REVOCATION_MANIFEST_NOT_OBJECT", "$")]
    find_undeclared_fields(findings, candidate, MANIFEST_FIELDS, "UNDECLARED_MANIFEST_FIELD", "$")
    if candidate.get("profile_id") != REVOCATION_PROFILE_ID:
        add_finding(findings, "MANIFEST_PROFILE_ID_INVALID", "$.profile_id")
    if not _fixture(candidate.get("manifest_id")):
        add_finding(findings, "MANIFEST_ID_INVALID", "$.manifest_id")
    if not _sha(candidate.get("revocation_root")):
        add_finding(findings, "REVOCATION_ROOT_INVALID", "$.revocation_root")
    if _datetime(candidate.get("generated_at")) is None:
        add_finding(findings, "MANIFEST_TIME_INVALID", "$.generated_at")
    revoked = candidate.get("revoked_overlay_ids")
    if not (
        isinstance(revoked, list) and len(revoked) <= 128
        and all(_sha(item) for item in revoked) and len(revoked) == len(set(revoked))
    ):
        add_finding(findings, "REVOKED_OVERLAY_IDS_INVALID", "$.revoked_overlay_ids")
    if candidate.get("source_posture") != "fixture_only":
        add_finding(findings, "MANIFEST_SOURCE_POSTURE_INVALID", "$.source_posture")
    if candidate.get("release_state") != "not_released":
        add_finding(findings, "MANIFEST_RELEASE_STATE_INVALID", "$.release_state")
    spec_hash = candidate.get("spec_hash")
    if not _sha(spec_hash):
        add_finding(findings, "MANIFEST_SPEC_HASH_INVALID", "$.spec_hash")
    elif spec_hash != revocation_manifest_spec_hash(candidate):
        add_finding(findings, "MANIFEST_SPEC_HASH_MISMATCH", "$.spec_hash")
    _scan(candidate, "$", findings)
    return sorted(findings)


def load_revocation_manifest(path: Path | str) -> tuple[dict[str, Any] | None, list[Finding]]:
    captured: dict[str, object] = {}
    def validate(candidate: object) -> list[Finding]:
        captured["candidate"] = candidate
        return validate_revocation_manifest(candidate)
    findings = validate_fixture_file(path, validate)
    candidate = captured.get("candidate")
    if findings or not isinstance(candidate, dict):
        return None, findings or [Finding("REVOCATION_MANIFEST_NOT_OBJECT", "$")]
    return candidate, []


def validate_candidate(candidate: object, *, revocation_manifest: Mapping[str, Any] | None) -> list[Finding]:
    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("CANDIDATE_NOT_OBJECT", "$")]
    find_undeclared_fields(findings, candidate, TOP_FIELDS, "UNDECLARED_TOP_LEVEL_FIELD", "$")
    if not _fixture(candidate.get("fixture_id")):
        add_finding(findings, "FIXTURE_ID_INVALID", "$.fixture_id")
    if candidate.get("profile_id") != PROFILE_ID:
        add_finding(findings, "PROFILE_ID_INVALID", "$.profile_id")
    if candidate.get("object_family") != OBJECT_FAMILY:
        add_finding(findings, "OBJECT_FAMILY_INVALID", "$.object_family")
    if not _sha(candidate.get("overlay_id")):
        add_finding(findings, "OVERLAY_ID_INVALID", "$.overlay_id")
    if candidate.get("source_role") != "fixture_only":
        add_finding(findings, "SOURCE_ROLE_INVALID", "$.source_role")
    if candidate.get("subject_posture") == "unknown":
        add_finding(findings, "SUBJECT_POSTURE_UNRESOLVED", "$.subject_posture")
    if candidate.get("disclosure_level") not in {"restricted", "internal"}:
        add_finding(findings, "DISCLOSURE_LEVEL_INVALID", "$.disclosure_level")
    evaluation = _datetime(candidate.get("evaluation_time"))
    if evaluation is None:
        add_finding(findings, "EVALUATION_TIME_INVALID", "$.evaluation_time")
    material = candidate.get("material_kind")
    if material == "dna_derived_summary":
        if not _sha(candidate.get("kit_hash")):
            add_finding(findings, "KIT_HASH_INVALID", "$.kit_hash")
        if candidate.get("kit_salt_version") != "fixture-v1":
            add_finding(findings, "KIT_SALT_VERSION_INVALID", "$.kit_salt_version")
    elif material == "documentary_genealogy_context":
        if candidate.get("kit_hash") is not None:
            add_finding(findings, "KIT_HASH_NOT_ALLOWED", "$.kit_hash")
        if candidate.get("kit_salt_version") is not None:
            add_finding(findings, "KIT_SALT_VERSION_NOT_ALLOWED", "$.kit_salt_version")
    else:
        add_finding(findings, "MATERIAL_KIND_INVALID", "$.material_kind")
    _consent(candidate, evaluation, findings)
    if not _sha(candidate.get("revocation_root")):
        add_finding(findings, "REVOCATION_ROOT_INVALID", "$.revocation_root")
    if revocation_manifest is None:
        add_finding(findings, "REVOCATION_MANIFEST_REQUIRED", "$.revocation_root")
    else:
        if candidate.get("revocation_root") != revocation_manifest.get("revocation_root"):
            add_finding(findings, "REVOCATION_ROOT_MISMATCH", "$.revocation_root")
        revoked = revocation_manifest.get("revoked_overlay_ids")
        if isinstance(revoked, list) and candidate.get("overlay_id") in revoked:
            add_finding(findings, "REVOCATION_ACTIVE", "$.overlay_id")
    _events(candidate.get("events"), findings)
    if not _refs(candidate.get("evidence_refs")):
        add_finding(findings, "EVIDENCE_REFS_INVALID", "$.evidence_refs")
    governance = candidate.get("governance")
    if not isinstance(governance, dict):
        add_finding(findings, "GOVERNANCE_INVALID", "$.governance")
    else:
        find_undeclared_fields(findings, governance, GOV_FIELDS, "UNDECLARED_GOVERNANCE_FIELD", "$.governance")
        for field, expected in EXPECTED_GOV.items():
            if governance.get(field) != expected:
                add_finding(findings, "GOVERNANCE_STATE_INVALID", f"$.governance.{field}")
    limitations = candidate.get("limitations")
    if not (
        isinstance(limitations, list) and len(limitations) == len(EXPECTED_LIMITATIONS)
        and all(is_nonempty_string(item) for item in limitations)
        and set(limitations) == EXPECTED_LIMITATIONS
    ):
        add_finding(findings, "LIMITATIONS_INVALID", "$.limitations")
    spec_hash = candidate.get("spec_hash")
    if not _sha(spec_hash):
        add_finding(findings, "SPEC_HASH_INVALID", "$.spec_hash")
    elif spec_hash != overlay_spec_hash(candidate):
        add_finding(findings, "SPEC_HASH_MISMATCH", "$.spec_hash")
    _scan(candidate, "$", findings)
    return sorted(findings)


def validate_file(path: Path | str, *, revocation_manifest: Mapping[str, Any] | None) -> list[Finding]:
    return validate_fixture_file(
        path,
        lambda candidate: validate_candidate(candidate, revocation_manifest=revocation_manifest),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate synthetic consent-safe genealogy-overlay fixtures.")
    parser.add_argument("--revocation-manifest", required=True, type=Path)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)
    manifest, findings = load_revocation_manifest(args.revocation_manifest)
    if findings:
        print(serialize_result("people-dna-land-genealogy-overlay-revocation-manifest", args.revocation_manifest, findings))
        return 1
    failed = False
    for path in sorted(args.files, key=str):
        findings = validate_file(path, revocation_manifest=manifest)
        failed = failed or bool(findings)
        print(serialize_result("people-dna-land-consent-overlay-fixture", path, findings))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
