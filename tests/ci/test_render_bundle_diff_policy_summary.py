#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


def test_render_bundle_diff_policy_summary() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "diff-policy.json"
        out = root / "summary.md"
        src.write_text(
            json.dumps({"decision": "allow", "reasons": ["no breaking drift"]}),
            encoding="utf-8",
        )

        subprocess.run(
            [
                "python3",
                "tools/ci/render_bundle_diff_policy_summary.py",
                "--input",
                str(src),
                "--output",
                str(out),
            ],
            check=True,
        )

        rendered = out.read_text(encoding="utf-8")
        assert "Decision: **allow**" in rendered
        assert "no breaking drift" in rendered
