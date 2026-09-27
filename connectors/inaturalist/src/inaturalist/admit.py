"""Route one recorded iNaturalist observations page to a candidate lane; never writes.

A response that was not captured is held; captured bytes that the page parser rejects
are a quarantine candidate; a parsed page is a raw candidate carrying page-level flags.
Every page with records is flagged ``SENSITIVITY_NOT_EVALUATED``: this connector cannot
judge taxon or location sensitivity. Obscured and private geoprivacy records are already
quarantine candidates at record level, and their coordinates are never de-obscured here.

The final route is HOLD while the connector descriptor leaves ``role`` or ``rights``
unresolved, and also unless ``sensitivity_floor`` is a reviewed non-public value
(``generalized``, ``restricted``, ``quarantine``): the connector-local ``public`` floor is an
unsafe placeholder (see connectors/inaturalist/README.md). A page is one step of a cursor
walk; continuity is established only by ``observations_api.reconcile``. Nothing here
grants admission, establishes coverage, evaluates sensitivity, or persists material.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from connectors_core import descriptor_gate

from . import observations_api
from .fetch import Retrieval

DESCRIPTOR = Path(__file__).resolve().with_name("descriptor.yaml")
NAME = "inaturalist"
RAW = "RAW_CANDIDATE"
QUARANTINE = "QUARANTINE_CANDIDATE"
HOLD = "HOLD"
# Record-level reasons surfaced as page-level flags (record route is unchanged).
PAGE_FLAGS = (
    ({"GEOPRIVACY_OBSCURED", "GEOPRIVACY_PRIVATE"}, "GEOPRIVACY_RESTRICTED_PRESENT"),
    ({"NONCOMMERCIAL_TERMS", "SHAREALIKE_TERMS", "NODERIVATIVES_TERMS"},
     "LICENSE_OBLIGATIONS_PRESENT"),
    ({"NOT_RESEARCH_GRADE"}, "NOT_RESEARCH_GRADE_PRESENT"),
    ({"CAPTIVE_OR_CULTIVATED"}, "CAPTIVE_OR_CULTIVATED_PRESENT"),
)


def load_descriptor(path: Path = DESCRIPTOR) -> dict[str, str]:
    return descriptor_gate.load_descriptor(path)


def descriptor_blockers(descriptor: dict[str, str]) -> tuple[str, ...]:
    blockers = descriptor_gate.descriptor_blockers(descriptor, name=NAME)
    if blockers == ("DESCRIPTOR_INVALID",):
        return blockers
    return blockers + descriptor_gate.sensitivity_floor_blockers(descriptor)


def _page_flags(page: observations_api.PageCandidate) -> tuple[str, ...]:
    reasons = {reason for record in page.records for reason in record.reasons}
    flags = ["SENSITIVITY_NOT_EVALUATED"] if page.records else []
    if any(record.route == QUARANTINE for record in page.records):
        flags.append("RECORD_QUARANTINE_CANDIDATES")
    flags.extend(flag for members, flag in PAGE_FLAGS if reasons & members)
    return tuple(flags)


@dataclass(frozen=True)
class AdmissionDecision:
    route: str
    provisional_route: str
    reasons: tuple[str, ...]
    episode_id: str
    source_url: str
    page: observations_api.PageCandidate | None
    # Routing is not admission, a coverage claim, a sensitivity decision, or a write.
    admission: str = "NOT_ADMITTED"
    coverage: str = "NOT_ESTABLISHED"
    sensitivity: str = "NOT_EVALUATED"
    write_performed: bool = False


def admit(retrieval: Retrieval, *, descriptor: dict[str, str] | None = None) -> AdmissionDecision:
    """Decide a candidate lane for one recorded cursor-page retrieval."""
    if not isinstance(retrieval, Retrieval):
        raise TypeError("retrieval must be a recorded RetrievalEpisode")
    episode = retrieval.episode
    page = None
    if not retrieval.captured:
        provisional, reasons = HOLD, tuple(episode["result"]["reason_codes"])
    else:
        try:
            page = observations_api.parse_page(
                retrieval.body, status=episode["transport"]["http_status"],
                source_url=retrieval.source_url, retrieved_at=episode["completed_at"])
        except observations_api.ObservationInputError as error:
            provisional, reasons = QUARANTINE, (f"PARSE_{error.args[0]}",)
        else:
            provisional, reasons = RAW, _page_flags(page)
    blockers = descriptor_blockers(load_descriptor() if descriptor is None else descriptor)
    route = HOLD if blockers else provisional
    return AdmissionDecision(route, provisional, reasons + blockers, episode["episode_id"],
                             retrieval.source_url, page)
