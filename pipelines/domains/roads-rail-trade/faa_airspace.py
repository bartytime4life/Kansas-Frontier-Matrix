"""FAA NASR airspace + airport snapshot -> Kansas aviation context product.

Inputs are an operator-supplied, digest-pinned NASR-derived snapshot (one 28-day
cycle). Output is EXTERNAL_CONTEXT_ONLY display context for the Site map: it is
not a KFM-released record, not the held APT candidate lane in faa_airports.py,
and never navigation or flight-planning data. Vertical limits keep their source
reference (MSL/AGL/SFC); nothing here converts AGL to MSL.
"""
from datetime import date, timedelta
import gzip
import hashlib
import json
import math
import re

import rfc8785

VERSION = "faa-airspace-v2"
PROFILE = "kfm.aviation-kansas-context/v2"
# Kansas plus a ~15 NM margin so neighbouring Class B/C/D and MOAs that reach
# into the state stay whole. Features are kept or dropped, never clipped.
REGION = (-102.3, 36.7, -94.3, 40.3)
VOLUME_TYPES = ("CLASS_B", "CLASS_C", "CLASS_D", "CLASS_E2", "CLASS_E3", "CLASS_E4", "CLASS_E5", "CLASS_E6",
                "CLASS_E7", "MOA", "RESTRICTED", "PROHIBITED", "WARNING", "ALERT", "NSA")
REFERENCES = {"MSL", "AGL", "SFC"}
MAX_VOLUMES = 2000
MAX_RING_POINTS = 20000
# Identifiers on Class B/C/D/E2-E4 are FAA location IDs of the associated airport.
AIRPORT_KEYED = {"CLASS_B", "CLASS_C", "CLASS_D", "CLASS_E2", "CLASS_E3", "CLASS_E4"}
# Federal airways and RNAV routes are the fixed structure IFR traffic flows along.
AIRWAY_TYPES = ("VICTOR", "JET", "RNAV_T", "RNAV_Q")
WEATHER_STATION = re.compile(r"^([A-Z0-9]{3,4}) (ASOS|AWOS-[0-9A-Z]+|AWOS)$")


def canonical(value):
    return rfc8785.dumps(value)


def sha(value):
    return "sha256:" + hashlib.sha256(value).hexdigest()


def _finite(value, low, high):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and low <= value <= high


def _bound(value):
    if not isinstance(value, dict) or value.get("reference") not in REFERENCES or not _finite(value.get("valueFt"), -2000, 100000):
        raise ValueError("VERTICAL_BOUND_INVALID")
    out = {"value_ft": int(round(value["valueFt"])), "reference": value["reference"]}
    if value["reference"] == "SFC" and out["value_ft"] != 0:
        raise ValueError("VERTICAL_BOUND_INVALID")
    if value.get("inclusive") is False:
        out["inclusive"] = False
    return out


def _rings(geometry):
    if not isinstance(geometry, dict) or geometry.get("type") != "Polygon" or not isinstance(geometry.get("coordinates"), list):
        raise ValueError("GEOMETRY_INVALID")
    rings, total = [], 0
    for ring in geometry["coordinates"]:
        if not isinstance(ring, list) or len(ring) < 4:
            raise ValueError("GEOMETRY_INVALID")
        points = []
        for point in ring:
            if not isinstance(point, list) or len(point) < 2 or not _finite(point[0], -180, 180) or not _finite(point[1], -90, 90):
                raise ValueError("GEOMETRY_INVALID")
            # Five decimals is ~1 m; finer digits are generator arc-tracing noise.
            rounded = [round(point[0], 5), round(point[1], 5)]
            if not points or points[-1] != rounded:
                points.append(rounded)
        if len(points) < 4 or points[0] != points[-1]:
            raise ValueError("GEOMETRY_INVALID")
        total += len(points)
        rings.append(points)
    if not rings or total > MAX_RING_POINTS:
        raise ValueError("GEOMETRY_INVALID")
    return rings


def _bbox(rings):
    xs = [p[0] for p in rings[0]]
    ys = [p[1] for p in rings[0]]
    return [min(xs), min(ys), max(xs), max(ys)]


def _intersects(box):
    return box[2] >= REGION[0] and box[0] <= REGION[2] and box[3] >= REGION[1] and box[1] <= REGION[3]


def _distance_km(lon1, lat1, lon2, lat2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    a = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(lon2 - lon1) / 2) ** 2
    return 6371.0088 * 2 * math.asin(min(1, math.sqrt(a)))


def _airport(record):
    """Published NASR facility fields. Contacts, owner/manager names and remarks are never copied."""
    stations = sorted({m.group(2) for f in record.get("frequencies") or [] if isinstance(f, dict)
                       for m in [WEATHER_STATION.match(str(f.get("use") or ""))] if m})
    ctaf = sorted({f["frequencyMhz"] for f in record.get("frequencies") or []
                   if isinstance(f, dict) and f.get("use") == "CTAF" and _finite(f.get("frequencyMhz"), 100, 400)})
    runways = []
    for runway in record.get("runways") or []:
        ends = [{"id": str(e["id"]), "lon": round(e["lon"], 6), "lat": round(e["lat"], 6),
                 "elevation_ft": e.get("elevationFt") if _finite(e.get("elevationFt"), -1500, 15000) else None}
                for e in runway.get("ends") or [] if _finite(e.get("lon"), -180, 180) and _finite(e.get("lat"), -90, 90)]
        if len(ends) != 2 or not _finite(runway.get("lengthFt"), 1, 30000):
            continue
        runways.append({"id": str(runway["id"]), "length_ft": int(runway["lengthFt"]),
                        "width_ft": int(runway["widthFt"]) if _finite(runway.get("widthFt"), 1, 1000) else None,
                        "surface": runway.get("surfaceType"), "lighting": runway.get("lighting"), "ends": ends})
    icao = record.get("icao")
    return {"faa_id": record["faaId"], "icao_id": icao if isinstance(icao, str) and re.fullmatch(r"[A-Z]{4}", icao) else None,
            "name": record["name"], "city": record.get("city"), "county": record.get("county"), "state": record.get("state"),
            "lon": round(record["lon"], 6), "lat": round(record["lat"], 6),
            "elevation_ft": round(record["elevationFt"], 1), "facility_type": record["facilityType"],
            "use": "PUBLIC" if record.get("useType") == "PUBLIC" else "PRIVATE",
            "ownership": record.get("ownershipType"), "tower": record.get("towerType"),
            "weather_station": stations[0] if stations else None, "ctaf_mhz": ctaf[0] if ctaf else None,
            "traffic_pattern_ft_agl": record.get("trafficPatternAltitudeFtAgl") if _finite(record.get("trafficPatternAltitudeFtAgl"), 100, 5000) else None,
            "runways": sorted(runways, key=lambda r: r["id"])}


def _airway_segments(record):
    """Consecutive-waypoint segments touching the region; MEA/MAA belong to the leg's first point."""
    points = [w for w in record.get("waypoints") or [] if isinstance(w, dict)]
    segments = []
    for start, end in zip(points, points[1:]):
        if not all(_finite(w.get("lon"), -180, 180) and _finite(w.get("lat"), -90, 90) for w in (start, end)):
            continue
        box = [min(start["lon"], end["lon"]), min(start["lat"], end["lat"]), max(start["lon"], end["lon"]), max(start["lat"], end["lat"])]
        if not _intersects(box):
            continue
        segments.append({"designation": record["designation"], "type": record["type"],
                         "from": start.get("identifier") or start.get("name"), "to": end.get("identifier") or end.get("name"),
                         "coords": [[round(start["lon"], 5), round(start["lat"], 5)], [round(end["lon"], 5), round(end["lat"], 5)]],
                         "mea_ft": start.get("minimumEnrouteAltitudeFt") if _finite(start.get("minimumEnrouteAltitudeFt"), 0, 60000) else None,
                         "maa_ft": start.get("maximumAuthorizedAltitudeFt") if _finite(start.get("maximumAuthorizedAltitudeFt"), 0, 99999) else None})
    return segments


def prepare(airspace_gz, airports_gz, airways_gz, source):
    """Deterministic product from one NASR cycle. Any shape drift fails the whole run.

    `source` binds the exact upstream package identity and integrity strings the
    operator verified; the data-file digests are recomputed here.
    """
    if any(len(blob) > 32 * 1024 * 1024 for blob in (airspace_gz, airports_gz, airways_gz)):
        raise ValueError("INPUT_TOO_LARGE")
    airspace, airports, airways = (json.loads(gzip.decompress(blob)) for blob in (airspace_gz, airports_gz, airways_gz))
    cycle = airspace.get("properties", {}).get("nasrCycleDate")
    if airspace.get("type") != "FeatureCollection" or not isinstance(airspace.get("features"), list) or not cycle:
        raise ValueError("AIRSPACE_SHAPE_INVALID")
    if any(other.get("meta", {}).get("nasrCycleDate") != cycle or not isinstance(other.get("records"), list) for other in (airports, airways)):
        raise ValueError("CYCLE_MISMATCH")
    effective = date.fromisoformat(cycle)
    if set(source) != {"airspace", "airports", "airways"} or any(not isinstance(source[k], dict) or set(source[k]) != {"package", "version", "integrity"}
                                                         or not all(isinstance(v, str) and v for v in source[k].values()) for k in source):
        raise ValueError("SOURCE_BINDING_INVALID")

    elevations, facilities, by_id = [], [], {}
    for record in airports["records"]:
        if not isinstance(record, dict) or not _finite(record.get("lon"), -180, 180) or not _finite(record.get("lat"), -90, 90):
            continue
        if not (REGION[0] <= record["lon"] <= REGION[2] and REGION[1] <= record["lat"] <= REGION[3]):
            continue
        if record.get("status") != "OPEN" or not _finite(record.get("elevationFt"), -1500, 15000) or not record.get("faaId"):
            continue
        # Every open facility, public or private use, is projected and may anchor
        # its own airspace. Nearest-ground anchors skip heliports, whose
        # published elevation can be a rooftop rather than the ground.
        by_id[record["faaId"]] = (record["lon"], record["lat"], record["elevationFt"])
        facilities.append(_airport(record))
        if record.get("facilityType") != "HELIPORT":
            elevations.append((record["faaId"], record["lon"], record["lat"], record["elevationFt"]))

    volumes, rejects, class_a = [], [], None
    for index, feature in enumerate(airspace["features"]):
        props = feature.get("properties") if isinstance(feature, dict) else None
        if not isinstance(props, dict):
            raise ValueError("AIRSPACE_SHAPE_INVALID")
        kind = props.get("type")
        try:
            rings = _rings(feature.get("geometry"))
        except ValueError as error:
            rejects.append({"index": index, "type": kind, "reason": str(error)})
            continue
        if not _intersects(_bbox(rings)):
            continue
        if kind == "CLASS_A":
            class_a = {"floor": _bound(props["floor"]), "ceiling": _bound(props["ceiling"])}
            continue
        if kind not in VOLUME_TYPES:
            continue
        try:
            floor, ceiling = _bound(props.get("floor")), _bound(props.get("ceiling"))
        except ValueError as error:
            rejects.append({"index": index, "type": kind, "reason": str(error)})
            continue
        identifier = props.get("identifier") or ""
        xs, ys = [p[0] for p in rings[0][:-1]], [p[1] for p in rings[0][:-1]]
        cx, cy = sum(xs) / len(xs), sum(ys) / len(ys)
        if kind in AIRPORT_KEYED and identifier in by_id:
            ground = {"ft": round(by_id[identifier][2]), "method": "ASSOCIATED_AIRPORT", "airport": identifier, "distance_km": 0}
        elif elevations:
            near = min(elevations, key=lambda e: _distance_km(cx, cy, e[1], e[2]))
            ground = {"ft": round(near[3]), "method": "NEAREST_AIRPORT", "airport": near[0],
                      "distance_km": round(_distance_km(cx, cy, near[1], near[2]), 1)}
        else:
            ground = None
        volumes.append({"type": kind, "identifier": identifier, "name": props.get("name") or "",
                        "state": props.get("state"), "floor": floor, "ceiling": ceiling,
                        "schedule": props.get("scheduleDescription"), "controlling_facility": props.get("controllingFacility"),
                        "ground_reference": ground, "bbox": _bbox(rings), "rings": rings})
    if len(volumes) > MAX_VOLUMES:
        raise ValueError("VOLUME_BUDGET_EXCEEDED")
    order = {kind: n for n, kind in enumerate(VOLUME_TYPES)}
    volumes.sort(key=lambda v: (order[v["type"]], v["identifier"], v["name"], v["floor"]["value_ft"], canonical(v["rings"])))
    for volume in volumes:
        # Identity is the content: a boundary or limit change yields a new ID.
        volume["id"] = "faa-airspace:" + hashlib.sha256(canonical({k: volume[k] for k in ("type", "identifier", "name", "floor", "ceiling", "rings")})).hexdigest()[:16]
    facilities.sort(key=lambda a: a["faa_id"])
    routes = sorted((segment for record in airways["records"] if isinstance(record, dict) and record.get("type") in AIRWAY_TYPES
                     and isinstance(record.get("designation"), str) for segment in _airway_segments(record)),
                    key=lambda r: (r["type"], r["designation"], r["coords"]))
    payload = {"profile": PROFILE, "generator": VERSION, "nasr_cycle": cycle,
               "valid_from": effective.isoformat(), "valid_to_exclusive": (effective + timedelta(days=28)).isoformat(),
               "evidence_role": "EXTERNAL_CONTEXT_ONLY", "region_bbox": list(REGION),
               "source": {"authority": "FAA NASR 28-day subscription (14 CFR Part 71/73 airspace; APT airports)",
                          "nasr_url": "https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/",
                          "airspace": {**source["airspace"], "sha256": sha(airspace_gz)},
                          "airports": {**source["airports"], "sha256": sha(airports_gz)},
                          "airways": {**source["airways"], "sha256": sha(airways_gz)}},
               "limitations": ["Not for navigation, flight planning or UAS authorization. Check current FAA charts, NOTAMs, TFRs and B4UFLY/LAANC.",
                               "Temporary flight restrictions, NOTAM activations and UAS Facility Map grid ceilings are not included.",
                               "Private-use facilities need the owner's permission to land; listing one is not an invitation to use it.",
                               "Display heights above ground use an associated or nearest airport elevation; source limits keep their MSL/AGL/SFC reference.",
                               "Horizontal coordinates are NASR NAD83 values used as WGS84 for display (sub-metre difference in Kansas)."],
               "class_a": class_a, "volumes": volumes, "airports": facilities, "airways": routes,
               "airport_counts": {"public_use": sum(a["use"] == "PUBLIC" for a in facilities),
                                  "private_use": sum(a["use"] == "PRIVATE" for a in facilities)},
               "rejects": rejects}
    payload["product_id"] = sha(canonical(payload))
    return payload


def verify(product):
    """Integrity seal check for a committed product; not authentication of the FAA source."""
    subject = {k: v for k, v in product.items() if k != "product_id"}
    if product.get("profile") != PROFILE or product.get("evidence_role") != "EXTERNAL_CONTEXT_ONLY" or product.get("product_id") != sha(canonical(subject)):
        raise ValueError("PRODUCT_DIGEST_MISMATCH")
    return product


if __name__ == "__main__":
    import argparse
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("airspace_gz")
    parser.add_argument("airports_gz")
    parser.add_argument("airways_gz")
    parser.add_argument("output")
    parser.add_argument("--source", required=True, help="JSON {airspace|airports|airways: {package, version, integrity}}")
    args = parser.parse_args()
    out = Path(args.output)
    if out.exists():
        raise SystemExit("OUTPUT_EXISTS")
    result = prepare(Path(args.airspace_gz).read_bytes(), Path(args.airports_gz).read_bytes(), Path(args.airways_gz).read_bytes(),
                     json.loads(args.source))
    out.write_text(json.dumps(result, separators=(",", ":"), sort_keys=True) + "\n")
    print(json.dumps({"product_id": result["product_id"], "volumes": len(result["volumes"]),
                      "airports": len(result["airports"]), "airway_segments": len(result["airways"]), "rejects": len(result["rejects"]), "bytes": out.stat().st_size}))
