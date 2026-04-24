#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


def test_render_promotion_bundle_summary() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "bundle.json"
        out = root / "summary.md"
        src.write_text(json.dumps({"bundle_id": "b1", "artifacts": ["a", "b"]}), encoding="utf-8")

        subprocess.run(
            [
                "python3",
                "tools/ci/render_promotion_bundle_summary.py",
                "--input",
                str(src),
                "--output",
                str(out),
            ],
            check=True,
        )

        rendered = out.read_text(encoding="utf-8")
        assert "Bundle: **b1**" in rendered
        assert "Artifacts: **2**" in rendered


def test_render_promotion_bundle_summary_missing_bundle_id_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "bundle.json"
        src.write_text(json.dumps({"artifacts": ["a"]}), encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_promotion_bundle_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "missing required string key: bundle_id" in proc.stderr


def test_render_promotion_bundle_summary_artifacts_must_be_list() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "bundle.json"
        src.write_text(json.dumps({"bundle_id": "b1", "artifacts": "not-a-list"}), encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/render_promotion_bundle_summary.py", "--input", str(src)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "missing required list key: artifacts" in proc.stderr
