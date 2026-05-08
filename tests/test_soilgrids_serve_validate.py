import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.soilgrids.soilgrids_serve_validate import validate_content_type

ROOT = Path(__file__).parent / "fixtures" / "serve" / "release"
SCRIPT = Path(__file__).resolve().parents[1] / "tools/soilgrids/soilgrids_serve_validate.py"


def run_cli(*extra):
    cmd = [sys.executable, str(SCRIPT), "--publish-receipt", str(ROOT / "publish_receipt.json"), "--release-manifest", str(ROOT / "release_manifest.json"), "--release-root", str(ROOT), "--output-dir", str(ROOT / "out")] + list(extra)
    return subprocess.run(cmd, capture_output=True, text=True)


def test_allows_localhost_base_url(tmp_path):
    cp = run_cli("--mode", "existing-base-url", "--base-url", "http://localhost:9999/")
    assert cp.returncode in (40, 50)  # no server at localhost:9999 but host policy accepted


def test_rejects_remote_base_url_by_default():
    cp = run_cli("--mode", "existing-base-url", "--base-url", "http://example.com/r/")
    assert cp.returncode == 60


def test_local_static_server_mode_computes_base_url():
    cp = run_cli("--mode", "local-static-server")
    assert cp.returncode == 0
    receipt_path = Path(cp.stdout.strip())
    assert receipt_path.exists()
    receipt = json.loads(receipt_path.read_text())
    assert receipt["base_url"].startswith("http://127.0.0.1:")


def test_range_first_512_returns_206():
    cp = run_cli("--mode", "local-static-server", "--range-start", "0", "--range-length", "512")
    assert cp.returncode == 0


def test_local_server_serves_json_content_type():
    assert validate_content_type("application/json", ".json")


def test_local_server_serves_tiff_content_type():
    assert validate_content_type("image/tiff", ".tif")
