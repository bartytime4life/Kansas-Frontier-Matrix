"""Run one planner-issued NRCS SCAN (AWDB) GET through the shared injected transport.

The URL must be exactly what ``scan_awdb.data_url`` emits for the request it encodes
(Kansas ``SCAN``-network stations only). Transport effects are supplied by the caller and
executed by ``connectors_core.transport.execute_retrieval``; the result is recorded by
``connectors_core.retrieval_episode``. No network library is imported. The episode
contract fixes ``execution_mode: FIXTURE_ONLY``, so only synthetic transports are in
scope. Soil Data Access is not planned here: it is a POST query surface and the shared
transport is GET/HEAD only. Requires ``packages/connectors-core/src`` on the import path.
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

from . import scan_awdb

SOURCE_ID = "nrcs.scan-awdb"
PROFILE_ID = "nrcs-scan-awdb-json-v1"
RETRIEVAL_PROFILE = f"kfm:source-profile:{PROFILE_ID}"
MAX_BYTES = 16 * 1024 * 1024

# Stable connector-level names for the shared value object and diagnostic.
Retrieval = RetrievalEpisode
FetchInputError = EpisodeInputError


def profile(max_bytes: int = MAX_BYTES, timeout_seconds: float = 60.0) -> ct.TransportProfile:
    if type(max_bytes) is not int or not 1 <= max_bytes <= MAX_BYTES:
        raise FetchInputError("RESPONSE_BOUND")
    return ct.TransportProfile(PROFILE_ID, frozenset({"wcc.sc.egov.usda.gov"}),
                               frozenset({"application/json"}),
                               timeout_seconds=timeout_seconds, max_response_bytes=max_bytes)


def _require_planned(source_url: str) -> None:
    scan_awdb.parse_request(source_url)


def retrieve(source_url: str, *, transport: ct.Transport, clock: ct.Clock,
             sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
             retry_policy: cc.RetryPolicy | None = None,
             jitter_source: ct.JitterSource | None = None,
             cancellation: ct.CancellationToken | None = None,
             max_bytes: int = MAX_BYTES) -> Retrieval:
    """Execute one planner-canonical AWDB data GET and record it as an episode."""
    _require_planned(source_url)
    request = ct.TransportRequest(ct.TransportMethod.GET, source_url,
                                  {"Accept": "application/json"})
    attempted = clock.now()
    result = ct.execute_retrieval(transport, request, profile=profile(max_bytes),
                                  retry_policy=retry_policy or cc.RetryPolicy(),
                                  clock=clock, sleeper=sleeper, jitter_source=jitter_source,
                                  cancellation=cancellation)
    return build_retrieval_episode(result, source_url=source_url, source_id=SOURCE_ID,
                                   retrieval_profile_ref=RETRIEVAL_PROFILE,
                                   attempted_at=attempted, completed_at=clock.now(),
                                   spec_hash=spec_hash)
