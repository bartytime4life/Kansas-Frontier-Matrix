"""Pure, deterministic USCRN daily01 soil transformation from verified captured bytes.

Produces review candidates only: a complete capture is neither source
admission nor release. Each station-day keeps NOAA's daily soil moisture
(m3/m3) and soil temperature (degC) at 5, 10, 20, 50 and 100 cm with the
source token verbatim. A missing sentinel is withheld (value null, MISSING) and
never counts as zero; a value outside the physical range is withheld as
OUT_OF_RANGE. observation_date is the station's local-standard-time day.
"""
from __future__ import annotations

from datetime import date, timedelta
import math
import re

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.noaa.src.noaa import uscrn_daily
from connectors.noaa.src.noaa.uscrn_daily_capture import (
    PROFILE, SOURCE_ID, STALE_AFTER_DAYS, STATIONS, VARIABLES, WINDOW_DAYS, capture_keys, object_limit, window,
)

CANDIDATE_PROFILE = "kfm.uscrn-daily-candidate/v1"
OBSERVATION_PROFILE = "kfm.daily-soil-observation/v1"
UNITS = {"SOIL_MOISTURE": "m3/m3", "SOIL_TEMP": "degC"}
RANGES = {"SOIL_MOISTURE": (0.0, 1.0), "SOIL_TEMP": (-50.0, 60.0)}
SENTINELS = {"SOIL_MOISTURE": uscrn_daily.MOISTURE_MISSING, "SOIL_TEMP": uscrn_daily.NUMBER_MISSING}
WITHHELD = ("MISSING", "OUT_OF_RANGE")
DIGEST = re.compile(r"sha256:[a-f0-9]{64}\Z")
# Kansas bounding box shared with the GHCN-Daily pilot.
LAT, LON = (36.9, 40.1), (-102.2, -94.4)


def station_name(wban: str) -> str:
    """'KS_Manhattan_6_SSW' -> 'Manhattan 6 SSW'."""
    return uscrn_daily.STATIONS[wban].removeprefix("KS_").replace("_", " ")


def reading(variable: str, token: str) -> tuple:
    """(value, withheld) for one daily token."""
    if token == SENTINELS[variable]:
        return None, "MISSING"
    value = float(token)
    low, high = RANGES[variable]
    if not math.isfinite(value) or not low <= value <= high:
        return None, "OUT_OF_RANGE"
    return value, None


def observation(wban, variable, depth, day, token, datalogger, page) -> dict:
    value, withheld = reading(variable, token)
    identity = digest_bytes(canonical_bytes([wban, variable, depth, day])).split(":")[1]
    record = {"profile": OBSERVATION_PROFILE, "id": "kfm:soil:" + identity, "station_id": wban,
              "variable": variable, "depth_cm": depth, "observation_date": day, "source_token": token,
              "value": value, "unit": UNITS[variable], "withheld": withheld, "datalogger_version": datalogger,
              "source_role": "reference_station", "page_digest": page["sha256"],
              "retrieved_at": page["retrieved_at"], "evidence_ref": "kfm:evidence:soil:" + identity}
    record["record_digest"] = digest_bytes(canonical_bytes(record))
    return record


def freshness(observations: list[dict], end: str) -> dict:
    """RECENT, STALE (latest reported soil moisture more than STALE_AFTER_DAYS before end) or EMPTY."""
    last_day = date.fromisoformat(end)
    states = {}
    for station in STATIONS:
        latest = max((r["observation_date"] for r in observations
                      if r["station_id"] == station and r["variable"] == "SOIL_MOISTURE" and r["value"] is not None),
                     default=None)
        states[station] = ("EMPTY" if latest is None else
                           "STALE" if (last_day - date.fromisoformat(latest)).days > STALE_AFTER_DAYS else "RECENT")
    return states


def coverage(states: dict) -> str:
    values = set(states.values())
    return "EMPTY" if values == {"EMPTY"} else "PARTIAL" if "EMPTY" in values else "COMPLETE"


def withheld_counts(observations: list[dict]) -> dict:
    return {station: {reason: sum(1 for r in observations if r["station_id"] == station and r["withheld"] == reason)
                      for reason in WITHHELD} for station in STATIONS}


def _station(wban: str, coordinates: set, pages: list[dict]) -> dict:
    if len(coordinates) != 1:
        raise ValueError("STATION_LOCATION_INVALID")
    lon, lat = next(iter(coordinates))
    if not (LAT[0] <= lat <= LAT[1] and LON[0] <= lon <= LON[1]):
        raise ValueError("STATION_LOCATION_INVALID")
    latest = max(pages, key=lambda p: p["key"])
    return {"id": wban, "name": station_name(wban), "geometry": {"type": "Point", "coordinates": [lon, lat]},
            "page_digest": latest["sha256"], "retrieved_at": latest["retrieved_at"]}


def normalize_capture(manifest: dict, objects: dict[str, bytes]) -> dict:
    """Check capture closure and scope, then select the window's soil values."""
    body = {key: value for key, value in manifest.items() if key != "capture_id"}
    if manifest.get("capture_id") != digest_bytes(canonical_bytes(body)):
        raise ValueError("CAPTURE_DIGEST_MISMATCH")
    if manifest.get("profile") != PROFILE or manifest.get("complete") is not True:
        raise ValueError("CAPTURE_INCOMPLETE")
    if (manifest.get("source_id") != SOURCE_ID or manifest.get("station_ids") != list(STATIONS)
            or manifest.get("variables") != list(VARIABLES) or manifest.get("depths_cm") != list(uscrn_daily.DEPTHS_CM)):
        raise ValueError("CAPTURE_SCOPE_MISMATCH")
    start, end = window(manifest.get("end"))
    if manifest.get("start") != start or str(manifest.get("captured_at", ""))[:10] < end:
        raise ValueError("CAPTURE_WINDOW_INVALID")
    pages = manifest.get("pages")
    if not isinstance(pages, list) or [p.get("key") for p in pages if isinstance(p, dict)] != capture_keys(end):
        raise ValueError("CAPTURE_PAGE_CHAIN_MISMATCH")
    verified = {}
    for page in pages:
        raw = objects.get(page["sha256"])
        if (page.get("url") != uscrn_daily.object_url(page["key"]) or not DIGEST.fullmatch(str(page["sha256"]))
                or raw is None or digest_bytes(raw) != page["sha256"] or len(raw) != page.get("bytes")
                or len(raw) > object_limit(page["key"]) or not isinstance(page.get("retrieved_at"), str)
                or page["retrieved_at"] > manifest["captured_at"]):
            raise ValueError("PAGE_DIGEST_MISMATCH")
        verified[page["key"]] = (page, raw)
    uscrn_daily.check_headers(verified[uscrn_daily.HEADERS_KEY][1])
    days = {(date.fromisoformat(start) + timedelta(days=n)).strftime("%Y%m%d") for n in range(WINDOW_DAYS)}
    index = uscrn_daily.INDEX
    observations, stations = {}, []
    for wban in STATIONS:
        station_pages, coordinates, seen, last_row = [], set(), set(), None
        for key, (page, raw) in verified.items():
            if key == uscrn_daily.HEADERS_KEY or not key.endswith(uscrn_daily.STATIONS[wban] + ".txt"):
                continue
            station_pages.append(page)
            for fields in uscrn_daily.rows(raw, wban):
                day = fields[index["LST_DATE"]]
                if last_row is None or day > last_row[index["LST_DATE"]]:
                    last_row = fields
                if day not in days:
                    continue
                if day in seen:
                    raise ValueError("DUPLICATE_STATION_DAY")
                seen.add(day)
                coordinates.add((float(fields[index["LONGITUDE"]]), float(fields[index["LATITUDE"]])))
                iso = f"{day[:4]}-{day[4:6]}-{day[6:]}"
                for variable in VARIABLES:
                    for depth in uscrn_daily.DEPTHS_CM:
                        token = fields[index[f"{variable}_{depth}_DAILY"]]
                        observations[(wban, iso, variable, depth)] = observation(
                            wban, variable, depth, iso, token, fields[index["CRX_VN"]], page)
        if not seen:
            # No rows in the window (an outage): place the station from its latest row; freshness reports EMPTY.
            if last_row is None:
                raise ValueError("STATION_FILE_EMPTY")
            coordinates.add((float(last_row[index["LONGITUDE"]]), float(last_row[index["LATITUDE"]])))
        stations.append(_station(wban, coordinates, station_pages))
    ordered = [observations[key] for key in sorted(observations)]
    states = freshness(ordered, end)
    candidate = {"profile": CANDIDATE_PROFILE, "capture_id": manifest["capture_id"], "source_id": SOURCE_ID,
                 "start": start, "end": end, "retrieved_at": manifest["captured_at"], "stations": stations,
                 "observations": ordered, "freshness_at_capture": states, "stale_after_days": STALE_AFTER_DAYS,
                 "coverage": coverage(states), "withheld_counts": withheld_counts(ordered),
                 "review_state": "PENDING", "source_admission": "PENDING", "release_state": "UNRELEASED"}
    candidate["candidate_id"] = digest_bytes(canonical_bytes(candidate))
    return candidate
