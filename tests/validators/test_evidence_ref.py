from __future__ import annotations

import json
from pathlib import Path

import pytest

from packages.evidence.evidence_ref_resolver import (
    resolve_evidence_ref,
    validate_evidence_ref_schema,
    APPROVED_RELEASE_STATES,
)


SCHEMA_PATH = Path("schemas/contracts/v1/evidence/evidence_ref.schema.json")

SPEC_DIGEST = "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def published_ref() -> dict:
    return {
        "evidence_ref_id": "kfm:evidence:hydrology:huc12:102600080305",
        "domain": "hydrology",
        "ref": "data/catalog/hydrology/huc12/102600080305.json",
        "release_state": "PUBLISHED",
        "digest": SPEC_DIGEST,
        "sensitivity": "public",
        "review_state": "approved",
    }


def catalog_ref() -> dict:
    return {
        "evidence_ref_id": "kfm:evidence:flora:taxon:POPR",
        "domain": "flora",
        "ref": "data/catalog/flora/taxon/POPR.json",
        "release_state": "CATALOG",
    }


class TestEvidenceRefSchemaValidation:
    def test_valid_published_ref_passes_schema(self) -> None:
        errors = validate_evidence_ref_schema(
            evidence_ref=published_ref(),
            schema_path=SCHEMA_PATH,
        )
        assert errors == []

    def test_valid_catalog_ref_passes_schema(self) -> None:
        errors = validate_evidence_ref_schema(
            evidence_ref=catalog_ref(),
            schema_path=SCHEMA_PATH,
        )
        assert errors == []

    def test_missing_evidence_ref_id_fails_schema(self) -> None:
        ref = published_ref()
        ref.pop("evidence_ref_id")
        errors = validate_evidence_ref_schema(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert errors
        assert any("evidence_ref_id" in error for error in errors)

    def test_missing_domain_fails_schema(self) -> None:
        ref = published_ref()
        ref.pop("domain")
        errors = validate_evidence_ref_schema(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert errors
        assert any("domain" in error for error in errors)

    def test_missing_release_state_fails_schema(self) -> None:
        ref = published_ref()
        ref.pop("release_state")
        errors = validate_evidence_ref_schema(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert errors
        assert any("release_state" in error for error in errors)

    def test_invalid_release_state_fails_schema(self) -> None:
        ref = published_ref()
        ref["release_state"] = "NOT_A_VALID_STATE"
        errors = validate_evidence_ref_schema(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert errors
        assert any("release_state" in error for error in errors)

    def test_invalid_digest_pattern_fails_schema(self) -> None:
        ref = published_ref()
        ref["digest"] = "not-a-valid-digest"
        errors = validate_evidence_ref_schema(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert errors
        assert any("digest" in error for error in errors)

    def test_valid_sha256_digest_passes_schema(self) -> None:
        ref = published_ref()
        ref["digest"] = "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        errors = validate_evidence_ref_schema(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert errors == []


class TestEvidenceRefResolution:
    def test_published_ref_resolves_to_render_true(self) -> None:
        result = resolve_evidence_ref(
            evidence_ref=published_ref(),
            schema_path=SCHEMA_PATH,
        )
        assert result.render is True
        assert result.decision == "cite"
        assert result.error_code is None

    def test_catalog_ref_resolves_to_render_true(self) -> None:
        result = resolve_evidence_ref(
            evidence_ref=catalog_ref(),
            schema_path=SCHEMA_PATH,
        )
        assert result.render is True
        assert result.decision == "cite"

    def test_raw_release_state_abstains(self) -> None:
        ref = published_ref()
        ref["release_state"] = "RAW"
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert result.render is False
        assert result.decision == "abstain"
        assert result.error_code == "EVREF_RELEASE_STATE_NOT_APPROVED"

    def test_work_release_state_abstains(self) -> None:
        ref = published_ref()
        ref["release_state"] = "WORK"
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert result.render is False
        assert result.decision == "abstain"

    def test_quarantine_release_state_abstains(self) -> None:
        ref = published_ref()
        ref["release_state"] = "QUARANTINE"
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert result.render is False
        assert result.decision == "abstain"

    def test_processed_release_state_abstains(self) -> None:
        ref = published_ref()
        ref["release_state"] = "PROCESSED"
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert result.render is False
        assert result.decision == "abstain"

    def test_schema_invalid_abstains(self) -> None:
        ref = {"evidence_ref_id": "kfm:evidence:x", "ref": "x"}
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert result.render is False
        assert result.decision == "abstain"
        assert result.error_code == "EVREF_INVALID_SCHEMA"

    def test_digest_match_resolves(self) -> None:
        result = resolve_evidence_ref(
            evidence_ref=published_ref(),
            schema_path=SCHEMA_PATH,
            expected_digest=SPEC_DIGEST,
        )
        assert result.render is True
        assert result.decision == "cite"

    def test_digest_mismatch_abstains(self) -> None:
        result = resolve_evidence_ref(
            evidence_ref=published_ref(),
            schema_path=SCHEMA_PATH,
            expected_digest="sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        )
        assert result.render is False
        assert result.decision == "abstain"
        assert result.error_code == "EVREF_DIGEST_MISMATCH"


class TestEvidenceRefFixtures:
    def _load_fixture(self, name: str) -> dict:
        path = Path("tests/fixtures/evidence") / name
        return json.loads(path.read_text(encoding="utf-8"))

    def test_valid_published_fixture_resolves(self) -> None:
        ref = self._load_fixture("valid/evidence_ref_published.json")
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert result.render is True

    def test_valid_catalog_fixture_resolves(self) -> None:
        ref = self._load_fixture("valid/evidence_ref_catalog.json")
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert result.render is True

    def test_invalid_raw_fixture_abstains(self) -> None:
        ref = self._load_fixture("invalid/evidence_ref_raw_not_allowed.json")
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert result.render is False

    def test_invalid_quarantine_fixture_abstains(self) -> None:
        ref = self._load_fixture("invalid/evidence_ref_quarantine_not_allowed.json")
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert result.render is False

    def test_invalid_missing_domain_fixture_fails_schema(self) -> None:
        ref = self._load_fixture("invalid/evidence_ref_missing_domain.json")
        errors = validate_evidence_ref_schema(
            evidence_ref=ref,
            schema_path=SCHEMA_PATH,
        )
        assert errors
