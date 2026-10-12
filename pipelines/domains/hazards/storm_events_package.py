"""Compose a NOAA Storm Events review carrier from a validated WORK candidate.

Mirrors pipelines/domains/soil/uscrn_daily_package.py with the STORM_EVENTS
snapshot profile. It has no stations: evidence is one bundle per month that has
events (by the event's local begin month), split into numbered parts of 127
records so every bundle stays inside the resolver's 128-member limit. Records
are ``record`` members, not measurements. Preparation grants no lifecycle
transition: without ``admission`` every bundle carries the rights/sensitivity
hold, and release still needs a trusted kfm.storm-events-release-decision/v1
record that passes the serving gate.
"""
from collections import Counter
from datetime import timezone

from connectors_core.captured_json import canonical_bytes, digest_bytes, utc_time
from evidence_resolver.core import PROFILE, evaluate_resolution_candidate
from evidence_resolver.verification_history import canonical_spec_hash
from hashing import compute_spec_hash
from release.core import STORM_EVENTS, prepare_snapshot
from connectors.noaa.src.noaa import storm_events
from pipelines.domains.hazards.storm_events_validate import validate_candidate

EVIDENCE_PROFILE = "kfm.storm-events-evidence-candidate/v1"
CATALOG_PROFILE = "kfm.storm-events-catalog-candidate/v1"
DATABASE_URL = "https://www.ncdc.noaa.gov/stormevents/"


def storm_catalog(candidate: dict, validation: dict, start: str) -> dict:
    """Discovery projection for already validated records; candidate metadata only."""
    if (validation.get("candidate_id") != candidate.get("candidate_id")
            or validation.get("outcome") != "PASS"
            or validation.get("receipt_digest") != digest_bytes(canonical_bytes({k: v for k, v in validation.items() if k != "receipt_digest"}))):
        raise ValueError("CATALOG_VALIDATION_REQUIRED")
    observations = candidate["observations"]
    months = [{"month": month, "part": part, "observation_count": len(records),
               "evidence_ref": STORM_EVENTS.month_ref(start, month, part, candidate["candidate_id"])}
              for month, part, records in STORM_EVENTS.month_groups(observations)]
    dataset = {"id": "noaa-storm-events:ks:" + str(candidate["data_year"]),
               "title": "NOAA Storm Events, Kansas, " + str(candidate["data_year"]),
               "source_id": candidate["source_id"], "state_fips": candidate["state_fips"],
               "data_year": candidate["data_year"], "source_file": candidate["source_file"],
               "vintage_created": candidate["vintage_created"],
               "observation_count": len(observations), "withheld_rows": candidate["withheld_rows"],
               "withheld_counts": candidate["withheld_counts"],
               "event_types": dict(sorted(Counter(r["event_type"] for r in observations).items())),
               "latest_event_date": candidate["latest_event_date"],
               "freshness_at_capture": candidate["freshness_at_capture"], "coverage": candidate["coverage"],
               "interval": {"start": start, "end": start[:4] + "-12-31", "basis": "event begin, local time"},
               "narratives": "excluded", "validation_ref": validation["receipt_digest"]}
    return {"profile": CATALOG_PROFILE, "candidate_id": candidate["candidate_id"], "dataset": dataset,
            "entries": months, "authoritative": False, "release_state": "UNRELEASED"}


def prepare_storm_events_package(candidate: dict, *, rollback_target=None, admission: dict | None = None) -> dict:
    """``admission`` comes from storm_events_admission.load_admission(); it releases nothing."""
    validation = validate_candidate(candidate)
    start, _ = STORM_EVENTS.candidate_window(candidate)
    groups = STORM_EVENTS.month_groups(candidate["observations"])
    if not groups:
        raise ValueError("NO_EVENTS_TO_PACKAGE")
    catalog = storm_catalog(candidate, validation, start)
    verified_at = utc_time(candidate["retrieved_at"]).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    short = candidate["candidate_id"].split(":")[1]
    source_url = storm_events.HOST + storm_events.DIRECTORY + candidate["source_file"]
    entries = []
    for month, part, records in groups:
        label = f"{start[:4]}-{month:02d}"
        parts = sum(1 for m, _, _ in groups if m == month)
        bundle_id = f"storm-events:{label}:part-{part}:{short}"
        ref = {"ref": STORM_EVENTS.month_ref(start, month, part, candidate["candidate_id"]), "kind": "dataset", "bundle_ref": bundle_id}
        bundle = {"bundle_id": bundle_id,
                  "claim_scope": ("Preserved NOAA NCEI Storm Events details-file rows for Kansas (STATE_FIPS 20), events "
                                  "beginning in " + label + " (local time), part " + str(part) + " of " + str(parts)
                                  + ", from " + candidate["source_file"] + "; National Weather Service event reports, "
                                  "not measurements, footprints or warnings; narratives excluded; records subject to "
                                  "revision; review candidate only."),
                  "evidence_refs": [ref] + [{"ref": r["evidence_ref"], "kind": STORM_EVENTS.member_kind, "bundle_ref": bundle_id}
                                            for r in records],
                  "source_records": sorted({r["page_digest"] for r in records}),
                  "citations": [source_url, DATABASE_URL],
                  "rights": {"license": admission["license"] if admission else "NOAA NCEI source terms; independent rights review required"},
                  "sensitivity": ({"level": "public", "reason": "Admitted public source " + admission["source_ref"], "applied_at": verified_at}
                                  if admission else
                                  {"level": "quarantine", "reason": "Candidate pending source, rights and sensitivity review", "applied_at": verified_at}),
                  "transforms": ["kfm:transform:storm-events-pilot:v1"],
                  "checksums": {"candidate": candidate["candidate_id"], "validation": validation["receipt_digest"]}}
        bundle["spec_hash"] = {"value": compute_spec_hash(bundle)}
        history = {"schema_version": "1.0.0", "history_id": f"kfm:verification-history:storm-events:{label}:part-{part}",
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
    return prepare_snapshot(candidate, catalog, evidence, validation, rollback_target=rollback_target, profile=STORM_EVENTS)
