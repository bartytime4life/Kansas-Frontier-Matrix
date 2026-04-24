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

    assert proc.returncode == 2
    assert expected_stderr in proc.stderr


@pytest.mark.parametrize(
    ("missing_arg", "expected_stderr"),
    [
        ("--promotion", "render_promotion_review_handoff: promotion input not found"),
        ("--bundle", "render_promotion_review_handoff: bundle input not found"),
        ("--diff", "render_promotion_review_handoff: diff input not found"),
        ("--diff-policy", "render_promotion_review_handoff: diff-policy input not found"),
    ],
)
def test_review_handoff_renderer_fails_on_missing_required_input(
    missing_arg: str, expected_stderr: str
) -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        promotion = root / "promotion.json"
        bundle = root / "bundle.json"
        diff = root / "diff.json"
        diff_policy = root / "diff-policy.json"

        promotion.write_text('{"release_id":"r1","state":"approved"}', encoding="utf-8")
        bundle.write_text('{"bundle_id":"b1","artifacts":[]}', encoding="utf-8")
        diff.write_text('{"added":0,"changed":0,"removed":0}', encoding="utf-8")
        diff_policy.write_text('{"decision":"allow"}', encoding="utf-8")

        args = {
            "--promotion": str(promotion),
            "--bundle": str(bundle),
            "--diff": str(diff),
            "--diff-policy": str(diff_policy),
        }
        args[missing_arg] = "does-not-exist.json"

        proc = subprocess.run(
            [
                "python3",
                "tools/ci/render_promotion_review_handoff.py",
                "--promotion",
                args["--promotion"],
                "--bundle",
                args["--bundle"],
                "--diff",
                args["--diff"],
                "--diff-policy",
                args["--diff-policy"],
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode == 2
        assert expected_stderr in proc.stderr
