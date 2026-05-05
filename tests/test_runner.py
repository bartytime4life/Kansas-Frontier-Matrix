from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

from tools.ingest.event_queue import JsonlQueue
from tools.ingest.models import ProbeResult
from tools.ingest.runner import run_once
from tools.ingest.token_bucket import TokenBucketStore
from tools.ingest.watcher import check_sources


class FixtureHandler(BaseHTTPRequestHandler):
    body = b"huc12,comid\n070900020101,123456\n"
    etag = '"fixture-v1"'
    last_modified = "Tue, 05 May 2026 12:00:00 GMT"

    def log_message(self, fmt: str, *args: Any) -> None:
        return

    def do_HEAD(self) -> None:
        self.send_response(200)
        self.send_header("ETag", self.etag)
        self.send_header("Last-Modified", self.last_modified)
        self.send_header("Content-Type", "text/csv")
        self.send_header("Content-Length", str(len(self.body)))
        self.end_headers()

    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("ETag", self.etag)
        self.send_header("Last-Modified", self.last_modified)
        self.send_header("Content-Type", "text/csv")
        self.send_header("Content-Length", str(len(self.body)))
        self.end_headers()
        self.wfile.write(self.body)


def _config(tmp_path: Path, url: str) -> Path:
    cfg = {
        "runner": {
            "max_changes_per_run": 10,
            "batch_size": 5,
            "max_workers": 2,
            "token_rate_per_minute": 60,
            "token_burst": 10,
            "max_download_bytes": 1024 * 1024,
            "max_retries": 1,
            "meta_dir": str(tmp_path / ".last_meta"),
            "queue_path": str(tmp_path / ".queue" / "watcher.events.jsonl"),
            "dlq_path": str(tmp_path / ".queue" / "dlq.events.jsonl"),
            "state_dir": str(tmp_path / ".state"),
            "work_dir": str(tmp_path / "WORK"),
            "receipts_dir": str(tmp_path / "receipts"),
            "signing": {"enabled": False},
        },
        "sources": [
            {
                "source_id": "usgs/huc12-comid",
                "url": url,
                "download_key": "demo://fixture.csv",
                "source_version": "v1",
                "domain": "hydrology",
                "policy_label": "restricted",
                "rights_status": "controlled",
                "artifact_name": "fixture.csv",
                "validators": ["shape:v1"],
            }
        ],
    }
    path = tmp_path / "config.json"
    path.write_text(json.dumps(cfg), encoding="utf-8")
    return path


def test_token_bucket_throttles(tmp_path: Path) -> None:
    bucket = TokenBucketStore(tmp_path / "bucket.json")
    assert bucket.try_consume("hot/source", rate_per_minute=0, burst=1)
    assert not bucket.try_consume("hot/source", rate_per_minute=0, burst=1)


def test_runner_builds_unsigned_evidence_bundle(tmp_path: Path) -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 0), FixtureHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        config = _config(tmp_path, f"http://127.0.0.1:{server.server_port}/fixture.csv")
        watch = check_sources(config)
        assert watch["enqueued"] == 1
        result = run_once(config, sign_override=False)
        assert result["dequeued"] == 1
        assert result["results"][0]["status"] == "BUILT"
        receipt_path = Path(result["results"][0]["receipt_path"])
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        assert receipt["result"] == "PENDING_SIGNATURE"
        assert (receipt_path.parent / "evidence_bundle.json").exists()
        assert (receipt_path.parent / "decision_log.json").exists()
    finally:
        server.shutdown()
        thread.join(timeout=5)


def test_runner_dlq_for_missing_http_validators(tmp_path: Path) -> None:
    config = _config(tmp_path, "http://example.test/unused")
    event = {
        "source_id": "usgs/huc12-comid",
        "prev_spec_hash": None,
        "next_spec_hash": "sha256-highrisk",
        "material": True,
        "reason": "initial:missing_http_validators",
        "high_risk": True,
        "seen_at": "2026-05-05T12:00:00Z",
    }
    JsonlQueue(tmp_path / ".queue" / "watcher.events.jsonl").append(event)
    result = run_once(config, sign_override=False)
    assert result["results"][0]["status"] == "DLQ"
    assert "fail_closed_missing_http_validators" in (tmp_path / ".queue" / "dlq.events.jsonl").read_text(encoding="utf-8")
