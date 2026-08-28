"""Tests for the synthetic SSURGO/SDA micro-snapshot comparator."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = REPO_ROOT / "tools/ingest/ssurgo_watch/sda_micro_snapshot.py"
FIXTURE_ROOT = REPO_ROOT / "tests/ingest/ssurgo_watch/fixtures/sda_micro_snapshot"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/soil/ssurgo_sda_micro_snapshot_report.schema.json"

SPEC = importlib.util.spec_from_file_location("kfm_sda_micro_snapshot", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

compare_snapshots = MODULE.compare_snapshots
VALIDATOR = Draft202012Validator(
    json.loads(SCHEMA_PATH.read_text(encoding="utf-8")),
    format_checker=FormatChecker(),
)


def _fixture(name: str) -> dict[str, object]:
    value = json.loads((FIXTURE_ROOT / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _validate_report(report: dict[str, object]) -> None:
    errors = sorted(VALIDATOR.iter_errors(report), key=lambda error: list(error.path))
    assert not errors, [error.message for error in errors]


def test_row_order_and_retrieval_time_alone_are_not_material() -> None:
    prior = _fixture("prior.json")
    current = _fixture("current_unchanged.json")
    prior_snapshot = copy.deepcopy(prior)
    current_snapshot = copy.deepcopy(current)

    first = compare_snapshots(prior, current)
    second = compare_snapshots(prior, current)

    assert first == second
    assert prior == prior_snapshot
    assert current == current_snapshot
    assert first.ok
    assert first.reason_codes == ()
    assert first.report is not None
    _validate_report(first.report)
    assert first.report["prior"]["content_spec_hash"] == first.report["current"]["content_spec_hash"]
    assert first.report["prior"]["retrieval_hash"] != first.report["current"]["retrieval_hash"]
    assert first.report["diff_summary"] == {
        "metadata_changed_fields": [],
        "rows_added": 0,
        "rows_removed": 0,
        "fields_changed": 0,
    }
    assert first.report["governance"]["steward_review_required"] is False


def test_metadata_row_addition_and_field_changes_emit_review_signal() -> None:
    result = compare_snapshots(_fixture("prior.json"), _fixture("current_changed.json"))

    assert result.outcome == "PROPOSED_WORK_RECORD"
    assert result.report is not None
    _validate_report(result.report)
    assert result.reason_codes == (
        "SDA_FIELDS_CHANGED",
        "SDA_ROWS_ADDED",
        "SOURCE_METADATA_CHANGED",
    )
    assert result.report["diff_summary"] == {
        "metadata_changed_fields": ["product_version", "source_etag"],
        "rows_added": 1,
        "rows_removed": 0,
        "fields_changed": 2,
    }
    assert result.report["added_rows"] == [{"mukey": "SYN-MU-A", "cokey": "SYN-CO-A3"}]
    assert result.report["governance"] == {
        "promotion_allowed": False,
        "publication_allowed": False,
        "release_state": "not_released",
        "review_state": "fixture_only",
        "steward_review_required": True,
    }


def test_component_percentage_sum_outside_one_point_holds() -> None:
    result = compare_snapshots(_fixture("prior.json"), _fixture("invalid_component_sum.json"))

    assert result.outcome == "VALIDATION_HOLD"
    assert result.report is None
    assert MODULE.Finding(
        "COMPONENT_PCT_SUM_OUTSIDE_TOLERANCE",
        "/current/rows@mukey=SYN-MU-A",
    ) in result.findings


def test_slope_outside_zero_to_one_hundred_holds() -> None:
    result = compare_snapshots(_fixture("prior.json"), _fixture("invalid_slope.json"))

    assert result.outcome == "VALIDATION_HOLD"
    assert result.report is None
    assert MODULE.Finding(
        "SLOPE_R_OUT_OF_RANGE", "/current/rows/0/slope_r"
    ) in result.findings


def test_duplicate_component_identity_holds() -> None:
    current = _fixture("prior.json")
    current["rows"].append(copy.deepcopy(current["rows"][0]))

    result = compare_snapshots(_fixture("prior.json"), current)

    assert result.outcome == "VALIDATION_HOLD"
    assert result.report is None
    codes = {finding.code for finding in result.findings}
    assert {"ROW_IDENTITY_DUPLICATE", "COKEY_DUPLICATE"} <= codes
