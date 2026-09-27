"""Route one recorded GBIF occurrence-search page to a candidate lane; never writes.

A response that was not captured is held; captured bytes that the page parser rejects
are a quarantine candidate; a parsed page is a raw candidate carrying page-level flags.
Every page with records is flagged ``SENSITIVITY_NOT_EVALUATED``: this connector cannot
judge taxon or location sensitivity, and coordinates are carried exactly as supplied.

The final route is HOLD while the connector descriptor leaves ``role`` or ``rights``
unresolved, and also unless ``sensitivity_floor`` is a recognized non-public value
(``generalized``, ``restricted``, ``quarantine``): GBIF
occurrences can carry rare-species or precise-location concerns, so a public floor is an
unsafe placeholder that must not authorize a candidate route (see connectors/gbif/README.md).
A page is one step of an offset capture; continuity is established only by
``occurrence_api.reconcile`` over all pages. Nothing here grants admission, establishes
coverage, evaluates sensitivity, or persists material.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from connectors_core import descriptor_gate, retrieval_episode

from . import occurrence_api
from . import fetch
from .fetch import Retrieval

DESCRIPTOR = Path(__file__).resolve().with_name("descriptor.yaml")
NAME = "gbif"
RAW = "RAW_CANDIDATE"
QUARANTINE = "QUARANTINE_CANDIDATE"
HOLD = "HOLD"


def load_descriptor(path: Path = DESCRIPTOR) -> dict[str, str]:
    return descriptor_gate.load_descriptor(path)


def descriptor_blockers(descriptor: dict[str, str]) -> tuple[str, ...]:
    blockers = descriptor_gate.descriptor_blockers(descriptor, name=NAME)
    if blockers == ("DESCRIPTOR_INVALID",):
        return blockers
    return blockers + descriptor_gate.sensitivity_floor_blockers(descriptor)


def _page_flags(page: occurrence_api.PageCandidate) -> tuple[str, ...]:
    reasons = {reason for record in page.records for reason in record.reasons}
    flags = []
    if page.records:
        flags.append("SENSITIVITY_NOT_EVALUATED")
    if any(record.route == QUARANTINE for record in page.records):
        flags.append("RECORD_QUARANTINE_CANDIDATES")
    if "NONCOMMERCIAL_TERMS" in reasons:
        flags.append("NONCOMMERCIAL_TERMS_PRESENT")
    if "ABSENCE_ASSERTION" in reasons:
        flags.append("ABSENCE_ASSERTIONS_PRESENT")
    if page.count > occurrence_api.PAGING_CEILING:
        flags.append("PAGING_CEILING_USE_ASYNC_DOWNLOAD")
    return tuple(flags)


@dataclass(frozen=True)
class AdmissionDecision:
    route: str
    provisional_route: str
    reasons: tuple[str, ...]
    episode_id: str
    source_url: str
    page: occurrence_api.PageCandidate | None
    # Routing is not admission, a coverage claim, a sensitivity decision, or a write.
    admission: str = "NOT_ADMITTED"
    coverage: str = "NOT_ESTABLISHED"
    sensitivity: str = "NOT_EVALUATED"
    write_performed: bool = False


def admit(retrieval: Retrieval, *, descriptor: dict[str, str] | None = None) -> AdmissionDecision:
    """Decide a candidate lane for one recorded page retrieval."""
    retrieval_episode.require_source(retrieval, source_id=fetch.SOURCE_ID,
                                     retrieval_profile_ref=fetch.RETRIEVAL_PROFILE)
    episode = retrieval.episode
    page = None
    if not retrieval.captured:
        provisional, reasons = HOLD, tuple(episode["result"]["reason_codes"])
    else:
        try:
            page = occurrence_api.parse_page(
                retrieval.body, status=episode["transport"]["http_status"],
                source_url=retrieval.source_url, retrieved_at=episode["completed_at"])
        except occurrence_api.OccurrenceInputError as error:
            provisional, reasons = QUARANTINE, (f"PARSE_{error.args[0]}",)
        else:
            provisional, reasons = RAW, _page_flags(page)
    blockers = descriptor_blockers(load_descriptor() if descriptor is None else descriptor)
    route = HOLD if blockers else provisional
    return AdmissionDecision(route, provisional, reasons + blockers, episode["episode_id"],
                             retrieval.source_url, page)
