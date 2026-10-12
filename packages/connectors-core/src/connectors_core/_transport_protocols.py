"""Caller-owned effect protocols for the connector transport boundary."""
from __future__ import annotations

from datetime import datetime
from typing import Protocol, runtime_checkable


@runtime_checkable
class Transport(Protocol):
    def send(
        self,
        request,
        *,
        timeout_seconds: float,
        max_response_bytes: int,
        allow_redirects: bool,
    ): ...


class Clock(Protocol):
    def now(self) -> datetime: ...
    def monotonic(self) -> float: ...


class Sleeper(Protocol):
    def sleep(self, seconds: float) -> None: ...


class JitterSource(Protocol):
    def unit(self, attempt_number: int) -> float: ...


class CancellationToken(Protocol):
    def is_cancelled(self) -> bool: ...
