#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path


def test_end_to_end_promotion_bundle_summary_golden() -> None:
    fixture = Path("tests/ci/fixtures/promotion_bundle/bundle.json")
    out_path = Path("tests/ci/golden/.tmp-promotion-bundle-summary.md")
    golden_path = Path("tests/ci/golden/promotion_bundle_summary.md")

    try:
        subprocess.run(
            [
                "python3",
                "tools/ci/render_promotion_bundle_summary.py",
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
