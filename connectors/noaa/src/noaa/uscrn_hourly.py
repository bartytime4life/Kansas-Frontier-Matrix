"""Offline USCRN hourly02 file planning and parsing under one versioned profile; never fetches.

Columns are interpreted only through ``PROFILE`` (the published hourly02
layout). A line with a different field count is schema drift and rejects the
file. Source value tokens are kept beside parsed ``Decimal`` values, missing
sentinels stay missing (never zero), QC flags are preserved verbatim, and each
soil value keeps its depth. Calculated, averaged, and extreme values keep their
source derivation. Station metadata review, activation, persistence, and any
aggregation or interpolation belong to owning layers.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
from hashlib import sha256
import re

HOST = "https://www.ncei.noaa.gov"
DIRECTORY = "/pub/data/uscrn/products/hourly02/"
PROFILE_ID = "uscrn-hourly02-v1"
STATION_FILE = re.compile(r"CRNH0203-(\d{4})-([A-Z]{2})_([A-Za-z0-9_.]+)\.txt\Z")


@dataclass(frozen=True)
class Column:
    name: str
    unit: str | None
    derivation: str | None
    missing: frozenset[str]
    flag_column: str | None = None
    depth_cm: int | None = None


_NUM = frozenset({"-9999.0", "-9999"})
_SM = frozenset({"-99.000", "-99.0", "-99"})
# Published hourly02 order: 38 whitespace-separated fields.
PROFILE: tuple[Column, ...] = (
    Column("WBANNO", None, None, frozenset()),
    Column("UTC_DATE", None, None, frozenset()),
    Column("UTC_TIME", None, None, frozenset()),
    Column("LST_DATE", None, None, frozenset()),
    Column("LST_TIME", None, None, frozenset()),
    Column("CRX_VN", None, None, frozenset({"-9.000", "-9"})),
    Column("LONGITUDE", "degree", None, _NUM),
    Column("LATITUDE", "degree", None, _NUM),
    Column("T_CALC", "degC", "calculated_last_5_min", _NUM),
    Column("T_HR_AVG", "degC", "hourly_average", _NUM),
    Column("T_MAX", "degC", "hourly_max", _NUM),
    Column("T_MIN", "degC", "hourly_min", _NUM),
    Column("P_CALC", "mm", "hourly_total", _NUM),
    Column("SOLARAD", "W/m2", "hourly_average", _NUM, "SOLARAD_FLAG"),
    Column("SOLARAD_FLAG", None, None, frozenset()),
    Column("SOLARAD_MAX", "W/m2", "hourly_max", _NUM, "SOLARAD_MAX_FLAG"),
    Column("SOLARAD_MAX_FLAG", None, None, frozenset()),
    Column("SOLARAD_MIN", "W/m2", "hourly_min", _NUM, "SOLARAD_MIN_FLAG"),
    Column("SOLARAD_MIN_FLAG", None, None, frozenset()),
    Column("SUR_TEMP_TYPE", None, None, frozenset()),
    Column("SUR_TEMP", "degC", "hourly_average", _NUM, "SUR_TEMP_FLAG"),
    Column("SUR_TEMP_FLAG", None, None, frozenset()),
    Column("SUR_TEMP_MAX", "degC", "hourly_max", _NUM, "SUR_TEMP_MAX_FLAG"),
    Column("SUR_TEMP_MAX_FLAG", None, None, frozenset()),
    Column("SUR_TEMP_MIN", "degC", "hourly_min", _NUM, "SUR_TEMP_MIN_FLAG"),
    Column("SUR_TEMP_MIN_FLAG", None, None, frozenset()),
    Column("RH_HR_AVG", "percent", "hourly_average", _NUM, "RH_HR_AVG_FLAG"),
    Column("RH_HR_AVG_FLAG", None, None, frozenset()),
    *(Column(f"SOIL_MOISTURE_{d}", "m3/m3", "hourly_average", _SM, depth_cm=d)
      for d in (5, 10, 20, 50, 100)),
    *(Column(f"SOIL_TEMP_{d}", "degC", "hourly_average", _NUM, depth_cm=d)
      for d in (5, 10, 20, 50, 100)),
)
MEASUREMENTS = tuple(c for c in PROFILE if c.derivation is not None)
INDEX = {column.name: position for position, column in enumerate(PROFILE)}
QC_FLAGS = {"0": "GOOD", "3": "FAILED_QC_CHECK"}
SURFACE_TYPES = {"R": "RAW", "C": "CORRECTED", "U": "UNKNOWN"}
NUMBER = re.compile(r"-?\d+(?:\.\d+)?\Z")


class UscrnInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected candidate input."""


def _utc(value: object) -> str:
    try:
        if not isinstance(value, str) or len(value) > 40:
            raise ValueError
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        return result.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    except (ValueError, TypeError, OverflowError):
        raise UscrnInputError("UTC_TIME") from None


def hourly_url(year: int, station: str) -> str:
    """Return one station-year URL, e.g. station ``KS_Manhattan_6_SSW``."""
    if type(year) is not int or not 2000 <= year <= 2100:
        raise UscrnInputError("YEAR")
    name = f"CRNH0203-{year}-{station}.txt" if isinstance(station, str) else ""
    if not STATION_FILE.fullmatch(name):
        raise UscrnInputError("STATION")
    return f"{HOST}{DIRECTORY}{year}/{name}"


@dataclass(frozen=True)
class StationFile:
    year: int
    state: str
    station: str
    file_name: str


def station_file(source_url: object) -> StationFile:
    if not isinstance(source_url, str) or not source_url.startswith(HOST + DIRECTORY):
        raise UscrnInputError("SOURCE_URL")
    year, _, name = source_url[len(HOST + DIRECTORY):].partition("/")
    match = STATION_FILE.fullmatch(name)
    if match is None or match.group(1) != year:
        raise UscrnInputError("SOURCE_URL")
    return StationFile(int(year), match.group(2), f"{match.group(2)}_{match.group(3)}", name)


@dataclass(frozen=True)
class Measurement:
    variable: str
    raw: str
    value: Decimal | None
    unit: str
    derivation: str
    missing: bool
    depth_cm: int | None
    qc_flag_raw: str | None
    qc_status: str | None


@dataclass(frozen=True)
class HourlyRecord:
    wban: str
    # UTC_DATE/UTC_TIME mark the end of the hourly interval.
    interval_start_utc: str
    interval_end_utc: str
    lst_date: str
    lst_time: str
    datalogger_version: str
    longitude: Decimal | None
    latitude: Decimal | None
    surface_temperature_type: str
    measurements: tuple[Measurement, ...]
    route: str
    reasons: tuple[str, ...]
    line_number: int
    line_sha256: str


@dataclass(frozen=True)
class StationYearCandidate:
    source_url: str
    station: StationFile
    profile_id: str
    retrieved_at: str
    body_sha256: str
    wban: str
    records: tuple[HourlyRecord, ...]
    missing_hours: int
    # Parsing proves neither station-metadata validity nor completeness of the year.
    coverage: str = "NOT_ESTABLISHED"
    admission: str = "NOT_ADMITTED"


def _decimal(token: str) -> Decimal:
    if not NUMBER.fullmatch(token):
        raise UscrnInputError("VALUE_FORMAT")
    try:
        return Decimal(token)
    except InvalidOperation:
        raise UscrnInputError("VALUE_FORMAT") from None


def _time(date: str, hhmm: str) -> datetime:
    if not (re.fullmatch(r"\d{8}", date) and re.fullmatch(r"\d{4}", hhmm)):
        raise UscrnInputError("TIME_FORMAT")
    base = datetime.strptime(date, "%Y%m%d").replace(tzinfo=timezone.utc)
    hours, minutes = int(hhmm[:2]), int(hhmm[2:])
    # Accept a midnight interval end written as 2400 on the prior date or 0000 on the
    # next; both resolve to the same instant, so a file using both fails TIME_ORDER.
    if minutes != 0 or not 0 <= hours <= 24:
        raise UscrnInputError("TIME_FORMAT")
    return base + timedelta(hours=hours)


def _record(fields: list[str], line_number: int, raw_line: str) -> HourlyRecord:
    reasons: list[str] = []
    end = _time(fields[INDEX["UTC_DATE"]], fields[INDEX["UTC_TIME"]])
    measurements: list[Measurement] = []
    for column in MEASUREMENTS:
        raw = fields[INDEX[column.name]]
        missing = raw in column.missing
        value = None if missing else _decimal(raw)
        flag_raw = fields[INDEX[column.flag_column]] if column.flag_column else None
        qc_status = None
        if flag_raw is not None:
            qc_status = QC_FLAGS.get(flag_raw)
            if qc_status is None:
                reasons.append("QUALITY_UNKNOWN")
        measurements.append(Measurement(column.name, raw, value, column.unit or "",
                                        column.derivation or "", missing, column.depth_cm,
                                        flag_raw, qc_status))
    surface = SURFACE_TYPES.get(fields[INDEX["SUR_TEMP_TYPE"]])
    if surface is None:
        reasons.append("SURFACE_TEMPERATURE_TYPE_UNKNOWN")
    coordinates = []
    for name, bound in (("LONGITUDE", 180), ("LATITUDE", 90)):
        raw = fields[INDEX[name]]
        value = None if raw in PROFILE[INDEX[name]].missing else _decimal(raw)
        if value is not None and abs(value) > bound:
            raise UscrnInputError("COORDINATE_RANGE")
        coordinates.append(value)
    return HourlyRecord(
        fields[INDEX["WBANNO"]], (end - timedelta(hours=1)).isoformat().replace("+00:00", "Z"),
        end.isoformat().replace("+00:00", "Z"), fields[INDEX["LST_DATE"]],
        fields[INDEX["LST_TIME"]], fields[INDEX["CRX_VN"]], coordinates[0], coordinates[1],
        surface or "INVALID", tuple(measurements),
        "QUARANTINE_CANDIDATE" if reasons else "RAW_CANDIDATE", tuple(dict.fromkeys(reasons)),
        line_number, "sha256:" + sha256(raw_line.encode("ascii")).hexdigest())


def parse_station_year(body: bytes, *, status: int, source_url: str, retrieved_at: str,
                       max_bytes: int = 32 * 1024 * 1024,
                       max_records: int = 9000) -> StationYearCandidate:
    """Parse one supplied station-year file; reject it whole on drift or inconsistency."""
    station = station_file(source_url)
    retrieved = _utc(retrieved_at)
    if type(status) is not int or not isinstance(body, bytes) or len(body) > max_bytes:
        raise UscrnInputError("RESPONSE_BOUND")
    if status != 200:
        raise UscrnInputError("HTTP_STATUS")
    try:
        text = body.decode("ascii")
    except UnicodeDecodeError:
        raise UscrnInputError("ENCODING") from None
    records: list[HourlyRecord] = []
    wbans: set[str] = set()
    previous: str | None = None
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        fields = line.split()
        if len(fields) != len(PROFILE):
            raise UscrnInputError("SCHEMA_DRIFT")
        if len(records) >= max_records:
            raise UscrnInputError("RECORD_BOUND")
        if not re.fullmatch(r"\d{5}", fields[0]):
            raise UscrnInputError("STATION_ID")
        if fields[INDEX["LST_DATE"]][:4] != str(station.year):
            raise UscrnInputError("RECORD_OUTSIDE_FILE_YEAR")
        record = _record(fields, line_number, line)
        if previous is not None and record.interval_end_utc <= previous:
            raise UscrnInputError("TIME_ORDER")
        previous = record.interval_end_utc
        wbans.add(record.wban)
        records.append(record)
    if not records:
        raise UscrnInputError("EMPTY_FILE")
    if len(wbans) != 1:
        raise UscrnInputError("MIXED_STATIONS")
    first = datetime.fromisoformat(records[0].interval_end_utc.replace("Z", "+00:00"))
    last = datetime.fromisoformat(records[-1].interval_end_utc.replace("Z", "+00:00"))
    expected = int((last - first) / timedelta(hours=1)) + 1
    return StationYearCandidate(source_url, station, PROFILE_ID, retrieved,
                                "sha256:" + sha256(body).hexdigest(), wbans.pop(),
                                tuple(records), expected - len(records))
