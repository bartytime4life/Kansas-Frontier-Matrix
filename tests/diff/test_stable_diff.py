#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests" / "diff" / "fixtures"
TOOL = ROOT / "tools" / "diff" / "stable_diff.py"


def test_stable_diff_same_when_only_key_order_changes() -> None:
    proc = subprocess.run(
        [
            "python3",
            str(TOOL),
            "--left",
            str(FIXTURES / "same" / "left.json"),
            "--right",
            str(FIXTURES / "same" / "right.json"),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 0
    payload = json.loads(proc.stdout)
    assert payload["status"] == "same"
    assert payload["blocking"] is False
    assert payload["summary"] == {"added": [], "removed": [], "changed": []}


def test_stable_diff_reports_added_removed_and_changed_keys() -> None:
    proc = subprocess.run(
        [
            "python3",
            str(TOOL),
            "--left",
            str(FIXTURES / "changed" / "left.json"),
            "--right",
            str(FIXTURES / "changed" / "right.json"),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 0
    payload = json.loads(proc.stdout)
    assert payload["status"] == "changed"
    assert payload["summary"]["added"] == ["delta"]
    assert payload["summary"]["removed"] == ["charlie"]
    assert payload["summary"]["changed"] == ["shared"]


def test_stable_diff_fail_on_change_exits_nonzero_and_sets_blocking() -> None:
    proc = subprocess.run(
        [
            "python3",
            str(TOOL),
            "--left",
            str(FIXTURES / "changed" / "left.json"),
            "--right",
            str(FIXTURES / "changed" / "right.json"),
            "--fail-on-change",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 1
    payload = json.loads(proc.stdout)
    assert payload["status"] == "changed"
    assert payload["blocking"] is True


def test_stable_diff_missing_input_fails_clearly() -> None:
    proc = subprocess.run(
        [
            "python3",
            str(TOOL),
            "--left",
            str(FIXTURES / "same" / "left.json"),
            "--right",
            str(FIXTURES / "same" / "does-not-exist.json"),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 2
    assert "input not found" in proc.stderr


def test_stable_diff_malformed_json_fails_clearly() -> None:
    proc = subprocess.run(
        [
            "python3",
            str(TOOL),
            "--left",
            str(FIXTURES / "malformed" / "broken.json"),
            "--right",
            str(FIXTURES / "same" / "right.json"),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 2
    assert "invalid JSON" in proc.stderr
