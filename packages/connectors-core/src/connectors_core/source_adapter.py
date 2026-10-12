"""Pure SourceAdapter protocol and source-agnostic boundary value objects.

This module defines the executable shape shared by future source-specific KFM
adapters. It deliberately performs no network, filesystem, environment, clock,
registry, lifecycle, policy, review, receipt, release, or publication work.
Callers inject transport and artifact implementations and remain responsible for
all governance-bearing decisions.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
import hashlib
import json
import math
import re
from types import MappingProxyType
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from .core import redact_url, validate_sha256_digest

if TYPE_CHECKING:
    from .transport import RetrievalResult

_TOKEN_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,159}$")
_REASON_RE = re.compile(r"^[A-Z][A-Z0-9_]{2,79}$")
_MEDIA_TYPE_RE = re.compile(
    r"^[a-z0-9][a-z0-9!#$&^_.+-]{0,126}/[a-z0-9][a-z0-9!#$&^_.+-]{0,126}$"
)
_ARTIFACT_REF_RE = re.compile(r"^source-artifact:sha256:[0-9a-f]{64}$")
_CONTROL_RE = re.compile(r"[\x00-\x1f\x7f]")
_SECRET_RE = re.compile(
    r"(?i)(authorization|cookie|api[-_]?key|access[-_]?token|refresh[-_]?token|"
    r"bearer|secret|password)"
)
_FORBIDDEN_CAPABILITIES = (
    "activate_source",
    "admit_source",
    "clear_advisory",
    "create_evidence_bundle",
    "merge_pr",
    "publish",
    "release",
    "write_lifecycle",
)


class AdapterBoundaryError(ValueError):
    """Raised when an adapter value exceeds the source-adapter boundary."""


class ParseOutcome(str, Enum):
    """Finite parser outcomes; none grants evidence or release authority."""

    PARSED = "PARSED"
    MALFORMED = "MALFORMED"
    UNSUPPORTED = "UNSUPPORTED"
    CONFLICT = "CONFLICT"
    ERROR = "ERROR"


class SourceHealthStatus(str, Enum):
    """Finite source-health observations, never domain-event clear states."""

    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    UNREACHABLE = "UNREACHABLE"
    AUTH_REQUIRED = "AUTH_REQUIRED"
    RATE_LIMITED = "RATE_LIMITED"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True, slots=True)
class DiscoveryCursor:
    """Caller-supplied, deterministic discovery boundary.

    ``observed_at`` is injected by the caller; no wall-clock value is sampled.
    ``cursor`` is an opaque source token and must not contain secret-like text.
    """

    profile_id: str
    observed_at: datetime
    cursor: str | None = None
    limit: int = 100

    def __post_init__(self) -> None:
        _token(self.profile_id, "profile_id")
        _aware(self.observed_at, "observed_at")
        if self.cursor is not None:
            _safe_text(self.cursor, "cursor", maximum=512, reject_secret=True)
        if isinstance(self.limit, bool) or not isinstance(self.limit, int):
            raise TypeError("limit must be an integer")
        if not 1 <= self.limit <= 10_000:
            raise AdapterBoundaryError("limit must be within 1..10000")


@dataclass(frozen=True, slots=True)
class SourceLocator:
    """Value-minimized locator discovered under one approved adapter profile."""

    source_descriptor_ref: str
    profile_id: str
    native_id: str
    safe_locator: str
    locator_kind: str
    parameter_names: tuple[str, ...] = ()
    expected_media_types: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _reference(self.source_descriptor_ref, "source_descriptor_ref")
        _token(self.profile_id, "profile_id")
        _safe_text(self.native_id, "native_id", maximum=320, reject_secret=True)
        if self.locator_kind not in {"api_record", "https_url"}:
            raise AdapterBoundaryError("locator_kind must be api_record or https_url")
        try:
            redacted = redact_url(self.safe_locator)
        except (TypeError, ValueError) as exc:
            raise AdapterBoundaryError("safe_locator is invalid") from exc
        if redacted != self.safe_locator:
            raise AdapterBoundaryError(
                "safe_locator must already be canonical and secret-safe"
            )
        if not self.safe_locator.startswith("https://"):
            raise AdapterBoundaryError("safe_locator must use https")
        names = _canonical_tokens(self.parameter_names, "parameter_names")
        media_types = tuple(
            sorted(
                {
                    _media_type(value, "expected_media_types")
                    for value in self.expected_media_types
                }
            )
        )
        if not media_types:
            raise AdapterBoundaryError("expected_media_types cannot be empty")
        object.__setattr__(self, "parameter_names", names)
        object.__setattr__(self, "expected_media_types", media_types)

    @property
    def locator_digest(self) -> str:
        payload = {
            "expected_media_types": list(self.expected_media_types),
            "locator_kind": self.locator_kind,
            "native_id": self.native_id,
            "parameter_names": list(self.parameter_names),
            "profile_id": self.profile_id,
            "safe_locator": self.safe_locator,
            "source_descriptor_ref": self.source_descriptor_ref,
        }
        return _sha256(_canonical_json(payload).encode("utf-8"))


@dataclass(frozen=True, order=True, slots=True)
class ParseFinding:
    """Stable parser diagnostic with a finite code and JSON-pointer-like path."""

    code: str
    path: str

    def __post_init__(self) -> None:
        if _REASON_RE.fullmatch(self.code) is None:
            raise AdapterBoundaryError("finding code is not canonical")
        if self.path != "/" and not self.path.startswith("/"):
            raise AdapterBoundaryError("finding path must be '/' or start with '/'")
        _safe_text(self.path, "finding path", maximum=512)


@dataclass(frozen=True, slots=True)
class ParseResult:
    """Immutable parser result bound to one SourceArtifact identity.

    Records are deeply frozen. A result never creates evidence, lifecycle,
    policy, review, receipt, release, publication, or repository authority.
    """

    source_artifact_ref: str
    parser_id: str
    parser_version: str
    parser_spec_digest: str
    outcome: ParseOutcome
    records: tuple[Mapping[str, object], ...] = ()
    findings: tuple[ParseFinding, ...] = ()
    unsupported_flags: tuple[str, ...] = ()
    source_conflict_ref: str | None = None
    authority_created: bool = False
    evidence_created: bool = False
    lifecycle_write_allowed: bool = False
    receipt_created: bool = False
    release_authorized: bool = False
    publication_authorized: bool = False
    public_use_allowed: bool = False
    repository_mutation_allowed: bool = False

    def __post_init__(self) -> None:
        if _ARTIFACT_REF_RE.fullmatch(self.source_artifact_ref) is None:
            raise AdapterBoundaryError("source_artifact_ref is invalid")
        _reference(self.parser_id, "parser_id")
        _safe_text(self.parser_version, "parser_version", maximum=80)
        validate_sha256_digest(self.parser_spec_digest)
        if self.parser_spec_digest == _zero_digest():
            raise AdapterBoundaryError("parser_spec_digest cannot be all-zero")
        if not isinstance(self.outcome, ParseOutcome):
            raise TypeError("outcome must be ParseOutcome")

        frozen_records = tuple(_freeze(record) for record in self.records)
        if not all(isinstance(record, Mapping) for record in frozen_records):
            raise TypeError("records must contain mappings")
        findings = tuple(sorted(set(self.findings)))
        flags = _canonical_reason_codes(self.unsupported_flags, "unsupported_flags")
        if self.source_conflict_ref is not None:
            _reference(self.source_conflict_ref, "source_conflict_ref")
        if any(
            (
                self.authority_created,
                self.evidence_created,
                self.lifecycle_write_allowed,
                self.receipt_created,
                self.release_authorized,
                self.publication_authorized,
                self.public_use_allowed,
                self.repository_mutation_allowed,
            )
        ):
            raise AdapterBoundaryError(
                "ParseResult cannot create authority, lifecycle, receipt, release, or public use"
            )

        if self.outcome is ParseOutcome.PARSED:
            if not frozen_records:
                raise AdapterBoundaryError("PARSED requires at least one record")
            if flags or self.source_conflict_ref is not None:
                raise AdapterBoundaryError(
                    "PARSED cannot carry unsupported flags or a conflict reference"
                )
        elif self.outcome is ParseOutcome.CONFLICT:
            if len(frozen_records) < 2:
                raise AdapterBoundaryError("CONFLICT requires at least two records")
            if self.source_conflict_ref is None:
                raise AdapterBoundaryError("CONFLICT requires source_conflict_ref")
            if "SOURCE_CONFLICT" not in {finding.code for finding in findings}:
                raise AdapterBoundaryError(
                    "CONFLICT requires a SOURCE_CONFLICT finding"
                )
        elif self.outcome is ParseOutcome.UNSUPPORTED:
            if frozen_records:
                raise AdapterBoundaryError("UNSUPPORTED cannot carry parsed records")
            if not flags:
                raise AdapterBoundaryError("UNSUPPORTED requires unsupported_flags")
            if self.source_conflict_ref is not None:
                raise AdapterBoundaryError(
                    "UNSUPPORTED cannot carry source_conflict_ref"
                )
        else:
            if frozen_records:
                raise AdapterBoundaryError(
                    f"{self.outcome.value} cannot carry parsed records"
                )
            if not findings:
                raise AdapterBoundaryError(
                    f"{self.outcome.value} requires at least one finding"
                )
            if flags or self.source_conflict_ref is not None:
                raise AdapterBoundaryError(
                    f"{self.outcome.value} cannot carry unsupported flags or conflict reference"
                )

        if self.outcome is not ParseOutcome.CONFLICT and self.source_conflict_ref is not None:
            raise AdapterBoundaryError(
                "only CONFLICT may carry source_conflict_ref"
            )
        object.__setattr__(self, "records", frozen_records)
        object.__setattr__(self, "findings", findings)
        object.__setattr__(self, "unsupported_flags", flags)

    @property
    def record_count(self) -> int:
        return len(self.records)

    def records_copy(self) -> list[dict[str, object]]:
        """Return a mutable plain-data copy without weakening stored immutability."""

        return [_thaw(record) for record in self.records]


@dataclass(frozen=True, slots=True)
class SourceHealth:
    """One source-health observation with explicit false-clear prevention."""

    adapter_id: str
    source_descriptor_ref: str
    profile_id: str
    observed_at: datetime
    status: SourceHealthStatus
    reason_codes: tuple[str, ...]
    status_check_completed: bool
    last_success_at: datetime | None = None
    last_artifact_ref: str | None = None
    clear_signal_allowed: bool = False
    authority_created: bool = False
    lifecycle_write_allowed: bool = False
    release_authorized: bool = False
    publication_authorized: bool = False
    public_use_allowed: bool = False

    def __post_init__(self) -> None:
        _token(self.adapter_id, "adapter_id")
        _reference(self.source_descriptor_ref, "source_descriptor_ref")
        _token(self.profile_id, "profile_id")
        _aware(self.observed_at, "observed_at")
        if not isinstance(self.status, SourceHealthStatus):
            raise TypeError("status must be SourceHealthStatus")
        reasons = _canonical_reason_codes(self.reason_codes, "reason_codes")
        if not reasons:
            raise AdapterBoundaryError("reason_codes cannot be empty")
        if not isinstance(self.status_check_completed, bool):
            raise TypeError("status_check_completed must be boolean")
        if self.last_success_at is not None:
            _aware(self.last_success_at, "last_success_at")
            if self.last_success_at > self.observed_at:
                raise AdapterBoundaryError(
                    "last_success_at cannot be after observed_at"
                )
        if self.last_artifact_ref is not None:
            if _ARTIFACT_REF_RE.fullmatch(self.last_artifact_ref) is None:
                raise AdapterBoundaryError("last_artifact_ref is invalid")
            if self.last_success_at is None:
                raise AdapterBoundaryError(
                    "last_artifact_ref requires last_success_at"
                )
        if self.status is SourceHealthStatus.HEALTHY:
            if not self.status_check_completed or self.last_success_at is None:
                raise AdapterBoundaryError(
                    "HEALTHY requires a completed check and last_success_at"
                )
        if self.clear_signal_allowed:
            raise AdapterBoundaryError(
                "source health must never authorize clearing a domain event"
            )
        if any(
            (
                self.authority_created,
                self.lifecycle_write_allowed,
                self.release_authorized,
                self.publication_authorized,
                self.public_use_allowed,
            )
        ):
            raise AdapterBoundaryError(
                "SourceHealth cannot create authority, lifecycle, release, or public use"
            )
        object.__setattr__(self, "reason_codes", reasons)


@runtime_checkable
class SourceArtifactView(Protocol):
    """Structural view required by parsers; implemented by artifact handoffs."""

    @property
    def content_digest(self) -> str: ...

    @property
    def byte_length(self) -> int: ...

    def metadata_dict(self) -> dict[str, object]: ...

    def payload_bytes(self) -> bytes: ...


@runtime_checkable
class SourceAdapter(Protocol):
    """Source-specific mechanics behind an explicit, no-authority boundary."""

    @property
    def adapter_id(self) -> str: ...

    def discover(self, cursor: DiscoveryCursor) -> Sequence[SourceLocator]: ...

    def fetch(self, locator: SourceLocator) -> RetrievalResult: ...

    def parse(self, artifact: SourceArtifactView) -> ParseResult: ...

    def source_health(self) -> SourceHealth: ...


def assert_source_adapter_boundary(adapter: object) -> SourceAdapter:
    """Validate structural conformance without invoking adapter operations.

    This check cannot prove implementation purity. It catches missing protocol
    members and explicitly authority-bearing method names before a caller admits
    an adapter into a stricter source-specific review.
    """

    if not isinstance(adapter, SourceAdapter):
        raise AdapterBoundaryError("object does not satisfy SourceAdapter protocol")
    _token(adapter.adapter_id, "adapter_id")
    forbidden = [
        name
        for name in _FORBIDDEN_CAPABILITIES
        if callable(getattr(adapter, name, None))
    ]
    if forbidden:
        raise AdapterBoundaryError(
            "adapter exposes forbidden capabilities: " + ", ".join(forbidden)
        )
    return adapter


def _aware(value: datetime, field: str) -> datetime:
    if not isinstance(value, datetime):
        raise TypeError(f"{field} must be a datetime")
    if value.tzinfo is None or value.utcoffset() is None:
        raise AdapterBoundaryError(f"{field} must be timezone-aware")
    return value.astimezone(timezone.utc)


def _token(value: str, field: str) -> str:
    if not isinstance(value, str) or _TOKEN_RE.fullmatch(value) is None:
        raise AdapterBoundaryError(f"{field} is not a safe token")
    return value


def _safe_text(
    value: str,
    field: str,
    *,
    maximum: int,
    reject_secret: bool = False,
) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string")
    if not value or len(value) > maximum or _CONTROL_RE.search(value):
        raise AdapterBoundaryError(f"{field} is empty, too long, or contains controls")
    if reject_secret and _SECRET_RE.search(value):
        raise AdapterBoundaryError(f"{field} contains secret-like text")
    return value


def _reference(value: str, field: str) -> str:
    _safe_text(value, field, maximum=640, reject_secret=True)
    if any(char.isspace() for char in value):
        raise AdapterBoundaryError(f"{field} cannot contain whitespace")
    return value


def _canonical_tokens(values: Sequence[str], field: str) -> tuple[str, ...]:
    canonical = tuple(sorted({_token(value, field) for value in values}))
    if tuple(values) != canonical:
        raise AdapterBoundaryError(f"{field} must already be sorted and unique")
    return canonical


def _canonical_reason_codes(values: Sequence[str], field: str) -> tuple[str, ...]:
    canonical = tuple(sorted(set(values)))
    if tuple(values) != canonical:
        raise AdapterBoundaryError(f"{field} must already be sorted and unique")
    if any(_REASON_RE.fullmatch(value) is None for value in canonical):
        raise AdapterBoundaryError(f"{field} contains a noncanonical code")
    return canonical


def _media_type(value: str, field: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field} values must be strings")
    normalized = value.strip().lower()
    if _MEDIA_TYPE_RE.fullmatch(normalized) is None:
        raise AdapterBoundaryError(f"{field} contains an invalid media type")
    return normalized


def _freeze(value: object) -> object:
    if isinstance(value, Mapping):
        if any(not isinstance(key, str) for key in value):
            raise TypeError("record mapping keys must be strings")
        return MappingProxyType(
            {key: _freeze(value[key]) for key in sorted(value)}
        )
    if isinstance(value, (list, tuple)):
        return tuple(_freeze(item) for item in value)
    if isinstance(value, float):
        if not math.isfinite(value):
            raise TypeError("record numbers must be finite")
        return value
    if value is None or isinstance(value, (str, int, bool)):
        return value
    raise TypeError(f"unsupported record value type: {type(value).__name__}")


def _thaw(value: object) -> object:
    if isinstance(value, Mapping):
        return {str(key): _thaw(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_thaw(item) for item in value]
    return value


def _canonical_json(value: object) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def _sha256(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def _zero_digest() -> str:
    return "sha256:" + ("0" * 64)


__all__ = [
    "AdapterBoundaryError",
    "DiscoveryCursor",
    "ParseFinding",
    "ParseOutcome",
    "ParseResult",
    "SourceAdapter",
    "SourceArtifactView",
    "SourceHealth",
    "SourceHealthStatus",
    "SourceLocator",
    "assert_source_adapter_boundary",
]
