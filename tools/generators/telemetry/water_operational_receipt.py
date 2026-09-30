"""Safe local operational events using the existing run and source-health contracts."""
from datetime import timedelta
from pathlib import Path

from connectors_core.captured_json import canonical_bytes, digest_bytes, timestamp, utc_time
from hashing import compute_spec_hash

ROOT = Path(__file__).resolve().parents[3]
BUILD_FILES = ("connectors/usgs/water_data/pilot_capture.py", "pipelines/domains/hydrology/normalize.py", "pipelines/domains/hydrology/validate.py", "tools/local_data/water_pilot.py")


def build_identity():
    return digest_bytes(canonical_bytes({name: digest_bytes((ROOT/name).read_bytes()) for name in BUILD_FILES}))


def operational_receipt(manifest: dict, candidate: dict | None, validation: dict | None) -> dict:
    run = manifest["capture_id"].split(":")[1]
    receipt = {"run_id": "water:" + run, "stage": "water_candidate_validation", "inputs": [manifest["capture_id"]],
               "outputs": [candidate["candidate_id"]] if candidate else [], "code_ref": build_identity(),
               "source_descriptor_refs": ["kfm://source/usgs-nwis"],
               "validation_refs": [validation["receipt_digest"]] if validation else [], "outcome": "SUCCESS" if candidate else "FAIL",
               "operational": {"component": "water-pilot", "correlation_id": run, "source_id": "usgs-nwis",
                               "occurred_at": manifest["captured_at"], "reason_code": "REVIEW_REQUIRED" if candidate else "CAPTURE_OR_NORMALIZATION_INVALID",
                               "source_admitted": False, "release_authorized": False}}
    receipt["spec_hash"] = compute_spec_hash(receipt)
    return receipt


def source_health(manifest: dict, candidate: dict | None, *, station_id: str) -> dict:
    probed = manifest["captured_at"]
    records = [] if candidate is None else [r for r in candidate["observations"] if r["station_id"] == station_id and r["value"] is not None]
    latest = max((utc_time(r["observed_at"]) for r in records), default=None)
    deadline = latest + timedelta(seconds=candidate["stale_after_seconds"] if candidate else 7200) if latest else None
    if candidate is None:
        result, outcome, reasons = "PARSE_ERROR", "UNAVAILABLE", ["RETRIEVAL_FAILED", "SCHEMA_OR_PARSE_FAILURE", "NO_PRIOR_SUCCESS"]
    elif latest is None:
        result, outcome, reasons = "EMPTY", "DEGRADED", ["EMPTY_NOT_CLEAR"]
    elif utc_time(probed) > deadline:
        result, outcome, reasons = "SUCCESS", "STALE", ["FRESHNESS_EXPIRED"]
    else:
        result, outcome, reasons = "SUCCESS", "HEALTHY", ["WITHIN_FRESHNESS"]
    return {"assessment_id": "kfm:source-health:water:" + station_id.lower() + ":" + manifest["capture_id"].split(":")[1],
            "source_id": "usgs-nwis:" + station_id, "probed_at": probed,
            "last_success_at": probed if candidate else None, "freshness_deadline": timestamp(deadline) if deadline else None,
            "result_class": result, "health_outcome": outcome, "material_change": False, "reasons": reasons}
