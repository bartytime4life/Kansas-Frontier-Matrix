#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path


REQUIRED_FILES = [
    "tests/ci/fixtures/diff_summary/diff.json",
    "tests/ci/fixtures/diff_policy/diff_policy.json",
    "tests/ci/fixtures/promotion_summary/promotion.json",
    "tests/ci/fixtures/promotion_bundle/bundle.json",
    "tests/ci/fixtures/review_handoff/promotion.json",
    "tests/ci/fixtures/review_handoff/bundle.json",
    "tests/ci/fixtures/review_handoff/diff.json",
    "tests/ci/fixtures/review_handoff/diff_policy.json",
    "schemas/contracts/v1/runtime/renderers/diff_summary_input.schema.json",
    "schemas/contracts/v1/runtime/renderers/diff_policy_summary_input.schema.json",
    "schemas/contracts/v1/runtime/renderers/promotion_summary_input.schema.json",
    "schemas/contracts/v1/runtime/renderers/promotion_bundle_summary_input.schema.json",
    "schemas/contracts/v1/runtime/renderers/review_handoff_inputs.schema.json",
]


def test_validate_renderer_fixtures_passes_current_repo() -> None:
    subprocess.run(["python3", "tools/ci/validate_renderer_fixtures.py"], check=True)


def test_validate_renderer_fixtures_fails_on_invalid_fixture() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)

        for rel in REQUIRED_FILES:
            src = Path(rel)
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

        broken = root / "tests/ci/fixtures/diff_summary/diff.json"
        broken.write_text(json.dumps({"added": "bad", "changed": 2, "removed": 1}), encoding="utf-8")

        proc = subprocess.run(
            ["python3", "tools/ci/validate_renderer_fixtures.py", "--root", str(root)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode == 1
        assert "diff_summary.added: expected integer" in proc.stderr


def test_validate_renderer_fixtures_fails_on_non_utf8_fixture() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)

        for rel in REQUIRED_FILES:
            src = Path(rel)
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

        broken = root / "tests/ci/fixtures/diff_summary/diff.json"
        broken.write_bytes(b"\xff\xfe")

        proc = subprocess.run(
            ["python3", "tools/ci/validate_renderer_fixtures.py", "--root", str(root)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode == 1
        assert "invalid UTF-8 in" in proc.stderr
