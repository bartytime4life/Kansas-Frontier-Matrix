"""Attempt, failure, clock, and result helpers for transport execution."""
from __future__ import annotations

from datetime import datetime
import math

from .core import FailureDetail, TransportCategory, make_failure_detail
from ._transport_evaluation import Evaluation
from ._transport_request import TransportInputError, TransportRequest
from ._transport_result import AttemptRecord, RetrievalResult


def failure_detail(category, code, message, request, attempt_number) -> FailureDetail:
    return make_failure_detail(
        category,
        code=code,
        message=message,
        locator=request.url,
        attempt_count=max(1, attempt_number),
    )


def attempt_record(
    attempt_number: int,
    evaluation: Evaluation,
    observed_at: datetime,
    duration: float,
    request: TransportRequest,
    *,
    retry_delay: float = 0.0,
) -> AttemptRecord:
    return AttemptRecord(
        attempt_number=attempt_number,
        category=evaluation.category,
        code=evaluation.code,
        observed_at=observed_at,
        duration_seconds=duration,
        safe_locator=request.safe_locator,
        status_code=evaluation.status_code,
        byte_length=evaluation.byte_length,
        digest=evaluation.digest,
        retry_delay_seconds=retry_delay,
    )


def failed_result(request, category, attempts, failure) -> RetrievalResult:
    return RetrievalResult(
        method=request.method,
        category=category,
        safe_locator=request.safe_locator,
        attempts=tuple(attempts),
        failure=failure,
    )


def read_now(clock) -> datetime:
    value = clock.now()
    if not isinstance(value, datetime) or value.tzinfo is None or value.utcoffset() is None:
        raise TransportInputError("clock.now() must return a timezone-aware datetime")
    return value


def read_monotonic(clock) -> float:
    value = clock.monotonic()
    if not isinstance(value, (int, float)) or not math.isfinite(float(value)):
        raise TransportInputError("clock.monotonic() must return a finite number")
    return float(value)
