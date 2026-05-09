import json
from pathlib import Path

import pytest

from tools.validators._common.jsonschema_runner import load_validator

ROOT = Path(__file__).resolve().parents[2]
FAMILIES = ["evidence", "runtime", "common", "policy", "source", "governance", "release"]


def _schema_cases():
    cases = []
    for family in FAMILIES:
        for schema_path in sorted((ROOT / "schemas" / "contracts" / "v1" / family).glob("*.schema.json")):
            name = schema_path.name.replace(".schema.json", "")
            fixture_dir = ROOT / "fixtures" / "contracts" / "v1" / family / name
            if fixture_dir.exists():
                cases.append((family, name, schema_path, fixture_dir))
    return cases


@pytest.mark.parametrize("family,name,schema_path,fixture_dir", _schema_cases())
def test_contract_fixtures(family, name, schema_path, fixture_dir):
    validator = load_validator(schema_path)

    for valid_fp in sorted((fixture_dir / "valid").glob("valid_*.json")):
        errors = list(validator.iter_errors(json.loads(valid_fp.read_text(encoding="utf-8"))))
        assert not errors, f"{family}/{name} valid fixture failed: {valid_fp}"

    for invalid_fp in sorted((fixture_dir / "invalid").glob("invalid_*.json")):
        errors = list(validator.iter_errors(json.loads(invalid_fp.read_text(encoding="utf-8"))))
        assert errors, f"{family}/{name} invalid fixture passed: {invalid_fp}"
        expected_fp = invalid_fp.with_suffix(".expected_error.txt")
        if expected_fp.exists():
            expected = expected_fp.read_text(encoding="utf-8").strip().lower()
            combined = "\n".join(e.message.lower() for e in errors)
            assert expected in combined
