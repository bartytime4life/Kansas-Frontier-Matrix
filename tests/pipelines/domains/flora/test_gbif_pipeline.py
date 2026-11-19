"""Full GBIF intake composition retains source identity, schema and authority limits."""
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys

import pytest

from connectors_core.captured_json import canonical_bytes
from pipelines.domains.flora.gbif_ingest import prepare_records, replay_fixture
from tools.validators.validate_pipeline_spec_declarations import validate_declaration

ROOT = Path(__file__).resolve().parents[4]
FIXTURES = ROOT / "fixtures/domains/flora/flora_occurrence_candidate"


def record():
    return json.loads((FIXTURES / "input/gbif_big_bluestem.json").read_text())


def run(records):
    return prepare_records(canonical_bytes({"records": records}))


@pytest.mark.parametrize("name,file", [("big-bluestem", "gbif_big_bluestem"), ("no-coordinate", "gbif_no_coordinate")])
def test_replay_matches_existing_golden_candidates_and_stays_unapproved(name, file):
    result = replay_fixture(name)
    expected = json.loads((FIXTURES / f"expected/{file}.candidate.json").read_text())
    assert list(result.candidates) == [expected]
    assert result == replay_fixture(name)
    summary = result.summary()
    assert summary["outcome"] == "REVIEW_REQUIRED"
    assert summary["normalized"] == summary["proposed_for_work"] == 1
    assert summary["invalid"] == 0
    assert all(value is False for key, value in summary.items() if key.endswith(("_authorized", "_allowed", "_admitted", "_completed", "_executed")))
    assert not any(value is True for value in result.decisions[0]["governance"].values())


def test_missing_identity_is_explicit_and_valid_sibling_is_retained():
    missing = record()
    missing.pop("key")
    result = run([record(), missing])
    assert result.summary()["outcome"] == "PARTIAL"
    assert result.summary()["normalized"] == result.summary()["invalid"] == 1
    assert result.issues == ((1, "SOURCE_RECORD_ID_MISSING"),)


def test_invalid_geometry_does_not_escape_and_duplicate_identity_refuses_whole_batch():
    invalid = record()
    invalid["decimalLongitude"] = 181
    result = run([invalid])
    assert result.summary()["outcome"] == "ERROR"
    assert not result.candidates
    with pytest.raises(ValueError, match="GBIF_DUPLICATE_SOURCE_IDENTITY"):
        run([record(), deepcopy(record())])


@pytest.mark.parametrize("license", [None, "CC-BY-NC-4.0", "https://creativecommons.org/licenses/by/4.0/legalcode"])
def test_unresolved_or_conditional_rights_are_quarantined_without_remapping_source_terms(license):
    value = record()
    value["license"] = license
    result = run([value])
    assert result.summary()["quarantined"] == 1
    assert result.candidates[0]["source_context"]["license"] == license
    assert result.decisions[0]["governance"]["legal_rights_decided"] is False


def test_sensitive_exact_geometry_stays_private_and_held():
    value = record()
    value["informationWithheld"] = "synthetic sensitivity hint"
    result = run([value])
    assert result.summary()["held"] == 1
    assert result.candidates[0]["spatial"]["coordinate_exposure"] == "INTERNAL_EXACT"
    assert result.decisions[0]["sensitivity"]["disposition"] == "GENERALIZE_REQUIRED"
    assert "coordinates" not in canonical_bytes(result.summary()).decode()
    assert "SYNTH" not in repr(result)


@pytest.mark.parametrize("packet", [{"records": []}, {"records": [None]}, {"records": [{}] * 301}, {"records": [{}], "activate": True}])
def test_batch_shape_is_bounded(packet):
    with pytest.raises(ValueError, match="GBIF_BATCH_SHAPE_INVALID"):
        prepare_records(canonical_bytes(packet))


def test_bound_declaration_and_aggregate_only_cli(tmp_path, monkeypatch):
    declaration = ROOT / "pipeline_specs/flora/gbif_ingest.yaml"
    status, spec = validate_declaration(declaration)
    assert not status.findings
    assert spec["implementation_status"] == "IMPLEMENTED_FIXTURE_FIRST"
    assert spec["execution"]["source_activation"] == "DENIED"
    assert "SOURCE_ADMISSION_UNVERIFIED" in spec["reason_codes"]
    monkeypatch.setenv("PYTHONPATH", str(ROOT / "tools/ci/kfm_no_network") + ":" + str(ROOT))
    result = subprocess.run([sys.executable, "-B", "-m", "pipelines.domains.flora.gbif_ingest", "big-bluestem"],
                            cwd=tmp_path, capture_output=True, text=True, check=True)
    assert json.loads(result.stdout) == replay_fixture("big-bluestem").summary()
    assert not result.stderr
    assert "Andropogon" not in result.stdout and "-98.123456" not in result.stdout
    assert list(tmp_path.iterdir()) == []


def test_cli_failure_does_not_echo_input_or_file_exception(monkeypatch, capsys):
    from pipelines.domains.flora import gbif_ingest

    def fail(_name):
        raise ValueError("private candidate payload")

    monkeypatch.setattr(gbif_ingest, "replay_fixture", fail)
    assert gbif_ingest.main(["big-bluestem"]) == 1
    captured = capsys.readouterr()
    assert not captured.out
    assert json.loads(captured.err) == {"outcome": "ERROR", "reason": "GBIF_FIXTURE_REPLAY_FAILED"}


def test_existing_peer_rules_propose_the_same_duplicate_target_after_reordering():
    first, second = record(), record()
    second["key"] += 1
    result = run([first, second])
    assert result == run([second, first])
    assert result.summary()["duplicates"] == result.summary()["proposed_for_work"] == 1
    assert result.decisions[1]["duplicate"]["duplicate_of_candidate_ref"] == result.candidates[0]["candidate_id"]
    assert result.decisions[1]["duplicate"]["method"] == "PRIMARY_INSTITUTION_CATALOG"
    assert result.decisions[1]["governance"]["lifecycle_transition_executed"] is False


def test_duplicate_proposals_do_not_hide_rights_or_sensitivity_holds():
    first, restricted = record(), record()
    restricted["key"] += 1
    restricted["license"] = "CC-BY-NC-4.0"
    restricted["informationWithheld"] = "synthetic sensitivity hint"
    summary = run([first, restricted]).summary()
    assert summary["duplicates"] == summary["quarantined"] == summary["held"] == 1
    assert summary["outcome"] == "REVIEW_REQUIRED"
    assert summary["public_use_allowed"] is False
