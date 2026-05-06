import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.soilgrids import soilgrids_assurance_pack as mod


def _spec():
    return json.loads(Path("assurance/assurance_spec_example.json").read_text())


def test_rejects_missing_assurance_spec(tmp_path):
    rc = subprocess.run([sys.executable, "soilgrids_assurance_pack.py", "--assurance-spec", "missing.json", "--output-root", str(tmp_path), "--mode", "catalog-only", "--allow-absolute-output"], capture_output=True, text=True)
    assert rc.returncode == 40

def test_rejects_unsupported_assurance_schema():
    s = _spec(); s["schema"] = "Bad"
    with pytest.raises(mod.AssuranceError): mod.validate_assurance_spec(s)

def test_assurance_spec_hash_stable():
    s = _spec()
    assert mod.compute_assurance_spec_hash(s) == mod.compute_assurance_spec_hash(dict(s))

def test_builds_internal_control_catalog():
    c = mod.build_control_catalog(_spec(), mod.now_iso())
    ids = {x["control_id"] for x in c["controls"]}
    assert "DATA.PROV-01" in ids

def test_control_profile_includes_requested_controls():
    s = _spec(); c = mod.build_control_catalog(s, mod.now_iso())
    p = mod.build_control_profile(s, c, mod.now_iso())
    assert p["included_controls"] == sorted(s["control_profile"]["include_controls"])

def test_evidence_map_hash_stable():
    s = _spec(); c = mod.build_control_catalog(s, mod.now_iso())
    inputs = {"evidence_corpus":{"path":"x","json":{"schema":"EvidenceCorpus.v1"},"sha256":"a"}}
    e = mod.map_evidence_to_controls(s, c, inputs, mod.now_iso())
    assert mod.compute_evidence_map_hash(e) == mod.compute_evidence_map_hash(e)

def test_assurance_pack_receipt_written_success(tmp_path):
    out = tmp_path / "packs"
    cp = subprocess.run([sys.executable, "soilgrids_assurance_pack.py", "--assurance-spec", "assurance/assurance_spec_example.json", "--output-root", str(out), "--mode", "catalog-only", "--overwrite", "--allow-absolute-output"], capture_output=True, text=True)
    assert cp.returncode in (0,10,20)
    p = Path(cp.stdout.strip())
    assert p.exists()

