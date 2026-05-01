from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools/catalog/soil/build_catalog.py"
FIXTURE_ROOT = ROOT / "tests/fixtures/soil/catalog"


def run_builder(receipt: Path, out_root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--receipt", str(receipt), "--out-root", str(out_root)],
        capture_output=True,
        text=True,
        check=False,
    )


def test_pass_embedded_fixture_generates_outputs(tmp_path: Path) -> None:
    result = run_builder(FIXTURE_ROOT / "run_receipt_pass_embedded_bundle.json", tmp_path)
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["promotion_allowed"] is True

    sid = "soil.bundle.pass.001"
    expected = [
        tmp_path / "catalog/stac/soil" / f"{sid}.json",
        tmp_path / "catalog/dcat/soil" / f"{sid}.jsonld",
        tmp_path / "catalog/prov/soil" / f"{sid}.jsonld",
        tmp_path / "triplets/soil" / f"{sid}.nt",
        tmp_path / "receipts/soil" / f"{sid}.promotion_receipt.json",
    ]
    for path in expected:
        assert path.exists(), f"missing {path}"

    for catalog in expected[:4]:
        if catalog.suffix in {".json", ".jsonld"}:
            json.loads(catalog.read_text(encoding="utf-8"))

    promotion = json.loads(expected[4].read_text(encoding="utf-8"))
    generated = promotion["generated_artifacts"]
    assert set(generated.keys()) == {"stac", "dcat", "prov", "triplets"}
    for value in generated.values():
        assert "sha256" in value and len(value["sha256"]) == 64


def test_triples_deterministic_across_runs(tmp_path: Path) -> None:
    out_a = tmp_path / "a"
    out_b = tmp_path / "b"
    assert run_builder(FIXTURE_ROOT / "run_receipt_pass_embedded_bundle.json", out_a).returncode == 0
    assert run_builder(FIXTURE_ROOT / "run_receipt_pass_embedded_bundle.json", out_b).returncode == 0
    sid = "soil.bundle.pass.001"
    nt_a = (out_a / "triplets/soil" / f"{sid}.nt").read_text(encoding="utf-8")
    nt_b = (out_b / "triplets/soil" / f"{sid}.nt").read_text(encoding="utf-8")
    assert nt_a == nt_b


def test_blocked_fixtures_nonzero_and_no_outputs(tmp_path: Path) -> None:
    for name in [
        "run_receipt_block_review.json",
        "run_receipt_block_missing_signature.json",
        "run_receipt_block_unknown_rights.json",
    ]:
        out = tmp_path / name.replace(".json", "")
        result = run_builder(FIXTURE_ROOT / name, out)
        assert result.returncode != 0
        assert not (out / "catalog").exists()
        assert not (out / "triplets").exists()
