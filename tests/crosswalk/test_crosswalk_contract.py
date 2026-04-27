import json
import subprocess
from pathlib import Path

import pytest
from jsonschema import validate, ValidationError


ROOT = Path(__file__).resolve().parents[2]

SCHEMA_PATH = ROOT / "schemas/contracts/v1/crosswalk/crosswalk_pair.schema.json"

VALID_FIXTURE = ROOT / "tests/fixtures/crosswalk/valid/crosswalk_pair.valid.json"
INVALID_CRS_FIXTURE = ROOT / "tests/fixtures/crosswalk/invalid/crosswalk_pair.bad_crs.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def schema():
    return load_json(SCHEMA_PATH)


def test_valid_fixture_passes_schema(schema):
    data = load_json(VALID_FIXTURE)
    validate(instance=data, schema=schema)


def test_invalid_crs_fails_schema(schema):
    data = load_json(INVALID_CRS_FIXTURE)

    # JSON schema should NOT catch CRS error (policy should)
    validate(instance=data, schema=schema)


def opa_available():
    try:
        subprocess.run(["opa", "version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


@pytest.mark.skipif(not opa_available(), reason="OPA not installed")
def test_policy_valid_allows():
    data = load_json(VALID_FIXTURE)

    result = subprocess.run(
        ["opa", "eval", "-i", "-", "-d", str(ROOT / "policy/crosswalk"), "data.kfm.crosswalk.allow"],
        input=json.dumps(data),
        text=True,
        capture_output=True,
        check=True,
    )

    assert "true" in result.stdout


@pytest.mark.skipif(not opa_available(), reason="OPA not installed")
def test_policy_bad_crs_denies():
    data = load_json(INVALID_CRS_FIXTURE)

    result = subprocess.run(
        ["opa", "eval", "-i", "-", "-d", str(ROOT / "policy/crosswalk"), "data.kfm.crosswalk.deny"],
        input=json.dumps(data),
        text=True,
        capture_output=True,
        check=True,
    )

    assert "crosswalk must use EPSG:5070" in result.stdout
