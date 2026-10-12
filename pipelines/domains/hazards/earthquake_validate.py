"""Validate a closed USGS ComCat earthquake WORK candidate without authorizing promotion."""
from datetime import datetime
from pathlib import Path
import json

from jsonschema import Draft202012Validator, FormatChecker
from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.usgs.src.usgs.earthquake_capture import BOUNDS, SOURCE_ID, data_year
from pipelines.domains.hazards.earthquake_normalize import (
    CANDIDATE_PROFILE, DIGEST, MAX_EVENTS, WITHHELD, expected_flags, identity, number, year_state,
)

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/domains/hazards/earthquake_record.schema.json"
CANDIDATE_KEYS = {
    "profile", "capture_id", "source_id", "data_year", "bounds", "retrieved_at", "months", "observations",
    "latest_event_date", "withheld_counts", "year_state", "coverage", "review_state", "source_admission",
    "release_state", "candidate_id",
}


def validate_candidate(candidate: dict) -> dict:
    if not isinstance(candidate, dict) or set(candidate) != CANDIDATE_KEYS:
        raise ValueError("CANDIDATE_SHAPE_INVALID")
    if len(canonical_bytes(candidate)) > 32 * 1024 * 1024:
        raise ValueError("CANDIDATE_BYTE_LIMIT")
    if (candidate["profile"] != CANDIDATE_PROFILE or candidate["source_id"] != SOURCE_ID
            or candidate["bounds"] != BOUNDS or not DIGEST.fullmatch(str(candidate["capture_id"]))
            or candidate["source_admission"] != "PENDING" or candidate["review_state"] != "PENDING"
            or candidate["release_state"] != "UNRELEASED" or candidate["coverage"] != "NOT_ESTABLISHED"):
        raise ValueError("CANDIDATE_AUTHORITY_OR_PROFILE_INVALID")
    expected = digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "candidate_id"}))
    if expected != candidate["candidate_id"]:
        raise ValueError("CANDIDATE_DIGEST_MISMATCH")
    try:
        year = data_year(candidate["data_year"])
        retrieved = datetime.fromisoformat(str(candidate["retrieved_at"]).replace("Z", "+00:00"))
    except ValueError:
        raise ValueError("CANDIDATE_TIME_INVALID") from None
    if retrieved.year < year or candidate["year_state"] != year_state(year, candidate["retrieved_at"]):
        raise ValueError("CANDIDATE_TIME_INVALID")
    counts = candidate["withheld_counts"]
    if (not isinstance(counts, dict) or set(counts) != set(WITHHELD)
            or any(type(n) is not int or n < 0 for n in counts.values())):
        raise ValueError("WITHHELD_COUNTS_INVALID")
    validator = Draft202012Validator(json.loads(SCHEMA.read_text()), format_checker=FormatChecker())
    observations = candidate["observations"]
    if not isinstance(observations, list) or len(observations) > MAX_EVENTS:
        raise ValueError("OBSERVATION_COUNT_INVALID")
    previous, aliases, per_month = None, set(), [0] * 12
    for record in observations:
        if not validator.is_valid(record):
            raise ValueError("EARTHQUAKE_SCHEMA_INVALID")
        if digest_bytes(canonical_bytes({k: v for k, v in record.items() if k != "record_digest"})) != record["record_digest"]:
            raise ValueError("RECORD_DIGEST_MISMATCH")
        key = identity(record["event_id"])
        if record["id"] != "kfm:quake:" + key or record["evidence_ref"] != "kfm:evidence:quake:" + key:
            raise ValueError("RECORD_IDENTITY_MISMATCH")
        # The preferred id leads its aliases, and no alias names two records.
        if record["aliases"][0] != record["event_id"] or aliases.intersection(record["aliases"]):
            raise ValueError("RECORD_ORDER_OR_DUPLICATE")
        aliases.update(record["aliases"])
        order = (record["origin_utc"], record["event_id"])
        if previous is not None and order <= previous:
            raise ValueError("RECORD_ORDER_OR_DUPLICATE")
        previous = order
        try:
            origin = datetime.fromisoformat(record["origin_utc"].replace("Z", "+00:00"))
            if record["updated_utc"] is not None:
                datetime.fromisoformat(record["updated_utc"].replace("Z", "+00:00"))
        except ValueError:
            raise ValueError("RECORD_TIME_INVALID") from None
        if origin.year != year or record["retrieved_at"] > candidate["retrieved_at"]:
            raise ValueError("RECORD_TIME_INVALID")
        per_month[origin.month - 1] += 1
        if any(number(record[field]) != record[field] or type(number(record[field])) is not type(record[field])
               for field in ("longitude", "latitude", "depth_km", "magnitude")):
            raise ValueError("RECORD_NUMBER_NOT_CANONICAL")
        if record["review_status"] == "deleted":
            raise ValueError("RECORD_STATUS_WITHHELD")
        if record["flags"] != expected_flags(record):
            raise ValueError("RECORD_FLAGS_MISMATCH")
    months = candidate["months"]
    if (not isinstance(months, list) or len(months) != 12
            or any(not isinstance(m, dict) or set(m) != {"month", "query_status", "events"} or m["month"] != i + 1
                   or m["query_status"] not in (200, 204) or m["events"] != per_month[i]
                   or (m["query_status"] == 204 and m["events"])
                   for i, m in enumerate(months))):
        raise ValueError("MONTH_SUMMARY_MISMATCH")
    if candidate["latest_event_date"] != max((r["origin_utc"][:10] for r in observations), default=None):
        raise ValueError("LATEST_EVENT_DATE_MISMATCH")
    report = {"profile": "kfm.earthquake-validation/v1", "candidate_id": expected, "outcome": "PASS",
              "observations": len(observations), "withheld": sum(counts.values()),
              "review_required": True, "promotion_authorized": False,
              "release_authorized": False, "publication_authorized": False}
    report["receipt_digest"] = digest_bytes(canonical_bytes(report))
    return report
