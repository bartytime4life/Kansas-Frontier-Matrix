"""Exact-byte validation for successful GET responses."""
from __future__ import annotations

import hmac

from .core import (
    ConnectorPrimitiveError,
    ResponseTooLargeError,
    SourceHeadObservation,
    TransportCategory,
    sanitize_response_headers,
    sha256_stream,
)
from ._transport_evaluation import Evaluation, failure_evaluation
from ._transport_request import TransportProfile, TransportRequest, TransportResponse
from ._transport_result import CapturedPayload


def evaluate_payload(
    request: TransportRequest,
    response: TransportResponse,
    profile: TransportProfile,
    observed_at,
    media_type: str,
) -> Evaluation:
    safe_headers = sanitize_response_headers(response.headers)
    declared, declared_failure = declared_length(
        safe_headers.get("content-length"), request, response, profile
    )
    if declared_failure is not None:
        return declared_failure
    try:
        digest_result = sha256_stream(
            response.body_chunks,
            max_bytes=profile.max_response_bytes,
        )
    except ResponseTooLargeError as exc:
        return failure_evaluation(
            TransportCategory.RESPONSE_TOO_LARGE,
            "OBSERVED_RESPONSE_TOO_LARGE",
            "The observed response exceeded the admitted byte budget.",
            request,
            response.status_code,
            bytes_received=exc.observed,
        )
    if digest_result.byte_length == 0:
        return failure_evaluation(
            TransportCategory.INVALID_RESPONSE_METADATA,
            "EMPTY_RESPONSE_BODY",
            "A successful GET response must contain captured bytes.",
            request,
            response.status_code,
        )
    if declared is not None and declared != digest_result.byte_length:
        return failure_evaluation(
            TransportCategory.INVALID_RESPONSE_METADATA,
            "CONTENT_LENGTH_MISMATCH",
            "Declared and observed response lengths differ.",
            request,
            response.status_code,
            bytes_received=digest_result.byte_length,
        )
    if request.expected_digest is not None and not hmac.compare_digest(
        request.expected_digest, digest_result.digest
    ):
        return failure_evaluation(
            TransportCategory.INTEGRITY_MISMATCH,
            "INTEGRITY_MISMATCH",
            "The captured bytes do not match the expected digest.",
            request,
            response.status_code,
            bytes_received=digest_result.byte_length,
        )
    try:
        source_head = SourceHeadObservation.from_headers(
            response.headers,
            observed_at=observed_at,
            computed_digest=digest_result.digest,
        )
        payload = CapturedPayload(
            response.body_chunks,
            digest_result.digest,
            digest_result.byte_length,
            media_type,
        )
    except (ConnectorPrimitiveError, TypeError, ValueError):
        return failure_evaluation(
            TransportCategory.INVALID_RESPONSE_METADATA,
            "INVALID_SOURCE_HEAD",
            "Source-head metadata is invalid.",
            request,
            response.status_code,
            bytes_received=digest_result.byte_length,
        )
    return Evaluation(
        TransportCategory.SUCCESS,
        "FETCH_SUCCESS",
        payload=payload,
        source_head=source_head,
        status_code=response.status_code,
        byte_length=digest_result.byte_length,
        digest=digest_result.digest,
    )


def declared_length(raw, request, response, profile):
    if raw is None:
        return None, None
    try:
        value = int(raw, 10)
    except ValueError:
        return None, failure_evaluation(
            TransportCategory.INVALID_RESPONSE_METADATA,
            "INVALID_CONTENT_LENGTH",
            "Content-Length metadata is invalid.",
            request,
            response.status_code,
            bytes_received=response.byte_length,
        )
    if value < 0:
        return None, failure_evaluation(
            TransportCategory.INVALID_RESPONSE_METADATA,
            "INVALID_CONTENT_LENGTH",
            "Content-Length metadata is invalid.",
            request,
            response.status_code,
            bytes_received=response.byte_length,
        )
    if value > profile.max_response_bytes:
        return None, failure_evaluation(
            TransportCategory.RESPONSE_TOO_LARGE,
            "DECLARED_RESPONSE_TOO_LARGE",
            "The declared response length exceeds the admitted byte budget.",
            request,
            response.status_code,
        )
    return value, None
