"""Pure, deterministic GHCN-Daily transformation from verified captured bytes.

Produces review candidates only: a complete capture is neither source
admission nor release. Each station-day element keeps its raw tenths value and
its M/Q/S flags verbatim. A missing value (-9999) or a quality-flagged value
is withheld with value null and never counts as zero; a trace (M=T) is 0 with
trace=true. observation_date is the station's local observation day.
"""
from __future__ import annotations

from datetime import date, timedelta
import gzip
import io
import math
import re

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.noaa.src.noaa import ghcnd
from connectors.noaa.src.noaa.ghcnd_daily_capture import (
    ELEMENTS, PROFILE, SOURCE_ID, STALE_AFTER_DAYS, STATION_LIST_KEY, STATIONS, WINDOW_DAYS,
    capture_keys, object_limit, window,
)

CANDIDATE_PROFILE = "kfm.ghcnd-daily-candidate/v1"
OBSERVATION_PROFILE = "kfm.daily-weather-observation/v1"
UNITS = {"PRCP": "mm", "TMAX": "degC", "TMIN": "degC"}
DIGEST = re.compile(r"sha256:[a-f0-9]{64}\Z")
# Kansas bounding box used by ghcnd.kansas_stations.
LAT, LON = (36.9, 40.1), (-102.2, -94.4)


def _station(raw: bytes, station_id: str, page: dict) -> dict:
    """Read one station's fixed-width row from ghcnd-stations.txt."""
    rows = [line for line in raw.decode("utf-8").splitlines() if line[:11] == station_id]
    if len(rows) != 1:
        raise ValueError("STATION_LIST_MISMATCH")
    line = rows[0]
    try:
        lat, lon, elevation = float(line[12:20]), float(line[21:30]), float(line[31:37])
    except ValueError:
        raise ValueError("STATION_LIST_MISMATCH") from None
    name = line[41:71].strip()
    if (line[38:40] != "KS" or not all(map(math.isfinite, (lat, lon, elevation)))
            or not (LAT[0] <= lat <= LAT[1] and LON[0] <= lon <= LON[1])
            or not name or any(ord(c) < 32 for c in name)):
        raise ValueError("STATION_LIST_MISMATCH")
    return {"id": station_id, "name": name, "geometry": {"type": "Point", "coordinates": [lon, lat]},
            "elevation_m": None if elevation == -999.9 else elevation,
            "page_digest": page["sha256"], "retrieved_at": page["retrieved_at"]}


def _rows(raw: bytes, station_id: str):
    """Yield (day, element, value, m, q, s, obs) for every row, checked like ghcnd.inspect_station."""
    expanded = 0
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as stream:
        while True:
            line = stream.readline(513)
            if not line:
                return
            expanded += len(line)
            if expanded > ghcnd.EXPANDED_BYTES or len(line) > 512:
                raise ValueError("STATION_EXPANSION_LIMIT")
            try:
                fields = line.decode("ascii").rstrip("\r\n").split(",")
            except UnicodeDecodeError:
                raise ValueError("STATION_ROW_FORMAT") from None
            if len(fields) != 8 or fields[0] != station_id:
                raise ValueError("STATION_ROW_ID_OR_SHAPE")
            _, day, element, value, mf, qf, sf, obs = fields
            if (not re.fullmatch(r"\d{8}", day) or not re.fullmatch(r"[A-Z0-9]{4}", element)
                    or not re.fullmatch(r"-?\d{1,6}", value) or any(not re.fullmatch(r"[A-Z0-9]?", f) for f in (mf, qf, sf))
                    or (obs and not re.fullmatch(r"\d{4}", obs))):
                raise ValueError("STATION_ROW_FORMAT")
            yield day, element, int(value), mf, qf, sf, obs or None


def _reading(raw_value: int, mflag: str, qflag: str) -> tuple:
    """(value, trace, withheld) for one raw tenths value."""
    if raw_value == -9999:
        return None, False, "MISSING"
    if qflag:
        return None, False, "QUALITY_FLAG"
    if mflag == "T":
        return 0.0, True, None
    if mflag == "P":  # "missing presumed zero" is still missing
        return None, False, "MISSING"
    return raw_value / 10, False, None


def observation(station_id, element, day, raw_value, mflag, qflag, sflag, obs, page) -> dict:
    value, trace, withheld = _reading(raw_value, mflag, qflag)
    identity = digest_bytes(canonical_bytes([station_id, element, day])).split(":")[1]
    record = {"profile": OBSERVATION_PROFILE, "id": "kfm:weather:" + identity, "station_id": station_id,
              "element": element, "observation_date": day, "raw_value": raw_value, "value": value,
              "unit": UNITS[element], "measurement_flag": mflag, "quality_flag": qflag, "source_flag": sflag,
              "observation_time": obs, "trace": trace, "withheld": withheld, "preliminary": True,
              "source_role": "observed_station", "page_digest": page["sha256"],
              "retrieved_at": page["retrieved_at"], "evidence_ref": "kfm:evidence:weather:" + identity}
    record["record_digest"] = digest_bytes(canonical_bytes(record))
    return record


def freshness(observations: list[dict], end: str) -> dict:
    """RECENT, STALE (latest non-null value more than STALE_AFTER_DAYS before end) or EMPTY."""
    last_day = date.fromisoformat(end)
    states = {}
    for station in STATIONS:
        latest = max((r["observation_date"] for r in observations
                      if r["station_id"] == station and r["value"] is not None), default=None)
        states[station] = ("EMPTY" if latest is None else
                           "STALE" if (last_day - date.fromisoformat(latest)).days > STALE_AFTER_DAYS else "RECENT")
    return states


def coverage(states: dict) -> str:
    values = set(states.values())
    return "EMPTY" if values == {"EMPTY"} else "PARTIAL" if "EMPTY" in values else "COMPLETE"


def withheld_counts(observations: list[dict]) -> dict:
    return {station: {reason: sum(1 for r in observations if r["station_id"] == station and r["withheld"] == reason)
                      for reason in ("MISSING", "QUALITY_FLAG")} for station in STATIONS}


def normalize_capture(manifest: dict, objects: dict[str, bytes]) -> dict:
    """Check capture closure and scope, then select the window's PRCP/TMAX/TMIN rows."""
    body = {key: value for key, value in manifest.items() if key != "capture_id"}
    if manifest.get("capture_id") != digest_bytes(canonical_bytes(body)):
        raise ValueError("CAPTURE_DIGEST_MISMATCH")
    if manifest.get("profile") != PROFILE or manifest.get("complete") is not True:
        raise ValueError("CAPTURE_INCOMPLETE")
    if (manifest.get("source_id") != SOURCE_ID or manifest.get("station_ids") != list(STATIONS)
            or manifest.get("elements") != list(ELEMENTS)):
        raise ValueError("CAPTURE_SCOPE_MISMATCH")
    start, end = window(manifest.get("end"))
    if manifest.get("start") != start or str(manifest.get("captured_at", ""))[:10] < end:
        raise ValueError("CAPTURE_WINDOW_INVALID")
    pages = manifest.get("pages")
    if not isinstance(pages, list) or [p.get("key") for p in pages if isinstance(p, dict)] != capture_keys():
        raise ValueError("CAPTURE_PAGE_CHAIN_MISMATCH")
    verified = {}
    for page in pages:
        raw = objects.get(page["sha256"])
        if (page.get("url") != ghcnd.object_url(page["key"]) or not DIGEST.fullmatch(str(page["sha256"]))
                or raw is None or digest_bytes(raw) != page["sha256"] or len(raw) != page.get("bytes")
                or len(raw) > object_limit(page["key"]) or not isinstance(page.get("retrieved_at"), str)
                or page["retrieved_at"] > manifest["captured_at"]):
            raise ValueError("PAGE_DIGEST_MISMATCH")
        verified[page["key"]] = (page, raw)
    station_page, station_raw = verified[STATION_LIST_KEY]
    stations = [_station(station_raw, sid, station_page) for sid in STATIONS]
    days = {(date.fromisoformat(start) + timedelta(days=n)).strftime("%Y%m%d") for n in range(WINDOW_DAYS)}
    observations = {}
    for sid in STATIONS:
        page, raw = verified[f"by_station/{sid}.csv.gz"]
        for day, element, value, mf, qf, sf, obs in _rows(raw, sid):
            if day not in days or element not in ELEMENTS:
                continue
            key = (sid, element, day)
            if key in observations:
                raise ValueError("DUPLICATE_STATION_DAY_ELEMENT")
            iso = f"{day[:4]}-{day[4:6]}-{day[6:]}"
            observations[key] = observation(sid, element, iso, value, mf, qf, sf, obs, page)
    ordered = sorted(observations.values(), key=lambda r: (r["station_id"], r["observation_date"], r["element"]))
    states = freshness(ordered, end)
    candidate = {"profile": CANDIDATE_PROFILE, "capture_id": manifest["capture_id"], "source_id": SOURCE_ID,
                 "start": start, "end": end, "retrieved_at": manifest["captured_at"], "stations": stations,
                 "observations": ordered, "freshness_at_capture": states, "stale_after_days": STALE_AFTER_DAYS,
                 "coverage": coverage(states), "withheld_counts": withheld_counts(ordered),
                 "review_state": "PENDING", "source_admission": "PENDING", "release_state": "UNRELEASED"}
    candidate["candidate_id"] = digest_bytes(canonical_bytes(candidate))
    return candidate
