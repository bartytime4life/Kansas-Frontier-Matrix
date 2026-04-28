#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path


def _run(*args: str) -> None:
    subprocess.run(["python3", *args], check=True)


def test_fixture_case_catalog_renders() -> None:
    diff_cases = sorted(Path("tests/ci/fixtures/diff_summary/cases").glob("*.json"))
    for case in diff_cases:
        _run("tools/ci/render_diff_summary.py", "--input", str(case))

    diff_policy_cases = sorted(Path("tests/ci/fixtures/diff_policy/cases").glob("*.json"))
    for case in diff_policy_cases:
        _run("tools/ci/render_bundle_diff_policy_summary.py", "--input", str(case))

    promotion_cases = sorted(Path("tests/ci/fixtures/promotion_summary/cases").glob("*.json"))
    for case in promotion_cases:
        _run("tools/ci/render_promotion_summary.py", "--input", str(case))

    bundle_cases = sorted(Path("tests/ci/fixtures/promotion_bundle/cases").glob("*.json"))
    for case in bundle_cases:
        _run("tools/ci/render_promotion_bundle_summary.py", "--input", str(case))

    review_case_roots = sorted(Path("tests/ci/fixtures/review_handoff/cases").glob("*"))
    for case_root in review_case_roots:
        _run(
            "tools/ci/render_promotion_review_handoff.py",
            "--promotion",
            str(case_root / "promotion.json"),
            "--bundle",
            str(case_root / "bundle.json"),
            "--diff",
            str(case_root / "diff.json"),
            "--diff-policy",
            str(case_root / "diff_policy.json"),
        )
