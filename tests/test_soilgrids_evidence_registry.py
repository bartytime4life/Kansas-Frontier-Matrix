from pathlib import Path
import json
import shutil

import soilgrids_evidence_registry as reg


def test_rejects_missing_evidence_crate(tmp_path):
    p = tmp_path / "missing"
    try:
        reg.load_registry_inputs(p)
        assert False
    except ValueError:
        assert True


def test_validates_crate_checksums():
    crate = reg.load_registry_inputs(Path("tests/fixtures/evidence_registry/valid_crate"))
    ok, errs = reg.validate_crate_checksums(crate)
    assert ok
    assert not errs


def test_rdf_nquads_written(tmp_path):
    entities = [{"registry_entity_id": "a", "entity_type": "e"}]
    edges = []
    sha = reg.build_registry_rdf_export(tmp_path / "rdf/registry.nq", entities, edges)
    assert len(sha) == 64
    assert (tmp_path / "rdf/registry.nq").exists()


def test_openapi_version_3_1_1(tmp_path):
    doc = reg.build_openapi_description(tmp_path / "api/openapi.json")
    assert doc["openapi"] == "3.1.1"


def test_registry_build_end_to_end(tmp_path):
    crate = Path("tests/fixtures/evidence_registry/valid_crate")
    receipt = reg.build_evidence_registry([crate], tmp_path / "registries", "local-registry", "SoilGrids Evidence Registry", "soilgrids-v2")
    assert receipt.exists()
    data = json.loads(receipt.read_text())
    assert data["schema"] == "RegistryReceipt.v1"
