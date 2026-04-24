```python
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ERROR_CODES = {
    "proof_pack_missing": "ECO_EB_PROOF_PACK_MISSING",
    "proof_pack_invalid": "ECO_EB_PROOF_PACK_INVALID",
    "spec_hash_mismatch": "ECO_EB_SPEC_HASH_MISMATCH",
    "catalog_refs_unresolved": "ECO_EB_CATALOG_REFS_UNRESOLVED",
    "review_required": "ECO_EB_REVIEW_REQUIRED",
    "internal_error": "ECO_EB_INTERNAL_ERROR",
}


@dataclass(frozen=True)
class ResolverConfig:
    proof_root: Path
    schema_path: Path


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(value, dict):
        raise ValueError("Resolved proof-pack document must be a JSON object.")

    return value


def proof_pack_path(config: ResolverConfig, candidate_id: str) -> Path:
    return config.proof_root / f"{candidate_id}.proof_pack.json"


def validate_proof_pack(
    *,
    proof_pack: dict[str, Any],
    schema_path: Path,
) -> list[str]:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    return [
        f"{'.'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
        for error in sorted(
            validator.iter_errors(proof_pack),
            key=lambda item: list(item.path),
        )
    ]


def has_required_catalog_refs(proof_pack: dict[str, Any]) -> bool:
    catalog_refs = proof_pack.get("catalog_refs", {})
    if not isinstance(catalog_refs, dict):
        return False

    prov_refs = catalog_refs.get("prov", [])
    return isinstance(prov_refs, list) and bool(prov_refs)


def abstain_bundle(
    *,
    candidate_id: str,
    reason: str,
    error_code: str,
) -> dict[str, Any]:
    return {
        "status": "ok",
        "data": {
            "evidence_bundle_id": f"kfm.evidence.ecology.{candidate_id}",
            "candidate_id": candidate_id,
            "decision": "abstain",
            "status": "unresolved",
            "reason": reason,
            "error_code": error_code,
            "claim_text": "KFM abstained because the ecological proof pack could not be resolved."
        },
        "meta": {
            "resolver": "ecology_evidencebundle",
            "evidence_drawer_required": True,
        },
    }


def cite_bundle(
    *,
    candidate_id: str,
    proof_pack_ref: Path,
    proof_pack: dict[str, Any],
) -> dict[str, Any]:
    return {
        "status": "ok",
        "data": {
            "evidence_bundle_id": f"kfm.evidence.ecology.{candidate_id}",
            "candidate_id": candidate_id,
            "spec_hash": proof_pack["spec_hash"],
            "decision": "cite",
            "status": "resolved",
            "proof_pack_ref": str(proof_pack_ref),
            "evidence": {
                "receipts": proof_pack.get("receipts", []),
                "catalog_refs": proof_pack.get("catalog_refs", {}),
            },
            "uncertainty": {
                "status": "declared",
                "summary": "Uncertainty inherited from proof-pack evidence where available.",
            },
        },
        "meta": {
            "resolver": "ecology_evidencebundle",
            "evidence_drawer_required": True,
        },
    }


def resolve_ecology_evidence_bundle(
    *,
    candidate_id: str,
    config: ResolverConfig,
    expected_spec_hash: str | None = None,
) -> dict[str, Any]:
    path = proof_pack_path(config, candidate_id)

    if not path.exists():
        return abstain_bundle(
            candidate_id=candidate_id,
            reason="proof_pack_missing",
            error_code=ERROR_CODES["proof_pack_missing"],
        )

    try:
        proof_pack = load_json(path)
        schema_errors = validate_proof_pack(
            proof_pack=proof_pack,
            schema_path=config.schema_path,
        )
    except Exception:
        return abstain_bundle(
            candidate_id=candidate_id,
            reason="proof_pack_invalid",
            error_code=ERROR_CODES["proof_pack_invalid"],
        )

    if schema_errors:
        return abstain_bundle(
            candidate_id=candidate_id,
            reason="proof_pack_invalid",
            error_code=ERROR_CODES["proof_pack_invalid"],
        )

    if expected_spec_hash and proof_pack.get("spec_hash") != expected_spec_hash:
        return abstain_bundle(
            candidate_id=candidate_id,
            reason="spec_hash_mismatch",
            error_code=ERROR_CODES["spec_hash_mismatch"],
        )

    if proof_pack.get("status") != "proof_complete":
        return abstain_bundle(
            candidate_id=candidate_id,
            reason="proof_pack_invalid",
            error_code=ERROR_CODES["proof_pack_invalid"],
        )

    if not has_required_catalog_refs(proof_pack):
        return abstain_bundle(
            candidate_id=candidate_id,
            reason="catalog_refs_unresolved",
            error_code=ERROR_CODES["catalog_refs_unresolved"],
        )

    return cite_bundle(
        candidate_id=candidate_id,
        proof_pack_ref=path,
        proof_pack=proof_pack,
    )
```
