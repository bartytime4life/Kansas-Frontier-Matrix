"""Raw-data intake: projections, profiling, routing, budget, pipeline and loopback API."""
import io
import json
import os
from email.message import Message
from pathlib import Path
import tempfile
import threading
import time
from types import SimpleNamespace
import unittest
from unittest.mock import Mock
import zipfile

from tests.local_data import intake_samples as samples
from tools.local_data import intake, intake_crs, intake_route, intake_service
from tools.local_data.intake_profile import profile_file
from tools.local_data.manage import canonical, init_store


class ProjectionTests(unittest.TestCase):
    def test_lambert_conformal_matches_epsg_guidance_note_example(self):
        # EPSG Guidance Note 7-2, method 9802: NAD27 / Texas South Central, US survey feet.
        p = intake_crs._lcc(27 + 50 / 60, -99.0, 28 + 23 / 60, 30 + 17 / 60, 2000000 * intake_crs.US_FOOT, 0.0,
                            intake_crs.US_FOOT, intake_crs.CLARKE1866)
        x, y = intake_crs.lcc_forward(p, -96.0, 28.5)
        self.assertAlmostEqual(x, 2963503.91, delta=0.05)
        self.assertAlmostEqual(y, 254759.80, delta=0.05)
        lon, lat = intake_crs._lcc_inverse(p, x, y)
        self.assertAlmostEqual(lon, -96.0, places=8)
        self.assertAlmostEqual(lat, 28.5, places=8)

    def test_albers_matches_snyder_worked_example(self):
        # Snyder (1987) p. 292: Clarke 1866, standard parallels 29.5/45.5, origin 23N 96W.
        p = {"kind": "aea", "lat0": 23.0, "lon0": -96.0, "sp1": 29.5, "sp2": 45.5, "fe": 0.0, "fn": 0.0, "ellipsoid": intake_crs.CLARKE1866}
        x, y = intake_crs.aea_forward(p, -75.0, 35.0)
        self.assertAlmostEqual(x, 1885472.7, delta=0.1)
        self.assertAlmostEqual(y, 1535925.0, delta=0.1)
        lon, lat = intake_crs._aea_inverse(p, x, y)
        self.assertAlmostEqual(lon, -75.0, places=7)
        self.assertAlmostEqual(lat, 35.0, places=7)

    def test_kansas_systems_round_trip_across_the_state(self):
        points = [(-95.689, 39.0473), (-100.0171, 37.7528), (-102.05, 40.0), (-94.6, 37.0)]
        for code, p in intake_crs.PROJECTED.items():
            forward = {"lcc": intake_crs.lcc_forward, "aea": intake_crs.aea_forward, "utm": intake_crs.utm_forward}.get(p["kind"])
            if forward is None:
                continue
            for lon, lat in points:
                if p["kind"] == "utm" and abs(lon - (-183 + 6 * p["zone"])) > 6:
                    continue  # far outside the zone; the series is only used within it
                back = intake_crs.to_wgs84(code, *forward(p, lon, lat))
                self.assertAlmostEqual(back[0], lon, delta=2e-5, msg=code)
                self.assertAlmostEqual(back[1], lat, delta=2e-5, msg=code)
        self.assertEqual(intake_crs.lcc_forward(intake_crs.PROJECTED[26977], -98.0, 38 + 1 / 3), (400000.0, 0.0))

    def test_wkt_detection_and_kansas_relation(self):
        cases = {
            'PROJCS["NAD_1983_StatePlane_Kansas_North_FIPS_1501_Feet",GEOGCS["GCS_North_American_1983"]]': 3419,
            'PROJCS["NAD_1983_StatePlane_Kansas_South_FIPS_1502"]': 26978,
            'PROJCS["NAD_1983_UTM_Zone_14N",GEOGCS["GCS_North_American_1983"]]': 26914,
            'PROJCS["NAD_1927_UTM_Zone_15N"]': 26715,
            'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984"]]': 4326,
            'GEOGCS["GCS_North_American_1927"]': 4267,
            'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version"]': 5070,
            'PROJCS["x",AUTHORITY["EPSG","32614"]]': 32614,
            'PROJCS["Some_Local_Grid"]': None,
        }
        for wkt, code in cases.items():
            self.assertEqual(intake_crs.epsg_from_wkt(wkt), code, wkt)
        self.assertEqual(intake_crs.kansas_relation([-99, 38, -98, 39]), "inside")
        self.assertEqual(intake_crs.kansas_relation([-103, 38, -98, 39]), "overlaps")
        self.assertEqual(intake_crs.kansas_relation([-105, 30, -104, 31]), "outside")
        self.assertEqual(intake_crs.kansas_relation(None), "unknown")
        self.assertIsNone(intake_crs.bbox_to_wgs84(99999, [0, 0, 1, 1]))
        self.assertIsNone(intake_crs.bbox_to_wgs84(4326, [1, 1, 0, 0]))


class ProfileTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.dir = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    def profile(self, name, content):
        path = self.dir / name
        path.write_bytes(content)
        return profile_file(path, display_path=name)

    def test_geotiff_geographic_and_projected_extents(self):
        p = self.profile("prism_ppt_2024.tif", samples.geotiff())
        self.assertEqual((p["format"]["kind"], p["spatial"]["crs"], p["spatial"]["kansas"]), ("geotiff", "EPSG:4326", "inside"))
        self.assertEqual(p["spatial"]["bbox_wgs84"], [-98.0, 38.8, -97.9, 39.0])
        self.assertEqual((p["structure"]["width"], p["structure"]["height"]), (10, 20))
        self.assertEqual(p["temporal"]["file_metadata_time"], "2024-05-01")
        self.assertIsNone(p["temporal"]["content_start"], "file metadata time is not content coverage")
        self.assertEqual(p["temporal"]["path_year_hint"], ["2024", "2024"])
        self.assertEqual(p["hints"]["domain"], "atmosphere")
        utm = self.profile("dem.tif", samples.geotiff(origin=(600000, 4300000), pixel=(30, 30), epsg=26914, geographic=False))
        self.assertEqual(utm["spatial"]["crs"], "EPSG:26914")
        self.assertEqual(utm["spatial"]["kansas"], "inside")
        unknown = self.profile("odd.tif", samples.geotiff(origin=(1, 2), pixel=(1, 1), epsg=2000, geographic=False))
        self.assertIn("crs_not_transformable_offline", unknown["issues"])
        self.assertEqual(unknown["spatial"]["kansas"], "unknown")

    def test_zipped_shapefile_reads_headers_without_extraction(self):
        p = self.profile("kgs_wells.zip", samples.shapefile_zip())
        self.assertEqual(p["format"]["kind"], "zipped-shapefile")
        self.assertEqual(p["spatial"]["crs"], "EPSG:4269")
        self.assertEqual(p["structure"]["features"], 3)
        self.assertEqual(p["structure"]["fields"], ["WELL_ID", "DEPTH_FT", "DATE_DRILL"])
        self.assertEqual(p["hints"]["domain"], "geology")
        self.assertEqual(list(self.dir.iterdir()), [self.dir / "kgs_wells.zip"])
        state_plane = self.profile("roads.zip", samples.shapefile_zip(
            bbox=(1300000, 100000, 1500000, 300000), stem="roads",
            prj='PROJCS["NAD_1983_StatePlane_Kansas_North_FIPS_1501_Feet"]'))
        self.assertEqual(state_plane["spatial"]["crs"], "EPSG:3419")
        self.assertEqual(state_plane["spatial"]["kansas"], "inside")
        no_prj = self.profile("x.zip", samples.shapefile_zip(prj=None))
        self.assertIn("shapefile_missing_prj", no_prj["issues"])
        self.assertIn("crs_assumed_geographic", no_prj["issues"])

    def test_unsafe_or_bomb_like_zip_is_flagged(self):
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("../escape.txt", b"x")
            archive.writestr("zeros.bin", bytes(5_000_000))
        p = self.profile("bundle.zip", buffer.getvalue())
        self.assertIn("zip_unsafe_member_paths", p["issues"])
        self.assertIn("zip_high_compression_ratio", p["issues"])

    def test_points_tiles_photos_tables_documents(self):
        las = self.profile("lidar.las", samples.las())
        self.assertEqual((las["format"]["kind"], las["structure"]["points"]), ("las", 1234))
        tiles = self.profile("ks.pmtiles", samples.pmtiles())
        self.assertEqual(tiles["spatial"]["bbox_wgs84"], [-102.0, 37.0, -94.6, 40.0])
        self.assertEqual(tiles["structure"]["max_zoom"], 12)
        photo = self.profile("site.jpg", samples.jpeg_with_gps())
        self.assertAlmostEqual(photo["spatial"]["bbox_wgs84"][0], -97.3375, places=3)
        self.assertEqual(photo["temporal"]["content_start"], "2019-06-02")
        self.assertIn("exact_location", photo["hints"]["review_flags"])
        geojson = self.profile("gauges.geojson", samples.GEOJSON)
        self.assertEqual((geojson["temporal"]["content_start"], geojson["temporal"]["content_end"]), ("2021-03-04", "2023-08-09"))
        self.assertEqual(geojson["spatial"]["geometry_types"], {"Point": 2})
        self.assertEqual(geojson["hints"]["domain"], "hydrology")
        table = self.profile("ghcn_precip.csv", samples.CSV)
        self.assertEqual(table["format"]["kind"], "csv-points")
        self.assertEqual(table["structure"]["rows"], 3)
        self.assertEqual(table["spatial"]["bbox_wgs84"], [-98.0, 38.5, -95.7, 39.1])
        self.assertEqual((table["temporal"]["content_start"], table["temporal"]["content_end"]), ("1951-01-01", "2020-12-31"))
        pdf = self.profile("road_map_1997-1998.pdf", samples.PDF)
        self.assertEqual((pdf["structure"]["pages"], pdf["temporal"]["file_metadata_time"]), (12, "1998-03-15"))
        self.assertEqual(pdf["temporal"]["path_year_hint"], ["1997", "1998"])
        kml = self.profile("trail.kml", samples.KML)
        self.assertEqual(kml["spatial"]["bbox_wgs84"], [-98.0, 38.0, -97.0, 39.0])
        self.assertEqual(kml["temporal"]["content_start"], "1870-05-01")
        unknown = self.profile("blob.bin", b"\x00\x01\x02" * 50)
        self.assertIn("format_unrecognized", unknown["issues"])

    def test_sensitive_names_raise_review_flags_and_outside_extent_is_noted(self):
        csv = b"burial_site,latitude,longitude,owner_name\nA,38.5,-98.0,X\n"
        p = self.profile("cemetery_survey.csv", csv)
        self.assertIn("possible_cultural_sites", p["hints"]["review_flags"])
        self.assertIn("possible_living_persons", p["hints"]["review_flags"])
        far = self.profile("far.geojson", b'{"type":"Point","coordinates":[-120.0,47.0]}')
        self.assertIn("outside_kansas", far["issues"])

    def test_symlinks_are_not_followed(self):
        target = self.dir / "real.csv"
        target.write_bytes(samples.CSV)
        (self.dir / "link.csv").symlink_to(target)
        with self.assertRaises(ValueError):
            profile_file(self.dir / "link.csv")

    def test_readers_fail_closed_into_issues(self):
        p = self.profile("broken.tif", b"II*\0" + b"\xff" * 12)
        self.assertIn("format_reader_failed", p["issues"])


def budget(**patch):
    value = {"schema": "kfm-github-storage-budget/v1", "github_limit_bytes": 100_000, "reserved_for_code_and_interface_bytes": 20_000,
             "warn_at_fraction_of_data_ceiling": 0.85, "max_release_asset_bytes": 4_000, "max_git_card_bytes": 16384,
             "max_git_cards_total_bytes": 50_000, "min_release_candidate_bytes": 100, "committed": [{"id": "repo", "bytes": 60_000}],
             "baseline_check": "not-checked"}
    value.update(patch)
    return value


def public_item(size=1000, **declared):
    base = {"source_id": "usgs", "dataset_id": "gauges", "version": "v1", "relative_path": "gauges.geojson", "domain": "hydrology",
            "rights": {"license_id": "US-PD", "redistribution": "allowed"}, "sensitivity": "public"}
    base.update(declared)
    return {"id": "a" * 32, "lane": "quarantine", "relative_path": "usgs/objects/sha256/x/payload", "store_path": "data/quarantine/usgs/x",
            "size_bytes": size, "sha256": "b" * 64, "declared": base}


def profile(**patch):
    value = {"format": {"family": "vector", "kind": "geojson"}, "spatial": {"kansas": "inside", "crs": "EPSG:4326", "bbox_wgs84": [-98, 38, -97, 39]},
             "hints": {"domain": "hydrology", "review_flags": []}, "issues": [], "structure": {}, "temporal": {}}
    value.update(patch)
    return value


def tiers(decision):
    return {p["tier"]: p for p in decision["placements"]}


class RouteTests(unittest.TestCase):
    def test_repository_budget_reserves_interface_room_and_matches_the_baseline_release(self):
        real = intake_route.load_budget()
        self.assertEqual(real["baseline_check"], "match")
        state = intake_route.budget_state(real)
        self.assertEqual(state["data_ceiling_bytes"] + state["reserved_for_code_and_interface_bytes"], 100_000_000_000)
        self.assertEqual(state["reserved_for_code_and_interface_bytes"], 20_000_000_000)
        self.assertGreater(state["available_for_new_data_bytes"], 0)

    def test_public_data_inside_budget_is_a_release_candidate_with_card_and_stage(self):
        decision = intake_route.decide(public_item(), profile(), budget())
        self.assertEqual(decision["status"], "ready")
        t = tiers(decision)
        self.assertEqual(t["local_store"]["action"], "keep")
        self.assertEqual(t["work_lane"]["action"], "stage")
        self.assertTrue(t["work_lane"]["target"].startswith("data/work/intake/hydrology/usgs/gauges/"))
        self.assertEqual(t["git_repo"]["action"], "metadata_card")
        self.assertEqual((t["github_release"]["action"], t["github_release"]["budget_after_bytes"]), ("candidate", 19_000))
        self.assertEqual(decision["authority"], {"network": False, "source_admission": False, "promotion": False, "release": False, "publication": False})

    def test_budget_ceiling_splitting_and_small_file_bundling(self):
        self.assertEqual(tiers(intake_route.decide(public_item(size=25_000), profile(), budget()))["github_release"]["reason"], "GITHUB_BUDGET_EXCEEDED")
        self.assertEqual(tiers(intake_route.decide(public_item(size=9_000), profile(), budget()))["github_release"]["asset_parts"], 3)
        self.assertEqual(tiers(intake_route.decide(public_item(size=50), profile(), budget()))["github_release"]["action"], "bundle")
        over = intake_route.budget_state(budget(committed=[{"id": "repo", "bytes": 90_000}]))
        self.assertEqual((over["level"], over["available_for_new_data_bytes"]), ("over", 0))

    def test_unknown_rights_sensitivity_and_flags_hold_everything_but_local_and_index(self):
        for item, prof in [(public_item(rights={"license_id": None, "redistribution": "unknown"}), profile()),
                           (public_item(sensitivity="restricted"), profile()),
                           (public_item(), profile(hints={"domain": "hydrology", "review_flags": ["possible_rare_species"]})),
                           (public_item(domain="archaeology"), profile(hints={"domain": "archaeology", "review_flags": []}))]:
            decision = intake_route.decide(item, prof, budget())
            t = tiers(decision)
            self.assertEqual(decision["status"], "review")
            self.assertEqual(t["git_repo"]["action"], "hold")
            self.assertEqual(t["github_release"]["action"], "hold")
            self.assertEqual(t["local_store"]["action"], "keep")

    def test_blocking_issues_outside_kansas_and_inbox(self):
        blocked = intake_route.decide(public_item(), profile(issues=["zip_unsafe_member_paths"]), budget())
        self.assertEqual((blocked["status"], tiers(blocked)["work_lane"]["action"]), ("blocked", "hold"))
        outside = intake_route.decide(public_item(), profile(spatial={"kansas": "outside", "bbox_wgs84": [-120, 40, -119, 41]}), budget())
        self.assertEqual(tiers(outside)["github_release"]["reason"], "OUTSIDE_KANSAS")
        inbox = dict(public_item(), lane="inbox", store_path=None, declared=None)
        decision = intake_route.decide(inbox, profile(), budget())
        self.assertEqual(tiers(decision)["work_lane"]["action"], "capture_first")
        self.assertIn("CAPTURE_REQUIRED", decision["holds"])

    def test_budget_policy_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "b.json"
            path.write_text(json.dumps(budget(reserved_for_code_and_interface_bytes=100_000)))
            with self.assertRaises(intake_route.BudgetError):
                intake_route.load_budget(path, None)
            path.write_text(json.dumps(budget(committed=[{"id": "a", "bytes": 1}, {"id": "a", "bytes": 2}])))
            with self.assertRaises(intake_route.BudgetError):
                intake_route.load_budget(path, None)


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "store"
        init_store(self.root)
        self.budget = budget(github_limit_bytes=10**12, reserved_for_code_and_interface_bytes=10**11, committed=[])
        raw = self.root / "data/raw/kgs"
        raw.mkdir(parents=True)
        (raw / "kgs_wells.zip").write_bytes(samples.shapefile_zip())
        (raw / "unknown.bin").write_bytes(b"\x00\x01" * 40)
        (raw / ".hidden").write_bytes(b"secret")
        (raw / "credentials.json").write_bytes(b"{}")
        # A quarantine capture laid out exactly as manage.py sync writes it.
        content = samples.GEOJSON
        digest = __import__("hashlib").sha256(content).hexdigest()
        payload = self.root / f"data/quarantine/usgs/objects/sha256/{digest}/payload"
        payload.parent.mkdir(parents=True)
        payload.write_bytes(content)
        binding = {"source_id": "usgs", "dataset_id": "ks-gauges", "domain": "hydrology", "version": "v1", "relative_path": "gauges.geojson",
                   "source_uri": "https://waterdata.usgs.gov/ks", "media_type": "application/geo+json",
                   "rights": {"license_id": "US-PD", "redistribution": "allowed"}, "sensitivity": "public",
                   "sha256": digest, "size_bytes": len(content), "captured_at": "2026-10-01T00:00:00Z"}
        version = self.root / "data/quarantine/usgs/versions/ks-gauges/v1/x.json"
        version.parent.mkdir(parents=True)
        version.write_bytes(canonical(binding))
        self.inbox = Path(self.temporary.name) / "downloads"
        self.inbox.mkdir()
        (self.inbox / "trail.kml").write_bytes(samples.KML)

    def tearDown(self):
        self.temporary.cleanup()

    def items(self, **query):
        return {i["name"]: i for i in intake.list_items(self.root, **query)["items"]}

    def test_analyze_indexes_routes_and_reuses_unchanged_profiles(self):
        first = intake.analyze(self.root, inbox=self.inbox, budget=self.budget)
        self.assertEqual((first["discovered"], first["analyzed"], first["failed"], first["state"]), (4, 4, 0, "complete"))
        found = self.items()
        self.assertEqual(set(found), {"kgs_wells.zip", "unknown.bin", "gauges.geojson", "trail.kml"})
        self.assertEqual(found["gauges.geojson"]["status"], "ready")
        self.assertEqual(found["gauges.geojson"]["declared_label"], "usgs/ks-gauges/v1")
        self.assertEqual(found["kgs_wells.zip"]["status"], "review")
        self.assertIn("RIGHTS_UNKNOWN", found["kgs_wells.zip"]["holds"])
        self.assertEqual(len(found["kgs_wells.zip"]["sha256"]), 64)
        self.assertEqual(found["trail.kml"]["lane"], "inbox")
        second = intake.analyze(self.root, budget=self.budget)
        self.assertEqual((second["discovered"], second["analyzed"], second["reused"]), (3, 0, 3))
        self.assertIn("trail.kml", self.items(), "an unscanned inbox is not marked missing")
        (self.root / "data/raw/kgs/unknown.bin").unlink()
        intake.analyze(self.root, budget=self.budget)
        self.assertNotIn("unknown.bin", self.items())
        self.assertIn("unknown.bin", self.items(include_missing=True), "history is retained")

    def test_spatial_and_attribute_queries(self):
        intake.analyze(self.root, inbox=self.inbox, budget=self.budget)
        self.assertEqual(set(self.items(bbox=[-96.5, 39.0, -96.0, 39.5])), {"gauges.geojson"})
        self.assertEqual(set(self.items(bbox=[-99.4, 37.6, -99.3, 37.7])), {"kgs_wells.zip"})
        self.assertEqual(set(self.items(status="ready")), {"gauges.geojson"})
        self.assertEqual(set(self.items(text="wells")), {"kgs_wells.zip"})
        self.assertEqual(set(self.items(text="%")), set(), "LIKE wildcards are escaped")
        overview = intake.overview(self.root, self.budget)
        self.assertEqual(overview["files"], 4)
        self.assertEqual(overview["by_status"]["ready"]["files"], 1)

    def test_apply_stages_a_verified_copy_and_writes_receipts_without_touching_sources(self):
        intake.analyze(self.root, budget=self.budget)
        ready = self.items()["gauges.geojson"]
        source = next((self.root / "data/quarantine/usgs/objects").rglob("payload"))
        before = source.stat()
        result = intake.apply(self.root, ready["id"], "stage")
        self.assertEqual(result["outcome"], "APPLIED")
        staged = self.root / result["target"]
        self.assertEqual(staged.read_bytes(), samples.GEOJSON)
        self.assertNotEqual(staged.stat().st_ino, before.st_ino, "a copy, never a hard link")
        self.assertEqual(source.stat().st_mtime_ns, before.st_mtime_ns)
        receipt = json.loads((self.root / result["receipt"]).read_text())
        self.assertEqual((receipt["action"], receipt["sha256"]), ("stage", ready["sha256"]))
        self.assertEqual(intake.apply(self.root, ready["id"], "stage")["outcome"], "ALREADY_STAGED")
        card = intake.apply(self.root, ready["id"], "card")
        written = json.loads((self.root / card["target"]).read_text())
        self.assertEqual((written["schema"], written["dataset_id"]), ("kfm-intake-card/v1", "ks-gauges"))
        self.assertEqual(intake.apply(self.root, ready["id"], "card")["outcome"], "ALREADY_WRITTEN")
        self.assertEqual([a["action"] for a in intake.get_item(self.root, ready["id"])["applications"]], ["stage", "card"])
        held = self.items()["kgs_wells.zip"]
        with self.assertRaisesRegex(ValueError, "CARD_NOT_RECOMMENDED"):
            intake.apply(self.root, held["id"], "card")
        unknown = self.items()["unknown.bin"]
        with self.assertRaisesRegex(ValueError, "STAGE_NOT_RECOMMENDED"):
            intake.apply(self.root, unknown["id"], "stage")
        with self.assertRaisesRegex(ValueError, "ACTION_UNSUPPORTED"):
            intake.apply(self.root, ready["id"], "publish")
        self.assertEqual(len(intake.cards(self.root)), 1)

    def test_release_plan_defers_what_does_not_fit(self):
        intake.analyze(self.root, budget=self.budget)
        roomy = budget(github_limit_bytes=10**9, reserved_for_code_and_interface_bytes=10**8, committed=[], min_release_candidate_bytes=1)
        intake.analyze(self.root, budget=roomy)
        plan = intake.release_plan(self.root, roomy)
        self.assertEqual([r["relative_path"].split("/")[0] for r in plan["selected"]], ["usgs"])
        self.assertEqual(plan["budget_after_plan"]["planned_bytes"], len(samples.GEOJSON))
        tight = dict(roomy, committed=[{"id": "x", "bytes": 9 * 10**8 - 10}])
        self.assertEqual(intake.release_plan(self.root, tight)["selected"], [])

    def test_single_writer_and_cancellation(self):
        with intake.writer_lock(self.root):
            with self.assertRaisesRegex(ValueError, "INTAKE_BUSY"):
                intake.analyze(self.root, budget=self.budget)
        cancel = threading.Event()
        cancel.set()
        self.assertEqual(intake.analyze(self.root, budget=self.budget, cancel=cancel)["state"], "cancelled")


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "store"
        init_store(self.root)
        (self.root / "data/raw/misc").mkdir(parents=True)
        (self.root / "data/raw/misc/gauges.geojson").write_bytes(samples.GEOJSON)
        self.desk = intake_service.Desk(self.root, budget=budget(github_limit_bytes=10**12, reserved_for_code_and_interface_bytes=10**11, committed=[]))
        self.desk.token = "t" * 43

    def tearDown(self):
        if self.desk.thread:
            self.desk.thread.join(5)
        self.temporary.cleanup()

    def request(self, method, path, body=None, headers=None, raw=False):
        Handler = intake_service.handler(self.desk)
        h = Handler.__new__(Handler)
        encoded = json.dumps({} if body is None else body).encode()
        h.headers = Message()
        values = {"Host": "127.0.0.1:8771", "Origin": "http://127.0.0.1:8771", "X-KFM-Session": self.desk.token,
                  "Content-Type": "application/json", "Content-Length": str(len(encoded))}
        values.update(headers or {})
        for key, value in values.items():
            if value is not None:
                h.headers[key] = value
        h.path = path
        h.rfile = io.BytesIO(encoded)
        h.wfile = io.BytesIO()
        h.connection = SimpleNamespace(settimeout=Mock())
        h.send_response = Mock()
        h.send_header = Mock()
        h.end_headers = Mock()
        getattr(h, "do_" + method)()
        sent = dict(c.args for c in h.send_header.call_args_list)
        status = h.send_response.call_args.args[0]
        return (status, h.wfile.getvalue(), sent) if raw else (status, json.loads(h.wfile.getvalue() or b"null"), sent)

    def wait(self):
        for _ in range(200):
            if self.desk.job["state"] != "running":
                return
            time.sleep(0.02)
        self.fail("analysis did not finish")

    def test_desk_page_embeds_session_and_strict_headers(self):
        status, body, headers = self.request("GET", "/", headers={"Origin": None}, raw=True)
        self.assertEqual(status, 200)
        self.assertIn(self.desk.token.encode(), body)
        self.assertNotIn(b"__KFM_SESSION__", body)
        self.assertIn("default-src 'none'", headers["Content-Security-Policy"])
        self.assertEqual(headers["X-Frame-Options"], "DENY")
        self.assertNotIn("Access-Control-Allow-Origin", headers)
        for asset in ("/desk.js", "/desk.css"):
            self.assertEqual(self.request("GET", asset, headers={"Origin": None}, raw=True)[0], 200)

    def test_host_origin_and_session_are_checked_before_any_effect(self):
        self.assertEqual(self.request("GET", "/api/overview", headers={"Host": "attacker.example:8771"})[0], 403)
        self.assertEqual(self.request("GET", "/", headers={"Host": "localhost:8771", "Origin": None}, raw=True)[0], 403)
        self.assertEqual(self.request("GET", "/api/overview", headers={"Origin": "https://attacker.example"})[0], 403)
        for headers in ({"X-KFM-Session": "wrong"}, {"Origin": None}, {"Origin": "https://attacker.example"}, {"Host": "127.0.0.1:9999"}):
            self.assertEqual(self.request("POST", "/api/analyze", headers=headers)[0], 403)
        self.assertEqual(self.request("POST", "/api/analyze", headers={"Content-Type": "text/plain"})[0], 415)
        self.assertEqual(self.request("POST", "/api/analyze", headers={"Content-Length": "5000"})[0], 400)
        self.assertEqual(self.desk.job["state"], "idle")
        status, body, headers = self.request("GET", "/api/status", headers={"Origin": "http://127.0.0.1:4173"})
        self.assertEqual((status, body["sessionToken"], headers["Access-Control-Allow-Origin"]), (200, self.desk.token, "http://127.0.0.1:4173"))
        self.assertNotIn("sessionToken", self.request("GET", "/api/status", headers={"Origin": None})[1])
        self.assertEqual(self.request("OPTIONS", "/api/analyze", headers={"Origin": "https://attacker.example"})[0], 403)

    def test_analyze_list_detail_extents_and_apply_over_http(self):
        status, body, _ = self.request("POST", "/api/analyze", {"includeInbox": False})
        self.assertEqual((status, body["state"]), (200, "running"))
        self.wait()
        self.assertEqual(self.desk.job["state"], "complete")
        self.assertEqual(self.request("POST", "/api/analyze", {"includeInbox": True})[1]["error"], "INBOX_NOT_CONFIGURED")
        listing = self.request("GET", "/api/items?lane=raw&bbox=-98,38,-96,40")[1]
        self.assertEqual(listing["total"], 1)
        identity = listing["items"][0]["id"]
        detail = self.request("GET", f"/api/items/{identity}")[1]
        self.assertEqual(detail["profile"]["format"]["kind"], "geojson")
        extents = self.request("GET", "/api/extents")[1]
        self.assertEqual(extents["features"][0]["properties"]["id"], identity)
        self.assertEqual(self.request("GET", "/api/items/" + "f" * 32)[0], 404)
        for bad in ("/api/items?bbox=1,2,3", "/api/items?limit=-1", "/api/items?unknown=1", "/api/items/../../etc"):
            self.assertEqual(self.request("GET", bad)[0], 400, bad)
        self.assertEqual(self.request("POST", "/api/apply", {"id": identity, "action": "stage", "extra": 1})[1]["error"], "APPLY_REQUEST_INVALID")
        held = self.request("POST", "/api/apply", {"id": identity, "action": "card"})
        self.assertEqual((held[0], held[1]["error"]), (400, "CARD_NOT_RECOMMENDED:CARD_REQUIRES_PUBLIC_RIGHTS_AND_REVIEW"))
        staged = self.request("POST", "/api/apply", {"id": identity, "action": "stage"})
        self.assertEqual((staged[0], staged[1]["outcome"]), (200, "APPLIED"))
        self.assertTrue(staged[1]["target"].startswith("data/work/intake/hydrology/unregistered/"))
        self.assertEqual(self.request("GET", "/api/budget")[1]["schema"], "kfm-github-storage-state/v1")
        self.assertEqual(self.request("GET", "/api/release-plan")[1]["selected"], [])
        self.assertEqual(self.request("POST", "/api/cancel", {})[1]["error"], "NO_ACTIVE_ANALYSIS")

    def test_unexpected_failures_are_reported_without_internals(self):
        original = intake_service.intake.overview
        intake_service.intake.overview = Mock(side_effect=RuntimeError("/private/path leaked"))
        try:
            status, body, _ = self.request("GET", "/api/overview")
        finally:
            intake_service.intake.overview = original
        self.assertEqual((status, body), (500, {"error": "INTERNAL_ERROR"}))


if __name__ == "__main__":
    unittest.main()
