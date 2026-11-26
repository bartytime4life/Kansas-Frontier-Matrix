"""Offline scientific parsing and source-integrity checks; fixtures are synthetic."""
import csv
from datetime import date, timedelta
import importlib.util
import io
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("drought_and_soil_display", ROOT / "apps/site/source/scripts/prepare-drought-and-soil.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def drought_csv():
    stream = io.StringIO()
    writer = csv.writer(stream)
    writer.writerow(["MapDate", "FIPS", "County", "State", "None", "D0", "D1", "D2", "D3", "D4", "ValidStart", "ValidEnd", "StatisticFormatID"])
    for fips in sorted(MODULE.COUNTIES):
        for day in MODULE.tuesdays(2024):
            writer.writerow([day.replace("-", ""), fips, "Synthetic County", "KS", "20.00", "80.00", "50.00", "20.00", "10.00", "0.00", day, (date.fromisoformat(day) + timedelta(days=6)).isoformat(), "1"])
    return stream.getvalue().encode()


def soil_rows():
    out = []
    for number in range(366):
        day = date(2024, 1, 1) + timedelta(days=number)
        row = ["03067", day.strftime("%Y%m%d"), "-9.000" if number == 0 else "2.622", "-100.96", "38.87", *("0.0" for _ in range(13)),
               "0.000", "0.200", "-99.000", "0.300", "0.400", "0.0", "-9999.0", "-1.0", "1.0", "2.0"]
        out.append(" ".join(row))
    return ("\n".join(out) + "\n").encode()


def test_drought_annual_window_uses_first_tuesday_not_overlapping_previous_year():
    plan = MODULE.plans()[4]
    assert "startdate=1%2F2%2F2024" in plan[1]
    names, rows = MODULE.parse_drought(drought_csv(), 2024)
    assert len(names) == 105 and len(rows) == 105 * 53
    assert rows[("20055", "2024-12-31")] == [20, 80, 50, 20, 10, 0]


@pytest.mark.parametrize("mutate", [
    lambda raw: raw.replace(b",1\r\n", b",2\r\n", 1),
    lambda raw: raw.replace(b",80.00,50.00,", b",40.00,50.00,", 1),
    lambda raw: raw.replace(b",20.00,80.00,", b",19.00,80.00,", 1),
    lambda raw: raw.replace(b",KS,", b",NE,", 1),
    lambda raw: raw + raw.splitlines(keepends=True)[1],
    lambda raw: b"\n".join(raw.splitlines()[:-1]),
    lambda raw: raw.replace(b"2024-01-02", b"2024-01-03", 1),
])
def test_drought_rejects_wrong_format_overlap_duplicate_truncation_or_identity(mutate):
    with pytest.raises(ValueError):
        MODULE.parse_drought(mutate(drought_csv()), 2024)


def test_soil_preserves_five_depths_zero_sentinels_leap_day_and_missing_version_text():
    rows, coordinates = MODULE.parse_soil(soil_rows(), "03067", 2024)
    assert len(rows) == 366 and "2024-02-29" in rows
    assert coordinates == (-100.96, 38.87)
    assert rows["2024-01-01"]["version"] == "-9.000"
    assert rows["2024-01-01"]["moisture"] == ["0.000", "0.200", "-99.000", "0.300", "0.400"]
    assert rows["2024-01-01"]["temperature"] == ["0.0", "-9999.0", "-1.0", "1.0", "2.0"]


@pytest.mark.parametrize("mutate", [
    lambda raw: raw.replace(b"03067", b"53974", 1),
    lambda raw: raw + raw.splitlines(keepends=True)[0],
    lambda raw: b"\n".join(raw.splitlines()[:-1]),
    lambda raw: raw.replace(b"20240229", b"20240230", 1),
    lambda raw: raw.replace(b"-100.96", b"-110.96", 1),
    lambda raw: raw.replace(b"0.200", b"0.2oops", 1),
])
def test_soil_rejects_wrong_station_duplicate_missing_calendar_bad_coordinate_or_token(mutate):
    with pytest.raises(ValueError):
        MODULE.parse_soil(mutate(soil_rows()), "03067", 2024)


def test_offline_sources_require_exact_scope_url_size_and_digest(tmp_path):
    pages = []
    for key, url, _ in MODULE.plans():
        raw = b"synthetic capture bytes\n"
        (tmp_path / key).write_bytes(raw)
        pages.append({"key": key, "url": url, "bytes": len(raw), "sha256": MODULE.sha(raw), "capturedAt": "2026-11-26T00:00:00Z"})
    receipt = {"schema": "kfm.historical-science-capture/v1", "pages": pages}
    (tmp_path / "capture.json").write_text(json.dumps(receipt))
    assert len(MODULE.verified(tmp_path)) == 20
    (tmp_path / pages[0]["key"]).write_bytes(b"changed bytes")
    with pytest.raises(ValueError, match="CAPTURE_DIGEST_MISMATCH"):
        MODULE.verified(tmp_path)
