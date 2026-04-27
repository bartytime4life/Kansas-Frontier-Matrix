"""
Catalog emission tests for the KFM HUC12 ↔ admin crosswalk lane.

Requires PostGIS.

Run manually:

  KFM_CROSSWALK_TEST_DSN="postgresql://postgres:postgres@localhost:5432/postgres" \
  python3 -m pytest -q tests/crosswalk/test_crosswalk_catalog.py
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest
from jsonschema import validate


ROOT = Path(__file__).resolve().parents[2]
WATCHER_DIR = ROOT / "pipelines/watchers/hydrology_huc12_admin_crosswalk_watch"

FIXTURE_SQL = WATCHER_DIR / "fixtures/create_fixture.sql"
RUNNER = WATCHER_DIR / "runner.py"
EMIT_CATALOG = WATCHER_DIR / "emit_catalog.py"
MANIFEST_SCHEMA = ROOT / "schemas/contracts/v1/crosswalk/crosswalk_catalog_manifest.schema.json"


def require_command(name: str) -> None:
    if shutil.which(name) is None:
        pytest.skip(f"{name} is not installed")


def dsn() -> str:
    value = os.environ.get("KFM_CROSSWALK_TEST_DSN") or os.environ.get("DATABASE_URL")
    if not value:
        pytest.skip("KFM_CROSSWALK_TEST_DSN or DATABASE_URL is required")
    return value


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )


@pytest.mark.integration
def test_crosswalk_catalog_manifest_emits_and_validates() -> None:
    require_command("psql")
    require_command("python3")

    run_id = "pytest-crosswalk-catalog"

    run(["psql", dsn(), "-v", "ON_ERROR_STOP=1", "-f", str(FIXTURE_SQL)])

    run([
        "python3",
        str(RUNNER),
        "--dsn",
        dsn(),
        "--run-id",
        run_id,
        "--no-publish",
        "--replace-run",
    ])

    result = run([
        "python3",
        str(EMIT_CATALOG),
        "--dsn",
        dsn(),
        "--run-id",
        run_id,
        "--public-base-href",
        "https://example.invalid/kfm",
    ])

    manifest = json.loads(result.stdout)
    schema = json.loads(MANIFEST_SCHEMA.read_text(encoding="utf-8"))

    validate(instance=manifest, schema=schema)

    assert manifest["object_type"] == "crosswalk_catalog_manifest"
    assert manifest["record_count"] == 2
    assert manifest["publication"]["published"] is False

    for key in ["stac", "dcat", "prov"]:
        assert Path(manifest["catalog_outputs"][key]).exists()
