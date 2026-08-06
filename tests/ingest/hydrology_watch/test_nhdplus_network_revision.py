"""Tests for the no-network NHDPlus HR network revision comparator."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = REPO_ROOT / "tools/ingest/hydrology_watch/nhdplus_network_revision.py"
FIXTURES = Path(__file__).parent / "fixtures/nhdplus_network_revision"
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/hydrology/nhdplus_network_revision_report.schema.json"
)

SPEC = importlib.util.spec_from_file_location("kfm_nhdplus_network_revision", MODULE_PATH)
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
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(report)
    )
    assert errors == []


def test_retrieval_only_change_is_non_material_and_deterministic() -> None:
    prior = _fixture("prior.json")
    current = _fixture("current_unchanged.json")

    first = MODULE.compare_snapshots(prior, current)
    second = MODULE.compare_snapshots(prior, current)

    assert first == second
    assert first.outcome == "NO_MATERIAL_CHANGE"
    assert first.reason_code == "NHDPLUS_NO_MATERIAL_CHANGE"
    assert first.report is not None
    _assert_report_schema(first.report)
    assert first.report["changes"] == []
    assert (
        first.report["prior_snapshot"]["network_spec_hash"]
        == first.report["current_snapshot"]["network_spec_hash"]
    )
    assert (
        first.report["prior_snapshot"]["retrieval_hash"]
        != first.report["current_snapshot"]["retrieval_hash"]
    )


def test_geometry_threshold_breach_abstains_and_emits_actions() -> None:
    result = MODULE.compare_snapshots(
        _fixture("prior.json"), _fixture("current_geometry_shift.json")
    )

    assert result.outcome == "ABSTAIN"
    assert result.reason_code == "NHDPLUS_HIGH_IMPACT_NETWORK_REVISION"
    assert result.report is not None
    _assert_report_schema(result.report)
    assert result.report["changes"][0]["change_type"] == "GEOMETRY_SHIFT"
    assert result.report["changes"][0]["area_delta_pct"] > 0.1
    assert result.report["changes"][0]["centroid_shift_m"] > 100
    assert result.report["required_actions"] == [
        "RECOMPUTE_COMID_HUC12",
        "REVIEW_GEOMETRY_ALIGNMENT",
    ]


def test_linear_reference_change_abstains() -> None:
    result = MODULE.compare_snapshots(
        _fixture("prior.json"), _fixture("current_linear_reference_change.json")
    )

    assert result.outcome == "ABSTAIN"
    assert result.report is not None
    assert result.report["changes"] == [
        {
            "comid": 1002,
            "change_type": "LINEAR_REFERENCE_CHANGE",
            "impact": "HIGH",
            "changed_fields": ["from_measure", "hydroseq"],
        }
    ]
    assert result.report["required_actions"] == [
        "REFRESH_LINEAR_REFERENCED_EVENTS",
        "REINDEX_NWM_FORECAST_ATTACHMENTS",
    ]


def test_added_comid_proposes_work_record() -> None:
    result = MODULE.compare_snapshots(
        _fixture("prior.json"), _fixture("current_added.json")
    )

    assert result.outcome == "PROPOSED_WORK_RECORD"
    assert result.report is not None
    assert result.report["changes"][-1]["change_type"] == "COMID_ADDED"
    assert result.report["governance"]["promotion_allowed"] is False


def test_exact_geometry_thresholds_are_low_impact_not_high_impact() -> None:
    prior = _fixture("prior.json")
    current = _fixture("current_unchanged.json")
    current["flowlines"].reverse()
    geometry = current["flowlines"][0]["geometry_metrics"]
    geometry["catchment_area_m2"] = 1001000.0
    geometry["centroid_easting_m"] = 500100.0

    result = MODULE.compare_snapshots(prior, current)

    assert result.outcome == "PROPOSED_WORK_RECORD"
    assert result.report is not None
    assert result.report["changes"][0]["change_type"] == "GEOMETRY_CORRECTION"
    assert result.report["changes"][0]["impact"] == "LOW"


def test_input_order_does_not_change_report_identity() -> None:
    prior = _fixture("prior.json")
    current = _fixture("current_geometry_shift.json")
    prior_reversed = copy.deepcopy(prior)
    current_reversed = copy.deepcopy(current)
    prior_reversed["flowlines"].reverse()
    current_reversed["flowlines"].reverse()

    assert MODULE.compare_snapshots(prior, current) == MODULE.compare_snapshots(
        prior_reversed, current_reversed
    )


def test_duplicate_comid_fails_closed(tmp_path: Path) -> None:
    candidate = _fixture("prior.json")
    candidate["flowlines"].append(copy.deepcopy(candidate["flowlines"][0]))
    path = tmp_path / "duplicate.json"
    path.write_text(json.dumps(candidate), encoding="utf-8")

    result = MODULE.load_snapshot(path)

    assert result.candidate is None
    assert MODULE.Finding("COMID_DUPLICATE", "/flowlines/2/comid") in result.findings


def test_report_never_echoes_raw_centroid_coordinates() -> None:
    result = MODULE.compare_snapshots(
        _fixture("prior.json"), _fixture("current_geometry_shift.json")
    )
    assert result.report is not None

    encoded = json.dumps(result.report, sort_keys=True)
    assert "centroid_easting_m" not in encoded
    assert "centroid_northing_m" not in encoded
