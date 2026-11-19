#!/usr/bin/env python3
"""Build bounded public Kansas ACS county snapshots without an API key.

Uses official Census bulk summary files, not keyed API data queries. Raw federal
responses and SHA-256 acquisition receipts stay in /tmp/kfm-labs-county-raw.
--offline verifies receipts and rebuilds identical shipping bytes.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import math
import re
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://www2.census.gov/programs-surveys/acs/summary_file/"
VINTAGES = (2014, 2019, 2024)
PREFIX_BYTES = 2_097_152
MAX_RAW = 16_000_000
MAX_BUNDLE = 3_000_000
METHOD = "https://www2.census.gov/programs-surveys/acs/tech_docs/accuracy/2023_ACS_Accuracy_Document_Worked_Examples.pdf"
RIGHTS = "https://www.census.gov/about/policies/open-gov/open-data.html"
GEO_URL = "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer/1/query?" + urlencode({
    "where": "STATE='20'", "outFields": "GEOID,NAME", "outSR": "4326", "f": "geojson", "geometryPrecision": "3", "maxAllowableOffset": "0.015", "returnGeometry": "true"})

# Stable detailed-table cells; unlike profile variable numbers, their meanings
# are verified from each vintage's actual lookup and current table metadata.
CELLS = {
    "medianIncome": ("B19013", 1, "Median household income", "vintage-year dollars"),
    "medianAge": ("B01002", 1, "Median age", "years"),
    "povertyPopulation": ("B17001", 1, "Population for whom poverty status is determined", "people"),
    "belowPoverty": ("B17001", 2, "People below poverty level", "people"),
    "adult25Population": ("B15003", 1, "Population age 25 and over", "people"),
    "bachelors": ("B15003", 22, "Bachelor's degree", "people"),
    "masters": ("B15003", 23, "Master's degree", "people"),
    "professional": ("B15003", 24, "Professional school degree", "people"),
    "doctorate": ("B15003", 25, "Doctorate degree", "people"),
    "civilianLaborForce": ("B23025", 3, "Civilian labor force age 16 and over", "people"),
    "unemployed": ("B23025", 5, "Unemployed civilian labor force", "people"),
    "occupiedUnits": ("B25003", 1, "Occupied housing units", "housing units"),
    "ownerUnits": ("B25003", 2, "Owner-occupied housing units", "housing units"),
    "housingUnits": ("B25002", 1, "Housing units", "housing units"),
    "vacantUnits": ("B25002", 3, "Vacant housing units", "housing units"),
    "medianHomeValue": ("B25077", 1, "Median owner-occupied home value", "vintage-year dollars"),
    "medianRent": ("B25064", 1, "Median monthly gross rent", "vintage-year dollars/month"),
}
PROPORTIONS = {
    "povertyPct": ("belowPoverty", "povertyPopulation", "People below poverty level"),
    "educationPct": ("bachelorsOrHigher", "adult25Population", "Age 25+ with bachelor's degree or higher"),
    "unemploymentPct": ("unemployed", "civilianLaborForce", "Civilian unemployment rate, age 16+"),
    "ownerOccupiedPct": ("ownerUnits", "occupiedUnits", "Owner-occupied share of occupied housing"),
    "vacancyPct": ("vacantUnits", "housingUnits", "Vacant share of housing units"),
}
SENTINELS = {str(-int(str(n) * 9)) for n in range(2, 10)} | {"", ".", "-", "**", "***", "*****", "(X)", "N", "null"}


def encoded(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


class Fetcher:
    def __init__(self, cache, offline=False):
        self.cache, self.offline = cache, offline
        cache.mkdir(parents=True, exist_ok=True)

    def get(self, url, byte_range=None):
        if urlparse(url).scheme != "https" or not re.search(r"(?:^|\.)census\.gov$", urlparse(url).hostname or ""):
            raise ValueError("Only official public Census HTTPS sources are permitted")
        key = sha((url + ("\nRange:" + byte_range if byte_range else "")).encode())
        raw_path, meta_path = self.cache / (key + ".raw"), self.cache / (key + ".json")
        if self.offline:
            raw, meta = raw_path.read_bytes(), json.loads(meta_path.read_text())
            if meta["url"] != url or meta.get("requestRange") != byte_range or meta["rawSha256"] != sha(raw) or meta["rawBytes"] != len(raw) or len(raw) > MAX_RAW:
                raise ValueError(f"Cache receipt mismatch: {url}")
            return raw, meta
        headers = {"User-Agent": "KFM-Labs-County-Science/1.0", "Accept": "*/*"}
        if byte_range:
            headers["Range"] = byte_range
        with urlopen(Request(url, headers=headers), timeout=90) as response:
            if response.status != (206 if byte_range else 200):
                raise ValueError(f"Unexpected HTTP status {response.status}: {url}")
            raw = response.read(MAX_RAW + 1)
            if len(raw) > MAX_RAW:
                raise ValueError("Source response exceeds bounded acquisition")
            content_range = response.headers.get("Content-Range")
            if byte_range and not re.fullmatch(r"bytes 0-\d+/\d+", content_range or ""):
                raise ValueError("Source did not honor the requested bounded byte prefix")
            meta = {"url": url, "retrievedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"), "rawSha256": sha(raw),
                    "rawBytes": len(raw), "lastModified": response.headers.get("Last-Modified"), "httpStatus": response.status,
                    "requestRange": byte_range, "contentRange": content_range,
                    "hashScope": "exact returned byte prefix, not entire national table" if byte_range else "entire response"}
        raw_path.write_bytes(raw)
        meta_path.write_bytes(encoded(meta))
        return raw, meta


def source(name, url, citation):
    return {"name": name, "url": url, "citation": citation,
            "license": "U.S. government public-domain statistical data (17 USC 105); credit Census; no warranty or endorsement. Open data policy: " + RIGHTS}


def numeric(value):
    text = "" if value is None else str(value).strip()
    if text in SENTINELS:
        return None
    number = float(text)
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"Unexpected ACS value/sentinel: {value!r}")
    return int(number) if number.is_integer() else number


def proportion(numerator, denominator, numerator_moe, denominator_moe):
    """Census worked examples pp.5–7, using MOEs directly, all at 90%.

    Subset proportion MOE = 100 / Y * sqrt(MOE_X² - P² MOE_Y²).
    When the radical is negative, use the general ratio plus-sign formula.
    Missing inputs stay missing; missing MOE does not erase a usable estimate.
    """
    if numerator is None or denominator is None or denominator <= 0:
        return None, None, "unavailable denominator or numerator"
    if not 0 <= numerator <= denominator:
        raise ValueError("Derived subset numerator exceeds its own denominator")
    p = numerator / denominator
    if numerator_moe is None or denominator_moe is None:
        return 100 * p, None, "component MOE unavailable"
    radical = numerator_moe ** 2 - p ** 2 * denominator_moe ** 2
    method = "Census subset proportion approximation"
    if radical < 0:
        radical = numerator_moe ** 2 + p ** 2 * denominator_moe ** 2
        method = "Census general ratio fallback (negative subset radical)"
    return 100 * p, 100 * math.sqrt(radical) / denominator, method


def old_year(fetch, year, expected):
    lookup_url = BASE + f"{year}/documentation/user_tools/ACS_5yr_Seq_Table_Number_Lookup.txt"
    lookup_raw, lookup_meta = fetch.get(lookup_url)
    lookup = list(csv.DictReader(io.StringIO(lookup_raw.decode("cp1252"))))
    tables = {row["Table ID"]: row for row in lookup if row["Table ID"] in {cell[0] for cell in CELLS.values()} and row["Start Position"].strip()}
    if len(tables) != 9:
        raise ValueError("Required ACS detailed table absent from vintage lookup")
    base = BASE + f"{year}/data/5_year_seq_by_state/Kansas/All_Geographies_Not_Tracts_Block_Groups/"
    geo_raw, geo_meta = fetch.get(base + f"g{year}5ks.csv")
    geo = {}
    for row in csv.reader(io.StringIO(geo_raw.decode("cp1252"))):
        if row[2:4] != ["050", "00"]:
            continue
        fips = row[9] + row[10]
        if fips not in expected or not row[48].endswith(fips) or fips in {g[0] for g in geo.values()}:
            raise ValueError("ACS geography/FIPS mismatch or duplicate")
        geo[row[4]] = (fips, row[49])
    if {g[0] for g in geo.values()} != expected:
        raise ValueError("ACS vintage does not contain exactly the 105 Kansas counties")
    sequences = sorted({row["Sequence Number"].zfill(4) for row in tables.values()})
    with ThreadPoolExecutor(max_workers=4) as pool:
        replies = list(pool.map(fetch.get, [base + f"{year}5ks{seq}000.zip" for seq in sequences]))
    records = {fips: {"fips": fips, "sourceName": name, "sourceFlags": {}} for fips, name in geo.values()}
    for sequence, (raw, _) in zip(sequences, replies):
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            for kind in ("e", "m"):
                member = f"{kind}{year}5ks{sequence}000.txt"
                if archive.getinfo(member).file_size > 50_000_000:
                    raise ValueError("Uncompressed sequence exceeds bound")
                with archive.open(member) as stream:
                    count = 0
                    for item in csv.reader(io.TextIOWrapper(stream, encoding="ascii")):
                        if item[5] not in geo:
                            continue
                        count += 1
                        fips = geo[item[5]][0]
                        for key, (table, line, _, _) in CELLS.items():
                            definition = tables[table]
                            if definition["Sequence Number"].zfill(4) != sequence:
                                continue
                            cell = item[int(definition["Start Position"]) - 1 + line - 1]
                            target = key + ("Moe" if kind == "m" else "")
                            records[fips][target] = numeric(cell)
                            if records[fips][target] is None:
                                records[fips]["sourceFlags"][target] = cell
                    if count != 105:
                        raise ValueError("Missing or repeated county observations in ACS sequence")
    definitions = {key: {"estimate": f"{table}_{line:03d}E", "moe": f"{table}_{line:03d}M", "table": tables[table]["Table Title"]}
                   for key, (table, line, _, _) in CELLS.items()}
    return records, [lookup_meta, geo_meta] + [meta for _, meta in replies], definitions


def recent_year(fetch, expected):
    tables = sorted({cell[0] for cell in CELLS.values()})
    data_base = BASE + "2024/table-based-SF/data/5YRData/"
    jobs = [(data_base + f"acsdt5y2024-{table.lower()}.dat", f"bytes=0-{PREFIX_BYTES - 1}") for table in tables]
    with ThreadPoolExecutor(max_workers=4) as pool:
        replies = list(pool.map(lambda pair: fetch.get(*pair), jobs))
    records = {fips: {"fips": fips, "sourceFlags": {}} for fips in expected}
    for table, (raw, _) in zip(tables, replies):
        # A bounded prefix can end mid-record; only complete lines are parsed.
        text = raw.rsplit(b"\n", 1)[0].decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(text), delimiter="|")
        seen = set()
        for row in reader:
            if not re.fullmatch(r"0500000US20\d{3}", row["GEO_ID"]):
                continue
            fips = row["GEO_ID"][-5:]
            if fips not in expected or fips in seen:
                raise ValueError("County table contains unexpected or repeated FIPS")
            seen.add(fips)
            for key, (cell_table, line, _, _) in CELLS.items():
                if cell_table != table:
                    continue
                for kind, suffix in (("E", ""), ("M", "Moe")):
                    value = row[f"{table}_{kind}{line:03d}"]
                    records[fips][key + suffix] = numeric(value)
                    if records[fips][key + suffix] is None:
                        records[fips]["sourceFlags"][key + suffix] = value
        if seen != expected:
            raise ValueError(f"Byte prefix does not include all 105 Kansas counties: {table}; increase the explicit prefix bound before rebuilding")
    definitions = {key: {"estimate": f"{table}_{line:03d}E", "moe": f"{table}_{line:03d}M"} for key, (table, line, _, _) in CELLS.items()}
    return records, [meta for _, meta in replies], definitions


def build(fetch):
    geo_raw, geo_meta = fetch.get(GEO_URL)
    geo = json.loads(geo_raw)
    if geo.get("exceededTransferLimit") or len(geo.get("features", [])) != 105:
        raise ValueError("Census county boundary selection incomplete")
    counties = {feature["properties"]["GEOID"]: feature for feature in geo["features"]}
    if len(counties) != 105 or any(not re.fullmatch(r"20\d{3}", key) for key in counties):
        raise ValueError("Invalid Kansas county reference")
    rows, snapshots, definitions = [], [geo_meta], {}
    for year in VINTAGES:
        records, receipts, definition = recent_year(fetch, set(counties)) if year == 2024 else old_year(fetch, year, set(counties))
        snapshots += receipts
        definitions[str(year)] = definition
        for fips, row in sorted(records.items()):
            feature = counties[fips]
            row.update(id=f"{fips}/{year}", name=feature["properties"]["NAME"].removesuffix(" County") + " County", year=year,
                       period=f"{year - 4}–{year}", geometry=feature["geometry"], moeMethods={})
            if "sourceName" in row and row["sourceName"] != row["name"] + ", Kansas":
                raise ValueError("County name does not reconcile across official sources")
            components = [row[key] for key in ("bachelors", "masters", "professional", "doctorate")]
            moes = [row[key + "Moe"] for key in ("bachelors", "masters", "professional", "doctorate")]
            row["bachelorsOrHigher"] = sum(components) if all(value is not None for value in components) else None
            row["bachelorsOrHigherMoe"] = math.sqrt(sum(value * value for value in moes)) if all(value is not None for value in moes) else None
            for key, (numerator, denominator, _) in PROPORTIONS.items():
                estimate, moe, method = proportion(row[numerator], row[denominator], row[numerator + "Moe"], row[denominator + "Moe"])
                row[key], row[key + "Moe"] = estimate, moe
                row["moeMethods"][key] = method
            rows.append(row)
    columns = [{"key": "name", "label": "County", "type": "string"}, {"key": "fips", "label": "County FIPS", "type": "string"},
               {"key": "year", "label": "ACS vintage ending year", "type": "year"}, {"key": "period", "label": "Five-year observation period", "type": "string"}]
    preferred = ["medianIncome", "medianAge", "medianHomeValue", "medianRent"]
    for key in preferred + [key for key in CELLS if key not in preferred]:
        _, _, label, unit = CELLS[key]
        columns += [{"key": key, "label": label, "type": "number", "unit": unit},
                    {"key": key + "Moe", "label": label + " — source 90% MOE", "type": "number", "unit": unit, "analysis": False, "metric": False}]
    for key, (_, _, label) in PROPORTIONS.items():
        columns += [{"key": key, "label": label, "type": "number", "unit": "%"},
                    {"key": key + "Moe", "label": label + " — approximate 90% MOE", "type": "number", "unit": "percentage points", "analysis": False, "metric": False}]
    columns += [{"key": "bachelorsOrHigher", "label": "Bachelor's degree or higher (sum)", "type": "number", "unit": "people"},
                {"key": "bachelorsOrHigherMoe", "label": "Bachelor's degree or higher — approximate sum 90% MOE", "type": "number", "unit": "people", "analysis": False, "metric": False}]
    sources = [source(f"Census ACS {year} public bulk summary file", BASE + f"{year}/", f"U.S. Census Bureau, {year - 4}–{year} ACS 5-year detailed-table estimates and 90% margins of error for all 105 Kansas counties. Exact acquisition URLs and response hashes are in sourceSnapshots.") for year in VINTAGES]
    sources += [source("Census ACS MOE approximation methods", METHOD, "Census worked examples, pp.5–7: sum MOE by root-sum-square; subset proportion MOE with general ratio fallback for negative radical. Approximations omit unavailable covariance."),
                source("Census ACS comparison guidance", "https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data.html", "Census guidance: compare non-overlapping five-year periods, account for sampling error and changing definitions; ACS period estimates differ from annual population estimates."),
                source("Census TIGERweb county boundaries", GEO_URL, "Census contemporary county boundaries simplified for display. County FIPS joins verified against every ACS input table."),
                source("Census open-data policy", RIGHTS, "Census public statistical data and associated open-data guidance.")]
    data = {"kind": "records", "records": rows, "columns": columns, "coverage": "105 Kansas counties × three non-overlapping ACS five-year periods: 2010–2014, 2015–2019, 2020–2024",
            "yearField": "year", "temporalMode": "snapshot", "categoryField": "name", "valueField": "medianIncome", "preferredView": "map",
            "sourceSnapshot": snapshots[0], "sourceSnapshots": snapshots, "sourceDefinitions": definitions, "confidenceLevel": 0.90,
            "derivedFields": {key: {"numerator": n, "denominator": d, "scale": 100, "moe": "Census subset proportion approximation; general ratio fallback when radical negative"} for key, (n, d, _) in PROPORTIONS.items()},
            "limits": ["These are sample-based ACS five-year period estimates, not an annual census or point-in-time population count. Vintage 2014 covers 2010–2014, 2019 covers 2015–2019, and 2024 covers 2020–2024.",
                       "Median income, home values and rents are expressed in each vintage's own year dollars. Across-vintage dollar differences have not been adjusted to a common price year and must not be labeled real income or purchasing-power change.",
                       "Direct source estimates and their published 90% margins of error are retained. Derived percentages use their own table denominators, not annual Population Estimates Program totals. Income, age, home-value and rent medians have different statistical universes.",
                       "Derived percentage 90% MOEs use Census's documented approximation: 100/Y × sqrt(MOE_X² − (X/Y)² MOE_Y²), using the plus-sign ratio formula when the radical is negative. Education's four component counts are summed; its numerator MOE uses root-sum-square. These approximations omit unavailable covariance and may understate or overstate sampling error.",
                       "Raw count components and their individual source MOEs remain downloadable. Source sentinel values, suppressed estimates, not-applicable values and unavailable MOEs become null with the original token retained in sourceFlags. Missing MOE never becomes zero.",
                       "To avoid downloading national tract/block-group data, 2024 uses explicit HTTP byte prefixes of official sorted table files. Every table must contain exactly the same 105 Kansas county FIPS before publication. Raw hashes bind the returned byte slices; requestRange and contentRange distinguish them from whole-file hashes.",
                       "Contemporary county shapes locate the reporting county; cross-source joins use FIPS. Small-county estimates can have large sampling error. Rank differences and cross-source correlations do not establish significance, individual circumstances or cause."]}
    return {"format": "kfm-story-bundle-v1", "story": "county-conditions", "version": 1, "built_at": max(item["retrievedAt"] for item in snapshots),
            "observed": {"from": "2010", "to": "2024"}, "sources": sources, "data": data}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=Path("/tmp/kfm-labs-county-raw"))
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    bundle = build(Fetcher(args.cache, args.offline))
    raw = encoded(bundle)
    if len(raw) > MAX_BUNDLE or len(bundle["data"]["records"]) != 315 or len(bundle["data"]["columns"]) > 60:
        raise ValueError("County bundle violates bounded story contract")
    digest = sha(raw)
    filename = f"county-conditions-{digest[:16]}.json"
    target = ROOT / "public/labs-data-observatory"
    target.mkdir(parents=True, exist_ok=True)
    (target / filename).write_bytes(raw)
    manifest = {"county-conditions": {"path": "/labs-data-observatory/" + filename, "sha256": digest, "bytes": len(raw),
                                       "observed": bundle["observed"], "retrievedAt": bundle["built_at"], "records": 315}}
    (ROOT / "app/labs/county-snapshots.mjs").write_text("// Generated from public Census responses by scripts/prepare-labs-county-data.py.\nexport const COUNTY_LAB_SNAPSHOTS = Object.freeze(" + json.dumps(manifest, indent=2) + ");\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
