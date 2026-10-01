"""Source-specific 1991–2020 monthly NOAA normals parsing; no release authority.

The public NODD bucket contains a fixed-width station inventory and one CSV per
station. These are station aggregates, never a continuous climate surface or a
current weather observation. Keep raw bytes and NOAA's value flags in the
capture; this module projects only monthly mean temperature and precipitation.
"""
from __future__ import annotations

import csv
from decimal import Decimal, InvalidOperation
from hashlib import sha256
from io import StringIO
import re

BUCKET = "https://noaa-normals-pds.s3.amazonaws.com"
PREFIX = "normals-monthly/1991-2020"
INVENTORY_KEY = f"{PREFIX}/doc/inventory_30yr.txt"
PROFILE = "kfm.noaa-monthly-normals-1991-2020/v1"
STATION_ID = re.compile(r"[A-Za-z0-9_]{11}\Z")
ELEMENTS = {"temperature_f": "MLY-TAVG-NORMAL", "precipitation_in": "MLY-PRCP-NORMAL"}
FLAGS = frozenset({"S", "R", "P", "E"})
MEASUREMENT_FLAGS = frozenset({"", "M", "V", "W", "X", "Y", "Z"})


class NormalsError(ValueError):
    """Safe, non-payload-bearing source validation error."""


def object_url(key: str) -> str:
    if key == INVENTORY_KEY:
        return f"{BUCKET}/{key}"
    if not isinstance(key, str) or not key.startswith(f"{PREFIX}/access/"):
        raise NormalsError("OBJECT_KEY_SCOPE")
    station = key.removeprefix(f"{PREFIX}/access/").removesuffix(".csv")
    if key != station_key(station):
        raise NormalsError("OBJECT_KEY_SCOPE")
    return f"{BUCKET}/{key}"


def station_key(station_id: str) -> str:
    if not isinstance(station_id, str) or STATION_ID.fullmatch(station_id) is None:
        raise NormalsError("STATION_ID")
    return f"{PREFIX}/access/{station_id}.csv"


def _number(token: str, code: str) -> Decimal:
    try:
        value = Decimal(token.strip())
        if not value.is_finite():
            raise ValueError
        return value
    except (InvalidOperation, ValueError):
        raise NormalsError(code) from None


def parse_inventory(raw: bytes) -> tuple[dict, ...]:
    if not isinstance(raw, bytes) or not 0 < len(raw) <= 2 * 1024 * 1024:
        raise NormalsError("INVENTORY_SIZE")
    try:
        lines = raw.decode("utf-8-sig").splitlines()
    except UnicodeDecodeError:
        raise NormalsError("INVENTORY_ENCODING") from None
    if not 1 <= len(lines) <= 25000:
        raise NormalsError("INVENTORY_ROWS")
    stations, seen = [], set()
    for line in lines:
        if len(line) < 42 or len(line) > 120:
            raise NormalsError("INVENTORY_LAYOUT")
        station_id, state = line[:11], line[38:40]
        if STATION_ID.fullmatch(station_id) is None or station_id in seen:
            raise NormalsError("INVENTORY_STATION_ID")
        seen.add(station_id)
        if state != "KS":
            continue
        latitude = _number(line[12:20], "INVENTORY_LATITUDE")
        longitude = _number(line[21:30], "INVENTORY_LONGITUDE")
        if not 36 <= latitude <= 41 or not -103 <= longitude <= -94:
            raise NormalsError("KANSAS_LOCATION")
        stations.append({"station_id": station_id, "state": state,
                         "latitude": str(latitude), "longitude": str(longitude),
                         "name": line[41:71].strip()})
    if not stations or len(stations) > 1000:
        raise NormalsError("KANSAS_STATION_COUNT")
    return tuple(sorted(stations, key=lambda item: item["station_id"]))


def _element(row: dict[str, str], name: str) -> dict | None:
    if name not in row:
        return None  # Some stations publish precipitation but no temperature.
    token = row[name].strip()
    measurement = row.get(f"meas_flag_{name}", "").strip()
    completeness = row.get(f"comp_flag_{name}", "").strip()
    years = row.get(f"years_{name}", "").strip()
    if measurement not in MEASUREMENT_FLAGS:
        raise NormalsError("MEASUREMENT_FLAG")
    if token in {"", "-9999", "-9999.0"}:
        if completeness or years:
            raise NormalsError("MISSING_VALUE_FLAGS")
        return {"value": None, "raw": token, "measurement_flag": measurement,
                "completeness_flag": None, "years": None}
    value = _number(token, "NORMAL_VALUE")
    if completeness not in FLAGS or not years.isdigit() or not 2 <= int(years) <= 30:
        raise NormalsError("COMPLETENESS_FLAGS")
    if name == "MLY-PRCP-NORMAL" and not 0 <= value <= 100:
        raise NormalsError("PRECIPITATION_RANGE")
    if name == "MLY-TAVG-NORMAL" and not -80 <= value <= 140:
        raise NormalsError("TEMPERATURE_RANGE")
    return {"value": str(value), "raw": token, "measurement_flag": measurement,
            "completeness_flag": completeness, "years": int(years)}


def parse_station(raw: bytes, station: dict) -> dict:
    if not isinstance(raw, bytes) or not 0 < len(raw) <= 128 * 1024:
        raise NormalsError("STATION_SIZE")
    try:
        text = raw.decode("utf-8-sig")
        reader = csv.DictReader(StringIO(text, newline=""), strict=True)
        rows = list(reader)
    except (UnicodeDecodeError, csv.Error):
        raise NormalsError("STATION_CSV") from None
    if len(rows) != 12 or not reader.fieldnames or len(reader.fieldnames) > 500:
        raise NormalsError("MONTH_COUNT")
    required = {"STATION", "DATE", "LATITUDE", "LONGITUDE", "NAME", "month"}
    if not required.issubset(reader.fieldnames) or len(reader.fieldnames) != len(set(reader.fieldnames)):
        raise NormalsError("STATION_COLUMNS")
    months = []
    for index, row in enumerate(rows, 1):
        month = f"{index:02d}"
        if (None in row or row["STATION"] != station["station_id"] or
                row["DATE"] != month or row["month"] != month or
                not row["NAME"].strip().endswith(", KS US")):
            raise NormalsError("STATION_IDENTITY_OR_MONTH")
        if (abs(_number(row["LATITUDE"], "STATION_LATITUDE") - Decimal(station["latitude"])) > Decimal("0.001")
                or abs(_number(row["LONGITUDE"], "STATION_LONGITUDE") - Decimal(station["longitude"])) > Decimal("0.001")):
            raise NormalsError("STATION_LOCATION_MISMATCH")
        months.append({"month": index, **{label: _element(row, column)
                                           for label, column in ELEMENTS.items()}})
    return {"station_id": station["station_id"], "name": rows[0]["NAME"].strip(),
            "state": "KS", "latitude": station["latitude"], "longitude": station["longitude"],
            "period": "1991-2020", "source_role": "aggregate", "months": months,
            "source_sha256": "sha256:" + sha256(raw).hexdigest()}
