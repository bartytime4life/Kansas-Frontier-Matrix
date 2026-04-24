#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


def test_render_diff_summary() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "diff.json"
        out = root / "summary.md"
        src.write_text(json.dumps({"added": 2, "changed": 3, "removed": 1}), encoding="utf-8")

        subprocess.run(
            ["python3", "tools/ci/render_diff_summary.py", "--input", str(src), "--output", str(out)],
            check=True,
        )

        rendered = out.read_text(encoding="utf-8")
        assert "Added: **2**" in rendered
        assert "Changed: **3**" in rendered
        assert "Removed: **1**" in rendered


def test_render_diff_summary_missing_key_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "diff.json"
        src.write_text(json.dumps({"added": 2, "changed": 3}), encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_diff_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "missing required key" in proc.stderr


def test_render_diff_summary_invalid_json_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "diff.json"
        src.write_text("{not-json", encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_diff_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "invalid JSON" in proc.stderr


def test_render_diff_summary_non_object_json_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "diff.json"
        src.write_text("[1,2,3]", encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_diff_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "expected top-level JSON object" in proc.stderr
