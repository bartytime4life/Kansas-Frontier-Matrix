#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    ("script", "args", "expected_stderr"),
    [
        (
            "tools/ci/render_diff_summary.py",
            ["--input", "does-not-exist.json"],
            "render_diff_summary: input not found",
        ),
        (
            "tools/ci/render_bundle_diff_policy_summary.py",
            ["--input", "does-not-exist.json"],
            "render_bundle_diff_policy_summary: input not found",
        ),
        (
            "tools/ci/render_promotion_summary.py",
            ["--input", "does-not-exist.json"],
            "render_promotion_summary: input not found",
        ),
        (
            "tools/ci/render_promotion_bundle_summary.py",
            ["--input", "does-not-exist.json"],
            "render_promotion_bundle_summary: input not found",
        ),
    ],
)
def test_single_input_renderers_fail_on_missing_input(script: str, args: list[str], expected_stderr: str) -> None:
    proc = subprocess.run(
        ["python3", script, *args],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode != 0
    assert expected_stderr in proc.stderr


def test_review_handoff_renderer_fails_on_missing_promotion_input() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        bundle = root / "bundle.json"
        diff = root / "diff.json"
        diff_policy = root / "diff-policy.json"

        bundle.write_text('{"bundle_id":"b1","artifacts":[]}', encoding="utf-8")
        diff.write_text('{"added":0,"changed":0,"removed":0}', encoding="utf-8")
        diff_policy.write_text('{"decision":"allow"}', encoding="utf-8")

        proc = subprocess.run(
            [
                "python3",
                "tools/ci/render_promotion_review_handoff.py",
                "--promotion",
                "does-not-exist.json",
                "--bundle",
                str(bundle),
                "--diff",
                str(diff),
                "--diff-policy",
                str(diff_policy),
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "render_promotion_review_handoff: promotion input not found" in proc.stderr
