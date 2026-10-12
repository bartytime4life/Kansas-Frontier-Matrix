"""Offline NCEI Storm Events details-file planning and parsing; never fetches.

A Storm Events record is a forecaster-compiled historical event record, not a
measurement, alert, inundation extent, or damage settlement. This module keeps
source values verbatim beside their parsed forms, marks every narrative
``unreviewed``, and leaves source activation, finalization review, sensitivity
decisions, persistence, and publication to owning layers.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
import gzip
from hashlib import sha256
import io
import json
import math
import re
import zlib

HOST = "https://www.ncei.noaa.gov"
DIRECTORY = "/pub/data/swdi/stormevents/csvfiles/"
FILE_NAME = re.compile(r"StormEvents_details-ftp_v1\.0_d(\d{4})_c(\d{8})\.csv\.gz\Z")
KANSAS_FIPS = 20
REQUIRED_COLUMNS = (
    "BEGIN_YEARMONTH", "BEGIN_DAY", "BEGIN_TIME", "END_YEARMONTH", "END_DAY", "END_TIME",
    "EPISODE_ID", "EVENT_ID", "STATE", "STATE_FIPS", "EVENT_TYPE", "CZ_TYPE", "CZ_FIPS",
    "CZ_NAME", "CZ_TIMEZONE", "INJURIES_DIRECT", "INJURIES_INDIRECT", "DEATHS_DIRECT",
    "DEATHS_INDIRECT", "DAMAGE_PROPERTY", "DAMAGE_CROPS", "MAGNITUDE", "MAGNITUDE_TYPE",
    "TOR_F_SCALE", "BEGIN_LAT", "BEGIN_LON", "END_LAT", "END_LON", "EPISODE_NARRATIVE",
    "EVENT_NARRATIVE")
# Event types named in NWS Directive 10-1605; older vintages use other labels,
# which are flagged for review rather than rejected or rewritten.
DIRECTIVE_EVENT_TYPES = frozenset({
    "Astronomical Low Tide", "Avalanche", "Blizzard", "Coastal Flood", "Cold/Wind Chill",
    "Debris Flow", "Dense Fog", "Dense Smoke", "Drought", "Dust Devil", "Dust Storm",
    "Excessive Heat", "Extreme Cold/Wind Chill", "Flash Flood", "Flood", "Freezing Fog",
    "Frost/Freeze", "Funnel Cloud", "Hail", "Heat", "Heavy Rain", "Heavy Snow", "High Surf",
    "High Wind", "Hurricane (Typhoon)", "Ice Storm", "Lake-Effect Snow", "Lakeshore Flood",
    "Lightning", "Marine Dense Fog", "Marine Hail", "Marine High Wind", "Marine Strong Wind",
    "Marine Thunderstorm Wind", "Rip Current", "Seiche", "Sleet", "Sneakerwave",
    "Storm Surge/Tide", "Strong Wind", "Thunderstorm Wind", "Tornado", "Tropical Depression",
    "Tropical Storm", "Tsunami", "Volcanic Ash", "Waterspout", "Wildfire", "Winter Storm",
    "Winter Weather"})
DAMAGE = re.compile(r"(\d+(?:\.\d+)?)([KMB]?)\Z")
DAMAGE_SCALE = {"": 1, "K": 1_000, "M": 1_000_000, "B": 1_000_000_000}
TIMEZONE = re.compile(r"[A-Z]{3}-(\d{1,2})\Z")


class StormEventsInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected candidate input."""


def _integer(value: object, minimum: int, maximum: int) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise StormEventsInputError("INTEGER_BOUND")
    return value


def _utc(value: object) -> str:
    try:
        if not isinstance(value, str) or len(value) > 40:
            raise ValueError
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        return result.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    except (ValueError, TypeError, OverflowError):
        raise StormEventsInputError("UTC_TIME") from None


def details_url(year: int, created: str) -> str:
    """Return one details-file URL for a data year and NCEI creation date (YYYYMMDD)."""
    _integer(year, 1950, 2100)
    if not isinstance(created, str) or not re.fullmatch(r"\d{8}", created):
        raise StormEventsInputError("CREATION_DATE")
    return f"{HOST}{DIRECTORY}StormEvents_details-ftp_v1.0_d{year}_c{created}.csv.gz"


@dataclass(frozen=True)
class FileVintage:
    data_year: int
    created: str
    file_name: str


def file_vintage(source_url: object) -> FileVintage:
    """Validate a details-file URL and return its data year and creation vintage."""
    if not isinstance(source_url, str) or not source_url.startswith(HOST + DIRECTORY):
        raise StormEventsInputError("SOURCE_URL")
    name = source_url[len(HOST + DIRECTORY):]
    match = FILE_NAME.fullmatch(name)
    if match is None:
        raise StormEventsInputError("SOURCE_URL")
    year, created = int(match.group(1)), match.group(2)
    try:
        created_day = datetime.strptime(created, "%Y%m%d")
    except ValueError:
        raise StormEventsInputError("CREATION_DATE") from None
    if created_day.year < year:
        raise StormEventsInputError("CREATION_BEFORE_DATA_YEAR")
    return FileVintage(year, created, name)


def parse_damage(value: str) -> int | None:
    """Parse an NCEI damage string such as ``10.00K`` to whole nominal USD, exactly.

    Blank means not reported (None), which is different from ``0.00K``.
    """
    if value == "":
        return None
    match = DAMAGE.fullmatch(value.strip().upper())
    if match is None:
        raise StormEventsInputError("DAMAGE_FORMAT")
    try:
        amount = Decimal(match.group(1)) * DAMAGE_SCALE[match.group(2)]
    except InvalidOperation:
        raise StormEventsInputError("DAMAGE_FORMAT") from None
    if amount != amount.to_integral_value():
        raise StormEventsInputError("DAMAGE_FRACTIONAL_DOLLARS")
    return int(amount)


def _count(value: str) -> int:
    if not re.fullmatch(r"\d{1,6}", value):
        raise StormEventsInputError("CASUALTY_FORMAT")
    return int(value)


def _local_time(yearmonth: str, day: str, hhmm: str) -> datetime:
    if not (re.fullmatch(r"\d{6}", yearmonth) and re.fullmatch(r"\d{1,2}", day)
            and re.fullmatch(r"\d{1,4}", hhmm)):
        raise StormEventsInputError("EVENT_TIME")
    clock = hhmm.zfill(4)
    try:
        return datetime(int(yearmonth[:4]), int(yearmonth[4:]), int(day),
                        int(clock[:2]), int(clock[2:]))
    except ValueError:
        raise StormEventsInputError("EVENT_TIME") from None


def _coordinate_pair(lat: str, lon: str) -> tuple[float | None, float | None]:
    if lat == "" and lon == "":
        return None, None
    try:
        latitude, longitude = float(lat), float(lon)
    except ValueError:
        raise StormEventsInputError("COORDINATE_FORMAT") from None
    if not (math.isfinite(latitude) and math.isfinite(longitude)
            and -90 <= latitude <= 90 and -180 <= longitude <= 180):
        raise StormEventsInputError("COORDINATE_RANGE")
    return latitude, longitude


@dataclass(frozen=True)
class EventCandidate:
    event_id: int
    episode_id: int | None
    state_fips: int
    event_type: str
    cz_type: str
    cz_fips: int
    cz_name: str
    # Local wall-clock times as issued, plus UTC only when the zone carries an offset.
    begin_local: str
    end_local: str
    begin_utc: str | None
    end_utc: str | None
    injuries_direct: int | None
    injuries_indirect: int | None
    deaths_direct: int | None
    deaths_indirect: int | None
    # Nominal event-year USD field estimates; never compensation or declaration values.
    damage_property_usd: int | None
    damage_crops_usd: int | None
    damage_property_source: str
    damage_crops_source: str
    # Magnitude and F/EF scale are classifications or estimates, never measurements.
    magnitude_source: str
    magnitude_type: str
    tor_f_scale: str
    begin_lat: float | None
    begin_lon: float | None
    end_lat: float | None
    end_lon: float | None
    has_narrative: bool
    route: str
    reasons: tuple[str, ...]
    # Every source column verbatim, narratives included. Never log or render it.
    raw_record_json: str
    record_sha256: str
    narrative_sensitivity_flag: str = "unreviewed"
    finalized_state: str = "NOT_DETERMINED"
    admission: str = "NOT_ADMITTED"


def _classify(row: dict[str, str]) -> EventCandidate:
    reasons: list[str] = []
    try:
        event_id = int(row["EVENT_ID"])
        state_fips = int(row["STATE_FIPS"])
        cz_fips = int(row["CZ_FIPS"])
    except ValueError:
        raise StormEventsInputError("IDENTITY_FORMAT") from None
    if event_id < 1:
        raise StormEventsInputError("IDENTITY_FORMAT")
    episode_id = None
    if row["EPISODE_ID"]:
        if not row["EPISODE_ID"].isdigit():
            raise StormEventsInputError("IDENTITY_FORMAT")
        episode_id = int(row["EPISODE_ID"])
    else:
        reasons.append("EPISODE_ID_ABSENT")
    event_type = row["EVENT_TYPE"]
    if not event_type:
        raise StormEventsInputError("EVENT_TYPE")
    if event_type not in DIRECTIVE_EVENT_TYPES:
        reasons.append("EVENT_TYPE_OUTSIDE_DIRECTIVE")
    begin = _local_time(row["BEGIN_YEARMONTH"], row["BEGIN_DAY"], row["BEGIN_TIME"])
    end = _local_time(row["END_YEARMONTH"], row["END_DAY"], row["END_TIME"])
    if end < begin:
        reasons.append("END_BEFORE_BEGIN")
    zone = TIMEZONE.fullmatch(row["CZ_TIMEZONE"])
    if zone is None:
        reasons.append("UTC_OFFSET_UNKNOWN")
        begin_utc = end_utc = None
    else:
        offset = timedelta(hours=int(zone.group(1)))
        begin_utc = (begin + offset).isoformat(timespec="minutes") + "Z"
        end_utc = (end + offset).isoformat(timespec="minutes") + "Z"
    casualties: list[int | None] = []
    for column in ("INJURIES_DIRECT", "INJURIES_INDIRECT", "DEATHS_DIRECT", "DEATHS_INDIRECT"):
        try:
            casualties.append(_count(row[column]))
        except StormEventsInputError:
            casualties.append(None)
            reasons.append("CASUALTY_UNPARSEABLE")
    damages: list[int | None] = []
    for column in ("DAMAGE_PROPERTY", "DAMAGE_CROPS"):
        try:
            damages.append(parse_damage(row[column]))
        except StormEventsInputError:
            damages.append(None)
            reasons.append("DAMAGE_UNPARSEABLE")
    begin_lat, begin_lon = _coordinate_pair(row["BEGIN_LAT"], row["BEGIN_LON"])
    end_lat, end_lon = _coordinate_pair(row["END_LAT"], row["END_LON"])
    if begin_lat is None:
        reasons.append("ZONE_OR_COUNTY_SUPPORT_ONLY")
    has_narrative = bool(row["EVENT_NARRATIVE"] or row["EPISODE_NARRATIVE"])
    raw_json = json.dumps(row, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    # Missing episode, pre-directive labels, zone-only support, and unknown UTC offset
    # are carried as flags; anything that makes a structured value unreadable or
    # temporally inconsistent goes to quarantine.
    blocking = {"CASUALTY_UNPARSEABLE", "DAMAGE_UNPARSEABLE", "END_BEFORE_BEGIN"}
    return EventCandidate(
        event_id, episode_id, state_fips, event_type, row["CZ_TYPE"], cz_fips, row["CZ_NAME"],
        begin.isoformat(timespec="minutes"), end.isoformat(timespec="minutes"), begin_utc,
        end_utc, *casualties, *damages, row["DAMAGE_PROPERTY"], row["DAMAGE_CROPS"],
        row["MAGNITUDE"], row["MAGNITUDE_TYPE"], row["TOR_F_SCALE"], begin_lat, begin_lon,
        end_lat, end_lon, has_narrative,
        "QUARANTINE_CANDIDATE" if blocking.intersection(reasons) else "RAW_CANDIDATE",
        tuple(dict.fromkeys(reasons)), raw_json,
        "sha256:" + sha256(raw_json.encode("utf-8")).hexdigest())


@dataclass(frozen=True)
class DetailsFileCandidate:
    source_url: str
    vintage: FileVintage
    retrieved_at: str
    body_sha256: str
    columns: tuple[str, ...]
    events: tuple[EventCandidate, ...]
    # A parsed file proves neither completeness nor that absence means no hazard.
    coverage: str = "NOT_ESTABLISHED"


def _decompress(body: bytes, max_bytes: int) -> bytes:
    if body[:2] != b"\x1f\x8b":
        raise StormEventsInputError("NOT_GZIP")
    try:
        with gzip.GzipFile(fileobj=io.BytesIO(body)) as stream:
            data = stream.read(max_bytes + 1)
    except (OSError, EOFError, zlib.error):
        raise StormEventsInputError("GZIP_CORRUPT") from None
    if len(data) > max_bytes:
        raise StormEventsInputError("DECOMPRESSED_BOUND")
    return data


def parse_details_file(body: bytes, *, status: int, source_url: str, retrieved_at: str,
                       max_bytes: int = 256 * 1024 * 1024,
                       max_rows: int = 200_000) -> DetailsFileCandidate:
    """Parse one supplied gzip details file; reject it whole on structural failure."""
    vintage = file_vintage(source_url)
    retrieved = _utc(retrieved_at)
    _integer(max_bytes, 1, 1024 * 1024 * 1024)
    _integer(max_rows, 1, 1_000_000)
    if type(status) is not int or not isinstance(body, bytes) or len(body) > max_bytes:
        raise StormEventsInputError("RESPONSE_BOUND")
    if status != 200:
        raise StormEventsInputError("HTTP_STATUS")
    try:
        text = _decompress(body, max_bytes).decode("utf-8")
    except UnicodeDecodeError:
        raise StormEventsInputError("ENCODING") from None
    reader = csv.reader(io.StringIO(text, newline=""), strict=True)
    try:
        header = next(reader)
    except (StopIteration, csv.Error):
        raise StormEventsInputError("HEADER_MISSING") from None
    if len(set(header)) != len(header):
        raise StormEventsInputError("DUPLICATE_COLUMN")
    if set(REQUIRED_COLUMNS) - set(header):
        raise StormEventsInputError("SCHEMA_DRIFT")
    events: list[EventCandidate] = []
    seen: set[int] = set()
    try:
        for values in reader:
            if len(values) != len(header):
                raise StormEventsInputError("ROW_WIDTH")
            if len(events) >= max_rows:
                raise StormEventsInputError("ROW_BOUND")
            row = dict(zip(header, values))
            if row["BEGIN_YEARMONTH"][:4] != str(vintage.data_year):
                raise StormEventsInputError("ROW_OUTSIDE_DATA_YEAR")
            candidate = _classify(row)
            if candidate.event_id in seen:
                raise StormEventsInputError("DUPLICATE_EVENT_ID")
            seen.add(candidate.event_id)
            events.append(candidate)
    except csv.Error:
        raise StormEventsInputError("CSV_STRUCTURE") from None
    return DetailsFileCandidate(source_url, vintage, retrieved,
                                "sha256:" + sha256(body).hexdigest(), tuple(header),
                                tuple(events))


def select_state(candidate: DetailsFileCandidate, *,
                 state_fips: int = KANSAS_FIPS) -> tuple[EventCandidate, ...]:
    """Select rows NCEI attributed to a state FIPS; not a spatial join or completeness claim."""
    _integer(state_fips, 1, 78)
    return tuple(event for event in candidate.events if event.state_fips == state_fips)


@dataclass(frozen=True)
class VintageDelta:
    added: tuple[int, ...]
    removed: tuple[int, ...]
    changed: tuple[int, ...]
    unchanged: int


def compare_vintages(older: DetailsFileCandidate,
                     newer: DetailsFileCandidate) -> VintageDelta:
    """Compare two vintages of one data year; changes are corrections, never overwrites.

    A changed or removed event must be carried forward as a new source state with
    lineage to the prior record; this function only names which events differ.
    """
    if older.vintage.data_year != newer.vintage.data_year:
        raise StormEventsInputError("DATA_YEAR_MISMATCH")
    if older.vintage.created >= newer.vintage.created:
        raise StormEventsInputError("VINTAGE_ORDER")
    before = {event.event_id: event.record_sha256 for event in older.events}
    after = {event.event_id: event.record_sha256 for event in newer.events}
    return VintageDelta(tuple(sorted(after.keys() - before.keys())),
                        tuple(sorted(before.keys() - after.keys())),
                        tuple(sorted(key for key in before.keys() & after.keys()
                                     if before[key] != after[key])),
                        sum(1 for key in before.keys() & after.keys()
                            if before[key] == after[key]))
