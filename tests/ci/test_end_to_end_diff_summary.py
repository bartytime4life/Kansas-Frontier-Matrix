#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path


def test_end_to_end_diff_summary_golden() -> None:
    fixture = Path("tests/ci/fixtures/diff_summary/diff.json")
    out_path = Path("tests/ci/golden/.tmp-diff-summary.md")
    golden_path = Path("tests/ci/golden/diff_summary.md")

    try:
        subprocess.run(
            [
                "python3",
                "tools/ci/render_diff_summary.py",
                "--input",
                str(fixture),
                "--output",
                str(out_path),
            ],
            check=True,
        )

        assert out_path.read_text(encoding="utf-8") == golden_path.read_text(encoding="utf-8")
    finally:
        if out_path.exists():
            out_path.unlink()
