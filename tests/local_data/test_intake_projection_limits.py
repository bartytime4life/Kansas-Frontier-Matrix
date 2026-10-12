"""Bounded projection sidecars through the actual loose-shapefile profiler."""
import io
import json
import os
import tracemalloc
from unittest.mock import patch
import zipfile

import pytest

from tests.local_data import intake_samples as samples
from tools.local_data import intake_profile


def loose_shapefile(directory):
    with zipfile.ZipFile(io.BytesIO(samples.shapefile_zip())) as archive:
        for name in archive.namelist():
            (directory / name).write_bytes(archive.read(name))
    return directory / "kgs_wells.shp"


@pytest.mark.parametrize("size", [65537, 512 * 1024 * 1024])
def test_oversized_projection_is_blocking_without_buffering(tmp_path, size):
    shp = loose_shapefile(tmp_path)
    with shp.with_suffix(".prj").open("wb") as handle:
        handle.truncate(size)  # Sparse file; no large payload allocation.
    tracemalloc.start()
    try:
        with patch("pathlib.Path.read_bytes", side_effect=AssertionError("unbounded read")):
            profile = intake_profile.profile_file(shp)
        _, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    assert peak < 1024 * 1024
    assert "format_reader_failed" in profile["issues"]
    assert profile["spatial"]["crs"] is None
    assert "crs_assumed_geographic" not in profile["issues"]


@pytest.mark.parametrize("size", [None, 65536])
def test_normal_and_limit_sized_projection_preserve_crs_and_dbf(tmp_path, size):
    shp = loose_shapefile(tmp_path)
    if size:
        with shp.with_suffix(".prj").open("ab") as handle:
            handle.write(b" " * (size - handle.tell()))
    # The DBF body is not subject to the projection metadata ceiling.
    with shp.with_suffix(".dbf").open("ab") as handle:
        handle.write(bytes(70000))
    profile = intake_profile.profile_file(shp)
    assert profile["format"]["kind"] == "shapefile"
    assert profile["spatial"]["crs"] == "EPSG:4269"
    assert profile["spatial"]["kansas"] == "inside"
    assert profile["structure"]["features"] == 3
    assert profile["structure"]["fields"] == ["WELL_ID", "DEPTH_FT", "DATE_DRILL"]
    assert "format_reader_failed" not in profile["issues"]


@pytest.mark.parametrize("kind", ["missing", "symlink", "directory", "fifo"])
def test_absent_or_nonregular_projection_is_not_read(tmp_path, kind):
    shp = loose_shapefile(tmp_path)
    prj = shp.with_suffix(".prj")
    prj.unlink()
    if kind == "symlink":
        target = tmp_path / "target"
        target.write_text('GEOGCS["GCS_North_American_1983"]')
        prj.symlink_to(target)
    elif kind == "directory":
        prj.mkdir()
    elif kind == "fifo":
        if not hasattr(os, "mkfifo"):
            pytest.skip("FIFO unavailable on this platform")
        os.mkfifo(prj)
    profile = intake_profile.profile_file(shp)
    assert "shapefile_missing_prj" in profile["issues"]
    assert "crs_assumed_geographic" in profile["issues"]
    assert profile["spatial"]["crs"] == "EPSG:4326"


def test_projection_replaced_by_symlink_before_open_fails_closed(tmp_path):
    from tools.local_data.file_io import read_regular

    shp = loose_shapefile(tmp_path)
    target = tmp_path / "target"
    target.write_text('GEOGCS["GCS_North_American_1983"]')

    def replace_then_read(path, limit):
        path.unlink()
        path.symlink_to(target)
        return read_regular(path, limit)

    with patch.object(intake_profile, "read_regular", side_effect=replace_then_read):
        profile = intake_profile.profile_file(shp)
    assert "format_reader_failed" in profile["issues"]
    assert profile["spatial"]["crs"] is None


def test_inbox_analysis_contains_oversized_sidecar_and_continues(tmp_path):
    from tools.local_data import intake
    from tools.local_data.manage import init_store

    root = tmp_path / "store"
    init_store(root)
    inbox = tmp_path / "inbox"
    inbox.mkdir()
    shp = loose_shapefile(inbox)
    with shp.with_suffix(".prj").open("wb") as handle:
        handle.truncate(65537)
    (inbox / "control.csv").write_bytes(samples.CSV)
    summary = intake.analyze(root, inbox=inbox)
    assert summary["state"] == "complete"
    with intake.open_index(root) as connection:
        rows = dict(connection.execute("SELECT relative_path, profile_json FROM items"))
    assert "format_reader_failed" in json.loads(rows[shp.name])["issues"]
    control = json.loads(rows["control.csv"])
    assert control["format"]["kind"] == "csv-points"
    assert "format_reader_failed" not in control["issues"]
