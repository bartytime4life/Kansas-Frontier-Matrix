import json
import re
from pathlib import Path
from typing import Any

import pytest

from tools.validators._common.jsonschema_runner import load_validator

ROOT = Path(__file__).resolve().parents[2]
FAMILIES = ["evidence", "runtime", "common", "policy", "source", "governance", "release"]


def _schema_cases():
    cases = []
    for family in FAMILIES:
        for schema_path in sorted(
            (ROOT / "schemas" / "contracts" / "v1" / family).glob("*.schema.json")
        ):
            name = schema_path.name.replace(".schema.json", "")
            fixture_dir = ROOT / "fixtures" / "contracts" / "v1" / family / name
            if fixture_dir.exists():
                cases.append((family, name, schema_path, fixture_dir))
    return cases


def _json_pointer(parts: Any) -> str:
    values = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(values) if values else "/"


def _assert_structured_schema_expectation(errors, expected, *, label: str) -> None:
    allowed = {"kind", "field", "keyword", "contains"}
    assert set(expected) <= allowed, f"{label} has unsupported sidecar keys"
    assert expected.get("kind") == "schema", f"{label} kind must be schema"

    field = expected.get("field")
    keyword = expected.get("keyword")
    contains = expected.get("contains")
    assert isinstance(field, str) and field.startswith("/"), (
        f"{label} field must be a JSON Pointer"
    )
    assert isinstance(keyword, str) and keyword, f"{label} keyword must be nonempty"
    assert contains is None or (isinstance(contains, str) and contains), (
        f"{label} contains must be a nonempty string when present"
    )

    contains_lower = contains.lower() if isinstance(contains, str) else None
    matched = any(
        _json_pointer(error.absolute_path) == field
        and (error.validator or "schema") == keyword
        and (
            contains_lower is None
            or contains_lower in error.message.lower()
        )
        for error in errors
    )
    assert matched, (
        f"{label} expected field={field!r}, keyword={keyword!r}, "
        f"contains={contains!r}; got "
        f"{[(_json_pointer(error.absolute_path), error.validator, error.message) for error in errors]!r}"
    )


def _assert_expected_error(errors, expected_text: str, *, label: str) -> None:
    stripped = expected_text.strip()
    assert stripped, f"{label} expected-error sidecar is empty"

    if stripped.startswith("{"):
        try:
            expected = json.loads(stripped)
        except json.JSONDecodeError as exc:
            raise AssertionError(f"{label} structured sidecar is invalid JSON") from exc
        assert isinstance(expected, dict), f"{label} structured sidecar must be an object"
        _assert_structured_schema_expectation(errors, expected, label=label)
        return

    expected = stripped.lower()
    combined = "\n".join(error.message.lower() for error in errors)
    if expected == "enum|pattern|date-time":
        assert (
            "is not one of" in combined
            or "does not match" in combined
            or "is not a 'date-time'" in combined
        ), f"{label} expected enum|pattern|date-time style error in {combined!r}"
    elif expected == "enum":
        assert "is not one of" in combined, (
            f"{label} expected enum error in {combined!r}"
        )
    elif "|" in expected:
        assert re.search(expected, combined), (
            f"{label} expected error pattern not found: {expected!r} in {combined!r}"
        )
    else:
        for expected_line in [
            line.strip() for line in expected.splitlines() if line.strip()
        ]:
            normalized = expected_line.replace("$: ", "").replace("sha256: ", "")
            assert normalized in combined, (
                f"{label} expected error line not found: {normalized!r} in {combined!r}"
            )


@pytest.mark.parametrize("family,name,schema_path,fixture_dir", _schema_cases())
def test_contract_fixtures(family, name, schema_path, fixture_dir):
    validator = load_validator(schema_path)

    for valid_fp in sorted((fixture_dir / "valid").glob("valid_*.json")):
        errors = list(
            validator.iter_errors(json.loads(valid_fp.read_text(encoding="utf-8")))
        )
        assert not errors, f"{family}/{name} valid fixture failed: {valid_fp}"

    for invalid_fp in sorted((fixture_dir / "invalid").glob("invalid_*.json")):
        errors = list(
            validator.iter_errors(json.loads(invalid_fp.read_text(encoding="utf-8")))
        )
        assert errors, f"{family}/{name} invalid fixture passed: {invalid_fp}"
        expected_fp = invalid_fp.with_suffix(".expected_error.txt")
        if expected_fp.exists():
            _assert_expected_error(
                errors,
                expected_fp.read_text(encoding="utf-8"),
                label=f"{family}/{name}/{invalid_fp.name}",
            )
