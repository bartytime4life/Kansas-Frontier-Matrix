"""Route one recorded NOAA retrieval (Storm Events, USCRN hourly02, NWS alerts); never writes.

The episode's own source identity selects the product parser: ``storm_events``,
``uscrn_hourly`` or ``nws_alerts``. Anything else is refused
(``EPISODE_SOURCE_MISMATCH``), and fetch's planner URL rule is re-applied so a stored or
reconstructed episode cannot carry a URL the planner would not have issued.

A response that was not captured is held; captured bytes that the product parser rejects
are a quarantine candidate. A parsed file or collection is a raw candidate, flagged
``RECORD_QUARANTINE_CANDIDATES`` when any record is a quarantine candidate, plus
product flags: ``MISSING_HOURS_PRESENT`` for USCRN gaps, and the NWS collection's own
reasons (a partial capture or the seven-day window). NWS freshness is computed as of the
retrieval instant only and must be recomputed on reuse. The final route is HOLD while the
connector descriptor leaves ``role`` or ``rights`` unresolved, and always for a product the
descriptor's role does not cover (``PRODUCT_ROLE_UNRESOLVED``; only USCRN is covered). Nothing here grants
admission, establishes coverage, relays an alert, or persists material.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
import re

from connectors_core import descriptor_gate, retrieval_episode

from . import fetch, nws_alerts, storm_events, uscrn_hourly
from .fetch import Retrieval

DESCRIPTOR = Path(__file__).resolve().with_name("descriptor.yaml")
NAME = "noaa"
RAW = "RAW_CANDIDATE"
QUARANTINE = "QUARANTINE_CANDIDATE"
HOLD = "HOLD"
LAST_MODIFIED = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
PRODUCTS = {fetch.STORM_SOURCE_ID: fetch.STORM_RETRIEVAL_PROFILE,
            fetch.USCRN_SOURCE_ID: fetch.USCRN_RETRIEVAL_PROFILE,
            fetch.NWS_SOURCE_ID: fetch.NWS_RETRIEVAL_PROFILE}
# Source role is product-level (README "Source-role posture"): the family descriptor's
# single role is applied only to these products. Storm Events (historical event records)
# and NWS alerts (official warning context) hold until their own roles are decided.
ROLE_COVERED_PRODUCTS = frozenset({fetch.USCRN_SOURCE_ID})
URL_RULES = {fetch.STORM_SOURCE_ID: fetch._require_planned_storm,
             fetch.USCRN_SOURCE_ID: fetch._require_planned_uscrn,
             fetch.NWS_SOURCE_ID: fetch._require_planned_nws}


def load_descriptor(path: Path = DESCRIPTOR) -> dict[str, str]:
    return descriptor_gate.load_descriptor(path)


def descriptor_blockers(descriptor: dict[str, str]) -> tuple[str, ...]:
    return descriptor_gate.descriptor_blockers(descriptor, name=NAME)


@dataclass(frozen=True)
class AdmissionDecision:
    route: str
    provisional_route: str
    reasons: tuple[str, ...]
    episode_id: str
    source_id: str
    source_url: str
    # Exactly one parsed candidate is present when the provisional route is RAW.
    details_file: storm_events.DetailsFileCandidate | None
    station_year: uscrn_hourly.StationYearCandidate | None
    alerts: nws_alerts.AlertCollectionCandidate | None
    # Routing is not admission, a coverage claim, or a write to data/raw or data/quarantine.
    admission: str = "NOT_ADMITTED"
    coverage: str = "NOT_ESTABLISHED"
    write_performed: bool = False


def _flags(records) -> tuple[str, ...]:
    return (("RECORD_QUARANTINE_CANDIDATES",)
            if any(record.route == QUARANTINE for record in records) else ())


def _cache_headers(transport: dict) -> dict[str, str]:
    """Rebuild the NWS cache headers the episode contract records (ETag, Last-Modified).

    ``Cache-Control``, ``Date`` and ``Expires`` are not SourceRetrievalEpisode fields, so
    they cannot survive recording and are never invented here.
    """
    headers = {}
    if isinstance(transport.get("etag"), str):
        headers["ETag"] = transport["etag"]
    recorded = transport.get("last_modified")
    if recorded is not None:
        # The recorder writes UTC seconds (``...Z``); anything else is a forged episode.
        try:
            if not isinstance(recorded, str) or not LAST_MODIFIED.fullmatch(recorded):
                raise ValueError
            instant = datetime.strptime(recorded, "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=timezone.utc)
        except ValueError:
            raise fetch.FetchInputError("EPISODE_LAST_MODIFIED") from None
        headers["Last-Modified"] = format_datetime(instant, usegmt=True)
    return headers


def _parse(source_id: str, retrieval: Retrieval, episode: dict):
    """Return (route, reasons, parsed) for one captured episode."""
    common = dict(status=episode["transport"]["http_status"],
                  source_url=retrieval.source_url, retrieved_at=episode["completed_at"])
    try:
        if source_id == fetch.STORM_SOURCE_ID:
            parsed = storm_events.parse_details_file(retrieval.body, **common)
            return RAW, _flags(parsed.events), parsed
        if source_id == fetch.USCRN_SOURCE_ID:
            parsed = uscrn_hourly.parse_station_year(retrieval.body, **common)
            gaps = ("MISSING_HOURS_PRESENT",) if parsed.missing_hours else ()
            return RAW, _flags(parsed.records) + gaps, parsed
        parsed = nws_alerts.parse_alerts(retrieval.body, **common,
                                         headers=_cache_headers(episode["transport"]))
        return RAW, _flags(parsed.alerts) + tuple(parsed.reasons), parsed
    except (storm_events.StormEventsInputError, uscrn_hourly.UscrnInputError,
            nws_alerts.NwsInputError) as error:
        return QUARANTINE, (f"PARSE_{error.args[0]}",), None


def admit(retrieval: Retrieval, *,
          descriptor: dict[str, str] | None = None) -> AdmissionDecision:
    """Decide a candidate lane for one recorded NOAA retrieval."""
    if not isinstance(retrieval, Retrieval):
        raise TypeError("retrieval must be a recorded RetrievalEpisode")
    source_id = retrieval.episode.get("source_id")
    if not isinstance(source_id, str) or source_id not in PRODUCTS:
        raise fetch.FetchInputError("EPISODE_SOURCE_MISMATCH")
    retrieval_episode.require_source(retrieval, source_id=source_id,
                                     retrieval_profile_ref=PRODUCTS[source_id])
    URL_RULES[source_id](retrieval.source_url)  # re-apply fetch's URL rule
    episode = retrieval.episode
    parsed = None
    if not retrieval.captured:
        provisional, reasons = HOLD, tuple(episode["result"]["reason_codes"])
    else:
        provisional, reasons, parsed = _parse(source_id, retrieval, episode)
    blockers = (() if source_id in ROLE_COVERED_PRODUCTS else ("PRODUCT_ROLE_UNRESOLVED",)) \
        + descriptor_blockers(load_descriptor() if descriptor is None else descriptor)
    route = HOLD if blockers else provisional
    return AdmissionDecision(
        route, provisional, reasons + blockers, episode["episode_id"], source_id,
        retrieval.source_url,
        parsed if source_id == fetch.STORM_SOURCE_ID else None,
        parsed if source_id == fetch.USCRN_SOURCE_ID else None,
        parsed if source_id == fetch.NWS_SOURCE_ID else None)
