#!/usr/bin/env python3
"""Prepare the fixed USGS Sedgwick nitrate investigation from public WQP data."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from datetime import date, datetime, timezone
from decimal import Decimal
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 500_000
SITE = "USGS-07144100"
QUERY_ROOT = "https://waterqualitydata.us/data/"
RESULT_URL = QUERY_ROOT + "Result/search?" + urlencode({
    "siteid": SITE, "characteristicName": "Nitrate",
    "startDateLo": "01-01-2019", "startDateHi": "12-31-2022",
    "mimeType": "csv", "zip": "no", "sorted": "yes",
})
STATION_URL = QUERY_ROOT + "Station/search?" + urlencode({"siteid": SITE, "mimeType": "csv", "zip": "no"})
STATION_PAGE = "https://waterdata.usgs.gov/monitoring-location/USGS-07144100/"
WQP_PAGE = "https://waterqualitydata.us/provider/NWIS/USGS-KS/USGS-07144100/"
RIGHTS_PAGE = "https://www.usgs.gov/information-policies-and-instructions/acknowledging-or-crediting-usgs"
PERIODS = (
    {"id": "earlier", "label": "2019–2020", "from": "2019-01-01", "to": "2020-12-31"},
    {"id": "later", "label": "2021–2022", "from": "2021-01-01", "to": "2022-12-31"},
)
CONTEXT = {
    "OrganizationIdentifier": "USGS-KS",
    "MonitoringLocationIdentifier": SITE,
    "ProviderName": "NWIS",
    "CharacteristicName": "Nitrate",
    "ActivityTypeCode": "Sample-Routine",
    "ActivityMediaName": "Water",
    "ActivityMediaSubdivisionName": "Surface Water",
    "ResultSampleFractionText": "Dissolved",
    "USGSPCode": "00618",
    "ResultAnalyticalMethod/MethodIdentifier": "ALGOR",
    "ResultAnalyticalMethod/MethodIdentifierContext": "USGS",
    "ResultAnalyticalMethod/MethodName": "Computation by NWIS algorithm",
    "SampleCollectionMethod/MethodIdentifier": "15",
    "SampleCollectionMethod/MethodIdentifierContext": "USGS parameter code 82398",
    "SampleCollectionEquipmentName": "US DH-81",
    "ResultStatusIdentifier": "Accepted",
    "ResultValueTypeName": "Actual",
    "ResultWeightBasisText": "",
    "ResultTimeBasisText": "",
    "ResultTemperatureBasisText": "",
    "ResultParticleSizeBasisText": "",
    "StatisticalBaseCode": "",
}
UNIT = "mg/l as N"
VALUE = "ResultMeasureValue"
VALUE_UNIT = "ResultMeasure/MeasureUnitCode"
LIMIT = "DetectionQuantitationLimitMeasure/MeasureValue"
LIMIT_UNIT = "DetectionQuantitationLimitMeasure/MeasureUnitCode"
DETECTION = "ResultDetectionConditionText"
QUALIFIER = "MeasureQualifierCode"


def read_csv(url, stem, cache, offline):
    raw_path, receipt_path = cache / f"{stem}.csv", cache / f"{stem}.json"
    if offline:
        raw, receipt = raw_path.read_bytes(), json.loads(receipt_path.read_text())
    else:
        request = Request(url, headers={"User-Agent": "KFM public research snapshot", "Accept": "text/csv"})
        with urlopen(request, timeout=30) as response:
            if response.status != 200 or response.geturl() != url:
                raise ValueError(f"Unexpected provider response for {stem}: {response.status}, {response.geturl()}")
            raw = response.read(MAX_BYTES + 1)
        receipt = {
            "url": url, "retrievedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "rawBytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
        }
    if (
        not raw or len(raw) > MAX_BYTES or receipt["url"] != url
        or receipt["rawBytes"] != len(raw) or receipt["sha256"] != hashlib.sha256(raw).hexdigest()
    ):
        raise ValueError(f"Provider receipt mismatch for {stem}")
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig"), newline=""), strict=True)
    if len(reader.fieldnames or []) != len(set(reader.fieldnames or [])):
        raise ValueError(f"Duplicate CSV headers in {stem}")
    rows = list(reader)
    if not rows or any(not all(isinstance(k, str) and isinstance(v, str) for k, v in row.items()) for row in rows):
        raise ValueError(f"Unexpected source rows in {stem}")
    if not offline:
        raw_path.write_bytes(raw)
        receipt_path.write_text(json.dumps(receipt, sort_keys=True) + "\n")
    return rows, receipt


def decimal_text(value):
    return bool(re.fullmatch(r"\d+(?:\.\d+)?", value)) and Decimal(value).is_finite()


def qualify(row):
    if any(row.get(key) != value for key, value in CONTEXT.items()):
        return "other-context"
    if row[QUALIFIER]:
        return "qualified-other"
    if row[DETECTION] == "Not Detected" and not row[VALUE] and row[LIMIT_UNIT] == UNIT and decimal_text(row[LIMIT]):
        return "not-detected"
    if not row[DETECTION] and row[VALUE_UNIT] == UNIT and decimal_text(row[VALUE]):
        return "numeric"
    return "qualified-other"


def build(result_rows, station_rows, receipts):
    if len(station_rows) != 1:
        raise ValueError("Expected one station result")
    station = station_rows[0]
    if (
        (station["MonitoringLocationIdentifier"], station["StateCode"], station["CountyCode"], station["ProviderName"],
         station["HorizontalCoordinateReferenceSystemDatumName"]) != (SITE, "20", "173", "NWIS", "NAD83")
        or not 37 <= float(station["LatitudeMeasure"]) < 40
        or not -103 < float(station["LongitudeMeasure"]) < -94
    ):
        raise ValueError("Station identity or Kansas coordinates changed")
    periods = [dict(period, returned=0, otherContext=0, qualifiedOther=0) for period in PERIODS]
    records = []
    seen = set()
    for row in result_rows:
        observed = row["ActivityStartDate"]
        if date.fromisoformat(observed).isoformat() != observed:
            raise ValueError(f"Noncanonical sample date: {observed}")
        period = next((item for item in periods if item["from"] <= observed <= item["to"]), None)
        if period is None or row["MonitoringLocationIdentifier"] != SITE or row["CharacteristicName"] != "Nitrate":
            raise ValueError("Result outside the source query bounds")
        period["returned"] += 1
        status = qualify(row)
        if status in {"other-context", "qualified-other"}:
            key = {"other-context": "otherContext", "qualified-other": "qualifiedOther"}[status]
            period[key] += 1
            continue
        identity = row["ActivityIdentifier"]
        if not re.fullmatch(r"nwisks\.01\.\d+", identity) or identity in seen:
            raise ValueError(f"Missing or duplicate provider activity identifier: {identity}")
        seen.add(identity)
        records.append({"activityId": identity, "period": period["id"], "status": status, "source": row})
    if not all(sum(record["period"] == period["id"] and record["status"] == "numeric" for record in records) >= 10 for period in periods):
        raise ValueError("Each window must retain enough numeric samples to show a useful distribution")
    records.sort(key=lambda record: (record["source"]["ActivityStartDate"], record["activityId"]))
    return {
        "format": "kfm-water-chemistry-v1",
        "station": {
            "id": SITE, "name": "Little Arkansas River near Sedgwick, Kansas",
            "latitude": station["LatitudeMeasure"], "longitude": station["LongitudeMeasure"],
            "datum": station["HorizontalCoordinateReferenceSystemDatumName"],
            "horizontalAccuracy": station["HorizontalAccuracyMeasure/MeasureValue"],
            "horizontalAccuracyUnit": station["HorizontalAccuracyMeasure/MeasureUnitCode"],
            "url": STATION_PAGE, "providerUrl": WQP_PAGE,
        },
        "context": CONTEXT,
        "unit": UNIT,
        "periods": periods,
        "records": records,
        "sources": receipts,
        "credit": {"name": "U.S. Geological Survey, Kansas Water Science Center via Water Quality Portal", "rightsUrl": RIGHTS_PAGE},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=ROOT / "work/labs-raw/water-chemistry")
    parser.add_argument("--output", type=Path, default=ROOT / "app/labs/water-chemistry/water-snapshot.json")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    results, result_receipt = read_csv(RESULT_URL, "nitrate", args.cache, args.offline)
    stations, station_receipt = read_csv(STATION_URL, "station", args.cache, args.offline)
    snapshot = build(results, stations, {"results": result_receipt, "station": station_receipt})
    args.output.write_text(json.dumps(snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
    print(f"{len(results)} source rows, {len(snapshot['records'])} retained")


if __name__ == "__main__":
    main()
