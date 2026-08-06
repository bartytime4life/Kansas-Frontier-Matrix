"""Value-minimized immutable observations returned by transport execution."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import hmac
import math

from .core import (
    FailureDetail,
    SourceHeadObservation,
    TransportCategory,
    TransportValueError,
    redact_url,
    sha256_stream,
    validate_sha256_digest,
)
from ._transport_identity import normalize_media_type
from ._transport_request import TransportInputError, TransportMethod


@dataclass(frozen=True, slots=True, repr=False)
class CapturedPayload:
    chunks: tuple[bytes, ...]
    digest: str
    byte_length: int
    media_type: str

    def __post_init__(self) -> None:
        normalized = tuple(bytes(v) for v in self.chunks)
        observed = sha256_stream(normalized)
        if observed.byte_length != self.byte_length:
            raise TransportInputError("payload byte_length does not match chunks")
        if not hmac.compare_digest(observed.digest, validate_sha256_digest(self.digest)):
            raise TransportInputError("payload digest does not match chunks")
        object.__setattr__(self, "chunks", normalized)
        try:
            object.__setattr__(self, "media_type", normalize_media_type(self.media_type))
        except (TransportValueError, ValueError) as exc:
            raise TransportInputError(str(exc)) from exc

    def __repr__(self) -> str:
        return (
            "CapturedPayload("
            f"digest={self.digest!r}, byte_length={self.byte_length}, media_type={self.media_type!r})"
        )


@dataclass(frozen=True, slots=True)
class AttemptRecord:
    attempt_number: int
    category: TransportCategory
    code: str
    observed_at: datetime
    duration_seconds: float
    safe_locator: str
    status_code: int | None = None
    byte_length: int = 0
    digest: str | None = None
    retry_delay_seconds: float = 0.0

    def __post_init__(self) -> None:
        if self.attempt_number < 0:
            raise TransportInputError("attempt_number must be non-negative")
        if not isinstance(self.category, TransportCategory):
            raise TransportInputError("category must be a TransportCategory")
        if self.observed_at.tzinfo is None:
            raise TransportInputError("observed_at must be timezone-aware")
        if not math.isfinite(self.duration_seconds) or self.duration_seconds < 0:
            raise TransportInputError("duration_seconds must be finite and non-negative")
        if self.safe_locator != redact_url(self.safe_locator):
            raise TransportInputError("safe_locator is not redacted")
        if self.status_code is not None and not 100 <= self.status_code <= 599:
            raise TransportInputError("status_code must be within 100..599")
        if self.byte_length < 0:
            raise TransportInputError("byte_length must be non-negative")
        if self.digest is not None:
            validate_sha256_digest(self.digest)
        if not math.isfinite(self.retry_delay_seconds) or self.retry_delay_seconds < 0:
            raise TransportInputError("retry_delay_seconds must be finite and non-negative")


@dataclass(frozen=True, slots=True, repr=False)
class RetrievalResult:
    method: TransportMethod
    category: TransportCategory
    safe_locator: str
    attempts: tuple[AttemptRecord, ...]
    payload: CapturedPayload | None = None
    source_head: SourceHeadObservation | None = None
    failure: FailureDetail | None = None
    prior_artifact_retained: bool = False
    authority_created: bool = False
    repository_mutation_allowed: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.method, TransportMethod):
            raise TransportInputError("method must be a TransportMethod")
        if not isinstance(self.category, TransportCategory):
            raise TransportInputError("category must be a TransportCategory")
        if self.safe_locator != redact_url(self.safe_locator):
            raise TransportInputError("safe_locator is not redacted")
        if not self.attempts:
            raise TransportInputError("attempts must not be empty")
        expected = tuple(range(1, len(self.attempts) + 1))
        numbers = tuple(v.attempt_number for v in self.attempts)
        if numbers != expected and numbers != (0,):
            raise TransportInputError("attempts must be contiguous and 1-based, except pre-transport cancellation")
        if self.attempts[-1].category is not self.category:
            raise TransportInputError("final category must match the last attempt")
        success = self.category in {TransportCategory.SUCCESS, TransportCategory.NOT_MODIFIED}
        if success:
            if self.source_head is None or self.failure is not None:
                raise TransportInputError("success requires source_head and no failure")
        else:
            if self.failure is None or self.payload is not None or self.source_head is not None:
                raise TransportInputError("failure requires failure detail and no payload/source_head")
        if self.category is TransportCategory.NOT_MODIFIED:
            if self.payload is not None or not self.prior_artifact_retained:
                raise TransportInputError("NOT_MODIFIED requires a prior artifact and no payload")
        if self.category is TransportCategory.SUCCESS:
            if self.method is TransportMethod.GET and self.payload is None:
                raise TransportInputError("successful GET requires captured bytes")
            if self.method is TransportMethod.HEAD and self.payload is not None:
                raise TransportInputError("HEAD success must not carry payload")
        if self.authority_created or self.repository_mutation_allowed:
            raise TransportInputError("retrieval cannot create authority or allow repository mutation")

    def __repr__(self) -> str:
        return (
            "RetrievalResult("
            f"method={self.method.value!r}, category={self.category.value!r}, "
            f"safe_locator={self.safe_locator!r}, attempts={len(self.attempts)}, "
            f"payload={self.payload!r}, source_head={self.source_head!r}, "
            f"prior_artifact_retained={self.prior_artifact_retained}, "
            f"authority_created={self.authority_created}, "
            f"repository_mutation_allowed={self.repository_mutation_allowed})"
        )
