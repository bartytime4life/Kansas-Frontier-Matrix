from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

VAL = "tools/validators/fauna/gbif_public_aggregate_validator.py"
FIX = Path("tests/fixtures/fauna/gbif")

def run(args):
    return subprocess.run([sys.executable, VAL, *args], text=True, capture_output=True)

def test_exact_coordinate_leak_fails(tmp_path: Path):
    p = tmp_path / "a.json"
    p.write_text("[" + (FIX / "invalid/evidencebundle_exact_public_coords.json").read_text() + "]")
    r = run(["--aggregate", str(p)])
    assert r.returncode != 0

def test_missing_geoprivacy_receipt_fails(tmp_path: Path):
    agg = json.loads((FIX / "invalid/evidencebundle_exact_public_coords.json").read_text())
    agg.pop("decimalLatitude", None); agg.pop("decimalLongitude", None); agg["geoprivacy_receipt_ref"] = ""
    p = tmp_path / "a.json"; p.write_text(json.dumps([agg]))
    assert run(["--aggregate", str(p)]).returncode != 0

def test_restricted_rights_and_sensitivity_fail(tmp_path: Path):
    agg = json.loads((FIX / "invalid/evidencebundle_exact_public_coords.json").read_text())
    agg.pop("decimalLatitude", None); agg.pop("decimalLongitude", None)
    agg["rights_posture"] = "restricted"; p = tmp_path / "r.json"; p.write_text(json.dumps([agg])); assert run(["--aggregate", str(p)]).returncode != 0
    agg["rights_posture"] = "public_allowed"; agg["sensitivity_posture"] = "restricted"; p2 = tmp_path / "s.json"; p2.write_text(json.dumps([agg])); assert run(["--aggregate", str(p2)]).returncode != 0

def test_reject_missing_source_or_download_key(tmp_path: Path):
    agg = json.loads((FIX / "invalid/evidencebundle_exact_public_coords.json").read_text())
    agg.pop("decimalLatitude", None); agg.pop("decimalLongitude", None); agg["source_evidence_bundle_id"] = ""; agg["download_key"] = ""
    p = tmp_path / "m.json"; p.write_text(json.dumps([agg]))
    assert run(["--aggregate", str(p)]).returncode != 0
