"""Route one recorded EPA AQS AirData daily-summary retrieval; never writes.

The episode must carry this connector's source identity and profile, and fetch's planner
URL rule is re-applied so a stored or reconstructed episode cannot carry a URL the planner
would not have issued. A response that was not captured is held; captured bytes that
``aqs_airdata.parse_daily_file`` rejects are a quarantine candidate. A parsed archive is a
raw candidate, flagged ``RECORD_QUARANTINE_CANDIDATES`` when any Kansas row is a
quarantine candidate, ``EVENT_TREATED_ROWS_PRESENT`` when any row was computed with or
without event-associated values, ``AQI_NOT_REPORTED_PRESENT`` when any row has a blank
AQI, and ``NO_KANSAS_ROWS`` when the file attributes no row to Kansas (not absence of
pollution or monitors). The final route is HOLD while the connector descriptor leaves
``role`` or ``rights`` unresolved. A daily summary is a monitor statistic, never area
truth, exposure, or attainment; nothing here grants admission, establishes coverage, or
persists material.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from connectors_core import descriptor_gate, retrieval_episode

from . import aqs_airdata, fetch
from .fetch import Retrieval

DESCRIPTOR = Path(__file__).resolve().with_name("descriptor.yaml")
NAME = "epa"
RAW = "RAW_CANDIDATE"
QUARANTINE = "QUARANTINE_CANDIDATE"
HOLD = "HOLD"


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
    source_url: str
    daily_file: aqs_airdata.DailyFileCandidate | None
    # Routing is not admission, a coverage claim, or a write to data/raw or data/quarantine.
    admission: str = "NOT_ADMITTED"
    coverage: str = "NOT_ESTABLISHED"
    write_performed: bool = False


def _flags(daily: aqs_airdata.DailyFileCandidate) -> tuple[str, ...]:
    reasons = {reason for record in daily.records for reason in record.reasons}
    flags = []
    if any(record.route == QUARANTINE for record in daily.records):
        flags.append("RECORD_QUARANTINE_CANDIDATES")
    if reasons & {"EVENTS_INCLUDED", "EVENTS_EXCLUDED"}:
        flags.append("EVENT_TREATED_ROWS_PRESENT")
    if "AQI_NOT_REPORTED" in reasons:
        flags.append("AQI_NOT_REPORTED_PRESENT")
    if not daily.records:
        flags.append("NO_KANSAS_ROWS")
    return tuple(flags)


def admit(retrieval: Retrieval, *,
          descriptor: dict[str, str] | None = None) -> AdmissionDecision:
    """Decide a candidate lane for one recorded AirData daily-summary retrieval."""
    retrieval_episode.require_source(retrieval, source_id=fetch.SOURCE_ID,
                                     retrieval_profile_ref=fetch.RETRIEVAL_PROFILE)
    fetch._require_planned(retrieval.source_url)  # re-apply fetch's URL rule
    episode = retrieval.episode
    daily = None
    if not retrieval.captured:
        provisional, reasons = HOLD, tuple(episode["result"]["reason_codes"])
    else:
        try:
            daily = aqs_airdata.parse_daily_file(retrieval.body,
                                                 status=episode["transport"]["http_status"],
                                                 source_url=retrieval.source_url,
                                                 retrieved_at=episode["completed_at"])
            provisional, reasons = RAW, _flags(daily)
        except aqs_airdata.AqsInputError as error:
            provisional, reasons = QUARANTINE, (f"PARSE_{error.args[0]}",)
    blockers = descriptor_blockers(load_descriptor() if descriptor is None else descriptor)
    route = HOLD if blockers else provisional
    return AdmissionDecision(route, provisional, reasons + blockers, episode["episode_id"],
                             retrieval.source_url, daily)
