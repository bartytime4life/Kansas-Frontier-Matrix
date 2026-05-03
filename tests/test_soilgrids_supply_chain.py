import json
from pathlib import Path

from tools.soilgrids import soilgrids_supply_chain as sc


def test_rejects_missing_supply_chain_spec(tmp_path):
    try:
        sc.load_supply_chain_spec(tmp_path / "missing.json")
        assert False
    except sc.SupplyChainError as e:
        assert e.code == 30


def test_rejects_malformed_supply_chain_spec(tmp_path):
    p = tmp_path / "spec.json"
    p.write_text("{", encoding="utf-8")
    try:
        sc.load_supply_chain_spec(p)
        assert False
    except sc.SupplyChainError as e:
        assert e.code == 30


def test_rejects_unsupported_schema():
    try:
        sc.validate_supply_chain_spec({"schema": "X", "supply_chain_id": "id"})
        assert False
    except sc.SupplyChainError as e:
        assert e.code == 30


def test_supply_chain_spec_hash_stable():
    s = {"schema": "SupplyChainSpec.v1", "supply_chain_id": "a"}
    assert sc.compute_supply_chain_spec_hash(s) == sc.compute_supply_chain_spec_hash(dict(s))


def test_parse_requirements_txt(tmp_path):
    p = tmp_path / "requirements.txt"
    p.write_text("requests==2.32.0\n", encoding="utf-8")
    deps = sc.parse_requirements_txt(p)
    assert deps[0]["name"] == "requests"


def test_dependency_graph_hash_stable():
    deps = [{"name": "requests", "version": "2.32.0", "source": "requirements.txt"}]
    g1 = sc.build_dependency_graph("id", deps)
    g2 = sc.build_dependency_graph("id", deps)
    assert g1["dependency_graph_hash"] == g2["dependency_graph_hash"]


def test_spdx_cdx_consistency():
    deps = [{"name": "requests", "version": "2.32.0"}]
    assert sc.validate_sbom_consistency(sc.build_spdx_sbom("id", deps), sc.build_cyclonedx_sbom("id", deps))


def test_run_cli_outputs_receipt(tmp_path):
    spec = tmp_path / "spec.json"
    spec.write_text(json.dumps({"schema": "SupplyChainSpec.v1", "supply_chain_id": "x", "inventory": {"include_globs": ["*.py"], "exclude_globs": []}, "vulnerabilities": {"mode": "offline"}}), encoding="utf-8")
    (tmp_path / "a.py").write_text("print('x')\n", encoding="utf-8")
    out = tmp_path / "out"
    receipt, code = sc.run_supply_chain_authority(supply_chain_spec=str(spec), repo_root=str(tmp_path), output_root=str(out), mode="sbom", allow_unknown_files=True)
    assert code == 0
    assert receipt.exists()
