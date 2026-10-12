"""HTTP status, redirect, method, and media-type response evaluation."""
from __future__ import annotations

from .core import (
    ConnectorPrimitiveError,
    SourceHeadObservation,
    TransportCategory,
    sanitize_response_headers,
)
from ._transport_evaluation import Evaluation, failure_evaluation
from ._transport_identity import TransportValueError, normalize_media_type, url_identity
from ._transport_request import TransportMethod, TransportProfile, TransportRequest, TransportResponse
from ._transport_retry import evaluate_rate_limit


def evaluate_status(
    request: TransportRequest,
    response: TransportResponse,
    profile: TransportProfile,
    observed_at,
) -> tuple[Evaluation | None, str | None]:
    final_url = response.final_url or request.url
    try:
        profile.validate_request(TransportRequest(request.method, final_url))
    except (ConnectorPrimitiveError, TypeError, ValueError):
        return failure_evaluation(
            TransportCategory.UNSAFE_METADATA,
            "REDIRECT_BLOCKED",
            "Redirected or final target is not admitted.",
            request,
            response.status_code,
        ), None
    if url_identity(final_url) != url_identity(request.url):
        return failure_evaluation(
            TransportCategory.UNSAFE_METADATA,
            "REDIRECT_BLOCKED",
            "Redirects or final-target changes are not permitted.",
            request,
            response.status_code,
        ), None

    status = response.status_code
    if status == 304:
        return evaluate_not_modified(request, response, observed_at), None
    if 300 <= status <= 399:
        return failure_evaluation(
            TransportCategory.UNSAFE_METADATA,
            "REDIRECT_BLOCKED",
            "Redirect responses are not permitted.",
            request,
            status,
        ), None
    if status == 206:
        return failure_evaluation(
            TransportCategory.PARTIAL,
            "PARTIAL_CONTENT",
            "A range or partial response is not complete source capture.",
            request,
            status,
            bytes_received=response.byte_length,
        ), None
    if status == 429:
        return evaluate_rate_limit(request, response, observed_at), None
    if status == 401:
        return failure_evaluation(
            TransportCategory.AUTH_REQUIRED,
            "AUTH_REQUIRED",
            "Authentication is required.",
            request,
            status,
        ), None
    if status in {403, 451}:
        return failure_evaluation(
            TransportCategory.ACCESS_DENIED,
            "ACCESS_DENIED",
            "Access to the source was denied.",
            request,
            status,
        ), None
    if status == 404:
        return failure_evaluation(
            TransportCategory.NOT_FOUND,
            "NOT_FOUND",
            "The source surface was not found.",
            request,
            status,
        ), None
    if status >= 500:
        return failure_evaluation(
            TransportCategory.TRANSPORT_ERROR,
            "UPSTREAM_ERROR",
            "The source returned an upstream error.",
            request,
            status,
        ), None
    if not 200 <= status <= 299:
        return failure_evaluation(
            TransportCategory.TRANSPORT_ERROR,
            "UNEXPECTED_STATUS",
            "The source returned an unexpected status.",
            request,
            status,
        ), None

    safe_headers = sanitize_response_headers(response.headers)
    raw_media = safe_headers.get("content-type")
    if raw_media is None:
        return failure_evaluation(
            TransportCategory.INVALID_RESPONSE_METADATA,
            "MISSING_CONTENT_TYPE",
            "The response is missing Content-Type metadata.",
            request,
            status,
        ), None
    try:
        media_type = normalize_media_type(raw_media.split(";", 1)[0])
    except (TransportValueError, TypeError):
        return failure_evaluation(
            TransportCategory.INVALID_RESPONSE_METADATA,
            "INVALID_MEDIA_TYPE",
            "The response media type is invalid.",
            request,
            status,
        ), None
    if media_type not in profile.allowed_media_types:
        return failure_evaluation(
            TransportCategory.INVALID_RESPONSE_METADATA,
            "WRONG_MEDIA_TYPE",
            "The response media type is not admitted.",
            request,
            status,
        ), None

    if request.method is TransportMethod.HEAD:
        if response.body_chunks:
            return failure_evaluation(
                TransportCategory.INVALID_RESPONSE_METADATA,
                "HEAD_BODY_UNEXPECTED",
                "HEAD responses must not carry a body.",
                request,
                status,
            ), None
        try:
            source_head = SourceHeadObservation.from_headers(response.headers, observed_at=observed_at)
        except (ConnectorPrimitiveError, TypeError, ValueError):
            return failure_evaluation(
                TransportCategory.INVALID_RESPONSE_METADATA,
                "INVALID_SOURCE_HEAD",
                "Source-head metadata is invalid.",
                request,
                status,
            ), None
        return Evaluation(
            TransportCategory.SUCCESS,
            "HEAD_SUCCESS",
            source_head=source_head,
            status_code=status,
        ), None

    if not response.complete:
        return failure_evaluation(
            TransportCategory.PARTIAL,
            "RESPONSE_PARTIAL",
            "The response body is partial.",
            request,
            status,
            bytes_received=response.byte_length,
        ), None
    return None, media_type


def evaluate_not_modified(request, response, observed_at):
    if response.body_chunks:
        return failure_evaluation(
            TransportCategory.INVALID_RESPONSE_METADATA,
            "NOT_MODIFIED_BODY_UNEXPECTED",
            "NOT_MODIFIED must not carry a body.",
            request,
            response.status_code,
        )
    try:
        source_head = SourceHeadObservation.from_headers(response.headers, observed_at=observed_at)
    except (ConnectorPrimitiveError, TypeError, ValueError):
        return failure_evaluation(
            TransportCategory.INVALID_RESPONSE_METADATA,
            "INVALID_NOT_MODIFIED_HEAD",
            "NOT_MODIFIED source-head metadata is invalid.",
            request,
            response.status_code,
        )
    return Evaluation(
        TransportCategory.NOT_MODIFIED,
        "NOT_MODIFIED",
        source_head=source_head,
        prior_artifact_retained=True,
        status_code=response.status_code,
    )