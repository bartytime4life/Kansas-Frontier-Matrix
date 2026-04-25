```python
from __future__ import annotations

import json
from pathlib import Path

from apps.governed_api.ecology.evidencebundle_resolver import (
    ERROR_CODES,
    ResolverConfig,
    resolve_ecology_evidence_bundle,
)


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": True,
        "required": [
            "proof_pack_id",
            "candidate_id",
            "candidate_type",
            "spec_hash",
            "manifest_ref",
            "receipts",
            "catalog_refs",
            "generated_at",
            "status",
        ],
        "properties": {
            "proof_pack_id": {"type": "string"},
            "candidate_id": {"type": "string"},
            "candidate_type": {"type": "string"},
            "spec_hash": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
            "manifest_ref": {"type": "string"},
            "receipts": {"type": "array", "minItems": 1},
            "catalog_refs": {
                "type": "object",
                "required": ["prov"],
                "properties": {
                    "prov": {"type": "array", "minItems": 1}
                },
            },
            "generated_at": {"type": "string"},
            "status": {"const": "proof_complete"},
        },
    }


def proof_pack(
    *,
    candidate_id: str = "eco_index.example",
    spec_hash: str = SPEC_HASH,
    status: str = "proof_complete",
    include_prov: bool = True,
) -> dict:
    return {
        "proof_pack_id": f"kfm.proof.ecology.{candidate_id}",
        "candidate_id": candidate_id,
        "candidate_type": "eco_index",
        "spec_hash": spec_hash,
        "manifest_ref": "data/receipts/ecology/manifests/example.receipt_manifest.json",
        "receipts": [
            {
                "receipt_type": "validator_result",
                "receipt_ref": "data/receipts/ecology/index/example.validator_receipt.json",
                "decision": "pass",
                "generated_at": "2026-04-24T00:00:00Z",
            }
        ],
        "catalog_refs": {
            "dcat": ["kfm:dcat:dataset:ecology:example"],
            "stac": ["kfm:stac:item:ecology:example"],
            "prov": ["kfm:prov:entity:ecology:example"] if include_prov else [],
        },
        "generated_at": "2026-04-24T00:00:00Z",
        "status": status,
    }


def config(tmp_path: Path) -> ResolverConfig:
    proof_root = tmp_path / "proofs"
    schema_path = tmp_path / "schema.json"
    write_json(schema_path, schema())

    return ResolverConfig(
        proof_root=proof_root,
        schema_path=schema_path,
    )


def write_proof_pack(tmp_path: Path, candidate_id: str, value: object) -> Path:
    path = tmp_path / "proofs" / f"{candidate_id}.proof_pack.json"
    write_json(path, value)
    return path


def test_resolver_returns_cite_for_valid_proof_pack(tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    resolver_config = config(tmp_path)
    proof_path = write_proof_pack(tmp_path, candidate_id, proof_pack(candidate_id=candidate_id))

    result = resolve_ecology_evidence_bundle(
        candidate_id=candidate_id,
        config=resolver_config,
        expected_spec_hash=SPEC_HASH,
    )

    assert result["status"] == "ok"
    assert result["data"]["decision"] == "cite"
    assert result["data"]["status"] == "resolved"
    assert result["data"]["candidate_id"] == candidate_id
    assert result["data"]["spec_hash"] == SPEC_HASH
    assert result["data"]["proof_pack_ref"] == str(proof_path)
    assert result["data"]["evidence"]["catalog_refs"]["prov"] == [
        "kfm:prov:entity:ecology:example"
    ]
    assert result["meta"]["evidence_drawer_required"] is True


def test_resolver_abstains_when_proof_pack_missing(tmp_path: Path) -> None:
    result = resolve_ecology_evidence_bundle(
        candidate_id="eco_index.example",
        config=config(tmp_path),
    )

    assert result["data"]["decision"] == "abstain"
    assert result["data"]["reason"] == "proof_pack_missing"
    assert result["data"]["error_code"] == ERROR_CODES["proof_pack_missing"]


def test_resolver_abstains_on_malformed_json(tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    resolver_config = config(tmp_path)

    path = tmp_path / "proofs" / f"{candidate_id}.proof_pack.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("{ not json", encoding="utf-8")

    result = resolve_ecology_evidence_bundle(
        candidate_id=candidate_id,
        config=resolver_config,
    )

    assert result["data"]["decision"] == "abstain"
    assert result["data"]["reason"] == "proof_pack_invalid"
    assert result["data"]["error_code"] == ERROR_CODES["proof_pack_invalid"]


def test_resolver_abstains_on_non_object_json(tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    resolver_config = config(tmp_path)
    write_proof_pack(tmp_path, candidate_id, [])

    result = resolve_ecology_evidence_bundle(
        candidate_id=candidate_id,
        config=resolver_config,
    )

    assert result["data"]["decision"] == "abstain"
    assert result["data"]["reason"] == "proof_pack_invalid"


def test_resolver_abstains_on_schema_failure(tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    resolver_config = config(tmp_path)

    value = proof_pack(candidate_id=candidate_id)
    value["spec_hash"] = "not-a-sha256"
    write_proof_pack(tmp_path, candidate_id, value)

    result = resolve_ecology_evidence_bundle(
        candidate_id=candidate_id,
        config=resolver_config,
    )

    assert result["data"]["decision"] == "abstain"
    assert result["data"]["reason"] == "proof_pack_invalid"


def test_resolver_abstains_on_spec_hash_mismatch(tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    resolver_config = config(tmp_path)
    write_proof_pack(tmp_path, candidate_id, proof_pack(candidate_id=candidate_id))

    result = resolve_ecology_evidence_bundle(
        candidate_id=candidate_id,
        config=resolver_config,
        expected_spec_hash="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    )

    assert result["data"]["decision"] == "abstain"
    assert result["data"]["reason"] == "spec_hash_mismatch"
    assert result["data"]["error_code"] == ERROR_CODES["spec_hash_mismatch"]


def test_resolver_abstains_when_prov_missing(tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    resolver_config = config(tmp_path)
    write_proof_pack(
        tmp_path,
        candidate_id,
        proof_pack(candidate_id=candidate_id, include_prov=False),
    )

    result = resolve_ecology_evidence_bundle(
        candidate_id=candidate_id,
        config=resolver_config,
    )

    assert result["data"]["decision"] == "abstain"
    assert result["data"]["reason"] == "proof_pack_invalid"


def test_resolver_abstains_when_status_not_complete(tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    resolver_config = config(tmp_path)
    write_proof_pack(
        tmp_path,
        candidate_id,
        proof_pack(candidate_id=candidate_id, status="draft"),
    )

    result = resolve_ecology_evidence_bundle(
        candidate_id=candidate_id,
        config=resolver_config,
    )

    assert result["data"]["decision"] == "abstain"
    assert result["data"]["reason"] == "proof_pack_invalid"
```
