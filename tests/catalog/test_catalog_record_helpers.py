from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MOUNT_SCRIPT = ROOT / "tools/catalog/catalog_record_mount_check.py"
FRESH_SCRIPT = ROOT / "tools/catalog/catalog_freshness_report.py"


def _write(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_mounted_record_alignment_passes(tmp_path: Path) -> None:
    stac = {
        "id": "stac-item-1",
        "properties": {
            "kfm:subject_id": "kfm:subject:floodplain-kansas",
            "kfm:version": "v1",
            "kfm:release_ref": "kfm:release:floodplain-kansas:v1",
        },
    }
    dcat = {
        "id": "kfm:subject:floodplain-kansas",
        "version": "v1",
        "release_ref": "kfm:release:floodplain-kansas:v1",
    }
    prov = {
        "subject_id": "kfm:subject:floodplain-kansas",
        "version": "v1",
        "release_ref": "kfm:release:floodplain-kansas:v1",
    }

    _write(tmp_path / "stac.json", stac)
    _write(tmp_path / "dcat.json", dcat)
    _write(tmp_path / "prov.json", prov)

    result = subprocess.run(
        [
            "python3",
            str(MOUNT_SCRIPT),
            "--stac",
            str(tmp_path / "stac.json"),
            "--dcat",
            str(tmp_path / "dcat.json"),
            "--prov",
            str(tmp_path / "prov.json"),
            "--output",
            str(tmp_path / "report.json"),
        ],
        check=False,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    report = json.loads((tmp_path / "report.json").read_text(encoding="utf-8"))
    assert report["status"] == "pass"


def test_freshness_report_fails_when_spread_exceeds_threshold(tmp_path: Path) -> None:
    stac = {"properties": {"updated": "2026-04-01T00:00:00Z"}}
    dcat = {"modified": "2026-04-02T00:00:00Z"}
    prov = {"generated_at": "2026-04-20T00:00:00Z"}

    _write(tmp_path / "stac.json", stac)
    _write(tmp_path / "dcat.json", dcat)
    _write(tmp_path / "prov.json", prov)

    result = subprocess.run(
        [
            "python3",
            str(FRESH_SCRIPT),
            "--stac",
            str(tmp_path / "stac.json"),
            "--dcat",
            str(tmp_path / "dcat.json"),
            "--prov",
            str(tmp_path / "prov.json"),
            "--max-spread-days",
            "7",
            "--output",
            str(tmp_path / "freshness-report.json"),
        ],
        check=False,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 1
    report = json.loads((tmp_path / "freshness-report.json").read_text(encoding="utf-8"))
    assert report["status"] == "fail"
    assert any("spread" in error for error in report["errors"])
