from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, *args], text=True, capture_output=True, check=False)


def test_hydrology_freshness_probe_observed(tmp_path: Path) -> None:
    payload = tmp_path / "hydrology.json"
    payload.write_text(json.dumps({"observed_at": "2026-04-27T23:00:00Z"}), encoding="utf-8")
    out = tmp_path / "report.json"

    result = _run(
        "tools/probes/hydrology_freshness_probe.py",
        "--input",
        str(payload),
        "--source-ref",
        "kfm://source/hydrology/demo",
        "--freshness-threshold-seconds",
        "86400",
        "--checked-at",
        "2026-04-28T00:00:00Z",
        "--output",
        str(out),
    )

    assert result.returncode == 0
    report = json.loads(out.read_text(encoding="utf-8"))
    assert report["status"] == "OBSERVED"
    assert report["observations"]["lag_seconds"] == 3600


def test_catalog_release_refs_probe_missing_ref(tmp_path: Path) -> None:
    payload = tmp_path / "catalog.json"
    payload.write_text(
        json.dumps({"refs": {"receipt_ref": "kfm://receipts/x", "proof_ref": "kfm://proofs/y"}}),
        encoding="utf-8",
    )
    out = tmp_path / "report.json"

    result = _run(
        "tools/probes/catalog_release_refs_probe.py",
        "--input",
        str(payload),
        "--source-ref",
        "kfm://catalog/stac/demo",
        "--output",
        str(out),
    )

    assert result.returncode == 1
    report = json.loads(out.read_text(encoding="utf-8"))
    assert report["status"] == "CHANGED"
    assert report["observations"]["missing_refs"] == ["release_ref"]


def test_stac_materiality_probe_changed(tmp_path: Path) -> None:
    baseline = tmp_path / "baseline.json"
    candidate = tmp_path / "candidate.json"
    baseline.write_text(json.dumps({"type": "FeatureCollection", "features": [{"id": "A"}]}), encoding="utf-8")
    candidate.write_text(
        json.dumps({"type": "FeatureCollection", "features": [{"id": "A"}, {"id": "B"}]}),
        encoding="utf-8",
    )
    out = tmp_path / "report.json"

    result = _run(
        "tools/probes/stac_materiality_probe.py",
        "--baseline",
        str(baseline),
        "--candidate",
        str(candidate),
        "--source-ref",
        "kfm://catalog/stac/demo",
        "--max-count-delta",
        "0",
        "--output",
        str(out),
    )

    assert result.returncode == 1
    report = json.loads(out.read_text(encoding="utf-8"))
    assert report["status"] == "CHANGED"
    assert report["observations"]["count_delta"] == 1
