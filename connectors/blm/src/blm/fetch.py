"""Run one planner-issued BLM PLSS (CadNSDI) query GET through the shared injected transport.

The URL must be exactly what ``plss_cadnsdi.query_url`` emits for the layer and page it
encodes (Kansas features only). Transport effects are supplied by the caller and
executed by ``connectors_core.transport.execute_retrieval``; the result is recorded by
``connectors_core.retrieval_episode``. No network library is imported. The episode
contract fixes ``execution_mode: FIXTURE_ONLY``, so only synthetic transports are in
scope. Pagination (issuing the next page) is the caller's decision. Requires
``packages/connectors-core/src`` on the import path.
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

from . import plss_cadnsdi

SOURCE_ID = "blm.plss-cadnsdi"
PROFILE_ID = "blm-plss-cadnsdi-geojson-v1"
RETRIEVAL_PROFILE = f"kfm:source-profile:{PROFILE_ID}"
MAX_BYTES = 64 * 1024 * 1024
# ArcGIS serves f=geojson as geo+json or json. NEEDS VERIFICATION against live headers.
MEDIA_TYPES = frozenset({"application/geo+json", "application/json"})

# Stable connector-level names for the shared value object and diagnostic.
Retrieval = RetrievalEpisode
FetchInputError = EpisodeInputError


def profile(max_bytes: int = MAX_BYTES, timeout_seconds: float = 120.0) -> ct.TransportProfile:
    if type(max_bytes) is not int or not 1 <= max_bytes <= MAX_BYTES:
        raise FetchInputError("RESPONSE_BOUND")
    return ct.TransportProfile(PROFILE_ID, frozenset({"gis.blm.gov"}), MEDIA_TYPES,
                               timeout_seconds=timeout_seconds, max_response_bytes=max_bytes)


def _require_planned(source_url: str) -> None:
    plss_cadnsdi.parse_request(source_url)


def retrieve(source_url: str, *, transport: ct.Transport, clock: ct.Clock,
             sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
             retry_policy: cc.RetryPolicy | None = None,
             jitter_source: ct.JitterSource | None = None,
             cancellation: ct.CancellationToken | None = None,
             max_bytes: int = MAX_BYTES) -> Retrieval:
    """Execute one planner-canonical PLSS query GET and record it as an episode."""
    _require_planned(source_url)
    request = ct.TransportRequest(ct.TransportMethod.GET, source_url,
                                  {"Accept": "application/geo+json, application/json"})
    attempted = clock.now()
    result = ct.execute_retrieval(transport, request, profile=profile(max_bytes),
                                  retry_policy=retry_policy or cc.RetryPolicy(),
                                  clock=clock, sleeper=sleeper, jitter_source=jitter_source,
                                  cancellation=cancellation)
    return build_retrieval_episode(result, source_url=source_url, source_id=SOURCE_ID,
                                   retrieval_profile_ref=RETRIEVAL_PROFILE,
                                   attempted_at=attempted, completed_at=clock.now(),
                                   spec_hash=spec_hash)
