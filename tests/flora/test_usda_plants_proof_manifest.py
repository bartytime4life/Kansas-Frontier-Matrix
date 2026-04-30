import json
import subprocess
import sys
from pathlib import Path


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


def _run_manifest(processed: Path, out_path: Path) -> dict:
    subprocess.run(
        [
            sys.executable,
            "tools/proofs/flora/usda_plants_proof_manifest.py",
            "--processed-dir",
            str(processed),
            "--out",
            str(out_path),
        ],
        check=True,
    )
    return json.loads(out_path.read_text(encoding="utf-8"))


def test_manifest_generation_and_determinism(tmp_path: Path) -> None:
    out_a = tmp_path / "a"
    out_b = tmp_path / "b"
    _run_loader(out_a)
    _run_loader(out_b)

    manifest_a = _run_manifest(out_a / "processed/flora/usda_plants", out_a / "proofs/flora/usda_plants/spec_hash_manifest.json")
    manifest_b = _run_manifest(out_b / "processed/flora/usda_plants", out_b / "proofs/flora/usda_plants/spec_hash_manifest.json")

    assert manifest_a["dataset_count"] == 2
    assert manifest_a["manifest_hash"].startswith("sha256:")
    assert all(item["spec_hash"].startswith("sha256:") for item in manifest_a["datasets"])

    manifest_a.pop("generated_at", None)
    manifest_b.pop("generated_at", None)
    for item in manifest_a["datasets"]:
        item["path"] = Path(item["path"]).name
    for item in manifest_b["datasets"]:
        item["path"] = Path(item["path"]).name
    assert manifest_a == manifest_b
