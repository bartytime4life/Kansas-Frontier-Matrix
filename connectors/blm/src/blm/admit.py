"""Route one recorded BLM PLSS (CadNSDI) query page; never writes.

The episode must carry this connector's source identity and profile, and fetch's planner
URL rule is re-applied so a stored or reconstructed episode cannot carry a URL the planner
would not have issued. A response that was not captured is held; captured bytes that
``plss_cadnsdi.parse_page`` rejects are a quarantine candidate. A parsed page is a raw
candidate, flagged ``RECORD_QUARANTINE_CANDIDATES`` when any feature is a quarantine
candidate (open ring or geometry outside the Kansas extent) and ``MORE_PAGES`` when the
service reports, or a full page implies, further features. The final route is HOLD while
the connector descriptor leaves ``role`` or ``rights`` unresolved. PLSS geometry is
survey reference context, never parcel ownership, title, deed, or access authority;
nothing here grants admission, establishes coverage, or persists material.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from connectors_core import descriptor_gate, retrieval_episode

from . import fetch, plss_cadnsdi
from .fetch import Retrieval

DESCRIPTOR = Path(__file__).resolve().with_name("descriptor.yaml")
NAME = "blm"
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
    page: plss_cadnsdi.PlssPageCandidate | None
    # Routing is not admission, a coverage claim, or a write to data/raw or data/quarantine.
    admission: str = "NOT_ADMITTED"
    coverage: str = "NOT_ESTABLISHED"
    write_performed: bool = False


def admit(retrieval: Retrieval, *,
          descriptor: dict[str, str] | None = None) -> AdmissionDecision:
    """Decide a candidate lane for one recorded PLSS query page."""
    retrieval_episode.require_source(retrieval, source_id=fetch.SOURCE_ID,
                                     retrieval_profile_ref=fetch.RETRIEVAL_PROFILE)
    fetch._require_planned(retrieval.source_url)  # re-apply fetch's URL rule
    episode = retrieval.episode
    page = None
    if not retrieval.captured:
        provisional, reasons = HOLD, tuple(episode["result"]["reason_codes"])
    else:
        try:
            page = plss_cadnsdi.parse_page(retrieval.body,
                                           status=episode["transport"]["http_status"],
                                           source_url=retrieval.source_url,
                                           retrieved_at=episode["completed_at"])
            flags = []
            if any(feature.route == QUARANTINE for feature in page.features):
                flags.append("RECORD_QUARANTINE_CANDIDATES")
            if page.more_pages:
                flags.append("MORE_PAGES")
            provisional, reasons = RAW, tuple(flags)
        except plss_cadnsdi.PlssInputError as error:
            provisional, reasons = QUARANTINE, (f"PARSE_{error.args[0]}",)
    blockers = descriptor_blockers(load_descriptor() if descriptor is None else descriptor)
    route = HOLD if blockers else provisional
    return AdmissionDecision(route, provisional, reasons + blockers, episode["episode_id"],
                             retrieval.source_url, page)
