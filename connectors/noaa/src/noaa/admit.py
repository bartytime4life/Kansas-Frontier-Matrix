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
connector descriptor leaves ``role`` or ``rights`` unresolved. Nothing here grants
admission, establishes coverage, relays an alert, or persists material.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from connectors_core import descriptor_gate, retrieval_episode

from . import fetch, nws_alerts, storm_events, uscrn_hourly
from .fetch import Retrieval

DESCRIPTOR = Path(__file__).resolve().with_name("descriptor.yaml")
NAME = "noaa"
RAW = "RAW_CANDIDATE"
QUARANTINE = "QUARANTINE_CANDIDATE"
HOLD = "HOLD"
PRODUCTS = {fetch.STORM_SOURCE_ID: fetch.STORM_RETRIEVAL_PROFILE,
            fetch.USCRN_SOURCE_ID: fetch.USCRN_RETRIEVAL_PROFILE,
            fetch.NWS_SOURCE_ID: fetch.NWS_RETRIEVAL_PROFILE}
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
        parsed = nws_alerts.parse_alerts(retrieval.body, **common)
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
    if source_id not in PRODUCTS:
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
    blockers = descriptor_blockers(load_descriptor() if descriptor is None else descriptor)
    route = HOLD if blockers else provisional
    return AdmissionDecision(
        route, provisional, reasons + blockers, episode["episode_id"], source_id,
        retrieval.source_url,
        parsed if source_id == fetch.STORM_SOURCE_ID else None,
        parsed if source_id == fetch.USCRN_SOURCE_ID else None,
        parsed if source_id == fetch.NWS_SOURCE_ID else None)
