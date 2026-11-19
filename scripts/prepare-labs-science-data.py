#!/usr/bin/env python3
"""Build public Energy Shift and Air Quality Labs from federal source responses.

python3 scripts/prepare-labs-science-data.py
python3 scripts/prepare-labs-science-data.py --offline

Raw responses and their acquisition receipts stay outside Git, by default in
/tmp/kfm-labs-science-raw. --offline verifies their SHA-256 before reuse. Nothing
reads a local research database, credentials, or held/private dataset.
"""
from __future__ import annotations

import argparse
import calendar
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
MAX_RAW = 50_000_000
MAX_MEMBER = 100_000_000
MAX_BUNDLE = 3_000_000
SEDS_URL = "https://www.eia.gov/opendata/bulk/SEDS.zip"
AQI_BASE = "https://aqs.epa.gov/aqsweb/airdata/"
AQI_YEARS = range(2000, 2026)  # Complete calendar years; deliberately excludes current 2026.
GEO_URL = "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer/1/query?" + urlencode({
    "where": "STATE='20'", "outFields": "GEOID,NAME", "outSR": "4326", "f": "geojson",
    "geometryPrecision": "3", "maxAllowableOffset": "0.015", "returnGeometry": "true"})
PUBLIC_DOMAIN = "U.S. government public-domain data (17 USC 105); credit the source; no warranty or endorsement."
EIA_RIGHTS = "https://www.eia.gov/about/copyrights_reuse.php"
EPA_RIGHTS = "https://edg.epa.gov/EPA_Data_License.html"

# The source's exact name and series ID are retained alongside these short labels.
# These are overlapping views of the energy system, never a list to sum together.
ENERGY_SERIES = {
    "TETCB": ("Total consumption", "Consumption", "All sectors", "All sources"),
    "CLTCB": ("Coal consumption", "Consumption", "All sectors", "Coal"),
    "NGTCB": ("Natural gas consumption", "Consumption", "All sectors", "Natural gas"),
    "PATCB": ("Petroleum consumption", "Consumption", "All sectors", "Petroleum"),
    "RETCB": ("Renewable consumption", "Consumption", "All sectors", "Renewables"),
    "WYTCB": ("Wind consumption", "Consumption", "All sectors", "Wind"),
    "SOTCB": ("Solar consumption", "Consumption", "All sectors", "Solar"),
    "HYTCB": ("Hydropower consumption", "Consumption", "All sectors", "Hydropower"),
    "GETCB": ("Geothermal consumption", "Consumption", "All sectors", "Geothermal"),
    "NUETB": ("Nuclear consumption", "Consumption", "Electricity generation", "Nuclear"),
    "BMTCB": ("Biomass consumption", "Consumption", "All sectors", "Biomass"),
    "TERCB": ("Residential consumption", "Consumption", "Residential", "All sources"),
    "TECCB": ("Commercial consumption", "Consumption", "Commercial", "All sources"),
    "TEICB": ("Industrial consumption", "Consumption", "Industrial", "All sources"),
    "TEACB": ("Transportation consumption", "Consumption", "Transportation", "All sources"),
    "TEEIB": ("Electric power consumption and net U.S. electricity imports", "Consumption", "Electric power", "All sources"),
    "TEPRB": ("Total primary production", "Production", "All sectors", "All sources"),
    "CLPRB": ("Coal production", "Production", "All sectors", "Coal"),
    "NGMPB": ("Marketed natural gas production", "Production", "All sectors", "Natural gas"),
    "PAPRB": ("Crude oil production", "Production", "All sectors", "Petroleum"),
    "WYPRB": ("Wind production", "Production", "All sectors", "Wind"),
    "SOPRB": ("Solar production", "Production", "All sectors", "Solar"),
    "HYPRB": ("Hydropower production", "Production", "All sectors", "Hydropower"),
    "NUPRB": ("Nuclear electricity production", "Production", "All sectors", "Nuclear"),
    "REPRB": ("Renewable production", "Production", "All sectors", "Renewables"),
    "WWPRB": ("Wood and waste production", "Production", "All sectors", "Wood and waste"),
}

AQI_FIELDS = {
    "daysWithAqi": ("Days with AQI", "Monitored days", "days"),
    "goodDays": ("Good Days", "Good AQI days (0–50)", "days"),
    "moderateDays": ("Moderate Days", "Moderate AQI days (51–100)", "days"),
    "sensitiveDays": ("Unhealthy for Sensitive Groups Days", "Unhealthy for sensitive groups days (101–150)", "days"),
    "unhealthyDays": ("Unhealthy Days", "Unhealthy AQI days (151–200)", "days"),
    "veryUnhealthyDays": ("Very Unhealthy Days", "Very unhealthy AQI days (201–300)", "days"),
    "hazardousDays": ("Hazardous Days", "Hazardous AQI days (301+)", "days"),
    "maxAqi": ("Max AQI", "Maximum daily AQI", "AQI"),
    "aqi90th": ("90th Percentile AQI", "90th percentile daily AQI", "AQI"),
    "medianAqi": ("Median AQI", "Median daily AQI", "AQI"),
    "coDays": ("Days CO", "CO main-pollutant days", "days"),
    "no2Days": ("Days NO2", "NO₂ main-pollutant days", "days"),
    "ozoneDays": ("Days Ozone", "Ozone main-pollutant days", "days"),
    "pm25Days": ("Days PM2.5", "PM₂.₅ main-pollutant days", "days"),
    "pm10Days": ("Days PM10", "PM₁₀ main-pollutant days", "days"),
}


def encoded(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode()


def sha(body):
    return hashlib.sha256(body).hexdigest()


class Fetcher:
    def __init__(self, cache, offline=False):
        self.cache, self.offline = cache, offline
        cache.mkdir(parents=True, exist_ok=True)

    def get(self, url):
        if urlparse(url).scheme != "https" or not re.search(r"(?:^|\.)(?:eia|epa|census)\.gov$", urlparse(url).hostname or ""):
            raise ValueError("Only named HTTPS federal sources are allowed")
        key = sha(url.encode())
        raw_path, meta_path = self.cache / (key + ".raw"), self.cache / (key + ".json")
        if self.offline:
            raw, meta = raw_path.read_bytes(), json.loads(meta_path.read_text())
            if meta["url"] != url or meta["rawSha256"] != sha(raw) or meta["rawBytes"] != len(raw) or len(raw) > MAX_RAW:
                raise ValueError(f"Cache receipt mismatch: {url}")
            return raw, meta
        with urlopen(Request(url, headers={"User-Agent": "KFM-Labs-Public-Science-Snapshot/1.0", "Accept": "*/*"}), timeout=90) as response:
            if response.status != 200:
                raise ValueError(f"HTTP {response.status}: {url}")
            raw = response.read(MAX_RAW + 1)
            if len(raw) > MAX_RAW:
                raise ValueError(f"Source exceeds acquisition bound: {url}")
            meta = {"url": url, "retrievedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "rawSha256": sha(raw), "rawBytes": len(raw), "lastModified": response.headers.get("Last-Modified")}
        raw_path.write_bytes(raw)
        meta_path.write_bytes(encoded(meta))
        return raw, meta


def member(archive, filename):
    item = archive.getinfo(filename)
    if item.file_size > MAX_MEMBER:
        raise ValueError(f"Uncompressed source exceeds bound: {filename}")
    return archive.open(item)


def column(key, label, kind="number", unit=None):
    return {"key": key, "label": label, "type": kind, **({"unit": unit} if unit else {})}


def source(name, url, citation, rights=None):
    return {"name": name, "url": url, "citation": citation, "license": PUBLIC_DOMAIN + (f" Basis: {rights}" if rights else "")}


def records(story, rows, columns, sources, snapshots, coverage, limits, **options):
    if not rows or len(rows) > 10000 or len({row["id"] for row in rows}) != len(rows):
        raise ValueError(f"Invalid record population: {story}")
    years = [row["year"] for row in rows]
    return {"format": "kfm-story-bundle-v1", "story": story, "version": 1,
            "built_at": max(item["retrievedAt"] for item in snapshots),
            "observed": {"from": str(min(years)), "to": str(max(years))}, "sources": sources,
            "data": {"kind": "records", "records": rows, "columns": columns, "coverage": coverage,
                     "yearField": "year", "sourceSnapshot": snapshots[0], "sourceSnapshots": snapshots,
                     "limits": limits, **options}}


def energy(fetch):
    raw, meta = fetch.get(SEDS_URL)
    rows, series = [], {}
    with zipfile.ZipFile(io.BytesIO(raw)) as archive, member(archive, "SEDS.txt") as stream:
        for line in stream:
            item = json.loads(line)
            identifier = item.get("series_id", "")
            parts = identifier.split(".")
            if len(parts) != 4 or parts[0] != "SEDS" or parts[1] not in ENERGY_SERIES or parts[2:] != ["KS", "A"]:
                continue
            if item.get("geography") != "USA-KS" or item.get("units") != "Billion Btu" or item.get("f") != "A":
                raise ValueError(f"Source geography, unit or frequency changed: {identifier}")
            code = parts[1]
            if code in series:
                raise ValueError(f"Repeated series: {identifier}")
            label, flow, sector, energy_source = ENERGY_SERIES[code]
            series[code] = {"id": identifier, "name": item["name"], "unit": item["units"],
                            "source": item["source"], "lastUpdated": item["last_updated"],
                            "sourceStart": item["start"], "sourceEnd": item["end"]}
            seen = set()
            for period, value in sorted(item["data"]):
                if not re.fullmatch(r"\d{4}", str(period)) or period in seen:
                    raise ValueError(f"Invalid annual observation: {identifier}")
                seen.add(period)
                year = int(period)
                if not 1960 <= year <= 2024:
                    continue
                if value is not None and (not isinstance(value, (float, int)) or not math.isfinite(value)):
                    raise ValueError(f"Unexpected value or missing sentinel: {identifier}/{period}")
                rows.append({"id": f"{identifier}/{year}", "name": item["name"], "series": label,
                             "seriesId": identifier, "year": year, "value": value, "unit": item["units"],
                             "flow": flow, "sector": sector, "energySource": energy_source})
            if seen != {str(year) for year in range(1960, 2025)}:
                raise ValueError(f"Annual coverage changed: {identifier}")
    if set(series) != set(ENERGY_SERIES):
        raise ValueError("Required energy series missing from EIA response")
    rows.sort(key=lambda row: (row["series"], row["year"]))
    return records("energy-shift", rows,
        [column("series", "Energy series", "string"), column("year", "Year", "year"), column("value", "Annual energy", unit="billion Btu"),
         column("flow", "Accounting view", "string"), column("sector", "Sector", "string"), column("energySource", "Energy source", "string"),
         column("unit", "Source unit", "string"), column("seriesId", "EIA series identifier", "string"), column("name", "Exact EIA series name", "string")],
        [source("EIA SEDS public bulk download", SEDS_URL, "U.S. Energy Information Administration, State Energy Data System bulk series, June 2026 release; 26 selected annual Kansas series, 1960–2024.", EIA_RIGHTS),
         source("EIA SEDS technical documentation", "https://www.eia.gov/state/seds/sep_use/notes/use_intro.pdf", "EIA, SEDS consumption technical notes: primary energy and end-use accounting, units, conversions, and limitations.", EIA_RIGHTS),
         source("EIA reuse policy", EIA_RIGHTS, "EIA permits use and distribution of its public data with source and publication-date acknowledgment.", EIA_RIGHTS)],
        [meta], "26 Kansas annual energy series × 65 years (1960–2024); 1,690 observations in one source unit",
        ["Annual state-level estimates in billion British thermal units (Btu), not electricity generation in MWh or installed capacity in MW. Source series names and IDs are retained.",
         "Consumption by fuel, consumption by sector, production, and their totals overlap. Do not sum all displayed series or interpret them as shares of a single additive energy mix.",
         "Production is a separate accounting view from consumption. Electricity conversion and system-loss accounting differ across primary fuels; a Btu comparison is not a lifecycle emissions comparison.",
         "Sector total consumption includes allocated electrical-system losses. The electric-power series also includes net U.S. electricity imports as specified by EIA; it must not be added to the end-use sector totals.",
         "Renewable totals overlap wind, solar, hydropower, geothermal and biomass components. Source-reported zeroes are preserved; missing values remain null and are never interpolated.",
         "Fixed snapshot of selected complete annual series ending in 2024; newer partial-release indicators are excluded. EIA can revise historical estimates. No facility locations, local exposure, emissions, forecasts or causal effects are inferred."],
        temporalMode="events", categoryField="series", valueField="value", preferredView="chart", timeLabel="Annual records through year",
        seriesPeriod="year", seriesMetadata=series, defaultCategory="Total consumption")


def number(value):
    # EPA blank means unavailable/not measured. Never coerce it to zero.
    if value is None or not value.strip():
        return None
    parsed = float(value)
    if not math.isfinite(parsed) or parsed < 0 or not parsed.is_integer():
        raise ValueError(f"Unexpected EPA annual statistic: {value!r}")
    return int(parsed)


def air(fetch):
    urls = [AQI_BASE + f"annual_aqi_by_county_{year}.zip" for year in AQI_YEARS]
    with ThreadPoolExecutor(max_workers=4) as pool:
        replies = list(pool.map(fetch.get, urls))
    geo_raw, geo_meta = fetch.get(GEO_URL)
    geo = json.loads(geo_raw)
    if geo.get("exceededTransferLimit") or len(geo.get("features", [])) != 105:
        raise ValueError("County boundary response is incomplete")
    counties = {feature["properties"]["NAME"].removesuffix(" County"): feature for feature in geo["features"]}
    rows, coverage = [], {}
    for year, (raw, _) in zip(AQI_YEARS, replies):
        with zipfile.ZipFile(io.BytesIO(raw)) as archive, member(archive, f"annual_aqi_by_county_{year}.csv") as stream:
            reader = csv.DictReader(io.TextIOWrapper(stream, encoding="utf-8-sig", newline=""))
            required = {"State", "County", "Year"} | {item[0] for item in AQI_FIELDS.values()}
            if not required.issubset(reader.fieldnames or []):
                raise ValueError(f"EPA schema changed: {year}")
            for item in reader:
                if item["State"] != "Kansas":
                    continue
                if item["Year"] != str(year) or item["County"] not in counties:
                    raise ValueError(f"EPA county or year mismatch: {year}/{item['County']}")
                feature = counties[item["County"]]
                fips = feature["properties"]["GEOID"]
                row = {"id": f"{fips}/{year}", "name": item["County"] + " County", "fips": fips, "year": year,
                       "geometry": feature["geometry"], **{key: number(item.get(spec[0])) for key, spec in AQI_FIELDS.items()}}
                days = row["daysWithAqi"]
                annual_days = 366 if calendar.isleap(year) else 365
                if days is None or not 0 < days <= annual_days:
                    raise ValueError(f"Invalid monitored-day denominator: {row['id']}")
                categories = [row[key] for key in ("goodDays", "moderateDays", "sensitiveDays", "unhealthyDays", "veryUnhealthyDays", "hazardousDays")]
                if all(value is not None for value in categories) and sum(categories) != days:
                    raise ValueError(f"AQI categories do not reconcile: {row['id']}")
                row["coveragePct"] = round(100 * days / annual_days, 2)
                unhealthy = [row[key] for key in ("sensitiveDays", "unhealthyDays", "veryUnhealthyDays", "hazardousDays")]
                row["daysAbove100"] = sum(unhealthy) if all(value is not None for value in unhealthy) else None
                row["above100Pct"] = round(100 * row["daysAbove100"] / days, 2) if row["daysAbove100"] is not None else None
                row["goodPct"] = round(100 * row["goodDays"] / days, 2) if row["goodDays"] is not None else None
                rows.append(row)
        coverage[str(year)] = sum(row["year"] == year for row in rows)
        if not coverage[str(year)]:
            raise ValueError(f"No Kansas observations in {year}")
    rows.sort(key=lambda row: (row["year"], row["fips"]))
    monitored = len({row["fips"] for row in rows})
    sources = [source(f"EPA county AQI annual summary {year}", url,
        f"U.S. Environmental Protection Agency, AirData AQS annual county AQI summary {year}; Kansas records only. Original annual statistics retained.", EPA_RIGHTS) for year, url in zip(AQI_YEARS, urls)]
    sources += [source("EPA annual AQI report definitions", "https://www.epa.gov/outdoor-air-quality-data/about-airdata-reports",
                       "EPA describes monitored-day denominators, AQI categories, max/median/90th percentile, and counts of main-pollutant days.", EPA_RIGHTS),
                source("Census TIGERweb county boundaries", GEO_URL,
                       "U.S. Census Bureau, contemporary Kansas counties; geometries simplified by the public TIGERweb query for display."),
                source("EPA open-data reuse policy", EPA_RIGHTS,
                       "EPA's default public-domain data license includes no warranty; consult dataset limitations.", EPA_RIGHTS)]
    return records("air-and-health", rows,
        [column("name", "County", "string"), column("fips", "County FIPS", "string"), column("year", "Year", "year"),
         column("aqi90th", "90th percentile daily AQI", unit="AQI"), column("medianAqi", "Median daily AQI", unit="AQI"), column("maxAqi", "Maximum daily AQI", unit="AQI"),
         column("daysWithAqi", "Monitored days", unit="days"), column("coveragePct", "Calendar days with AQI", unit="%"),
         column("daysAbove100", "Days AQI above 100", unit="days"), column("above100Pct", "Monitored days AQI above 100", unit="%"), column("goodPct", "Monitored days with good AQI", unit="%"),
         *[column(key, spec[1], unit=spec[2]) for key, spec in AQI_FIELDS.items() if key not in {"daysWithAqi", "aqi90th", "medianAqi", "maxAqi"}]],
        sources, [meta for _, meta in replies] + [geo_meta],
        f"{len(rows)} Kansas monitored county-years, 2000–2025; {monitored} counties appear at least once; {coverage['2025']} counties in 2025",
        ["Only counties and years with AQI observations appear. Unmonitored counties are missing, not clean air. Sampling days, pollutants and monitor networks differ by county and year; comparisons require checking coverage.",
         "EPA annual county AQI summarizes available outdoor monitors and the daily maximum across measured pollutants. It does not describe every neighborhood, indoor air, individual exposure or a measured health outcome.",
         "Days with AQI is the denominator for derived percentages. Coverage is monitored days divided by 365 or 366 calendar days. Days above 100 sums the four source AQI categories starting at 101; percentages are rounded to two decimals.",
         "Main-pollutant days count days on which that pollutant determined the daily AQI. They are not counts of violations or days exceeding a pollutant standard. Source blanks remain null; source zeroes remain zeroes.",
         "Max, median and 90th-percentile AQI are EPA's supplied annual statistics. Annual medians/percentiles cannot be summed or averaged into a statewide AQI. This instrument does not recompute AQI from concentrations or infer a cause.",
         "AQI definitions and monitoring methods can change; recent EPA releases can revise historical statistics. This snapshot preserves EPA's current published annual values without back-calculating older breakpoint rules.",
         "Each playback year selects one annual record per monitored county. Simplified contemporary county boundaries locate the reporting area, not the extent of a pollution plume. Fixed complete-year snapshots end in 2025; not a live air-quality service."],
        temporalMode="snapshot", categoryField="name", valueField="aqi90th", preferredView="chart", seriesPeriod="year", coverageByYear=coverage,
        derivedFields={"coveragePct": "100 × daysWithAqi / calendarDaysInYear", "daysAbove100": "sensitiveDays + unhealthyDays + veryUnhealthyDays + hazardousDays",
                       "above100Pct": "100 × daysAbove100 / daysWithAqi", "goodPct": "100 × goodDays / daysWithAqi"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=Path("/tmp/kfm-labs-science-raw"))
    parser.add_argument("--offline", action="store_true", help="Rebuild from SHA-256 verified raw response receipts")
    args = parser.parse_args()
    fetch = Fetcher(args.cache, args.offline)
    # Finish acquisitions and validate both bundles before touching shipping files.
    bundles = [energy(fetch), air(fetch)]
    manifest, outputs = {}, {}
    for result in bundles:
        raw = encoded(result)
        if not 0 < len(raw) <= MAX_BUNDLE:
            raise ValueError(f"Story exceeds bundle byte budget: {result['story']}")
        digest, story = sha(raw), result["story"]
        filename = f"{story}-{digest[:16]}.json"
        outputs[filename] = raw
        manifest[story] = {"path": "/labs-data-extension/" + filename, "sha256": digest, "bytes": len(raw),
                           "observed": result["observed"], "retrievedAt": result["built_at"], "records": len(result["data"]["records"])}
    target = ROOT / "public/labs-data-extension"
    target.mkdir(parents=True, exist_ok=True)
    for filename, raw in outputs.items():
        (target / filename).write_bytes(raw)
    module = "// Generated by scripts/prepare-labs-science-data.py from public federal responses.\nexport const EXTENSION_LAB_SNAPSHOTS = Object.freeze(" + json.dumps(manifest, indent=2) + ");\n"
    (ROOT / "app/labs/extension-snapshots.mjs").write_text(module)
    # Shipping validation permits only the current manifest files.
    for old in target.glob('*.json'):
        if old.name not in outputs:
            old.unlink()
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
