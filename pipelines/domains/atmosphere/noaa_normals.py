"""Deterministic Kansas station-normal candidate from preserved NOAA bytes."""
from __future__ import annotations

from hashlib import sha256

from connectors.noaa.src.noaa.climate_normals import parse_inventory, parse_station, station_key
from connectors.noaa.src.noaa.climate_normals_capture import canonical_bytes


def _digest(raw: bytes) -> str:
    return "sha256:" + sha256(raw).hexdigest()


def normalize_capture(manifest: dict, objects: dict[str, bytes]) -> dict:
    if (manifest.get("profile") != "kfm.noaa-monthly-normals-capture/v1"
            or manifest.get("period") != "1991-2020" or manifest.get("state") != "KS"
            or manifest.get("complete") is not True or manifest.get("failed_station_ids")
            or manifest.get("source_admission") != "PENDING"):
        raise ValueError("CAPTURE_NOT_COMPLETE")
    inventory_ref = manifest["inventory"]
    inventory = objects[inventory_ref["sha256"]]
    if _digest(inventory) != inventory_ref["sha256"] or len(inventory) != inventory_ref["bytes"]:
        raise ValueError("INVENTORY_DIGEST")
    stations = parse_inventory(inventory)
    entries = manifest["station_objects"]
    if (len(stations) != manifest["expected_stations"]
            or len(stations) != len(entries)
            or len(entries) != manifest["captured_stations"]):
        raise ValueError("STATION_COUNT")
    by_id = {entry["station_id"]: entry for entry in entries}
    if len(by_id) != len(entries) or set(by_id) != {station["station_id"] for station in stations}:
        raise ValueError("STATION_SET")
    projected = []
    for station in stations:
        entry = by_id[station["station_id"]]
        if entry["key"] != station_key(station["station_id"]):
            raise ValueError("STATION_KEY")
        raw = objects[entry["sha256"]]
        if _digest(raw) != entry["sha256"] or len(raw) != entry["bytes"]:
            raise ValueError("STATION_DIGEST")
        projected.append(parse_station(raw, station))
    candidate = {"profile": "kfm.noaa-monthly-normals-candidate/v1",
                 "source_id": "noaa-ncei-climate-normals", "source_role": "aggregate",
                 "period": "1991-2020", "state": "KS", "inventory_sha256": inventory_ref["sha256"],
                 "station_count": len(projected), "stations": projected,
                 "source_admission": "PENDING", "review_state": "PENDING",
                 "release_state": "UNRELEASED"}
    candidate["candidate_id"] = _digest(canonical_bytes(candidate))
    return candidate


def project_station_points(candidate: dict, *, month: int, variable: str) -> dict:
    """Build a review-only point carrier; never interpolate station values."""
    if (candidate.get("profile") != "kfm.noaa-monthly-normals-candidate/v1"
            or candidate.get("source_admission") != "PENDING"
            or candidate.get("release_state") != "UNRELEASED"):
        raise ValueError("CANDIDATE_STATE")
    if not isinstance(month, int) or isinstance(month, bool) or not 1 <= month <= 12:
        raise ValueError("MONTH")
    if variable not in {"temperature_f", "precipitation_in"}:
        raise ValueError("VARIABLE")
    if candidate.get("station_count") != len(candidate.get("stations", [])):
        raise ValueError("STATION_COUNT")
    features = []
    for station in candidate["stations"]:
        months = station["months"]
        if len(months) != 12 or months[month - 1]["month"] != month:
            raise ValueError("MONTH_SET")
        element = months[month - 1][variable]
        if element is None or element["value"] is None:
            continue
        features.append({"type": "Feature", "id": station["station_id"],
                         "geometry": {"type": "Point", "coordinates": [
                             float(station["longitude"]), float(station["latitude"])]},
                         "properties": {"station_id": station["station_id"],
                                        "name": station["name"], "period": "1991-2020",
                                        "month": month, "variable": variable,
                                        "value": float(element["value"]),
                                        "value_text": element["value"],
                                        "unit": "degF" if variable == "temperature_f" else "in",
                                        "measurement_flag": element["measurement_flag"],
                                        "completeness_flag": element["completeness_flag"],
                                        "years": element["years"],
                                        "source_sha256": station["source_sha256"]}})
    return {"type": "FeatureCollection", "profile": "kfm.noaa-monthly-normals-map-candidate/v1",
            "candidate_id": candidate["candidate_id"], "source_role": "aggregate",
            "release_state": "UNRELEASED", "period": "1991-2020",
            "month": month, "variable": variable, "features": features}
