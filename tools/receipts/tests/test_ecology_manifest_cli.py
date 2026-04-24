```python
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "tools.receipts.ecology_manifest", *args],
        check=False,
        text=True,
        capture_output=True,
    )


def validator_receipt(
    *,
    decision: str = "pass",
    spec_hash: str = SPEC_HASH,
) -> dict:
    return {
        "receipt_type": "validator_result",
        "validator": "tools/validators/ecology_index",
        "schema_ref": "schemas/ecology/kfm_eco_index.schema.json",
        "input_ref": "candidate.json",
        "decision": decision,
        "errors": [],
        "warnings": [],
        "spec_hash": spec_hash,
        "generated_at": "2026-04-24T00:00:00Z",
    }


def test_cli_writes_ready_manifest(tmp_path: Path) -> None:
    receipt_path = tmp_path / "receipt.json"
    out_path = tmp_path / "manifest.json"
    write_json(receipt_path, validator_receipt())

    result = run_cli(
        "--candidate-id",
        "eco_index.example",
        "--candidate-type",
        "eco_index",
        "--spec-hash",
        SPEC_HASH,
        "--receipt",
        str(receipt_path),
        "--out",
        str(out_path),
    )

    assert result.returncode == 0
    assert "manifest:" in result.stdout
    assert "decision: ready_for_promotion" in result.stdout
    assert result.stderr == ""
    assert out_path.exists()

    manifest = json.loads(out_path.read_text(encoding="utf-8"))
    assert manifest["decision"] == "ready_for_promotion"


def test_cli_writes_not_ready_manifest_for_failed_receipt(tmp_path: Path) -> None:
    receipt_path = tmp_path / "receipt.json"
    out_path = tmp_path / "manifest.json"
    write_json(receipt_path, validator_receipt(decision="fail"))

    result = run_cli(
        "--candidate-id",
        "eco_index.example",
        "--candidate-type",
        "eco_index",
        "--spec-hash",
        SPEC_HASH,
        "--receipt",
        str(receipt_path),
        "--out",
        str(out_path),
    )

    assert result.returncode == 0
    assert "decision: not_ready" in result.stdout

    manifest = json.loads(out_path.read_text(encoding="utf-8"))
    assert manifest["decision"] == "not_ready"


def test_cli_missing_receipt_exits_two(tmp_path: Path) -> None:
    out_path = tmp_path / "manifest.json"

    result = run_cli(
        "--candidate-id",
        "eco_index.example",
        "--candidate-type",
        "eco_index",
        "--spec-hash",
        SPEC_HASH,
        "--receipt",
        str(tmp_path / "missing.json"),
        "--out",
        str(out_path),
    )

    assert result.returncode == 2
    assert "missing receipt:" in result.stderr
    assert not out_path.exists()


def test_cli_malformed_receipt_json_exits_one(tmp_path: Path) -> None:
    receipt_path = tmp_path / "bad_receipt.json"
    out_path = tmp_path / "manifest.json"
    receipt_path.write_text("{ not json", encoding="utf-8")

    result = run_cli(
        "--candidate-id",
        "eco_index.example",
        "--candidate-type",
        "eco_index",
        "--spec-hash",
        SPEC_HASH,
        "--receipt",
        str(receipt_path),
        "--out",
        str(out_path),
    )

    assert result.returncode == 1
    assert "invalid receipt json:" in result.stderr
    assert not out_path.exists()


def test_cli_non_object_receipt_exits_one(tmp_path: Path) -> None:
    receipt_path = tmp_path / "array_receipt.json"
    out_path = tmp_path / "manifest.json"
    write_json(receipt_path, [])

    result = run_cli(
        "--candidate-id",
        "eco_index.example",
        "--candidate-type",
        "eco_index",
        "--spec-hash",
        SPEC_HASH,
        "--receipt",
        str(receipt_path),
        "--out",
        str(out_path),
    )

    assert result.returncode == 1
    assert "invalid receipt:" in result.stderr
    assert "Receipt must be a JSON object" in result.stderr
    assert not out_path.exists()
```
