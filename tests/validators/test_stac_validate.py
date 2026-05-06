from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


def test_temporal_gate_passes_with_valid_item_and_collection(tmp_path: Path) -> None:
    root = tmp_path / "stac"
    reports = tmp_path / "reports"
    write_json(
        root / "collection.json",
        {
            "type": "Collection",
            "stac_version": "1.0.0",
            "id": "demo",
            "description": "demo collection",
            "license": "proprietary",
            "extent": {
                "spatial": {"bbox": [[-180, -90, 180, 90]]},
                "temporal": {"interval": [["2026-05-01T00:00:00Z", "2026-05-31T23:59:59Z"]]},
            },
            "links": [],
        },
    )
    write_json(
        root / "item.json",
        {
            "type": "Feature",
            "stac_version": "1.0.0",
            "id": "item-1",
            "collection": "demo",
            "geometry": None,
            "bbox": [-180, -90, 180, 90],
            "properties": {"datetime": "2026-05-06T12:00:00Z"},
            "assets": {"data": {"href": "s3://bucket/item_20260506T120000Z.tif"}},
            "links": [],
        },
    )

    result = subprocess.run(
        [
            sys.executable,
            "tools/validators/stac_validate.py",
            str(root),
            "--skip-schema",
            "--reports-dir",
            str(reports),
        ],
        check=False,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stderr + result.stdout
    receipt = json.loads((reports / "run_receipt.json").read_text(encoding="utf-8"))
    assert receipt["outcome"] == "ANSWER"


def test_temporal_gate_denies_non_utc_time(tmp_path: Path) -> None:
    root = tmp_path / "stac"
    reports = tmp_path / "reports"
    write_json(
        root / "item.json",
        {
            "type": "Feature",
            "stac_version": "1.0.0",
            "id": "item-1",
            "geometry": None,
            "bbox": [-180, -90, 180, 90],
            "properties": {"datetime": "2026-05-06T12:00:00+00:00"},
            "assets": {"data": {"href": "s3://bucket/item.tif"}},
            "links": [],
        },
    )

    result = subprocess.run(
        [
            sys.executable,
            "tools/validators/stac_validate.py",
            str(root),
            "--skip-schema",
            "--reports-dir",
            str(reports),
        ],
        check=False,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 1
    report = json.loads((reports / "validation_report.json").read_text(encoding="utf-8"))
    assert any(e["code"] == "invalid-datetime" for e in report["errors"])
