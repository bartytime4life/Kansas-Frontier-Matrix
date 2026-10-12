"""Run one planner-issued GBIF occurrence-search page GET through the shared injected transport.

Transport effects (the HTTP client, clock, sleeper, jitter, cancellation) are supplied
by the caller and executed by ``connectors_core.transport.execute_retrieval``, which
owns redirect blocking, byte budgets, retries, media-type and digest checks. The result
is recorded by ``connectors_core.retrieval_episode``. This module adds only the GBIF
search-URL allowlist and transport profile, and imports no network library. The episode
contract currently fixes ``execution_mode: FIXTURE_ONLY`` and ``network_attempted:
false``, so only synthetic transports are in scope.

Requires ``packages/connectors-core/src`` on the import path (see pyproject.toml).
"""
from __future__ import annotations

from typing import Callable
from urllib.parse import urlencode

from connectors_core import core as cc
from connectors_core import transport as ct
from connectors_core.retrieval_episode import (
    EpisodeInputError,
    RetrievalEpisode,
    build_retrieval_episode,
)

from . import occurrence_api

SOURCE_ID = "gbif.occurrence-search"
PROFILE_ID = "gbif-occurrence-search-json-v1"
RETRIEVAL_PROFILE = f"kfm:source-profile:{PROFILE_ID}"
MAX_BYTES = 16 * 1024 * 1024
MEDIA_TYPES = frozenset({"application/json"})

# Stable connector-level names for the shared value object and diagnostic.
Retrieval = RetrievalEpisode
FetchInputError = EpisodeInputError


def profile(max_bytes: int = MAX_BYTES, timeout_seconds: float = 60.0) -> ct.TransportProfile:
    if type(max_bytes) is not int or not 1 <= max_bytes <= MAX_BYTES:
        raise FetchInputError("RESPONSE_BOUND")
    return ct.TransportProfile(PROFILE_ID, frozenset({"api.gbif.org"}), MEDIA_TYPES,
                               timeout_seconds=timeout_seconds, max_response_bytes=max_bytes)


def _require_planned(source_url: str) -> None:
    """Accept only a URL ``plan_pages`` could emit: scoped, canonical, and bounded.

    ``occurrence_api._request`` checks host, path, key names and the page window; this
    also rebuilds the ``OccurrenceQuery`` so the required country and state filters are
    present and valid, and requires the URL to equal the planner's canonical encoding.
    """
    params, offset, limit = occurrence_api._request(source_url)
    try:
        query = occurrence_api.OccurrenceQuery(
            country=params["country"], state_province=params["stateProvince"],
            taxon_key=int(params["taxonKey"]) if "taxonKey" in params else None,
            year=params.get("year"), basis_of_record=params.get("basisOfRecord"),
            has_coordinate={"true": True, "false": False}[params["hasCoordinate"]]
            if "hasCoordinate" in params else None)
        expected = query.params()
    except (KeyError, ValueError, TypeError, occurrence_api.OccurrenceInputError):
        raise occurrence_api.OccurrenceInputError("SOURCE_URL_SCOPE") from None
    # plan_pages advances offsets by a fixed page size and only the final page may be
    # shorter, so the window must fit that sequence: a full page sits on a multiple of
    # its own limit; a short final page sits on a multiple of some larger page size.
    if offset % limit and not any(offset % size == 0
                                  for size in range(limit + 1, occurrence_api.MAX_PAGE + 1)):
        raise occurrence_api.OccurrenceInputError("SOURCE_URL_SCOPE")
    canonical = (f"{occurrence_api.HOST}{occurrence_api.SEARCH_PATH}?"
                 + urlencode(dict(expected, limit=limit, offset=offset)))
    if canonical != source_url:
        raise occurrence_api.OccurrenceInputError("SOURCE_URL_SCOPE")


def retrieve(source_url: str, *, transport: ct.Transport, clock: ct.Clock,
             sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
             retry_policy: cc.RetryPolicy | None = None,
             jitter_source: ct.JitterSource | None = None,
             cancellation: ct.CancellationToken | None = None,
             max_bytes: int = MAX_BYTES) -> Retrieval:
    """Execute one page GET with caller-supplied effects and record it as an episode."""
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
