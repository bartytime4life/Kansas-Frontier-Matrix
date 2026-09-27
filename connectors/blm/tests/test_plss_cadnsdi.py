"""Deterministic synthetic tests; no BLM access, survey review, or title claim."""
import importlib.util
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[1] / "src/blm/plss_cadnsdi.py"
SPEC = importlib.util.spec_from_file_location("kfm_blm_plss_cadnsdi_tested", PATH)
pl = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = pl
SPEC.loader.exec_module(pl)
NOW = "2026-09-27T12:00:00Z"
URL = pl.query_url("township", offset=0, count=10)
SQUARE = [[-98.0, 38.0], [-97.9, 38.0], [-97.9, 38.1], [-98.0, 38.1], [-98.0, 38.0]]


def feature(object_id=1, identifier=None, ring=None, **properties):
    # Synthetic values only: not a real township, survey, or parcel.
    props = {"OBJECTID": object_id, "PLSSID": identifier or f"KS060{object_id:03d}S0010W0",
             "STATEABBR": "KS", "TWNSHPLAB": "SYNTHETIC"}
    props.update(properties)
    props = {k: v for k, v in props.items() if v is not ...}
    return {"type": "Feature", "geometry": {"type": "Polygon",
                                            "coordinates": [ring or SQUARE]},
            "properties": props}


def body(features=None, raw=None, **extra):
    payload = {"type": "FeatureCollection",
               "features": [feature()] if features is None else features, **extra}
    return (json.dumps(payload) if raw is None else raw).encode()


def parse(payload=None, url=URL):
    return pl.parse_page(body() if payload is None else payload, status=200, source_url=url,
                         retrieved_at=NOW)


class PlannerTests(unittest.TestCase):
    def test_canonical_url_round_trips(self):
        self.assertTrue(URL.startswith(
            "https://gis.blm.gov/arcgis/rest/services/Cadastral/BLM_Natl_PLSS_CadNSDI/"
            "MapServer/1/query?where=STATEABBR%3D%27KS%27"))
        self.assertEqual(pl.parse_request(URL), pl.QueryRequest("township", 0, 10))
        section = pl.query_url("first_division", offset=2000, count=1000)
        self.assertEqual(pl.parse_request(section), pl.QueryRequest("first_division", 2000, 1000))

    def test_bounded_planning(self):
        for kwargs, code in (({"layer": "parcels"}, "LAYER"), ({"offset": -1}, "OFFSET"),
                             ({"count": 0}, "PAGE_SIZE"), ({"count": 1001}, "PAGE_SIZE"),
                             ({"offset": True}, "OFFSET")):
            merged = {"layer": "township", "offset": 0, "count": 10, **kwargs}
            layer = merged.pop("layer")
            with self.subTest(kwargs=kwargs), self.assertRaises(pl.PlssInputError) as ctx:
                pl.query_url(layer, **merged)
            self.assertEqual(str(ctx.exception), code)

    def test_non_canonical_urls_are_refused(self):
        cases = {
            "SOURCE_URL": (URL.replace("gis.blm.gov", "example.org"), URL + "#x",
                           URL.replace("/query?", "/identify?"),
                           URL.replace("resultOffset=0", "resultOffset=x")),
            "LAYER": (URL.replace("/MapServer/1/", "/MapServer/7/"),),
            "SOURCE_URL_SCOPE": (URL.replace("%27KS%27", "%27NE%27"),
                                 URL.replace("f=geojson", "f=json"), URL + "&token=x",
                                 URL.replace("where=", "outFields=*&where=", 1)),
        }
        for code, urls in cases.items():
            for url in urls:
                with self.subTest(url=url), self.assertRaises(pl.PlssInputError) as ctx:
                    pl.parse_request(url)
                self.assertEqual(str(ctx.exception), code)


class ParserTests(unittest.TestCase):
    def test_features_are_reference_geometry_candidates(self):
        page = parse()
        item = page.features[0]
        self.assertEqual((item.object_id, item.identifier, item.geometry_type, item.ring_count,
                          item.route, item.source_role, item.title_authority),
                         (1, "KS060001S0010W0", "Polygon", 1, "RAW_CANDIDATE",
                          "REFERENCE_GEOMETRY_CANDIDATE", False))
        self.assertIn('"TWNSHPLAB":"SYNTHETIC"', item.raw_properties_json)
        self.assertFalse(page.more_pages)
        self.assertEqual((page.coverage, page.admission), ("NOT_ESTABLISHED", "NOT_ADMITTED"))

    def test_feature_level_quarantine(self):
        outside = [[-104.0, 38.0], [-103.9, 38.0], [-103.9, 38.1], [-104.0, 38.0]]
        page = parse(body([feature(1, ring=SQUARE[:-1]), feature(2, ring=outside)]))
        self.assertEqual([f.reasons for f in page.features],
                         [("RING_NOT_CLOSED",), ("GEOMETRY_OUTSIDE_KANSAS_EXTENT",)])
        self.assertTrue(all(f.route == "QUARANTINE_CANDIDATE" for f in page.features))

    def test_property_number_tokens_are_kept_exactly(self):
        raw = body([feature(GISACRE=0, TOWNSHIP=-0)]).decode().replace(
            '"GISACRE": 0', '"GISACRE": 23040.000000000000000001')
        item = parse(raw.encode()).features[0]
        self.assertIn('"GISACRE":"23040.000000000000000001"', item.raw_properties_json)
        raw = body([feature(TWNSHPNO=5)]).decode().replace('"TWNSHPNO": 5', '"TWNSHPNO": -0')
        self.assertIn('"TWNSHPNO":"-0"', parse(raw.encode()).features[0].raw_properties_json)
        self.assertIs(type(item.object_id), int)

    def test_out_of_range_numbers_reject_as_invalid_json(self):
        for token in ("1e" + "9" * 100, "1" * 5000):
            raw = body([feature(GISACRE=0)]).decode().replace('"GISACRE": 0',
                                                             '"GISACRE": ' + token)
            with self.subTest(token=token[:12]), self.assertRaises(pl.PlssInputError) as ctx:
                parse(raw.encode())
            self.assertEqual(str(ctx.exception), "INVALID_JSON")
        overflow = body([feature(ring=[[-98.0, 38.0], [-97.9, 38.0], [1e400, 38.1],
                                       [-98.0, 38.0]])]).decode()
        with self.assertRaises(pl.PlssInputError) as ctx:
            parse(overflow.replace("Infinity", "1e400").encode())
        self.assertEqual(str(ctx.exception), "GEOMETRY_SHAPE")

    def test_more_pages(self):
        self.assertTrue(parse(body(exceededTransferLimit=True)).more_pages)
        self.assertTrue(parse(body(properties={"exceededTransferLimit": True})).more_pages)
        self.assertFalse(parse(body(properties={"exceededTransferLimit": False})).more_pages)
        full = pl.query_url("township", offset=0, count=2)
        self.assertTrue(parse(body([feature(1), feature(2)]), url=full).more_pages)

    def test_scope_and_shape_drift_reject_whole_page(self):
        cases = {
            "STATE_SCOPE": body([feature(STATEABBR="NE")]),
            "IDENTIFIER": body([feature(PLSSID=...)]),
            "OBJECT_ID": body([feature(OBJECTID="1")]),
            "OBJECT_ID_ORDER": body([feature(2), feature(1)]),
            "DUPLICATE_IDENTIFIER": body([feature(1, "A"), feature(2, "A")]),
            "GEOMETRY_SHAPE": body([{**feature(), "geometry": {"type": "Point",
                                                               "coordinates": [-98, 38]}}]),
            "FEATURE_SHAPE": body([{"type": "Feature", "geometry": None}]),
            "SERVICE_ERROR": body(raw='{"error": {"code": 400}}'),
            "COLLECTION_SHAPE": body(raw='{"type": "Feature"}'),
            "INVALID_JSON": body(raw='{"type": "FeatureCollection", "features": [NaN]}'),
            "PAGE_BOUND": body([feature(i) for i in range(1, 12)]),
        }
        for code, payload in cases.items():
            with self.subTest(code=code), self.assertRaises(pl.PlssInputError) as ctx:
                parse(payload)
            self.assertEqual(str(ctx.exception), code)
        for payload, code in ((body(properties={"exceededTransferLimit": "yes"}),
                               "COLLECTION_SHAPE"),
                              (body(properties=[]), "COLLECTION_SHAPE"),
                              (body([feature(OBJECTID=True)]), "OBJECT_ID")):
            with self.subTest(code=code), self.assertRaises(pl.PlssInputError) as ctx:
                parse(payload)
            self.assertEqual(str(ctx.exception), code)
        for kwargs, code in (({"status": 500}, "HTTP_STATUS"),
                             ({"retrieved_at": "now"}, "UTC_TIME")):
            merged = {"status": 200, "source_url": URL, "retrieved_at": NOW, **kwargs}
            with self.subTest(code=code), self.assertRaises(pl.PlssInputError) as ctx:
                pl.parse_page(body(), **merged)
            self.assertEqual(str(ctx.exception), code)


class NoNetworkTests(unittest.TestCase):
    def test_module_never_opens_sockets(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            parse()


if __name__ == "__main__":
    unittest.main()
