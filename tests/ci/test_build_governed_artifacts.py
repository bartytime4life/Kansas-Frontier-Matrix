#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


def test_build_governed_artifacts_emits_manifest_and_outputs(tmp_path: Path) -> None:
    out_dir = tmp_path / "governed"

    subprocess.run(
        [
            "python3",
            "tools/ci/build_governed_artifacts.py",
            "--root",
            ".",
            "--out-dir",
            str(out_dir),
        ],
        check=True,
    )

    manifest_path = out_dir / "manifest.json"
    assert manifest_path.is_file()

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    artifacts = manifest.get("artifacts")
    assert isinstance(artifacts, list)
    assert len(artifacts) == 5

    for item in artifacts:
        assert isinstance(item, dict)
        inputs = item.get("inputs")
        assert isinstance(inputs, dict)
        assert inputs
        output = item.get("output")
        assert isinstance(output, str)
        assert output.endswith(".md")
        assert Path(output).is_file()
        digest = item.get("sha256")
        assert isinstance(digest, str)
        assert len(digest) == 64
