from __future__ import annotations
import subprocess, sys
from pathlib import Path

NORMALIZER = "tools/normalizers/fauna/kfm_gbif_normalize.py"
VALIDATOR = "tools/validators/fauna/gbif_evidencebundle_validator.py"
FIX = Path("tests/fixtures/fauna/gbif")


def test_schema_validation_passes_for_valid_output(tmp_path: Path) -> None:
    out = tmp_path / "eb.json"
    r = subprocess.run([sys.executable, NORMALIZER, "--input", str(FIX / "valid/simple_occurrences.csv"), "--query-predicate", str(FIX / "query_predicate.json"), "--download-key", "TEST", "--output", str(out)], text=True, capture_output=True)
    assert r.returncode == 0, r.stderr
    v = subprocess.run([sys.executable, VALIDATOR, str(out)], text=True, capture_output=True)
    assert v.returncode == 0, v.stderr
