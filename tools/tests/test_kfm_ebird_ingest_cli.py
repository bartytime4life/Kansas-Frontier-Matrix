from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = "tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_ingest.py"
LAYER_REGISTRY = Path("data/published/fauna/layers/ebird_agg_huc12.json")
VALIDATOR = "tools/validators/fauna/validate_evidencebundle.py"
FILTER = "complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10"
FIXTURE = Path("tools/tests/fixtures/ebird/sample_ebd.tsv")


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, SCRIPT, *args], check=False, text=True, capture_output=True)


def test_help_exits_successfully() -> None:
    assert run_cli("--help").returncode == 0


def test_non_dry_run_emits_outputs_and_manifest(tmp_path: Path) -> None:
    out = tmp_path / "obs.jsonl"; quarantine = tmp_path / "q.jsonl"; manifest = tmp_path / "m.json"; eb = tmp_path / "eb.json"
    r = run_cli("--ebd-file", str(FIXTURE), "--filter", FILTER, "--aggregate", "huc12", "--emit", str(eb), "--out", str(out), "--quarantine", str(quarantine), "--manifest", str(manifest))
    assert r.returncode == 0, r.stderr
    obs = [json.loads(x) for x in out.read_text().splitlines()]
    qu = [json.loads(x) for x in quarantine.read_text().splitlines()]
    man = json.loads(manifest.read_text())
    assert len(obs) == 2 and len(qu) == 6
    assert obs[1]["individualCount"] is None and obs[1]["observation_count_raw"] == "X"
    assert "reason_codes" in qu[0]
    assert man["counts"]["rows_seen"] == 8
    assert man["counts"]["rows_accepted"] == 2
    assert man["counts"]["rows_quarantined"] == 6
    for key in ("input_sha256", "output_sha256", "quarantine_sha256", "evidencebundle_sha256"):
        assert man[key].startswith("sha256:")


def test_missing_required_column_strict_fails(tmp_path: Path) -> None:
    miss = Path("tools/tests/fixtures/ebird/missing_column.tsv")
    r = run_cli("--ebd-file", str(miss), "--filter", FILTER, "--aggregate", "huc12", "--emit", str(tmp_path / "e.json"), "--out", str(tmp_path / "o.jsonl"), "--quarantine", str(tmp_path / "q.jsonl"), "--manifest", str(tmp_path / "m.json"))
    assert r.returncode != 0
    assert "Missing required columns" in r.stderr


def test_out_under_data_published_fails(tmp_path: Path) -> None:
    r = run_cli("--ebd-file", str(FIXTURE), "--filter", FILTER, "--aggregate", "huc12", "--emit", str(tmp_path / "e.json"), "--out", "data/published/fauna/o.jsonl", "--quarantine", str(tmp_path / "q.jsonl"), "--manifest", str(tmp_path / "m.json"))
    assert r.returncode != 0


def test_evidence_bundle_validates(tmp_path: Path) -> None:
    eb = tmp_path / "eb.json"
    r = run_cli("--ebd-file", str(FIXTURE), "--filter", FILTER, "--aggregate", "huc12", "--emit", str(eb), "--dry-run")
    assert r.returncode == 0
    v = subprocess.run([sys.executable, VALIDATOR, str(eb)], check=False, text=True, capture_output=True)
    assert v.returncode == 0


def test_layer_registry_safety() -> None:
    layer = json.loads(LAYER_REGISTRY.read_text())
    assert int(layer["suppression_min_n"]) >= 10
