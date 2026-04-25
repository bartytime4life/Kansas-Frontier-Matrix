from __future__ import annotations

import json
from pathlib import Path

import pytest

pytest.importorskip("jsonschema")
from jsonschema import Draft202012Validator

from apps.ui.ecology.evidence_drawer_mapper import map_evidence_bundle_to_drawer


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
SCHEMA_PATH = Path("schemas/contracts/v1/runtime/ecology_evidence_drawer.schema.json")


def validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def cite_response() -> dict:
    return {
        "status": "ok",
        "data": {
            "evidence_bundle_id": "kfm.evidence.ecology.eco_index.example",
            "candidate_id": "eco_index.example",
            "spec_hash": SPEC_HASH,
            "decision": "cite",
            "status": "resolved",
            "proof_pack_ref": "data/proofs/ecology/eco_index.example.proof_pack.json",
            "evidence": {
                "receipts": [
                    {
                        "receipt_ref": "data/receipts/ecology/index/example.validator_receipt.json",
                        "decision": "pass",
                    }
                ],
                "catalog_refs": {
                    "prov": ["kfm:prov:entity:ecology:example"],
                },
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


def abstain_response() -> dict:
    return {
        "status": "ok",
        "data": {
            "evidence_bundle_id": "kfm.evidence.ecology.eco_index.missing",
            "candidate_id": "eco_index.missing",
            "decision": "abstain",
            "status": "unresolved",
            "reason": "proof_pack_missing",
            "error_code": "ECO_EB_PROOF_PACK_MISSING",
            "claim_text": "KFM abstained because the ecological proof pack could not be resolved.",
        },
    }


def test_drawer_cite_payload_matches_contract_schema() -> None:
    drawer = map_evidence_bundle_to_drawer(cite_response())
    errors = sorted(validator().iter_errors(drawer), key=lambda err: list(err.path))
    assert errors == []


def test_drawer_abstain_payload_matches_contract_schema() -> None:
    drawer = map_evidence_bundle_to_drawer(abstain_response())
    errors = sorted(validator().iter_errors(drawer), key=lambda err: list(err.path))
    assert errors == []


def test_drawer_contract_negative_missing_actions_is_rejected() -> None:
    drawer = map_evidence_bundle_to_drawer(cite_response())
    del drawer["actions"]
    errors = sorted(validator().iter_errors(drawer), key=lambda err: list(err.path))

    assert errors
    assert any("'actions' is a required property" in err.message for err in errors)
