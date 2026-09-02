from __future__ import annotations

import json
import socket
import subprocess
import sys
from pathlib import Path

from tools.proof_pack.proof_pack_check import (
    REQUIRED_KINDS,
    SCHEMA_PATH,
    validate_manifest,
)

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/proof_pack"
VALID = FIXTURES / "valid/valid_release_support.json"
INVALID = FIXTURES / "invalid"
CHECKER = ROOT / "tools/proof_pack/proof_pack_check.py"


def codes(path: Path) -> set[str]:
    return {finding.code for finding in validate_manifest(path)}


def test_valid_release_support_pack_passes() -> None:
    assert validate_manifest(VALID) == ()


def test_corrected_pack_requires_and_accepts_history() -> None:
    path = FIXTURES / "valid/valid_corrected_release_support.json"
    assert validate_manifest(path) == ()


def test_fixture_lane_has_exact_expected_polarity() -> None:
    result = subprocess.run(
        [sys.executable, str(CHECKER), "--fixtures"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "valid=2 invalid=8" in result.stdout
    assert "release_authority=false" in result.stdout


def test_required_component_set_is_closed() -> None:
    assert REQUIRED_KINDS == {
        "EVIDENCE_BUNDLE",
        "VALIDATION_REPORT",
        "INTEGRITY_MANIFEST",
        "PROV_EXPORT",
        "LINEAGE_INDEX",
        "PROMOTION_DECISION",
        "RUNTIME_PROOF",
        "CITATION_SAMPLE",
        "CI_RUN",
        "RELEASE_ANCHOR",
        "ROLLBACK_REFERENCE",
    }


def test_semantic_negative_codes() -> None:
    expected = {
        "semantic_invalid_missing_rollback.json": "REQUIRED_COMPONENT_MISSING",
        "semantic_invalid_release_mismatch.json": "COMPONENT_RELEASE_MISMATCH",
        "semantic_invalid_subject_hash_mismatch.json": "COMPONENT_SPEC_HASH_MISMATCH",
        "semantic_invalid_digest_mismatch.json": "COMPONENT_DIGEST_MISMATCH",
        "semantic_invalid_missing_file.json": "COMPONENT_NOT_FILE",
        "semantic_invalid_correction_history_required.json": "CORRECTION_HISTORY_REQUIRED",
        "semantic_invalid_duplicate_component_id.json": "COMPONENT_ID_DUPLICATE",
    }
    for name, expected_code in expected.items():
        assert expected_code in codes(INVALID / name)


def test_schema_denies_self_authority() -> None:
    assert "SCHEMA_INVALID" in codes(INVALID / "invalid_self_authority.json")


def test_checker_does_not_require_network(monkeypatch) -> None:
    def denied(*_args, **_kwargs):
        raise AssertionError("network access attempted")

    monkeypatch.setattr(socket, "socket", denied)
    assert validate_manifest(VALID) == ()


def test_schema_is_closed_draft_2020_12() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["additionalProperties"] is False
    assert schema["properties"]["decision"]["$ref"] == "#/$defs/decision"
