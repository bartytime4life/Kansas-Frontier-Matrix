import json
import subprocess
import sys
from pathlib import Path

from tools.validators.flora.usda_plants_dataset_validator import validate_dataset


def _run_loader(out_dir: Path) -> None:
    subprocess.run(
        [
            sys.executable,
            "tools/ingest/flora/usda_plants_fixture_loader.py",
            "--checklist",
            "tests/fixtures/flora/usda_plants/raw/checklist.csv",
            "--states",
            "tests/fixtures/flora/usda_plants/raw/state_distribution.csv",
            "--counties",
            "tests/fixtures/flora/usda_plants/raw/county_distribution.csv",
            "--snapshot-date",
            "2026-04-30",
            "--out-dir",
            str(out_dir),
        ],
        check=True,
    )


def test_loader_emits_and_validates(tmp_path: Path) -> None:
    out_dir = tmp_path / "out"
    _run_loader(out_dir)

    processed_dir = out_dir / "processed/flora/usda_plants"
    datasets = sorted(processed_dir.glob("*.json"))
    assert len(datasets) == 2
    assert (out_dir / "receipts/flora/usda_plants/ingest_receipt.json").exists()
    assert (out_dir / "receipts/flora/usda_plants/validation_receipt.json").exists()

    for dataset_path in datasets:
        payload = json.loads(dataset_path.read_text(encoding="utf-8"))
        result = validate_dataset(payload)
        assert result["result"] == "pass"


def test_loader_is_deterministic(tmp_path: Path) -> None:
    out_a = tmp_path / "a"
    out_b = tmp_path / "b"
    _run_loader(out_a)
    _run_loader(out_b)

    rels = [
        "processed/flora/usda_plants/ACMI2.json",
        "processed/flora/usda_plants/SORGH2.json",
        "receipts/flora/usda_plants/ingest_receipt.json",
        "receipts/flora/usda_plants/validation_receipt.json",
    ]
    for rel in rels:
        left = json.loads((out_a / rel).read_text(encoding="utf-8"))
        right = json.loads((out_b / rel).read_text(encoding="utf-8"))
        left.pop("generated_at", None)
        right.pop("generated_at", None)
        assert left == right
