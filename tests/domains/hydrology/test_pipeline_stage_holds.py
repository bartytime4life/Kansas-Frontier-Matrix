"""Hydrology's held pipeline stage entry points must stay non-authorizing and write nothing."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

PIPELINE_ROOT = Path(__file__).resolve().parents[3] / "pipelines/domains/hydrology"

HELD_STAGES = {
    "ingest.py": {"reason_code": "INGEST_NOT_IMPLEMENTED", "ingestion_authorized": False},
    "publish.py": {"reason_code": "PUBLISH_NOT_IMPLEMENTED", "publication_authorized": False},
    "rollback.py": {"reason_code": "ROLLBACK_NOT_IMPLEMENTED", "rollback_authorized": False},
    "triplets.py": {"reason_code": "TRIPLETS_NOT_IMPLEMENTED", "triplet_emission_authorized": False},
}


@pytest.mark.parametrize("name", sorted(HELD_STAGES))
def test_stage_entry_point_holds_without_writing(name: str, tmp_path: Path) -> None:
    isolated = tmp_path / "repo/pipelines/domains/hydrology" / name
    isolated.parent.mkdir(parents=True)
    shutil.copyfile(PIPELINE_ROOT / name, isolated)

    completed = subprocess.run(
        [sys.executable, str(isolated)], cwd=tmp_path,
        capture_output=True, text=True, check=False, timeout=10,
    )

    assert completed.returncode == 2
    assert json.loads(completed.stdout) == {"outcome": "HOLD", **HELD_STAGES[name]}
    assert completed.stderr == ""
    assert sorted(path.relative_to(tmp_path).as_posix() for path in tmp_path.rglob("*")
                  if path.is_file()) == [f"repo/pipelines/domains/hydrology/{name}"]


@pytest.mark.parametrize("name", sorted(HELD_STAGES))
def test_stage_entry_point_has_no_write_or_network_calls(name: str) -> None:
    text = (PIPELINE_ROOT / name).read_text(encoding="utf-8")
    for marker in ("write_text(", "write_bytes(", "mkdir(", "open(", "urlopen(", "requests", "socket"):
        assert marker not in text, f"{name} gained {marker!r}; review it as an implementation"
