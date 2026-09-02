"""Internal response-evaluation record and failure constructor."""
from __future__ import annotations

from dataclasses import dataclass

from .core import FailureDetail, SourceHeadObservation, TransportCategory, make_failure_detail
from ._transport_request import TransportRequest
from ._transport_result import CapturedPayload


@dataclass(frozen=True, slots=True)
class Evaluation:
    category: TransportCategory
    code: str
    payload: CapturedPayload | None = None
    source_head: SourceHeadObservation | None = None
    failure: FailureDetail | None = None
    prior_artifact_retained: bool = False
    status_code: int | None = None
    byte_length: int = 0
    digest: str | None = None
    retry_after_seconds: float | None = None


def failure_evaluation(
    category: TransportCategory,
    code: str,
    message: str,
    request: TransportRequest,
    status_code: int | None,
    *,
    bytes_received: int = 0,
) -> Evaluation:
    return Evaluation(
        category,
        code,
        failure=make_failure_detail(
            category,
            code=code,
            message=message,
            status_code=status_code,
            locator=request.url,
            bytes_received=bytes_received,
        ),
        status_code=status_code,
        byte_length=bytes_received,
    )
