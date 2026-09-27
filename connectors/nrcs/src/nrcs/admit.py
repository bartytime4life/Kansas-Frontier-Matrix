"""Route one recorded NRCS SCAN (AWDB) retrieval; never writes.

The episode must carry this connector's source identity and profile, and fetch's planner
URL rule is re-applied so a stored or reconstructed episode cannot carry a URL the planner
would not have issued. A response that was not captured is held; captured bytes that
``scan_awdb.parse_data`` rejects are a quarantine candidate. A parsed response is a raw
candidate, flagged ``RECORD_QUARANTINE_CANDIDATES`` when any value is a quarantine
candidate, ``MISSING_VALUES_PRESENT`` when any value is missing (never zero),
``EMPTY_SERIES_PRESENT`` when a series has no values (not absence), and
``DEPTH_NOT_STATED`` when a soil series states no depth, and
``REQUESTED_SERIES_NOT_RETURNED`` when a requested station/element has no series. The final route is HOLD while the
connector descriptor leaves ``role`` or ``rights`` unresolved. A SCAN value is a station
observation, never area truth; nothing here grants admission, establishes coverage, or
persists material.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from connectors_core import descriptor_gate, retrieval_episode

from . import fetch, scan_awdb
from .fetch import Retrieval

DESCRIPTOR = Path(__file__).resolve().with_name("descriptor.yaml")
NAME = "nrcs"
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
    data: scan_awdb.ScanDataCandidate | None
    # Routing is not admission, a coverage claim, or a write to data/raw or data/quarantine.
    admission: str = "NOT_ADMITTED"
    coverage: str = "NOT_ESTABLISHED"
    write_performed: bool = False


def _flags(data: scan_awdb.ScanDataCandidate) -> tuple[str, ...]:
    values = [value for series in data.series for value in series.values]
    series_reasons = {reason for series in data.series for reason in series.reasons}
    flags = []
    if any(value.route == QUARANTINE for value in values):
        flags.append("RECORD_QUARANTINE_CANDIDATES")
    if any(value.missing for value in values):
        flags.append("MISSING_VALUES_PRESENT")
    if "EMPTY_SERIES_NOT_ABSENCE" in series_reasons:
        flags.append("EMPTY_SERIES_PRESENT")
    if "DEPTH_NOT_STATED" in series_reasons:
        flags.append("DEPTH_NOT_STATED")
    if data.unreturned:
        flags.append("REQUESTED_SERIES_NOT_RETURNED")
    return tuple(flags)


def admit(retrieval: Retrieval, *,
          descriptor: dict[str, str] | None = None) -> AdmissionDecision:
    """Decide a candidate lane for one recorded SCAN retrieval."""
    retrieval_episode.require_source(retrieval, source_id=fetch.SOURCE_ID,
                                     retrieval_profile_ref=fetch.RETRIEVAL_PROFILE)
    fetch._require_planned(retrieval.source_url)  # re-apply fetch's URL rule
    episode = retrieval.episode
    data = None
    if not retrieval.captured:
        provisional, reasons = HOLD, tuple(episode["result"]["reason_codes"])
    else:
        try:
            data = scan_awdb.parse_data(retrieval.body,
                                        status=episode["transport"]["http_status"],
                                        source_url=retrieval.source_url,
                                        retrieved_at=episode["completed_at"])
            provisional, reasons = RAW, _flags(data)
        except scan_awdb.ScanInputError as error:
            provisional, reasons = QUARANTINE, (f"PARSE_{error.args[0]}",)
    blockers = descriptor_blockers(load_descriptor() if descriptor is None else descriptor)
    route = HOLD if blockers else provisional
    return AdmissionDecision(route, provisional, reasons + blockers, episode["episode_id"],
                             retrieval.source_url, data)
