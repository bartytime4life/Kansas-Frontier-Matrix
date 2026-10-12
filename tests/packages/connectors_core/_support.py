"""Synthetic, no-network support objects for connectors_core transport tests."""
from __future__ import annotations

from collections import deque
from datetime import datetime, timedelta, timezone
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "packages/connectors-core/src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from connectors_core import core, transport  # noqa: E402


class Clock:
    def __init__(self) -> None:
        self.wall = datetime(2026, 8, 6, 18, tzinfo=timezone.utc)
        self.elapsed = 0.0

    def now(self):
        return self.wall + timedelta(seconds=self.elapsed)

    def monotonic(self):
        return self.elapsed


class Sleeper:
    def __init__(self, clock) -> None:
        self.clock, self.delays = clock, []

    def sleep(self, seconds) -> None:
        self.delays.append(seconds)
        self.clock.elapsed += seconds


class Jitter:
    def __init__(self, *values) -> None:
        self.values = deque(values)

    def unit(self, _attempt_number):
        return self.values.popleft()


class Cancel:
    def __init__(self, value=False) -> None:
        self.value = value

    def is_cancelled(self):
        return self.value


class FakeTransport:
    def __init__(self, clock, *outcomes) -> None:
        self.clock, self.outcomes, self.calls = clock, deque(outcomes), []

    def send(self, request, *, timeout_seconds, max_response_bytes, allow_redirects):
        self.calls.append((request, timeout_seconds, max_response_bytes, allow_redirects))
        self.clock.elapsed += 0.25
        outcome = self.outcomes.popleft()
        if isinstance(outcome, BaseException):
            raise outcome
        return outcome


def profile(**kw):
    values = dict(
        profile_id="fixture-source-v1",
        allowed_hosts=frozenset({"source.example.test"}),
        allowed_media_types=frozenset({"application/json"}),
        timeout_seconds=5.0,
        max_response_bytes=64,
    )
    values.update(kw)
    return transport.TransportProfile(**values)


def request(**kw):
    values = dict(
        method=transport.TransportMethod.GET,
        url="https://source.example.test/data?token=secret&county=001",
        headers={"Authorization": "Bearer fixture-secret", "Accept": "application/json"},
    )
    values.update(kw)
    return transport.TransportRequest(**values)


def response(status=200, body=(b'{"ok":true}',), headers=None, *, complete=True, final_url=None):
    values = {
        "Content-Type": "application/json; charset=utf-8",
        "Content-Length": str(sum(map(len, body))),
        "ETag": 'W/"fixture-head"',
        "Last-Modified": "Wed, 06 Aug 2025 12:00:00 GMT",
        "Set-Cookie": "session=must-not-survive",
    }
    values.update(headers or {})
    return transport.TransportResponse(
        status_code=status,
        headers=values,
        body_chunks=body,
        final_url=final_url or "https://source.example.test/data?token=secret&county=001",
        complete=complete,
    )


def retry(**kw):
    values = dict(
        max_attempts=3,
        base_delay_seconds=1.0,
        multiplier=2.0,
        max_delay_seconds=10.0,
        deadline_seconds=30.0,
        jitter_fraction=0.0,
    )
    values.update(kw)
    return core.RetryPolicy(**values)


def run(fake, req=None, *, prof=None, policy=None, clock=None, sleeper=None, **kw):
    clock = clock or fake.clock
    sleeper = sleeper or Sleeper(clock)
    return transport.execute_retrieval(
        fake,
        req or request(),
        profile=prof or profile(),
        retry_policy=policy or retry(),
        clock=clock,
        sleeper=sleeper,
        **kw,
    )
