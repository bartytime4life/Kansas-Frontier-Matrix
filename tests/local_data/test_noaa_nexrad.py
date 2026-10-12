"""Deterministic NEXRAD Level III decoding, storage-cap and capture-boundary tests."""
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from connectors.noaa.src.noaa import nexrad_level3 as s
from tools.local_data import noaa_nexrad as op
from tools.local_data.manage import init_store

FIXTURES = Path(__file__).resolve().parents[2] / "connectors/noaa/tests/fixtures/nexrad_level3"
RUN = "20261007T180000Z"
DAY = "2024-05-19"
NST, NMD = "ICT_NST_2024_05_19_23_16_04", "ICT_NMD_2024_05_19_23_16_04"


def fixture(key):
    return (FIXTURES / key.lower()).read_bytes()


def listing(radar, product):
    key = {"NST": NST, "NMD": NMD}[product] if radar == "ICT" else None
    rows = f"<Contents><Key>{key}</Key><Size>{len(fixture(key))}</Size></Contents>" if key else ""
    return f'<?xml version="1.0"?><ListBucketResult>{rows}<IsTruncated>false</IsTruncated></ListBucketResult>'.encode()


def getter(url, limit):
    radar, product = url.split("prefix=")[1][:3], url.split("prefix=")[1][4:7]
    return listing(radar, product), {"source_url": url}


def provider(key, limit):
    return fixture(key), {"source_url": s.object_url(key), "retrieved_at": "2026-10-07T18:00:00Z",
                          "etag": None, "last_modified": None, "provider_checksum": None}


class DecoderTests(unittest.TestCase):
    def test_storm_cells_have_positions_tracks_and_motion(self):
        parsed = s.parse_product(fixture(NST), NST)
        self.assertEqual(parsed["volume_time"], "2024-05-19T23:16:04Z")
        self.assertEqual(parsed["radar"], "KICT")
        cells = {cell["storm_id"]: cell for cell in parsed["detections"]}
        self.assertEqual(len(cells), 34)
        self.assertIsNone(cells["K7"]["forecast"] or None)
        cell = cells["X6"]
        # Within Kansas and north-northwest of Wichita (~60 nm, near McPherson).
        self.assertTrue(-98.2 < cell["position"][0] < -97.2 and 38.2 < cell["position"][1] < 38.9)
        self.assertTrue(cell["past"] and cell["forecast"])
        self.assertEqual(cell["motion"]["toward"], s._compass(cell["motion"]["toward_deg"]))

    def test_busy_volume_merges_truncated_text_table(self):
        parsed = s.parse_product(fixture("DDC_NST_2024_05_19_22_03_21"), "DDC_NST_2024_05_19_22_03_21")
        self.assertEqual(len(parsed["detections"]), 38)
        self.assertEqual(sum(not cell["in_text_table"] for cell in parsed["detections"]), 4)

    def test_rotation_classes_and_tornado_signature_flag(self):
        parsed = s.parse_product(fixture(NMD), NMD)
        classes = {item["rotation_class"] for item in parsed["detections"]}
        self.assertIn("tornado_signature", classes)
        self.assertTrue(all(item["tvs"] == (item["rotation_class"] == "tornado_signature") for item in parsed["detections"]))
        self.assertTrue(all("not a confirmed tornado" in s.ROTATION_LABELS[c] for c in classes if c == "tornado_signature"))

    def test_empty_product_is_valid_and_has_no_detections(self):
        key = "ICT_NMD_2024_05_06_18_47_19"
        self.assertEqual(s.parse_product(fixture(key), key)["detections"], [])

    def test_identity_time_and_truncation_are_rejected(self):
        body = fixture(NST)
        for raw, key in [(body, "DDC_NST_2024_05_19_23_16_04"), (body, "ICT_NST_2024_05_19_23_16_05"),
                         (body, NMD), (body[:-40], NST), (b"x" + body, NST)]:
            with self.assertRaises((ValueError, UnicodeDecodeError)):
                s.parse_product(raw, key)

    def test_fixed_keys_and_listing_scope(self):
        for key in ("../secret", "ICT_N0B_2024_05_19_23_16_04", "ABC_NST_2024_05_19_23_16_04", NST + "?x=1"):
            with self.assertRaises(ValueError):
                s.object_url(key)
        other_day = listing("ICT", "NST").replace(b"2024_05_19", b"2024_05_20")
        with self.assertRaises(ValueError):
            s.parse_listing(other_day, "ICT", "NST", DAY)
        with self.assertRaises(ValueError):
            s.parse_listing(b"<!DOCTYPE x><ListBucketResult/>", "ICT", "NST", DAY)

    def test_transport_rejects_oversize_and_redirect(self):
        class Response(io.BytesIO):
            status = 200
            def geturl(self):
                return self.url
        for body, declared, url in [(b"x", "999999", s.object_url(NST)), (b"xx", "1", s.object_url(NST)),
                                    (b"x", "1", "https://other.invalid/" + NST)]:
            response = Response(body)
            response.headers = {"Content-Length": declared}
            response.url = url
            with patch.object(s, "build_opener") as opener:
                opener.return_value.open.return_value = response
                with self.assertRaises(ValueError):
                    s.fetch(NST, 1000)

    def test_compact_feature_collection(self):
        collection = s.feature_collection([s.parse_product(fixture(NST), NST), s.parse_product(fixture(NMD), NMD)], "t")
        self.assertFalse(collection["released"])
        kinds = {feature["properties"]["kind"] for feature in collection["features"]}
        self.assertTrue({"storm_cell", "rotation", "storm_past_track", "storm_forecast_track"} <= kinds)
        for feature in collection["features"]:
            for value in feature["geometry"]["coordinates"] if feature["geometry"]["type"] == "LineString" else [feature["geometry"]["coordinates"]]:
                self.assertEqual(value, [round(value[0], 3), round(value[1], 3)])


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "store"
        init_store(self.root)
        self.free = patch.object(op.shutil, "disk_usage", return_value=type("Disk", (), {"free": 2**42})())
        self.free.start()
        self.addCleanup(self.free.stop)

    def prepare(self, **kwargs):
        return op.prepare(self.root, RUN, DAY, getter=getter, **kwargs)

    def test_plan_downloads_no_products_and_respects_hour_window(self):
        plan = self.prepare(start_hour=23, hours=1)
        self.assertEqual(plan["selected_products"], 2)
        self.assertFalse(any(op.paths(self.root, RUN)[0].glob("*")) if op.paths(self.root, RUN)[0].exists() else False)
        other = op.prepare(self.root, "20261007T180001Z", DAY, start_hour=0, hours=6, getter=getter)
        self.assertEqual(other["selected_products"], 0)

    def test_capture_verify_and_no_redownload_on_retry(self):
        self.prepare()
        report = op.capture(self.root, RUN, fetcher=provider)
        self.assertEqual(report["status"], "CAPTURED_UNREVIEWED")
        self.assertFalse(report["released"])
        result = op.verify(self.root, RUN)
        self.assertEqual(result["status"], "VERIFIED_CAPTURE")
        self.assertGreater(result["rotation_classes"]["tornado_signature"], 0)
        index = json.loads(Path(result["index"]).read_text())
        self.assertEqual(index["review_status"], "unreviewed")
        with patch.object(op.source, "utc_now", return_value="2026-10-07T18:30:00Z"):
            again = op.capture(self.root, RUN, fetcher=lambda *args: self.fail("must reuse"))
        self.assertEqual(again["captured_products"], 2)
        self.assertEqual(len(list(Path(result["index"]).parent.glob("storm-detections-*.geojson"))), 1)

    def test_tamper_is_rejected(self):
        self.prepare()
        op.capture(self.root, RUN, fetcher=provider)
        (op.paths(self.root, RUN)[0] / NST).write_bytes(b"bad")
        with self.assertRaises(ValueError):
            op.verify(self.root, RUN)

    def test_storage_cap_and_reserve_stop_before_any_listing(self):
        with self.assertRaisesRegex(ValueError, "SOURCE_STORAGE_CAP"):
            op.prepare(self.root, RUN, DAY, cap=100, getter=lambda *args: self.fail("no network"))
        with patch.object(op.shutil, "disk_usage", return_value=type("Disk", (), {"free": 100})()):
            with self.assertRaisesRegex(ValueError, "FREE_SPACE_RESERVE"):
                self.prepare()

    def test_bad_product_is_partial_not_saved(self):
        self.prepare()
        report = op.capture(self.root, RUN, fetcher=lambda key, limit: (b"junk", {}))
        self.assertEqual(report["status"], "PARTIAL")
        self.assertEqual(report["failure_count"], 2)
        self.assertFalse((op.paths(self.root, RUN)[0] / NST).exists())

    def test_binary_decoder_error_is_a_failed_product_and_run_resumes(self):
        self.prepare()
        def broken(*args):
            raise s.struct.error("unpack requires a buffer of 6 bytes")
        with patch.object(op.source, "_storm_geometry", side_effect=broken):
            report = op.capture(self.root, RUN, fetcher=provider)
        self.assertEqual(report["status"], "PARTIAL")
        self.assertEqual([f["key"] for f in report["failures"]], [NST])
        with patch.object(op.source, "utc_now", return_value="2026-10-07T18:30:00Z"):
            again = op.capture(self.root, RUN, fetcher=provider)
        self.assertEqual(again["status"], "CAPTURED_UNREVIEWED")

    def test_body_that_differs_from_planned_size_is_rejected(self):
        self.prepare()
        report = op.capture(self.root, RUN, fetcher=lambda key, limit: (fixture(key) + b"x", {}))
        self.assertEqual(report["failure_count"], 2)
        self.assertTrue(all("SIZE_DIFFERS_FROM_PLAN" in f["error_type"] for f in report["failures"]))
        self.assertFalse((op.paths(self.root, RUN)[0] / NST).exists())

    def test_invalid_selection_and_traversal_denied(self):
        for kwargs in ({"radars": ["XXX"]}, {"products": ["N0B"]}, {"start_hour": 20, "hours": 6}):
            with self.assertRaises(ValueError):
                self.prepare(**kwargs)
        with self.assertRaises(ValueError):
            op.paths(self.root, "../escape")
        with self.assertRaises(ValueError):
            op.prepare(self.root, RUN, "2024-02-30", getter=getter)


if __name__ == "__main__":
    unittest.main()
