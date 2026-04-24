#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


def test_render_bundle_diff_policy_summary() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "diff-policy.json"
        out = root / "summary.md"
        src.write_text(
            json.dumps({"decision": "allow", "reasons": ["no breaking drift"]}),
            encoding="utf-8",
        )

        subprocess.run(
            [
                "python3",
                "tools/ci/render_bundle_diff_policy_summary.py",
                "--input",
                str(src),
                "--output",
                str(out),
            ],
            check=True,
        )

        rendered = out.read_text(encoding="utf-8")
        assert "Decision: **allow**" in rendered
        assert "no breaking drift" in rendered


def test_render_bundle_diff_policy_summary_missing_decision_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "diff-policy.json"
        src.write_text(json.dumps({"reasons": ["x"]}), encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_bundle_diff_policy_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "missing required string key: decision" in proc.stderr


def test_render_bundle_diff_policy_summary_invalid_json_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "diff-policy.json"
        src.write_text("{not-json", encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_bundle_diff_policy_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "invalid JSON" in proc.stderr


def test_render_bundle_diff_policy_summary_reasons_must_be_list() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "diff-policy.json"
        src.write_text(json.dumps({"decision": "allow", "reasons": "not-a-list"}), encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_bundle_diff_policy_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "reasons must be a list when provided" in proc.stderr


def test_render_bundle_diff_policy_summary_non_object_json_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "diff-policy.json"
        src.write_text("[]", encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_bundle_diff_policy_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "expected top-level JSON object" in proc.stderr
