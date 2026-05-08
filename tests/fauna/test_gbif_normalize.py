from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

SCRIPT = "tools/normalize/fauna/kfm_gbif_normalize.py"
FIX = Path("tests/fixtures/fauna/gbif")

def run_cli(*args: str):
    return subprocess.run([sys.executable, SCRIPT, *args], text=True, capture_output=True)

def test_valid_fixture_normalizes_successfully(tmp_path: Path) -> None:
    out = tmp_path / "eb.json"
    r = run_cli("--input", str(FIX / "valid/simple_occurrences.csv"), "--query-predicate", str(FIX / "query_predicate.json"), "--download-key", "TEST", "--output", str(out))
    assert r.returncode == 0, r.stderr
    doc = json.loads(out.read_text())
    assert doc["source_system"] == "GBIF"
    assert doc["records_count"] == 10

def test_missing_dataset_key_fails(tmp_path: Path) -> None:
    r = run_cli("--input", str(FIX / "invalid/missing_dataset_key.csv"), "--query-predicate", str(FIX / "query_predicate.json"), "--download-key", "TEST", "--output", str(tmp_path / "x.json"))
    assert r.returncode != 0

def test_unknown_license_fails_closed(tmp_path: Path) -> None:
    bad = tmp_path / "bad.csv"
    bad.write_text("gbifID,datasetKey,scientificName,eventDate,decimalLatitude,decimalLongitude,basisOfRecord,coordinateUncertaintyInMeters,license\n1,ds,x,2025-01-01,1,1,HUMAN_OBSERVATION,5,Proprietary\n")
    r = run_cli("--input", str(bad), "--query-predicate", str(FIX / "query_predicate.json"), "--download-key", "TEST", "--output", str(tmp_path / "x.json"))
    assert r.returncode != 0

def test_spec_hash_stable_when_created_at_changes(tmp_path: Path) -> None:
    out = tmp_path / "eb.json"
    r = run_cli("--input", str(FIX / "valid/simple_occurrences.csv"), "--query-predicate", str(FIX / "query_predicate.json"), "--download-key", "TEST", "--output", str(out))
    assert r.returncode == 0
    doc = json.loads(out.read_text())
    from tools.normalize.fauna.kfm_gbif_normalize import compute_spec_hash
    h1 = compute_spec_hash(doc)
    doc["created_at"] = "2099-01-01T00:00:00Z"
    h2 = compute_spec_hash(doc)
    assert h1 == h2

def test_public_exact_sensitive_coordinate_denied(tmp_path: Path) -> None:
    r = run_cli("--input", str(FIX / "invalid/public_exact_sensitive_coordinate.csv"), "--query-predicate", str(FIX / "query_predicate.json"), "--download-key", "TEST", "--publication-target", "public", "--output", str(tmp_path / "x.json"))
    assert r.returncode != 0

def test_public_aggregate_below_threshold_denied(tmp_path: Path) -> None:
    small = tmp_path / "small.csv"
    small.write_text((FIX / "valid/simple_occurrences.csv").read_text().splitlines()[0] + "\n" + "\n".join((FIX / "valid/simple_occurrences.csv").read_text().splitlines()[1:5]))
    r = run_cli("--input", str(small), "--query-predicate", str(FIX / "query_predicate.json"), "--download-key", "TEST", "--publication-target", "public", "--output", str(tmp_path / "x.json"))
    assert r.returncode != 0
