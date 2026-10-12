"""Route one recorded OpenFEMA declarations page to a candidate lane; never writes.

A response that was not captured is held; captured bytes that the page parser rejects
are a quarantine candidate; a parsed page is a raw candidate, flagged when any of its
declaration records is itself a quarantine candidate. Whatever the provisional lane,
the final route is HOLD while the connector descriptor leaves ``role`` or ``rights``
unresolved. A page is one step of a keyset capture: completeness is established only by
``openfema_declarations.reconcile`` over the whole chain. Nothing here grants admission,
establishes coverage, or persists material. Declarations are administrative records,
not observed hazard footprints.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from connectors_core import descriptor_gate, retrieval_episode

from . import openfema_declarations as declarations
from . import fetch
from .fetch import Retrieval

DESCRIPTOR = Path(__file__).resolve().with_name("descriptor.yaml")
NAME = "fema"
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
    page: declarations.PageCandidate | None
    # Routing is not admission, a coverage claim, or a write to data/raw or data/quarantine.
    admission: str = "NOT_ADMITTED"
    coverage: str = "NOT_ESTABLISHED"
    write_performed: bool = False


def admit(retrieval: Retrieval, *, descriptor: dict[str, str] | None = None) -> AdmissionDecision:
    """Decide a candidate lane for one recorded page retrieval."""
    retrieval_episode.require_source(retrieval, source_id=fetch.SOURCE_ID,
                                     retrieval_profile_ref=fetch.RETRIEVAL_PROFILE)
    declarations._request(retrieval.source_url)  # re-apply fetch's URL rule
    episode = retrieval.episode
    page = None
    if not retrieval.captured:
        provisional, reasons = HOLD, tuple(episode["result"]["reason_codes"])
    else:
        try:
            page = declarations.parse_page(
                retrieval.body, status=episode["transport"]["http_status"],
                source_url=retrieval.source_url, retrieved_at=episode["completed_at"])
        except declarations.OpenFemaInputError as error:
            provisional, reasons = QUARANTINE, (f"PARSE_{error.args[0]}",)
        else:
            provisional = RAW
            reasons = (("RECORD_QUARANTINE_CANDIDATES",)
                       if any(r.route == QUARANTINE for r in page.records) else ())
    blockers = descriptor_blockers(load_descriptor() if descriptor is None else descriptor)
    route = HOLD if blockers else provisional
    return AdmissionDecision(route, provisional, reasons + blockers, episode["episode_id"],
                             retrieval.source_url, page)
