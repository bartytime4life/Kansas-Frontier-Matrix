import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/source/validate_official_source_snapshot_lineage_assessment.py"
FIXTURE_ROOT = ROOT / "fixtures/contracts/v1/source/official_source_snapshot_lineage_assessment"

spec = importlib.util.spec_from_file_location("snapshot_lineage_validator", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def load_fixture(name: str):
    return json.loads((FIXTURE_ROOT / name).read_text())


def test_valid_fixture_matrix_passes():
    for name in ("superseded.json", "corrected.json", "conflicted.json"):
        assert validator.validate(load_fixture(name)) == (True, "PASS")


def test_assessment_id_is_deterministic():
    obj = load_fixture("corrected.json")
    assert obj["assessment_id"] == validator.expected_id(obj)


def test_lineage_reference_must_remain_inside_snapshot_set():
    obj = load_fixture("superseded.json")
    obj["supersedes"] = ["kfm:source-snapshot:" + "3" * 64]
    obj["assessment_id"] = validator.expected_id(obj)
    assert validator.validate(obj) == (False, "LINEAGE_REF_OUTSIDE_SET")


def test_conflict_cannot_select_preferred_snapshot():
    obj = load_fixture("conflicted.json")
    obj["preferred_snapshot_ref"] = obj["snapshot_refs"][0]
    obj["assessment_id"] = validator.expected_id(obj)
    assert validator.validate(obj) == (False, "CONFLICTED_RULE")


def test_reason_code_must_match_lineage_state():
    obj = load_fixture("corrected.json")
    obj["reason_codes"] = ["NEWER_SNAPSHOT_SUPERSEDES_PRIOR"]
    obj["assessment_id"] = validator.expected_id(obj)
    assert validator.validate(obj) == (False, "REASON_CODE_MISMATCH")


def test_publication_authority_cannot_be_escalated():
    obj = copy.deepcopy(load_fixture("superseded.json"))
    obj["publication_authorized"] = True
    obj["assessment_id"] = validator.expected_id(obj)
    assert validator.validate(obj) == (False, "SCHEMA_INVALID")
