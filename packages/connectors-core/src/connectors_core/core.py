"""Pure, source-agnostic connector primitives for KFM.

This module deliberately performs no network, filesystem, environment, registry,
lifecycle, policy, receipt, release, or clock work at import time.  Callers own
all I/O and all governance-bearing decisions.

The primitives here preserve distinctions that are easy to collapse in source
integrations: weak versus strong ETags, source-reported versus observed time,
transport metadata versus content digests, transient versus permanent failures,
and integrity checks versus evidence or release authority.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from enum import Enum
import hashlib
import hmac
import math
import re
from types import MappingProxyType
from typing import Final, Iterable, Mapping
from urllib.parse import SplitResult, urlsplit, urlunsplit

_SHA256_RE: Final[re.Pattern[str]] = re.compile(r"^sha256:[a-f0-9]{64}$")
_ETAG_RE: Final[re.Pattern[str]] = re.compile(r'^(?P<weak>W/)?"(?P<opaque>[\x21\x23-\x5B\x5D-\x7E]*)"$')
_CONTROL_RE: Final[re.Pattern[str]] = re.compile(r"[\x00-\x1f\x7f]")
_SECRET_ASSIGNMENT_RE: Final[re.Pattern[str]] = re.compile(
    r"(?i)\b(authorization|proxy-authorization|cookie|set-cookie|x-api-key|api[-_]?key|"
    r"access[-_]?token|refresh[-_]?token|token|secret|password)\b\s*[:=]\s*"
    r"(?:\"[^\"]*\"|'[^']*'|[^\s,;]+)"
)
_BEARER_RE: Final[re.Pattern[str]] = re.compile(
    r"(?i)\bbearer\s+[A-Za-z0-9._~+/=-]+"
)
_QUERY_VALUE_RE: Final[re.Pattern[str]] = re.compile(r"([?&][^=\s&]+)=([^&\s]*)")

# Response metadata allowlist. Request headers are intentionally absent.
SAFE_RESPONSE_HEADERS: Final[frozenset[str]] = frozenset(
    {
        "cache-control",
        "content-length",
        "content-type",
        "date",
        "etag",
        "last-modified",
        "retry-after",
    }
)

_SECRET_HEADER_NAMES: Final[frozenset[str]] = frozenset(
    {
        "authorization",
        "proxy-authorization",
        "cookie",
        "set-cookie",
        "x-api-key",
        "api-key",
        "access-token",
        "refresh-token",
    }
)


class TransportCategory(str, Enum):
    """Finite package-local transport outcomes.

    These values are implementation observations, not SourceDescriptor admission,
    PolicyDecision, EvidenceBundle, lifecycle, release, or runtime-envelope states.
    """

    SUCCESS = "SUCCESS"
    NOT_MODIFIED = "NOT_MODIFIED"
    PARTIAL = "PARTIAL"
    TIMEOUT = "TIMEOUT"
    RATE_LIMITED = "RATE_LIMITED"
    AUTH_REQUIRED = "AUTH_REQUIRED"
    ACCESS_DENIED = "ACCESS_DENIED"
    NOT_FOUND = "NOT_FOUND"
    RETRY_EXHAUSTED = "RETRY_EXHAUSTED"
    CANCELLED = "CANCELLED"
    RESPONSE_TOO_LARGE = "RESPONSE_TOO_LARGE"
    INTEGRITY_MISMATCH = "INTEGRITY_MISMATCH"
    INVALID_RESPONSE_METADATA = "INVALID_RESPONSE_METADATA"
    UNSAFE_METADATA = "UNSAFE_METADATA"
    TRANSPORT_ERROR = "TRANSPORT_ERROR"


TRANSIENT_CATEGORIES: Final[frozenset[TransportCategory]] = frozenset(
    {
        TransportCategory.PARTIAL,
        TransportCategory.TIMEOUT,
        TransportCategory.RATE_LIMITED,
        TransportCategory.TRANSPORT_ERROR,
    }
)


class IntegrityStatus(str, Enum):
    MATCH = "MATCH"
    MISMATCH = "MISMATCH"


class ConnectorPrimitiveError(ValueError):
    """Base error for invalid primitive inputs."""


class ResponseTooLargeError(ConnectorPrimitiveError):
    """Raised when a caller-supplied byte budget would be exceeded."""

    def __init__(self, *, limit: int, observed: int) -> None:
        super().__init__(f"byte budget exceeded: limit={limit}, observed={observed}")
        self.limit = limit
        self.observed = observed


@dataclass(frozen=True, slots=True)
class ETag:
    """Opaque HTTP entity tag with weakness preserved explicitly."""

    opaque: str
    weak: bool = False

    def __post_init__(self) -> None:
        if len(self.opaque) > 512:
            raise ConnectorPrimitiveError("ETag opaque value exceeds 512 characters")
        if _CONTROL_RE.search(self.opaque) or '"' in self.opaque or "\\" in self.opaque:
            raise ConnectorPrimitiveError("ETag contains unsafe characters")

    @classmethod
    def parse(cls, value: str) -> "ETag":
        if not isinstance(value, str):
            raise TypeError("ETag value must be a string")
        match = _ETAG_RE.fullmatch(value.strip())
        if match is None:
            raise ConnectorPrimitiveError("ETag is not a safe quoted entity tag")
        return cls(opaque=match.group("opaque"), weak=bool(match.group("weak")))

    def render(self) -> str:
        prefix = "W/" if self.weak else ""
        return f'{prefix}"{self.opaque}"'


@dataclass(frozen=True, slots=True)
class SourceHeadObservation:
    """Immutable source-head metadata observed by a governed caller."""

    observed_at: datetime
    etag: ETag | None = None
    last_modified: datetime | None = None
    content_length: int | None = None
    upstream_revision: str | None = None
    computed_digest: str | None = None

    def __post_init__(self) -> None:
        _require_aware_datetime(self.observed_at, "observed_at")
        if self.last_modified is not None:
            _require_aware_datetime(self.last_modified, "last_modified")
            if self.last_modified > self.observed_at:
                raise ConnectorPrimitiveError(
                    "last_modified cannot be after observed_at in this observation"
                )
        if self.content_length is not None and self.content_length < 0:
            raise ConnectorPrimitiveError("content_length must be non-negative")
        if self.upstream_revision is not None:
            _validate_safe_text(self.upstream_revision, "upstream_revision", max_length=512)
        if self.computed_digest is not None:
            validate_sha256_digest(self.computed_digest)

    @classmethod
    def from_headers(
        cls,
        headers: Mapping[str, str],
        *,
        observed_at: datetime,
        upstream_revision: str | None = None,
        computed_digest: str | None = None,
    ) -> "SourceHeadObservation":
        safe = sanitize_response_headers(headers)
        etag = ETag.parse(safe["etag"]) if "etag" in safe else None
        last_modified = (
            parse_http_datetime(safe["last-modified"])
            if "last-modified" in safe
            else None
        )
        content_length: int | None = None
        if "content-length" in safe:
            try:
                content_length = int(safe["content-length"], 10)
            except ValueError as exc:
                raise ConnectorPrimitiveError(
                    "content-length must be a base-10 integer"
                ) from exc
            if content_length < 0:
                raise ConnectorPrimitiveError("content-length must be non-negative")
        return cls(
            observed_at=observed_at,
            etag=etag,
            last_modified=last_modified,
            content_length=content_length,
            upstream_revision=upstream_revision,
            computed_digest=computed_digest,
        )


@dataclass(frozen=True, slots=True)
class RetryDecision:
    retry: bool
    delay_seconds: float
    next_attempt: int | None
    reason: str

    def __post_init__(self) -> None:
        if not math.isfinite(self.delay_seconds) or self.delay_seconds < 0:
            raise ConnectorPrimitiveError("delay_seconds must be finite and non-negative")
        if self.retry and self.next_attempt is None:
            raise ConnectorPrimitiveError("retry decisions require next_attempt")
        if not self.retry and self.next_attempt is not None:
            raise ConnectorPrimitiveError("terminal decisions must not carry next_attempt")
        _validate_safe_text(self.reason, "reason", max_length=120)


@dataclass(frozen=True, slots=True)
class RetryPolicy:
    """Deterministic bounded retry policy.

    ``attempt_number`` passed to :meth:`decide` is the just-completed 1-based
    attempt. Jitter is caller-injected as a unit value in ``[0, 1]``; no ambient
    randomness is sampled.
    """

    max_attempts: int = 3
    base_delay_seconds: float = 1.0
    multiplier: float = 2.0
    max_delay_seconds: float = 30.0
    deadline_seconds: float = 60.0
    jitter_fraction: float = 0.0

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ConnectorPrimitiveError("max_attempts must be at least 1")
        for name, value in (
            ("base_delay_seconds", self.base_delay_seconds),
            ("max_delay_seconds", self.max_delay_seconds),
            ("deadline_seconds", self.deadline_seconds),
            ("multiplier", self.multiplier),
            ("jitter_fraction", self.jitter_fraction),
        ):
            if not math.isfinite(value):
                raise ConnectorPrimitiveError(f"{name} must be finite")
        if self.base_delay_seconds < 0:
            raise ConnectorPrimitiveError("base_delay_seconds must be non-negative")
        if self.multiplier < 1:
            raise ConnectorPrimitiveError("multiplier must be at least 1")
        if self.max_delay_seconds < self.base_delay_seconds:
            raise ConnectorPrimitiveError(
                "max_delay_seconds must be at least base_delay_seconds"
            )
        if self.deadline_seconds <= 0:
            raise ConnectorPrimitiveError("deadline_seconds must be positive")
        if not 0 <= self.jitter_fraction <= 1:
            raise ConnectorPrimitiveError("jitter_fraction must be within 0..1")

    def decide(
        self,
        category: TransportCategory,
        *,
        attempt_number: int,
        elapsed_seconds: float,
        retry_after_seconds: float | None = None,
        jitter_unit: float = 0.5,
    ) -> RetryDecision:
        if attempt_number < 1:
            raise ConnectorPrimitiveError("attempt_number must be at least 1")
        if not math.isfinite(elapsed_seconds) or elapsed_seconds < 0:
            raise ConnectorPrimitiveError(
                "elapsed_seconds must be finite and non-negative"
            )
        if retry_after_seconds is not None and (
            not math.isfinite(retry_after_seconds) or retry_after_seconds < 0
        ):
            raise ConnectorPrimitiveError(
                "retry_after_seconds must be finite and non-negative"
            )
        if not math.isfinite(jitter_unit) or not 0 <= jitter_unit <= 1:
            raise ConnectorPrimitiveError("jitter_unit must be within 0..1")

        if category in {TransportCategory.SUCCESS, TransportCategory.NOT_MODIFIED}:
            return RetryDecision(False, 0.0, None, "terminal_success")
        if category not in TRANSIENT_CATEGORIES:
            return RetryDecision(False, 0.0, None, "permanent_or_unsafe_failure")
        if attempt_number >= self.max_attempts:
            return RetryDecision(False, 0.0, None, "attempt_limit_reached")
        if elapsed_seconds >= self.deadline_seconds:
            return RetryDecision(False, 0.0, None, "deadline_reached")

        exponential = self.base_delay_seconds * (
            self.multiplier ** (attempt_number - 1)
        )
        base = min(exponential, self.max_delay_seconds)
        if retry_after_seconds is not None:
            base = max(base, min(retry_after_seconds, self.max_delay_seconds))

        # Symmetric deterministic jitter around the base delay.
        factor = 1.0 + self.jitter_fraction * ((2.0 * jitter_unit) - 1.0)
        delay = max(0.0, min(base * factor, self.max_delay_seconds))
        remaining = self.deadline_seconds - elapsed_seconds
        if delay >= remaining:
            return RetryDecision(False, 0.0, None, "deadline_would_be_exceeded")
        return RetryDecision(True, delay, attempt_number + 1, "transient_retry")


@dataclass(frozen=True, slots=True)
class DigestResult:
    digest: str
    byte_length: int

    def __post_init__(self) -> None:
        validate_sha256_digest(self.digest)
        if self.byte_length < 0:
            raise ConnectorPrimitiveError("byte_length must be non-negative")


@dataclass(frozen=True, slots=True)
class IntegrityResult:
    status: IntegrityStatus
    expected_digest: str
    observed_digest: str
    byte_length: int

    def __post_init__(self) -> None:
        validate_sha256_digest(self.expected_digest)
        validate_sha256_digest(self.observed_digest)
        if self.byte_length < 0:
            raise ConnectorPrimitiveError("byte_length must be non-negative")
        expected_status = (
            IntegrityStatus.MATCH
            if hmac.compare_digest(self.expected_digest, self.observed_digest)
            else IntegrityStatus.MISMATCH
        )
        if self.status is not expected_status:
            raise ConnectorPrimitiveError("integrity status does not match digests")


@dataclass(frozen=True, slots=True)
class FailureDetail:
    """Value-minimized, secret-safe failure information for governed callers."""

    category: TransportCategory
    code: str
    public_message: str
    status_code: int | None = None
    safe_locator: str | None = None
    attempt_count: int = 1
    bytes_received: int = 0

    def __post_init__(self) -> None:
        if self.category in {TransportCategory.SUCCESS, TransportCategory.NOT_MODIFIED}:
            raise ConnectorPrimitiveError("FailureDetail requires a failure category")
        _validate_safe_text(self.code, "code", max_length=120)
        _validate_safe_text(self.public_message, "public_message", max_length=500)
        if redact_text(self.public_message) != self.public_message:
            raise ConnectorPrimitiveError("public_message contains secret-like material")
        if self.status_code is not None and not 100 <= self.status_code <= 599:
            raise ConnectorPrimitiveError("status_code must be within 100..599")
        if self.safe_locator is not None:
            if redact_url(self.safe_locator) != self.safe_locator:
                raise ConnectorPrimitiveError("safe_locator is not redacted")
        if self.attempt_count < 1:
            raise ConnectorPrimitiveError("attempt_count must be at least 1")
        if self.bytes_received < 0:
            raise ConnectorPrimitiveError("bytes_received must be non-negative")


def validate_sha256_digest(value: str) -> str:
    if not isinstance(value, str) or _SHA256_RE.fullmatch(value) is None:
        raise ConnectorPrimitiveError(
            "digest must match sha256:<64 lowercase hexadecimal characters>"
        )
    return value


def sha256_stream(
    chunks: Iterable[bytes | bytearray | memoryview],
    *,
    max_bytes: int | None = None,
) -> DigestResult:
    """Hash exact bytes incrementally without implicit normalization."""

    if max_bytes is not None and max_bytes < 0:
        raise ConnectorPrimitiveError("max_bytes must be non-negative")
    digest = hashlib.sha256()
    total = 0
    for chunk in chunks:
        if not isinstance(chunk, (bytes, bytearray, memoryview)):
            raise TypeError("SHA-256 chunks must be bytes-like")
        view = memoryview(chunk)
        total += view.nbytes
        if max_bytes is not None and total > max_bytes:
            raise ResponseTooLargeError(limit=max_bytes, observed=total)
        digest.update(view)
    return DigestResult(digest=f"sha256:{digest.hexdigest()}", byte_length=total)


def verify_sha256_stream(
    chunks: Iterable[bytes | bytearray | memoryview],
    expected_digest: str,
    *,
    max_bytes: int | None = None,
) -> IntegrityResult:
    expected = validate_sha256_digest(expected_digest)
    observed = sha256_stream(chunks, max_bytes=max_bytes)
    status = (
        IntegrityStatus.MATCH
        if hmac.compare_digest(expected, observed.digest)
        else IntegrityStatus.MISMATCH
    )
    return IntegrityResult(
        status=status,
        expected_digest=expected,
        observed_digest=observed.digest,
        byte_length=observed.byte_length,
    )


def sanitize_response_headers(
    headers: Mapping[str, str],
    *,
    allowlist: frozenset[str] = SAFE_RESPONSE_HEADERS,
) -> Mapping[str, str]:
    """Return an immutable allowlisted, lower-case response-header projection."""

    safe: dict[str, str] = {}
    for raw_name, raw_value in headers.items():
        if not isinstance(raw_name, str) or not isinstance(raw_value, str):
            raise TypeError("header names and values must be strings")
        name = raw_name.strip().lower()
        if not name or _CONTROL_RE.search(name):
            raise ConnectorPrimitiveError("header name contains unsafe characters")
        if name in _SECRET_HEADER_NAMES:
            continue
        if name not in allowlist:
            continue
        value = raw_value.strip()
        _validate_safe_text(value, f"header:{name}", max_length=2048)
        safe[name] = value
    return MappingProxyType(dict(sorted(safe.items())))


def parse_http_datetime(value: str) -> datetime:
    """Parse an HTTP date and normalize it to timezone-aware UTC."""

    _validate_safe_text(value, "http_datetime", max_length=128)
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ConnectorPrimitiveError("invalid HTTP date") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def redact_url(value: str) -> str:
    """Return a diagnostic-safe HTTPS/HTTP URL without userinfo/query/fragment."""

    if not isinstance(value, str):
        raise TypeError("URL must be a string")
    _validate_safe_text(value, "url", max_length=4096)
    parts = urlsplit(value)
    if parts.scheme.lower() not in {"http", "https"}:
        raise ConnectorPrimitiveError("diagnostic URL must use http or https")
    if parts.hostname is None:
        raise ConnectorPrimitiveError("diagnostic URL requires a hostname")
    hostname = parts.hostname.lower()
    if _CONTROL_RE.search(hostname):
        raise ConnectorPrimitiveError("URL hostname contains unsafe characters")
    if ":" in hostname and not hostname.startswith("["):
        hostname = f"[{hostname}]"
    netloc = hostname
    if parts.port is not None:
        netloc = f"{netloc}:{parts.port}"
    safe = SplitResult(parts.scheme.lower(), netloc, parts.path or "/", "", "")
    return urlunsplit(safe)


def redact_text(value: str, *, replacement: str = "<redacted>") -> str:
    """Redact common credential forms and URL query values from diagnostics."""

    if not isinstance(value, str):
        raise TypeError("diagnostic text must be a string")
    if not replacement or _CONTROL_RE.search(replacement):
        raise ConnectorPrimitiveError("replacement must be non-empty and control-free")
    result = _BEARER_RE.sub(f"Bearer {replacement}", value)
    result = _SECRET_ASSIGNMENT_RE.sub(
        lambda match: f"{match.group(1)}={replacement}", result
    )
    result = _QUERY_VALUE_RE.sub(lambda match: f"{match.group(1)}={replacement}", result)
    return result


def make_failure_detail(
    category: TransportCategory,
    *,
    code: str,
    message: str,
    status_code: int | None = None,
    locator: str | None = None,
    attempt_count: int = 1,
    bytes_received: int = 0,
) -> FailureDetail:
    """Construct a value-minimized failure after redacting diagnostics."""

    public_message = redact_text(message)[:500]
    safe_locator = redact_url(locator) if locator is not None else None
    return FailureDetail(
        category=category,
        code=code,
        public_message=public_message,
        status_code=status_code,
        safe_locator=safe_locator,
        attempt_count=attempt_count,
        bytes_received=bytes_received,
    )


def _require_aware_datetime(value: datetime, name: str) -> None:
    if not isinstance(value, datetime):
        raise TypeError(f"{name} must be a datetime")
    if value.tzinfo is None or value.utcoffset() is None:
        raise ConnectorPrimitiveError(f"{name} must be timezone-aware")


def _validate_safe_text(value: str, name: str, *, max_length: int) -> None:
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a string")
    if not value:
        raise ConnectorPrimitiveError(f"{name} must be non-empty")
    if len(value) > max_length:
        raise ConnectorPrimitiveError(f"{name} exceeds {max_length} characters")
    if _CONTROL_RE.search(value):
        raise ConnectorPrimitiveError(f"{name} contains control characters")


__all__ = [
    "ConnectorPrimitiveError",
    "DigestResult",
    "ETag",
    "FailureDetail",
    "IntegrityResult",
    "IntegrityStatus",
    "ResponseTooLargeError",
    "RetryDecision",
    "RetryPolicy",
    "SAFE_RESPONSE_HEADERS",
    "SourceHeadObservation",
    "TRANSIENT_CATEGORIES",
    "TransportCategory",
    "make_failure_detail",
    "parse_http_datetime",
    "redact_text",
    "redact_url",
    "sanitize_response_headers",
    "sha256_stream",
    "validate_sha256_digest",
    "verify_sha256_stream",
]
