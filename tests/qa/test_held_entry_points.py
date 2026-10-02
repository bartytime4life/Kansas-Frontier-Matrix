"""Held worker, catalog, validator, and ingest-gate entry points stay non-authorizing and write nothing."""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]

HELD_ENTRY_POINTS = {
    "apps/workers/src/ai_focus_worker/main.py": {
        "reason_code": "AI_FOCUS_WORKER_NOT_IMPLEMENTED", "ai_focus_authorized": False},
    "apps/workers/src/correction_worker/main.py": {
        "reason_code": "CORRECTION_WORKER_NOT_IMPLEMENTED", "correction_authorized": False},
    "apps/workers/src/quarantine_review_worker/main.py": {
        "reason_code": "QUARANTINE_REVIEW_WORKER_NOT_IMPLEMENTED", "review_routing_authorized": False},
    "apps/workers/src/receipt_worker/main.py": {
        "reason_code": "RECEIPT_WORKER_NOT_IMPLEMENTED", "receipt_emission_authorized": False},
    "apps/workers/src/tile_worker/main.py": {
        "reason_code": "TILE_WORKER_NOT_IMPLEMENTED", "tile_build_authorized": False},
    "pipelines/catalog/main.py": {
        "reason_code": "CATALOG_NOT_IMPLEMENTED", "catalog_emission_authorized": False},
    "pipelines/domains/agriculture/catalog.py": {
        "reason_code": "CATALOG_NOT_IMPLEMENTED", "catalog_emission_authorized": False},
    "pipelines/domains/hazards/catalog.py": {
        "reason_code": "CATALOG_NOT_IMPLEMENTED", "catalog_emission_authorized": False},
    "pipelines/domains/roads-rail-trade/emit_catalog_records.py": {
        "reason_code": "CATALOG_NOT_IMPLEMENTED", "catalog_emission_authorized": False},
    "tools/ingest/hydrology/usgs_streamflow_gate.py": {
        "reason_code": "USGS_STREAMFLOW_GATE_NOT_IMPLEMENTED", "source_admission_authorized": False},
    "tools/validators/validate_catalog_matrix.py": {
        "reason_code": "CATALOG_MATRIX_VALIDATOR_NOT_IMPLEMENTED", "catalog_matrix_validated": False},
}


@pytest.mark.parametrize("relative", sorted(HELD_ENTRY_POINTS))
def test_entry_point_holds_without_writing(relative: str, tmp_path: Path) -> None:
    isolated = tmp_path / "repo" / relative
    isolated.parent.mkdir(parents=True)
    shutil.copyfile(ROOT / relative, isolated)

    completed = subprocess.run(
        [sys.executable, str(isolated)], cwd=tmp_path,
        capture_output=True, text=True, check=False, timeout=10,
    )

    assert completed.returncode == 2
    assert json.loads(completed.stdout) == {"outcome": "HOLD", **HELD_ENTRY_POINTS[relative]}
    assert completed.stderr == ""
    assert sorted(path.relative_to(tmp_path).as_posix() for path in tmp_path.rglob("*")
                  if path.is_file()) == [f"repo/{relative}"]


@pytest.mark.parametrize("relative", sorted(HELD_ENTRY_POINTS))
def test_entry_point_has_no_write_or_network_calls(relative: str) -> None:
    text = (ROOT / relative).read_text(encoding="utf-8")
    for marker in ("write_text(", "write_bytes(", "mkdir(", "open(", "urlopen(", "requests", "socket"):
        assert marker not in text, f"{relative} gained {marker!r}; review it as an implementation"


def test_backlog_projection_names_this_test_for_every_entry() -> None:
    spec = importlib.util.spec_from_file_location("kfm_completion_queue", ROOT / "tools/qa/completion_queue.py")
    assert spec and spec.loader
    queue = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(queue)
    projected = {path: reason for path, (reason, test) in queue.HELD_STAGE_PATHS.items()
                 if test == "tests/qa/test_held_entry_points.py"}
    assert projected == {path: envelope["reason_code"] for path, envelope in HELD_ENTRY_POINTS.items()}
