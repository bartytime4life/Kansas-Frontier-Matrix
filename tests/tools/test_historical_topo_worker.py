"""RAW capture stays incomplete on a failed provider stream."""
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

SOURCE = Path(__file__).resolve().parents[2] / "tools/historical_topo_worker.py"
spec = importlib.util.spec_from_file_location("kfm_historical_topo_worker", SOURCE)
worker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(worker)


class WorkerCaptureTests(unittest.TestCase):
    def test_capture_receipt_and_deduplicated_rerun(self):
        original = worker.stream_geotiff
        calls = []
        try:
            def stream(_item, emit):
                calls.append(1)
                emit(b"original GeoTIFF")
                return {"geotiff": {"bytes": 16, "sha256": "example"}}
            worker.stream_geotiff = stream
            with TemporaryDirectory() as directory:
                raw = Path(directory)
                receipt = worker.capture_raw({"scanId": 122705}, raw, 122705)
                self.assertEqual((raw / "122705.tif").read_bytes(), b"original GeoTIFF")
                self.assertEqual(json.loads(receipt.read_text())["geotiff"]["bytes"], 16)
                self.assertEqual(worker.capture_raw({"scanId": 122705}, raw, 122705), receipt)
                self.assertEqual(len(calls), 1)
        finally:
            worker.stream_geotiff = original

    def test_failed_stream_leaves_no_original_or_receipt(self):
        original = worker.stream_geotiff
        try:
            def fail(_item, emit):
                emit(b"partial")
                raise ValueError("incomplete provider response")
            worker.stream_geotiff = fail
            with TemporaryDirectory() as directory:
                raw = Path(directory)
                with self.assertRaisesRegex(ValueError, "incomplete"):
                    worker.capture_raw({"scanId": 122705}, raw, 122705)
                self.assertEqual(list(raw.iterdir()), [])
        finally:
            worker.stream_geotiff = original


if __name__ == "__main__":
    unittest.main()
