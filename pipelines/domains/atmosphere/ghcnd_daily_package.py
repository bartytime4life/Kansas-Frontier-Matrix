"""Compose a GHCN-Daily weather review carrier from a validated WORK candidate.

Mirrors pipelines/domains/hydrology/package.py with the WEATHER snapshot
profile. Preparation grants no lifecycle transition: without ``admission``
every bundle carries the rights/sensitivity hold, and release still needs a
trusted kfm.weather-release-decision/v1 record that passes the serving gate.
"""
from datetime import timezone

from connectors_core.captured_json import canonical_bytes, digest_bytes, utc_time
from evidence_resolver.core import PROFILE, evaluate_resolution_candidate
from evidence_resolver.verification_history import canonical_spec_hash
from hashing import compute_spec_hash
from release.core import WEATHER, prepare_snapshot
from pipelines.domains.atmosphere.ghcnd_daily_validate import validate_candidate

EVIDENCE_PROFILE = "kfm.weather-evidence-candidate/v1"
CATALOG_PROFILE = "kfm.weather-catalog-candidate/v1"
ELEMENT_UNITS = {"PRCP": "mm", "TMAX": "degC", "TMIN": "degC"}


def dataset_ref(station_id: str, candidate_id: str) -> str:
    return WEATHER.evidence_prefix + station_id + "/" + candidate_id.split(":")[1]


def weather_catalog(candidate: dict, validation: dict) -> dict:
    """Discovery projection for already validated records; candidate metadata only."""
    if (validation.get("candidate_id") != candidate.get("candidate_id")
            or validation.get("outcome") != "PASS"
            or validation.get("receipt_digest") != digest_bytes(canonical_bytes({k: v for k, v in validation.items() if k != "receipt_digest"}))):
        raise ValueError("CATALOG_VALIDATION_REQUIRED")
    entries = []
    for station in candidate["stations"]:
        records = [r for r in candidate["observations"] if r["station_id"] == station["id"]]
        entries.append({"id": station["id"], "title": station["name"], "geometry": station["geometry"],
                        "source_id": candidate["source_id"], "elements": ELEMENT_UNITS,
                        "observation_count": len(records),
                        "withheld_count": sum(r["withheld"] is not None for r in records),
                        "interval": {"start": candidate["start"], "end": candidate["end"], "basis": "station-local observation days"},
                        "freshness_at_capture": candidate["freshness_at_capture"][station["id"]],
                        "evidence_ref": dataset_ref(station["id"], candidate["candidate_id"]),
                        "validation_ref": validation["receipt_digest"]})
    return {"profile": CATALOG_PROFILE, "candidate_id": candidate["candidate_id"],
            "entries": entries, "authoritative": False, "release_state": "UNRELEASED"}


def prepare_weather_package(candidate: dict, *, rollback_target=None, admission: dict | None = None) -> dict:
    """``admission`` comes from ghcnd_daily_admission.load_admission(); it releases nothing."""
    validation = validate_candidate(candidate)
    catalog = weather_catalog(candidate, validation)
    verified_at = utc_time(candidate["retrieved_at"]).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entries = []
    for station in candidate["stations"]:
        records = [r for r in candidate["observations"] if r["station_id"] == station["id"]]
        if len(records) > 127:
            raise ValueError("PILOT_BUNDLE_MEMBER_LIMIT")
        bundle_id = "weather:" + station["id"].lower() + ":" + candidate["candidate_id"].split(":")[1]
        ref = {"ref": dataset_ref(station["id"], candidate["candidate_id"]), "kind": "dataset", "bundle_ref": bundle_id}
        bundle = {"bundle_id": bundle_id,
                  "claim_scope": ("Preserved NOAA GHCN-Daily PRCP, TMAX and TMIN for " + station["id"]
                                  + " (" + candidate["start"] + " to " + candidate["end"] + ", station-local days); "
                                  "preliminary data subject to revision; review candidate only."),
                  "evidence_refs": [ref] + [{"ref": r["evidence_ref"], "kind": "measurement", "bundle_ref": bundle_id} for r in records],
                  "source_records": sorted({station["page_digest"], *[r["page_digest"] for r in records]}),
                  "citations": ["https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_station/" + station["id"] + ".csv.gz",
                                "doi:10.7289/V5D21VHZ"],
                  "rights": {"license": admission["license"] if admission else "NOAA NCEI source terms; independent rights review required"},
                  "sensitivity": ({"level": "public", "reason": "Admitted public source " + admission["source_ref"], "applied_at": verified_at}
                                  if admission else
                                  {"level": "quarantine", "reason": "Candidate pending source, rights and sensitivity review", "applied_at": verified_at}),
                  "transforms": ["kfm:transform:ghcnd-daily-pilot:v1"],
                  "checksums": {"candidate": candidate["candidate_id"], "validation": validation["receipt_digest"]}}
        bundle["spec_hash"] = {"value": compute_spec_hash(bundle)}
        history = {"schema_version": "1.0.0", "history_id": "kfm:verification-history:weather:" + station["id"].lower(),
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
    evidence = {"profile": EVIDENCE_PROFILE, "candidate_id": candidate["candidate_id"], "entries": entries}
    return prepare_snapshot(candidate, catalog, evidence, validation, rollback_target=rollback_target, profile=WEATHER)
