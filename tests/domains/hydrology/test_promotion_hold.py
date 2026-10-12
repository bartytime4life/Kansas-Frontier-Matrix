"""Hydrology's executable promotion entry point must remain non-authorizing."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[3] / "pipelines/domains/hydrology/promote.py"


def test_promotion_entry_point_holds_without_writing(tmp_path: Path) -> None:
    isolated = tmp_path / "repo/pipelines/domains/hydrology/promote.py"
    isolated.parent.mkdir(parents=True)
    shutil.copyfile(SOURCE, isolated)

    completed = subprocess.run(
        [sys.executable, str(isolated)], cwd=tmp_path,
        capture_output=True, text=True, check=False, timeout=10,
    )

    assert completed.returncode == 2
    assert json.loads(completed.stdout) == {
        "outcome": "HOLD",
        "reason_code": "PROMOTION_NOT_IMPLEMENTED",
        "promotion_authorized": False,
    }
    assert completed.stderr == ""
    assert sorted(path.relative_to(tmp_path).as_posix() for path in tmp_path.rglob("*")
                  if path.is_file()) == ["repo/pipelines/domains/hydrology/promote.py"]
