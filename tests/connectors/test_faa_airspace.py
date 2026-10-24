"""Synthetic FAA airspace/airport/airway coverage; no provider calls or release grants."""
from copy import deepcopy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("faa_airspace", ROOT / "pipelines/domains/roads-rail-trade/faa_airspace.py")
airspace = importlib.util.module_from_spec(spec)
spec.loader.exec_module(airspace)
SOURCE = {k: {"package": "@example/" + k, "version": "1.0.0", "integrity": "sha512-test"} for k in ("airspace", "airports", "airways")}
PRODUCT = ROOT / "apps/site/source/public/data/aviation/kansas-aviation-context.json"


def square(lon, lat, size=0.1):
    return {"type": "Polygon", "coordinates": [[[lon, lat], [lon + size, lat], [lon + size, lat + size], [lon, lat + size], [lon, lat]]]}


def volume(kind="CLASS_D", identifier="ZZZ", floor=(0, "SFC"), ceiling=(3800, "MSL"), geometry=None, **extra):
    return {"type": "Feature", "geometry": geometry or square(-97.7, 38.7),
            "properties": {"type": kind, "name": "SYNTHETIC " + kind, "identifier": identifier,
                           "floor": {"valueFt": floor[0], "reference": floor[1]},
                           "ceiling": {"valueFt": ceiling[0], "reference": ceiling[1], **extra},
                           "state": "KS", "controllingFacility": None, "scheduleDescription": None}}


def airport(faa_id="ZZZ", use="PUBLIC", lon=-97.65, lat=38.75, elevation=1288, **extra):
    return {"faaId": faa_id, "name": "SYNTHETIC " + faa_id, "facilityType": "AIRPORT", "ownershipType": "PUBLIC", "useType": use,
            "status": "OPEN", "city": "TEST", "county": "TEST", "state": "KS", "lat": lat, "lon": lon, "elevationFt": elevation,
            "towerType": "ATCT", "runways": [{"id": "17/35", "lengthFt": 6000, "widthFt": 100, "surfaceType": "ASPH",
                                              "ends": [{"id": "17", "lat": lat + 0.01, "lon": lon}, {"id": "35", "lat": lat - 0.01, "lon": lon}]}],
            "frequencies": [{"frequencyMhz": 118.7, "use": "CTAF"}, {"frequencyMhz": 120.0, "use": faa_id + " ASOS", "remark": "PHONE 555"}],
            **extra}


def inputs(features=None, airports=None, routes=None, cycle="2026-10-29", airport_cycle=None):
    a = {"type": "FeatureCollection", "properties": {"nasrCycleDate": cycle},
         "features": features if features is not None else [volume(), volume("CLASS_A", "", (18000, "MSL"), (60000, "MSL"), square(-100, 37, 3))]}
    p = {"meta": {"nasrCycleDate": airport_cycle or cycle}, "records": airports if airports is not None else [airport(), airport("PVT", "PRIVATE", -97.0, 38.0, 1500)]}
    w = {"meta": {"nasrCycleDate": cycle}, "records": routes if routes is not None else [
        {"designation": "V4", "type": "VICTOR", "waypoints": [{"identifier": "AAA", "lon": -98.0, "lat": 38.0, "minimumEnrouteAltitudeFt": 4000, "maximumAuthorizedAltitudeFt": 17999},
                                                             {"identifier": "BBB", "lon": -97.0, "lat": 38.5}]},
        {"designation": "J99", "type": "JET", "waypoints": [{"identifier": "FAR", "lon": -80.0, "lat": 30.0}, {"identifier": "AWY", "lon": -79.0, "lat": 30.0}]}]}
    return [gzip.compress(json.dumps(x).encode()) for x in (a, p, w)]


def test_deterministic_product_keeps_vertical_references_and_cycle_validity():
    first, second = airspace.prepare(*inputs(), SOURCE), airspace.prepare(*inputs(), SOURCE)
    assert first == second and airspace.verify(first) is first
    assert (first["valid_from"], first["valid_to_exclusive"]) == ("2026-10-29", "2026-11-26")
    assert first["evidence_role"] == "EXTERNAL_CONTEXT_ONLY"
    assert first["class_a"] == {"floor": {"value_ft": 18000, "reference": "MSL"}, "ceiling": {"value_ft": 60000, "reference": "MSL"}}
    [d] = first["volumes"]
    assert d["floor"] == {"value_ft": 0, "reference": "SFC"} and d["ceiling"] == {"value_ft": 3800, "reference": "MSL"}
    assert d["ground_reference"] == {"ft": 1288, "method": "ASSOCIATED_AIRPORT", "airport": "ZZZ", "distance_km": 0}
    assert d["id"].startswith("faa-airspace:")
    assert first["source"]["airspace"]["sha256"].startswith("sha256:")


def test_private_use_facilities_are_flagged_and_anchor_ground_except_heliports():
    moa = [volume("MOA", "MTEST", (500, "AGL"), (18000, "MSL"), square(-97.05, 37.95, 0.1), inclusive=False)]
    product = airspace.prepare(*inputs(features=moa), SOURCE)
    assert [(a["faa_id"], a["use"]) for a in product["airports"]] == [("PVT", "PRIVATE"), ("ZZZ", "PUBLIC")]
    assert product["airport_counts"] == {"public_use": 1, "private_use": 1} and "withheld" not in product
    ground = product["volumes"][0]["ground_reference"]
    assert ground["method"] == "NEAREST_AIRPORT" and ground["airport"] == "PVT" and ground["ft"] == 1500
    assert product["volumes"][0]["ceiling"]["inclusive"] is False
    # A heliport's published elevation can be a rooftop: listed, but never the nearest-ground anchor.
    heliport = airspace.prepare(*inputs(features=moa, airports=[airport(), airport("H1", "PRIVATE", -97.0, 38.0, 1900, facilityType="HELIPORT")]), SOURCE)
    assert [a["faa_id"] for a in heliport["airports"]] == ["H1", "ZZZ"]
    assert heliport["volumes"][0]["ground_reference"]["airport"] == "ZZZ"


def test_airport_projection_drops_remarks_and_parses_weather_station():
    [a] = [item for item in airspace.prepare(*inputs(), SOURCE)["airports"] if item["faa_id"] == "ZZZ"]
    assert a["weather_station"] == "ASOS" and a["ctaf_mhz"] == 118.7
    assert "PHONE" not in json.dumps(a) and "frequencies" not in a
    assert a["runways"][0]["length_ft"] == 6000 and len(a["runways"][0]["ends"]) == 2


def test_airways_keep_only_region_segments_with_leg_altitudes():
    routes = airspace.prepare(*inputs(), SOURCE)["airways"]
    assert [(r["designation"], r["from"], r["to"], r["mea_ft"], r["maa_ft"]) for r in routes] == [("V4", "AAA", "BBB", 4000, 17999)]


def test_outside_region_and_unlisted_types_are_dropped_not_clipped():
    far = volume(geometry=square(-80, 30))
    artcc = volume("ARTCC", "ZKC", geometry=square(-98, 38))
    product = airspace.prepare(*inputs(features=[far, artcc, volume()]), SOURCE)
    assert len(product["volumes"]) == 1 and product["volumes"][0]["rings"][0][0] == [-97.7, 38.7]


@pytest.mark.parametrize("change,reason", [
    (lambda f: f["properties"]["floor"].update(reference="FL"), "VERTICAL_BOUND_INVALID"),
    (lambda f: f["properties"]["ceiling"].update(valueFt=float("nan")), "VERTICAL_BOUND_INVALID"),
    (lambda f: f["properties"]["floor"].update(valueFt=100), "VERTICAL_BOUND_INVALID"),
    (lambda f: f["geometry"]["coordinates"][0].pop(), "GEOMETRY_INVALID"),
    (lambda f: f["geometry"].update(type="MultiPolygon"), "GEOMETRY_INVALID"),
])
def test_bad_volumes_are_reported_not_silently_drawn(change, reason):
    bad = volume()
    change(bad)
    product = airspace.prepare(*inputs(features=[bad]), SOURCE)
    assert not product["volumes"] and product["rejects"][0]["reason"] == reason


@pytest.mark.parametrize("kwargs,error", [({"airport_cycle": "2026-10-01"}, "CYCLE_MISMATCH")])
def test_mixed_cycles_fail_whole_run(kwargs, error):
    with pytest.raises(ValueError, match=error):
        airspace.prepare(*inputs(**kwargs), SOURCE)


def test_source_binding_required_for_every_input():
    with pytest.raises(ValueError, match="SOURCE_BINDING_INVALID"):
        airspace.prepare(*inputs(), {k: v for k, v in SOURCE.items() if k != "airways"})


def test_tampered_product_fails_seal():
    product = deepcopy(airspace.prepare(*inputs(), SOURCE))
    product["volumes"][0]["ceiling"]["value_ft"] = 9999
    with pytest.raises(ValueError, match="PRODUCT_DIGEST_MISMATCH"):
        airspace.verify(product)


def test_committed_site_product_is_sealed_and_kansas_scoped():
    product = airspace.verify(json.loads(PRODUCT.read_text()))
    assert product["nasr_cycle"] == "2026-10-29" and product["rejects"] == []
    ids = {(v["type"], v["identifier"]) for v in product["volumes"]}
    assert {("CLASS_C", "ICT"), ("CLASS_D", "SLN"), ("RESTRICTED", "R3602A"), ("CLASS_B", "MCI")} <= ids
    assert all(a["faa_id"] and a["elevation_ft"] is not None for a in product["airports"])
    counts = product["airport_counts"]
    assert counts["private_use"] > 300 and counts["public_use"] > 150
    assert counts["public_use"] + counts["private_use"] == len(product["airports"])
    # The Site pins this digest; changing the file without the pin must fail.
    pin = (ROOT / "apps/site/source/app/aviation-airspace.ts").read_text()
    assert hashlib.sha256(PRODUCT.read_bytes()).hexdigest() in pin


def test_committed_and_synthetic_products_match_schema():
    jsonschema = pytest.importorskip("jsonschema")
    schema = json.loads((ROOT / "schemas/contracts/v1/domains/roads-rail-trade/faa_airspace_context.schema.json").read_text())
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(schema)
    for product in (json.loads(PRODUCT.read_text()), airspace.prepare(*inputs(), SOURCE)):
        errors = sorted(validator.iter_errors(product), key=lambda e: list(e.path))
        assert not errors, errors[0].message
