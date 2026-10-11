"""USCRN daily soil pilot store: capture -> WORK candidate, exact replay, quarantine, no release writes."""
import json

import pytest

from tests.domains.soil.uscrn_daily_fixtures import acquired
from tools.local_data import uscrn_daily_pilot as pilot
from tools.local_data.manage import init_store


def store(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    return root


def test_stage_writes_a_candidate_and_replay_reproduces_it(tmp_path):
    root = store(tmp_path)
    first = pilot.stage(root, acquired())
    assert (first["outcome"], first["reason_code"], first["released"]) == ("CANDIDATE_READY", "REVIEW_REQUIRED", False)
    assert first["counts"] == {"stations": 2, "observations": 600, "withheld": 28, "coverage": "COMPLETE"}
    short = first["candidate_id"].split(":")[1]
    candidate = json.loads((root / "data/work/soil/noaa-uscrn-daily" / short / "candidate.json").read_text())
    assert candidate["candidate_id"] == first["candidate_id"] and candidate["review_state"] == "PENDING"
    assert pilot.replay(root, first["capture_id"]) == first
    assert not (root / "release").exists()
    assert not [p for p in (root / "data/published").rglob("*") if p.is_file()]


def test_a_capture_that_does_not_normalize_is_quarantined(tmp_path):
    root = store(tmp_path)
    bad = acquired(lambda key, text: text.replace(" 0.280 ", " 0.28x ", 1) if key.endswith("KS_Manhattan_6_SSW.txt") else text)
    result = pilot.stage(root, bad)
    assert (result["outcome"], result["candidate_id"], result["counts"]) == ("QUARANTINED", None, {})
    assert not (root / "data/work/soil").exists()
    run = result["capture_id"].split(":")[1]
    assert (root / "data/receipts/ingest/noaa-uscrn-daily" / run / "quarantined.json").is_file()


def test_a_manifest_that_does_not_hash_to_its_id_writes_nothing(tmp_path):
    root = store(tmp_path)
    source = acquired()
    forged = type(source)({**source.manifest, "end": "2026-10-09"}, source.objects)
    with pytest.raises(ValueError, match="CAPTURE_DIGEST_MISMATCH"):
        pilot.stage(root, forged)
    assert not (root / "data/quarantine/noaa-uscrn-daily").exists()


def test_replay_refuses_unknown_or_malformed_ids(tmp_path):
    root = store(tmp_path)
    with pytest.raises(ValueError, match="INVALID_CAPTURE_ID"):
        pilot.replay(root, "../../etc")
    with pytest.raises(ValueError, match="DIRECTORY_MISSING"):
        pilot.replay(root, "sha256:" + "0" * 64)
    with pytest.raises(ValueError, match="INVALID_OBJECT_DIGEST"):
        pilot.object_path(root, "sha256:../x")


def test_cli_without_network_reports_a_finite_error(tmp_path, capsys, monkeypatch):
    def offline(_end):
        raise ValueError("SOURCE_FETCH_FAILED")
    monkeypatch.setattr(pilot, "capture", offline)
    assert pilot.main(["--root", str(tmp_path / "store"), "capture", "--end", "2026-10-10"]) == 1
    assert json.loads(capsys.readouterr().out) == {"outcome": "ERROR", "reason_code": "PILOT_OPERATION_FAILED"}
