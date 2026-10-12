"""Run one planner-issued iNaturalist observations cursor-page GET through the shared transport.

Transport effects (the HTTP client, clock, sleeper, jitter, cancellation) are supplied
by the caller and executed by ``connectors_core.transport.execute_retrieval``, which
owns redirect blocking, byte budgets, retries, media-type and digest checks. The result
is recorded by ``connectors_core.retrieval_episode``. This module adds only the
planner-canonical URL check and transport profile, and imports no network library. The
episode contract currently fixes ``execution_mode: FIXTURE_ONLY`` and
``network_attempted: false``, so only synthetic transports are in scope.

Requires ``packages/connectors-core/src`` on the import path (see pyproject.toml).
"""
from __future__ import annotations

from typing import Callable
from urllib.parse import parse_qsl, urlsplit

from connectors_core import core as cc
from connectors_core import transport as ct
from connectors_core.retrieval_episode import (
    EpisodeInputError,
    RetrievalEpisode,
    build_retrieval_episode,
)

from . import observations_api

SOURCE_ID = "inaturalist.observations"
PROFILE_ID = "inaturalist-observations-json-v1"
RETRIEVAL_PROFILE = f"kfm:source-profile:{PROFILE_ID}"
MAX_BYTES = 16 * 1024 * 1024
MEDIA_TYPES = frozenset({"application/json"})

# Stable connector-level names for the shared value object and diagnostic.
Retrieval = RetrievalEpisode
FetchInputError = EpisodeInputError


def profile(max_bytes: int = MAX_BYTES, timeout_seconds: float = 60.0) -> ct.TransportProfile:
    if type(max_bytes) is not int or not 1 <= max_bytes <= MAX_BYTES:
        raise FetchInputError("RESPONSE_BOUND")
    return ct.TransportProfile(PROFILE_ID, frozenset({"api.inaturalist.org"}), MEDIA_TYPES,
                               timeout_seconds=timeout_seconds, max_response_bytes=max_bytes)


def _require_planned(source_url: str) -> None:
    """Accept only a URL the planner could emit: scoped, canonical values, bounded.

    ``observations_api._request`` checks host, path, key names, cursor and page size;
    this rebuilds the ``ObservationQuery`` (exactly one of bbox or place) and requires
    the URL's parameters to equal the planner's canonical values for that cursor.
    Parameter order is not compared: ``page_url`` and ``next_page_url`` emit the same
    parameters in different orders, and both must be retrievable.
    """
    params, per_page, id_above = observations_api._request(source_url)
    values = dict(params)
    try:
        bbox = ("swlat", "swlng", "nelat", "nelng")
        bounds = None
        if any(key in values for key in bbox):
            bounds = (float(values["swlng"]), float(values["swlat"]),
                      float(values["nelng"]), float(values["nelat"]))
        query = observations_api.ObservationQuery(
            bounds=bounds,
            place_id=int(values["place_id"]) if "place_id" in values else None,
            taxon_id=int(values["taxon_id"]) if "taxon_id" in values else None,
            quality_grade=values.get("quality_grade"),
            observed_from=values.get("d1"), observed_to=values.get("d2"))
        canonical = observations_api.page_url(query, id_above=id_above, per_page=per_page)
    except (KeyError, ValueError, TypeError, observations_api.ObservationInputError):
        raise observations_api.ObservationInputError("SOURCE_URL_SCOPE") from None
    if (urlsplit(canonical)[:3] != urlsplit(source_url)[:3]
            or sorted(parse_qsl(urlsplit(canonical).query))
            != sorted(parse_qsl(urlsplit(source_url).query))):
        raise observations_api.ObservationInputError("SOURCE_URL_SCOPE")


def retrieve(source_url: str, *, transport: ct.Transport, clock: ct.Clock,
             sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
             retry_policy: cc.RetryPolicy | None = None,
             jitter_source: ct.JitterSource | None = None,
             cancellation: ct.CancellationToken | None = None,
             max_bytes: int = MAX_BYTES) -> Retrieval:
    """Execute one cursor-page GET with caller-supplied effects and record it."""
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
