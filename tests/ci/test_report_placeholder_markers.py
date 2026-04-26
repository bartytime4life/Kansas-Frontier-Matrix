#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


def test_report_placeholder_markers_text_output(tmp_path: Path) -> None:
    (tmp_path / "a.md").write_text("TODO\nUNKNOWN\n", encoding="utf-8")
    (tmp_path / "b.md").write_text("NEEDS VERIFICATION\nNEEDS VERIFICATION\n", encoding="utf-8")
    (tmp_path / "nested").mkdir()
    (tmp_path / "nested" / "c.md").write_text("TODO\n", encoding="utf-8")

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/report_placeholder_markers.py",
            "--root",
            str(tmp_path),
            "--top",
            "2",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 0
    assert "TODO: 2" in proc.stdout
    assert "UNKNOWN: 1" in proc.stdout
    assert "NEEDS VERIFICATION: 2" in proc.stdout
    assert "files_with_markers: 3" in proc.stdout
    assert f"- {Path('b.md')}: total=2 (NEEDS VERIFICATION=2)" in proc.stdout


def test_report_placeholder_markers_json_output(tmp_path: Path) -> None:
    (tmp_path / "x.md").write_text("ALPHA\nALPHA\nBETA\n", encoding="utf-8")
    (tmp_path / "y.md").write_text("BETA\n", encoding="utf-8")

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/report_placeholder_markers.py",
            "--root",
            str(tmp_path),
            "--marker",
            "ALPHA",
            "--marker",
            "BETA",
            "--format",
            "json",
            "--top",
            "1",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 0
    payload = json.loads(proc.stdout)
    assert payload["markers"] == ["ALPHA", "BETA"]
    assert payload["totals"] == {"ALPHA": 2, "BETA": 2}
    assert payload["files_with_markers"] == 2
    assert payload["top_files"][0]["path"] == "x.md"
    assert payload["top_files"][0]["total"] == 3


def test_report_placeholder_markers_invalid_root_fails() -> None:
    proc = subprocess.run(
        [
            "python3",
            "tools/ci/report_placeholder_markers.py",
            "--root",
            "does-not-exist",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 2
    assert "report_placeholder_markers: invalid root path" in proc.stderr


def test_report_placeholder_markers_threshold_failure(tmp_path: Path) -> None:
    (tmp_path / "a.md").write_text("TODO\nTODO\nUNKNOWN\n", encoding="utf-8")

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/report_placeholder_markers.py",
            "--root",
            str(tmp_path),
            "--max-overall",
            "2",
            "--max-marker",
            "TODO=1",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 1
    assert "threshold check failed" in proc.stderr
    assert "overall marker total 3 exceeds configured max-overall 2" in proc.stderr
    assert "marker 'TODO' count 2 exceeds configured max 1" in proc.stderr


def test_report_placeholder_markers_threshold_pass(tmp_path: Path) -> None:
    (tmp_path / "a.md").write_text("TODO\nUNKNOWN\n", encoding="utf-8")

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/report_placeholder_markers.py",
            "--root",
            str(tmp_path),
            "--max-overall",
            "2",
            "--max-marker",
            "TODO=1",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 0


def test_report_placeholder_markers_invalid_max_marker_fails(tmp_path: Path) -> None:
    (tmp_path / "a.md").write_text("TODO\n", encoding="utf-8")

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/report_placeholder_markers.py",
            "--root",
            str(tmp_path),
            "--max-marker",
            "BROKEN_FORMAT",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 2
    assert "invalid --max-marker value" in proc.stderr
