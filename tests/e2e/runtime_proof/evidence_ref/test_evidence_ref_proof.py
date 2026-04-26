from __future__ import annotations

import json
from pathlib import Path

import pytest

from packages.evidence.evidence_ref_resolver import (
    resolve_evidence_ref,
    resolve_evidence_ref_from_file,
)
from packages.evidence.composed_claim import resolve_composed_claim


EVIDENCE_REF_SCHEMA = Path("schemas/contracts/v1/evidence/evidence_ref.schema.json")
CLAIM_SCHEMA = Path("schemas/contracts/v1/evidence/claim_envelope.schema.json")


def make_published_ref(evidence_ref_id: str = "kfm:evidence:hydrology:huc12:test") -> dict:
    return {
        "evidence_ref_id": evidence_ref_id,
        "domain": "hydrology",
        "ref": "data/catalog/hydrology/huc12/test.json",
        "release_state": "PUBLISHED",
    }


def make_claim(
    *,
    evidence_refs: list[dict],
    composed_claim_refs: list[str] | None = None,
) -> dict:
    claim: dict = {
        "claim_id": "kfm:claim:runtime:test",
        "claim_text": "Runtime proof test claim.",
        "evidence_refs": evidence_refs,
        "render": True,
    }
    if composed_claim_refs is not None:
        claim["composed_claim_refs"] = composed_claim_refs
    return claim


class TestCoreInvariant:
    """
    Test the core evidence-chain invariant:
      - valid promoted evidence -> render allowed
      - missing / invalid / mismatched / unapproved evidence -> abstain
      - all required composed-claim refs resolved -> render=true
      - any required composed-claim ref unresolved -> render=false
    """

    def test_valid_promoted_evidence_renders(self) -> None:
        ref = make_published_ref()
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=EVIDENCE_REF_SCHEMA,
        )
        assert result.render is True, "valid promoted evidence must allow render"
        assert result.decision == "cite"

    def test_missing_evidence_file_abstains(self, tmp_path: Path) -> None:
        missing_path = tmp_path / "does_not_exist.json"
        result = resolve_evidence_ref_from_file(
            evidence_ref_path=missing_path,
            schema_path=EVIDENCE_REF_SCHEMA,
        )
        assert result.render is False, "missing evidence must abstain"
        assert result.decision == "abstain"
        assert result.error_code == "EVREF_MISSING"

    def test_invalid_evidence_ref_abstains(self) -> None:
        bad_ref = {"evidence_ref_id": "x", "ref": "x"}
        result = resolve_evidence_ref(
            evidence_ref=bad_ref,
            schema_path=EVIDENCE_REF_SCHEMA,
        )
        assert result.render is False, "invalid evidence must abstain"
        assert result.decision == "abstain"

    def test_unapproved_raw_evidence_abstains(self) -> None:
        ref = make_published_ref()
        ref["release_state"] = "RAW"
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=EVIDENCE_REF_SCHEMA,
        )
        assert result.render is False, "unapproved RAW evidence must abstain"
        assert result.decision == "abstain"
        assert result.error_code == "EVREF_RELEASE_STATE_NOT_APPROVED"

    def test_unapproved_work_evidence_abstains(self) -> None:
        ref = make_published_ref()
        ref["release_state"] = "WORK"
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=EVIDENCE_REF_SCHEMA,
        )
        assert result.render is False, "unapproved WORK evidence must abstain"

    def test_unapproved_quarantine_evidence_abstains(self) -> None:
        ref = make_published_ref()
        ref["release_state"] = "QUARANTINE"
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=EVIDENCE_REF_SCHEMA,
        )
        assert result.render is False, "QUARANTINE evidence must abstain"

    def test_mismatched_digest_abstains(self) -> None:
        ref = make_published_ref()
        ref["digest"] = "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        result = resolve_evidence_ref(
            evidence_ref=ref,
            schema_path=EVIDENCE_REF_SCHEMA,
            expected_digest="sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        )
        assert result.render is False, "digest mismatch must abstain"
        assert result.error_code == "EVREF_DIGEST_MISMATCH"

    def test_all_composed_claim_refs_resolved_renders(self) -> None:
        claim = make_claim(
            evidence_refs=[make_published_ref()],
            composed_claim_refs=["kfm:claim:sub1", "kfm:claim:sub2"],
        )
        result = resolve_composed_claim(
            claim_envelope=claim,
            claim_schema_path=CLAIM_SCHEMA,
            evidence_ref_schema_path=EVIDENCE_REF_SCHEMA,
            resolved_claim_ids={"kfm:claim:sub1", "kfm:claim:sub2"},
        )
        assert result.render is True, "all composed-claim refs resolved must render"

    def test_any_composed_claim_ref_unresolved_abstains(self) -> None:
        claim = make_claim(
            evidence_refs=[make_published_ref()],
            composed_claim_refs=["kfm:claim:sub1", "kfm:claim:missing"],
        )
        result = resolve_composed_claim(
            claim_envelope=claim,
            claim_schema_path=CLAIM_SCHEMA,
            evidence_ref_schema_path=EVIDENCE_REF_SCHEMA,
            resolved_claim_ids={"kfm:claim:sub1"},
        )
        assert result.render is False, "any unresolved composed-claim ref must abstain"
        assert result.decision == "abstain"
        assert "kfm:claim:missing" in result.unresolved_refs


class TestEvidenceRefFromFile:
    def test_valid_file_resolves(self, tmp_path: Path) -> None:
        evidence_ref_path = tmp_path / "test_ref.json"
        evidence_ref_path.write_text(
            json.dumps(make_published_ref()) + "\n",
            encoding="utf-8",
        )

        result = resolve_evidence_ref_from_file(
            evidence_ref_path=evidence_ref_path,
            schema_path=EVIDENCE_REF_SCHEMA,
        )
        assert result.render is True

    def test_invalid_json_file_abstains(self, tmp_path: Path) -> None:
        bad_path = tmp_path / "bad.json"
        bad_path.write_text("[not an object]", encoding="utf-8")

        result = resolve_evidence_ref_from_file(
            evidence_ref_path=bad_path,
            schema_path=EVIDENCE_REF_SCHEMA,
        )
        assert result.render is False
        assert result.decision == "abstain"

    def test_digest_match_via_file_resolves(self, tmp_path: Path) -> None:
        digest = "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        ref = make_published_ref()
        ref["digest"] = digest
        evidence_ref_path = tmp_path / "ref_with_digest.json"
        evidence_ref_path.write_text(json.dumps(ref) + "\n", encoding="utf-8")

        result = resolve_evidence_ref_from_file(
            evidence_ref_path=evidence_ref_path,
            schema_path=EVIDENCE_REF_SCHEMA,
            expected_digest=digest,
        )
        assert result.render is True

    def test_digest_mismatch_via_file_abstains(self, tmp_path: Path) -> None:
        ref = make_published_ref()
        ref["digest"] = "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        evidence_ref_path = tmp_path / "ref_digest_mismatch.json"
        evidence_ref_path.write_text(json.dumps(ref) + "\n", encoding="utf-8")

        result = resolve_evidence_ref_from_file(
            evidence_ref_path=evidence_ref_path,
            schema_path=EVIDENCE_REF_SCHEMA,
            expected_digest="sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        )
        assert result.render is False


class TestFailClosed:
    """
    Ensures that the resolver is fail-closed: any error path produces abstain,
    never a silent render=true.
    """

    def test_empty_object_abstains(self) -> None:
        result = resolve_evidence_ref(
            evidence_ref={},
            schema_path=EVIDENCE_REF_SCHEMA,
        )
        assert result.render is False

    def test_non_approved_states_all_abstain(self) -> None:
        non_approved = ["RAW", "WORK", "QUARANTINE", "PROCESSED"]
        for state in non_approved:
            ref = make_published_ref()
            ref["release_state"] = state
            result = resolve_evidence_ref(
                evidence_ref=ref,
                schema_path=EVIDENCE_REF_SCHEMA,
            )
            assert result.render is False, f"release_state={state} must not render"

    def test_approved_states_both_render(self) -> None:
        approved = ["PUBLISHED", "CATALOG"]
        for state in approved:
            ref = make_published_ref()
            ref["release_state"] = state
            result = resolve_evidence_ref(
                evidence_ref=ref,
                schema_path=EVIDENCE_REF_SCHEMA,
            )
            assert result.render is True, f"release_state={state} must render"
