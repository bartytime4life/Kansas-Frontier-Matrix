"""Pure retrieval-to-SourceArtifact candidate handoff.

This module performs no transport, storage, source admission, lifecycle write,
receipt emission, evidence closure, policy decision, release, or publication.
It converts one already-successful injected GET retrieval into exact bytes plus a
schema-shaped metadata candidate for a governed caller to validate and persist.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import re
from types import MappingProxyType
from typing import Mapping, Sequence

from .core import TransportCategory, validate_sha256_digest
from ._transport_request import TransportMethod
from ._transport_result import RetrievalResult

_TOKEN_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,159}$")
_HEADER_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,79}$")
_REF_RE = re.compile(r"^\S{1,640}$")
_SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
_ACCESS_CLASSES = frozenset({"public", "restricted", "controlled", "unknown"})
_REDISTRIBUTION = frozenset({"allowed", "restricted", "denied", "unknown"})
_REVIEW_STATES = frozenset({"pending", "reviewed", "unknown"})
_LOCATOR_KINDS = frozenset({"https_url", "api_record"})
_SURFACE_TYPES = frozenset(
    {
        "api_record",
        "current_table",
        "pdf_document",
        "gis_package",
        "repository_object",
        "structured_file",
        "other_binary",
    }
)
_CAPTURE_OUTCOMES = frozenset({"FETCHED", "MALFORMED", "SOURCE_CONFLICT"})


class ArtifactHandoffError(ValueError):
    """Invalid or unsupported retrieval-to-artifact handoff input."""


@dataclass(frozen=True, slots=True)
class RightsSnapshot:
    captured_at: datetime
    license_id: str | None
    terms_ref: str | None
    access_class: str
    redistribution_status: str
    review_state: str

    def __post_init__(self) -> None:
        _aware(self.captured_at, "rights.captured_at")
        if self.license_id is not None:
            _bounded_text(self.license_id, "rights.license_id", maximum=160)
        if self.terms_ref is not None:
            _reference(self.terms_ref, "rights.terms_ref")
        if self.access_class not in _ACCESS_CLASSES:
            raise ArtifactHandoffError("rights.access_class is unsupported")
        if self.redistribution_status not in _REDISTRIBUTION:
            raise ArtifactHandoffError("rights.redistribution_status is unsupported")
        if self.review_state not in _REVIEW_STATES:
            raise ArtifactHandoffError("rights.review_state is unsupported")


@dataclass(frozen=True, slots=True)
class ParserIdentity:
    parser_id: str
    version: str
    spec_digest: str

    def __post_init__(self) -> None:
        _reference(self.parser_id, "parser.parser_id")
        _bounded_text(self.version, "parser.version", maximum=80)
        validate_sha256_digest(self.spec_digest)
        if self.spec_digest == _zero_digest():
            raise ArtifactHandoffError("parser.spec_digest cannot be an all-zero placeholder")


@dataclass(frozen=True, slots=True)
class ArtifactHandoffContext:
    source_descriptor_ref: str
    ingest_receipt_ref: str
    locator_kind: str
    first_party_authority: bool
    profile_id: str
    parameter_names: tuple[str, ...]
    header_names: tuple[str, ...]
    rights_snapshot: RightsSnapshot
    parser: ParserIdentity
    source_surface_type: str
    governance_spec_hash: str
    retrieval_outcome: str = "FETCHED"
    supersedes_artifact_ref: str | None = None
    correction_refs: tuple[str, ...] = ()
    conflict_group_ref: str | None = None

    def __post_init__(self) -> None:
        _reference(self.source_descriptor_ref, "source_descriptor_ref")
        _reference(self.ingest_receipt_ref, "ingest_receipt_ref")
        if self.locator_kind not in _LOCATOR_KINDS:
            raise ArtifactHandoffError("locator_kind must be api_record or https_url")
        if not isinstance(self.first_party_authority, bool):
            raise TypeError("first_party_authority must be boolean")
        _token(self.profile_id, "profile_id")
        parameters = _canonical_tokens(self.parameter_names, "parameter_names")
        headers = _canonical_headers(self.header_names)
        if not isinstance(self.rights_snapshot, RightsSnapshot):
            raise TypeError("rights_snapshot must be RightsSnapshot")
        if not isinstance(self.parser, ParserIdentity):
            raise TypeError("parser must be ParserIdentity")
        if self.source_surface_type not in _SURFACE_TYPES:
            raise ArtifactHandoffError("source_surface_type is unsupported")
        validate_sha256_digest(self.governance_spec_hash)
        if self.governance_spec_hash == _zero_digest():
            raise ArtifactHandoffError("governance_spec_hash cannot be an all-zero placeholder")
        if self.retrieval_outcome not in _CAPTURE_OUTCOMES:
            raise ArtifactHandoffError("retrieval_outcome is unsupported")
        if self.supersedes_artifact_ref is not None:
            _artifact_ref(self.supersedes_artifact_ref, "supersedes_artifact_ref")
        corrections = tuple(sorted({_reference(value, "correction_refs") for value in self.correction_refs}))
        if self.conflict_group_ref is not None:
            _reference(self.conflict_group_ref, "conflict_group_ref")
        if self.supersedes_artifact_ref is not None and not corrections:
            raise ArtifactHandoffError("supersession requires at least one correction reference")
        if self.retrieval_outcome == "SOURCE_CONFLICT" and self.conflict_group_ref is None:
            raise ArtifactHandoffError("SOURCE_CONFLICT requires conflict_group_ref")
        if self.retrieval_outcome != "SOURCE_CONFLICT" and self.conflict_group_ref is not None:
            raise ArtifactHandoffError("non-conflict outcome cannot carry conflict_group_ref")
        object.__setattr__(self, "parameter_names", parameters)
        object.__setattr__(self, "header_names", headers)
        object.__setattr__(self, "correction_refs", corrections)


@dataclass(frozen=True, slots=True, repr=False)
class SourceArtifactHandoff:
    """Exact captured bytes and immutable SourceArtifact metadata candidate."""

    metadata: Mapping[str, object]
    payload_chunks: tuple[bytes, ...]
    authority_created: bool = False
    lifecycle_write_allowed: bool = False
    receipt_created: bool = False
    repository_mutation_allowed: bool = False

    def __post_init__(self) -> None:
        frozen = _freeze(self.metadata)
        if not isinstance(frozen, Mapping):
            raise TypeError("metadata must be a mapping")
        chunks = tuple(bytes(chunk) for chunk in self.payload_chunks)
        if not chunks or sum(len(chunk) for chunk in chunks) <= 0:
            raise ArtifactHandoffError("handoff requires non-empty captured bytes")
        if (
            self.authority_created
            or self.lifecycle_write_allowed
            or self.receipt_created
            or self.repository_mutation_allowed
        ):
            raise ArtifactHandoffError("handoff cannot create authority, receipts, or repository writes")
        object.__setattr__(self, "metadata", frozen)
        object.__setattr__(self, "payload_chunks", chunks)

    @property
    def content_digest(self) -> str:
        return str(self.metadata["content_digest"])

    @property
    def byte_length(self) -> int:
        return int(self.metadata["byte_length"])

    def metadata_dict(self) -> dict[str, object]:
        return _thaw(self.metadata)

    def payload_bytes(self) -> bytes:
        return b"".join(self.payload_chunks)

    def __repr__(self) -> str:
        return (
            "SourceArtifactHandoff("
            f"artifact_id={self.metadata.get('artifact_id')!r}, "
            f"content_digest={self.content_digest!r}, byte_length={self.byte_length}, "
            "authority_created=False, lifecycle_write_allowed=False, receipt_created=False)"
        )


def build_source_artifact_handoff(
    result: RetrievalResult,
    context: ArtifactHandoffContext,
) -> SourceArtifactHandoff:
    """Build one SourceArtifact candidate from a successful injected GET result.

    No-byte, HEAD, failed, partial, or not-modified outcomes are rejected. A
    governed caller remains responsible for schema/semantic validation, receipt
    existence, storage, lifecycle routing, evidence resolution, policy, and release.
    """

    if not isinstance(result, RetrievalResult):
        raise TypeError("result must be RetrievalResult")
    if not isinstance(context, ArtifactHandoffContext):
        raise TypeError("context must be ArtifactHandoffContext")
    if result.category is not TransportCategory.SUCCESS:
        raise ArtifactHandoffError("only SUCCESS retrievals can create an artifact handoff")
    if result.method is not TransportMethod.GET:
        raise ArtifactHandoffError("only successful GET retrievals carry artifact bytes")
    if result.payload is None or result.source_head is None:
        raise ArtifactHandoffError("successful GET retrieval requires payload and source head")
    if result.failure is not None or result.prior_artifact_retained:
        raise ArtifactHandoffError("artifact handoff cannot carry failure or prior-artifact-only state")
    if result.authority_created or result.repository_mutation_allowed:
        raise ArtifactHandoffError("retrieval result exceeds the admitted authority boundary")

    payload = result.payload
    source_head = result.source_head
    retrieved_at = _aware(source_head.observed_at, "source_head.observed_at")
    if context.rights_snapshot.captured_at > retrieved_at:
        raise ArtifactHandoffError("rights snapshot cannot occur after retrieval")
    if source_head.computed_digest is None or source_head.computed_digest != payload.digest:
        raise ArtifactHandoffError("source-head digest must match captured payload")
    if source_head.content_length is not None and source_head.content_length != payload.byte_length:
        raise ArtifactHandoffError("source-head length must match captured payload")
    final_attempt = result.attempts[-1]
    if final_attempt.status_code is None:
        raise ArtifactHandoffError("network retrieval handoff requires final HTTP status")
    if final_attempt.digest is not None and final_attempt.digest != payload.digest:
        raise ArtifactHandoffError("final-attempt digest must match captured payload")
    if final_attempt.byte_length not in {0, payload.byte_length}:
        raise ArtifactHandoffError("final-attempt length must match captured payload")

    artifact_id = f"source-artifact:{payload.digest}"
    if context.supersedes_artifact_ref == artifact_id:
        raise ArtifactHandoffError("artifact cannot supersede itself")
    locator_digest = _sha256(f"{context.locator_kind}\n{result.safe_locator}".encode("utf-8"))
    metadata: dict[str, object] = {
        "object_type": "SourceArtifact",
        "schema_version": "1.0.0",
        "artifact_id": artifact_id,
        "source_descriptor_ref": context.source_descriptor_ref,
        "ingest_receipt_ref": context.ingest_receipt_ref,
        "source_locator": {
            "kind": context.locator_kind,
            "value": result.safe_locator,
            "first_party_authority": context.first_party_authority,
            "locator_digest": locator_digest,
        },
        "retrieved_at": _iso8601(retrieved_at),
        "source_reported_at": (
            _iso8601(source_head.last_modified) if source_head.last_modified is not None else None
        ),
        "retrieval_outcome": context.retrieval_outcome,
        "status_code": final_attempt.status_code,
        "media_type": payload.media_type,
        "byte_length": payload.byte_length,
        "content_digest": payload.digest,
        "immutable_storage_ref": f"cas:{payload.digest}",
        "request_context": {
            "method": "GET",
            "profile_id": context.profile_id,
            "parameter_names": list(context.parameter_names),
            "header_names": list(context.header_names),
            "body_digest": None,
            "secrets_embedded": False,
        },
        "rights_snapshot": {
            "captured_at": _iso8601(context.rights_snapshot.captured_at),
            "license_id": context.rights_snapshot.license_id,
            "terms_ref": context.rights_snapshot.terms_ref,
            "access_class": context.rights_snapshot.access_class,
            "redistribution_status": context.rights_snapshot.redistribution_status,
            "review_state": context.rights_snapshot.review_state,
        },
        "parser": {
            "parser_id": context.parser.parser_id,
            "version": context.parser.version,
            "spec_digest": context.parser.spec_digest,
        },
        "source_surface_type": context.source_surface_type,
        "lineage": {
            "supersedes_artifact_ref": context.supersedes_artifact_ref,
            "correction_refs": list(context.correction_refs),
            "conflict_group_ref": context.conflict_group_ref,
        },
        "governance": {
            "public_use_allowed": False,
            "authority_created": False,
            "release_ref": None,
            "spec_hash": context.governance_spec_hash,
        },
    }
    return SourceArtifactHandoff(metadata=metadata, payload_chunks=payload.chunks)


def _zero_digest() -> str:
    return "sha256:" + ("0" * 64)


def _sha256(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def _aware(value: datetime, name: str) -> datetime:
    if not isinstance(value, datetime):
        raise TypeError(f"{name} must be datetime")
    if value.tzinfo is None or value.utcoffset() is None:
        raise ArtifactHandoffError(f"{name} must be timezone-aware")
    return value


def _iso8601(value: datetime) -> str:
    normalized = _aware(value, "timestamp").astimezone(timezone.utc)
    return normalized.isoformat(timespec="seconds").replace("+00:00", "Z")


def _bounded_text(value: str, name: str, *, maximum: int) -> str:
    if not isinstance(value, str) or not value or len(value) > maximum:
        raise ArtifactHandoffError(f"{name} must be a bounded non-empty string")
    if any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise ArtifactHandoffError(f"{name} contains control characters")
    return value


def _reference(value: str, name: str) -> str:
    if not isinstance(value, str) or _REF_RE.fullmatch(value) is None:
        raise ArtifactHandoffError(f"{name} must be a bounded non-whitespace reference")
    return value


def _token(value: str, name: str) -> str:
    if not isinstance(value, str) or _TOKEN_RE.fullmatch(value) is None:
        raise ArtifactHandoffError(f"{name} must be a bounded token")
    return value


def _artifact_ref(value: str, name: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"source-artifact:sha256:[0-9a-f]{64}", value):
        raise ArtifactHandoffError(f"{name} must be a SourceArtifact reference")
    return value


def _canonical_tokens(values: Sequence[str], name: str) -> tuple[str, ...]:
    if isinstance(values, (str, bytes)):
        raise TypeError(f"{name} must be a sequence of strings")
    result = tuple(sorted({_token(value, name) for value in values}))
    return result


def _canonical_headers(values: Sequence[str]) -> tuple[str, ...]:
    if isinstance(values, (str, bytes)):
        raise TypeError("header_names must be a sequence of strings")
    result: set[str] = set()
    for value in values:
        if not isinstance(value, str) or _HEADER_RE.fullmatch(value) is None:
            raise ArtifactHandoffError("header_names must contain lower-case HTTP tokens")
        result.add(value)
    return tuple(sorted(result))


def _freeze(value: object) -> object:
    if isinstance(value, Mapping):
        return MappingProxyType({str(key): _freeze(child) for key, child in value.items()})
    if isinstance(value, list | tuple):
        return tuple(_freeze(child) for child in value)
    return value


def _thaw(value: object) -> object:
    if isinstance(value, Mapping):
        return {str(key): _thaw(child) for key, child in value.items()}
    if isinstance(value, tuple):
        return [_thaw(child) for child in value]
    return value


__all__ = [
    "ArtifactHandoffContext",
    "ArtifactHandoffError",
    "ParserIdentity",
    "RightsSnapshot",
    "SourceArtifactHandoff",
    "build_source_artifact_handoff",
]
