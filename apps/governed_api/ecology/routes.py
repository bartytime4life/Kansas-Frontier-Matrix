from __future__ import annotations

from pathlib import Path

from .evidencebundle_resolver import ResolverConfig, resolve_ecology_evidence_bundle


DEFAULT_PROOF_ROOT = Path("data/proofs/ecology")
DEFAULT_SCHEMA_PATH = Path("schemas/contracts/v1/runtime/ecology_proof_pack.schema.json")


def get_ecology_evidence_bundle(
    *,
    candidate_id: str,
    spec_hash: str | None = None,
    include_receipts: bool = True,
    include_catalog_refs: bool = True,
    include_uncertainty: bool = True,
) -> dict:
    result = resolve_ecology_evidence_bundle(
        candidate_id=candidate_id,
        expected_spec_hash=spec_hash,
        config=ResolverConfig(
            proof_root=DEFAULT_PROOF_ROOT,
            schema_path=DEFAULT_SCHEMA_PATH,
        ),
    )

    data = result.get("data")
    if not isinstance(data, dict):
        return result

    if data.get("decision") != "cite":
        return result

    evidence = data.get("evidence")
    if isinstance(evidence, dict):
        if not include_receipts:
            evidence.pop("receipts", None)
        if not include_catalog_refs:
            evidence.pop("catalog_refs", None)

    if not include_uncertainty:
        data.pop("uncertainty", None)

    return result
