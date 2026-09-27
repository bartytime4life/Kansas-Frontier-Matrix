"""Route one recorded USGS earthquake retrieval to a candidate lane; never writes.

A response that was not captured is held; captured bytes that the parser rejects are a
quarantine candidate; parsed bytes are a raw candidate. Whatever the provisional lane,
the final route is HOLD while the connector descriptor leaves ``role`` or ``rights``
unresolved: rights and source role are steward decisions, not something this module may
infer. The recorded episode re-validates its own identity and bytes on construction.
Nothing here grants admission, establishes coverage, or persists material.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from connectors_core import descriptor_gate, retrieval_episode

from . import earthquake
from . import fetch
from .fetch import Retrieval

DESCRIPTOR = Path(__file__).resolve().with_name("descriptor.yaml")
NAME = "usgs"
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
    snapshot: earthquake.SnapshotCandidate | None
    # Routing is not admission, a coverage claim, or a write to data/raw or data/quarantine.
    admission: str = "NOT_ADMITTED"
    coverage: str = "NOT_ESTABLISHED"
    write_performed: bool = False


def admit(retrieval: Retrieval, *, descriptor: dict[str, str] | None = None) -> AdmissionDecision:
    """Decide a candidate lane for one recorded retrieval."""
    retrieval_episode.require_source(retrieval, source_id=fetch.SOURCE_ID,
                                     retrieval_profile_ref=fetch.RETRIEVAL_PROFILE)
    earthquake._request_kind(retrieval.source_url)  # re-apply fetch's URL rule
    episode = retrieval.episode
    snapshot = None
    if not retrieval.captured:
        provisional, reasons = HOLD, tuple(episode["result"]["reason_codes"])
    else:
        try:
            snapshot = earthquake.parse_snapshot(
                retrieval.body, status=episode["transport"]["http_status"],
                source_url=retrieval.source_url, retrieved_at=episode["completed_at"])
        except earthquake.EarthquakeInputError as error:
            provisional, reasons = QUARANTINE, (f"PARSE_{error.args[0]}",)
        else:
            provisional = RAW
            reasons = ("QUERY_LIMIT_REACHED",) if snapshot.query_limit_reached else ()
    blockers = descriptor_blockers(load_descriptor() if descriptor is None else descriptor)
    route = HOLD if blockers else provisional
    return AdmissionDecision(route, provisional, reasons + blockers, episode["episode_id"],
                             retrieval.source_url, snapshot)
