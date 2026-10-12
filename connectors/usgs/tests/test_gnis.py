"""Synthetic GNIS capture tests; live provider checks are separate."""

import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

PATH = Path(__file__).resolve().parents[1] / "src/usgs/gnis.py"
SPEC = importlib.util.spec_from_file_location("kfm_gnis_tested", PATH)
gnis = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = gnis
SPEC.loader.exec_module(gnis)


def feature(identifier=485477, name="Topeka", state="KS"):
    return {"type": "Feature", "geometry": {"type": "MultiPoint", "coordinates": [[-95.67, 39.04], [-95.75, 39.04]]},
            "properties": {"gaz_id": identifier, "gaz_name": name, "gaz_featureclass": "Populated Place", "state_alpha": state, "county_name": "Shawnee"}}


def body(features, **extra):
    return json.dumps({"type": "FeatureCollection", "features": features, **extra}).encode()


class GnisTest(unittest.TestCase):
    def test_query_fixed_to_kansas_and_name(self):
        url = urlsplit(gnis.query_url("Topeka"))
        self.assertEqual(url.netloc, "carto.nationalmap.gov")
        self.assertEqual(parse_qs(url.query)["where"], ["gaz_name = 'Topeka' AND state_alpha = 'KS'"])
        for invalid in ("Topeka' OR 1=1", "../Kansas", " https://x", "A" * 121):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                gnis.query_url(invalid)

    def test_capture_preserves_original_and_holds_release(self):
        raw = body([feature()])
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "capture"
            result = gnis.capture("Topeka", target, lambda _url: (200, raw, "application/geo+json"),
                                  lambda: datetime(2026, 9, 30, tzinfo=timezone.utc))
            self.assertEqual(result["state"], "CANDIDATE")
            self.assertEqual(result["release_state"], "UNRELEASED")
            self.assertEqual(result["source_admission"], "PENDING")
            self.assertEqual((target / "source.geojson").read_bytes(), raw)
            self.assertEqual(len(result["records"]), 1)
            self.assertEqual(result["records"][0]["geometry_role"], "GNIS representative location; not a place boundary")

    def test_out_of_scope_ambiguity_and_provider_errors(self):
        with self.assertRaisesRegex(ValueError, "FEATURE_SCOPE"):
            gnis.parse(body([feature(state="OK")]), "Topeka")
        self.assertEqual(gnis.parse(body([feature(), feature(123)]), "Topeka")[0], "AMBIGUOUS_HOLD")
        for raw in (b'{"error":{"code":400}}', body([feature()], exceededTransferLimit=True), body([feature(identifier=1, name="Kansas")])):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                gnis.parse(raw, "Topeka")
        with tempfile.TemporaryDirectory() as tmp:
            result = gnis.capture("Topeka", Path(tmp) / "bad", lambda _url: (200, b'{"error":{"code":400}}', "application/json"))
            self.assertEqual((result["state"], result["reason_code"]), ("INCOMPLETE", "PROVIDER_RESPONSE_INVALID"))
            self.assertEqual(result["release_state"], "UNRELEASED")


if __name__ == "__main__":
    unittest.main()
