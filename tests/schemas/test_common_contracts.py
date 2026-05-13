import json
import re
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
            if expected == "enum|pattern|date-time":
                assert (
                    "is not one of" in combined
                    or "does not match" in combined
                    or "is not a 'date-time'" in combined
                ), f"{family}/{name} expected enum|pattern|date-time style error in {combined!r}"
            elif expected == "enum":
                assert "is not one of" in combined, (
                    f"{family}/{name} expected enum error in {combined!r}"
                )
            elif "|" in expected:
                assert re.search(expected, combined), (
                    f"{family}/{name} expected error pattern not found: {expected!r} in {combined!r}"
                )
            else:
                for expected_line in [line.strip() for line in expected.splitlines() if line.strip()]:
                    normalized = expected_line.replace("$: ", "").replace("sha256: ", "")
                    assert normalized in combined, (
                        f"{family}/{name} expected error line not found: {normalized!r} in {combined!r}"
                    )
