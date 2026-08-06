"""Response evaluator joining status/metadata and exact-byte validation."""
from __future__ import annotations

from ._transport_payload import evaluate_payload
from ._transport_request import TransportProfile, TransportRequest, TransportResponse
from ._transport_status import evaluate_status


def evaluate_response(request, response, profile, observed_at):
    result, media_type = evaluate_status(request, response, profile, observed_at)
    if result is not None:
        return result
    if media_type is None:
        raise AssertionError("successful GET evaluation requires a media type")
    return evaluate_payload(request, response, profile, observed_at, media_type)
