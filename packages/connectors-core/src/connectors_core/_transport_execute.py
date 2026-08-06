"""Bounded executor for caller-injected connector transports."""
from __future__ import annotations

from dataclasses import replace

from .core import RetryPolicy, TRANSIENT_CATEGORIES, TransportCategory
from ._transport_eval import evaluate_response
from ._transport_evaluation import Evaluation
from ._transport_protocols import CancellationToken, Clock, JitterSource, Sleeper, Transport
from ._transport_records import (
    attempt_record,
    failed_result,
    failure_detail,
    read_monotonic,
    read_now,
)
from ._transport_request import (
    TransportCancelledError,
    TransportInputError,
    TransportProfile,
    TransportRequest,
    TransportResponse,
)
from ._transport_result import AttemptRecord, RetrievalResult

_EXHAUSTED_REASONS = frozenset(
    {"attempt_limit_reached", "deadline_reached", "deadline_would_be_exceeded"}
)


class _MidpointJitter:
    def unit(self, _attempt_number: int) -> float:
        return 0.5


class _NeverCancelled:
    def is_cancelled(self) -> bool:
        return False


def execute_retrieval(
    transport: Transport,
    request: TransportRequest,
    *,
    profile: TransportProfile,
    retry_policy: RetryPolicy,
    clock: Clock,
    sleeper: Sleeper,
    jitter_source: JitterSource | None = None,
    cancellation: CancellationToken | None = None,
) -> RetrievalResult:
    profile.validate_request(request)
    if not isinstance(retry_policy, RetryPolicy):
        raise TypeError("retry_policy must be a RetryPolicy")
    jitter = jitter_source or _MidpointJitter()
    cancel = cancellation or _NeverCancelled()
    start = read_monotonic(clock)
    attempts: list[AttemptRecord] = []

    for number in range(1, retry_policy.max_attempts + 1):
        observed_at = read_now(clock)
        if cancel.is_cancelled():
            failure = failure_detail(
                TransportCategory.CANCELLED,
                "CALLER_CANCELLED",
                "Retrieval was cancelled by the caller.",
                request,
                max(1, number),
            )
            attempts.append(
                AttemptRecord(
                    attempt_number=0 if not attempts else number,
                    category=TransportCategory.CANCELLED,
                    code="CALLER_CANCELLED",
                    observed_at=observed_at,
                    duration_seconds=0.0,
                    safe_locator=request.safe_locator,
                )
            )
            return failed_result(request, TransportCategory.CANCELLED, attempts, failure)

        before = read_monotonic(clock)
        remaining = retry_policy.deadline_seconds - max(0.0, before - start)
        if remaining <= 0:
            failure = failure_detail(
                TransportCategory.RETRY_EXHAUSTED,
                "RETRY_DEADLINE_REACHED",
                "The bounded transport deadline was reached before another attempt.",
                request,
                number,
            )
            attempts.append(
                AttemptRecord(
                    attempt_number=0 if not attempts else number,
                    category=TransportCategory.RETRY_EXHAUSTED,
                    code="RETRY_DEADLINE_REACHED",
                    observed_at=observed_at,
                    duration_seconds=0.0,
                    safe_locator=request.safe_locator,
                )
            )
            return failed_result(
                request, TransportCategory.RETRY_EXHAUSTED, attempts, failure
            )
        try:
            response = transport.send(
                request,
                timeout_seconds=min(profile.timeout_seconds, remaining),
                max_response_bytes=profile.max_response_bytes,
                allow_redirects=False,
            )
        except TransportCancelledError:
            evaluation = failed_evaluation(
                TransportCategory.CANCELLED,
                "TRANSPORT_CANCELLED",
                "The injected transport reported cancellation.",
                request,
                number,
            )
        except (TimeoutError, ConnectionTimeoutError):
            evaluation = failed_evaluation(
                TransportCategory.TIMEOUT,
                "TRANSPORT_TIMEOUT",
                "The injected transport timed out.",
                request,
                number,
            )
        except Exception:  # noqa: BLE001 - injected transport is a trust boundary.
            evaluation = failed_evaluation(
                TransportCategory.TRANSPORT_ERROR,
                "TRANSPORT_ERROR",
                "The injected transport failed.",
                request,
                number,
            )
        else:
            if not isinstance(response, TransportResponse):
                raise TransportInputError("injected transport returned an unsupported response type")
            evaluation = evaluate_response(request, response, profile, observed_at)

        duration = max(0.0, read_monotonic(clock) - before)
        if evaluation.category in {TransportCategory.SUCCESS, TransportCategory.NOT_MODIFIED}:
            attempts.append(attempt_record(number, evaluation, observed_at, duration, request))
            return RetrievalResult(
                method=request.method,
                category=evaluation.category,
                safe_locator=request.safe_locator,
                attempts=tuple(attempts),
                payload=evaluation.payload,
                source_head=evaluation.source_head,
                prior_artifact_retained=evaluation.prior_artifact_retained,
            )

        elapsed = max(0.0, read_monotonic(clock) - start)
        decision = retry_policy.decide(
            evaluation.category,
            attempt_number=number,
            elapsed_seconds=elapsed,
            retry_after_seconds=evaluation.retry_after_seconds,
            jitter_unit=jitter.unit(number),
        )
        if not decision.retry:
            final_category = evaluation.category
            failure = evaluation.failure
            if evaluation.category in TRANSIENT_CATEGORIES and decision.reason in _EXHAUSTED_REASONS:
                final_category = TransportCategory.RETRY_EXHAUSTED
                failure = failure_detail(
                    final_category,
                    "RETRY_EXHAUSTED",
                    "Bounded transport retries were exhausted.",
                    request,
                    number,
                )
            if failure is None:
                raise TransportInputError("failure evaluation did not carry failure detail")
            final_evaluation = replace(evaluation, category=final_category, failure=failure)
            attempts.append(attempt_record(number, final_evaluation, observed_at, duration, request))
            return failed_result(request, final_category, attempts, failure)

        attempts.append(
            attempt_record(
                number,
                evaluation,
                observed_at,
                duration,
                request,
                retry_delay=decision.delay_seconds,
            )
        )
        sleeper.sleep(decision.delay_seconds)

    raise AssertionError("bounded retrieval loop exited without a result")


def failed_evaluation(category, code, message, request, attempt_number):
    return Evaluation(
        category,
        code,
        failure=failure_detail(category, code, message, request, attempt_number),
    )
