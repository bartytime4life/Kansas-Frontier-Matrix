"""Safe local operational events using the existing run and source-health contracts."""
from datetime import timedelta
from pathlib import Path

from connectors_core.captured_json import canonical_bytes, digest_bytes, timestamp, utc_time
from hashing import compute_spec_hash

ROOT = Path(__file__).resolve().parents[3]
BUILD_FILES = ("connectors/usgs/water_data/pilot_capture.py", "pipelines/domains/hydrology/normalize.py", "pipelines/domains/hydrology/validate.py", "tools/local_data/water_pilot.py", "tools/generators/telemetry/water_operational_receipt.py")


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


def _station_attempts(manifest: dict, station_id: str) -> list[dict]:
    attempts = manifest.get("attempts")
    return ([item for item in attempts
             if isinstance(item, dict) and item.get("station_id") == station_id]
            if isinstance(attempts, list) else [])


def _last_success(scoped: list[dict], probed_at: str) -> str | None:
    limit = utc_time(probed_at)
    observed = []
    for item in scoped:
        if (item.get("outcome") != "SUCCESS" or item.get("code") != "FETCH_SUCCESS"
                or item.get("status") != 200 or not isinstance(item.get("observed_at"), str)):
            continue
        try:
            when = utc_time(item["observed_at"])
        except ValueError:
            continue
        if when <= limit:
            observed.append(when)
    return timestamp(max(observed)) if observed else None


def _failed_probe(manifest: dict, station_id: str) -> tuple[str, str, list[str], str | None]:
    scoped = _station_attempts(manifest, station_id)
    last_success = _last_success(scoped, manifest["captured_at"])
    if manifest.get("complete") is True:
        reasons = ["RETRIEVAL_FAILED", "SCHEMA_OR_PARSE_FAILURE"]
        if last_success is None:
            reasons.append("NO_PRIOR_SUCCESS")
        return "PARSE_ERROR", "UNAVAILABLE", reasons, last_success
    if not scoped:
        return "NOT_PROBED", "UNKNOWN", ["NOT_PROBED", "NO_PRIOR_SUCCESS", "CAPTURE_INCOMPLETE"], None
    last = scoped[-1]
    if last.get("outcome") == "RETRY_EXHAUSTED" and last.get("code") == "RETRY_DEADLINE_REACHED":
        terminal = "TIMEOUT"
    else:
        terminal = next((item.get("outcome") for item in reversed(scoped)
                         if item.get("outcome") != "RETRY_EXHAUSTED"), None)
    if terminal == "SUCCESS":
        if last_success is not None:
            return "SUCCESS", "UNKNOWN", ["CAPTURE_INCOMPLETE"], last_success
        return "ACQUISITION_ERROR", "UNAVAILABLE", ["RETRIEVAL_FAILED", "NO_PRIOR_SUCCESS"], None
    reasons = ["RETRIEVAL_FAILED"] + (["NO_PRIOR_SUCCESS"] if last_success is None else [])
    if terminal == "TIMEOUT":
        return "TIMEOUT", "UNAVAILABLE", reasons, last_success
    if terminal in {"AUTH_REQUIRED", "ACCESS_DENIED"}:
        return "AUTH_ERROR", "UNAVAILABLE", reasons + ["AUTH_FAILURE"], last_success
    if terminal in {"RATE_LIMITED", "NOT_FOUND"}:
        return "HTTP_ERROR", "UNAVAILABLE", reasons, last_success
    return "ACQUISITION_ERROR", "UNAVAILABLE", reasons, last_success


def source_health(manifest: dict, candidate: dict | None, *, station_id: str) -> dict:
    probed = manifest["captured_at"]
    records = [] if candidate is None else [r for r in candidate["observations"] if r["station_id"] == station_id and r["value"] is not None]
    latest = max((utc_time(r["observed_at"]) for r in records), default=None)
    deadline = latest + timedelta(seconds=candidate["stale_after_seconds"] if candidate else 7200) if latest else None
    if candidate is None:
        result, outcome, reasons, last_success = _failed_probe(manifest, station_id)
    else:
        last_success = _last_success(_station_attempts(manifest, station_id), probed)
        if latest is None:
            result, outcome, reasons = "EMPTY", "DEGRADED", ["EMPTY_NOT_CLEAR"]
        elif utc_time(probed) > deadline:
            result, outcome, reasons = "SUCCESS", "STALE", ["FRESHNESS_EXPIRED"]
        else:
            result, outcome, reasons = "SUCCESS", "HEALTHY", ["WITHIN_FRESHNESS"]
    return {"assessment_id": "kfm:source-health:water:" + station_id.lower() + ":" + manifest["capture_id"].split(":")[1],
            "source_id": "usgs-nwis:" + station_id, "probed_at": probed,
            "last_success_at": last_success, "freshness_deadline": timestamp(deadline) if deadline else None,
            "result_class": result, "health_outcome": outcome, "material_change": False, "reasons": reasons}
