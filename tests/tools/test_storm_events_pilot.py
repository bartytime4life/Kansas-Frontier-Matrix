"""Storm Events pilot store: capture -> WORK candidate, exact replay, quarantine, no release writes."""
import json

import pytest

from tests.domains.hazards.storm_events_fixtures import DETAILS, acquired
from tools.local_data import storm_events_pilot as pilot
from tools.local_data.manage import init_store


def store(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    return root


def test_stage_writes_a_candidate_and_replay_reproduces_it(tmp_path):
    root = store(tmp_path)
    first = pilot.stage(root, acquired())
    assert (first["outcome"], first["reason_code"], first["released"]) == ("CANDIDATE_READY", "REVIEW_REQUIRED", False)
    assert first["counts"] == {"data_year": 2025, "source_file": DETAILS, "observations": 6, "withheld": 2,
                               "freshness": "CURRENT", "coverage": "NOT_ESTABLISHED"}
    short = first["candidate_id"].split(":")[1]
    candidate = json.loads((root / "data/work/hazards/noaa-storm-events" / short / "candidate.json").read_text())
    assert candidate["candidate_id"] == first["candidate_id"] and candidate["review_state"] == "PENDING"
    assert (root / "data/receipts/validation/hazards" / short / "validation.json").is_file()
    assert pilot.replay(root, first["capture_id"]) == first
    loaded = pilot.load_capture(root, first["capture_id"])
    assert loaded.manifest["capture_id"] == first["capture_id"] and len(loaded.objects) == 2
    assert not (root / "release").exists()
    assert not [p for p in (root / "data/published").rglob("*") if p.is_file()]


def test_a_capture_that_does_not_normalize_is_quarantined(tmp_path):
    root = store(tmp_path)
    bad = acquired(lambda key, text: text if key == "listing" else text.replace("DAMAGE_PROPERTY,", "DAMAGE_PROP,", 1))
    result = pilot.stage(root, bad)
    assert (result["outcome"], result["candidate_id"], result["counts"]) == ("QUARANTINED", None, {})
    assert not (root / "data/work/hazards").exists()
    run = result["capture_id"].split(":")[1]
    assert (root / "data/receipts/ingest/noaa-storm-events" / run / "quarantined.json").is_file()


def test_a_manifest_that_does_not_hash_to_its_id_writes_nothing(tmp_path):
    root = store(tmp_path)
    source = acquired()
    forged = type(source)({**source.manifest, "data_year": 2024}, source.objects)
    with pytest.raises(ValueError, match="CAPTURE_DIGEST_MISMATCH"):
        pilot.stage(root, forged)
    assert not (root / "data/quarantine/noaa-storm-events").exists()


def test_load_capture_reads_only_the_listing_and_an_allowlisted_details_file(tmp_path):
    root = store(tmp_path)
    first = pilot.stage(root, acquired())
    path = root / "data/quarantine/noaa-storm-events/runs" / first["capture_id"].split(":")[1] / "manifest.json"
    manifest = json.loads(path.read_text())
    manifest["pages"][1]["key"] = "../../../etc/passwd"
    path.chmod(0o644)
    path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="CAPTURE_PAGE_CHAIN_MISMATCH"):
        pilot.load_capture(root, first["capture_id"])


def test_replay_refuses_unknown_or_malformed_ids(tmp_path):
    root = store(tmp_path)
    with pytest.raises(ValueError, match="INVALID_CAPTURE_ID"):
        pilot.replay(root, "../../etc")
    with pytest.raises(ValueError, match="DIRECTORY_MISSING"):
        pilot.replay(root, "sha256:" + "0" * 64)
    with pytest.raises(ValueError, match="INVALID_OBJECT_DIGEST"):
        pilot.object_path(root, "sha256:../x")


def test_cli_without_network_reports_a_finite_error(tmp_path, capsys, monkeypatch):
    def offline(_year):
        raise ValueError("SOURCE_FETCH_FAILED")
    monkeypatch.setattr(pilot, "capture", offline)
    assert pilot.main(["--root", str(tmp_path / "store"), "capture", "--year", "2025"]) == 1
    assert json.loads(capsys.readouterr().out) == {"outcome": "ERROR", "reason_code": "PILOT_OPERATION_FAILED"}
