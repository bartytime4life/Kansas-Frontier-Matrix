"""Provider Retry-After is a lower bound, including under negative jitter."""
from connectors_core.core import RetryPolicy, TransportCategory


def test_retry_after_over_budget_does_not_retry_early():
    decision = RetryPolicy(max_delay_seconds=10).decide(
        TransportCategory.RATE_LIMITED, attempt_number=1, elapsed_seconds=0, retry_after_seconds=30)
    assert not decision.retry


def test_jitter_cannot_reduce_provider_delay():
    decision = RetryPolicy(max_delay_seconds=30, jitter_fraction=1).decide(
        TransportCategory.RATE_LIMITED, attempt_number=1, elapsed_seconds=0,
        retry_after_seconds=8, jitter_unit=0)
    assert decision.delay_seconds >= 8
