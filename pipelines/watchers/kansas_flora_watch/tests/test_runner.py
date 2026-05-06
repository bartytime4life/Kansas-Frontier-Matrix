from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from pipelines.watchers.kansas_flora_watch import runner


def test_build_receipt_shape() -> None:
    receipt = runner.build_receipt(dry_run=True)

    assert receipt["watcher_id"] == "kansas_flora_watch"
    assert receipt["status"] == "noop"
    assert receipt["dry_run"] is True
    assert isinstance(receipt["timestamp"], str)
    assert "Scaffold runner executed" in receipt["message"]


def test_runner_writes_receipt_file(tmp_path: Path) -> None:
    out = tmp_path / "receipt.json"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pipelines.watchers.kansas_flora_watch.runner",
            "--once",
            "--dry-run",
            "--receipt",
            str(out),
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert out.exists()

    on_disk = json.loads(out.read_text(encoding="utf-8"))
    from_stdout = json.loads(result.stdout)

    assert on_disk["watcher_id"] == "kansas_flora_watch"
    assert on_disk["dry_run"] is True
    assert on_disk == from_stdout
