"""Tests for the fixture-only EPA AQS site-metadata delta comparator."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = REPO_ROOT / "tools/ingest/aqs_watch/aqs_site_delta.py"
FIXTURES = Path(__file__).parent / "fixtures"
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/atmosphere/"
    "aqs_site_metadata_delta_report.schema.json"
)

SPEC = importlib.util.spec_from_file_location("kfm_aqs_site_delta", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _fixture(name: str) -> dict[str, object]:
    value = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _assert_report_schema(report: dict[str, object]) -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    errors = list(
        Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        ).iter_errors(report)
    )
    assert errors == []


def test_retrieval_only_change_is_no_material_change_and_deterministic() -> None:
    prior = _fixture("prior.json")
    current = _fixture("current_unchanged.json")

    first = MODULE.compare_snapshots(prior, current)
    second = MODULE.compare_snapshots(prior, current)

    assert first == second
    assert first.outcome == "NO_MATERIAL_CHANGE"
    assert first.reason_code == "AQS_NO_MATERIAL_CHANGE"
    assert first.findings == ()
    assert first.report is not None
    _assert_report_schema(first.report)
    assert (
        first.report["prior_snapshot"]["content_hash"]
        == first.report["current_snapshot"]["content_hash"]
    )
    assert (
        first.report["prior_snapshot"]["retrieval_hash"]
        != first.report["current_snapshot"]["retrieval_hash"]
    )
    assert first.report["changes"] == []
    assert first.report["governance"] == {
        "steward_review_required": False,
        "promotion_allowed": False,
        "publication": False,
    }


def test_large_location_shift_abstains_without_echoing_coordinates() -> None:
    result = MODULE.compare_snapshots(
        _fixture("prior.json"),
        _fixture("current_location_shift.json"),
    )

    assert result.outcome == "ABSTAIN"
    assert result.reason_code == "AQS_HIGH_IMPACT_CHANGE_REQUIRES_REVIEW"
    assert result.report is not None
    _assert_report_schema(result.report)
    changes = result.report["changes"]
    assert [change["change_type"] for change in changes] == ["LOCATION_SHIFT"]
    assert changes[0]["impact"] == "HIGH"
    assert changes[0]["distance_m"] > 250

    def mapping_keys(value: object) -> set[str]:
        if isinstance(value, dict):
            keys = set(value)
            for child in value.values():
                keys.update(mapping_keys(child))
            return keys
        if isinstance(value, list):
            keys: set[str] = set()
            for child in value:
                keys.update(mapping_keys(child))
            return keys
        return set()

    assert "latitude" not in mapping_keys(result.report)
    assert "longitude" not in mapping_keys(result.report)


def test_method_change_abstains_as_comparability_risk() -> None:
    result = MODULE.compare_snapshots(
        _fixture("prior.json"),
        _fixture("current_method_change.json"),
    )

    assert result.outcome == "ABSTAIN"
    assert result.report is not None
    _assert_report_schema(result.report)
    assert result.report["changes"] == [
        {
            "site_id": "20-999-0001",
            "change_type": "METHOD_CHANGE",
            "impact": "HIGH",
            "changed_fields": ["method_code", "method_name"],
        }
    ]


def test_metadata_correction_proposes_work_record() -> None:
    result = MODULE.compare_snapshots(
        _fixture("prior.json"),
        _fixture("current_metadata_correction.json"),
    )

    assert result.outcome == "PROPOSED_WORK_RECORD"
    assert result.reason_code == "AQS_SOURCE_SURFACE_CHANGED"
    assert result.report is not None
    _assert_report_schema(result.report)
    assert result.report["decision"] == {
        "outcome": "PROPOSED_WORK_RECORD",
        "reason_codes": ["SOURCE_SURFACE_CHANGED"],
    }
    assert result.report["changes"][0]["impact"] == "LOW"


def test_poc_reassignment_and_lifecycle_change_abstain() -> None:
    prior = _fixture("prior.json")
    current = _fixture("current_unchanged.json")
    current["sites"][0]["poc"] = 2
    current["sites"][1]["status"] = "RETIRED"

    result = MODULE.compare_snapshots(prior, current)

    assert result.outcome == "ABSTAIN"
    assert result.report is not None
    _assert_report_schema(result.report)
    assert [change["change_type"] for change in result.report["changes"]] == [
        "POC_REASSIGNMENT",
        "SITE_LIFECYCLE",
    ]


def test_input_order_does_not_change_report_identity() -> None:
    prior = _fixture("prior.json")
    current = _fixture("current_unchanged.json")
    prior_reversed = copy.deepcopy(prior)
    current_reversed = copy.deepcopy(current)
    prior_reversed["sites"].reverse()
    current_reversed["sites"].reverse()

    assert MODULE.compare_snapshots(prior, current) == MODULE.compare_snapshots(
        prior_reversed, current_reversed
    )


def test_duplicate_site_identity_fails_closed() -> None:
    candidate = _fixture("prior.json")
    candidate["sites"].append(copy.deepcopy(candidate["sites"][0]))
    path = FIXTURES / "_duplicate-site.tmp.json"
    path.write_text(json.dumps(candidate), encoding="utf-8")
    try:
        result = MODULE.load_snapshot(path)
    finally:
        path.unlink(missing_ok=True)

    assert result.candidate is None
    assert MODULE.Finding("SITE_ID_DUPLICATE", "/sites/2/site_id") in result.findings


def test_non_object_input_returns_error() -> None:
    path = FIXTURES / "_non-object.tmp.json"
    path.write_text("[]", encoding="utf-8")
    try:
        result = MODULE.compare_files(path, FIXTURES / "current_unchanged.json")
    finally:
        path.unlink(missing_ok=True)

    assert result.outcome == "ERROR"
    assert result.reason_code == "AQS_SNAPSHOT_VALIDATION_ERROR"
    assert result.report is None
    assert MODULE.Finding("ROOT_NOT_OBJECT", "/prior/") in result.findings
