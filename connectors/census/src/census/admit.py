"""Route one recorded Census retrieval (ACS table or TIGER/Line package); never writes.

The episode's own source identity selects the product: ``census.acs-api`` episodes are
parsed by ``acs_api.parse_response`` and ``census.tiger-line`` episodes are inspected by
``tiger_package.inspect_package`` against their manifest entry. Anything else is refused
(``EPISODE_SOURCE_MISMATCH``).

A response that was not captured is held; captured bytes that the product parser rejects
are a quarantine candidate. A parsed ACS table is a raw candidate, flagged when rows are
quarantine candidates or the table carries its own reasons. An inspected TIGER package
keeps the route the inspector assigned. The final route is HOLD while the connector
descriptor leaves ``role`` or ``rights`` unresolved. TIGER/Line geometry is reference
geometry, not legal-boundary, cadastral or demographic authority. Nothing here grants
admission, establishes coverage, or persists material.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from connectors_core import descriptor_gate, retrieval_episode

from . import acs_api, fetch, tiger_package
from .fetch import Retrieval

DESCRIPTOR = Path(__file__).resolve().with_name("descriptor.yaml")
NAME = "census"
RAW = "RAW_CANDIDATE"
QUARANTINE = "QUARANTINE_CANDIDATE"
HOLD = "HOLD"
# Source role is product-level, set by the repository owner on 2026-09-28. The family
# descriptor still gates role/rights resolution; each decision carries its product's own
# role. A product missing here holds with PRODUCT_ROLE_UNRESOLVED.
PRODUCT_ROLES = {
    fetch.ACS_SOURCE_ID: "aggregate",          # survey estimate tables
    fetch.TIGER_SOURCE_ID: "administrative",   # reference geometry, not legal-boundary authority
}
PRODUCTS = {fetch.ACS_SOURCE_ID: fetch.ACS_RETRIEVAL_PROFILE,
            fetch.TIGER_SOURCE_ID: fetch.TIGER_RETRIEVAL_PROFILE}


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
    table: acs_api.AcsTableCandidate | None
    package: tiger_package.PackageCandidate | None
    # Routing is not admission, a coverage claim, or a write to data/raw or data/quarantine.
    admission: str = "NOT_ADMITTED"
    coverage: str = "NOT_ESTABLISHED"
    write_performed: bool = False
    # The product's source role (``PRODUCT_ROLES``), or None when it is unresolved.
    source_role: str | None = None


def _acs(retrieval: Retrieval, episode: dict):
    try:
        table = acs_api.parse_response(
            retrieval.body, status=episode["transport"]["http_status"],
            source_url=retrieval.source_url, retrieved_at=episode["completed_at"])
    except acs_api.AcsInputError as error:
        return QUARANTINE, (f"PARSE_{error.args[0]}",), None
    flags = (("RECORD_QUARANTINE_CANDIDATES",)
             if any(row.route == QUARANTINE for row in table.rows) else ())
    return RAW, flags + tuple(table.table_reasons), table


def _tiger(retrieval: Retrieval, manifest: dict | None):
    file_name = retrieval.source_url.rsplit("/", 1)[-1]
    try:
        entry = fetch.tiger_entry(file_name, manifest)
        package = tiger_package.inspect_package(retrieval.body, file_name=file_name,
                                                entry=entry)
    except tiger_package.TigerPackageError as error:
        return QUARANTINE, (f"PARSE_{error.args[0]}",), None
    return package.route, tuple(package.reasons), package


def admit(retrieval: Retrieval, *, descriptor: dict[str, str] | None = None,
          manifest: dict | None = None) -> AdmissionDecision:
    """Decide a candidate lane for one recorded Census retrieval."""
    if not isinstance(retrieval, Retrieval):
        raise TypeError("retrieval must be a recorded RetrievalEpisode")
    source_id = retrieval.episode.get("source_id")
    if not isinstance(source_id, str) or source_id not in PRODUCTS:
        raise fetch.FetchInputError("EPISODE_SOURCE_MISMATCH")
    retrieval_episode.require_source(retrieval, source_id=source_id,
                                     retrieval_profile_ref=PRODUCTS[source_id])
    # Re-apply fetch's product-specific URL rule: stored or reconstructed episodes must
    # carry exactly the URL the planner or the manifest would have issued.
    if source_id == fetch.ACS_SOURCE_ID:
        fetch._require_planned_acs(retrieval.source_url)
    elif fetch.tiger_entry(retrieval.source_url.rsplit("/", 1)[-1],
                           manifest)["source_url"] != retrieval.source_url:
        raise tiger_package.TigerPackageError("SOURCE_URL_SCOPE")
    episode = retrieval.episode
    table = package = None
    if not retrieval.captured:
        provisional, reasons = HOLD, tuple(episode["result"]["reason_codes"])
    elif source_id == fetch.ACS_SOURCE_ID:
        provisional, reasons, table = _acs(retrieval, episode)
    else:
        provisional, reasons, package = _tiger(retrieval, manifest)
    blockers = (() if source_id in PRODUCT_ROLES else ("PRODUCT_ROLE_UNRESOLVED",)) \
        + descriptor_blockers(load_descriptor() if descriptor is None else descriptor)
    route = HOLD if blockers else provisional
    return AdmissionDecision(route, provisional, reasons + blockers, episode["episode_id"],
                             source_id, retrieval.source_url, table, package,
                             source_role=PRODUCT_ROLES.get(source_id))
