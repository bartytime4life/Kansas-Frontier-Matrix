"""Historical context is replayed from original pages and never gains release authority."""
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

from connectors_core.captured_json import canonical_bytes
from connectors_core.transport import TransportResponse
from connectors.usgs.water_data.pilot_capture import capture
from pipelines.domains.hydrology.normalize import normalize_capture
from tools.local_data.file_io import write_new
from tools.local_data.historical_water import derive, FIELDS, PROFILE
from tools.local_data.manage import init_store
from tools.local_data.review_packages import ReviewPackages


class Clock:
    def now(self):
        return datetime(2026, 9, 30, 18, 1, tzinfo=timezone.utc)

    def monotonic(self):
        return 0

    def sleep(self, _seconds):
        pass


class Transport:
    def send(self, request, **_options):
        query = parse_qs(urlsplit(request.url).query)
        if "/monitoring-locations/" in request.url:
            station = "USGS-" + query["monitoring_location_number"][0]
            feature = {"type": "Feature", "id": station, "geometry": {"type": "Point", "coordinates": [-98, 38]},
                       "properties": {"agency_code": "USGS", "monitoring_location_number": station[5:],
                                      "monitoring_location_name": "Synthetic station", "state_code": "20"}}
        else:
            station = query["monitoring_location_id"][0]
            feature = {"type": "Feature", "id": "synthetic-" + station, "geometry": None,
                       "properties": {"monitoring_location_id": station, "time_series_id": "synthetic-" + station,
                                      "parameter_code": "00060", "statistic_id": "00011", "method_category": None,
                                      "time": "2026-09-30T18:00:00Z", "last_modified": "2026-09-30T18:00:01Z",
                                      "value": None if station.endswith("900") else "12.5", "unit_of_measure": "ft^3/s",
                                      "approval_status": "Provisional", "qualifier": None}}
        return TransportResponse(200, {"content-type": "application/geo+json"},
                                 (canonical_bytes({"type": "FeatureCollection", "features": [feature], "links": []}),))


class HistoricalWaterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name) / "archive"
        self.root = Path(self.temp.name) / "working"
        init_store(self.root)
        acquired = capture("2026-09-29T18:00:00Z", "2026-09-30T18:00:00Z", transport=Transport(), clock=Clock())
        self.capture = acquired.manifest["capture_id"]
        self.raw_paths = []
        for digest, raw in acquired.objects.items():
            path = self.source / "data/quarantine/usgs-nwis/objects/sha256" / digest[7:] / "payload"
            write_new(path, raw)
            self.raw_paths.append(path)
        write_new(self.source / "data/quarantine/usgs-nwis/runs" / self.capture[7:] / "manifest.json", canonical_bytes(acquired.manifest))
        candidate = normalize_capture(acquired.manifest, acquired.objects)
        table = io.StringIO(newline="")
        writer = csv.DictWriter(table, fieldnames=FIELDS)
        writer.writeheader()
        for item in candidate["observations"]:
            writer.writerow({k: json.dumps(item[k], separators=(",", ":")) if k == "qualifiers" else item[k] for k in FIELDS})
        self.package = self.source / "data/work/hydrology/example"
        for name, raw in {"README.md": b"Dated source review", "accuracy-review.json": b"{}", "rights-review.json": b"{}",
                          "discharge-stations-captured-20260929-30.geojson": b'{"type":"FeatureCollection","features":[]}',
                          "captured-discharge-observations.csv": table.getvalue().encode()}.items():
            write_new(self.package / name, raw)
        self.pin()

    def pin(self):
        outputs = [{"file": p.name, "bytes": p.stat().st_size, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
                   for p in sorted(self.package.iterdir()) if p.name != "review-manifest.json"]
        manifest = {"profile": "kfm-private-collection-readiness/v1", "review_state": "PENDING", "released": False,
                    "published": False, "source_admitted": False, "output_bytes": sum(r["bytes"] for r in outputs), "outputs": outputs}
        self.manifest = self.package / "review-manifest.json"
        self.manifest.write_bytes(canonical_bytes(manifest))
        self.pin_hash = hashlib.sha256(self.manifest.read_bytes()).hexdigest()

    def run_derivation(self):
        return derive(self.source, self.root, str(self.manifest.relative_to(self.source)), self.pin_hash, self.capture)

    def test_old_observations_remain_usable_offline_and_idempotent_with_false_authority(self):
        before = {str(p): p.read_bytes() for p in self.source.rglob("*") if p.is_file()}
        with patch("socket.socket.connect", side_effect=AssertionError("network forbidden")):
            result = self.run_derivation()
            self.assertEqual(result, self.run_derivation())
        self.assertEqual(result["observations"], 2)
        self.assertFalse(any(result["authority"].values()))
        reader = ReviewPackages(self.root, [result["binding"]])
        collection = reader.catalog()["packages"][0]
        self.assertEqual(collection["profile"], PROFILE)
        member = next(m for m in collection["members"] if m["name"] == "coverage.json")
        preview, _ = reader.preview(collection["id"], member["id"])
        coverage = json.loads(preview["text"])
        self.assertEqual(coverage["use"], "HISTORICAL_CONTEXT")
        self.assertEqual(coverage["observed_from"], "2026-09-30T18:00:00Z")
        self.assertEqual(coverage["missing_values"], 1)
        self.assertEqual(coverage["units"], ["ft^3/s"])
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.source.rglob("*") if p.is_file()})
        self.assertFalse((self.source / ".local-data.lock").exists())

    def test_rehashed_edited_table_still_must_match_original_pages(self):
        table = self.package / "captured-discharge-observations.csv"
        table.write_text(table.read_text().replace("12.5", "9999"))
        self.pin()
        with self.assertRaisesRegex(ValueError, "TABLE_REPLAY_MISMATCH"):
            self.run_derivation()
        self.assertFalse((self.root / "data/work/hydrology/historical-water").exists())

    def test_raw_and_pinned_manifest_tampering_fail_before_output(self):
        self.raw_paths[0].write_bytes(b"corrupt")
        with self.assertRaisesRegex(ValueError, "CAPTURE_LIMIT_OR_CHANGED"):
            self.run_derivation()
        self.manifest.write_text("{}")
        with self.assertRaisesRegex(ValueError, "MANIFEST_CHANGED"):
            self.run_derivation()

    def test_symlink_and_overlapping_destination_fail_closed(self):
        table = self.package / "captured-discharge-observations.csv"
        table.unlink()
        table.symlink_to(self.raw_paths[0])
        with self.assertRaisesRegex(ValueError, "SYMLINK"):
            self.run_derivation()
        with self.assertRaisesRegex(ValueError, "SEPARATE_DESTINATION"):
            derive(self.source, self.source, str(self.manifest.relative_to(self.source)), self.pin_hash, self.capture)

    def test_changed_output_is_not_overwritten_on_replay(self):
        result = self.run_derivation()
        target = self.root / result["binding"].split("@")[0]
        output = target.parent / "observations.csv"
        output.write_bytes(b"retained unrelated edit")
        with self.assertRaisesRegex(ValueError, "OUTPUT_CHANGED|BYTE_LIMIT"):
            self.run_derivation()
        self.assertEqual(output.read_bytes(), b"retained unrelated edit")
