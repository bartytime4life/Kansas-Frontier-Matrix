#!/usr/bin/env python3
"""Support fixture-only AdvisoryEventEnvelope validation without network access.

The envelope provides shared mechanics for volatile advisories while the
referenced domain payload remains authoritative for native meaning. A green
result proves bounded shape, local payload binding, finite status mapping,
false-clear defenses, time/scope consistency, and release-neutral controls.
It does not fetch a source, authenticate evidence, evaluate policy, issue an
alert, write lifecycle state, release, deploy, publish, or authorize public use.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import stat
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))
from tools.validators._common.local_resolver import build_registry

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/advisory_event_envelope.schema.json"
PAYLOAD_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/hazards/kdhe_hab_advisory_snapshot.schema.json"
FIXTURE_CASES = REPO_ROOT / "fixtures/contracts/v1/common/advisory_event_envelope/cases.json"
FIXTURE_ROOT = FIXTURE_CASES.parent
FIXTURE_BASES_ROOT = FIXTURE_ROOT / "bases"
MAX_FILE_BYTES = 1_048_576
MAX_DEPTH = 64
MAX_SCHEMA_FINDINGS = 100
SCOPE = "fixture-only-advisory-event-envelope-and-local-domain-payload-binding"
PAYLOAD_ROOT = Path("fixtures/domains/hazards/kdhe_hab_advisory_snapshot/valid")
ERROR_CODES = frozenset({
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE", "INPUT_SYMLINK_DENIED",
    "INPUT_NOT_REGULAR_FILE", "JSON_COMPLEXITY_LIMIT", "JSON_DUPLICATE_KEY",
    "JSON_INVALID", "JSON_NONFINITE_NUMBER", "JSON_NOT_UTF8", "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE", "SCHEMA_EVALUATION_LIMIT", "PAYLOAD_FILE_UNSAFE",
    "PAYLOAD_SCHEMA_UNAVAILABLE", "FIXTURE_MANIFEST_INVALID",
    "FIXTURE_CASE_INVALID", "FIXTURE_PATCH_INVALID",
    "FIXTURE_BASE_FILE_INVALID",
})
CLEAR_STATES = frozenset({"RESCINDED", "EXPIRED", "CANCELLED"})
ACTIVE_STATES = frozenset({"ISSUED", "ACTIVE_CONFIRMED", "UPDATED"})
EXPECTED_PAYLOAD_STATUS = {
    "WATCH": "ACTIVE_CONFIRMED",
    "WARNING": "ACTIVE_CONFIRMED",
    "HAZARD": "ACTIVE_CONFIRMED",
    "LIFTED": "RESCINDED",
    "SOURCE_UNAVAILABLE": "STATUS_CHECK_FAILED",
    "STALE_SOURCE": "STATUS_UNCONFIRMED",
    "IDENTITY_UNRESOLVED": "IDENTITY_CONFLICT",
    "GEOMETRY_UNRESOLVED": "GEOMETRY_UNRESOLVED",
    "QUARANTINED": "STATUS_UNCONFIRMED",
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
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(finding.code in ERROR_CODES for finding in self.findings)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _too_deep(text: str) -> bool:
    depth = 0
    in_string = False
    escaped = False
    for char in text:
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char in "[{":
            depth += 1
            if depth > MAX_DEPTH:
                return True
        elif char in "]}":
            depth -= 1
    return False


def _has_symlink_component(path: Path) -> bool:
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current /= part
        if current.is_symlink():
            return True
    return False


def _read_object(path: Path, *, prefix: str = "") -> tuple[dict[str, Any] | None, list[Finding]]:
    unsafe_code = f"{prefix}PAYLOAD_FILE_UNSAFE" if prefix else "INPUT_SYMLINK_DENIED"
    if _has_symlink_component(path):
        return None, [Finding(unsafe_code, "/")]

    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    descriptor: int | None = None
    try:
        descriptor = os.open(path, flags)
        file_stat = os.fstat(descriptor)
        if not stat.S_ISREG(file_stat.st_mode):
            code = "PAYLOAD_FILE_UNSAFE" if prefix else "INPUT_NOT_REGULAR_FILE"
            return None, [Finding(code, "/")]
        if file_stat.st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        chunks: list[bytes] = []
        remaining = MAX_FILE_BYTES + 1
        while remaining:
            block = os.read(descriptor, min(64 * 1024, remaining))
            if not block:
                break
            chunks.append(block)
            remaining -= len(block)
        data = b"".join(chunks)
        if len(data) > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        text = data.decode("utf-8")
    except FileNotFoundError:
        return None, [Finding("FILE_NOT_FOUND", "/")]
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    finally:
        if descriptor is not None:
            os.close(descriptor)

    if _too_deep(text):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    try:
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_validator(path: Path) -> Draft202012Validator:
    schema = json.loads(path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(
        schema,
        registry=build_registry(REPO_ROOT),
        format_checker=FormatChecker(),
    )


def _schema_findings(validator: Draft202012Validator, value: Mapping[str, Any], *, prefix: str = "") -> list[Finding]:
    try:
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (RecursionError, ValueError):
        return [Finding("SCHEMA_EVALUATION_LIMIT", prefix or "/")]
    ordered = sorted(
        errors[:MAX_SCHEMA_FINDINGS],
        key=lambda error: (_pointer(tuple(error.absolute_path)), str(error.validator)),
    )
    findings = [
        Finding(
            "PAYLOAD_SCHEMA_INVALID" if prefix else "SCHEMA_INVALID",
            f"{prefix}{_pointer(tuple(error.absolute_path))}",
        )
        for error in ordered
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", prefix or "/"))
    return findings


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _parse_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed


def canonical_record_digest(value: Mapping[str, Any]) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def canonical_event_id(envelope: Mapping[str, Any]) -> str:
    event = _mapping(envelope.get("event"))
    payload = _mapping(envelope.get("domain_payload"))
    temporal = _mapping(envelope.get("temporal_authority"))
    identity = _mapping(temporal.get("identity"))
    projection = {
        "profile_id": event.get("profile_id"),
        "native_event_id": event.get("native_event_id"),
        "payload_record_digest": payload.get("payload_record_digest"),
        "revision_id": identity.get("revision_id"),
    }
    encoded = json.dumps(projection, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "kfm:advisory:" + hashlib.sha256(encoded).hexdigest()


def _safe_payload_path(value: Any) -> Path | None:
    if not isinstance(value, str):
        return None
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        return None
    if candidate.parts[: len(PAYLOAD_ROOT.parts)] != PAYLOAD_ROOT.parts:
        return None
    resolved = REPO_ROOT / candidate
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError:
        return None
    return resolved


def _temporal_findings(envelope: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    temporal = _mapping(envelope.get("temporal_authority"))
    identity = _mapping(temporal.get("identity"))
    source = _mapping(temporal.get("source"))
    times = _mapping(temporal.get("time"))
    lineage = _mapping(temporal.get("lineage"))

    object_id = identity.get("object_id")
    revision_id = identity.get("revision_id")
    if object_id == revision_id and isinstance(object_id, str):
        findings.append(Finding("REVISION_ID_COLLAPSE", "/temporal_authority/identity/revision_id"))

    source_descriptor_ref = source.get("source_descriptor_ref")
    source_role_ref = source.get("source_role_ref")
    if isinstance(source_descriptor_ref, str) and isinstance(source_role_ref, str):
        if source_role_ref != f"{source_descriptor_ref}#/source_role":
            findings.append(Finding("SOURCE_ROLE_REF_UNBOUND", "/temporal_authority/source/source_role_ref"))

    parsed = {key: _parse_datetime(value) for key, value in times.items()}
    valid_from = parsed.get("valid_from")
    valid_to = parsed.get("valid_to")
    if valid_from is not None and valid_to is not None and valid_from > valid_to:
        findings.append(Finding("TEMPORAL_ORDER_INVALID", "/temporal_authority/time/valid_to"))

    retrieved = parsed.get("retrieved_at")
    if retrieved is not None:
        for key in ("issued_at", "observed_at", "corrected_at", "superseded_at"):
            timestamp = parsed.get(key)
            if timestamp is not None and timestamp > retrieved:
                findings.append(Finding("SOURCE_TIME_AFTER_RETRIEVAL", f"/temporal_authority/time/{key}"))

    supersedes = {item for item in _array(lineage.get("supersedes")) if isinstance(item, str)}
    superseded_by = {item for item in _array(lineage.get("superseded_by")) if isinstance(item, str)}
    if isinstance(revision_id, str) and revision_id in supersedes | superseded_by:
        findings.append(Finding("SELF_LINEAGE_REFERENCE", "/temporal_authority/lineage"))
    if supersedes & superseded_by:
        findings.append(Finding("LINEAGE_DIRECTION_CONFLICT", "/temporal_authority/lineage"))

    advisory = _mapping(envelope.get("advisory"))
    onset = _parse_datetime(advisory.get("onset_at"))
    expires = _parse_datetime(advisory.get("expires_at"))
    cancelled = _parse_datetime(advisory.get("cancelled_at"))
    rescinded = _parse_datetime(advisory.get("rescinded_at"))
    if onset is not None and expires is not None and expires < onset:
        findings.append(Finding("TEMPORAL_ORDER_INVALID", "/advisory/expires_at"))
    if onset is not None and cancelled is not None and cancelled < onset:
        findings.append(Finding("TEMPORAL_ORDER_INVALID", "/advisory/cancelled_at"))
    if onset is not None and rescinded is not None and rescinded < onset:
        findings.append(Finding("TEMPORAL_ORDER_INVALID", "/advisory/rescinded_at"))
    return findings


def _payload_findings(envelope: Mapping[str, Any]) -> tuple[dict[str, Any] | None, list[Finding]]:
    domain_payload = _mapping(envelope.get("domain_payload"))
    payload_path = _safe_payload_path(domain_payload.get("payload_ref"))
    if payload_path is None:
        return None, [Finding("PAYLOAD_FILE_UNSAFE", "/domain_payload/payload_ref")]
    payload, findings = _read_object(payload_path, prefix="DOMAIN_")
    if payload is None:
        return None, [Finding("PAYLOAD_FILE_UNSAFE", "/domain_payload/payload_ref"), *findings]
    try:
        validator = _schema_validator(PAYLOAD_SCHEMA_PATH)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return None, [Finding("PAYLOAD_SCHEMA_UNAVAILABLE", "/domain_payload/payload_schema_id")]
    findings = _schema_findings(validator, payload, prefix="/domain_payload/record")
    if findings:
        return payload, findings

    expected_record_digest = canonical_record_digest(payload)
    if domain_payload.get("payload_record_digest") != expected_record_digest:
        findings.append(Finding("PAYLOAD_RECORD_DIGEST_MISMATCH", "/domain_payload/payload_record_digest"))
    if domain_payload.get("payload_source_content_digest") != payload.get("content_digest"):
        findings.append(Finding("PAYLOAD_SOURCE_DIGEST_MISMATCH", "/domain_payload/payload_source_content_digest"))
    return payload, findings


def _semantic_findings(envelope: Mapping[str, Any], payload: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    temporal = _mapping(envelope.get("temporal_authority"))
    identity = _mapping(temporal.get("identity"))
    source = _mapping(temporal.get("source"))
    time = _mapping(temporal.get("time"))
    space = _mapping(temporal.get("space"))
    lineage = _mapping(temporal.get("lineage"))
    governance = _mapping(temporal.get("governance"))
    event = _mapping(envelope.get("event"))
    surface = _mapping(envelope.get("source_surface"))
    advisory = _mapping(envelope.get("advisory"))
    scope = _mapping(envelope.get("scope"))
    controls = _mapping(envelope.get("controls"))

    if event.get("event_id") != canonical_event_id(envelope):
        findings.append(Finding("EVENT_ID_MISMATCH", "/event/event_id"))
    if event.get("native_event_id") != payload.get("advisory_snapshot_id"):
        findings.append(Finding("NATIVE_EVENT_ID_MISMATCH", "/event/native_event_id"))
    if identity.get("native_id") != payload.get("advisory_snapshot_id"):
        findings.append(Finding("TEMPORAL_NATIVE_ID_MISMATCH", "/temporal_authority/identity/native_id"))
    if identity.get("object_type") != "AdvisoryEventEnvelope":
        findings.append(Finding("OBJECT_TYPE_MISMATCH", "/temporal_authority/identity/object_type"))
    temporal_state = _mapping(temporal.get("state"))
    if temporal_state.get("normalized_state") != str(advisory.get("normalized_status", "")).lower():
        findings.append(Finding("TEMPORAL_STATE_MISMATCH", "/temporal_authority/state/normalized_state"))
    if temporal_state.get("native_state") != payload.get("normalized_state"):
        findings.append(Finding("TEMPORAL_NATIVE_STATE_MISMATCH", "/temporal_authority/state/native_state"))
    if source.get("source_descriptor_ref") != payload.get("source_id"):
        findings.append(Finding("SOURCE_DESCRIPTOR_MISMATCH", "/temporal_authority/source/source_descriptor_ref"))
    if source.get("issuing_authority_ref") != "authority:ks:kdhe":
        findings.append(Finding("ISSUING_AUTHORITY_MISSING", "/temporal_authority/source/issuing_authority_ref"))

    expected_semantics = "complete_snapshot" if payload.get("source_surface_type") == "current_table" else "single_event"
    for field, expected in (
        ("semantics", expected_semantics),
        ("snapshot_complete", payload.get("snapshot_complete")),
        ("retrieval_status", payload.get("retrieval_status")),
        ("parse_status", payload.get("parse_status")),
        ("freshness_status", payload.get("freshness_status")),
        ("checked_at", payload.get("retrieved_at")),
        ("freshness_budget_hours", payload.get("freshness_budget_hours")),
    ):
        if surface.get(field) != expected:
            findings.append(Finding("SOURCE_SURFACE_MISMATCH", f"/source_surface/{field}"))

    if advisory.get("native_status") != payload.get("advisory_level_native"):
        findings.append(Finding("NATIVE_STATUS_MISMATCH", "/advisory/native_status"))
    if controls.get("public_guidance_ref") != payload.get("recommendation_version_ref"):
        findings.append(Finding("PUBLIC_GUIDANCE_MISMATCH", "/controls/public_guidance_ref"))

    payload_state = payload.get("normalized_state")
    expected_status = EXPECTED_PAYLOAD_STATUS.get(payload_state)
    if expected_status is not None and advisory.get("normalized_status") != expected_status:
        findings.append(Finding("STATUS_MAPPING_MISMATCH", "/advisory/normalized_status"))

    normalized = advisory.get("normalized_status")
    retrieval_ok = (
        surface.get("retrieval_status") == "success"
        and surface.get("parse_status") == "success"
        and surface.get("freshness_status") == "current"
    )
    if normalized in CLEAR_STATES and not retrieval_ok:
        findings.append(Finding("FALSE_CLEAR_ATTEMPT", "/advisory/normalized_status"))
    if surface.get("retrieval_status") == "source_unavailable" and normalized != "STATUS_CHECK_FAILED":
        findings.append(Finding("STATUS_CHECK_FAILED_REQUIRED", "/advisory/normalized_status"))
    if surface.get("freshness_status") == "stale" and normalized != "STATUS_UNCONFIRMED":
        findings.append(Finding("SOURCE_STALE", "/advisory/normalized_status"))
    if normalized in ACTIVE_STATES and not retrieval_ok:
        findings.append(Finding("ACTIVE_STATUS_UNVERIFIED", "/advisory/normalized_status"))

    if normalized == "RESCINDED":
        if advisory.get("rescinded_at") is None or controls.get("rescission_ref") is None:
            findings.append(Finding("RESCISSION_REQUIRED", "/controls/rescission_ref"))
        if not _array(lineage.get("supersedes")):
            findings.append(Finding("STATUS_UNCONFIRMED", "/temporal_authority/lineage/supersedes"))
    if normalized == "SUPERSEDED" and not _array(lineage.get("superseded_by")):
        findings.append(Finding("SUPERSESSION_REQUIRED", "/temporal_authority/lineage/superseded_by"))

    if advisory.get("basis") != "regulatory_advisory":
        findings.append(Finding("SOURCE_ROLE_COLLAPSE", "/advisory/basis"))

    payload_scope = payload.get("scope_type")
    identity_conflict = payload.get("identity_resolution_status") == "CONFLICT"
    geometry_unresolved = payload_state == "GEOMETRY_UNRESOLVED" or payload.get("geometry_ref") is None
    if identity_conflict:
        if normalized != "IDENTITY_CONFLICT" or scope.get("affected_area_ref") is not None:
            findings.append(Finding("IDENTITY_CONFLICT", "/scope/affected_area_ref"))
    elif geometry_unresolved:
        if normalized != "GEOMETRY_UNRESOLVED" or scope.get("affected_area_ref") is not None:
            findings.append(Finding("AFFECTED_AREA_UNRESOLVED", "/scope/affected_area_ref"))
    else:
        if scope.get("affected_area_ref") != payload.get("geometry_ref"):
            findings.append(Finding("AFFECTED_AREA_MISMATCH", "/scope/affected_area_ref"))
        if scope.get("geometry_confidence") != payload.get("geometry_confidence"):
            findings.append(Finding("GEOMETRY_CONFIDENCE_MISMATCH", "/scope/geometry_confidence"))

    expected_zone_scope = "unresolved" if identity_conflict or geometry_unresolved else payload_scope
    if scope.get("zone_scope") != expected_zone_scope:
        code = "ZONE_SCOPE_COLLAPSE" if payload_scope == "zone" else "ZONE_SCOPE_MISMATCH"
        findings.append(Finding(code, "/scope/zone_scope"))

    if payload_scope == "zone" and scope.get("geometry_role") != "administrative_zone":
        findings.append(Finding("ZONE_SCOPE_COLLAPSE", "/scope/geometry_role"))
    if not identity_conflict and not geometry_unresolved and payload_scope != "zone":
        if scope.get("geometry_role") != "advisory_area":
            findings.append(Finding("GEOMETRY_ROLE_MISMATCH", "/scope/geometry_role"))

    if controls.get("release_neutral") is not True or controls.get("public_use_allowed") is not False or controls.get("alerts_allowed") is not False:
        findings.append(Finding("RELEASE_NEUTRALITY_VIOLATION", "/controls"))
    if governance.get("release_ref") is not None or governance.get("public_use_allowed") is not False:
        findings.append(Finding("RELEASE_AUTHORITY_PRESENT", "/temporal_authority/governance"))

    if time.get("retrieved_at") != surface.get("checked_at"):
        findings.append(Finding("RETRIEVAL_TIME_MISMATCH", "/source_surface/checked_at"))
    if space.get("geography_ref") != scope.get("affected_area_ref"):
        findings.append(Finding("TEMPORAL_GEOGRAPHY_MISMATCH", "/temporal_authority/space/geography_ref"))
    return findings


def validate_envelope_object(envelope: Mapping[str, Any]) -> ValidationResult:
    try:
        validator = _schema_validator(SCHEMA_PATH)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return ValidationResult((Finding("SCHEMA_UNAVAILABLE", "/"),))
    findings = _schema_findings(validator, envelope)
    if findings:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_temporal_findings(envelope))
    payload, payload_findings = _payload_findings(envelope)
    findings.extend(payload_findings)
    if payload is not None and not payload_findings:
        findings.extend(_semantic_findings(envelope, payload))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_envelope(path: Path) -> ValidationResult:
    envelope, findings = _read_object(path)
    if envelope is None:
        return ValidationResult(tuple(sorted(set(findings))))
    return validate_envelope_object(envelope)
