"""Offline regression coverage for bounded NASA solar-data preparation."""
import copy
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sunlight_display", ROOT / "scripts/prepare-sunlight.py")
solar = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solar)
MANIFEST = json.loads((ROOT / "app/labs/sunlight-and-sky/snapshot-manifest.json").read_bytes())


def response():
    descriptor = MANIFEST["points"][0]
    snapshot = json.loads((ROOT / "public" / descriptor["url"].lstrip("/")).read_bytes())
    return {"type": "Feature", "geometry": {"type": "Point", "coordinates": descriptor["provider"]["returnedCoordinates"]},
            "properties": {"parameter": {
                code: {r["date"].replace("-", ""): r[field] for r in snapshot["records"]}
                for code, field in solar.CODES.items()}},
            "header": {"title": "NASA/POWER Source Native Resolution Daily Data", "api": descriptor["provider"]["api"],
                       "sources": ["SYN1DEG"], "fill_value": -999, "time_standard": "LST", "start": "20200101", "end": "20251231"},
            "messages": [], "parameters": solar.PARAMETERS}


def parse(value):
    return solar.parse_point(solar.encoded(value), solar.POINTS[0], MANIFEST["points"][0]["source"])


def test_complete_leap_calendar_and_source_values():
    value = response()
    result = parse(value)
    assert len(result["records"]) == 2192
    assert len([r for r in result["records"] if r["date"] == "2024-02-29"]) == 1
    for row in result["records"]:
        for code, field in solar.CODES.items():
            assert row[field] == value["properties"]["parameter"][code][row["date"].replace("-", "")]


def test_preserve_missing_zero_and_value_above_clear_sky():
    value = response()
    series = value["properties"]["parameter"]
    series["ALLSKY_SFC_SW_DWN"]["20200101"] = 0
    series["ALLSKY_SFC_SW_DWN"]["20200102"] = -999
    series["ALLSKY_SFC_SW_DWN"]["20200103"] = 10
    series["CLRSKY_SFC_SW_DWN"]["20200103"] = 5
    records = parse(value)["records"]
    assert [r["allSky"] for r in records[:3]] == [0, -999, 10]
    assert records[2]["clearSky"] == 5


@pytest.mark.parametrize("change", [
    lambda d: d["header"].update(time_standard="UTC"),
    lambda d: d["header"].update(sources=["FLASHFLUX"]),
    lambda d: d["header"].update(end="20261231"),
    lambda d: d["header"].update(fill_value=0),
    lambda d: d["parameters"]["ALLSKY_SFC_SW_DWN"].update(units="W/m2"),
    lambda d: d["geometry"].update(coordinates=[-97, 38, 300]),
    lambda d: d.update(geometry=None),
    lambda d: d["messages"].append("Parameter warning"),
    lambda d: d["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"].pop("20240229"),
    lambda d: d["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"].update({"20230229": 3}),
    lambda d: d["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"].update({"20200101": True}),
    lambda d: d["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"].update({"20200101": -0.1}),
    lambda d: d["properties"].update(parameter=[]),
])
def test_reject_changed_identity_clock_units_calendar_and_values(change):
    value = copy.deepcopy(response())
    change(value)
    with pytest.raises(ValueError):
        parse(value)


def test_duplicate_keys_and_nonfinite_json_are_rejected():
    for raw in (b'{"a":1,"a":2}', b'{"a":NaN}', b'{"a":Infinity}'):
        with pytest.raises(ValueError):
            solar.strict_json(raw)


def test_original_captures_cannot_be_inside_git_or_symlinked(tmp_path):
    with pytest.raises(ValueError):
        solar.private_path(ROOT / "capture")
    with pytest.raises(ValueError):
        solar.private_path(Path("relative"))
    target = tmp_path / "target"
    target.mkdir()
    link = tmp_path / "linked"
    link.symlink_to(target, target_is_directory=True)
    with pytest.raises(ValueError):
        solar.private_path(link)


def test_offline_receipt_rejects_unplanned_source_and_oversize(tmp_path, monkeypatch):
    monkeypatch.setattr(solar, "private_path", lambda p: Path(p))
    capture = tmp_path / "capture"
    capture.mkdir()
    (capture / "capture.json").write_bytes(solar.encoded({"schema": "kfm.sunlight-capture/v1", "sources": {"extra": {}}}))
    with pytest.raises(ValueError, match="plan"):
        solar.verified_sources(capture)
    (capture / "capture.json").write_bytes(b" " * (32 * 1024 + 1))
    with pytest.raises(ValueError, match="oversized"):
        solar.verified_sources(capture)
