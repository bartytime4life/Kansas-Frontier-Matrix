#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


def test_render_diff_summary() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "diff.json"
        out = root / "summary.md"
        src.write_text(json.dumps({"added": 2, "changed": 3, "removed": 1}), encoding="utf-8")

        subprocess.run(
            ["python3", "tools/ci/render_diff_summary.py", "--input", str(src), "--output", str(out)],
            check=True,
        )

        rendered = out.read_text(encoding="utf-8")
        assert "Added: **2**" in rendered
        assert "Changed: **3**" in rendered
        assert "Removed: **1**" in rendered
