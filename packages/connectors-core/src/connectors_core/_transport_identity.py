"""Pure validation and redaction helpers for connector transport values."""
from __future__ import annotations

import re
from types import MappingProxyType
from typing import Mapping
from urllib.parse import SplitResult, urlsplit

from .core import redact_url

_PROFILE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
_HEADER_RE = re.compile(r"^[!#$%&'*+.^_`|~0-9A-Za-z-]+$")
_MEDIA_RE = re.compile(r"^[A-Za-z0-9!#$&^_.+-]+/[A-Za-z0-9!#$&^_.+-]+$")
_CONTROL_RE = re.compile(r"[\x00-\x1f\x7f]")


class TransportValueError(ValueError):
    """Unsafe or malformed transport value."""


def validate_profile_id(value: str) -> str:
    if not isinstance(value, str) or _PROFILE_RE.fullmatch(value) is None:
        raise TransportValueError("profile_id must be a bounded stable identifier")
    return value


def normalize_host(value: str) -> str:
    if not isinstance(value, str) or not value:
        raise TransportValueError("host must be a non-empty string")
    if _CONTROL_RE.search(value) or any(ch in value for ch in "/\\:@?#*"):
        raise TransportValueError("host contains unsafe characters")
    host = value.rstrip(".").lower()
    if not host:
        raise TransportValueError("host must be non-empty")
    try:
        host.encode("idna")
    except UnicodeError as exc:
        raise TransportValueError("host is not valid IDNA") from exc
    return host


def normalize_media_type(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("media type must be a string")
    result = value.strip().lower()
    if _MEDIA_RE.fullmatch(result) is None:
        raise TransportValueError("media type must be an exact type/subtype token")
    return result


def parse_url(value: str) -> SplitResult:
    if not isinstance(value, str) or not value:
        raise TransportValueError("request URL must be a non-empty string")
    if len(value) > 4096 or _CONTROL_RE.search(value) or "\\" in value:
        raise TransportValueError("request URL is unsafe or too large")
    parts = urlsplit(value)
    if parts.scheme.lower() != "https" or parts.hostname is None:
        raise TransportValueError("request URL must be absolute HTTPS")
    if parts.username is not None or parts.password is not None:
        raise TransportValueError("credentials must not be embedded in request URLs")
    if parts.fragment:
        raise TransportValueError("request URL fragments are not permitted")
    try:
        _ = parts.port
    except ValueError as exc:
        raise TransportValueError("request URL port is invalid") from exc
    return parts


def url_identity(value: str) -> tuple[str, str, int, str, str]:
    parts = parse_url(value)
    return (
        parts.scheme.lower(),
        normalize_host(parts.hostname or ""),
        parts.port or 443,
        parts.path or "/",
        parts.query,
    )


def safe_locator(value: str) -> str:
    parse_url(value)
    return redact_url(value)


def freeze_headers(headers: Mapping[str, str]) -> Mapping[str, str]:
    if not isinstance(headers, Mapping):
        raise TypeError("headers must be a mapping")
    result: dict[str, str] = {}
    for raw_name, raw_value in headers.items():
        if not isinstance(raw_name, str) or not isinstance(raw_value, str):
            raise TypeError("header names and values must be strings")
        name = raw_name.strip().lower()
        if _HEADER_RE.fullmatch(name) is None or name in result:
            raise TransportValueError("header name is invalid or duplicated")
        if len(raw_value) > 8192 or _CONTROL_RE.search(raw_value):
            raise TransportValueError("header value is unsafe or too large")
        result[name] = raw_value
    return MappingProxyType(dict(sorted(result.items())))
