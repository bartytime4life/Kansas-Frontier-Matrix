from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


SCRIPT = "tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_ingest.py"
LAYER_REGISTRY = Path("data/published/fauna/layers/ebird_agg_huc12.json")
VALIDATOR = "tools/validators/fauna/validate_evidencebundle.py"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        check=False,
        text=True,
        capture_output=True,
    )


def test_help_exits_successfully() -> None:
    result = run_cli("--help")
    assert result.returncode == 0
    assert "kfm-ebird-ingest" in result.stdout


def test_invalid_suppression_fails(tmp_path: Path) -> None:
    out = tmp_path / "bundle.json"
    result = run_cli(
        "--ebd-file",
        "placeholder.txt",
        "--filter",
        "complete==TRUE",
        "--aggregate",
        "huc12",
        "--suppression",
        "9",
        "--emit",
        str(out),
        "--dry-run",
    )
    assert result.returncode != 0
    assert "--suppression must be >= 10" in result.stderr


def test_dry_run_emits_evidence_bundle(tmp_path: Path) -> None:
    out = tmp_path / "bundle.json"
    result = run_cli(
        "--ebd-file",
        "/tmp/ebd-EBD.txt",
        "--source-uri",
        "https://ebird.org/data?request_id=abc123",
        "--filter",
        "complete==TRUE",
        "--aggregate",
        "huc12",
        "--emit",
        str(out),
        "--dry-run",
    )
    assert result.returncode == 0
    bundle = json.loads(out.read_text(encoding="utf-8"))
    assert bundle["source_uri"] == "https://ebird.org/data?request_id=abc123"
    assert bundle["query_predicate"] == "complete==TRUE"
    assert isinstance(bundle["mapping"], dict)
    assert "kfm:spec_hash" in bundle
    assert bundle["kfm:spec_hash"].startswith("sha256:")


def test_layer_registry_suppression_and_coordinate_safety() -> None:
    layer = json.loads(LAYER_REGISTRY.read_text(encoding="utf-8"))
    assert int(layer["suppression_min_n"]) >= 10
    merged_fields = " ".join(layer["allowlist_fields"])
    for forbidden in ("decimalLatitude", "decimalLongitude", "latitude", "longitude"):
        assert forbidden not in merged_fields


def test_dry_run_output_validates_with_evidencebundle_validator(tmp_path: Path) -> None:
    out = tmp_path / "evidencebundle.json"
    result = run_cli(
        "--ebd-file",
        "/tmp/ebd-EBD.txt",
        "--filter",
        "complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10",
        "--aggregate",
        "huc12",
        "--emit",
        str(out),
        "--dry-run",
    )
    assert result.returncode == 0

    validate = subprocess.run(
        [sys.executable, VALIDATOR, str(out)],
        check=False,
        text=True,
        capture_output=True,
    )
    assert validate.returncode == 0
