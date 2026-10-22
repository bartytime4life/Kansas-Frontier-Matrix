"""FAA writes use the existing private operator boundary; no live provider."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import io
import json
from pathlib import Path
from threading import Barrier
from types import SimpleNamespace

import pytest

from tools.local_data import candidate_capture as writer
from tools.validators.connector_gate.output_paths import scan_connector_file

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("faa_capture_paths", ROOT / "connectors/faa/capture.py")
capture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capture)


class Response(io.BytesIO):
    status = 200

    def __init__(self, body=b"synthetic archive"):
        super().__init__(body)
        self.headers = {"Content-Length": str(len(body))}

    def geturl(self):
        return capture.PRODUCTS["2026-10-01"]


def test_configured_raw_capture_is_private_and_replay_is_unchanged(tmp_path, monkeypatch):
    monkeypatch.setenv("KFM_DATA_ROOT", str(tmp_path))
    raw = tmp_path / "data/raw/faa"
    raw.mkdir(parents=True)
    calls = []
    def acquire(*args, **kwargs):
        calls.append(1)
        return Response()
    target = capture.capture(raw, "2026-10-01", opener=SimpleNamespace(open=acquire))
    assert target.parent == raw
    assert {path.name for path in target.iterdir()} == {"archive.zip", "receipt.json"}
    assert target.stat().st_mode & 0o077 == 0
    assert all(path.stat().st_mode & 0o077 == 0 for path in target.iterdir())
    receipt = json.loads((target / "receipt.json").read_bytes())
    assert receipt["sha256"] == hashlib.sha256((target / "archive.zip").read_bytes()).hexdigest()
    assert receipt["lifecycle"] == "RAW" and receipt["release_state"] == "HELD"
    before = {path.name: path.read_bytes() for path in target.iterdir()}
    assert capture.capture(raw, "2026-10-01", opener=SimpleNamespace(open=acquire)) == target
    assert calls == [1]
    assert before == {path.name: path.read_bytes() for path in target.iterdir()}


@pytest.mark.parametrize("lane", ["data/published", "data/catalog", "data/work", "release", "apps/site/source/public"])
def test_configured_nonraw_destinations_denied_before_acquisition(tmp_path, monkeypatch, lane):
    monkeypatch.setenv("KFM_DATA_ROOT", str(tmp_path))
    root = tmp_path / lane
    root.mkdir(parents=True)
    def forbidden(*args, **kwargs):
        pytest.fail("A denied destination must not acquire provider bytes")
    with pytest.raises(ValueError, match="CANDIDATE_OUTPUT_NOT_RAW"):
        capture.capture(root, "2026-10-01", opener=SimpleNamespace(open=forbidden))
    assert not list(root.iterdir())


def test_repository_destination_denied_even_if_store_points_to_repository(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "REPOSITORY", tmp_path)
    monkeypatch.setenv("KFM_DATA_ROOT", str(tmp_path))
    root = tmp_path / "data/raw/faa"
    root.mkdir(parents=True)
    with pytest.raises(ValueError, match="CANDIDATE_INSIDE_REPOSITORY"):
        capture.capture(root, "2026-10-01", opener=SimpleNamespace(open=lambda *a, **k: pytest.fail("network")))
    assert not list(root.iterdir())


def test_symlink_and_traversal_roots_denied(tmp_path, monkeypatch):
    monkeypatch.delenv("KFM_DATA_ROOT", raising=False)
    root = tmp_path / "raw"
    root.mkdir()
    link = tmp_path / "link"
    link.symlink_to(root, target_is_directory=True)
    for unsafe in (link, root / ".." / "raw"):
        with pytest.raises(ValueError, match="RAW_ROOT_INVALID|CANDIDATE_PATH_INVALID"):
            capture.capture(unsafe, "2026-10-01")
    assert not list(root.iterdir())


def test_receipt_write_failure_removes_partial_candidate(tmp_path, monkeypatch):
    original = capture.write_candidate
    def fail_receipt(directory, name, body):
        if name == "receipt.json":
            raise OSError("synthetic interrupted receipt")
        return original(directory, name, body)
    monkeypatch.setattr(capture, "write_candidate", fail_receipt)
    with pytest.raises(OSError, match="interrupted receipt"):
        capture.capture(tmp_path, "2026-10-01", opener=SimpleNamespace(open=lambda *a, **k: Response()))
    assert not list(tmp_path.iterdir())


def test_concurrent_capture_preserves_one_complete_candidate(tmp_path):
    barrier = Barrier(2)
    def acquire(*args, **kwargs):
        barrier.wait(timeout=10)
        return Response()
    def run():
        try:
            return capture.capture(tmp_path, "2026-10-01", opener=SimpleNamespace(open=acquire))
        except FileExistsError:
            return None
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(lambda _: run(), range(2)))
    assert sum(result is not None for result in results) == 1
    target = tmp_path / "faa-apt-2026-10-01"
    assert list(tmp_path.iterdir()) == [target]
    assert set(path.name for path in target.iterdir()) == {"archive.zip", "receipt.json"}
    assert capture.capture(tmp_path, "2026-10-01") == target


def test_capture_has_no_unresolved_connector_output_sinks():
    assert not scan_connector_file(ROOT / "connectors/faa/capture.py", ROOT)
