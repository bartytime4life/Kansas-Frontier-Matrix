from __future__ import annotations

from apps.ui.ecology.evidence_drawer_mapper import map_evidence_bundle_to_drawer


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


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
                    "dcat": ["kfm:dcat:dataset:ecology:example"],
                    "stac": ["kfm:stac:item:ecology:example"],
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
        "meta": {
            "resolver": "ecology_evidencebundle",
            "evidence_drawer_required": True,
        },
    }


def test_maps_cite_response_to_drawer_payload() -> None:
    drawer = map_evidence_bundle_to_drawer(cite_response())

    assert drawer["drawer_id"] == "kfm.drawer.ecology.eco_index.example"
    assert drawer["candidate_id"] == "eco_index.example"
    assert drawer["decision"] == "cite"
    assert drawer["status"] == "resolved"
    assert drawer["title"] == "Ecology evidence"
    assert drawer["proof_pack"] == {
        "ref": "data/proofs/ecology/eco_index.example.proof_pack.json",
        "spec_hash": SPEC_HASH,
    }
    assert drawer["actions"] == {
        "copy_citation": True,
        "open_catalog": True,
        "open_provenance": True,
    }

    sections = {section["section_id"]: section for section in drawer["sections"]}
    assert sections["receipts"]["items"] == [
        {
            "receipt_ref": "data/receipts/ecology/index/example.validator_receipt.json",
            "decision": "pass",
        }
    ]
    assert sections["catalog_refs"]["items"]["prov"] == [
        "kfm:prov:entity:ecology:example"
    ]
    assert sections["uncertainty"]["items"]["status"] == "declared"


def test_maps_abstain_response_to_drawer_payload() -> None:
    drawer = map_evidence_bundle_to_drawer(abstain_response())

    assert drawer["drawer_id"] == "kfm.drawer.ecology.eco_index.missing"
    assert drawer["candidate_id"] == "eco_index.missing"
    assert drawer["decision"] == "abstain"
    assert drawer["status"] == "unresolved"
    assert drawer["title"] == "Ecology evidence unavailable"
    assert drawer["failure"] == {
        "reason": "proof_pack_missing",
        "error_code": "ECO_EB_PROOF_PACK_MISSING",
    }
    assert drawer["actions"] == {
        "copy_citation": False,
        "open_catalog": False,
        "open_provenance": False,
    }

    sections = {section["section_id"]: section for section in drawer["sections"]}
    assert sections["failure"]["items"] == [
        {
            "label": "Reason",
            "value": "proof_pack_missing",
        }
    ]


def test_malformed_response_defaults_to_abstain() -> None:
    drawer = map_evidence_bundle_to_drawer({"status": "ok", "data": []})

    assert drawer["drawer_id"] == "kfm.drawer.ecology.unknown"
    assert drawer["candidate_id"] == "unknown"
    assert drawer["decision"] == "abstain"
    assert drawer["failure"]["reason"] == "invalid_response_shape"
    assert drawer["failure"]["error_code"] == "ECO_DRAWER_INVALID_RESPONSE"
    assert drawer["actions"]["copy_citation"] is False


def test_missing_evidence_sections_render_empty_values() -> None:
    response = cite_response()
    response["data"].pop("evidence")
    response["data"].pop("uncertainty")

    drawer = map_evidence_bundle_to_drawer(response)

    assert drawer["decision"] == "cite"

    sections = {section["section_id"]: section for section in drawer["sections"]}
    assert sections["receipts"]["items"] == []
    assert sections["catalog_refs"]["items"] == {}
    assert sections["uncertainty"]["items"] == {}


def test_non_cite_decision_maps_to_abstain() -> None:
    response = cite_response()
    response["data"]["decision"] = "review_required"
    response["data"]["reason"] = "policy_review_required"
    response["data"]["error_code"] = "ECO_EB_REVIEW_REQUIRED"

    drawer = map_evidence_bundle_to_drawer(response)

    assert drawer["decision"] == "abstain"
    assert drawer["failure"]["reason"] == "policy_review_required"
    assert drawer["failure"]["error_code"] == "ECO_EB_REVIEW_REQUIRED"
