"""Offline fixed-width NOAA display-derivative parsing; no provider dependency."""
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("daily_climate_display", ROOT / "apps/site/source/scripts/prepare-daily-climate.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def line(year=2024, month=2, element="PRCP", station="USW00003928"):
    return f"{station}{year:04}{month:02}{element}" + "".join(f"{day:5d}T W" if day == 29 else f"{day:5d}  W" for day in range(1, 32))


def test_offline_parser_preserves_leap_day_raw_flags_and_explicit_missing_dates():
    rows = MODULE.parse_station((line() + "\n").encode(), "USW00003928")
    assert len(rows) == 2192
    leap = next(row for row in rows if row["date"] == "2024-02-29")
    assert leap["prcp"] == [29, "T", "", "W"]
    assert leap["tmax"] is None
    assert not any(row["date"] == "2024-02-30" for row in rows)
    assert rows[0] == {"date": "2020-01-01", "tmax": None, "tmin": None, "prcp": None}


@pytest.mark.parametrize("content", [line() + "\n" + line(), line(station="USW00013996"), line()[:-1], line(month=13)])
def test_parser_rejects_ambiguous_or_malformed_provider_records(content):
    with pytest.raises(ValueError):
        MODULE.parse_station(content.encode(), "USW00003928")
