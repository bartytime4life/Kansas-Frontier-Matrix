import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools" / "validators" / "air_quality" / "validate_airnow_layer1.py"
FIXTURES = ROOT / "tests" / "fixtures" / "air_quality" / "airnow"


def _run(path: Path):
    return subprocess.run([sys.executable, str(VALIDATOR), str(path)], capture_output=True, text=True)


def test_valid_observation_passes():
    out = _run(FIXTURES / "valid" / "observation_wichita_pm25.json")
    assert out.returncode == 0


def test_valid_forecast_passes():
    out = _run(FIXTURES / "valid" / "forecast_wichita_ozone.json")
    assert out.returncode == 0


def test_valid_manifest_passes():
    out = _run(FIXTURES / "valid" / "intake_manifest_fixture_only.json")
    assert out.returncode == 0


def test_unknown_pollutant_fails():
    out = _run(FIXTURES / "invalid" / "observation_unknown_pollutant.json")
    assert out.returncode != 0


def test_missing_forecast_date_fails():
    out = _run(FIXTURES / "invalid" / "forecast_missing_date_forecast.json")
    assert out.returncode != 0


def test_bulk_zip_loop_manifest_fails():
    out = _run(FIXTURES / "invalid" / "intake_manifest_bulk_zip_loop.json")
    assert out.returncode != 0


def test_category_aqi_mismatch_fails(tmp_path: Path):
    src = json.loads((FIXTURES / "valid" / "observation_wichita_pm25.json").read_text())
    src["aqi"] = 180
    test_file = tmp_path / "category_mismatch.json"
    test_file.write_text(json.dumps(src))
    out = _run(test_file)
    assert out.returncode != 0


def test_preliminary_data_false_fails(tmp_path: Path):
    src = json.loads((FIXTURES / "valid" / "forecast_wichita_ozone.json").read_text())
    src["preliminary_data"] = False
    test_file = tmp_path / "prelim_false.json"
    test_file.write_text(json.dumps(src))
    out = _run(test_file)
    assert out.returncode != 0


def test_no_network_false_fails(tmp_path: Path):
    src = json.loads((FIXTURES / "valid" / "intake_manifest_fixture_only.json").read_text())
    src["no_network"] = False
    test_file = tmp_path / "no_network_false.json"
    test_file.write_text(json.dumps(src))
    out = _run(test_file)
    assert out.returncode != 0
