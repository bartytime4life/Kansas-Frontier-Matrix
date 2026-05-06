from __future__ import annotations

import json
from pathlib import Path

from packages.evidence.composed_claim import (
    resolve_composed_claim,
    validate_claim_envelope_schema,
)


CLAIM_SCHEMA_PATH = Path("schemas/contracts/v1/evidence/claim_envelope.schema.json")
EVIDENCE_REF_SCHEMA_PATH = Path("schemas/contracts/v1/evidence/evidence_ref.schema.json")


def published_ref() -> dict:
    return {
        "evidence_ref_id": "kfm:evidence:hydrology:huc12:102600080305",
        "domain": "hydrology",
        "ref": "data/catalog/hydrology/huc12/102600080305.json",
        "release_state": "PUBLISHED",
        "sensitivity": "public",
        "review_state": "approved",
    }


def valid_claim_envelope() -> dict:
    return {
        "claim_id": "kfm:claim:hydrology:huc12:102600080305:render_allowed",
        "claim_text": "HUC12 102600080305 has documented hydrology evidence.",
        "evidence_refs": [published_ref()],
        "render": True,
        "decision": "cite",
    }


class TestClaimEnvelopeSchemaValidation:
    def test_valid_claim_passes_schema(self) -> None:
        errors = validate_claim_envelope_schema(
            claim_envelope=valid_claim_envelope(),
            schema_path=CLAIM_SCHEMA_PATH,
        )
        assert errors == []

    def test_missing_claim_id_fails_schema(self) -> None:
        claim = valid_claim_envelope()
        claim.pop("claim_id")
        errors = validate_claim_envelope_schema(
            claim_envelope=claim,
            schema_path=CLAIM_SCHEMA_PATH,
        )
        assert errors
        assert any("claim_id" in error for error in errors)

    def test_missing_claim_text_fails_schema(self) -> None:
        claim = valid_claim_envelope()
        claim.pop("claim_text")
        errors = validate_claim_envelope_schema(
            claim_envelope=claim,
            schema_path=CLAIM_SCHEMA_PATH,
        )
        assert errors
        assert any("claim_text" in error for error in errors)

    def test_empty_evidence_refs_fails_schema(self) -> None:
        claim = valid_claim_envelope()
        claim["evidence_refs"] = []
        errors = validate_claim_envelope_schema(
            claim_envelope=claim,
            schema_path=CLAIM_SCHEMA_PATH,
        )
        assert errors
        assert any("evidence_refs" in error for error in errors)

    def test_missing_render_field_fails_schema(self) -> None:
        claim = valid_claim_envelope()
        claim.pop("render")
        errors = validate_claim_envelope_schema(
            claim_envelope=claim,
            schema_path=CLAIM_SCHEMA_PATH,
        )
        assert errors
        assert any("render" in error for error in errors)

    def test_invalid_decision_fails_schema(self) -> None:
        claim = valid_claim_envelope()
        claim["decision"] = "maybe"
        errors = validate_claim_envelope_schema(
            claim_envelope=claim,
            schema_path=CLAIM_SCHEMA_PATH,
        )
        assert errors
        assert any("decision" in error for error in errors)


class TestComposedClaimResolution:
    def test_all_published_refs_render_true(self) -> None:
        result = resolve_composed_claim(
            claim_envelope=valid_claim_envelope(),
            claim_schema_path=CLAIM_SCHEMA_PATH,
            evidence_ref_schema_path=EVIDENCE_REF_SCHEMA_PATH,
        )
        assert result.render is True
        assert result.decision == "cite"
        assert result.unresolved_refs == []
        assert result.unresolved_evidence_refs == []

    def test_raw_evidence_ref_renders_false(self) -> None:
        claim = valid_claim_envelope()
        claim["evidence_refs"] = [
            {
                "evidence_ref_id": "kfm:evidence:hydrology:raw",
                "domain": "hydrology",
                "ref": "data/raw/hydrology/something.json",
                "release_state": "RAW",
            }
        ]
        result = resolve_composed_claim(
            claim_envelope=claim,
            claim_schema_path=CLAIM_SCHEMA_PATH,
            evidence_ref_schema_path=EVIDENCE_REF_SCHEMA_PATH,
        )
        assert result.render is False
        assert result.decision == "abstain"
        assert "kfm:evidence:hydrology:raw" in result.unresolved_evidence_refs

    def test_all_composed_refs_resolved_render_true(self) -> None:
        claim = valid_claim_envelope()
        claim["composed_claim_refs"] = [
            "kfm:claim:hydrology:sub1",
            "kfm:claim:hydrology:sub2",
        ]
        result = resolve_composed_claim(
            claim_envelope=claim,
            claim_schema_path=CLAIM_SCHEMA_PATH,
            evidence_ref_schema_path=EVIDENCE_REF_SCHEMA_PATH,
            resolved_claim_ids={
                "kfm:claim:hydrology:sub1",
                "kfm:claim:hydrology:sub2",
            },
        )
        assert result.render is True
        assert result.decision == "cite"

    def test_any_composed_ref_unresolved_render_false(self) -> None:
        claim = valid_claim_envelope()
        claim["composed_claim_refs"] = [
            "kfm:claim:hydrology:sub1",
            "kfm:claim:hydrology:unresolved",
        ]
        result = resolve_composed_claim(
            claim_envelope=claim,
            claim_schema_path=CLAIM_SCHEMA_PATH,
            evidence_ref_schema_path=EVIDENCE_REF_SCHEMA_PATH,
            resolved_claim_ids={"kfm:claim:hydrology:sub1"},
        )
        assert result.render is False
        assert result.decision == "abstain"
        assert "kfm:claim:hydrology:unresolved" in result.unresolved_refs
        assert result.error_code == "CLAIM_COMPOSED_REF_UNRESOLVED"

    def test_no_composed_refs_with_all_evidence_resolved(self) -> None:
        claim = valid_claim_envelope()
        claim["composed_claim_refs"] = []
        result = resolve_composed_claim(
            claim_envelope=claim,
            claim_schema_path=CLAIM_SCHEMA_PATH,
            evidence_ref_schema_path=EVIDENCE_REF_SCHEMA_PATH,
        )
        assert result.render is True

    def test_schema_invalid_claim_abstains(self) -> None:
        claim = {"claim_id": "kfm:claim:invalid", "claim_text": "no evidence refs"}
        result = resolve_composed_claim(
            claim_envelope=claim,
            claim_schema_path=CLAIM_SCHEMA_PATH,
            evidence_ref_schema_path=EVIDENCE_REF_SCHEMA_PATH,
        )
        assert result.render is False
        assert result.decision == "abstain"
        assert result.error_code == "CLAIM_SCHEMA_INVALID"


class TestClaimEnvelopeFixtures:
    def _load_fixture(self, name: str) -> dict:
        path = Path("tests/fixtures/evidence") / name
        return json.loads(path.read_text(encoding="utf-8"))

    def test_valid_render_allowed_fixture_resolves(self) -> None:
        claim = self._load_fixture("valid/claim_envelope_render_allowed.json")
        result = resolve_composed_claim(
            claim_envelope=claim,
            claim_schema_path=CLAIM_SCHEMA_PATH,
            evidence_ref_schema_path=EVIDENCE_REF_SCHEMA_PATH,
        )
        assert result.render is True

    def test_valid_composed_render_allowed_fixture_resolves(self) -> None:
        claim = self._load_fixture("valid/claim_envelope_composed_render_allowed.json")
        resolved_ids = {
            "kfm:claim:hydrology:huc12:102600080305:render_allowed",
            "kfm:claim:flora:taxon:POPR:render_allowed",
        }
        result = resolve_composed_claim(
            claim_envelope=claim,
            claim_schema_path=CLAIM_SCHEMA_PATH,
            evidence_ref_schema_path=EVIDENCE_REF_SCHEMA_PATH,
            resolved_claim_ids=resolved_ids,
        )
        assert result.render is True

    def test_invalid_unresolved_composed_ref_fixture_abstains(self) -> None:
        claim = self._load_fixture("invalid/claim_envelope_render_false_unresolved_ref.json")
        result = resolve_composed_claim(
            claim_envelope=claim,
            claim_schema_path=CLAIM_SCHEMA_PATH,
            evidence_ref_schema_path=EVIDENCE_REF_SCHEMA_PATH,
        )
        assert result.render is False
        assert result.decision == "abstain"
