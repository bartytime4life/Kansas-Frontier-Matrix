"""Validate a closed GHCN-Daily WORK candidate without authorizing promotion."""
from datetime import date
from pathlib import Path
import json
import math

from jsonschema import Draft202012Validator, FormatChecker
from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.noaa.src.noaa.ghcnd_daily_capture import ELEMENTS, SOURCE_ID, STALE_AFTER_DAYS, STATIONS, WINDOW_DAYS, window
from pipelines.domains.atmosphere.ghcnd_daily_normalize import (
    CANDIDATE_PROFILE, DIGEST, LAT, LON, _reading, coverage, freshness, withheld_counts,
)

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/domains/atmosphere/daily_weather_observation.schema.json"
CANDIDATE_KEYS = {
    "profile", "capture_id", "source_id", "start", "end", "retrieved_at", "stations", "observations",
    "freshness_at_capture", "stale_after_days", "coverage", "withheld_counts", "review_state",
    "source_admission", "release_state", "candidate_id",
}
STATION_KEYS = {"id", "name", "geometry", "elevation_m", "page_digest", "retrieved_at"}
MAX_OBSERVATIONS = len(STATIONS) * len(ELEMENTS) * WINDOW_DAYS


def validate_candidate(candidate: dict) -> dict:
    if not isinstance(candidate, dict) or set(candidate) != CANDIDATE_KEYS:
        raise ValueError("CANDIDATE_SHAPE_INVALID")
    if len(canonical_bytes(candidate)) > 8 * 1024 * 1024:
        raise ValueError("CANDIDATE_BYTE_LIMIT")
    if (candidate["profile"] != CANDIDATE_PROFILE or candidate["source_id"] != SOURCE_ID
            or candidate["source_admission"] != "PENDING" or candidate["review_state"] != "PENDING"
            or candidate["release_state"] != "UNRELEASED" or candidate["stale_after_days"] != STALE_AFTER_DAYS):
        raise ValueError("CANDIDATE_AUTHORITY_OR_PROFILE_INVALID")
    expected = digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "candidate_id"}))
    if expected != candidate["candidate_id"]:
        raise ValueError("CANDIDATE_DIGEST_MISMATCH")
    if window(candidate["end"]) != (candidate["start"], candidate["end"]) or str(candidate["retrieved_at"])[:10] < candidate["end"]:
        raise ValueError("CANDIDATE_INTERVAL_INVALID")
    stations = candidate["stations"]
    if not isinstance(stations, list) or [s.get("id") if isinstance(s, dict) else None for s in stations] != list(STATIONS):
        raise ValueError("STATION_SCOPE_INVALID")
    for station in stations:
        xy = station.get("geometry", {}).get("coordinates") if isinstance(station.get("geometry"), dict) else None
        if (set(station) != STATION_KEYS or station["geometry"] != {"type": "Point", "coordinates": xy}
                or not isinstance(xy, list) or len(xy) != 2
                or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in xy)
                or not (LON[0] <= xy[0] <= LON[1] and LAT[0] <= xy[1] <= LAT[1])
                or not isinstance(station["name"], str) or not 0 < len(station["name"]) <= 64
                or not DIGEST.fullmatch(str(station["page_digest"])) or station["retrieved_at"] > candidate["retrieved_at"]):
            raise ValueError("STATION_SHAPE_INVALID")
    validator = Draft202012Validator(json.loads(SCHEMA.read_text()), format_checker=FormatChecker())
    observations = candidate["observations"]
    if not isinstance(observations, list) or len(observations) > MAX_OBSERVATIONS:
        raise ValueError("OBSERVATION_COUNT_INVALID")
    start, end = date.fromisoformat(candidate["start"]), date.fromisoformat(candidate["end"])
    seen = set()
    for record in observations:
        if not validator.is_valid(record):
            raise ValueError("WEATHER_OBSERVATION_SCHEMA_INVALID")
        if digest_bytes(canonical_bytes({k: v for k, v in record.items() if k != "record_digest"})) != record["record_digest"]:
            raise ValueError("OBSERVATION_DIGEST_MISMATCH")
        identity = digest_bytes(canonical_bytes([record["station_id"], record["element"], record["observation_date"]])).split(":")[1]
        if record["id"] != "kfm:weather:" + identity or record["evidence_ref"] != "kfm:evidence:weather:" + identity:
            raise ValueError("OBSERVATION_IDENTITY_MISMATCH")
        try:
            day = date.fromisoformat(record["observation_date"])
        except ValueError:
            raise ValueError("OBSERVATION_DATE_INVALID") from None
        if not start <= day <= end or record["retrieved_at"] > candidate["retrieved_at"]:
            raise ValueError("OBSERVATION_DATE_INVALID")
        if (record["value"], record["trace"], record["withheld"]) != _reading(record["raw_value"], record["measurement_flag"], record["quality_flag"]):
            raise ValueError("OBSERVATION_VALUE_MISMATCH")
        key = (record["station_id"], record["element"], record["observation_date"])
        if key in seen:
            raise ValueError("DUPLICATE_STATION_DAY_ELEMENT")
        seen.add(key)
    if observations != sorted(observations, key=lambda r: (r["station_id"], r["observation_date"], r["element"])):
        raise ValueError("OBSERVATION_ORDER_INVALID")
    states = freshness(observations, candidate["end"])
    if (candidate["freshness_at_capture"] != states or candidate["coverage"] != coverage(states)
            or candidate["withheld_counts"] != withheld_counts(observations)):
        raise ValueError("COVERAGE_OR_FRESHNESS_MISMATCH")
    report = {"profile": "kfm.ghcnd-daily-validation/v1", "candidate_id": expected, "outcome": "PASS",
              "observations": len(observations), "withheld": sum(1 for r in observations if r["withheld"]),
              "review_required": True, "promotion_authorized": False,
              "release_authorized": False, "publication_authorized": False}
    report["receipt_digest"] = digest_bytes(canonical_bytes(report))
    return report
