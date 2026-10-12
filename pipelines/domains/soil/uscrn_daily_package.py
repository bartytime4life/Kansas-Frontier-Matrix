"""Compose a USCRN daily soil review carrier from a validated WORK candidate.

Mirrors pipelines/domains/atmosphere/ghcnd_daily_package.py with the SOIL
snapshot profile, which splits each station's evidence into one bundle per
sensor depth: a station-depth holds 30 days of moisture and temperature (60
values), inside the resolver's 128-member bundle limit. Preparation grants no
lifecycle transition: without ``admission`` every bundle carries the
rights/sensitivity hold, and release still needs a trusted
kfm.soil-release-decision/v1 record that passes the serving gate.
"""
from datetime import timezone

from connectors_core.captured_json import canonical_bytes, digest_bytes, utc_time
from evidence_resolver.core import PROFILE, evaluate_resolution_candidate
from evidence_resolver.verification_history import canonical_spec_hash
from hashing import compute_spec_hash
from release.core import SOIL, prepare_snapshot
from connectors.noaa.src.noaa import uscrn_daily
from pipelines.domains.soil.uscrn_daily_normalize import UNITS
from pipelines.domains.soil.uscrn_daily_validate import validate_candidate

EVIDENCE_PROFILE = "kfm.soil-evidence-candidate/v1"
CATALOG_PROFILE = "kfm.soil-catalog-candidate/v1"


def dataset_ref(station_id: str, depth_cm: int, candidate_id: str) -> str:
    return SOIL.entry_ref(station_id, depth_cm, candidate_id)


def soil_catalog(candidate: dict, validation: dict) -> dict:
    """Discovery projection for already validated records; candidate metadata only."""
    if (validation.get("candidate_id") != candidate.get("candidate_id")
            or validation.get("outcome") != "PASS"
            or validation.get("receipt_digest") != digest_bytes(canonical_bytes({k: v for k, v in validation.items() if k != "receipt_digest"}))):
        raise ValueError("CATALOG_VALIDATION_REQUIRED")
    entries = []
    for station in candidate["stations"]:
        records = [r for r in candidate["observations"] if r["station_id"] == station["id"]]
        entries.append({"id": station["id"], "title": station["name"], "geometry": station["geometry"],
                        "source_id": candidate["source_id"], "variables": UNITS, "depths_cm": list(uscrn_daily.DEPTHS_CM),
                        "observation_count": len(records),
                        "withheld_count": sum(r["withheld"] is not None for r in records),
                        "interval": {"start": candidate["start"], "end": candidate["end"], "basis": "station local-standard-time days"},
                        "freshness_at_capture": candidate["freshness_at_capture"][station["id"]],
                        "evidence_refs": [dataset_ref(station["id"], depth, candidate["candidate_id"]) for depth in uscrn_daily.DEPTHS_CM],
                        "validation_ref": validation["receipt_digest"]})
    return {"profile": CATALOG_PROFILE, "candidate_id": candidate["candidate_id"],
            "entries": entries, "authoritative": False, "release_state": "UNRELEASED"}


def prepare_soil_package(candidate: dict, *, rollback_target=None, admission: dict | None = None) -> dict:
    """``admission`` comes from uscrn_daily_admission.load_admission(); it releases nothing."""
    validation = validate_candidate(candidate)
    catalog = soil_catalog(candidate, validation)
    verified_at = utc_time(candidate["retrieved_at"]).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stations = {station["id"]: station for station in candidate["stations"]}
    entries = []
    for station_id, depth in SOIL.evidence_keys():
        station = stations[station_id]
        records = SOIL.entry_records(candidate["observations"], station_id, depth)
        if len(records) > 127:
            raise ValueError("PILOT_BUNDLE_MEMBER_LIMIT")
        bundle_id = "soil:" + station_id + ":" + str(depth) + "cm:" + candidate["candidate_id"].split(":")[1]
        ref = {"ref": dataset_ref(station_id, depth, candidate["candidate_id"]), "kind": "dataset", "bundle_ref": bundle_id}
        bundle = {"bundle_id": bundle_id,
                  "claim_scope": ("Preserved NOAA USCRN daily soil moisture and soil temperature at " + str(depth)
                                  + " cm for WBAN " + station_id + " " + station["name"] + " (" + candidate["start"]
                                  + " to " + candidate["end"] + ", local-standard-time days); "
                                  "station point only; values subject to revision; review candidate only."),
                  "evidence_refs": [ref] + [{"ref": r["evidence_ref"], "kind": "measurement", "bundle_ref": bundle_id} for r in records],
                  "source_records": sorted({station["page_digest"], *[r["page_digest"] for r in records]}),
                  "citations": [uscrn_daily.BASE, "doi:10.1175/BAMS-D-12-00170.1"],
                  "rights": {"license": admission["license"] if admission else "NOAA NCEI source terms; independent rights review required"},
                  "sensitivity": ({"level": "public", "reason": "Admitted public source " + admission["source_ref"], "applied_at": verified_at}
                                  if admission else
                                  {"level": "quarantine", "reason": "Candidate pending source, rights and sensitivity review", "applied_at": verified_at}),
                  "transforms": ["kfm:transform:uscrn-daily-pilot:v1"],
                  "checksums": {"candidate": candidate["candidate_id"], "validation": validation["receipt_digest"]}}
        bundle["spec_hash"] = {"value": compute_spec_hash(bundle)}
        history = {"schema_version": "1.0.0", "history_id": "kfm:verification-history:soil:" + station_id + ":" + str(depth) + "cm",
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
        entries.append({"station_id": station_id, "series": depth, "evidence_ref": ref, "bundle": bundle,
                        "verification_history": history, "candidate_resolution": resolution.as_dict()})
    evidence = {"profile": EVIDENCE_PROFILE, "candidate_id": candidate["candidate_id"], "entries": entries}
    return prepare_snapshot(candidate, catalog, evidence, validation, rollback_target=rollback_target, profile=SOIL)
