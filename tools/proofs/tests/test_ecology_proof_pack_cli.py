```python
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
        [sys.executable, "-m", "tools.proofs.ecology_proof_pack", *args],
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


def cli_args(
    *,
    manifest_path: Path,
    catalog_refs_path: Path,
    out_path: Path,
    schema_ref: str = SCHEMA_REF,
) -> list[str]:
    return [
        "--manifest",
        str(manifest_path),
        "--catalog-refs",
        str(catalog_refs_path),
        "--schema",
        schema_ref,
        "--out",
        str(out_path),
    ]


def test_cli_writes_proof_pack(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    catalog_refs_path = tmp_path / "catalog_refs.json"
    out_path = tmp_path / "proof_pack.json"

    write_json(manifest_path, manifest())
    write_json(catalog_refs_path, catalog_refs())

    result = run_cli(
        *cli_args(
            manifest_path=manifest_path,
            catalog_refs_path=catalog_refs_path,
            out_path=out_path,
        )
    )

    assert result.returncode == 0
    assert "proof pack:" in result.stdout
    assert "status: proof_complete" in result.stdout
    assert result.stderr == ""
    assert out_path.exists()

    proof_pack = json.loads(out_path.read_text(encoding="utf-8"))
    assert proof_pack["proof_pack_id"] == "kfm.proof.ecology.eco_index.example"
    assert proof_pack["status"] == "proof_complete"
    assert proof_pack["catalog_refs"]["prov"] == ["kfm:prov:entity:ecology:example"]


def test_cli_missing_manifest_exits_two(tmp_path: Path) -> None:
    catalog_refs_path = tmp_path / "catalog_refs.json"
    out_path = tmp_path / "proof_pack.json"
    write_json(catalog_refs_path, catalog_refs())

    result = run_cli(
        *cli_args(
            manifest_path=tmp_path / "missing_manifest.json",
            catalog_refs_path=catalog_refs_path,
            out_path=out_path,
        )
    )

    assert result.returncode == 2
    assert "missing manifest:" in result.stderr
    assert not out_path.exists()


def test_cli_missing_catalog_refs_exits_two(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    out_path = tmp_path / "proof_pack.json"
    write_json(manifest_path, manifest())

    result = run_cli(
        *cli_args(
            manifest_path=manifest_path,
            catalog_refs_path=tmp_path / "missing_catalog_refs.json",
            out_path=out_path,
        )
    )

    assert result.returncode == 2
    assert "missing catalog refs:" in result.stderr
    assert not out_path.exists()


def test_cli_missing_schema_exits_three(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    catalog_refs_path = tmp_path / "catalog_refs.json"
    out_path = tmp_path / "proof_pack.json"

    write_json(manifest_path, manifest())
    write_json(catalog_refs_path, catalog_refs())

    result = run_cli(
        *cli_args(
            manifest_path=manifest_path,
            catalog_refs_path=catalog_refs_path,
            out_path=out_path,
            schema_ref=str(tmp_path / "missing_schema.json"),
        )
    )

    assert result.returncode == 3
    assert "missing schema:" in result.stderr
    assert not out_path.exists()


def test_cli_invalid_schema_exits_three(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    catalog_refs_path = tmp_path / "catalog_refs.json"
    schema_path = tmp_path / "invalid_schema.json"
    out_path = tmp_path / "proof_pack.json"

    write_json(manifest_path, manifest())
    write_json(catalog_refs_path, catalog_refs())
    write_json(
        schema_path,
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": 123,
        },
    )

    result = run_cli(
        *cli_args(
            manifest_path=manifest_path,
            catalog_refs_path=catalog_refs_path,
            out_path=out_path,
            schema_ref=str(schema_path),
        )
    )

    assert result.returncode == 3
    assert "invalid proof-pack schema:" in result.stderr
    assert not out_path.exists()


def test_cli_malformed_manifest_json_exits_one(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    catalog_refs_path = tmp_path / "catalog_refs.json"
    out_path = tmp_path / "proof_pack.json"

    manifest_path.write_text("{ not json", encoding="utf-8")
    write_json(catalog_refs_path, catalog_refs())

    result = run_cli(
        *cli_args(
            manifest_path=manifest_path,
            catalog_refs_path=catalog_refs_path,
            out_path=out_path,
        )
    )

    assert result.returncode == 1
    assert "invalid json:" in result.stderr
    assert not out_path.exists()


def test_cli_non_promotable_manifest_exits_one(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    catalog_refs_path = tmp_path / "catalog_refs.json"
    out_path = tmp_path / "proof_pack.json"

    write_json(manifest_path, manifest(decision="not_ready"))
    write_json(catalog_refs_path, catalog_refs())

    result = run_cli(
        *cli_args(
            manifest_path=manifest_path,
            catalog_refs_path=catalog_refs_path,
            out_path=out_path,
        )
    )

    assert result.returncode == 1
    assert "invalid proof-pack input:" in result.stderr
    assert "manifest not promotable: not_ready" in result.stderr
    assert not out_path.exists()


def test_cli_missing_prov_catalog_ref_exits_one(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    catalog_refs_path = tmp_path / "catalog_refs.json"
    out_path = tmp_path / "proof_pack.json"

    write_json(manifest_path, manifest())
    write_json(catalog_refs_path, catalog_refs(include_prov=False))

    result = run_cli(
        *cli_args(
            manifest_path=manifest_path,
            catalog_refs_path=catalog_refs_path,
            out_path=out_path,
        )
    )

    assert result.returncode == 1
    assert "proof pack requires at least one PROV catalog reference" in result.stderr
    assert not out_path.exists()
```
