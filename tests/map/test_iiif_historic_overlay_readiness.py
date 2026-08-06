"""Focused no-network tests for IIIF historic-overlay readiness."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.map import validate_iiif_historic_overlay_readiness as target

REPO_ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/map/iiif_historic_overlay_readiness/cases.json"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/map/iiif_historic_overlay_readiness.schema.json"

def _manifest() -> dict:
    return json.loads(CASES_PATH.read_text(encoding="utf-8"))

def _cases() -> list[dict]:
    return _manifest()["cases"]

def _case(case_id: str) -> dict:
    manifest = _manifest()
    entry = next(item for item in manifest["cases"] if item["case_id"] == case_id)
    return {
        "candidate": target.materialize_fixture_case(manifest, entry),
        "expected": copy.deepcopy(entry["expected"]),
    }

def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)

def test_fixture_manifest_has_all_finite_outcomes() -> None:
    outcomes = {item["expected"]["outcome"] for item in _cases()}
    assert outcomes == {"READY", "HOLD", "DENY", "ERROR"}

def test_all_fixture_cases_match_exact_expected_decision() -> None:
    manifest = _manifest()
    assert len(manifest["cases"]) >= 8
    for item in manifest["cases"]:
        candidate = target.materialize_fixture_case(manifest, item)
        result = target.validate_candidate(candidate)
        assert {"outcome": result.outcome, "reasons": list(result.reasons)} == item["expected"]

def test_ready_annotation_digest_recomputes_from_exact_embedded_bytes() -> None:
    candidate = _case("ready_iiif3_georef")["candidate"]
    payload = candidate["raw_capture"]["annotation_payload_utf8"].encode("utf-8")
    expected = "sha256:" + hashlib.sha256(payload).hexdigest()
    assert candidate["raw_capture"]["annotation_digest"] == expected
    assert target.validate_candidate(candidate).outcome == "READY"

def test_error_precedes_deny_and_hold() -> None:
    candidate = _case("ready_iiif3_georef")["candidate"]
    candidate["raw_capture"]["annotation_digest"] = "sha256:" + "a" * 64
    candidate["public_boundary"]["raw_route_exposed"] = True
    candidate["rights"]["kfm_rights_state"] = "UNKNOWN"
    outcome, reasons, _ = target.derive_decision(candidate)
    assert outcome == "ERROR"
    assert reasons == ("ANNOTATION_DIGEST_MISMATCH",)

def test_deny_precedes_hold() -> None:
    candidate = _case("ready_iiif3_georef")["candidate"]
    candidate["renderer"]["allowlisted"] = False
    candidate["source"]["freshness"] = "STALE"
    outcome, reasons, _ = target.derive_decision(candidate)
    assert outcome == "DENY"
    assert reasons == ("PLUGIN_NOT_ALLOWLISTED",)

def test_preview_presentation_api_remains_hold() -> None:
    candidate = _case("ready_iiif3_georef")["candidate"]
    candidate["source"]["presentation_api_version"] = "4.0-preview"
    outcome, reasons, _ = target.derive_decision(candidate)
    assert outcome == "HOLD"
    assert "PREVIEW_API_NOT_ADOPTED" in reasons

def test_legacy_2_1_can_clear_hold_with_explicit_normalization_ref() -> None:
    candidate = _case("ready_iiif3_georef")["candidate"]
    candidate["source"]["presentation_api_version"] = "2.1.1"
    candidate["source"]["image_api_version"] = "2.1.1"
    candidate["source"]["legacy_normalization_ref"] = "kfm:normalization:iiif-2.1-to-3-profile"
    outcome, reasons, _ = target.derive_decision(candidate)
    assert outcome == "READY"
    assert reasons == ("IIIF_HISTORIC_OVERLAY_READY",)

def test_care_authority_requires_consent_reference() -> None:
    candidate = _case("ready_iiif3_georef")["candidate"]
    candidate["care"]["authority_to_control"] = ["tribal-cultural-authority"]
    outcome, reasons, _ = target.derive_decision(candidate)
    assert outcome == "DENY"
    assert reasons == ("CARE_CONSENT_MISSING",)

def test_validator_has_no_network_or_execution_imports() -> None:
    source = Path(target.__file__).read_text(encoding="utf-8")
    denied = ("import socket", "import requests", "import httpx", "import urllib", "import subprocess")
    assert not any(token in source for token in denied)

def test_fixture_cli_contract_passes() -> None:
    assert target.validate_fixtures() == 0
