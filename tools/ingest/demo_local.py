from __future__ import annotations

import argparse
import gzip
import json
import shutil
import threading
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

from .runner import run_once
from .watcher import check_sources


HUC12_BYTES = gzip.compress(b"huc12,comid\n070900020101,123456\n070900020102,123457\n")
PMTILES_BYTES = b"PMTiles\x03\x00demo-delta-fixture"


class DemoHandler(BaseHTTPRequestHandler):
    fixtures = {
        "/huc12-comid.csv.gz": {
            "body": HUC12_BYTES,
            "etag": '"demo-huc12-v1"',
            "last_modified": "Tue, 05 May 2026 12:00:00 GMT",
            "content_type": "application/gzip",
        },
        "/delta.pmtiles": {
            "body": PMTILES_BYTES,
            "etag": '"demo-pmtiles-v1"',
            "last_modified": "Tue, 05 May 2026 12:05:00 GMT",
            "content_type": "application/vnd.pmtiles",
        },
        "/server-error": {
            "body": b"",
            "etag": '"server-error"',
            "last_modified": "Tue, 05 May 2026 12:05:00 GMT",
            "content_type": "text/plain",
            "status": 503,
        },
    }

    def log_message(self, fmt: str, *args: Any) -> None:  # keep demo output clean
        return

    def _serve(self, include_body: bool) -> None:
        item = self.fixtures.get(self.path)
        if item is None:
            self.send_response(404)
            self.end_headers()
            return
        status = int(item.get("status", 200))
        body = item["body"]
        self.send_response(status)
        self.send_header("ETag", item["etag"])
        self.send_header("Last-Modified", item["last_modified"])
        self.send_header("Content-Type", item["content_type"])
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if include_body and status < 500:
            self.wfile.write(body)

    def do_HEAD(self) -> None:
        self._serve(include_body=False)

    def do_GET(self) -> None:
        self._serve(include_body=True)


def build_config(root: Path, port: int) -> Path:
    config = {
        "runner": {
            "max_changes_per_run": 10,
            "batch_size": 5,
            "max_workers": 4,
            "token_rate_per_minute": 60,
            "token_burst": 10,
            "max_download_bytes": 1024 * 1024,
            "max_retries": 1,
            "backoff_base_seconds": 1,
            "backoff_max_seconds": 3,
            "fail_on_missing_http_validators": True,
            "meta_dir": str(root / ".last_meta"),
            "queue_path": str(root / ".queue" / "watcher.events.jsonl"),
            "dlq_path": str(root / ".queue" / "dlq.events.jsonl"),
            "state_dir": str(root / ".state"),
            "work_dir": str(root / "WORK"),
            "receipts_dir": str(root / "receipts"),
            "signing": {
                "enabled": False,
                "mode": "keyless",
                "certificate_identity": "",
                "certificate_identity_regexp": ".*",
                "certificate_oidc_issuer": "https://token.actions.githubusercontent.com",
                "key": "",
                "public_key": "",
            },
        },
        "sources": [
            {
                "source_id": "usgs/huc12-comid",
                "url": f"http://127.0.0.1:{port}/huc12-comid.csv.gz",
                "download_key": "demo://huc12-comid.csv.gz",
                "source_version": "v1",
                "domain": "hydrology",
                "policy_label": "restricted",
                "rights_status": "controlled",
                "artifact_name": "huc12-comid.csv.gz",
                "validators": ["shape:v1", "policy:hydrology/publication.rego"],
            },
            {
                "source_id": "pmtiles/example-delta",
                "url": f"http://127.0.0.1:{port}/delta.pmtiles",
                "download_key": "demo://delta.pmtiles",
                "source_version": "v1",
                "domain": "tiles",
                "policy_label": "restricted",
                "rights_status": "controlled",
                "artifact_name": "example.pmtiles",
                "validators": ["shape:v1", "policy:tiles/publication.rego"],
            },
            {
                "source_id": "demo/server-error-fail-closed",
                "url": f"http://127.0.0.1:{port}/server-error",
                "download_key": "demo://server-error",
                "source_version": "v1",
                "domain": "test",
                "policy_label": "restricted",
                "rights_status": "controlled",
                "artifact_name": "server-error.txt",
                "validators": ["shape:v1"],
            },
        ],
    }
    root.mkdir(parents=True, exist_ok=True)
    config_path = root / "sources.demo.json"
    config_path.write_text(json.dumps(config, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return config_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run local KFM HUC12/PMTiles demo")
    parser.add_argument("--root", default=".demo", help="Demo output root")
    parser.add_argument("--clean", action="store_true", help="Remove demo root before running")
    parser.add_argument("--sign", action="store_true", help="Force cosign signing")
    args = parser.parse_args(argv)

    root = Path(args.root)
    if args.clean and root.exists():
        shutil.rmtree(root)
    server = ThreadingHTTPServer(("127.0.0.1", 0), DemoHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        config_path = build_config(root, server.server_port)
        watcher_result = check_sources(config_path)
        runner_result = run_once(config_path, sign_override=args.sign)
        print(json.dumps({"config": str(config_path), "watcher": watcher_result, "runner": runner_result}, indent=2, sort_keys=True))
        return 1 if any(item.get("status") == "DLQ" for item in runner_result.get("results", [])) else 0
    finally:
        server.shutdown()
        thread.join(timeout=5)


if __name__ == "__main__":
    raise SystemExit(main())
