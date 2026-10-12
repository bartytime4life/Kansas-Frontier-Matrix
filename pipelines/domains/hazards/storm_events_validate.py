"""Validate a closed NOAA Storm Events WORK candidate without authorizing promotion."""
from datetime import datetime, timedelta
from pathlib import Path
import json

from jsonschema import Draft202012Validator, FormatChecker
from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.noaa.src.noaa import storm_events
from connectors.noaa.src.noaa.storm_events_capture import SOURCE_ID, STATE_FIPS, data_year
from pipelines.domains.hazards.storm_events_normalize import (
    CANDIDATE_PROFILE, DIGEST, MAX_EVENTS, STALE_AFTER_DAYS, WITHHELD, freshness, identity,
)

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/domains/hazards/storm_event_record.schema.json"
CANDIDATE_KEYS = {
    "profile", "capture_id", "source_id", "state_fips", "data_year", "source_file", "vintage_created",
    "retrieved_at", "observations", "latest_event_date", "withheld_counts", "freshness_at_capture",
    "stale_after_days", "coverage", "review_state", "source_admission", "release_state", "candidate_id",
}


def expected_flags(record: dict) -> list[str]:
    """The parser's review flags for a quarantine-free event, in its order."""
    flags = []
    if record["episode_id"] is None:
        flags.append("EPISODE_ID_ABSENT")
    if record["event_type"] not in storm_events.DIRECTIVE_EVENT_TYPES:
        flags.append("EVENT_TYPE_OUTSIDE_DIRECTIVE")
    if record["begin_utc"] is None:
        flags.append("UTC_OFFSET_UNKNOWN")
    if record["begin_lat"] is None:
        flags.append("ZONE_OR_COUNTY_SUPPORT_ONLY")
    return flags


def expected_utc(local: str, zone_token: str) -> str | None:
    zone = storm_events.TIMEZONE.fullmatch(zone_token)
    if zone is None:
        return None
    return (datetime.fromisoformat(local) + timedelta(hours=int(zone.group(1)))).isoformat(timespec="minutes") + "Z"


def validate_candidate(candidate: dict) -> dict:
    if not isinstance(candidate, dict) or set(candidate) != CANDIDATE_KEYS:
        raise ValueError("CANDIDATE_SHAPE_INVALID")
    if len(canonical_bytes(candidate)) > 32 * 1024 * 1024:
        raise ValueError("CANDIDATE_BYTE_LIMIT")
    if (candidate["profile"] != CANDIDATE_PROFILE or candidate["source_id"] != SOURCE_ID
            or candidate["state_fips"] != STATE_FIPS or not DIGEST.fullmatch(str(candidate["capture_id"]))
            or candidate["source_admission"] != "PENDING" or candidate["review_state"] != "PENDING"
            or candidate["release_state"] != "UNRELEASED" or candidate["coverage"] != "NOT_ESTABLISHED"
            or candidate["stale_after_days"] != STALE_AFTER_DAYS):
        raise ValueError("CANDIDATE_AUTHORITY_OR_PROFILE_INVALID")
    expected = digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "candidate_id"}))
    if expected != candidate["candidate_id"]:
        raise ValueError("CANDIDATE_DIGEST_MISMATCH")
    # The source file names the data year and its creation vintage; both must agree with the candidate.
    try:
        year = data_year(candidate["data_year"])
        vintage = storm_events.file_vintage(storm_events.HOST + storm_events.DIRECTORY + str(candidate["source_file"]))
    except (ValueError, storm_events.StormEventsInputError):
        raise ValueError("CANDIDATE_SOURCE_FILE_INVALID") from None
    created = vintage.created
    if (vintage.data_year != year or candidate["vintage_created"] != f"{created[:4]}-{created[4:6]}-{created[6:]}"
            or str(candidate["retrieved_at"])[:10] < candidate["vintage_created"]):
        raise ValueError("CANDIDATE_SOURCE_FILE_INVALID")
    counts = candidate["withheld_counts"]
    if (not isinstance(counts, dict) or set(counts) != set(WITHHELD)
            or any(type(n) is not int or n < 0 for n in counts.values())):
        raise ValueError("WITHHELD_COUNTS_INVALID")
    validator = Draft202012Validator(json.loads(SCHEMA.read_text()), format_checker=FormatChecker())
    observations = candidate["observations"]
    if not isinstance(observations, list) or len(observations) > MAX_EVENTS:
        raise ValueError("OBSERVATION_COUNT_INVALID")
    previous = 0
    for record in observations:
        if not validator.is_valid(record):
            raise ValueError("STORM_EVENT_SCHEMA_INVALID")
        if digest_bytes(canonical_bytes({k: v for k, v in record.items() if k != "record_digest"})) != record["record_digest"]:
            raise ValueError("RECORD_DIGEST_MISMATCH")
        key = identity(record["event_id"])
        if record["id"] != "kfm:storm:" + key or record["evidence_ref"] != "kfm:evidence:storm:" + key:
            raise ValueError("RECORD_IDENTITY_MISMATCH")
        if record["event_id"] <= previous:
            raise ValueError("RECORD_ORDER_OR_DUPLICATE")
        previous = record["event_id"]
        if record["begin_local"][:4] != str(year) or record["end_local"] < record["begin_local"]:
            raise ValueError("RECORD_TIME_INVALID")
        if record["retrieved_at"] > candidate["retrieved_at"]:
            raise ValueError("RECORD_TIME_INVALID")
        try:
            damages = (storm_events.parse_damage(record["damage_property_source"]),
                       storm_events.parse_damage(record["damage_crops_source"]))
        except storm_events.StormEventsInputError:
            raise ValueError("RECORD_DAMAGE_MISMATCH") from None
        if damages != (record["damage_property_usd"], record["damage_crops_usd"]):
            raise ValueError("RECORD_DAMAGE_MISMATCH")
        if (expected_utc(record["begin_local"], record["cz_timezone"]) != record["begin_utc"]
                or expected_utc(record["end_local"], record["cz_timezone"]) != record["end_utc"]):
            raise ValueError("RECORD_UTC_MISMATCH")
        if (record["begin_lat"] is None) != (record["begin_lon"] is None) or (record["end_lat"] is None) != (record["end_lon"] is None):
            raise ValueError("RECORD_COORDINATE_INVALID")
        if record["flags"] != expected_flags(record):
            raise ValueError("RECORD_FLAGS_MISMATCH")
    if candidate["latest_event_date"] != max((r["begin_local"][:10] for r in observations), default=None):
        raise ValueError("LATEST_EVENT_DATE_MISMATCH")
    if candidate["freshness_at_capture"] != freshness(candidate["vintage_created"], candidate["retrieved_at"]):
        raise ValueError("FRESHNESS_MISMATCH")
    report = {"profile": "kfm.storm-events-validation/v1", "candidate_id": expected, "outcome": "PASS",
              "observations": len(observations), "withheld": sum(counts.values()),
              "review_required": True, "promotion_authorized": False,
              "release_authorized": False, "publication_authorized": False}
    report["receipt_digest"] = digest_bytes(canonical_bytes(report))
    return report
