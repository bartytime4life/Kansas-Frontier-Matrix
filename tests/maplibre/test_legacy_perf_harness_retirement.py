"""Regression guards for the removed standalone MapLibre performance harness."""

from __future__ import annotations

import json
from pathlib import Path

from tools.validators.maplibre.assess_acquisition_inventory import Outcome, scan


ROOT = Path(__file__).resolve().parents[2]
REMOVED_PATHS = (
    "scripts/maplibre-smoke-perf.mjs",
    "scripts/attest-maplibre-perf.mjs",
    "scripts/build-maplibre-render-diff.mjs",
    "scripts/build-maplibre-perf-proof-pack.mjs",
    "scripts/build-maplibre-perf-release-manifest.mjs",
    "scripts/build-maplibre-perf-failure-bundle.mjs",
    "scripts/build-maplibre-perf-correction-and-rollback.mjs",
    "tools/validators/maplibre/validate_perf_governance.py",
    "schemas/maplibre/perf-proof-pack.schema.json",
)


def test_retired_harness_and_its_trust_shaped_builders_stay_removed() -> None:
    assert [path for path in REMOVED_PATHS if (ROOT / path).exists()] == []


def test_root_workspace_exposes_no_perf_harness_commands() -> None:
    package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    assert [name for name in package.get("scripts", {}) if name.startswith("maplibre:")] == []
    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    for target in ("maplibre-perf:", "maplibre-govern:", "maplibre-proof:", "maplibre-clean:"):
        assert f"\n{target}" not in makefile


def test_current_renderer_acquisition_is_confined_to_package_seam() -> None:
    result = scan(ROOT)
    outside_seam = [
        finding
        for finding in result.findings
        if not finding.candidate_seam
    ]

    assert result.outcome is Outcome.HOLD
    assert "ACQUISITION_OUTSIDE_CANDIDATE_SEAM" not in result.reasons
    assert "RENDERER_ACQUISITION_PRESENT" in result.reasons
    assert result.findings
    assert not outside_seam
    assert all(finding.candidate_seam for finding in result.findings)
