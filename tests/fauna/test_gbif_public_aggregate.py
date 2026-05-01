from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

PUB = "tools/publishers/fauna/kfm_gbif_public_aggregate.py"
VAL = "tools/validators/fauna/gbif_public_aggregate_validator.py"
FIX = Path("tests/fixtures/fauna/gbif")

def run(cmd):
    return subprocess.run([sys.executable, *cmd], text=True, capture_output=True)

def test_valid_emits_aggregate_and_receipt(tmp_path: Path):
    out = tmp_path / "aggs.json"; rec = tmp_path / "rec.json"
    r = run([PUB, "--input", str(FIX / "valid/evidencebundle.json"), "--aggregation-unit", "county", "--suppression-threshold", "10", "--output", str(out), "--receipt-output", str(rec)])
    assert r.returncode == 0, r.stderr
    assert len(json.loads(out.read_text())) == 1
    assert json.loads(rec.read_text())["receipt_id"]

def test_n_lt_10_suppressed(tmp_path: Path):
    out = tmp_path / "aggs.json"; rec = tmp_path / "rec.json"
    r = run([PUB, "--input", str(FIX / "invalid/evidencebundle_sparse.json"), "--aggregation-unit", "county", "--suppression-threshold", "10", "--output", str(out), "--receipt-output", str(rec)])
    assert r.returncode == 0
    assert json.loads(out.read_text()) == []

def test_spec_hash_stable_when_created_at_changes(tmp_path: Path):
    from tools.publishers.fauna.kfm_gbif_public_aggregate import compute_spec_hash
    d = json.loads((FIX / "valid/evidencebundle.json").read_text())
    h1 = compute_spec_hash(d)
    d["created_at"] = "2099-01-01T00:00:00Z"
    assert h1 == compute_spec_hash(d)
