from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools/catalog/catalog_crosslink.py"
FIXTURES = ROOT / "tests/catalog/fixtures"


def _run(decision_payload: dict, record_payload: dict, tmp_path: Path) -> subprocess.CompletedProcess[str]:
    decision = tmp_path / "decision.json"
    record = tmp_path / "record.json"
    output = tmp_path / "report.json"

    decision.write_text(json.dumps(decision_payload), encoding="utf-8")
    record.write_text(json.dumps(record_payload), encoding="utf-8")

    return subprocess.run(
        [
            "python3",
            str(SCRIPT),
            "--decision",
            str(decision),
            "--record",
            str(record),
            "--output",
            str(output),
        ],
        check=False,
        text=True,
        capture_output=True,
    )


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_catalog_crosslink_passes_for_aligned_triplet(tmp_path: Path) -> None:
    decision = {
        "release_ref": "kfm:release:floodplain-kansas:v1",
        "catalog_refs": {
            "stac": {
                "subject_id": "kfm:subject:floodplain-kansas",
                "version": "v1",
                "release_ref": "kfm:release:floodplain-kansas:v1",
            },
            "dcat": {
                "subject_id": "kfm:subject:floodplain-kansas",
                "version": "v1",
                "release_ref": "kfm:release:floodplain-kansas:v1",
            },
            "prov": {
                "subject_id": "kfm:subject:floodplain-kansas",
                "version": "v1",
                "release_ref": "kfm:release:floodplain-kansas:v1",
            },
        },
    }

    record = {
        "release_ref": "kfm:release:floodplain-kansas:v1",
        "catalog_refs": decision["catalog_refs"],
    }

    result = _run(decision, record, tmp_path)
    assert result.returncode == 0

    report = _read(tmp_path / "report.json")
    assert report["status"] == "pass"
    assert report["blocking"] is False
    assert report["errors"] == []
    assert len(report["checks"]) == 5


def test_catalog_crosslink_fails_for_prov_subject_mismatch(tmp_path: Path) -> None:
    decision = {
        "release_ref": "kfm:release:floodplain-kansas:v1",
        "catalog_refs": {
            "stac": {
                "subject_id": "kfm:subject:floodplain-kansas",
                "version": "v1",
                "release_ref": "kfm:release:floodplain-kansas:v1",
            },
            "dcat": {
                "subject_id": "kfm:subject:floodplain-kansas",
                "version": "v1",
                "release_ref": "kfm:release:floodplain-kansas:v1",
            },
            "prov": {
                "subject_id": "kfm:subject:floodplain-kansas",
                "version": "v1",
                "release_ref": "kfm:release:floodplain-kansas:v1",
            },
        },
    }
    record = _read(FIXTURES / "prov-mismatch.json")

    result = _run(decision, record, tmp_path)
    assert result.returncode == 1

    report = _read(tmp_path / "report.json")
    assert report["status"] == "fail"
    assert report["blocking"] is True
    assert any(
        "subject alignment failed" in e or "decision/record catalog triplet mismatch" in e
        for e in report["errors"]
    )


def test_catalog_crosslink_fails_for_release_ref_mismatch(tmp_path: Path) -> None:
    decision = {
        "release_ref": "kfm:release:floodplain-kansas:v1",
        "catalog_refs": {
            "stac": {
                "subject_id": "kfm:subject:floodplain-kansas",
                "version": "v1",
                "release_ref": "kfm:release:floodplain-kansas:v1",
            },
            "dcat": {
                "subject_id": "kfm:subject:floodplain-kansas",
                "version": "v1",
                "release_ref": "kfm:release:floodplain-kansas:v1",
            },
            "prov": {
                "subject_id": "kfm:subject:floodplain-kansas",
                "version": "v1",
                "release_ref": "kfm:release:floodplain-kansas:v1",
            },
        },
    }
    record = _read(FIXTURES / "promotion-record-mismatch.json")

    result = _run(decision, record, tmp_path)
    assert result.returncode == 1

    report = _read(tmp_path / "report.json")
    assert report["status"] == "fail"
    assert report["blocking"] is True
    assert any("release-ref alignment failed" in e for e in report["errors"])


def test_catalog_crosslink_fails_for_missing_triplet_ref(tmp_path: Path) -> None:
    decision = {
        "release_ref": "kfm:release:floodplain-kansas:v1",
        "catalog_refs": {
            "stac": {
                "subject_id": "kfm:subject:floodplain-kansas",
                "version": "v1",
                "release_ref": "kfm:release:floodplain-kansas:v1",
            },
            "dcat": {
                "subject_id": "kfm:subject:floodplain-kansas",
                "version": "v1",
                "release_ref": "kfm:release:floodplain-kansas:v1",
            },
        },
    }
    record = {
        "release_ref": "kfm:release:floodplain-kansas:v1",
        "catalog_refs": decision["catalog_refs"],
    }

    result = _run(decision, record, tmp_path)
    assert result.returncode == 1

    report = _read(tmp_path / "report.json")
    assert report["status"] == "fail"
    assert any("missing catalog refs: prov" in e for e in report["errors"])
