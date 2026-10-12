"""Compose a USGS ComCat earthquake review carrier from a validated WORK candidate.

Mirrors pipelines/domains/hazards/storm_events_package.py with the EARTHQUAKES
snapshot profile. It has no stations: evidence is one bundle per UTC origin
month that has events, split into numbered parts of 127 records so every bundle
stays inside the resolver's 128-member limit. Records are ``record`` members.
Preparation grants no lifecycle transition: without ``admission`` every bundle
carries the rights/sensitivity hold, and release still needs a trusted
kfm.earthquake-release-decision/v1 record that passes the serving gate.
"""
from collections import Counter
from datetime import timezone

from connectors_core.captured_json import canonical_bytes, digest_bytes, utc_time
from evidence_resolver.core import PROFILE, evaluate_resolution_candidate
from evidence_resolver.verification_history import canonical_spec_hash
from hashing import compute_spec_hash
from release.core import EARTHQUAKES, prepare_snapshot
from connectors.usgs.src.usgs.earthquake_capture import object_url
from pipelines.domains.hazards.earthquake_validate import validate_candidate

EVIDENCE_PROFILE = "kfm.earthquake-evidence-candidate/v1"
CATALOG_PROFILE = "kfm.earthquake-catalog-candidate/v1"
CATALOG_URL = "https://earthquake.usgs.gov/data/comcat/"


def earthquake_catalog(candidate: dict, validation: dict, start: str) -> dict:
    """Discovery projection for already validated records; candidate metadata only."""
    if (validation.get("candidate_id") != candidate.get("candidate_id")
            or validation.get("outcome") != "PASS"
            or validation.get("receipt_digest") != digest_bytes(canonical_bytes({k: v for k, v in validation.items() if k != "receipt_digest"}))):
        raise ValueError("CATALOG_VALIDATION_REQUIRED")
    observations = candidate["observations"]
    months = [{"month": month, "part": part, "observation_count": len(records),
               "evidence_ref": EARTHQUAKES.month_ref(start, month, part, candidate["candidate_id"])}
              for month, part, records in EARTHQUAKES.month_groups(observations)]
    magnitudes = [r["magnitude"] for r in observations if r["magnitude"] is not None]
    dataset = {"id": "usgs-earthquakes:ks-envelope:" + str(candidate["data_year"]),
               "title": "USGS ComCat earthquakes, Kansas context envelope, " + str(candidate["data_year"]),
               "source_id": candidate["source_id"], "bounds": candidate["bounds"],
               "data_year": candidate["data_year"], "observation_count": len(observations),
               "withheld_counts": candidate["withheld_counts"],
               "context_margin_count": sum(1 for r in observations if "CONTEXT_MARGIN" in r["flags"]),
               "review_status": dict(sorted(Counter(r["review_status"] or "unknown" for r in observations).items())),
               "magnitude_range": [min(magnitudes), max(magnitudes)] if magnitudes else None,
               "latest_event_date": candidate["latest_event_date"], "year_state": candidate["year_state"],
               "coverage": candidate["coverage"],
               "interval": {"start": start, "end": start[:4] + "-12-31", "basis": "origin time, UTC"},
               "validation_ref": validation["receipt_digest"]}
    return {"profile": CATALOG_PROFILE, "candidate_id": candidate["candidate_id"], "dataset": dataset,
            "entries": months, "authoritative": False, "release_state": "UNRELEASED"}


def prepare_earthquake_package(candidate: dict, *, rollback_target=None, admission: dict | None = None) -> dict:
    """``admission`` comes from earthquake_admission.load_admission(); it releases nothing."""
    validation = validate_candidate(candidate)
    start, _ = EARTHQUAKES.candidate_window(candidate)
    groups = EARTHQUAKES.month_groups(candidate["observations"])
    if not groups:
        raise ValueError("NO_EVENTS_TO_PACKAGE")
    catalog = earthquake_catalog(candidate, validation, start)
    verified_at = utc_time(candidate["retrieved_at"]).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    short = candidate["candidate_id"].split(":")[1]
    entries = []
    for month, part, records in groups:
        label = f"{start[:4]}-{month:02d}"
        parts = sum(1 for m, _, _ in groups if m == month)
        bundle_id = f"earthquakes:{label}:part-{part}:{short}"
        ref = {"ref": EARTHQUAKES.month_ref(start, month, part, candidate["candidate_id"]), "kind": "dataset", "bundle_ref": bundle_id}
        bundle = {"bundle_id": bundle_id,
                  "claim_scope": ("Preserved USGS ANSS ComCat earthquake solutions with epicenters in the Kansas context "
                                  "envelope (-102.1 to -94.5 longitude, 36.9 to 40.1 latitude; not the state boundary), "
                                  "origin times in " + label + " (UTC), part " + str(part) + " of " + str(parts)
                                  + "; catalog solutions at retrieval, not shaking, damage or felt reports; solutions "
                                  "subject to revision; review candidate only."),
                  "evidence_refs": [ref] + [{"ref": r["evidence_ref"], "kind": EARTHQUAKES.member_kind, "bundle_ref": bundle_id}
                                            for r in records],
                  "source_records": sorted({r["page_digest"] for r in records}),
                  "citations": [object_url(label), CATALOG_URL],
                  "rights": {"license": admission["license"] if admission else "USGS source terms; independent rights review required"},
                  "sensitivity": ({"level": "public", "reason": "Admitted public source " + admission["source_ref"], "applied_at": verified_at}
                                  if admission else
                                  {"level": "quarantine", "reason": "Candidate pending source, rights and sensitivity review", "applied_at": verified_at}),
                  "transforms": ["kfm:transform:earthquake-pilot:v1"],
                  "checksums": {"candidate": candidate["candidate_id"], "validation": validation["receipt_digest"]}}
        bundle["spec_hash"] = {"value": compute_spec_hash(bundle)}
        history = {"schema_version": "1.0.0", "history_id": f"kfm:verification-history:earthquakes:{label}:part-{part}",
                   "subject_ref": ref["ref"], "profile_id": "kfm://profile/verification-state-replay/v1",
                   "events": [{"event_id": "evt:001", "event_type": "VERIFIED", "state": "ACTIVE",
                               "effective_at": verified_at, "recorded_at": verified_at,
                               "reason_code": "CAPTURE_AND_TRANSFORMATION_VALIDATED",
                               "basis_refs": ["kfm://receipt/validation/" + validation["receipt_digest"].split(":")[1]]}]}
        history["spec_hash"] = canonical_spec_hash(history)
        request = {"profile": PROFILE, "evidence_ref": ref, "bundle_candidate": bundle,
                   "lookup_context": {"bundle_id": bundle_id, "current_head": True, "policy_outcome": "ABSTAIN",
                                      "policy_decision_ref": None, "correction_state": "ACTIVE", "correction_ref": None},
                   "verification_history": history,
                   "verification_as_of": {"effective_as_of": verified_at, "recorded_as_of": verified_at}}
        resolution = evaluate_resolution_candidate(request)
        if resolution.status == "ERROR":
            raise ValueError("EVIDENCE_CANDIDATE_INVALID")
        entries.append({"month": month, "part": part, "evidence_ref": ref, "bundle": bundle,
                        "verification_history": history, "candidate_resolution": resolution.as_dict()})
    evidence = {"profile": EVIDENCE_PROFILE, "candidate_id": candidate["candidate_id"], "entries": entries}
    return prepare_snapshot(candidate, catalog, evidence, validation, rollback_target=rollback_target, profile=EARTHQUAKES)
