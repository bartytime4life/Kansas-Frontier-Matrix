"""Climate Stripes: NOAA nClimDiv monthly temperature, precipitation and drought index for Kansas since 1895."""
from __future__ import annotations

from collections import defaultdict

from tools.local_data.stories import scaled

STORY = {
    "id": "climate-stripes",
    "version": 1,
    "db": "observations",
    "tables": ["kfm_climdiv_monthly", "kfm_climdiv_normals"],
    "sources": [{
        "name": "NOAA NCEI nClimDiv, U.S. Climate Divisional Dataset",
        "license": "U.S. government work, distributed without warranty",
        "url": "https://www.ncei.noaa.gov/pub/data/cirs/climdiv/",
        "citation": "NOAA National Centers for Environmental Information, nClimDiv monthly state and divisional "
                    "series and period averages.",
    }],
}

STATE = "20"
# NCEI's conventional names for Kansas's nine climate divisions, 1401-1409; the tables hold only the numbers.
DIVISIONS = {"1401": "Northwest", "1402": "North Central", "1403": "Northeast", "1404": "West Central", "1405": "Central",
             "1406": "East Central", "1407": "Southwest", "1408": "South Central", "1409": "Southeast"}
# How each element is stored in the bundle: value times scale, as an integer.
ELEMENTS = {
    "tmpc": {"label": "Temperature", "unit": "°F", "scale": 10, "annual": "mean", "family": "heat"},
    "pcpn": {"label": "Precipitation", "unit": "in", "scale": 100, "annual": "sum", "family": "water"},
    "pdsi": {"label": "Drought index (PDSI)", "unit": "index", "scale": 100, "annual": "mean", "family": "water"},
}
BASELINES = {"1901-2000": "0031", "1991-2020": "0010"}


def build(db) -> dict | None:
    marks = ",".join("?" for _ in ELEMENTS)
    series: dict[tuple[str, str], dict[tuple[int, int], float | None]] = defaultdict(dict)
    years: set[int] = set()
    latest = {}
    for area, element, year, month, value in db.execute(
            f"SELECT area_code, element, year, month, value FROM kfm_climdiv_monthly "
            f"WHERE area_type IN ('state','division') AND element IN ({marks})", tuple(ELEMENTS)):
        if area != STATE and area not in DIVISIONS:
            continue
        series[element, area][year, month] = value
        years.add(year)
        if value is not None and element == "tmpc" and area == STATE:
            latest["to"] = max(latest.get("to", (0, 0)), (year, month))
            latest["from"] = min(latest.get("from", (9999, 0)), (year, month))
    if not series or not latest:
        return None
    ordered = list(range(min(years), max(years) + 1))
    areas = [{"id": STATE, "name": "Kansas"}] + [{"id": code, "name": name} for code, name in DIVISIONS.items()]
    values: dict[str, dict[str, list]] = {}
    for element, spec in ELEMENTS.items():
        values[element] = {}
        for area in areas:
            months = series.get((element, area["id"]), {})
            flat = [months.get((year, month)) for year in ordered for month in range(1, 13)]
            values[element][area["id"]] = scaled(flat, spec["scale"])
    normals: dict[str, dict[str, dict[str, list]]] = {name: {} for name in BASELINES}
    by_code = {code: name for name, code in BASELINES.items()}
    found: dict[tuple[str, str, str], dict[int, float | None]] = defaultdict(dict)
    marks_period = ",".join("?" for _ in by_code)
    for area, element, period, month, value in db.execute(
            f"SELECT area_code, element, period_code, month, value FROM kfm_climdiv_normals "
            f"WHERE area_type IN ('state','division') AND element IN ('tmpc','pcpn') AND period_code IN ({marks_period})",
            tuple(by_code)):
        if area == STATE or area in DIVISIONS:
            found[by_code[period], element, area][month] = value
    for (baseline, element, area), months in sorted(found.items()):
        normals[baseline].setdefault(element, {})[area] = scaled([months.get(m) for m in range(1, 13)],
                                                                 ELEMENTS[element]["scale"])
    start, end = latest["from"], latest["to"]
    partial = end[1] != 12
    limits = [
        "Values are area averages NCEI grids from station reports, not readings at a place. Fewer stations stand "
        "behind the early decades.",
        "NCEI revises at least the latest two years in each monthly release, so recent values can change.",
        "Anomalies use NCEI's published period averages. The drought index has none: PDSI is already relative to "
        "each place's own climate, so it is shown as the index itself and the baseline does not change it.",
        "Climate divisions are NCEI's and reflect climate and geography, not county or watershed lines.",
    ]
    if partial:
        limits.append(f"{end[0]} runs through month {end[1]} of 12. Its stripe compares only those months with the same "
                      "months of the baseline, and it is drawn with a hatch.")
    return {
        "_observed": {"from": f"{start[0]}-{start[1]:02d}", "to": f"{end[0]}-{end[1]:02d}"},
        "years": ordered,
        "areas": areas,
        "elements": ELEMENTS,
        "values": values,
        "normals": normals,
        "baselines": list(BASELINES),
        "latest": {"year": end[0], "month": end[1]},
        "limits": limits,
    }
