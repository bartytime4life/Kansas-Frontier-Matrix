from __future__ import annotations
import json, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
VAL = ROOT / "tools/validators/maps/validate_signed_release_manifest.py"

def run_fixture(rel):
    p = ROOT / rel
    out = subprocess.check_output(["python3", str(VAL), "--input", str(p)], text=True)
    return json.loads(out)

def test_valid_allows():
    assert run_fixture("tests/fixtures/maps/trust/valid/signed_manifest.valid.json")["status"] == "pass"

def test_invalid_fixtures_fail():
    for name in ["missing_bundle.json","hash_mismatch.json","unsupported_signer_identity.json","stale_trust_root.json","tampered_pmtiles_metadata.json"]:
        assert run_fixture(f"tests/fixtures/maps/trust/invalid/{name}")["status"] == "fail"
