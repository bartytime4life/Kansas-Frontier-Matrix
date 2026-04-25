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
        [
            sys.executable,
            "-m",
            "tools.validators.promotion_gate.ecology_manifest_cli",
            *args,
        ],
        check=False,
        text=True,
        capture_output=True,
    )


def manifest(*, decision: str = "ready_for_promotion") -> dict:
    return {
        "manifest_id": "kfm.receipt_manifest.ecology.eco_index.example",
        "candidate_id": "eco_index.example",
        "candidate_type": "eco_index",
        "spec_hash": SPEC_HASH,
        "receipts": [
            {
                "receipt_type": "validator_result",
                "validator": "tools/validators/ecology_index",
                "receipt_ref": "data/receipts/ecology/index/example.validator_receipt.json",
                "decision": "pass",
                "spec_hash": SPEC_HASH,
                "generated_at": "2026-04-24T00:00:00Z",
            }
        ],
        "decision": decision,
        "generated_at": "2026-04-24T00:00:00Z",
    }


def test_cli_pass_manifest_exits_zero(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, manifest(decision="ready_for_promotion"))

    result = run_cli("--manifest", str(manifest_path))

    assert result.returncode == 0
    assert "decision: pass" in result.stdout
    assert result.stderr == ""


def test_cli_hold_manifest_exits_one(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, manifest(decision="hold"))

    result = run_cli("--manifest", str(manifest_path))

    assert result.returncode == 1
    assert "decision: hold" in result.stdout
    assert result.stderr == ""


def test_cli_fail_manifest_exits_one(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, manifest(decision="not_ready"))

    result = run_cli("--manifest", str(manifest_path))

    assert result.returncode == 1
    assert "decision: fail" in result.stdout
    assert result.stderr == ""


def test_cli_missing_manifest_exits_two(tmp_path: Path) -> None:
    result = run_cli("--manifest", str(tmp_path / "missing_manifest.json"))

    assert result.returncode == 2
    assert "missing manifest:" in result.stderr


def test_cli_malformed_manifest_json_exits_one(tmp_path: Path) -> None:
    manifest_path = tmp_path / "malformed_manifest.json"
    manifest_path.write_text("{ not json", encoding="utf-8")

    result = run_cli("--manifest", str(manifest_path))

    assert result.returncode == 1
    assert "invalid manifest json:" in result.stderr


def test_cli_non_object_manifest_exits_one(tmp_path: Path) -> None:
    manifest_path = tmp_path / "array_manifest.json"
    write_json(manifest_path, [])

    result = run_cli("--manifest", str(manifest_path))

    assert result.returncode == 1
    assert "invalid manifest:" in result.stderr
    assert "Receipt manifest must be a JSON object" in result.stderr


def test_cli_writes_gate_result(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    out_path = tmp_path / "nested" / "gate_result.json"

    write_json(manifest_path, manifest(decision="ready_for_promotion"))

    result = run_cli(
        "--manifest",
        str(manifest_path),
        "--out",
        str(out_path),
    )

    assert result.returncode == 0
    assert out_path.exists()

    gate_result = json.loads(out_path.read_text(encoding="utf-8"))

    assert gate_result == {
        "gate": "ecology_receipt_manifest",
        "decision": "pass",
        "manifest_ref": str(manifest_path),
        "candidate_id": "eco_index.example",
        "spec_hash": SPEC_HASH,
        "errors": [],
        "warnings": [],
    }
```
