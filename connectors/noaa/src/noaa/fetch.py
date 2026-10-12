"""Run planner-issued NOAA GETs through the shared injected transport.

Three products, each with its own source identity and transport profile:

* NCEI Storm Events details files (``retrieve_storm_events``): the URL must be exactly
  ``storm_events.details_url(year, created)`` for the vintage it names.
* USCRN hourly02 station-year files (``retrieve_uscrn_hourly``): the URL must be exactly
  ``uscrn_hourly.hourly_url(year, station)``.
* NWS API alert collections (``retrieve_nws_alerts``): the URL must be exactly
  ``nws_alerts.alerts_url(area, active=...)``. NWS remains the issuing authority; an
  episode is official-source context, never a KFM alert.

Transport effects are supplied by the caller and executed by
``connectors_core.transport.execute_retrieval``; results are recorded by
``connectors_core.retrieval_episode``. No network library is imported and no identifying
``User-Agent`` is invented here. The episode contract fixes ``execution_mode:
FIXTURE_ONLY``, so only synthetic transports are in scope. Requires
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

from . import nws_alerts, storm_events, uscrn_hourly

STORM_SOURCE_ID = "noaa.storm-events"
STORM_PROFILE_ID = "noaa-storm-events-details-gzip-v1"
STORM_RETRIEVAL_PROFILE = f"kfm:source-profile:{STORM_PROFILE_ID}"
STORM_MAX_BYTES = 256 * 1024 * 1024
STORM_MEDIA_TYPES = frozenset({"application/gzip", "application/x-gzip"})
USCRN_SOURCE_ID = "noaa.uscrn-hourly02"
USCRN_PROFILE_ID = "noaa-uscrn-hourly02-text-v1"
USCRN_RETRIEVAL_PROFILE = f"kfm:source-profile:{USCRN_PROFILE_ID}"
USCRN_MAX_BYTES = 32 * 1024 * 1024
NWS_SOURCE_ID = "noaa.nws-alerts"
NWS_PROFILE_ID = "noaa-nws-alerts-geojson-v1"
NWS_RETRIEVAL_PROFILE = f"kfm:source-profile:{NWS_PROFILE_ID}"
NWS_MAX_BYTES = 16 * 1024 * 1024
NWS_MEDIA_TYPES = frozenset({"application/geo+json", "application/json"})
NCEI_HOST = "www.ncei.noaa.gov"

# Stable connector-level names for the shared value object and diagnostic.
Retrieval = RetrievalEpisode
FetchInputError = EpisodeInputError


def _profile(profile_id: str, host: str, media_types: frozenset[str], limit: int,
             max_bytes: int, timeout_seconds: float) -> ct.TransportProfile:
    if type(max_bytes) is not int or not 1 <= max_bytes <= limit:
        raise FetchInputError("RESPONSE_BOUND")
    return ct.TransportProfile(profile_id, frozenset({host}), media_types,
                               timeout_seconds=timeout_seconds, max_response_bytes=max_bytes)


def storm_profile(max_bytes: int = STORM_MAX_BYTES,
                  timeout_seconds: float = 300.0) -> ct.TransportProfile:
    return _profile(STORM_PROFILE_ID, NCEI_HOST, STORM_MEDIA_TYPES, STORM_MAX_BYTES,
                    max_bytes, timeout_seconds)


def uscrn_profile(max_bytes: int = USCRN_MAX_BYTES,
                  timeout_seconds: float = 120.0) -> ct.TransportProfile:
    return _profile(USCRN_PROFILE_ID, NCEI_HOST, frozenset({"text/plain"}), USCRN_MAX_BYTES,
                    max_bytes, timeout_seconds)


def nws_profile(max_bytes: int = NWS_MAX_BYTES,
                timeout_seconds: float = 30.0) -> ct.TransportProfile:
    return _profile(NWS_PROFILE_ID, "api.weather.gov", NWS_MEDIA_TYPES, NWS_MAX_BYTES,
                    max_bytes, timeout_seconds)


def _require_planned_storm(source_url: str) -> None:
    vintage = storm_events.file_vintage(source_url)
    if storm_events.details_url(vintage.data_year, vintage.created) != source_url:
        raise storm_events.StormEventsInputError("SOURCE_URL_SCOPE")


def _require_planned_uscrn(source_url: str) -> None:
    station = uscrn_hourly.station_file(source_url)
    if uscrn_hourly.hourly_url(station.year, station.station) != source_url:
        raise uscrn_hourly.UscrnInputError("SOURCE_URL_SCOPE")


def _require_planned_nws(source_url: str) -> None:
    path, area = nws_alerts._request(source_url)
    if nws_alerts.alerts_url(area, active=path == "/alerts/active") != source_url:
        raise nws_alerts.NwsInputError("SOURCE_URL_SCOPE")


def _execute(source_url: str, accept: str, profile: ct.TransportProfile, *, source_id: str,
             profile_ref: str, transport, clock, sleeper, spec_hash, retry_policy,
             jitter_source, cancellation) -> Retrieval:
    request = ct.TransportRequest(ct.TransportMethod.GET, source_url, {"Accept": accept})
    attempted = clock.now()
    result = ct.execute_retrieval(transport, request, profile=profile,
                                  retry_policy=retry_policy or cc.RetryPolicy(),
                                  clock=clock, sleeper=sleeper, jitter_source=jitter_source,
                                  cancellation=cancellation)
    return build_retrieval_episode(result, source_url=source_url, source_id=source_id,
                                   retrieval_profile_ref=profile_ref, attempted_at=attempted,
                                   completed_at=clock.now(), spec_hash=spec_hash)


def retrieve_storm_events(source_url: str, *, transport: ct.Transport, clock: ct.Clock,
                          sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
                          retry_policy: cc.RetryPolicy | None = None,
                          jitter_source: ct.JitterSource | None = None,
                          cancellation: ct.CancellationToken | None = None,
                          max_bytes: int = STORM_MAX_BYTES) -> Retrieval:
    """Execute one planner-canonical Storm Events details-file GET as an episode."""
    _require_planned_storm(source_url)
    return _execute(source_url, "application/gzip", storm_profile(max_bytes),
                    source_id=STORM_SOURCE_ID, profile_ref=STORM_RETRIEVAL_PROFILE,
                    transport=transport, clock=clock, sleeper=sleeper, spec_hash=spec_hash,
                    retry_policy=retry_policy, jitter_source=jitter_source,
                    cancellation=cancellation)


def retrieve_uscrn_hourly(source_url: str, *, transport: ct.Transport, clock: ct.Clock,
                          sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
                          retry_policy: cc.RetryPolicy | None = None,
                          jitter_source: ct.JitterSource | None = None,
                          cancellation: ct.CancellationToken | None = None,
                          max_bytes: int = USCRN_MAX_BYTES) -> Retrieval:
    """Execute one planner-canonical USCRN hourly02 station-year GET as an episode."""
    _require_planned_uscrn(source_url)
    return _execute(source_url, "text/plain", uscrn_profile(max_bytes),
                    source_id=USCRN_SOURCE_ID, profile_ref=USCRN_RETRIEVAL_PROFILE,
                    transport=transport, clock=clock, sleeper=sleeper, spec_hash=spec_hash,
                    retry_policy=retry_policy, jitter_source=jitter_source,
                    cancellation=cancellation)


def retrieve_nws_alerts(source_url: str, *, transport: ct.Transport, clock: ct.Clock,
                        sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
                        retry_policy: cc.RetryPolicy | None = None,
                        jitter_source: ct.JitterSource | None = None,
                        cancellation: ct.CancellationToken | None = None,
                        max_bytes: int = NWS_MAX_BYTES) -> Retrieval:
    """Execute one planner-canonical NWS alert-collection GET as an episode."""
    _require_planned_nws(source_url)
    return _execute(source_url, "application/geo+json", nws_profile(max_bytes),
                    source_id=NWS_SOURCE_ID, profile_ref=NWS_RETRIEVAL_PROFILE,
                    transport=transport, clock=clock, sleeper=sleeper, spec_hash=spec_hash,
                    retry_policy=retry_policy, jitter_source=jitter_source,
                    cancellation=cancellation)
