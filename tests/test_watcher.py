from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.ingest.models import ProbeResult
from tools.ingest.watcher import check_sources


def _write_config(tmp_path: Path, url: str = "http://example.test/data.csv") -> Path:
    cfg = {
        "runner": {
            "meta_dir": str(tmp_path / ".last_meta"),
            "queue_path": str(tmp_path / ".queue" / "watcher.events.jsonl"),
            "dlq_path": str(tmp_path / ".queue" / "dlq.events.jsonl"),
            "state_dir": str(tmp_path / ".state"),
            "work_dir": str(tmp_path / "WORK"),
            "receipts_dir": str(tmp_path / "receipts"),
        },
        "sources": [
            {
                "source_id": "usgs/huc12-comid",
                "url": url,
                "download_key": "demo://data.csv",
                "source_version": "v1",
                "domain": "hydrology",
                "policy_label": "restricted",
                "rights_status": "controlled",
                "artifact_name": "data.csv",
                "validators": ["shape:v1"],
            }
        ],
    }
    path = tmp_path / "config.json"
    path.write_text(json.dumps(cfg), encoding="utf-8")
    return path


def test_watcher_idempotent_after_first_material_event(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    config = _write_config(tmp_path)

    def fake_head(url, headers):
        return ProbeResult(status=200, etag='"v1"', last_modified="Tue, 05 May 2026 12:00:00 GMT")

    monkeypatch.setattr("tools.ingest.watcher.head_probe", fake_head)
    first = check_sources(config)
    second = check_sources(config)

    assert first["enqueued"] == 1
    assert second["enqueued"] == 0
    meta_files = list((tmp_path / ".last_meta").glob("*.json"))
    assert len(meta_files) == 1
    queue_lines = (tmp_path / ".queue" / "watcher.events.jsonl").read_text(encoding="utf-8").strip().splitlines()
    assert len(queue_lines) == 1


def test_watcher_seed_only_writes_meta_without_event(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    config = _write_config(tmp_path)

    def fake_head(url, headers):
        return ProbeResult(status=200, etag='"v1"', last_modified="Tue, 05 May 2026 12:00:00 GMT")

    monkeypatch.setattr("tools.ingest.watcher.head_probe", fake_head)
    result = check_sources(config, seed_only=True)

    assert result["enqueued"] == 0
    assert list((tmp_path / ".last_meta").glob("*.json"))
    assert not (tmp_path / ".queue" / "watcher.events.jsonl").exists()


def test_missing_http_validators_marked_high_risk(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    config = _write_config(tmp_path)

    def fake_head(url, headers):
        return ProbeResult(status=200, etag=None, last_modified=None)

    monkeypatch.setattr("tools.ingest.watcher.head_probe", fake_head)
    result = check_sources(config)

    assert result["enqueued"] == 1
    event = result["events"][0]
    assert event["high_risk"] is True
    assert "missing_http_validators" in event["reason"]
