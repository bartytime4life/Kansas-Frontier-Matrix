"""Tests for the reviewer-only runtime-proof summary renderer."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from tools.ci.render_runtime_proof_summary import (
    SummaryRenderError,
    render_runtime_proof_summary,
)


def _report() -> dict[str, object]:
    return {
        "report_version": "soil-moisture-runtime-proof-report-v1",
        "profile_version": "soil-moisture-runtime-proof-v1",
        "issued_at": "2026-08-05T22:00:00Z",
        "cases": [
            {
                "case_id": "valid_fixture_not_released",
                "expected_outcome": "ABSTAIN",
                "expected_reason_code": "SOIL_MOISTURE_FIXTURE_NOT_RELEASED",
                "actual": {
                    "outcome": "ABSTAIN",
                    "reason_code": "SOIL_MOISTURE_FIXTURE_NOT_RELEASED",
                    "policy_state": "fixture_only_not_released",
                    "freshness": "fixture_only",
                    "evidence_refs": [
                        {
                            "ref": "evidence:synthetic-soil-moisture-series",
                            "kind": "measurement",
                        }
                    ],
                },
                "matched": True,
            }
        ],
    }


def _write(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_renders_matching_report_and_writes_output(tmp_path: Path) -> None:
    report_path = tmp_path / "report.json"
    output_path = tmp_path / "summary.md"
    _write(report_path, _report())

    summary = render_runtime_proof_summary(
        report_path, output_path=output_path, title="Custom Summary"
    )

    assert summary == output_path.read_text(encoding="utf-8")
    assert "# Custom Summary" in summary
    assert "**Matched:** `1`" in summary
    assert "**Mismatched:** `0`" in summary
    assert "`fixture_only_not_released`" in summary
    assert "| `valid_fixture_not_released` | `ABSTAIN` | `ABSTAIN` | ✅ |" in summary


def test_surfaces_mismatch_without_hiding_actual_outcome(tmp_path: Path) -> None:
    payload = _report()
    case = payload["cases"][0]
    case["actual"]["outcome"] = "DENY"
    case["matched"] = False
    report_path = tmp_path / "report.json"
    _write(report_path, payload)

    summary = render_runtime_proof_summary(report_path)

    assert "**Mismatched:** `1`" in summary
    assert "| `valid_fixture_not_released` | `ABSTAIN` | `DENY` | ❌ |" in summary


def test_rejects_contradictory_match_flag(tmp_path: Path) -> None:
    payload = _report()
    payload["cases"][0]["matched"] = False
    report_path = tmp_path / "report.json"
    _write(report_path, payload)

    with pytest.raises(SummaryRenderError, match="contradictory match flag"):
        render_runtime_proof_summary(report_path)


def test_does_not_mutate_report_input(tmp_path: Path) -> None:
    payload = _report()
    snapshot = copy.deepcopy(payload)
    report_path = tmp_path / "report.json"
    _write(report_path, payload)

    render_runtime_proof_summary(report_path)

    assert payload == snapshot
