"""Regression guards for the retired standalone MapLibre performance harness."""

from __future__ import annotations

import subprocess
from pathlib import Path

from tools.validators.maplibre.assess_acquisition_inventory import Outcome, scan


ROOT = Path(__file__).resolve().parents[2]
HARNESS = ROOT / "scripts" / "maplibre-smoke-perf.mjs"


def test_retired_harness_fails_with_a_finite_hold() -> None:
    completed = subprocess.run(
        ["node", str(HARNESS)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 3
    assert completed.stdout == ""
    assert "WORKFLOW_HOLD" in completed.stderr
    assert "legacy MapLibre performance harness is retired" in completed.stderr
    assert "performance execution remains NOT_RUN" in completed.stderr


def test_retired_harness_has_no_renderer_or_network_acquisition() -> None:
    text = HARNESS.read_text(encoding="utf-8")

    for forbidden in (
        "unpkg.com",
        "demotiles.maplibre.org",
        "maplibregl",
        "playwright",
        "http://",
        "https://",
    ):
        assert forbidden not in text

    result = scan(ROOT)
    assert all(finding.path != "scripts/maplibre-smoke-perf.mjs" for finding in result.findings)


def test_current_renderer_acquisition_fails_outside_package_seam() -> None:
    result = scan(ROOT)
    outside_seam = [
        finding
        for finding in result.findings
        if not finding.candidate_seam
    ]

    assert result.outcome is Outcome.FAIL
    assert "ACQUISITION_OUTSIDE_CANDIDATE_SEAM" in result.reasons
    assert "RENDERER_ACQUISITION_PRESENT" in result.reasons
    assert outside_seam
    assert all(
        finding.path != "scripts/maplibre-smoke-perf.mjs"
        for finding in outside_seam
    )
