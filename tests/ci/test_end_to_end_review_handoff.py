#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path


def test_end_to_end_review_handoff_golden() -> None:
    fixture_root = Path("tests/ci/fixtures/review_handoff")
    out_path = Path("tests/ci/golden/.tmp-review-handoff.md")
    golden_path = Path("tests/ci/golden/review_handoff.md")

    try:
        subprocess.run(
            [
                "python3",
                "tools/ci/render_promotion_review_handoff.py",
                "--promotion",
                str(fixture_root / "promotion.json"),
                "--bundle",
                str(fixture_root / "bundle.json"),
                "--diff",
                str(fixture_root / "diff.json"),
                "--diff-policy",
                str(fixture_root / "diff_policy.json"),
                "--output",
                str(out_path),
            ],
            check=True,
        )

        actual = out_path.read_text(encoding="utf-8")
        expected = golden_path.read_text(encoding="utf-8")
        assert actual == expected
    finally:
        if out_path.exists():
            out_path.unlink()
