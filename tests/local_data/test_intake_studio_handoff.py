"""Exercise reviewed Studio originals through real capture and Working Data indexing."""
import base64
import fcntl
import json
import io
from email.message import Message
from types import SimpleNamespace
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch, Mock

from tools.local_data import intake, manage
from tools.local_data.intake_studio.intake_server import Store, Handler

PNG = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aGZkAAAAASUVORK5CYII=")


def fake_extract(command, **kwargs):
    work = Path(command[command.index("--bind") + 1])
    (work / "analysis.json").write_text(json.dumps({
        "status": "Partial", "method": "Synthetic OCR for capture tests", "pages": 1,
        "text": "Kansas water notes", "metadata": {}, "warnings": [], "suggestions": [], "flags": []}))
    return type("Result", (), {"returncode": 0})()


class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.kfm = self.base / "working"
        manage.init_store(self.kfm)
        self.lock = self.base / "pipeline.lock"
        self.store = Store(self.base / "studio", self.base / "runtime", kfm_root=self.kfm, pipeline_lock=self.lock)
        self.record = self.upload()

    def upload(self, name="water-photo.png"):
        with patch("tools.local_data.intake_studio.intake_server.subprocess.run", side_effect=fake_extract):
            return self.store.ingest(name, PNG)[0]

    def ready(self, record=None):
        r = record or self.record
        return self.store.review(r["id"], {"version": r["version"], **r["review"],
            "source": "Synthetic owner field photograph", "reviewer": "QA", "rights": "Owned by me",
            "sensitivity": "Public", "domain": "hydrology", "surface": "Reference library",
            "decision": "Ready for integration review"})

    def send(self, record=None):
        r = record or self.ready()
        return self.store.send(r["id"], {"version": r["version"]})

    def test_capture_original_review_and_working_index_preserve_holds(self):
        r = self.ready()
        sent, duplicate = self.send(r)
        self.assertFalse(duplicate)
        transfer = sent["transfer"]
        self.assertEqual(transfer["state"], "CAPTURED_IN_WORKING_DATA")
        self.assertFalse(any(transfer["authority"].values()))
        item = intake.get_item(self.kfm, transfer["itemId"])
        self.assertEqual((self.kfm / item["store_path"]).read_bytes(), PNG)
        self.assertEqual(item["declared"]["rights"]["redistribution"], "unknown")
        self.assertEqual(item["decision"]["domain"], "hydrology")
        self.assertNotEqual(item["status"], "ready")
        review = json.loads((self.kfm / transfer["reviewPath"]).read_text())
        self.assertEqual(review["review"], r["review"])
        self.assertEqual(review["history"], r["history"])
        self.assertEqual((self.kfm / transfer["reviewPath"]).with_name("extracted-text.txt").read_text(), "Kansas water notes")
        self.assertEqual(intake.list_items(self.kfm)["items"][0]["name"], "source-water-photo.png")

    def test_retry_and_restart_do_not_duplicate_capture(self):
        r = self.ready()
        first, _ = self.send(r)
        again, duplicate = self.send(r)
        self.assertTrue(duplicate)
        self.assertEqual(first, again)
        restarted = Store(self.store.root, self.store.runtime, kfm_root=self.kfm, pipeline_lock=self.lock)
        self.assertTrue(restarted.send(r["id"], {"version": again["version"]})[1])
        self.assertEqual(len(list((self.kfm / "data/quarantine").rglob("payload"))), 1)
        self.assertEqual(len(intake.list_items(self.kfm)["items"]), 1)

    def test_duplicate_bytes_keep_separate_provenance(self):
        one, _ = self.send()
        two, _ = self.send(self.ready(self.upload("other-source.png")))
        self.assertNotEqual(one["transfer"]["sourceId"], two["transfer"]["sourceId"])
        self.assertEqual(len(intake.list_items(self.kfm)["items"]), 2)

    def test_send_refuses_unreviewed_and_unconfigured_files(self):
        with self.assertRaisesRegex(ValueError, "ready review"):
            self.store.send(self.record["id"], {"version": self.record["version"]})
        r = self.ready()
        self.store.kfm_root = None
        with self.assertRaisesRegex(ValueError, "not configured"):
            self.send(r)
        self.assertFalse(list((self.kfm / "data/quarantine").rglob("payload")))

    def test_stale_review_and_extra_fields_refused_before_capture(self):
        r = self.ready()
        self.store.review(r["id"], {"version": r["version"], **r["review"], "description": "updated context"})
        with self.assertRaisesRegex(RuntimeError, "changed"):
            self.send(r)
        for value in ({"version": True}, {"version": r["version"], "root": "/tmp"}, []):
            with self.assertRaises(ValueError):
                self.store.send(r["id"], value)
        self.assertFalse(list((self.kfm / "data/quarantine").rglob("payload")))

    def test_server_rechecks_review_holds(self):
        r = self.ready()
        for field, value in (("rights", "Unknown"), ("rights", "Restricted"), ("sensitivity", "Private / personal"),
                             ("source", ""), ("domain", "Unassigned"), ("surface", "Unassigned")):
            current = self.store.get(r["id"])
            current["review"][field] = value
            self.store.save(current)
            with self.assertRaises(ValueError):
                self.send(r)
            self.store.save(r)
        for field, value in (("status", "Failed"), ("flags", ["sensitive location"])):
            current = self.store.get(r["id"])
            current["analysis"][field] = value
            self.store.save(current)
            with self.assertRaises(ValueError):
                self.send(r)
            self.store.save(r)

    def test_corrupt_or_symlink_original_refused(self):
        r = self.ready()
        original = self.store.objects / r["sha256"] / "original"
        original.write_bytes(b"corrupted")
        with self.assertRaises(ValueError):
            self.send(r)
        original.unlink()
        other = self.base / "other.png"
        other.write_bytes(PNG)
        original.symlink_to(other)
        with self.assertRaises(ValueError):
            self.send(r)

    def test_busy_pipeline_does_not_capture(self):
        r = self.ready()
        with self.lock.open("w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with self.assertRaisesRegex(RuntimeError, "another job"):
                self.send(r)
        self.assertFalse(list((self.kfm / "data/quarantine").rglob("payload")))

    def test_busy_working_writer_does_not_capture(self):
        r = self.ready()
        with intake.writer_lock(self.kfm):
            with self.assertRaisesRegex(RuntimeError, "Working Data is busy"):
                self.send(r)
        self.assertFalse(list((self.kfm / "data/quarantine").rglob("payload")))

    def test_two_simultaneous_clicks_capture_once(self):
        r = self.ready()
        results = []
        threads = [threading.Thread(target=lambda: results.append(self.send(r))) for _ in range(2)]
        for t in threads:
            t.start()
        for t in threads:
            t.join(10)
        self.assertEqual(len(results), 2)
        self.assertEqual(sorted(duplicate for _, duplicate in results), [False, True])
        self.assertEqual(len(list((self.kfm / "data/quarantine").rglob("payload"))), 1)

    def test_missing_volume_check_and_nested_store_refuse_capture(self):
        r = self.ready()
        self.store.store_check = self.base / "missing-volume-check.py"
        with self.assertRaisesRegex(RuntimeError, "data volume"):
            self.send(r)
        self.store = Store(self.kfm / "data/work/studio", self.base / "runtime", kfm_root=self.kfm)
        r = self.ready(self.upload())
        with self.assertRaisesRegex(ValueError, "separate"):
            self.send(r)
        self.assertFalse(list((self.kfm / "data/quarantine").rglob("payload")))

    def test_interrupted_index_can_retry_same_capture(self):
        r = self.ready()
        with patch.object(intake, "_upsert", side_effect=RuntimeError("Synthetic interrupted index")):
            with self.assertRaises(RuntimeError):
                self.send(r)
        sent, _ = self.send(r)
        self.assertTrue(sent["transfer"]["indexed"])
        self.assertEqual(len(list((self.kfm / "data/quarantine").rglob("payload"))), 1)

    def test_interrupted_studio_save_can_retry_same_capture(self):
        r = self.ready()
        with patch.object(self.store, "save", side_effect=RuntimeError("Synthetic interrupted save")):
            with self.assertRaises(RuntimeError):
                self.send(r)
        self.send(r)
        self.assertEqual(len(list((self.kfm / "data/quarantine").rglob("payload"))), 1)

    def test_targeted_index_does_not_hide_existing_files(self):
        (self.kfm / "data/raw/old.csv").write_text("a,b\n1,2\n")
        intake.analyze(self.kfm)
        self.send()
        self.assertEqual(len(intake.list_items(self.kfm)["items"]), 2)

    def test_changed_sent_review_needs_review_then_gets_separate_snapshot(self):
        first, _ = self.send()
        changed = self.store.review(first["id"], {"version": first["version"], **first["review"], "source": "Corrected source context"})
        self.assertEqual(changed["review"]["decision"], "Needs review")
        with self.assertRaises(ValueError):
            self.send(changed)
        second, _ = self.send(self.ready(changed))
        self.assertNotEqual(first["transfer"]["sourceId"], second["transfer"]["sourceId"])

    def test_http_send_requires_session_origin_and_saved_revision(self):
        r = self.ready()
        server = SimpleNamespace(origin="http://127.0.0.1:18776", token="synthetic-session", store=self.store)
        body = json.dumps({"version": r["version"]}).encode()

        def request(headers):
            h = Handler.__new__(Handler)
            h.path = "/api/files/" + r["id"] + "/send"
            h.headers = Message()
            for key, value in {"Host": "127.0.0.1:18776", "Content-Length": str(len(body)), **headers}.items():
                h.headers[key] = value
            h.rfile, h.wfile = io.BytesIO(body), io.BytesIO()
            h.connection = SimpleNamespace(settimeout=Mock())
            h.server = server
            result = {}
            h.send_response = lambda code: result.update(code=code)
            h.send_header = lambda *_: None
            h.end_headers = lambda: None
            h.do_POST()
            return result["code"], json.loads(h.wfile.getvalue())

        for headers in ({}, {"X-KFM-Token": server.token, "Origin": "https://example.org"},
                        {"X-KFM-Token": server.token, "Host": "example.org"}):
            self.assertEqual(request(headers)[0], 403)
        code, result = request({"X-KFM-Token": server.token})
        self.assertEqual(code, 200)
        self.assertTrue(result["file"]["transfer"]["indexed"])


if __name__ == "__main__":
    unittest.main()
