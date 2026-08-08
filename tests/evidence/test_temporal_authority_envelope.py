import importlib.util
from pathlib import Path

ROOT=Path(__file__).parents[2]
SPEC=importlib.util.spec_from_file_location("tae", ROOT/"tools/validators/evidence/validate_temporal_authority_envelope.py")
M=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(M)

def load(rel):
    import json
    return json.loads((ROOT/rel).read_text())

def test_valid_fixture():
    assert M.validate_doc(load("fixtures/contracts/v1/evidence/temporal_authority_envelope/valid/current_observation.json")) == []

def test_inverted_validity_rejected():
    assert any("valid_from" in e for e in M.validate_doc(load("fixtures/contracts/v1/evidence/temporal_authority_envelope/invalid/inverted_validity.json")))

def test_source_after_retrieval_rejected():
    assert any("source_updated_at" in e for e in M.validate_doc(load("fixtures/contracts/v1/evidence/temporal_authority_envelope/invalid/source_after_retrieval.json")))
