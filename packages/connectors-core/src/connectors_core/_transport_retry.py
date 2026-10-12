"""Retry-After parsing and rate-limit response evaluation."""
from __future__ import annotations

from dataclasses import replace
from datetime import datetime

from .core import ConnectorPrimitiveError, TransportCategory, parse_http_datetime, sanitize_response_headers
from ._transport_evaluation import Evaluation, failure_evaluation
from ._transport_request import TransportInputError, TransportRequest, TransportResponse


def parse_retry_after(value: str | None, *, observed_at: datetime) -> float | None:
    if value is None:
        return None
    if observed_at.tzinfo is None or observed_at.utcoffset() is None:
        raise TransportInputError("observed_at must be timezone-aware")
    if not isinstance(value, str) or not value.strip():
        raise TransportInputError("Retry-After must be a non-empty string")
    raw = value.strip()
    if raw.isdigit():
        seconds = int(raw, 10)
    else:
        try:
            target = parse_http_datetime(raw)
        except ConnectorPrimitiveError as exc:
            raise TransportInputError("Retry-After is not delta-seconds or an HTTP date") from exc
        seconds = max(0, int((target - observed_at).total_seconds()))
    if seconds > 86400:
        raise TransportInputError("Retry-After exceeds the one-day safety bound")
    return float(seconds)


def evaluate_rate_limit(
    request: TransportRequest,
    response: TransportResponse,
    observed_at: datetime,
) -> Evaluation:
    result = failure_evaluation(
        TransportCategory.RATE_LIMITED,
        "RATE_LIMITED",
        "The source rate limited the request.",
        request,
        response.status_code,
    )
    try:
        retry_after = parse_retry_after(
            sanitize_response_headers(response.headers).get("retry-after"),
            observed_at=observed_at,
        )
    except (ConnectorPrimitiveError, TransportInputError, TypeError, ValueError):
        return failure_evaluation(
            TransportCategory.INVALID_RESPONSE_METADATA,
            "INVALID_RETRY_AFTER",
            "Retry-After metadata is invalid.",
            request,
            response.status_code,
        )
    return replace(result, retry_after_seconds=retry_after)
