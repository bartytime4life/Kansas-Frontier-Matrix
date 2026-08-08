import importlib.util, json
from pathlib import Path
ROOT=Path(__file__).parents[2]
SPEC=importlib.util.spec_from_file_location("sha", ROOT/"tools/validators/source/validate_source_health_assessment.py")
M=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(M)
def load(rel): return json.loads((ROOT/rel).read_text())
def test_healthy_not_modified():
    assert M.validate_doc(load("fixtures/contracts/v1/source/source_health_assessment/valid/healthy_not_modified.json")) == []
def test_timeout_cannot_be_healthy():
    assert any("failed retrieval cannot be HEALTHY" in e for e in M.validate_doc(load("fixtures/contracts/v1/source/source_health_assessment/invalid/timeout_marked_healthy.json")))
