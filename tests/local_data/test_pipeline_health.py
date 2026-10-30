"""Private pipeline health: bounds, stale reports, redaction and session boundaries."""
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest
from tests.local_data import test_intake as service_tests
from tools.local_data.pipeline_health import read_health


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / "data/work/pipeline-health.json"
        self.path.parent.mkdir(parents=True)
        self.now = datetime.now(timezone.utc)

    def write(self, **changes):
        value = {"format": "kfm-pipeline-operator-health-v1", "checkedAt": self.now.isoformat().replace("+00:00", "Z"),
                 "state": "checked", "publication": "disabled", "jobs": [{"sourceId": "nws-alerts", "state": "held", "attempts": 3,
                 "reason": "UPSTREAM_TIMEOUT", "exhausted": True, "workerSecret": "SECRET", "path": "/private/SECRET"}],
                 "backup": {"state": "verified-copy", "files": 10}, "restore": {"state": "verified", "matchesLatestBackup": False}}
        value.update(changes)
        self.path.write_text(json.dumps(value))

    def test_missing_and_oversized_reports_fail_without_initializing(self):
        self.assertEqual(read_health(self.root)["state"], "unavailable")
        self.assertFalse(self.path.exists())
        self.path.write_text(" " * 65537)
        self.assertEqual(read_health(self.root)["state"], "unavailable")

    def test_redaction_and_clock_freshness(self):
        self.write()
        value = read_health(self.root, now=self.now)
        self.assertFalse(value["stale"])
        self.assertTrue(value["jobs"][0]["exhausted"])
        self.assertFalse(value["restore"]["matchesLatestBackup"])
        self.assertNotIn("SECRET", json.dumps(value))
        self.assertTrue(read_health(self.root, now=self.now + timedelta(minutes=16))["stale"])
        self.assertTrue(read_health(self.root, now=self.now - timedelta(minutes=2))["stale"])

    def test_symlinks_and_invalid_clocks_fail_closed(self):
        self.write(checkedAt="bad")
        self.assertEqual(read_health(self.root)["state"], "unavailable")
        self.path.unlink()
        target = self.root / "outside.json"
        target.write_text('{"secret":"SECRET"}')
        self.path.symlink_to(target)
        self.assertEqual(read_health(self.root)["state"], "unavailable")


class HealthServiceTests(unittest.TestCase):
    setUp = service_tests.ServiceTests.setUp
    tearDown = service_tests.ServiceTests.tearDown
    request = service_tests.ServiceTests.request

    def test_private_route_needs_session_and_local_origin(self):
        status, value, _ = self.request("GET", "/api/pipeline-health")
        self.assertEqual(status, 200)
        self.assertEqual(value["state"], "unavailable")
        self.assertEqual(self.request("GET", "/api/pipeline-health", headers={"X-KFM-Session": None})[0], 403)
        self.assertEqual(self.request("GET", "/api/pipeline-health", headers={"Origin": "https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site"})[0], 403)
        self.assertEqual(self.request("GET", "/api/pipeline-health?path=elsewhere")[0], 400)
        self.desk.catalog_only = True
        self.assertEqual(self.request("GET", "/api/pipeline-health")[0], 400)
