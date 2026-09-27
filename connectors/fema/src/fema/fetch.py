"""Run one planner-issued OpenFEMA declarations page GET through the shared injected transport.

Transport effects (the HTTP client, clock, sleeper, jitter, cancellation) are supplied
by the caller and executed by ``connectors_core.transport.execute_retrieval``, which
owns redirect blocking, byte budgets, retries, media-type and digest checks. The result
is recorded by ``connectors_core.retrieval_episode``. This module adds only the OpenFEMA
page-URL allowlist and transport profile, and imports no network library. The episode
contract currently fixes ``execution_mode: FIXTURE_ONLY`` and ``network_attempted:
false``, so only synthetic transports are in scope.

Requires ``packages/connectors-core/src`` on the import path (see pyproject.toml).
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

from . import openfema_declarations as declarations

SOURCE_ID = "fema.openfema.disaster-declarations-summaries"
PROFILE_ID = "fema-openfema-declarations-json-v1"
RETRIEVAL_PROFILE = f"kfm:source-profile:{PROFILE_ID}"
MAX_BYTES = 64 * 1024 * 1024
MEDIA_TYPES = frozenset({"application/json"})

# Stable connector-level names for the shared value object and diagnostic.
Retrieval = RetrievalEpisode
FetchInputError = EpisodeInputError


def profile(max_bytes: int = MAX_BYTES, timeout_seconds: float = 60.0) -> ct.TransportProfile:
    if type(max_bytes) is not int or not 1 <= max_bytes <= MAX_BYTES:
        raise FetchInputError("RESPONSE_BOUND")
    return ct.TransportProfile(PROFILE_ID, frozenset({"www.fema.gov"}), MEDIA_TYPES,
                               timeout_seconds=timeout_seconds, max_response_bytes=max_bytes)


def retrieve(source_url: str, *, transport: ct.Transport, clock: ct.Clock,
             sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
             retry_policy: cc.RetryPolicy | None = None,
             jitter_source: ct.JitterSource | None = None,
             cancellation: ct.CancellationToken | None = None,
             max_bytes: int = MAX_BYTES) -> Retrieval:
    """Execute one page GET with caller-supplied effects and record it as an episode."""
    declarations._request(source_url)
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
