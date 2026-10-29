"""Canonical draft OccurrenceEvidence identity shared by packages and tools.

Identity compatibility is intentional: this retains the existing draft subject,
which does not bind source family or role. It must not be used as an admission,
release, or global cross-source deduplication key.
"""
from __future__ import annotations

from typing import Any, Mapping

def occurrence_identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    """Return the exact Pass-3 identity subject for RFC 8785 + SHA-256."""

    observation = candidate.get("observation")
    geometry = candidate.get("geometry")
    taxon = candidate.get("taxon")
    if not isinstance(observation, Mapping):
        observation = {}
    if not isinstance(geometry, Mapping):
        geometry = {}
    if not isinstance(taxon, Mapping):
        taxon = {}

    normalized_geometry = {
        "geoprivacy_status": geometry.get("geoprivacy_status"),
        "latitude": geometry.get("latitude"),
        "longitude": geometry.get("longitude"),
        "precision_class": geometry.get("precision_class"),
        "public_safe_geometry": geometry.get("public_safe_geometry"),
    }
    return {
        "accepted_taxon_name": taxon.get("accepted_scientific_name"),
        "event_date": observation.get("event_date"),
        "normalized_geometry": normalized_geometry,
        "source_record_id": candidate.get("source_record_id"),
    }


def compute_occurrence_spec_hash(candidate: Mapping[str, Any]) -> str:
    """Compute the deterministic occurrence identity digest."""

    try:
        from hashing import compute_spec_hash
    except ImportError as exc:
        raise RuntimeError("hashing package unavailable") from exc
    return compute_spec_hash(occurrence_identity_subject(candidate))
