"""Tests for the fixture-only HLS NDVI zonal materiality assessment."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[5]
MODULE_PATH = REPO_ROOT / (
    "tools/validators/domains/agriculture/hls_ndvi_zonal_materiality/"
    "validate_hls_ndvi_zonal_materiality.py"
)
FIXTURES = (
    REPO_ROOT / "fixtures/domains/agriculture/hls_ndvi_zonal_materiality/valid"
)

SPEC = importlib.util.spec_from_file_location("kfm_hls_ndvi_materiality", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _fixture(name: str) -> dict[str, object]:
    value = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _refresh(payload: dict[str, object]) -> None:
    payload["computed"] = MODULE.derive_computed(payload)
    payload["decision"] = {
        "outcome": MODULE.expected_outcome(payload),
        "reasons": MODULE.expected_reasons(payload),
    }
    payload["spec_hash"] = MODULE.canonical_spec_hash(payload)


def test_material_change_candidate_is_valid_and_deterministic() -> None:
    payload = _fixture("material_change_candidate.json")

    first = MODULE.validate_payload(payload)
    second = MODULE.validate_payload(copy.deepcopy(payload))

    assert first == second
    assert first.ok
    assert payload["decision"] == {
        "outcome": "MATERIAL_CHANGE_CANDIDATE",
        "reasons": [],
    }


def test_small_signal_is_no_material_change() -> None:
    payload = _fixture("no_material_signal.json")

    result = MODULE.validate_payload(payload)

    assert result.ok
    assert payload["decision"] == {
        "outcome": "NO_MATERIAL_CHANGE",
        "reasons": ["SIGNAL_BELOW_THRESHOLD"],
    }


def test_low_valid_fraction_is_hold() -> None:
    payload = _fixture("low_valid_hold.json")

    result = MODULE.validate_payload(payload)

    assert result.ok
    assert payload["decision"]["outcome"] == "HOLD"
    assert "VALID_FRACTION_BELOW_MINIMUM" in payload["decision"]["reasons"]


def test_source_unchanged_is_no_material_change() -> None:
    payload = _fixture("source_unchanged.json")

    result = MODULE.validate_payload(payload)

    assert result.ok
    assert payload["decision"] == {
        "outcome": "NO_MATERIAL_CHANGE",
        "reasons": ["SOURCE_UNCHANGED"],
    }


def test_threshold_equality_is_not_material() -> None:
    payload = _fixture("material_change_candidate.json")
    payload["prior"]["statistics"]["mean_ndvi"] = 0.5
    payload["current"]["statistics"]["mean_ndvi"] = 0.55
    _refresh(payload)

    result = MODULE.validate_payload(payload)

    assert result.ok
    assert payload["computed"]["absolute_change"] == 0.05
    assert payload["computed"]["relative_change"] == 0.1
    assert payload["decision"] == {
        "outcome": "NO_MATERIAL_CHANGE",
        "reasons": ["SIGNAL_BELOW_THRESHOLD"],
    }


def test_pixel_count_closure_is_required() -> None:
    payload = _fixture("material_change_candidate.json")
    payload["current"]["pixel_counts"]["cloud"] += 1
    _refresh(payload)

    result = MODULE.validate_payload(payload)

    assert MODULE.Finding(
        "PIXEL_COUNT_CLOSURE_INVALID", "/current/pixel_counts"
    ) in result.findings


def test_support_identity_matches_support_kind() -> None:
    payload = _fixture("material_change_candidate.json")
    payload["support"] = {"kind": "huc12", "id": "20091"}
    _refresh(payload)

    result = MODULE.validate_payload(payload)

    assert MODULE.Finding("HUC12_ID_INVALID", "/support/id") in result.findings


def test_summary_percentile_order_is_required() -> None:
    payload = _fixture("material_change_candidate.json")
    payload["current"]["statistics"]["p95_ndvi"] = 0.2
    _refresh(payload)

    result = MODULE.validate_payload(payload)

    assert MODULE.Finding(
        "SUMMARY_STAT_ORDER_INVALID", "/current/statistics"
    ) in result.findings


def test_computed_fields_cannot_be_fabricated() -> None:
    payload = _fixture("material_change_candidate.json")
    payload["computed"]["source_changed"] = False
    payload["spec_hash"] = MODULE.canonical_spec_hash(payload)

    result = MODULE.validate_payload(payload)

    assert MODULE.Finding(
        "COMPUTED_FIELD_MISMATCH", "/computed/source_changed"
    ) in result.findings


def test_spec_hash_mismatch_is_rejected() -> None:
    payload = _fixture("material_change_candidate.json")
    payload["current"]["collection_version"] = "unexpected"

    result = MODULE.validate_payload(payload)

    assert MODULE.Finding("SPEC_HASH_MISMATCH", "/spec_hash") in result.findings
