#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


def test_render_promotion_summary() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "promotion.json"
        out = root / "summary.md"
        src.write_text(json.dumps({"release_id": "r1", "state": "approved"}), encoding="utf-8")

        subprocess.run(
            ["python3", "tools/ci/render_promotion_summary.py", "--input", str(src), "--output", str(out)],
            check=True,
        )

        rendered = out.read_text(encoding="utf-8")
        assert "Release: **r1**" in rendered
        assert "State: **approved**" in rendered


def test_render_promotion_summary_missing_key_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "promotion.json"
        src.write_text(json.dumps({"release_id": "r1"}), encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_promotion_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "missing required string key: state" in proc.stderr


def test_render_promotion_summary_invalid_json_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "promotion.json"
        src.write_text("{not-json", encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_promotion_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "invalid JSON" in proc.stderr


def test_render_promotion_summary_non_object_json_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "promotion.json"
        src.write_text("[]", encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_promotion_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "expected top-level JSON object" in proc.stderr
