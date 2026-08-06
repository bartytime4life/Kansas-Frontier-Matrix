"""Retry, cancellation, and injected-time behavior."""
from __future__ import annotations

from datetime import datetime, timezone

from _support import (
    Cancel,
    Clock,
    FakeTransport,
    Jitter,
    Sleeper,
    core,
    profile,
    response,
    retry,
    run,
    transport,
)


def test_rate_limit_retry_after_and_timeout_exhaustion_are_bounded():
    clock = Clock()
    sleeper = Sleeper(clock)
    fake = FakeTransport(
        clock,
        response(
            429,
            body=(),
            headers={"Retry-After": "4", "Content-Length": "0"},
        ),
        response(),
    )
    result = run(
        fake,
        clock=clock,
        sleeper=sleeper,
        policy=retry(jitter_fraction=0.25),
        jitter_source=Jitter(0.5, 0.5),
    )
    assert result.category is core.TransportCategory.SUCCESS
    assert (
        result.attempts[0].category
        is core.TransportCategory.RATE_LIMITED
    )
    assert result.attempts[0].retry_delay_seconds == 4.0
    assert sleeper.delays == [4.0]

    clock = Clock()
    sleeper = Sleeper(clock)
    exhausted = run(
        FakeTransport(clock, TimeoutError(), TimeoutError()),
        clock=clock,
        sleeper=sleeper,
        policy=retry(max_attempts=2),
    )
    assert (
        exhausted.category
        is core.TransportCategory.RETRY_EXHAUSTED
    )
    assert exhausted.failure
    assert exhausted.failure.code == "RETRY_EXHAUSTED"
    assert [item.category for item in exhausted.attempts] == [
        core.TransportCategory.TIMEOUT,
        core.TransportCategory.RETRY_EXHAUSTED,
    ]
    assert sleeper.delays == [1.0]


def test_cancellation_stops_before_transport_and_between_retries():
    clock = Clock()
    token = Cancel(True)
    fake = FakeTransport(clock, response())
    first = run(
        fake,
        clock=clock,
        cancellation=token,
    )
    assert first.category is core.TransportCategory.CANCELLED
    assert fake.calls == []
    assert first.attempts[0].attempt_number == 0

    class CancelSleeper(Sleeper):
        def sleep(self, seconds):
            super().sleep(seconds)
            token.value = True

    token.value = False
    clock = Clock()
    fake = FakeTransport(clock, TimeoutError(), response())
    second = run(
        fake,
        clock=clock,
        sleeper=CancelSleeper(clock),
        cancellation=token,
    )
    assert second.category is core.TransportCategory.CANCELLED
    assert len(fake.calls) == 1
    assert [item.attempt_number for item in second.attempts] == [1, 2]


def test_transport_timeout_is_capped_by_remaining_retry_deadline():
    clock = Clock()
    fake = FakeTransport(clock, TimeoutError())
    result = run(
        fake,
        clock=clock,
        prof=profile(timeout_seconds=30.0),
        policy=retry(max_attempts=1, deadline_seconds=2.0),
    )
    assert (
        result.category
        is core.TransportCategory.RETRY_EXHAUSTED
    )
    assert fake.calls[0][1] == 2.0
    assert fake.calls[0][2] == 64
    assert fake.calls[0][3] is False


def test_retry_after_uses_injected_time():
    observed = datetime(2026, 8, 6, 18, tzinfo=timezone.utc)
    assert transport.parse_retry_after(
        "5",
        observed_at=observed,
    ) == 5.0
    assert transport.parse_retry_after(
        "Thu, 06 Aug 2026 18:00:07 GMT",
        observed_at=observed,
    ) == 7.0
    assert transport.parse_retry_after(
        "Thu, 06 Aug 2026 17:59:00 GMT",
        observed_at=observed,
    ) == 0.0
