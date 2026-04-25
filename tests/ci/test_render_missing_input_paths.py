#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

import pytest


def _write_review_handoff_inputs(root: Path) -> dict[str, Path]:
    promotion = root / "promotion.json"
    bundle = root / "bundle.json"
    diff = root / "diff.json"
    diff_policy = root / "diff-policy.json"

    promotion.write_text('{"release_id":"r1","state":"approved"}', encoding="utf-8")
    bundle.write_text('{"bundle_id":"b1","artifacts":[]}', encoding="utf-8")
    diff.write_text('{"added":0,"changed":0,"removed":0}', encoding="utf-8")
    diff_policy.write_text('{"decision":"allow"}', encoding="utf-8")

    return {
        "--promotion": promotion,
        "--bundle": bundle,
        "--diff": diff,
        "--diff-policy": diff_policy,
    }


def _run_review_handoff_renderer(
    args: dict[str, Path],
    overrides: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    cli_args = {flag: str(path) for flag, path in args.items()}
    cli_args.update(overrides or {})
    return subprocess.run(
        [
            "python3",
            "tools/ci/render_promotion_review_handoff.py",
            "--promotion",
            cli_args["--promotion"],
            "--bundle",
            cli_args["--bundle"],
            "--diff",
            cli_args["--diff"],
            "--diff-policy",
            cli_args["--diff-policy"],
        ],
        check=False,
        capture_output=True,
        text=True,
    )


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
    ("script", "expected_stderr"),
    [
        ("tools/ci/render_diff_summary.py", "render_diff_summary: input is not valid UTF-8"),
        (
            "tools/ci/render_bundle_diff_policy_summary.py",
            "render_bundle_diff_policy_summary: input is not valid UTF-8",
        ),
        ("tools/ci/render_promotion_summary.py", "render_promotion_summary: input is not valid UTF-8"),
        (
            "tools/ci/render_promotion_bundle_summary.py",
            "render_promotion_bundle_summary: input is not valid UTF-8",
        ),
    ],
)
def test_single_input_renderers_fail_on_non_utf8_input(script: str, expected_stderr: str) -> None:
    with tempfile.TemporaryDirectory() as td:
        bad = Path(td) / "bad.json"
        bad.write_bytes(b"\xff\xfe")

        proc = subprocess.run(
            ["python3", script, "--input", str(bad)],
            check=False,
            capture_output=True,
            text=True,
        )

    assert proc.returncode == 2
    assert expected_stderr in proc.stderr


@pytest.mark.parametrize(
    ("script", "expected_stderr"),
    [
        ("tools/ci/render_diff_summary.py", "render_diff_summary: unable to read input"),
        ("tools/ci/render_bundle_diff_policy_summary.py", "render_bundle_diff_policy_summary: unable to read input"),
        ("tools/ci/render_promotion_summary.py", "render_promotion_summary: unable to read input"),
        ("tools/ci/render_promotion_bundle_summary.py", "render_promotion_bundle_summary: unable to read input"),
    ],
)
def test_single_input_renderers_fail_on_unreadable_path(script: str, expected_stderr: str) -> None:
    with tempfile.TemporaryDirectory() as td:
        directory_input = Path(td)
        proc = subprocess.run(
            ["python3", script, "--input", str(directory_input)],
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
        args = _write_review_handoff_inputs(root)
        proc = _run_review_handoff_renderer(args, overrides={missing_arg: "does-not-exist.json"})

        assert proc.returncode == 2
        assert expected_stderr in proc.stderr


@pytest.mark.parametrize(
    ("bad_arg", "expected_stderr"),
    [
        ("--promotion", "render_promotion_review_handoff: promotion input is not valid UTF-8"),
        ("--bundle", "render_promotion_review_handoff: bundle input is not valid UTF-8"),
        ("--diff", "render_promotion_review_handoff: diff input is not valid UTF-8"),
        ("--diff-policy", "render_promotion_review_handoff: diff-policy input is not valid UTF-8"),
    ],
)
def test_review_handoff_renderer_fails_on_non_utf8_input(bad_arg: str, expected_stderr: str) -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        args = _write_review_handoff_inputs(root)
        args[bad_arg].write_bytes(b"\xff\xfe")
        proc = _run_review_handoff_renderer(args)

    assert proc.returncode == 2
    assert expected_stderr in proc.stderr


@pytest.mark.parametrize(
    ("bad_arg", "expected_stderr"),
    [
        ("--promotion", "render_promotion_review_handoff: unable to read promotion input"),
        ("--bundle", "render_promotion_review_handoff: unable to read bundle input"),
        ("--diff", "render_promotion_review_handoff: unable to read diff input"),
        ("--diff-policy", "render_promotion_review_handoff: unable to read diff-policy input"),
    ],
)
def test_review_handoff_renderer_fails_on_unreadable_input_path(
    bad_arg: str, expected_stderr: str
) -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        args = _write_review_handoff_inputs(root)
        proc = _run_review_handoff_renderer(args, overrides={bad_arg: str(root)})

    assert proc.returncode == 2
    assert expected_stderr in proc.stderr
