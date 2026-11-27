"""Meaningful parser/integrity regression cases, independent of live EPA access."""
from __future__ import annotations

import csv
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import zipfile

import pytest

SPEC = importlib.util.spec_from_file_location("daily_air_quality_display", Path(__file__).resolve().parents[1] / "scripts/prepare-daily-air-quality.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def archive(rows, *, name="daily_aqi_by_county_2024.csv", header=None, extra=False):
    text = io.StringIO(newline="")
    writer = csv.writer(text)
    writer.writerows([MODULE.HEADER if header is None else header, *rows])
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zipped:
        zipped.writestr(name, text.getvalue())
        if extra:
            zipped.writestr("extra.csv", "unexpected")
    return output.getvalue()


def row(**changes):
    values = {"State Name": "Kansas", "county Name": "Sedgwick", "State Code": "20", "County Code": "173", "Date": "2024-02-29", "AQI": "0", "Category": "Good", "Defining Parameter": "PM2.5", "Defining Site": "20-173-0010", "Number of Sites Reporting": "2"}
    values.update(changes)
    return [values[key] for key in MODULE.HEADER]


def test_zero_is_reported_and_only_kansas_rows_are_kept():
    other = row(**{"State Name": "Colorado", "State Code": "08"})
    records, encoding = MODULE.county_rows(archive([other, row()]), 2024, 2)
    assert encoding == "utf-8-sig"
    assert records == [("20173", "Sedgwick", "2024-02-29", ["0", "Good", "PM2.5", "20-173-0010", "2", 3])]


@pytest.mark.parametrize("changes", [
    {"Date": "2024-02-30"}, {"Date": "2023-02-28"}, {"County Code": "174"}, {"State Name": "Elsewhere"},
    {"AQI": ""}, {"AQI": "-1"}, {"AQI": "2.5"}, {"AQI": "101", "Category": "Good"},
    {"Number of Sites Reporting": "0"}, {"Number of Sites Reporting": ""}, {"Defining Parameter": "unknown"},
    {"Defining Site": "=FORMULA()"}, {"Defining Site": "20-091-0010"},
])
def test_invalid_kansas_values_are_not_silently_published(changes):
    with pytest.raises(ValueError):
        MODULE.county_rows(archive([row(**changes)]), 2024, 1)


def test_duplicate_county_date_and_incomplete_national_file_are_rejected():
    with pytest.raises(ValueError, match="Duplicate"):
        MODULE.county_rows(archive([row(), row()]), 2024, 2)
    with pytest.raises(ValueError, match="row count"):
        MODULE.county_rows(archive([row()]), 2024, 2)


@pytest.mark.parametrize("options", [{"name": "../source.csv"}, {"extra": True}, {"header": ["changed"]}])
def test_archive_layout_and_exact_header_are_enforced(options):
    with pytest.raises(ValueError):
        MODULE.county_rows(archive([row()], **options), 2024, 1)


def test_decompression_budget_is_enforced(monkeypatch):
    monkeypatch.setattr(MODULE, "MAX_MEMBER", 10)
    with pytest.raises(ValueError, match="oversized"):
        MODULE.county_rows(archive([row()]), 2024, 1)


def test_source_receipt_rejects_tampering_and_symlink_inputs():
    with tempfile.TemporaryDirectory(prefix="kfm-aqi-parser-", dir="/var/tmp") as folder:
        root = Path(folder)
        sources = {}
        for name in MODULE.PLAN:
            raw = b"public fixture"
            (root / name).write_bytes(raw)
            sources[name] = {"url": MODULE.BASE + name, "bytes": len(raw), "sha256": MODULE.sha(raw), "capturedAt": "2026-11-26T00:00:00Z", "lastModified": None}
        (root / "capture.json").write_text(json.dumps({"schema": "kfm.daily-air-quality-capture/v1", "sources": sources}))
        assert len(MODULE.verified_sources(root)) == 8
        (root / "file_list.csv").write_bytes(b"changed")
        with pytest.raises(ValueError, match="integrity"):
            MODULE.verified_sources(root)
        (root / "file_list.csv").unlink()
        (root / "file_list.csv").symlink_to(root / "FileFormats.html")
        with pytest.raises(ValueError, match="linked"):
            MODULE.verified_sources(root)


def test_capture_refuses_an_existing_directory_or_repository_destination():
    with tempfile.TemporaryDirectory(prefix="kfm-aqi-parser-", dir="/var/tmp") as folder:
        with pytest.raises(ValueError, match="already exists"):
            MODULE.capture(Path(folder))
    with pytest.raises(ValueError, match="outside Git"):
        MODULE.private_path(MODULE.ROOT / "private-capture")
