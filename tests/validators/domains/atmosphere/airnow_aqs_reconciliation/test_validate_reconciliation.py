"""Tests for the fixture-only AirNow-to-AQS reconciliation gate."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[5]
MODULE_PATH = REPO_ROOT / "tools/validators/domains/atmosphere/airnow_aqs_reconciliation/validate_reconciliation.py"
FIXTURES = REPO_ROOT / "fixtures/domains/atmosphere/airnow_aqs_reconciliation/valid"
REPORT_SCHEMA = REPO_ROOT / "schemas/contracts/v1/domains/atmosphere/airnow_aqs_reconciliation_report.schema.json"

SPEC = importlib.util.spec_from_file_location("kfm_airnow_aqs_reconciliation", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _fixture(name: str) -> dict[str, object]:
    value = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _assert_report_schema(report: dict[str, object]) -> None:
    schema = json.loads(REPORT_SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(report))
    assert errors == []


def test_certified_aqs_record_proposes_reviewed_replacement() -> None:
    result = MODULE.validate_candidate(_fixture("certified_replacement.json"))
    assert result.ok
    assert result.report is not None
    _assert_report_schema(result.report)
    assert result.report["canonical_monitor_key"] == "20-173-0010-88101-1"
    assert result.report["decision"] == {
        "outcome": "PROPOSED_WORK_RECORD",
        "reason_code": "AQS_AUTHORITATIVE_REPLACEMENT_AVAILABLE",
    }
    assert result.report["lineage"]["preserve_airnow_record"] is True
    assert result.report["lineage"]["superseding_source"] == "AQS"


def test_airnow_only_public_context_abstains() -> None:
    result = MODULE.validate_candidate(_fixture("provisional_context_only.json"))
    assert result.ok
    assert result.report is not None
    assert result.report["decision"]["reason_code"] == "AIRNOW_PROVISIONAL_CONTEXT_ONLY"
    assert result.report["lineage"]["superseding_source"] is None


def test_regulatory_use_without_aqs_is_denied() -> None:
    result = MODULE.validate_candidate(_fixture("regulatory_without_aqs.json"))
    assert result.ok
    assert result.report is not None
    assert result.report["decision"] == {
        "outcome": "DENY",
        "reason_code": "AQS_AUTHORITATIVE_RECORD_MISSING",
    }


def test_pending_aqs_certification_abstains() -> None:
    result = MODULE.validate_candidate(_fixture("pending_certification.json"))
    assert result.ok
    assert result.report is not None
    assert result.report["decision"]["reason_code"] == "AQS_CERTIFICATION_PENDING"


def test_nowcast_remains_derived_and_is_not_replaced_by_concentration() -> None:
    result = MODULE.validate_candidate(_fixture("nowcast_derived.json"))
    assert result.ok
    assert result.report is not None
    assert result.report["decision"]["reason_code"] == "AIRNOW_NOWCAST_DERIVED_ONLY"
    assert result.report["lineage"]["superseding_source"] is None


def test_monitor_key_mismatch_fails_closed() -> None:
    candidate = _fixture("certified_replacement.json")
    candidate["aqs"]["identity"]["poc"] = 2
    result = MODULE.validate_candidate(candidate)
    assert not result.ok
    assert result.report is None
    assert MODULE.Finding("MONITOR_KEY_MISMATCH", "/aqs/identity") in result.findings


def test_source_role_collapse_fails_schema() -> None:
    candidate = _fixture("certified_replacement.json")
    candidate["airnow"]["source_role"] = "regulatory_archive"
    result = MODULE.validate_candidate(candidate)
    assert not result.ok
    assert any(f.code == "SCHEMA_INVALID" and f.path == "/airnow/source_role" for f in result.findings)


def test_reconciliation_identity_is_deterministic() -> None:
    candidate = _fixture("certified_replacement.json")
    first = MODULE.validate_candidate(candidate)
    second = MODULE.validate_candidate(copy.deepcopy(candidate))
    assert first == second


def test_report_does_not_echo_measurement_values() -> None:
    result = MODULE.validate_candidate(_fixture("certified_replacement.json"))
    assert result.report is not None
    encoded = json.dumps(result.report, sort_keys=True)
    assert '"value"' not in encoded
    assert "35.2" not in encoded
    assert "34.8" not in encoded
