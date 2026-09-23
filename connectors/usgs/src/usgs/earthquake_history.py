"""Bounded, injected USGS history acquisition; candidates only, never publication.

The reader owns authenticated transport, redirect denial and hard read deadlines.
Use the existing connectors-core transport/handoff at that boundary. This module
imports no network client, starts no schedule, and writes no files. Two matching
passes are an observation of stability, NOT an atomic or complete event catalog.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from hashlib import sha256
import math
import re
import time
from typing import Callable, Protocol
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from .earthquake import (
    EPOCH, KANSAS_CONTEXT, EarthquakeInputError, EventCandidate,
    HistoryWindow, history_windows, parse_snapshot,
)


@dataclass(frozen=True)
class HistoryRequest:
    url: str
    max_bytes: int
    timeout_seconds: float
    allow_redirects: bool = field(default=False, init=False)


@dataclass(frozen=True)
class HistoryResponse:
    final_url: str
    status: int
    media_type: str
    retrieved_at: str
    body: bytes = field(repr=False)


class HistoryReader(Protocol):
    def __call__(self, request: HistoryRequest) -> HistoryResponse:
        """Honor byte/deadline bounds before buffering; never follow redirects."""
        ...


@dataclass(frozen=True)
class HistoryCapture:
    request: HistoryRequest
    response: HistoryResponse
    body_sha256: str


@dataclass(frozen=True)
class HistoryResult:
    outcome: str
    reason: str
    events: tuple[EventCandidate, ...]
    captures: tuple[HistoryCapture, ...] = field(repr=False)
    requests_attempted: int
    passes_completed: int
    # These are fixed and cannot be raised by a caller-supplied constructor field.
    admission: str = field(default="NOT_ADMITTED", init=False)
    coverage: str = field(default="NOT_ESTABLISHED", init=False)


class _Hold(Exception):
    pass


def _edit_url(url: str, **changes: object) -> str:
    parts = urlsplit(url)
    params = dict(parse_qsl(parts.query, strict_parsing=True))
    params.update({key: str(value) for key, value in changes.items()})
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(params), ""))


def _instant(text: str) -> datetime:
    if not isinstance(text, str) or len(text) > 40:
        raise _Hold("RETRIEVAL_TIME")
    try:
        result = datetime.fromisoformat(text.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        return result.astimezone(timezone.utc)
    except (ValueError, OverflowError):
        raise _Hold("RETRIEVAL_TIME") from None


def acquire_history(start: str, end: str, reader: HistoryReader, *,
                    bounds=KANSAS_CONTEXT, page_size: int = 1000,
                    max_requests: int = 128, max_events: int = 20000,
                    max_bytes: int = 32 * 1024 * 1024,
                    deadline_seconds: float = 120,
                    clock: Callable[[], float] = time.monotonic,
                    cancelled: Callable[[], bool] = lambda: False) -> HistoryResult:
    """Run count -> pages -> count twice; withhold events on any incomplete run.

    Count requests use the provider's plain-text format. Query counts include
    both endpoints, while returned event ownership is [start, end). Oversized
    windows are bisected at millisecond precision within the same global budget.
    Failed captures remain available to the internal custody layer. No response
    URL/metadata link is followed. No retry hides an unstable result.

    Configuration errors raise ValueError before transport. Execution failures
    return HELD and no events; the caller must not replace a previous snapshot
    with that empty tuple. A cooperative deadline cannot preempt a bad reader.
    """
    if not all(callable(hook) for hook in (reader, clock, cancelled)):
        raise ValueError("HISTORY_CALLBACK")
    limits = ((page_size, 1, 20000), (max_requests, 6, 1000),
              (max_events, 1, 100000), (max_bytes, 1024, 64 * 1024 * 1024))
    if any(type(v) is not int or not lo <= v <= hi for v, lo, hi in limits):
        raise ValueError("HISTORY_BUDGET")
    if (type(deadline_seconds) not in (int, float)
            or not math.isfinite(deadline_seconds) or not 0 < deadline_seconds <= 600):
        raise ValueError("HISTORY_DEADLINE")
    # Reuse the existing closed request planner, including UTC/bbox validation.
    plans = history_windows(start, end, bounds=bounds, limit=page_size,
                            max_windows=max_requests)
    bounds = tuple(float(value) for value in bounds)
    if len(plans) * 6 > max_requests:
        raise ValueError("HISTORY_MINIMUM_REQUEST_BUDGET")
    first_tick = clock()
    if type(first_tick) not in (int, float) or not math.isfinite(first_tick):
        raise ValueError("HISTORY_CLOCK")
    last_tick = first_tick
    used = 0
    attempted = 0
    passes = 0
    captures: list[HistoryCapture] = []
    last_retrieval: datetime | None = None

    def remaining() -> float:
        nonlocal last_tick
        try:
            cancellation = cancelled()
        except Exception:
            raise _Hold("CANCELLATION_ERROR") from None
        if type(cancellation) is not bool:
            raise _Hold("CANCELLATION_INVALID")
        if cancellation:
            raise _Hold("CANCELLED")
        try:
            tick = clock()
        except Exception:
            raise _Hold("CLOCK_INVALID") from None
        if type(tick) not in (int, float) or not math.isfinite(tick) or tick < last_tick:
            raise _Hold("CLOCK_INVALID")
        last_tick = tick
        left = deadline_seconds - (tick - first_tick)
        if left <= 0:
            raise _Hold("DEADLINE_EXCEEDED")
        return left

    def request(url: str, count: bool = False) -> HistoryResponse:
        nonlocal attempted, used, last_retrieval
        left = remaining()
        if attempted >= max_requests:
            raise _Hold("REQUEST_BUDGET")
        cap = min(128 if count else 8 * 1024 * 1024, max_bytes - used)
        if cap <= 0:
            raise _Hold("BYTE_BUDGET")
        req = HistoryRequest(url, cap, min(30.0, left))
        attempted += 1
        try:
            response = reader(req)
        except Exception:
            raise _Hold("TRANSPORT_ERROR") from None
        if (not isinstance(response, HistoryResponse)
                or not isinstance(response.body, bytes)
                or type(response.status) is not int
                or not 100 <= response.status <= 599
                or not isinstance(response.media_type, str)
                or len(response.media_type) > 128
                or not isinstance(response.final_url, str)
                or len(response.final_url) > 4096
                or not isinstance(response.retrieved_at, str)
                or len(response.retrieved_at) > 40):
            raise _Hold("RESPONSE_SHAPE")
        if len(response.body) > cap:
            raise _Hold("BYTE_BUDGET")
        used += len(response.body)
        captures.append(HistoryCapture(req, response, "sha256:" + sha256(response.body).hexdigest()))
        remaining()
        if response.final_url != url or 300 <= response.status <= 399:
            raise _Hold("REDIRECT_DENIED")
        retrieved = _instant(response.retrieved_at)
        if last_retrieval is not None and retrieved < last_retrieval:
            raise _Hold("RETRIEVAL_ORDER")
        last_retrieval = retrieved
        media = response.media_type.split(";", 1)[0].strip().lower()
        allowed = {"text/plain"} if count else {"application/json", "application/geo+json"}
        if response.status == 204 and not count and not response.body:
            return response
        if response.status != 200:
            raise _Hold("UPSTREAM_HTTP")
        if media not in allowed:
            raise _Hold("MEDIA_TYPE")
        return response

    def get_count(plan: HistoryWindow) -> int:
        response = request(_edit_url(plan.count_url, format="text"), count=True)
        if not re.fullmatch(rb"(?:0|[1-9][0-9]{0,11})\s*", response.body):
            raise _Hold("COUNT_SHAPE")
        return int(response.body)

    def one_pass() -> tuple[EventCandidate, ...]:
        queue = list(reversed(plans))
        selected: list[EventCandidate] = []
        selected_aliases: set[str] = set()
        while queue:
            remaining()
            plan = queue.pop()
            before = get_count(plan)
            if before > min(max_events, 20000):
                a, b = _instant(plan.start), _instant(plan.end_exclusive)
                delta = b - a
                millis = (delta.days * 86400 + delta.seconds) * 1000 + delta.microseconds // 1000
                if millis <= 1:
                    raise _Hold("SATURATED_INTERVAL")
                middle = a + timedelta(milliseconds=millis // 2)
                left = history_windows(a.isoformat(), middle.isoformat(), bounds=bounds, limit=page_size)[0]
                right = history_windows(middle.isoformat(), b.isoformat(), bounds=bounds, limit=page_size)[0]
                queue.extend((right, left))
                continue
            inclusive: list[EventCandidate] = []
            aliases: set[str] = set()
            # A zero count still requires a genuine empty query response.
            pages = max(1, (before + page_size - 1) // page_size)
            for page in range(pages):
                url = _edit_url(plan.query_url, offset=1 + page * page_size)
                response = request(url)
                snapshot = parse_snapshot(response.body, status=response.status, source_url=url,
                                          retrieved_at=response.retrieved_at, max_events=page_size)
                expected = min(page_size, max(0, before - page * page_size))
                if len(snapshot.events) != expected:
                    raise _Hold("PAGE_COUNT_CHANGED")
                a, b = _instant(plan.start), _instant(plan.end_exclusive)
                for event in snapshot.events:
                    instant = EPOCH + timedelta(milliseconds=event.origin_ms)
                    if (event.event_type != "earthquake" or not a <= instant <= b
                            or not bounds[0] <= event.longitude <= bounds[2]
                            or not bounds[1] <= event.latitude <= bounds[3]):
                        raise _Hold("QUERY_MEMBERSHIP")
                    if inclusive and event.origin_ms < inclusive[-1].origin_ms:
                        raise _Hold("PAGE_ORDER")
                    if aliases.intersection(event.aliases):
                        raise _Hold("PAGE_IDENTITY_CONFLICT")
                    aliases.update(event.aliases)
                    inclusive.append(event)
            if get_count(plan) != before:
                raise _Hold("COUNT_CHANGED")
            for event in inclusive:
                if EPOCH + timedelta(milliseconds=event.origin_ms) >= _instant(plan.end_exclusive):
                    continue
                if selected_aliases.intersection(event.aliases):
                    raise _Hold("WINDOW_IDENTITY_CONFLICT")
                selected_aliases.update(event.aliases)
                selected.append(event)
                if len(selected) > max_events:
                    raise _Hold("EVENT_BUDGET")
        return tuple(sorted(selected, key=lambda event: (event.origin_ms, event.event_id)))

    try:
        previous = one_pass()
        passes = 1
        current = one_pass()
        passes = 2
        if tuple((e.event_id, e.feature_sha256) for e in previous) != tuple((e.event_id, e.feature_sha256) for e in current):
            raise _Hold("CATALOG_CHANGED")
        remaining()
        return HistoryResult("TWO_PASS_MATCH", "BOUNDED_CURRENT_CATALOG_ONLY", current,
                             tuple(captures), attempted, passes)
    except EarthquakeInputError:
        reason = "PAGE_INVALID"
    except _Hold as error:
        reason = str(error)
    return HistoryResult("HELD", reason, (), tuple(captures), attempted, passes)
