#!/usr/bin/env python3
"""Validate deterministically identified, non-authoritative KFM BriefingSignals.

A passing signal is discovery and routing metadata only. It cannot admit a source,
mutate the repository, construct proof, release, deploy, publish, or serve public
truth. Parsing, identity reproduction, routing checks, and output are deterministic
and no-network.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    validate_fixture_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/briefing_signal.schema.json"
SCOPE = "briefing-signal-discovery-only"
IDENTITY_ALGORITHM = "kfm-briefing-identity-v1"
OPEN_ISSUE_DISPOSITIONS = frozenset(
    {"OPEN_SOURCE_DISCOVERY_ISSUE", "OPEN_OBJECT_MODEL_ISSUE"}
)
MATCH_REASON_CODES = frozenset(
    {
        "EVENT_CLUSTER_ID_MATCH",
        "NATIVE_ID_MATCH",
        "EXISTING_KFM_LINK_MATCH",
        "AUTHORITY_PLACE_TYPE_MATCH",
        "IDEMPOTENT_REPLAY",
    }
)
INLINE_GEOMETRY_KEYS = frozenset(
    {
        "geometry",
        "coordinates",
        "latitude",
        "longitude",
        "lat",
        "lon",
        "lng",
        "bbox",
        "centroid",
        "easting",
        "northing",
        "x",
        "y",
    }
)
TRUST_BEARING_TRUE_KEYS = frozenset(
    {
        "approved",
        "admitted",
        "released",
        "published",
        "public",
        "promotion_eligible",
        "source_active",
    }
)
SECRET_LIKE_KEYS = frozenset(
    {
        "api_key",
        "authorization",
        "cookie",
        "credential",
        "password",
        "secret",
        "token",
    }
)
WHITESPACE_RE = re.compile(r"\s+")


def _normalize_text(value: str) -> str:
    return WHITESPACE_RE.sub(" ", unicodedata.normalize("NFKC", value).strip())


def normalize_identity_token(value: str) -> str:
    """Normalize one stable identity token without guessing semantic aliases."""

    return _normalize_text(value).casefold().replace(" ", "-")


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _normalized_generic(value: object) -> object:
    if isinstance(value, Mapping):
        return {
            str(key): _normalized_generic(value[key])
            for key in sorted(value, key=lambda item: str(item))
        }
    if isinstance(value, list):
        normalized = [_normalized_generic(item) for item in value]
        return sorted(normalized, key=lambda item: _canonical_bytes(item))
    if isinstance(value, str):
        return _normalize_text(value)
    return value


def _signal_projection(candidate: Mapping[str, Any]) -> dict[str, object]:
    geographic_scope = candidate.get("geographic_scope")
    geographic_projection: object = geographic_scope
    if isinstance(geographic_scope, Mapping):
        geographic_projection = {
            "kind": geographic_scope.get("kind"),
            "identifiers": sorted(
                _normalize_text(str(item))
                for item in geographic_scope.get("identifiers", [])
            )
            if isinstance(geographic_scope.get("identifiers"), list)
            else geographic_scope.get("identifiers"),
            "geometry_ref": geographic_scope.get("geometry_ref"),
            "geometry_status": geographic_scope.get("geometry_status"),
        }

    claims_projection: list[object] = []
    claims = candidate.get("claims")
    if isinstance(claims, list):
        for claim in claims:
            if not isinstance(claim, Mapping):
                claims_projection.append(_normalized_generic(claim))
                continue
            refs = claim.get("evidence_refs")
            claims_projection.append(
                {
                    "claim_id": claim.get("claim_id"),
                    "text": _normalize_text(str(claim.get("text", ""))),
                    "truth_label": claim.get("truth_label"),
                    "evidence_refs": sorted(str(item) for item in refs)
                    if isinstance(refs, list)
                    else refs,
                }
            )
        claims_projection.sort(key=lambda item: _canonical_bytes(item))

    source_projection: list[object] = []
    sources = candidate.get("official_source_candidates")
    if isinstance(sources, list):
        for source in sources:
            if not isinstance(source, Mapping):
                source_projection.append(_normalized_generic(source))
                continue
            source_projection.append(
                {
                    "source_kind": source.get("source_kind"),
                    "authority_name": _normalize_text(
                        str(source.get("authority_name", ""))
                    ),
                    "locator": _normalize_text(str(source.get("locator", ""))),
                }
            )
        source_projection.sort(key=lambda item: _canonical_bytes(item))

    domains = candidate.get("domains")
    families = candidate.get("proposed_object_families")
    return {
        "identity_profile": IDENTITY_ALGORITHM,
        "briefing_date": candidate.get("briefing_date"),
        "headline": _normalize_text(str(candidate.get("headline", ""))),
        "story_type": candidate.get("story_type"),
        "domains": sorted(str(item) for item in domains)
        if isinstance(domains, list)
        else domains,
        "geographic_scope": geographic_projection,
        "claims": claims_projection,
        "official_source_candidates": source_projection,
        "proposed_object_families": sorted(str(item) for item in families)
        if isinstance(families, list)
        else families,
        "candidate_payload": _normalized_generic(candidate.get("candidate_payload")),
    }


def compute_signal_digest(candidate: Mapping[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(
        _canonical_bytes(_signal_projection(candidate))
    ).hexdigest()


def compute_signal_id(candidate: Mapping[str, Any]) -> str:
    digest = compute_signal_digest(candidate).removeprefix("sha256:")
    return f"kfm:briefing-signal:{candidate.get('briefing_date')}:{digest[:24]}"


def compute_event_cluster_id(candidate: Mapping[str, Any]) -> str:
    identity = candidate.get("identity")
    if not isinstance(identity, Mapping):
        identity = {}
    projection = {
        "story_type": candidate.get("story_type"),
        "primary_authority_id": normalize_identity_token(
            str(identity.get("primary_authority_id", ""))
        ),
        "native_id_or_identity_key": normalize_identity_token(
            str(identity.get("native_id_or_identity_key", ""))
        ),
        "geography_identity": normalize_identity_token(
            str(identity.get("geography_identity", ""))
        ),
        "durable_subject_key": normalize_identity_token(
            str(identity.get("durable_subject_key", ""))
        ),
    }
    digest = hashlib.sha256(_canonical_bytes(projection)).hexdigest()
    return f"kfm:event-cluster:{candidate.get('story_type')}:{digest[:24]}"


def compute_issue_idempotency_key(candidate: Mapping[str, Any]) -> str:
    next_action = candidate.get("next_action")
    if not isinstance(next_action, Mapping):
        next_action = {}
    existing_links = candidate.get("existing_kfm_links")
    if not isinstance(existing_links, Mapping):
        existing_links = {}
    deduplication = candidate.get("deduplication")
    if not isinstance(deduplication, Mapping):
        deduplication = {}
    projection = {
        "event_cluster_id": candidate.get("event_cluster_id"),
        "disposition": next_action.get("disposition"),
        "scope": _normalize_text(str(next_action.get("scope", ""))),
        "existing_issue_ids": sorted(existing_links.get("issues", []))
        if isinstance(existing_links.get("issues"), list)
        else existing_links.get("issues"),
        "matched_issue_ids": sorted(deduplication.get("matched_issue_ids", []))
        if isinstance(deduplication.get("matched_issue_ids"), list)
        else deduplication.get("matched_issue_ids"),
    }
    return "sha256:" + hashlib.sha256(_canonical_bytes(projection)).hexdigest()


def _load_schema() -> Mapping[str, object]:
    payload = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(payload)
    return payload


def _json_path(parts: Sequence[object]) -> str:
    if not parts:
        return "$"
    return "$." + ".".join(str(part) for part in parts)


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code=code, path=path))


def _walk(value: object, path: tuple[object, ...] = ()):  # noqa: ANN202
    if isinstance(value, Mapping):
        for key in sorted(value, key=str):
            child_path = (*path, key)
            yield child_path, key, value[key]
            yield from _walk(value[key], child_path)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            child_path = (*path, index)
            yield child_path, index, item
            yield from _walk(item, child_path)


def _validate_identity(candidate: Mapping[str, Any], findings: set[Finding]) -> None:
    identity = candidate.get("identity")
    if not isinstance(identity, Mapping):
        return
    for field in (
        "primary_authority_id",
        "native_id_or_identity_key",
        "geography_identity",
        "durable_subject_key",
    ):
        value = identity.get(field)
        if isinstance(value, str) and normalize_identity_token(value) != value:
            _add(findings, "IDENTITY_TOKEN_NOT_NORMALIZED", f"$.identity.{field}")

    if identity.get("algorithm") == IDENTITY_ALGORITHM:
        expected_digest = compute_signal_digest(candidate)
        if identity.get("signal_digest") != expected_digest:
            _add(findings, "SIGNAL_DIGEST_MISMATCH", "$.identity.signal_digest")
        if candidate.get("signal_id") != compute_signal_id(candidate):
            _add(findings, "SIGNAL_ID_MISMATCH", "$.signal_id")
        if candidate.get("event_cluster_id") != compute_event_cluster_id(candidate):
            _add(findings, "EVENT_CLUSTER_ID_MISMATCH", "$.event_cluster_id")


def _validate_deduplication(candidate: Mapping[str, Any], findings: set[Finding]) -> None:
    dedup = candidate.get("deduplication")
    next_action = candidate.get("next_action")
    links = candidate.get("existing_kfm_links")
    if not isinstance(dedup, Mapping) or not isinstance(next_action, Mapping):
        return
    matched_signals = dedup.get("matched_signal_ids")
    matched_issues = dedup.get("matched_issue_ids")
    reasons = dedup.get("reason_codes")
    status = dedup.get("status")
    signal_status = candidate.get("status")
    disposition = next_action.get("disposition")

    if isinstance(matched_signals, list) and candidate.get("signal_id") in matched_signals:
        _add(findings, "SELF_DUPLICATE_REFERENCE_FORBIDDEN", "$.deduplication.matched_signal_ids")

    if status == "UNIQUE":
        if matched_signals or matched_issues:
            _add(findings, "UNIQUE_SIGNAL_HAS_MATCHES", "$.deduplication")
        if not isinstance(reasons, list) or "NEW_CLUSTER" not in reasons:
            _add(findings, "UNIQUE_SIGNAL_REASON_INVALID", "$.deduplication.reason_codes")
    elif status == "DUPLICATE":
        if not matched_signals and not matched_issues:
            _add(findings, "DUPLICATE_MATCH_REQUIRED", "$.deduplication")
        if not isinstance(reasons, list) or not (set(reasons) & MATCH_REASON_CODES):
            _add(findings, "DUPLICATE_REASON_INVALID", "$.deduplication.reason_codes")
        if disposition in OPEN_ISSUE_DISPOSITIONS:
            _add(findings, "DUPLICATE_CANNOT_OPEN_ISSUE", "$.next_action.disposition")
    elif status == "CONFLICTED":
        if not isinstance(reasons, list) or "IDENTITY_CONFLICT" not in reasons:
            _add(findings, "CONFLICT_REASON_REQUIRED", "$.deduplication.reason_codes")

    if signal_status == "DUPLICATE" and status != "DUPLICATE":
        _add(findings, "SIGNAL_DEDUP_STATUS_MISMATCH", "$.deduplication.status")
    if status == "DUPLICATE" and signal_status != "DUPLICATE":
        _add(findings, "SIGNAL_DEDUP_STATUS_MISMATCH", "$.status")
    if signal_status == "CONFLICTED" and status != "CONFLICTED":
        _add(findings, "SIGNAL_DEDUP_STATUS_MISMATCH", "$.deduplication.status")
    if status == "CONFLICTED" and signal_status != "CONFLICTED":
        _add(findings, "SIGNAL_DEDUP_STATUS_MISMATCH", "$.status")

    existing_issues = links.get("issues") if isinstance(links, Mapping) else None
    if isinstance(matched_issues, list) and isinstance(existing_issues, list):
        if not set(matched_issues).issubset(existing_issues):
            _add(findings, "MATCHED_ISSUE_NOT_LINKED", "$.deduplication.matched_issue_ids")
    if disposition == "UPDATE_EXISTING_ISSUE":
        if not isinstance(matched_issues, list) or not matched_issues:
            _add(findings, "UPDATE_ISSUE_TARGET_REQUIRED", "$.deduplication.matched_issue_ids")

    expected_key = compute_issue_idempotency_key(candidate)
    if next_action.get("idempotency_key") != expected_key:
        _add(findings, "ISSUE_IDEMPOTENCY_KEY_MISMATCH", "$.next_action.idempotency_key")


def _validate_time(candidate: Mapping[str, Any], findings: set[Finding]) -> None:
    briefing_date = candidate.get("briefing_date")
    expires_at = candidate.get("expires_at")
    if not isinstance(briefing_date, str) or not isinstance(expires_at, str):
        return
    try:
        briefing = date.fromisoformat(briefing_date)
        expiry = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
    except ValueError:
        return
    if expiry.date() < briefing:
        _add(findings, "SIGNAL_EXPIRY_PRECEDES_BRIEFING", "$.expires_at")


def _validate_payload(candidate: Mapping[str, Any], findings: set[Finding]) -> None:
    payload = candidate.get("candidate_payload")
    if not isinstance(payload, Mapping):
        return
    attributes = payload.get("attributes")
    if not isinstance(attributes, Mapping):
        return
    for path, key, value in _walk(attributes):
        dotted = "$.candidate_payload.attributes." + ".".join(str(part) for part in path)
        if isinstance(key, str):
            normalized_key = key.casefold()
            if normalized_key in INLINE_GEOMETRY_KEYS:
                _add(findings, "INLINE_GEOMETRY_FORBIDDEN", dotted)
            if normalized_key in SECRET_LIKE_KEYS:
                _add(findings, "SECRET_LIKE_FIELD_FORBIDDEN", dotted)
            if normalized_key in TRUST_BEARING_TRUE_KEYS and value is True:
                _add(findings, "TRUST_BEARING_STATE_FORBIDDEN", dotted)


def validate_candidate(candidate: object) -> list[Finding]:
    findings: set[Finding] = set()
    if not isinstance(candidate, Mapping):
        return [Finding("DOCUMENT_NOT_OBJECT", "$")]

    try:
        schema = _load_schema()
    except (OSError, UnicodeError, ValueError):
        return [Finding("BRIEFING_SIGNAL_SCHEMA_UNAVAILABLE", "$")]

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(validator.iter_errors(candidate), key=lambda item: list(item.path)):
        _add(findings, "BRIEFING_SIGNAL_SCHEMA_INVALID", _json_path(tuple(error.path)))

    claims = candidate.get("claims")
    if isinstance(claims, list):
        for index, claim in enumerate(claims):
            if isinstance(claim, Mapping):
                if claim.get("truth_label") == "CONFIRMED" and not claim.get("evidence_refs"):
                    _add(
                        findings,
                        "CONFIRMED_CLAIM_WITHOUT_EVIDENCE",
                        f"$.claims.{index}.evidence_refs",
                    )

    if candidate.get("public_use_allowed") is not False:
        _add(findings, "PUBLIC_USE_MUST_REMAIN_FALSE", "$.public_use_allowed")

    permissions = candidate.get("permissions")
    if isinstance(permissions, Mapping):
        for field in (
            "source_activation",
            "proof_construction",
            "release",
            "deployment",
            "publication",
        ):
            if permissions.get(field) is not False:
                _add(findings, "CONSEQUENTIAL_PERMISSION_FORBIDDEN", f"$.permissions.{field}")

    next_action = candidate.get("next_action")
    if isinstance(next_action, Mapping):
        if next_action.get("repository_mutation_allowed") is not False:
            _add(
                findings,
                "REPOSITORY_MUTATION_PERMISSION_FORBIDDEN",
                "$.next_action.repository_mutation_allowed",
            )

    _validate_identity(candidate, findings)
    _validate_deduplication(candidate, findings)
    _validate_time(candidate, findings)
    _validate_payload(candidate, findings)
    return sorted(findings)


def load_candidate(path: Path | str) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    captured: dict[str, object] = {}

    def _capture(candidate: object) -> list[Finding]:
        captured["candidate"] = candidate
        return validate_candidate(candidate)

    raw_findings = validate_fixture_file(path, _capture)
    findings: list[Finding] = []
    for finding in raw_findings:
        if finding.code == "FIXTURE_TOO_LARGE":
            findings.append(Finding("BRIEFING_SIGNAL_TOO_LARGE", finding.path))
        elif finding.code == "FIXTURE_JSON_INVALID":
            findings.append(Finding("BRIEFING_SIGNAL_JSON_INVALID", finding.path))
        else:
            findings.append(finding)
    candidate = captured.get("candidate")
    if not isinstance(candidate, dict):
        return None, tuple(sorted(findings))
    return candidate, tuple(sorted(findings))


def validate_file(path: Path | str) -> tuple[Finding, ...]:
    _candidate, findings = load_candidate(path)
    return findings


def serialize_result(path: Path, findings: Sequence[Finding]) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in sorted(findings)
            ],
            "outcome": "PASS" if not findings else "FAIL",
            "scope": SCOPE,
            "authority_created": False,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate non-authoritative, deterministically identified KFM BriefingSignals."
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        findings = validate_file(path)
        print(serialize_result(path, findings))
        failed = failed or bool(findings)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
