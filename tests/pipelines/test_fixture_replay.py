"""Exercise the bound transforms on sealed synthetic captures and reject broken closure."""
from copy import deepcopy
import base64
import json
from pathlib import Path
import subprocess
import sys

import pytest

from connectors_core.captured_json import canonical_bytes
from pipelines.fixture_replay import PIPELINES, fixture_path, replay_fixture, replay_packet
from tools.validators.validate_pipeline_spec_declarations import validate_declaration

ROOT = Path(__file__).resolve().parents[2]
CASES = [
    ("earthquake", "hazards/usgs_earthquake.yaml", 5),
    ("storm-events", "hazards/noaa_storm_events.yaml", 6),
    ("water-observations", "hydrology/usgs_water_observations.yaml", 2),
]


@pytest.mark.parametrize("name,declaration,count", CASES)
def test_sealed_capture_runs_bound_pipeline_without_writes(name, declaration, count):
    first = replay_fixture(name)
    assert first == replay_fixture(name)
    assert first["fixture_only"] is True
    candidate, report = first["candidate"], first["validation"]
    assert report["outcome"] == "PASS"
    assert len(candidate["observations"]) == count
    assert report["review_required"] is True
    assert candidate["release_state"] == "UNRELEASED"
    assert candidate["source_admission"] == candidate["review_state"] == "PENDING"
    for authority in ("promotion_authorized", "release_authorized", "publication_authorized"):
        assert report[authority] is False
    path = ROOT / "pipeline_specs" / declaration
    result, spec = validate_declaration(path, expected_path=path.relative_to(ROOT).as_posix())
    assert not result.findings
    assert spec["implementation_status"] == "IMPLEMENTED_FIXTURE_FIRST"
    assert fixture_path(name).relative_to(ROOT).as_posix() in spec["bindings"]["fixture_refs"]
    assert "pipelines/fixture_replay.py" in spec["bindings"]["implementation_refs"]
    assert ".github/workflows/pipeline-spec-declarations.yml" in spec["bindings"]["workflow_refs"]
    assert spec["execution"]["mode"] == "FIXTURE_ONLY"
    assert spec["lifecycle"]["writes_targets"] is False


@pytest.mark.parametrize("name", PIPELINES)
def test_tampered_capture_is_refused(name):
    packet = json.loads(fixture_path(name).read_bytes())
    key = next(iter(packet["objects_base64"]))
    packet["objects_base64"][key] = base64.b64encode(b"substituted source bytes").decode()
    with pytest.raises(ValueError, match="FIXTURE_OBJECT_DIGEST_MISMATCH"):
        replay_packet(name, canonical_bytes(packet))


@pytest.mark.parametrize("name", PIPELINES)
def test_incomplete_and_surplus_object_closure_is_refused(name):
    packet = json.loads(fixture_path(name).read_bytes())
    incomplete = deepcopy(packet)
    incomplete["objects_base64"].pop(next(iter(incomplete["objects_base64"])))
    with pytest.raises(ValueError, match="FIXTURE_OBJECT_CLOSURE_INVALID"):
        replay_packet(name, canonical_bytes(incomplete))
    packet["manifest"]["pages"][0]["bytes"] = 0
    with pytest.raises(ValueError, match="FIXTURE_OBJECT_CLOSURE_INVALID"):
        replay_packet(name, canonical_bytes(packet))


def test_replay_identity_and_packet_boundaries():
    packet = json.loads(fixture_path("earthquake").read_bytes())
    packet["expected_candidate_id"] = "sha256:" + "0" * 64
    with pytest.raises(ValueError, match="FIXTURE_REPLAY_IDENTITY_MISMATCH"):
        replay_packet("earthquake", canonical_bytes(packet))
    packet["fixture_only"] = False
    with pytest.raises(ValueError, match="FIXTURE_PACKET_INVALID"):
        replay_packet("earthquake", canonical_bytes(packet))
    with pytest.raises(ValueError, match="FIXTURE_PIPELINE_UNKNOWN"):
        replay_packet("https://example.test", b"{}")
    with pytest.raises(ValueError, match="JSON_BYTE_LIMIT"):
        replay_packet("earthquake", b" " * (1024 * 1024 + 1))
    with pytest.raises(ValueError, match="INVALID_JSON"):
        replay_packet("earthquake", b'{"fixture_only":true,"fixture_only":false}')


@pytest.mark.parametrize("name", PIPELINES)
def test_cli_replays_in_an_empty_directory_without_creating_files(name, tmp_path, monkeypatch):
    monkeypatch.setenv("PYTHONPATH", str(ROOT / "tools/ci/kfm_no_network") + ":" + str(ROOT)
                       + ":" + str(ROOT / "packages/connectors-core/src"))
    result = subprocess.run([sys.executable, "-B", "-m", "pipelines.fixture_replay", name],
                            cwd=tmp_path, check=True, capture_output=True, text=True)
    assert json.loads(result.stdout) == replay_fixture(name)
    assert not result.stderr
    assert list(tmp_path.iterdir()) == []
