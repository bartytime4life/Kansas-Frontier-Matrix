from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
SCHEMA_REF = "schemas/ecology/ecology_receipt_manifest.schema.json"


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "tools.receipts.validate_receipt_manifest", *args],
        check=False,
        text=True,
        capture_output=True,
    )


def valid_manifest() -> dict:
    return {
        "manifest_id": "kfm.receipt_manifest.ecology.eco_index.example",
        "candidate_id": "eco_index.example",
        "candidate_type": "eco_index",
        "spec_hash": SPEC_HASH,
        "receipts": [
            {
                "receipt_type": "validator_result",
                "validator": "tools/validators/ecology_index",
                "receipt_ref": "receipt.json",
                "decision": "pass",
                "spec_hash": SPEC_HASH,
                "generated_at": "2026-04-24T00:00:00Z",
            }
        ],
        "decision": "ready_for_promotion",
        "generated_at": "2026-04-24T00:00:00Z",
    }


def test_cli_valid_manifest(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, valid_manifest())

    result = run_cli("--manifest", str(manifest_path), "--schema", SCHEMA_REF)

    assert result.returncode == 0
    assert "manifest schema valid" in result.stdout
    assert result.stderr == ""


def test_cli_invalid_manifest(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    bad = valid_manifest()
    bad["receipts"] = []
    write_json(manifest_path, bad)

    result = run_cli("--manifest", str(manifest_path), "--schema", SCHEMA_REF)

    assert result.returncode == 1
    assert "manifest schema invalid:" in result.stderr


def test_cli_missing_manifest(tmp_path: Path) -> None:
    result = run_cli("--manifest", str(tmp_path / "missing.json"), "--schema", SCHEMA_REF)

    assert result.returncode == 2
    assert "missing manifest:" in result.stderr


def test_cli_missing_schema(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, valid_manifest())

    result = run_cli(
        "--manifest",
        str(manifest_path),
        "--schema",
        str(tmp_path / "missing_schema.json"),
    )

    assert result.returncode == 3
    assert "missing schema:" in result.stderr
