"""Run one planner-issued EPA AQS AirData daily-summary GET through the shared transport.

The URL must be exactly what ``aqs_airdata.daily_url`` emits for the criteria-pollutant
parameter and year it names. Transport effects are supplied by the caller and executed by
``connectors_core.transport.execute_retrieval``; the result is recorded by
``connectors_core.retrieval_episode``. No network library is imported. The episode
contract fixes ``execution_mode: FIXTURE_ONLY``, so only synthetic transports are in
scope. The AQS API is not planned here: it needs an account e-mail and key in the query
string. Requires ``packages/connectors-core/src`` on the import path.
"""
from __future__ import annotations

from typing import Callable

from connectors_core import core as cc
from connectors_core import transport as ct
from connectors_core.retrieval_episode import (
    EpisodeInputError,
    RetrievalEpisode,
    build_retrieval_episode,
)

from . import aqs_airdata

SOURCE_ID = "epa.aqs-airdata-daily"
PROFILE_ID = "epa-aqs-airdata-daily-zip-v1"
RETRIEVAL_PROFILE = f"kfm:source-profile:{PROFILE_ID}"
MAX_BYTES = 128 * 1024 * 1024
MEDIA_TYPES = frozenset({"application/zip", "application/x-zip-compressed"})

# Stable connector-level names for the shared value object and diagnostic.
Retrieval = RetrievalEpisode
FetchInputError = EpisodeInputError


def profile(max_bytes: int = MAX_BYTES, timeout_seconds: float = 300.0) -> ct.TransportProfile:
    if type(max_bytes) is not int or not 1 <= max_bytes <= MAX_BYTES:
        raise FetchInputError("RESPONSE_BOUND")
    return ct.TransportProfile(PROFILE_ID, frozenset({"aqs.epa.gov"}), MEDIA_TYPES,
                               timeout_seconds=timeout_seconds, max_response_bytes=max_bytes)


def _require_planned(source_url: str) -> None:
    aqs_airdata.daily_file(source_url)


def retrieve(source_url: str, *, transport: ct.Transport, clock: ct.Clock,
             sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
             retry_policy: cc.RetryPolicy | None = None,
             jitter_source: ct.JitterSource | None = None,
             cancellation: ct.CancellationToken | None = None,
             max_bytes: int = MAX_BYTES) -> Retrieval:
    """Execute one planner-canonical daily-summary archive GET and record it as an episode."""
    _require_planned(source_url)
    request = ct.TransportRequest(ct.TransportMethod.GET, source_url,
                                  {"Accept": "application/zip"})
    attempted = clock.now()
    result = ct.execute_retrieval(transport, request, profile=profile(max_bytes),
                                  retry_policy=retry_policy or cc.RetryPolicy(),
                                  clock=clock, sleeper=sleeper, jitter_source=jitter_source,
                                  cancellation=cancellation)
    return build_retrieval_episode(result, source_url=source_url, source_id=SOURCE_ID,
                                   retrieval_profile_ref=RETRIEVAL_PROFILE,
                                   attempted_at=attempted, completed_at=clock.now(),
                                   spec_hash=spec_hash)
