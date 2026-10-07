"""Offline bounds, immutable capture, geometry join and model-time regressions."""
from datetime import datetime, timedelta, timezone
import gzip
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from connectors.noaa.src.noaa import nwm as s
from pipelines.domains.hydrology import nwm_subset as p
from tools.local_data import noaa_nwm as op
from tools.local_data.manage import init_store

RUN = "20261007T180550Z"


def page():
    return {"geometryType": "esriGeometryPolyline", "spatialReference": {"wkid": 4326},
            "features": [{"attributes": {"oid": 1, "feature_id": "10", "nwm_vers": 3.0},
                          "geometry": {"paths": [[[-98, 38], [-97.9, 38.1]]]}}]}


def listing():
    return "".join(f'<a href="{i["name"]}">' for i in s.model_objects("20261007", 16)[1:]).encode()


def fake_fetch(url, limit, *, head=False):
    if url == s.BASE:
        body = b'<a href="nwm.20261007/">'
    elif url.endswith("short_range/"):
        body = listing()
    elif url == s.ids_url():
        body = b'{"objectIdFieldName":"oid","objectIds":[1]}'
    elif url == s.FLOWLINES+"?f=json":
        body = b'{"objectIdField":"oid"}'
    elif url == s.page_url([1]):
        body = json.dumps(page()).encode()
    else:
        body = b"source-bytes"
    return (b"" if head else body), {"source_url": url, "declared_bytes": len(body),
        "retrieved_at": "2026-10-07T18:00:00Z", "last_modified": "fixed", "etag": None, "provider_checksum": None}


class SourceTests(unittest.TestCase):
    def test_latest_complete_cycle_ignores_partial_new_cycle(self):
        self.assertEqual(s.latest_complete_cycle(listing()+b'<a href="nwm.t17z.short_range.channel_rt.f001.conus.nc">'), 16)
        with self.assertRaisesRegex(ValueError, "NO_COMPLETE"):
            s.latest_complete_cycle(b'<a href="nwm.t17z.short_range.channel_rt.f001.conus.nc">')

    def test_cycle_rollover_and_request_allowlist(self):
        specs = s.model_objects("20261231", 23)
        self.assertEqual(specs[-1]["valid_time"], "2027-01-01T17:00:00Z")
        self.assertNotIn("reference_time", specs[0])  # filename cycle is not initialization
        for url in (s.BASE, s.ids_url(), s.page_url([1, 2]), *(v["url"] for v in specs)):
            self.assertTrue(s.allowed_url(url))
        for url in (s.BASE+"../secret", s.BASE+"nwm.20261007/forcing/", "https://evil.invalid/", s.BASE+"?redirect=evil"):
            self.assertFalse(s.allowed_url(url))
        with self.assertRaises(ValueError):
            s.model_objects("20260230", 25)

    def test_ids_reject_truncation_duplicate_and_empty(self):
        for obj in ({"objectIdFieldName": "oid", "objectIds": []},
                    {"objectIdFieldName": "oid", "objectIds": [1, 1]},
                    {"objectIdFieldName": "oid", "objectIds": [1], "exceededTransferLimit": True}):
            with self.assertRaises(ValueError):
                s.object_ids(json.dumps(obj).encode())

    def test_http_padding_limits_short_bodies_and_no_redirect(self):
        class Response(io.BytesIO):
            status = 200
            def geturl(self):
                return self.url
        for data, size, url, fails in [(b"ab", "2     ", s.BASE, False),
                                       (b"ab", "3", s.BASE, True), (b"abcd", None, s.BASE, True),
                                       (b"ab", "2", "https://evil.invalid", True)]:
            response = Response(data)
            response.url = url
            response.headers = {} if size is None else {"Content-Length": size}
            with patch.object(s, "build_opener") as opener:
                opener.return_value.open.return_value = response
                if fails:
                    with self.assertRaises(ValueError):
                        s.fetch(s.BASE, 3)
                else:
                    self.assertEqual(s.fetch(s.BASE, 3)[0], data)

    def test_unknown_head_size_and_unsafe_url_stop(self):
        with patch.object(s, "build_opener") as opener:
            with self.assertRaises(ValueError):
                s.fetch("https://evil.invalid", 8)
            opener.assert_not_called()
        response = unittest.mock.MagicMock()
        response.__enter__.return_value = response
        response.status = 200
        response.geturl.return_value = s.BASE
        response.headers = {}
        with patch.object(s, "build_opener") as opener:
            opener.return_value.open.return_value = response
            with self.assertRaisesRegex(ValueError, "SOURCE_SIZE_UNKNOWN"):
                s.fetch(s.BASE, 8, head=True)
        with self.assertRaises(ValueError):
            s.page_url([True])


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)/"store"
        init_store(self.root)
        # Deterministic offline free-space checks, independent of CI disk size.
        self.disk = patch.object(op.shutil, "disk_usage", return_value=type("Disk", (), {"free": 1024**4})())
        self.disk.start()
        self.addCleanup(self.disk.stop)

    def prepare(self):
        return op.prepare(self.root, RUN, fetcher=fake_fetch)

    def test_prepare_only_metadata_then_idempotent_capture(self):
        plan = self.prepare()
        self.assertEqual(len(plan["models"]), 19)
        raw, _, _ = op.paths(self.root, RUN)
        self.assertFalse((raw/"models").exists())
        with patch("builtins.print"):
            report = op.capture(self.root, RUN, fetcher=fake_fetch)
            def forbidden(*args, **kwargs):
                self.fail("Unexpected repeat network transfer")
            self.assertEqual(op.capture(self.root, RUN, fetcher=forbidden), report)
        self.assertFalse(report["source_admitted"])

    def test_storage_and_free_reserve_stop_before_fetch(self):
        with patch.object(op, "CAP", 1), patch.object(s, "fetch") as fetch:
            with self.assertRaisesRegex(ValueError, "SOURCE_STORAGE_CAP"):
                op.prepare(self.root, RUN, fetcher=fetch)
            fetch.assert_not_called()
        with patch.object(op.shutil, "disk_usage", return_value=type("Disk", (), {"free": 0})()):
            with self.assertRaisesRegex(ValueError, "FREE_SPACE_RESERVE"):
                self.prepare()

    def test_corruption_and_symlink_rejected(self):
        plan = self.prepare()
        ref = plan["metadata"]["prod.html"]
        (self.root/ref["path"]).write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "CAPTURE_HASH_MISMATCH"):
            op.load_plan(self.root, RUN)
        raw, _, _ = op.paths(self.root, RUN)
        (raw/"unsafe").symlink_to(self.root/ref["path"])
        with self.assertRaisesRegex(ValueError, "SOURCE_STORE_UNSAFE_FILE"):
            op.usage(self.root)

    def test_unreceipted_source_is_preserved_for_inspection(self):
        plan = self.prepare()
        raw, _, _ = op.paths(self.root, RUN)
        path = raw/"models"/plan["models"][0]["name"]
        path.parent.mkdir()
        path.write_bytes(b"interrupted capture")
        with self.assertRaisesRegex(ValueError, "UNRECEIPTED_CAPTURE"):
            op.capture(self.root, RUN, fetcher=fake_fetch)
        self.assertEqual(path.read_bytes(), b"interrupted capture")

    def test_mutated_plan_model_or_geometry_ids_rejected(self):
        plan = self.prepare()
        _, work, _ = op.paths(self.root, RUN)
        plan["object_ids"] = [2]
        (work/"plan-v2.json").write_text(json.dumps(plan))
        with self.assertRaisesRegex(ValueError, "PLAN_GEOMETRY_IDS"):
            op.load_plan(self.root, RUN)

    def test_source_change_and_truncated_geometry_not_complete(self):
        self.prepare()
        def changed(url, limit, **kwargs):
            body, head = fake_fetch(url, limit, **kwargs)
            head["last_modified"] = "changed"
            return body, head
        with self.assertRaisesRegex(ValueError, "SOURCE_CHANGED_SINCE_PLAN"):
            op.capture(self.root, RUN, fetcher=changed)
        def truncated(url, limit, **kwargs):
            body, head = fake_fetch(url, limit, **kwargs)
            if url == s.page_url([1]):
                obj = page(); obj["exceededTransferLimit"] = True
                body = json.dumps(obj).encode()
            return body, head
        with patch("builtins.print"), self.assertRaisesRegex(ValueError, "FLOWLINE_PAGE_INCOMPLETE"):
            op.capture(self.root, RUN, fetcher=truncated)
        self.assertFalse(list(op.paths(self.root, RUN)[2].glob("capture-*.json")))

    def test_unknown_retained_files_count_toward_all_runs(self):
        raw, _, _ = op.paths(self.root, RUN)
        raw.mkdir(parents=True)
        (raw/"unknown").write_bytes(b"x"*100)
        self.assertGreaterEqual(op.usage(self.root), 100)
        with patch.object(op, "CAP", op.usage(self.root)+op.REPORT_RESERVE):
            with self.assertRaises(ValueError):
                op.room(self.root, 1)


class GeometryTests(unittest.TestCase):
    def test_exact_geometry_set_versions_and_no_clip(self):
        features, versions = p.geometry([page()], [1])
        self.assertEqual(versions, {"3.0": 1})
        self.assertEqual(features["10"]["geometry"]["coordinates"], page()["features"][0]["geometry"]["paths"])

    def test_bad_crs_duplicate_coordinates_and_selection(self):
        for change in ("crs", "duplicate", "coordinates", "ids"):
            obj = page()
            if change == "crs": obj["spatialReference"]["wkid"] = 3857
            if change == "duplicate": obj["features"] *= 2
            if change == "coordinates": obj["features"][0]["geometry"]["paths"][0][0][0] = float("nan")
            with self.assertRaises(ValueError):
                p.geometry([obj], [2] if change == "ids" else [1])


class NetCDFTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            import netCDF4
            import numpy
        except ImportError:
            raise unittest.SkipTest("Install the optional NWM requirements to validate binary fixtures")

    def fixture(self, spec, *, ids=(20, 10), valid=None, units="m3 s-1"):
        import netCDF4
        import numpy as np
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)/"frame.nc"
            with netCDF4.Dataset(path, "w") as d:
                d.createDimension("feature_id", len(ids)); d.createDimension("time", 1)
                d.model_output_type = "channel_rt"
                d.model_configuration = "short_range" if spec["product"] == "short_range" else "analysis_and_assimilation"
                d.NWM_version_number = "v3.1"
                ref = datetime.fromisoformat(spec["filename_cycle_time"].replace("Z", "+00:00"))
                if spec["product"] == "analysis_assim": ref -= timedelta(hours=3)
                when = datetime.fromisoformat((valid or spec["valid_time"]).replace("Z", "+00:00"))
                d.model_initialization_time = ref.strftime("%Y-%m-%d_%H:%M:%S")
                d.model_output_valid_time = when.strftime("%Y-%m-%d_%H:%M:%S")
                for name, value in [("reference_time", ref), ("time", when)]:
                    v = d.createVariable(name, "i4", ("time",)); v.units = "minutes since 1970-01-01 00:00:00 UTC"
                    v[:] = [int(value.timestamp()/60)]
                d.createVariable("feature_id", "i8", ("feature_id",))[:] = ids
                for name, unit in p.VARIABLES.items():
                    v = d.createVariable(name, "i4", ("feature_id",), fill_value=-9999)
                    v.units = units if name == "streamflow" else unit
                    v.scale_factor = np.float32(.01); v.add_offset = np.float32(0)
                    v.missing_value = -9999; v.valid_range = np.array([0, 1000], dtype=np.int32)
                    v.set_auto_maskandscale(False)
                    v[:] = [-9999, 123]
            return path.read_bytes()

    def test_join_by_id_packing_and_analysis_initialization(self):
        spec = s.model_objects("20261007", 16)[0]
        meta, arrays = p.frame(self.fixture(spec), spec, ["10", "20"])
        self.assertEqual(meta["reference_time"], "2026-10-07T13:00:00Z")
        self.assertEqual(meta["valid_time"], "2026-10-07T16:00:00Z")
        self.assertEqual(arrays["streamflow"][0].tolist(), [123, -9999])
        self.assertEqual(arrays["streamflow"][2].tolist(), ["valid", "missing"])
        self.assertAlmostEqual(arrays["streamflow"][1][0], 1.23, places=6)

    def test_wrong_time_units_missing_and_duplicate_ids_fail(self):
        spec = s.model_objects("20261007", 16)[1]
        for kwargs, ids in [({"valid": "2026-10-07T18:00:00Z"}, ["10"]),
                            ({"units": "ft3 s-1"}, ["10"]), ({}, ["30"]), ({"ids": (10, 10)}, ["10"])]:
            with self.assertRaises(ValueError):
                p.frame(self.fixture(spec, **kwargs), spec, ids)

    def test_projection_is_deterministic_and_source_roles_remain_separate(self):
        models = s.model_objects("20261007", 16)
        bodies = [self.fixture(spec) for spec in models]+[json.dumps(page()).encode()]
        refs = [{"index": i, "sha256": "fixture"} for i in range(20)]
        plan = {"models": models, "object_ids": [1], "selection": "Kansas envelope"}
        outputs, summary = p.subset(plan, {"sources": refs}, lambda r: bodies[r["index"]])
        self.assertEqual(summary["rows"], 19)
        self.assertEqual(summary["geometry_version_compatibility_review"], "pending")
        self.assertIn(b"analysis_assim", gzip.decompress(outputs["kansas-envelope-streamflow.csv.gz"]))
        self.assertIn(b"NWM_MODELED_FORECAST_GUIDANCE", outputs["subset-metadata.json"])
        self.assertEqual(outputs, p.subset(plan, {"sources": refs}, lambda r: bodies[r["index"]])[0])
