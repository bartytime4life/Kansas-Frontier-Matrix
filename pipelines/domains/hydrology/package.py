"""Compose a water review carrier from a validated WORK candidate.

Preparation grants no lifecycle transition. Rights and sensitivity statements
are proposed review inputs; trusted release metadata must independently clear
all required gates before a serving projection can answer.
"""
from datetime import timezone

from catalog.core import water_catalog
from connectors_core.captured_json import utc_time
from evidence_resolver.core import PROFILE, evaluate_resolution_candidate
from evidence_resolver.verification_history import canonical_spec_hash
from hashing import compute_spec_hash
from release.core import prepare_snapshot
from pipelines.domains.hydrology.validate import validate_candidate


def prepare_water_package(candidate: dict, *, rollback_target=None) -> dict:
    validation = validate_candidate(candidate)
    catalog = water_catalog(candidate, validation)
    entries = []
    verified_at = utc_time(candidate["retrieved_at"]).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for station in candidate["stations"]:
        records = [r for r in candidate["observations"] if r["station_id"] == station["id"]]
        if len(records) > 127:
            raise ValueError("PILOT_BUNDLE_MEMBER_LIMIT")
        record = next(e for e in catalog["entries"] if e["id"] == station["id"])
        bundle_id = "water:" + station["id"].lower() + ":" + candidate["candidate_id"].split(":")[1]
        ref = {"ref": record["evidence_ref"], "kind": "dataset", "bundle_ref": bundle_id}
        bundle = {"bundle_id": bundle_id,
                  "claim_scope": "Preserved USGS discharge records for " + station["id"] + "; provisional data subject to revision; review candidate only.",
                  "evidence_refs": [ref] + [{"ref": r["evidence_ref"], "kind": "measurement", "bundle_ref": bundle_id} for r in records],
                  "source_records": sorted({station["page_digest"], *[r["page_digest"] for r in records]}),
                  "citations": ["https://waterdata.usgs.gov/monitoring-location/" + station["id"] + "/"],
                  "rights": {"license": "USGS source terms; independent rights review required"},
                  "sensitivity": {"level": "quarantine", "reason": "Candidate pending source, rights and sensitivity review", "applied_at": verified_at},
                  "transforms": ["kfm:transform:usgs-water-pilot:v1"],
                  "checksums": {"candidate": candidate["candidate_id"], "validation": validation["receipt_digest"]}}
        bundle["spec_hash"] = {"value": compute_spec_hash(bundle)}
        history = {"schema_version": "1.0.0", "history_id": "kfm:verification-history:water:" + station["id"].lower(),
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
        entries.append({"station_id": station["id"], "evidence_ref": ref, "bundle": bundle,
                        "verification_history": history, "candidate_resolution": resolution.as_dict()})
    evidence = {"profile": "kfm.water-evidence-candidate/v1", "candidate_id": candidate["candidate_id"], "entries": entries}
    return prepare_snapshot(candidate, catalog, evidence, validation, rollback_target=rollback_target)
