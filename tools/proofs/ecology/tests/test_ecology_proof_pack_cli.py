from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
SCHEMA_REF = "schemas/ecology/ecology_proof_pack.schema.json"


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "tools.proofs.ecology.ecology_proof_pack", *args],
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


def catalog_refs(*, include_prov: bool = True) -> dict:
    return {
        "dcat": ["kfm:dcat:dataset:ecology:example"],
        "stac": ["kfm:stac:item:ecology:example"],
        "prov": ["kfm:prov:entity:ecology:example"] if include_prov else [],
    }


def test_cli_writes_proof_pack(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    catalog_refs_path = tmp_path / "catalog_refs.json"
    out_path = tmp_path / "proof_pack.json"

    write_json(manifest_path, manifest())
    write_json(catalog_refs_path, catalog_refs())

    result = run_cli(
        "--manifest",
        str(manifest_path),
        "--catalog-refs",
        str(catalog_refs_path),
        "--schema",
        SCHEMA_REF,
        "--out",
        str(out_path),
    )

    assert result.returncode == 0
    assert "proof pack:" in result.stdout
    assert out_path.exists()


def test_cli_missing_prov_catalog_ref_exits_one(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    catalog_refs_path = tmp_path / "catalog_refs.json"
    out_path = tmp_path / "proof_pack.json"

    write_json(manifest_path, manifest())
    write_json(catalog_refs_path, catalog_refs(include_prov=False))

    result = run_cli(
        "--manifest",
        str(manifest_path),
        "--catalog-refs",
        str(catalog_refs_path),
        "--schema",
        SCHEMA_REF,
        "--out",
        str(out_path),
    )

    assert result.returncode == 1
    assert "proof pack requires at least one PROV catalog reference" in result.stderr
