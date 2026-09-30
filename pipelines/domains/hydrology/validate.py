"""Validate a closed water-pilot WORK candidate without authorizing promotion."""
from pathlib import Path
import json
import math
import re

from jsonschema import Draft202012Validator, FormatChecker
from connectors_core.captured_json import canonical_bytes, digest_bytes, utc_time
from connectors.usgs.water_data.pilot_capture import STATIONS, STALE_AFTER_SECONDS

ROOT = Path(__file__).resolve().parents[3]
CANDIDATE_KEYS = {
    "profile", "capture_id", "source_id", "start", "end", "retrieved_at",
    "stations", "observations", "revision_history", "freshness_at_capture",
    "stale_after_seconds", "coverage", "review_state", "source_admission",
    "release_state", "candidate_id",
}


def validate_candidate(candidate: dict) -> dict:
    if not isinstance(candidate, dict) or set(candidate) != CANDIDATE_KEYS:
        raise ValueError("CANDIDATE_SHAPE_INVALID")
    if len(canonical_bytes(candidate)) > 8 * 1024 * 1024:
        raise ValueError("CANDIDATE_BYTE_LIMIT")
    if (candidate["profile"] != "kfm.usgs-water-candidate/v1" or candidate["source_id"] != "usgs-nwis"
            or candidate["source_admission"] != "PENDING" or candidate["review_state"] != "PENDING"
            or candidate["release_state"] != "UNRELEASED" or candidate["stale_after_seconds"] != STALE_AFTER_SECONDS):
        raise ValueError("CANDIDATE_AUTHORITY_OR_PROFILE_INVALID")
    expected = digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "candidate_id"}))
    if expected != candidate["candidate_id"]:
        raise ValueError("CANDIDATE_DIGEST_MISMATCH")
    start, end, retrieved = [utc_time(candidate[k]) for k in ("start", "end", "retrieved_at")]
    if not 0 < (end - start).total_seconds() <= 86400:
        raise ValueError("CANDIDATE_INTERVAL_INVALID")
    if not isinstance(candidate["stations"], list) or len(candidate["stations"]) != 2:
        raise ValueError("STATIONS_REQUIRED")
    if {s["id"] for s in candidate["stations"]} != set(STATIONS):
        raise ValueError("STATION_SCOPE_INVALID")
    for station in candidate["stations"]:
        if set(station) != {"id", "name", "geometry", "page_digest", "retrieved_at",
                            "horizontal_accuracy", "original_horizontal_datum", "provider_revision_at"}:
            raise ValueError("STATION_SHAPE_INVALID")
        if (not isinstance(station["name"], str) or not 0 < len(station["name"]) <= 256
                or not re.fullmatch(r"sha256:[a-f0-9]{64}", station["page_digest"])
                or utc_time(station["retrieved_at"]) > retrieved):
            raise ValueError("STATION_PROVENANCE_INVALID")
        geometry = station["geometry"]
        if set(geometry) != {"type", "coordinates"} or geometry["type"] != "Point":
            raise ValueError("STATION_GEOMETRY_INVALID")
        xy = geometry["coordinates"]
        if (not isinstance(xy, list) or len(xy) != 2
                or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not -180 <= v <= 180 or not math.isfinite(v) for v in xy)
                or not -180 <= xy[0] <= 180 or not -90 <= xy[1] <= 90):
            raise ValueError("STATION_GEOMETRY_INVALID")
    schema = json.loads((ROOT / "schemas/contracts/v1/domains/hydrology/flow_observation.schema.json").read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    history = {}
    for field in ("revision_history", "observations"):
        values = candidate[field]
        if not isinstance(values, list) or len(values) > 4000:
            raise ValueError("OBSERVATION_COUNT_INVALID")
        for record in values:
            if not validator.is_valid(record):
                raise ValueError("FLOW_OBSERVATION_SCHEMA_INVALID")
            content = {k: v for k, v in record.items() if k != "record_digest"}
            if digest_bytes(canonical_bytes(content)) != record["record_digest"]:
                raise ValueError("OBSERVATION_DIGEST_MISMATCH")
            identity = digest_bytes(canonical_bytes([record["station_id"], record["time_series_id"], "00060", record["observed_at"]])).split(":")[1]
            if record["id"] != "kfm:flow:" + identity or record["evidence_ref"] != "kfm:evidence:flow:" + identity:
                raise ValueError("OBSERVATION_IDENTITY_MISMATCH")
            if (not start <= utc_time(record["observed_at"]) <= end
                    or not utc_time(record["observed_at"]) <= utc_time(record["provider_revision_at"]) <= utc_time(record["retrieved_at"]) <= retrieved):
                raise ValueError("OBSERVATION_TIME_MISMATCH")
            if record["provisional"] != (record["approval_status"] in {"P", "Provisional"}):
                raise ValueError("PROVISIONAL_STATUS_MISMATCH")
            if field == "revision_history":
                key = (record["id"], record["provider_revision_at"])
                if key in history:
                    raise ValueError("DUPLICATE_REVISION")
                history[key] = record
    latest = {}
    for record in sorted(history.values(), key=lambda r: (utc_time(r["provider_revision_at"]), r["record_digest"])):
        latest[record["id"]] = record
    if candidate["observations"] != sorted(latest.values(), key=lambda r: (r["station_id"], r["observed_at"], r["id"])):
        raise ValueError("LATEST_REVISION_MISMATCH")
    latest_times = {station: max((utc_time(r["observed_at"]) for r in candidate["observations"] if r["station_id"] == station), default=None) for station in STATIONS}
    freshness = {station: "EMPTY" if when is None else "STALE" if (retrieved - when).total_seconds() > STALE_AFTER_SECONDS else "RECENT" for station, when in latest_times.items()}
    coverage = "EMPTY" if not candidate["observations"] else "PARTIAL" if "EMPTY" in freshness.values() else "COMPLETE"
    if candidate["freshness_at_capture"] != freshness or candidate["coverage"] != coverage:
        raise ValueError("COVERAGE_OR_FRESHNESS_MISMATCH")
    report = {"profile": "kfm.water-pilot-validation/v1", "candidate_id": expected,
              "outcome": "PASS", "observations": len(candidate["observations"]),
              "review_required": True, "promotion_authorized": False,
              "release_authorized": False, "publication_authorized": False}
    report["receipt_digest"] = digest_bytes(canonical_bytes(report))
    return report
