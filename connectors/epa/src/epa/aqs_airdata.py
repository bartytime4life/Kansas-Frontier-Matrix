"""Offline EPA AQS AirData daily-summary file planning and parsing; never fetches.

An AirData daily-summary row is EPA's computed daily summary for one regulatory monitor
(site, parameter, POC) under one sample duration, pollutant standard and event-type
treatment. It is not an exposure estimate, an attainment or design-value determination,
an AQI forecast, or an area-wide air-quality claim. This module plans one canonical
pre-generated ``daily_<parameter>_<year>.zip`` URL for a criteria-pollutant parameter
code, and parses an *already supplied* archive: the national CSV is streamed, only rows
EPA attributes to Kansas (``State Code`` ``20``) are classified, numbers stay exact
``Decimal`` values with every source token kept verbatim, and a blank AQI stays blank.

The archive layout, column set, event-type vocabulary and row identity are NEEDS
VERIFICATION against current AirData documentation: any unexpected archive member,
column set, identity or shape rejects the whole file rather than being coerced. The AQS
API (which needs an account key) is not planned here. Exceptional-event review, site
metadata review, activation, persistence and aggregation belong to owning layers.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from hashlib import sha256
import io
import json
import re
import zipfile
import zlib

HOST = "https://aqs.epa.gov"
DIRECTORY = "/aqsweb/airdata/"
FILE_NAME = re.compile(r"daily_(\d{5})_(\d{4})\.zip\Z")
KANSAS_STATE_CODE = "20"
FIRST_YEAR = 1980
# Criteria-pollutant parameter codes published as daily-summary files.
PARAMETERS = {
    "42101": "Carbon monoxide",
    "42401": "Sulfur dioxide",
    "42602": "Nitrogen dioxide (NO2)",
    "44201": "Ozone",
    "81102": "PM10 Total 0-10um STP",
    "88101": "PM2.5 - Local Conditions",
    "88502": "Acceptable PM2.5 AQI & Speciation Mass",
}
REQUIRED_COLUMNS = (
    "State Code", "County Code", "Site Num", "Parameter Code", "POC", "Latitude",
    "Longitude", "Datum", "Parameter Name", "Sample Duration", "Pollutant Standard",
    "Date Local", "Units of Measure", "Event Type", "Observation Count",
    "Observation Percent", "Arithmetic Mean", "1st Max Value", "1st Max Hour", "AQI",
    "Method Code", "Method Name", "Local Site Name", "Address", "State Name",
    "County Name", "City Name", "CBSA Name", "Date of Last Change")
# Event treatment -> flag. AirData documents ``No Events``, ``Events Included``,
# ``Events Excluded`` and ``Concurred Events Excluded``; the short forms are also accepted
# (which spelling current files carry is NEEDS VERIFICATION). The value stays verbatim;
# anything else is not interpreted.
EVENT_TYPES = {
    "No Events": None, "None": None,
    "Events Included": "EVENTS_INCLUDED", "Included": "EVENTS_INCLUDED",
    "Events Excluded": "EVENTS_EXCLUDED", "Excluded": "EVENTS_EXCLUDED",
    "Concurred Events Excluded": "CONCURRED_EVENTS_EXCLUDED",
    "Concurred": "CONCURRED_EVENTS_EXCLUDED",
}
NUMBER = re.compile(r"-?\d{1,9}(?:\.\d{1,9})?\Z")
DAY = re.compile(r"\d{4}-\d{2}-\d{2}\Z")
# A CSV this regular compresses well, but not by more than this; beyond it is a bomb.
MAX_COMPRESSION_RATIO = 200


class AqsInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected candidate input."""


def _integer(value: object, minimum: int, maximum: int) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise AqsInputError("INTEGER_BOUND")
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
        raise AqsInputError("UTC_TIME") from None


def daily_url(parameter: str, year: int) -> str:
    """Return the one pre-generated daily-summary archive URL for a parameter and year."""
    if not isinstance(parameter, str) or parameter not in PARAMETERS:
        raise AqsInputError("PARAMETER_SCOPE")
    _integer(year, FIRST_YEAR, 2100)
    return f"{HOST}{DIRECTORY}daily_{parameter}_{year}.zip"


@dataclass(frozen=True)
class DailyFile:
    parameter: str
    year: int
    file_name: str

    @property
    def member_name(self) -> str:
        return self.file_name[:-len(".zip")] + ".csv"


def daily_file(source_url: object) -> DailyFile:
    """Validate a daily-summary archive URL and return the parameter and year it names."""
    if not isinstance(source_url, str) or not source_url.startswith(HOST + DIRECTORY):
        raise AqsInputError("SOURCE_URL")
    name = source_url[len(HOST + DIRECTORY):]
    match = FILE_NAME.fullmatch(name)
    if match is None:
        raise AqsInputError("SOURCE_URL")
    parameter, year = match.group(1), int(match.group(2))
    if daily_url(parameter, year) != source_url:
        raise AqsInputError("SOURCE_URL_SCOPE")
    return DailyFile(parameter, year, name)


def _decimal(token: str) -> Decimal:
    if not NUMBER.fullmatch(token):
        raise AqsInputError("NUMBER_FORMAT")
    try:
        return Decimal(token)
    except InvalidOperation:
        raise AqsInputError("NUMBER_FORMAT") from None


@dataclass(frozen=True)
class DailyRecord:
    # ``SS-CCC-NNNN`` AQS site identity as EPA reports it; never re-geocoded here.
    site_id: str
    parameter_code: str
    poc: int
    date_local: str
    sample_duration: str
    pollutant_standard: str
    units: str
    event_type: str
    # Exact source values; None only where the token could not be read (quarantined).
    observation_count: int | None
    observation_percent: Decimal | None
    arithmetic_mean: Decimal | None
    first_max_value: Decimal | None
    first_max_hour: int | None
    # EPA's daily AQI where it reports one; blank stays None (not zero, not "good").
    aqi: int | None
    method_code: str
    latitude: Decimal | None
    longitude: Decimal | None
    datum: str
    date_of_last_change: str
    route: str
    reasons: tuple[str, ...]
    # Every source column verbatim. Never log or render it.
    raw_record_json: str
    record_sha256: str
    admission: str = "NOT_ADMITTED"

    @property
    def identity(self) -> tuple[str, int, str, str, str, str]:
        return (self.site_id, self.poc, self.date_local, self.sample_duration,
                self.pollutant_standard, self.event_type)


def _classify(row: dict[str, str], file: DailyFile) -> DailyRecord:
    county, site, poc = row["County Code"], row["Site Num"], row["POC"]
    if not re.fullmatch(r"\d{3}", county) or not re.fullmatch(r"\d{4}", site):
        raise AqsInputError("SITE_IDENTITY")
    if not re.fullmatch(r"\d{1,2}", poc) or int(poc) < 1:
        raise AqsInputError("POC_FORMAT")
    day = row["Date Local"]
    try:
        if not DAY.fullmatch(day):
            raise ValueError
        parsed_day = datetime.strptime(day, "%Y-%m-%d")
    except ValueError:
        raise AqsInputError("DATE_FORMAT") from None
    if parsed_day.year != file.year:
        raise AqsInputError("ROW_OUTSIDE_DATA_YEAR")
    if not row["Sample Duration"] or not row["Units of Measure"]:
        raise AqsInputError("ROW_IDENTITY")
    reasons: list[str] = []
    event_type = row["Event Type"]
    if event_type not in EVENT_TYPES:
        reasons.append("EVENT_TYPE_UNRECOGNIZED")
    elif EVENT_TYPES[event_type] is not None:
        reasons.append(EVENT_TYPES[event_type])
    numbers: dict[str, Decimal | None] = {}
    for column in ("Observation Percent", "Arithmetic Mean", "1st Max Value"):
        try:
            numbers[column] = _decimal(row[column])
        except AqsInputError:
            numbers[column] = None
            reasons.append("NUMBER_UNPARSEABLE")
    count = int(row["Observation Count"]) if re.fullmatch(r"\d{1,6}", row["Observation Count"]) \
        else None
    hour = int(row["1st Max Hour"]) if re.fullmatch(r"\d{1,2}", row["1st Max Hour"]) \
        and int(row["1st Max Hour"]) <= 23 else None
    if count is None or hour is None:
        reasons.append("NUMBER_UNPARSEABLE")
    aqi = None
    if row["AQI"] == "":
        reasons.append("AQI_NOT_REPORTED")
    elif re.fullmatch(r"\d{1,4}", row["AQI"]):
        aqi = int(row["AQI"])
    else:
        reasons.append("NUMBER_UNPARSEABLE")
    try:
        latitude, longitude = _decimal(row["Latitude"]), _decimal(row["Longitude"])
        if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
            raise AqsInputError("COORDINATE_RANGE")
    except AqsInputError:
        latitude = longitude = None
        reasons.append("COORDINATE_UNPARSEABLE")
    raw_json = json.dumps(row, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    # Event treatment and a blank AQI are carried as flags; an unreadable number or
    # coordinate, or an event type this module does not know, goes to quarantine.
    blocking = {"EVENT_TYPE_UNRECOGNIZED", "NUMBER_UNPARSEABLE", "COORDINATE_UNPARSEABLE"}
    return DailyRecord(
        f"{KANSAS_STATE_CODE}-{county}-{site}", file.parameter, int(poc), day,
        row["Sample Duration"], row["Pollutant Standard"], row["Units of Measure"], event_type,
        count, numbers["Observation Percent"], numbers["Arithmetic Mean"],
        numbers["1st Max Value"], hour, aqi, row["Method Code"], latitude, longitude,
        row["Datum"], row["Date of Last Change"],
        "QUARANTINE_CANDIDATE" if blocking.intersection(reasons) else "RAW_CANDIDATE",
        tuple(dict.fromkeys(reasons)), raw_json,
        "sha256:" + sha256(raw_json.encode("utf-8")).hexdigest())


@dataclass(frozen=True)
class DailyFileCandidate:
    source_url: str
    file: DailyFile
    retrieved_at: str
    body_sha256: str
    member_bytes: int
    columns: tuple[str, ...]
    # Every data row read (all states), and the Kansas rows classified from them.
    rows_total: int
    records: tuple[DailyRecord, ...]
    # Rows EPA attributes to State Code 20, not a spatial join; a parsed file proves
    # neither monitoring completeness nor that absence means clean air.
    scope: str = "STATE_CODE_20_ROWS"
    coverage: str = "NOT_ESTABLISHED"


def _member(archive: zipfile.ZipFile, file: DailyFile, max_member_bytes: int,
            body_bytes: int) -> zipfile.ZipInfo:
    members = archive.infolist()
    if len(members) != 1:
        raise AqsInputError("ZIP_MEMBERS")
    info = members[0]
    if info.filename != file.member_name or info.is_dir():
        raise AqsInputError("ZIP_MEMBER_NAME")
    if info.flag_bits & 0x1:
        raise AqsInputError("ZIP_ENCRYPTED")
    if info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
        raise AqsInputError("ZIP_COMPRESSION")
    if info.file_size > max_member_bytes:
        raise AqsInputError("DECOMPRESSED_BOUND")
    if info.file_size > MAX_COMPRESSION_RATIO * max(info.compress_size, 1) \
            or info.compress_size > body_bytes:
        raise AqsInputError("COMPRESSION_RATIO")
    return info


def parse_daily_file(body: bytes, *, status: int, source_url: str, retrieved_at: str,
                     max_bytes: int = 128 * 1024 * 1024,
                     max_member_bytes: int = 1024 * 1024 * 1024,
                     max_rows_total: int = 5_000_000,
                     max_rows: int = 200_000) -> DailyFileCandidate:
    """Parse one supplied daily-summary archive; reject it whole on structural failure."""
    file = daily_file(source_url)
    retrieved = _utc(retrieved_at)
    _integer(max_bytes, 1, 1024 * 1024 * 1024)
    _integer(max_member_bytes, 1, 4 * 1024 * 1024 * 1024)
    _integer(max_rows_total, 1, 20_000_000)
    _integer(max_rows, 1, 1_000_000)
    if type(status) is not int or not isinstance(body, bytes) or len(body) > max_bytes:
        raise AqsInputError("RESPONSE_BOUND")
    if status != 200:
        raise AqsInputError("HTTP_STATUS")
    if body[:4] != b"PK\x03\x04":
        raise AqsInputError("NOT_ZIP")
    records: list[DailyRecord] = []
    seen: set[tuple[str, int, str, str, str, str]] = set()
    rows_total = 0
    try:
        with zipfile.ZipFile(io.BytesIO(body)) as archive:
            info = _member(archive, file, max_member_bytes, len(body))
            with archive.open(info) as raw, \
                    io.TextIOWrapper(raw, encoding="utf-8", newline="") as text:
                reader = csv.reader(text, strict=True)
                try:
                    header = next(reader)
                except StopIteration:
                    raise AqsInputError("HEADER_MISSING") from None
                if len(set(header)) != len(header):
                    raise AqsInputError("DUPLICATE_COLUMN")
                if set(REQUIRED_COLUMNS) - set(header):
                    raise AqsInputError("SCHEMA_DRIFT")
                state = header.index("State Code")
                parameter = header.index("Parameter Code")
                for values in reader:
                    rows_total += 1
                    if rows_total > max_rows_total:
                        raise AqsInputError("ROW_BOUND")
                    if len(values) != len(header):
                        raise AqsInputError("ROW_WIDTH")
                    if values[parameter] != file.parameter:
                        raise AqsInputError("PARAMETER_MISMATCH")
                    if values[state] != KANSAS_STATE_CODE:
                        continue
                    if len(records) >= max_rows:
                        raise AqsInputError("KANSAS_ROW_BOUND")
                    record = _classify(dict(zip(header, values)), file)
                    if record.identity in seen:
                        raise AqsInputError("DUPLICATE_RECORD")
                    seen.add(record.identity)
                    records.append(record)
    except AqsInputError:
        raise
    except UnicodeDecodeError:
        raise AqsInputError("ENCODING") from None
    except csv.Error:
        raise AqsInputError("CSV_STRUCTURE") from None
    except (zipfile.BadZipFile, zlib.error, EOFError, OSError, NotImplementedError):
        raise AqsInputError("ZIP_CORRUPT") from None
    return DailyFileCandidate(source_url, file, retrieved, "sha256:" + sha256(body).hexdigest(),
                              info.file_size, tuple(header), rows_total, tuple(records))
