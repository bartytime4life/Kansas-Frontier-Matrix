"""Immutable request, response, and source-profile types."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import math
from typing import Mapping

from .core import ConnectorPrimitiveError, validate_sha256_digest
from ._transport_identity import (
    TransportValueError,
    freeze_headers,
    normalize_host,
    normalize_media_type,
    parse_url,
    safe_locator,
    validate_profile_id,
)


class TransportMethod(str, Enum):
    GET = "GET"
    HEAD = "HEAD"


class TransportInputError(ConnectorPrimitiveError):
    """Invalid request, response, profile, or injected dependency."""


class TransportCancelledError(RuntimeError):
    """Explicit caller-owned transport cancellation."""


@dataclass(frozen=True, slots=True)
class TransportProfile:
    profile_id: str
    allowed_hosts: frozenset[str]
    allowed_media_types: frozenset[str]
    allowed_ports: frozenset[int] = frozenset({443})
    timeout_seconds: float = 30.0
    max_response_bytes: int = 8 * 1024 * 1024

    def __post_init__(self) -> None:
        try:
            validate_profile_id(self.profile_id)
            hosts = frozenset(normalize_host(v) for v in self.allowed_hosts)
            media = frozenset(normalize_media_type(v) for v in self.allowed_media_types)
        except TransportValueError as exc:
            raise TransportInputError(str(exc)) from exc
        ports = frozenset(self.allowed_ports)
        if not hosts or not media:
            raise TransportInputError("profile requires exact hosts and media types")
        if not ports or any(not isinstance(v, int) or not 1 <= v <= 65535 for v in ports):
            raise TransportInputError("allowed_ports must contain valid TCP ports")
        if not math.isfinite(self.timeout_seconds) or self.timeout_seconds <= 0:
            raise TransportInputError("timeout_seconds must be finite and positive")
        if not isinstance(self.max_response_bytes, int) or self.max_response_bytes <= 0:
            raise TransportInputError("max_response_bytes must be a positive integer")
        object.__setattr__(self, "allowed_hosts", hosts)
        object.__setattr__(self, "allowed_media_types", media)
        object.__setattr__(self, "allowed_ports", ports)

    def validate_request(self, request: "TransportRequest") -> None:
        try:
            parts = parse_url(request.url)
            host = normalize_host(parts.hostname or "")
        except TransportValueError as exc:
            raise TransportInputError(str(exc)) from exc
        if host not in self.allowed_hosts:
            raise TransportInputError("request host is not admitted by the profile")
        if (parts.port or 443) not in self.allowed_ports:
            raise TransportInputError("request port is not admitted by the profile")


@dataclass(frozen=True, slots=True, repr=False)
class TransportRequest:
    method: TransportMethod
    url: str
    headers: Mapping[str, str] = field(default_factory=dict, repr=False)
    expected_digest: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.method, TransportMethod):
            try:
                object.__setattr__(self, "method", TransportMethod(self.method))
            except (TypeError, ValueError) as exc:
                raise TransportInputError("unsupported transport method") from exc
        try:
            parse_url(self.url)
            object.__setattr__(self, "headers", freeze_headers(self.headers))
        except TransportValueError as exc:
            raise TransportInputError(str(exc)) from exc
        if self.expected_digest is not None:
            validate_sha256_digest(self.expected_digest)
            if self.method is TransportMethod.HEAD:
                raise TransportInputError("HEAD cannot declare an expected body digest")

    @property
    def safe_locator(self) -> str:
        return safe_locator(self.url)

    @property
    def header_names(self) -> tuple[str, ...]:
        return tuple(self.headers)

    def __repr__(self) -> str:
        return (
            "TransportRequest("
            f"method={self.method.value!r}, safe_locator={self.safe_locator!r}, "
            f"header_names={self.header_names!r}, expected_digest={self.expected_digest!r})"
        )


@dataclass(frozen=True, slots=True, repr=False)
class TransportResponse:
    status_code: int
    headers: Mapping[str, str]
    body_chunks: tuple[bytes, ...] = ()
    final_url: str | None = None
    complete: bool = True

    def __post_init__(self) -> None:
        if not isinstance(self.status_code, int) or not 100 <= self.status_code <= 599:
            raise TransportInputError("status_code must be within 100..599")
        try:
            object.__setattr__(self, "headers", freeze_headers(self.headers))
            if self.final_url is not None:
                parse_url(self.final_url)
        except TransportValueError as exc:
            raise TransportInputError(str(exc)) from exc
        chunks: list[bytes] = []
        for chunk in self.body_chunks:
            if not isinstance(chunk, (bytes, bytearray, memoryview)):
                raise TypeError("response body chunks must be bytes-like")
            chunks.append(bytes(chunk))
        object.__setattr__(self, "body_chunks", tuple(chunks))
        if not isinstance(self.complete, bool):
            raise TypeError("complete must be boolean")

    @property
    def byte_length(self) -> int:
        return sum(len(v) for v in self.body_chunks)

    def __repr__(self) -> str:
        locator = safe_locator(self.final_url) if self.final_url else None
        return (
            "TransportResponse("
            f"status_code={self.status_code}, header_names={tuple(self.headers)!r}, "
            f"byte_length={self.byte_length}, final_locator={locator!r}, complete={self.complete})"
        )
