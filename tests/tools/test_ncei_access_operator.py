"""Offline private-store integrity, replay, and capture-failure checks."""
import contextlib
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.local_data import noaa_ncei_access as operator
from connectors.noaa.src.noaa import ncei_access as api
from tools.local_data.manage import init_store


class OperatorTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "store"
        init_store(self.root)
        self.query = api.Query("daily-summaries", ("USW00003928",), "2024-01-01", "2024-01-02", ("PRCP",))
        self.raw = json.dumps([{"STATION": "USW00003928", "NAME": "SYNTHETIC, KS US", "DATE": "2024-01-01",
                    "LATITUDE": "37.6", "LONGITUDE": "-97.4", "ELEVATION": "401.7",
                    "PRCP": "", "PRCP_ATTRIBUTES": ",Q,W"}]).encode()
        self.fetcher = lambda query: (self.raw, {"url": query.url(), "retrieved_at": "2026-10-14T00:00:00Z",
                                                "status": 200, "content_type": "application/json"})
        self.capture = api.capture(self.query, fetcher=self.fetcher)

    def test_capture_exact_readback_replay_and_pending_receipt_are_idempotent(self):
        receipt = operator.acquire(self.root, self.query, fetcher=self.fetcher)
        self.assertEqual(receipt["outcome"], "QUARANTINED")
        self.assertEqual(receipt["review_state"], "pending")
        for field in ("source_admitted", "promoted", "released", "published"):
            self.assertFalse(receipt[field])
        loaded = operator.load_capture(self.root, receipt["capture_id"])
        self.assertEqual(loaded.raw, self.raw)
        self.assertEqual(loaded.manifest, self.capture.manifest)
        self.assertEqual(operator.stage(self.root, loaded), receipt)
        for lane in ("raw", "work", "processed", "catalog", "triplets", "published", "registry", "proofs"):
            self.assertEqual(list((self.root / "data" / lane).iterdir()), [])

    def test_every_product_can_use_the_same_quarantine_and_replay_operator(self):
        for dataset, product in api.PRODUCTS.items():
            window = (None, None) if product.period in ("normal-month", "normal-year") else ("2024-01-01", "2024-01-02")
            query = api.Query(dataset, ("USW00003928",), *window)
            receipt = operator.acquire(self.root, query, fetcher=lambda q: (
                b"[]", {"url": q.url(), "retrieved_at": "2026-10-14T00:00:00Z", "status": 200, "content_type": "application/json"}))
            with self.subTest(dataset=dataset):
                self.assertEqual(receipt["row_count"], 0)
                self.assertEqual(operator.load_capture(self.root, receipt["capture_id"]).raw, b"[]")
                self.assertEqual(receipt["source_role"], product.role)

    def test_tampered_capture_cannot_write(self):
        manifest = copy.deepcopy(self.capture.manifest)
        manifest["published"] = True
        with self.assertRaises(ValueError):
            operator.stage(self.root, api.Capture(manifest, self.raw))
        self.assertFalse((self.root / "data/quarantine" / operator.LANE).exists())

    def test_corrupt_stored_bytes_and_path_ids_are_refused(self):
        receipt = operator.stage(self.root, self.capture)
        payload = operator.object_path(self.root, self.capture.manifest["response"]["sha256"])
        payload.write_bytes(self.raw + b" ")
        with self.assertRaises(ValueError):
            operator.load_capture(self.root, receipt["capture_id"])
        for value in ("../x", "sha256:../x", "0" * 64):
            with self.assertRaises(ValueError):
                operator.load_capture(self.root, value)

    def test_symlink_input_and_immutable_conflict_are_refused(self):
        receipt = operator.stage(self.root, self.capture)
        payload = operator.object_path(self.root, self.capture.manifest["response"]["sha256"])
        payload.unlink()
        external = Path(self.temporary.name) / "external.json"
        external.write_bytes(self.raw)
        payload.symlink_to(external)
        with self.assertRaises(ValueError):
            operator.load_capture(self.root, receipt["capture_id"])
        conflict = self.root / "conflict"
        operator.immutable(conflict, b"one")
        with self.assertRaises(ValueError):
            operator.immutable(conflict, b"two")

    def test_failed_source_and_schema_drift_keep_failure_receipts(self):
        def failure(_query):
            raise ValueError("PROVIDER_UNAVAILABLE")
        receipt = operator.acquire(self.root, self.query, fetcher=failure)
        self.assertEqual(receipt["outcome"], "ERROR")
        self.assertIsNone(receipt["response_sha256"])
        receipt = operator.acquire(self.root, self.query, fetcher=lambda q: (
            b'{"errorCode":400}', {"url": q.url(), "retrieved_at": "2026-10-14T00:00:00Z", "status": 200, "content_type": "application/json"}))
        self.assertEqual(receipt["outcome"], "ERROR")
        self.assertIsNotNone(receipt["response_sha256"])
        self.assertEqual(operator.object_path(self.root, receipt["response_sha256"]).read_bytes(), b'{"errorCode":400}')
        self.assertEqual(len(list((self.root / "data/receipts/ingest" / operator.LANE / "failed").glob("*/receipt.json"))), 2)
        self.assertFalse((self.root / "data/quarantine" / operator.LANE / "runs").exists())

    def test_cli_products_plan_replay_are_offline_and_reject_repository_store(self):
        with patch.object(operator, "acquire", side_effect=AssertionError("network")), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(operator.main(["products"]), 0)
            self.assertEqual(operator.main(["plan", "--dataset", "daily-summaries", "--start", "2024-01-01",
                            "--end", "2024-01-02", "--max-bytes", "10000"]), 0)
            self.assertEqual(operator.main(["capture", "--dataset", "daily-summaries", "--start", "2024-01-01",
                            "--end", "2024-01-02", "--max-bytes", "10000", "--root", str(operator.REPO_ROOT)]), 1)
        receipt = operator.stage(self.root, self.capture)
        with patch.object(api, "fetch", side_effect=AssertionError("network")), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(operator.main(["replay", "--root", str(self.root), "--capture-id", receipt["capture_id"]]), 0)


if __name__ == "__main__":
    unittest.main()
