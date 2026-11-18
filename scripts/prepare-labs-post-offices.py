#!/usr/bin/env python3
"""Derive the Douglas County postal timeline from the published original CSV.

Pass the pinned Harvard Dataverse original and the actual retrieval timestamp.
Keep the original CSV outside the application checkout.
"""

import argparse
import csv
import hashlib
import io
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COUNTY = "DOUGLAS"
FIPS = "20045"
RAW_BYTES = 31_415_567
RAW_SHA256 = "b860791be2542d9da6224c4fc91801e1fbe2236fbf98cd0f22751e9c7ae83499"
SOURCE_URL = "https://dataverse.harvard.edu/api/access/datafile/4491713?format=original"
BOUNDARY_SNAPSHOT = ROOT / "public/labs-data/census-mosaic-a3c82ebd5d89619c.json"
DESTINATION = ROOT / "app/labs/ghost-towns/post-office-snapshot.json"


def optional_year(value):
    if value == "":
        return None
    year = int(value)
    if not 1800 <= year <= 2000:
        raise ValueError(f"Unexpected Douglas County year: {year}")
    return year


def source_boolean(value):
    return {"TRUE": True, "FALSE": False, "": None}[value]


def county_records(raw):
    records = []
    rows = csv.DictReader(io.StringIO(raw.decode("utf-8-sig"), newline=""))
    for row in rows:
        counties = [row[f"County{index}"] for index in range(1, 4) if row[f"County{index}"]]
        if row["State"] != "KS" or COUNTY not in counties:
            continue
        location = None
        if row["Coordinates"] == "TRUE" and row["GNIS.Match"] == "TRUE":
            lon, lat = float(row["Longitude"]), float(row["Latitude"])
            if not (-103 <= lon <= -94 and 36 <= lat <= 41 and row["GNIS.State"] == "KS"):
                raise ValueError("Matched landmark fell outside the Kansas location profile")
            location = {"longitude": lon, "latitude": lat, "gnisId": row["GNIS.FEATURE_ID"],
                        "gnisName": row["GNIS.OrigName"], "gnisCounty": row["GNIS.County"]}
        established, discontinued = optional_year(row["Established"]), optional_year(row["Discontinued"])
        if established is not None and discontinued is not None and established > discontinued:
            raise ValueError(f"Reversed source dates for record {row['ID']}")
        records.append({
            "id": row["ID"], "name": row["OrigName"] or row["Name"], "alternateName": row["AltName"] or None,
            "counties": counties, "established": established, "discontinued": discontinued,
            "continuous": source_boolean(row["Continuous"]), "location": location,
        })
    if len(records) != 59 or len({record["id"] for record in records}) != 59:
        raise ValueError("County rows no longer match the exact reviewed source scope")
    return sorted(records, key=lambda record: (record["name"], int(record["id"])))


def build(path, retrieved_at):
    if datetime.fromisoformat(retrieved_at).utcoffset() is None:
        raise ValueError("Supply an ISO timestamp with a timezone")
    with path.open("rb") as source:
        raw = source.read(RAW_BYTES + 1)
    if len(raw) != RAW_BYTES or hashlib.sha256(raw).hexdigest() != RAW_SHA256:
        raise ValueError("Expected the pinned original us-post-offices.csv, Harvard Dataverse file 4491713")
    records = county_records(raw)
    boundary_raw = BOUNDARY_SNAPSHOT.read_bytes()
    boundary_bundle = json.loads(boundary_raw)
    boundary_source = next(source for source in boundary_bundle["data"]["sourceSnapshots"] if
                           source["url"].startswith("https://tigerweb.geo.census.gov/"))
    boundary = next(record["geometry"] for record in boundary_bundle["data"]["records"] if record["fips"] == FIPS)
    if boundary["type"] != "Polygon" or len(boundary["coordinates"]) != 1:
        raise ValueError("Douglas County context must be a single polygon ring")
    return {
        "format": "kfm-post-office-history-v1",
        "scope": {"county": "Douglas County", "state": "Kansas", "fips": FIPS,
                  "selection": "Every source row labeled KS with DOUGLAS in County1, County2 or County3"},
        "source": {
            "title": "US Post Offices", "authors": "Cameron Blevins and Richard W. Helbock", "edition": "V1 (2021)",
            "doi": "https://doi.org/10.7910/DVN/NUKCNA", "url": SOURCE_URL, "bytes": RAW_BYTES, "sha256": RAW_SHA256,
            "retrievedAt": retrieved_at, "license": "CC0 1.0", "licenseUrl": "https://creativecommons.org/publicdomain/zero/1.0/",
            "methodUrl": "https://cblevins.github.io/us-post-offices/data-biography/",
            "dictionaryUrl": "https://dataverse.harvard.edu/api/access/datafile/4491716?format=original",
        },
        "boundary": {
            "label": "Contemporary county outline", "source": "U.S. Census Bureau TIGERweb",
            "bundleSha256": hashlib.sha256(boundary_raw).hexdigest(), **boundary_source,
            "ring": boundary["coordinates"][0],
        },
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("--retrieved-at", required=True)
    parser.add_argument("--output", type=Path, default=DESTINATION)
    args = parser.parse_args()
    snapshot = build(args.original, args.retrieved_at)
    args.output.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
