from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

from tools.ingest.runner import run_once
from tools.ingest.watcher import check_sources
from tools.validators.basic import validate_tree


class Handler(BaseHTTPRequestHandler):
    body = b"abc"

    def log_message(self, fmt: str, *args: Any) -> None:
        return

    def do_HEAD(self) -> None:
        self.send_response(200)
        self.send_header("ETag", '"abc"')
        self.send_header("Last-Modified", "Tue, 05 May 2026 12:00:00 GMT")
        self.send_header("Content-Length", str(len(self.body)))
        self.end_headers()

    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-Length", str(len(self.body)))
        self.end_headers()
        self.wfile.write(self.body)


def _config(tmp_path: Path, url: str) -> Path:
    cfg = {
        "runner": {
            "token_rate_per_minute": 60,
            "token_burst": 10,
            "meta_dir": str(tmp_path / ".last_meta"),
            "queue_path": str(tmp_path / ".queue" / "watcher.events.jsonl"),
            "dlq_path": str(tmp_path / ".queue" / "dlq.events.jsonl"),
            "state_dir": str(tmp_path / ".state"),
            "work_dir": str(tmp_path / "WORK"),
            "receipts_dir": str(tmp_path / "receipts"),
        },
        "sources": [
            {
                "source_id": "s",
                "url": url,
                "download_key": "demo://s",
                "artifact_name": "s.bin",
                "validators": ["shape:v1"],
            }
        ],
    }
    p = tmp_path / "config.json"
    p.write_text(json.dumps(cfg), encoding="utf-8")
    return p


def test_basic_validator_catches_tampered_bundle(tmp_path: Path) -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        config = _config(tmp_path, f"http://127.0.0.1:{server.server_port}/s.bin")
        check_sources(config)
        result = run_once(config, sign_override=False)
        receipt_path = Path(result["results"][0]["receipt_path"])
        assert validate_tree(tmp_path / "receipts") == []
        bundle_path = receipt_path.parent / "evidence_bundle.json"
        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
        bundle["notes"].append("tampered")
        bundle_path.write_text(json.dumps(bundle), encoding="utf-8")
        errors = validate_tree(tmp_path / "receipts")
        assert any("fingerprint mismatch" in error for error in errors)
    finally:
        server.shutdown()
        thread.join(timeout=5)
