#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


def _write_config(path: Path, checks: list[dict[str, object]]) -> None:
    path.write_text(json.dumps({"checks": checks}, indent=2), encoding="utf-8")


def test_markdown_authority_thresholds_pass(tmp_path: Path) -> None:
    (tmp_path / "docs").mkdir()
    target = tmp_path / "docs" / "README.md"
    target.write_text("TODO\nUNKNOWN\n", encoding="utf-8")

    config = tmp_path / "config.json"
    _write_config(config, [{"path": "docs/README.md", "max_total": 2}])

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/check_markdown_authority_thresholds.py",
            "--root",
            str(tmp_path),
            "--config",
            "config.json",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 0
    assert "check_markdown_authority_thresholds: ok" in proc.stdout


def test_markdown_authority_thresholds_fail_when_exceeds(tmp_path: Path) -> None:
    (tmp_path / "docs").mkdir()
    target = tmp_path / "docs" / "README.md"
    target.write_text("TODO\nUNKNOWN\nNEEDS VERIFICATION\n", encoding="utf-8")

    config = tmp_path / "config.json"
    _write_config(config, [{"path": "docs/README.md", "max_total": 2}])

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/check_markdown_authority_thresholds.py",
            "--root",
            str(tmp_path),
            "--config",
            "config.json",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 1
    assert "check_markdown_authority_thresholds: FAILED" in proc.stderr


def test_markdown_authority_thresholds_invalid_config_fails(tmp_path: Path) -> None:
    config = tmp_path / "config.json"
    config.write_text("{}", encoding="utf-8")

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/check_markdown_authority_thresholds.py",
            "--root",
            str(tmp_path),
            "--config",
            "config.json",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 2
    assert "config.checks must be a non-empty array" in proc.stderr
