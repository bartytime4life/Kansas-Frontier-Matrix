"""Deterministic discovery projection for the bounded water pilot.

This pure producer accepts already validated records. Its result is candidate
metadata; only a lifecycle-aware caller may place it in the catalog lane.
"""
from connectors_core.captured_json import canonical_bytes, digest_bytes


def water_catalog(candidate: dict, validation: dict) -> dict:
    if (validation.get("candidate_id") != candidate.get("candidate_id")
            or validation.get("outcome") != "PASS"
            or validation.get("receipt_digest") != digest_bytes(canonical_bytes({k: v for k, v in validation.items() if k != "receipt_digest"}))):
        raise ValueError("CATALOG_VALIDATION_REQUIRED")
    entries = []
    for station in candidate["stations"]:
        records = [r for r in candidate["observations"] if r["station_id"] == station["id"]]
        entries.append({"id": station["id"], "title": station["name"], "geometry": station["geometry"],
                        "source_id": candidate["source_id"], "parameter_code": "00060", "unit": "ft^3/s",
                        "observation_count": len(records), "missing_value_count": sum(r["value"] is None for r in records),
                        "interval": {"start": candidate["start"], "end": candidate["end"]},
                        "evidence_ref": "kfm://water/station/" + station["id"] + "/" + candidate["candidate_id"].split(":")[1],
                        "validation_ref": validation["receipt_digest"]})
    return {"profile": "kfm.water-catalog-candidate/v1", "candidate_id": candidate["candidate_id"],
            "entries": entries, "authoritative": False, "release_state": "UNRELEASED"}
