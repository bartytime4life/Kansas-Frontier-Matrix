"""Pure, deterministic NOAA Storm Events normalization from verified captured bytes.

Produces review candidates only: a complete capture is neither source admission
nor release. Each Kansas event keeps its source strings (damage, magnitude,
F/EF scale, time zone) verbatim beside parsed values, and carries the parser's
review flags. Narratives are never copied into a candidate (only whether one
exists), because they are unreviewed free text. Events the parser routes to
quarantine (unreadable casualties or damage, end before begin) are withheld and
counted by reason. A parsed file proves neither completeness nor that the
absence of a record means no hazard.
"""
from __future__ import annotations

from datetime import date
import json
import re

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.noaa.src.noaa import storm_events
from connectors.noaa.src.noaa.storm_events_capture import (
    LISTING_KEY, PROFILE, SOURCE_ID, STATE_FIPS, latest_details, object_limit, object_url,
)

CANDIDATE_PROFILE = "kfm.storm-events-candidate/v1"
RECORD_PROFILE = "kfm.storm-event-record/v1"
DIGEST = re.compile(r"sha256:[a-f0-9]{64}\Z")
# Parser reasons that route an event to quarantine; every other reason is a review flag.
WITHHELD = ("CASUALTY_UNPARSEABLE", "DAMAGE_UNPARSEABLE", "END_BEFORE_BEGIN")
FLAGS = ("EPISODE_ID_ABSENT", "EVENT_TYPE_OUTSIDE_DIRECTIVE", "UTC_OFFSET_UNKNOWN", "ZONE_OR_COUNTY_SUPPORT_ONLY")
# NCEI reissues files roughly monthly; an older vintage at capture time is stale.
STALE_AFTER_DAYS = 45
MAX_EVENTS = 20_000


def identity(event_id: int) -> str:
    return digest_bytes(canonical_bytes([SOURCE_ID, event_id])).split(":")[1]


def record(event: storm_events.EventCandidate, page: dict) -> dict:
    """A closed candidate record; the raw row (and its narratives) stays out."""
    raw = json.loads(event.raw_record_json)
    key = identity(event.event_id)
    value = {"profile": RECORD_PROFILE, "id": "kfm:storm:" + key, "event_id": event.event_id,
             "episode_id": event.episode_id, "event_type": event.event_type, "cz_type": event.cz_type,
             "cz_fips": event.cz_fips, "cz_name": event.cz_name, "cz_timezone": raw["CZ_TIMEZONE"],
             "begin_local": event.begin_local, "end_local": event.end_local,
             "begin_utc": event.begin_utc, "end_utc": event.end_utc,
             "injuries_direct": event.injuries_direct, "injuries_indirect": event.injuries_indirect,
             "deaths_direct": event.deaths_direct, "deaths_indirect": event.deaths_indirect,
             "damage_property_usd": event.damage_property_usd, "damage_crops_usd": event.damage_crops_usd,
             "damage_property_source": event.damage_property_source,
             "damage_crops_source": event.damage_crops_source,
             "magnitude_source": event.magnitude_source, "magnitude_type": event.magnitude_type,
             "tor_f_scale": event.tor_f_scale,
             "begin_lat": event.begin_lat, "begin_lon": event.begin_lon,
             "end_lat": event.end_lat, "end_lon": event.end_lon,
             "has_narrative": event.has_narrative, "flags": list(event.reasons),
             "source_row_digest": event.record_sha256, "page_digest": page["sha256"],
             "retrieved_at": page["retrieved_at"], "evidence_ref": "kfm:evidence:storm:" + key}
    value["record_digest"] = digest_bytes(canonical_bytes(value))
    return value


def freshness(vintage_created: str, retrieved_at: str) -> str:
    """CURRENT while the captured file vintage is at most STALE_AFTER_DAYS old at retrieval."""
    age = (date.fromisoformat(retrieved_at[:10]) - date.fromisoformat(vintage_created)).days
    return "STALE" if age > STALE_AFTER_DAYS else "CURRENT"


def normalize_capture(manifest: dict, objects: dict[str, bytes]) -> dict:
    """Check capture closure and scope, then select the year's Kansas events."""
    body = {key: value for key, value in manifest.items() if key != "capture_id"}
    if manifest.get("capture_id") != digest_bytes(canonical_bytes(body)):
        raise ValueError("CAPTURE_DIGEST_MISMATCH")
    if manifest.get("profile") != PROFILE or manifest.get("complete") is not True:
        raise ValueError("CAPTURE_INCOMPLETE")
    if manifest.get("source_id") != SOURCE_ID or manifest.get("state_fips") != STATE_FIPS:
        raise ValueError("CAPTURE_SCOPE_MISMATCH")
    year = manifest.get("data_year")
    pages = manifest.get("pages")
    if (not isinstance(pages, list) or len(pages) != 2 or not all(isinstance(p, dict) for p in pages)
            or pages[0].get("key") != LISTING_KEY):
        raise ValueError("CAPTURE_PAGE_CHAIN_MISMATCH")
    verified = []
    for page in pages:
        raw = objects.get(page.get("sha256"))
        if (page.get("url") != object_url(page["key"]) or not DIGEST.fullmatch(str(page.get("sha256")))
                or raw is None or digest_bytes(raw) != page["sha256"] or len(raw) != page.get("bytes")
                or len(raw) > object_limit(page["key"]) or not isinstance(page.get("retrieved_at"), str)
                or page["retrieved_at"] > manifest.get("captured_at", "")):
            raise ValueError("PAGE_DIGEST_MISMATCH")
        verified.append(raw)
    # The details file must be the one the captured listing names as newest for the year.
    if pages[1]["key"] != latest_details(verified[0], year):
        raise ValueError("CAPTURE_PAGE_CHAIN_MISMATCH")
    details_page = pages[1]
    try:
        parsed = storm_events.parse_details_file(verified[1], status=200, source_url=details_page["url"],
                                                 retrieved_at=details_page["retrieved_at"])
    except storm_events.StormEventsInputError as exc:
        raise ValueError("DETAILS_FILE_" + str(exc)) from None
    if parsed.vintage.data_year != year:
        raise ValueError("CAPTURE_SCOPE_MISMATCH")
    kansas = storm_events.select_state(parsed, state_fips=STATE_FIPS)
    if len(kansas) > MAX_EVENTS:
        raise ValueError("EVENT_COUNT_LIMIT")
    withheld = {reason: 0 for reason in WITHHELD}
    records = []
    for event in sorted(kansas, key=lambda e: e.event_id):
        blocking = [reason for reason in event.reasons if reason in WITHHELD]
        if blocking:
            withheld[blocking[0]] += 1
            continue
        records.append(record(event, details_page))
    created = parsed.vintage.created
    vintage = f"{created[:4]}-{created[4:6]}-{created[6:]}"
    candidate = {"profile": CANDIDATE_PROFILE, "capture_id": manifest["capture_id"], "source_id": SOURCE_ID,
                 "state_fips": STATE_FIPS, "data_year": year, "source_file": details_page["key"],
                 "vintage_created": vintage, "retrieved_at": manifest["captured_at"], "observations": records,
                 "latest_event_date": max((r["begin_local"][:10] for r in records), default=None),
                 "withheld_counts": withheld, "freshness_at_capture": freshness(vintage, manifest["captured_at"]),
                 "stale_after_days": STALE_AFTER_DAYS, "coverage": "NOT_ESTABLISHED",
                 "review_state": "PENDING", "source_admission": "PENDING", "release_state": "UNRELEASED"}
    candidate["candidate_id"] = digest_bytes(canonical_bytes(candidate))
    return candidate
