import importlib.util, json
from pathlib import Path
ROOT=Path(__file__).parents[2]
SPEC=importlib.util.spec_from_file_location("rbn", ROOT/"tools/validators/evidence/validate_reality_boundary_note.py")
M=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(M)
def load(rel): return json.loads((ROOT/rel).read_text())
def test_valid_synthetic_scene_is_explicitly_illustrative():
    assert M.validate_doc(load("fixtures/contracts/v1/evidence/reality_boundary_note/valid/synthetic_scene.json")) == []
def test_synthetic_cannot_claim_direct_evidence():
    assert any("cannot claim DIRECT_EVIDENCE" in e for e in M.validate_doc(load("fixtures/contracts/v1/evidence/reality_boundary_note/invalid/synthetic_as_direct_evidence.json")))
