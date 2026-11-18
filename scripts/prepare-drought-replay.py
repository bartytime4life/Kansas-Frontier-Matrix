#!/usr/bin/env python3
"""Build the bounded Finney County replay from saved provider responses."""

import argparse
import csv
import hashlib
import io
import json
import math
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import urlencode

START = date(2012, 6, 5)
LAST_MAP = date(2012, 9, 25)
END = date(2012, 10, 1)
COUNTY = "20055"
STATION = "USGS-07139000"
SERIES = "1d41eba3a3a84af7b0e76139c087c5b2"
DROUGHT_QUERY = (
    "https://usdmdataservices.unl.edu/api/CountyStatistics/GetDroughtSeverityStatisticsByAreaPercent?"
    + urlencode({"aoi": COUNTY, "startdate": "6/5/2012", "enddate": "9/25/2012", "statisticsType": 1})
)
FLOW_QUERY = (
    "https://api.waterdata.usgs.gov/ogcapi/v0/collections/daily/items?"
    + urlencode({
        "monitoring_location_id": STATION, "parameter_code": "00060", "statistic_id": "00003",
        "time": f"{START}/{END}", "limit": 150, "f": "json",
    })
)


def calendar(start, end, step=1):
    return [(start + timedelta(days=offset)).isoformat()
            for offset in range(0, (end - start).days + 1, step)]


def drought_rows(raw):
    rows = []
    for row in csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))):
        start = date.fromisoformat(row["ValidStart"])
        end = date.fromisoformat(row["ValidEnd"])
        shares = [float(row[f"D{level}"]) for level in range(5)]
        if ((row["FIPS"], row["County"], row["State"], row["StatisticFormatID"])
                != (COUNTY, "Finney County", "KS", "1")
                or start.strftime("%Y%m%d") != row["MapDate"]
                or end - start != timedelta(days=6)
                or not all(0 <= share <= 100 for share in shares)
                or shares != sorted(shares, reverse=True)):
            raise ValueError(f"Unexpected county statistic on {start}")
        rows.append({"validFrom": start.isoformat(), "validThrough": end.isoformat(), "shares": shares})
    rows.sort(key=lambda row: row["validFrom"])
    if [row["validFrom"] for row in rows] != calendar(START, LAST_MAP, 7):
        raise ValueError("Expected one Finney County record for each of the 17 map dates")
    return rows


def flow_rows(raw):
    response = json.loads(raw)
    features = response["features"]
    if (response["type"] != "FeatureCollection" or response["numberReturned"] != len(features)
            or any(link["rel"] == "next" for link in response["links"])):
        raise ValueError("Incomplete daily values response")
    rows = []
    for feature in features:
        record = feature["properties"]
        value = float(record["value"])
        if (record["monitoring_location_id"] != STATION or record["time_series_id"] != SERIES
                or (record["parameter_code"], record["statistic_id"]) != ("00060", "00003")
                or record["unit_of_measure"] != "ft^3/s" or record["approval_status"] != "Approved"
                or record["qualifier"] is not None or not math.isfinite(value) or value < 0):
            raise ValueError(f"Unexpected daily mean on {record['time']}")
        rows.append({"date": record["time"], "value": value, "id": feature["id"]})
    rows.sort(key=lambda row: row["date"])
    if ([row["date"] for row in rows] != calendar(START, END)
            or len({row["id"] for row in rows}) != len(rows)):
        raise ValueError("Expected 119 unique daily means covering the whole replay")
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("county_csv", type=Path)
    parser.add_argument("daily_json", type=Path)
    parser.add_argument("retrieved_at", help="ISO timestamp for this capture")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    timestamp = datetime.fromisoformat(args.retrieved_at)
    if timestamp.utcoffset() is None:
        raise ValueError("Capture time must include an offset")
    county, daily = args.county_csv.read_bytes(), args.daily_json.read_bytes()
    output = {
        "format": "kfm-finney-drought-replay-v1",
        "retrievedAt": args.retrieved_at,
        "county": {"name": "Finney County, Kansas", "fips": COUNTY},
        "station": {
            "name": "Arkansas River at Garden City, Kansas", "id": STATION, "seriesId": SERIES,
            "parameter": "00060", "statistic": "00003", "unit": "ft³/s", "approval": "Approved",
        },
        "sources": {
            "drought": {"url": DROUGHT_QUERY, "sha256": hashlib.sha256(county).hexdigest()},
            "flow": {"url": FLOW_QUERY, "sha256": hashlib.sha256(daily).hexdigest()},
        },
        "weeks": drought_rows(county),
        "dailyFlow": flow_rows(daily),
    }
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
