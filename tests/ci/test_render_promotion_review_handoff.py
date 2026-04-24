#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


def test_render_promotion_review_handoff() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        promotion = root / "promotion.json"
        bundle = root / "bundle.json"
        diff = root / "diff.json"
        diff_policy = root / "diff-policy.json"
        out = root / "handoff.md"

        promotion.write_text(json.dumps({"release_id": "r1", "state": "approved"}), encoding="utf-8")
        bundle.write_text(json.dumps({"bundle_id": "b1", "artifacts": ["a", "b"]}), encoding="utf-8")
        diff.write_text(json.dumps({"added": 1, "changed": 0, "removed": 0}), encoding="utf-8")
        diff_policy.write_text(json.dumps({"decision": "allow"}), encoding="utf-8")

        subprocess.run(
            [
                "python3",
                "tools/ci/render_promotion_review_handoff.py",
                "--promotion",
                str(promotion),
                "--bundle",
                str(bundle),
                "--diff",
                str(diff),
                "--diff-policy",
                str(diff_policy),
                "--output",
                str(out),
            ],
            check=True,
        )

        rendered = out.read_text(encoding="utf-8")
        assert "Release: **r1**" in rendered
        assert "Diff policy decision: **allow**" in rendered


def test_render_promotion_review_handoff_missing_key_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        promotion = root / "promotion.json"
        bundle = root / "bundle.json"
        diff = root / "diff.json"
        diff_policy = root / "diff-policy.json"

        promotion.write_text(json.dumps({"release_id": "r1"}), encoding="utf-8")
        bundle.write_text(json.dumps({"bundle_id": "b1", "artifacts": ["a", "b"]}), encoding="utf-8")
        diff.write_text(json.dumps({"added": 1, "changed": 0, "removed": 0}), encoding="utf-8")
        diff_policy.write_text(json.dumps({"decision": "allow"}), encoding="utf-8")

        proc = subprocess.run(
            [
                "python3",
                "tools/ci/render_promotion_review_handoff.py",
                "--promotion",
                str(promotion),
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
        assert "missing required str key: state" in proc.stderr


def test_render_promotion_review_handoff_invalid_json_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        promotion = root / "promotion.json"
        bundle = root / "bundle.json"
        diff = root / "diff.json"
        diff_policy = root / "diff-policy.json"

        promotion.write_text(json.dumps({"release_id": "r1", "state": "approved"}), encoding="utf-8")
        bundle.write_text(json.dumps({"bundle_id": "b1", "artifacts": ["a", "b"]}), encoding="utf-8")
        diff.write_text("{not-json", encoding="utf-8")
        diff_policy.write_text(json.dumps({"decision": "allow"}), encoding="utf-8")

        proc = subprocess.run(
            [
                "python3",
                "tools/ci/render_promotion_review_handoff.py",
                "--promotion",
                str(promotion),
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
        assert "invalid JSON in diff input" in proc.stderr


def test_render_promotion_review_handoff_non_object_json_fails() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        promotion = root / "promotion.json"
        bundle = root / "bundle.json"
        diff = root / "diff.json"
        diff_policy = root / "diff-policy.json"

        promotion.write_text(json.dumps({"release_id": "r1", "state": "approved"}), encoding="utf-8")
        bundle.write_text("[]", encoding="utf-8")
        diff.write_text(json.dumps({"added": 1, "changed": 0, "removed": 0}), encoding="utf-8")
        diff_policy.write_text(json.dumps({"decision": "allow"}), encoding="utf-8")

        proc = subprocess.run(
            [
                "python3",
                "tools/ci/render_promotion_review_handoff.py",
                "--promotion",
                str(promotion),
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
        assert "expected top-level JSON object in bundle input" in proc.stderr
