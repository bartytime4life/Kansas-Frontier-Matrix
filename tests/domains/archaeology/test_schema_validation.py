"""Every Archaeology schema is valid Draft 2020-12, and every schema with fields is tested.

Planned intent (docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md): Validate every archaeology schema in `schemas/contracts/v1/domains/archaeology/` parses and accepts / rejects fixtures correctly.

Most Archaeology schemas are PROPOSED scaffolds with no domain fields, or only
the generic id / spec_hash / version trio. The four schemas that define real
fields are each exercised against valid and invalid inputs by the test listed in
TESTED_SCHEMAS. A scaffold that gains fields without a test entry here fails
with SCHEMA_VALIDATION_NOT_IMPLEMENTED.
"""
from __future__ import annotations

import io
import json
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tools.validators.domains.archaeology.validate_schema import SCHEMA_ROOT, main as validate_schemas

REPO_ROOT = Path(__file__).resolve().parents[3]
GENERIC_FIELDS = {"id", "spec_hash", "version"}

# schema (relative to SCHEMA_ROOT) -> (test that exercises it, file that loads the schema)
TESTED_SCHEMAS = {
    "archaeological_volume_measurement_assessment.schema.json": (
        "tests/validators/domains/archaeology/test_validate_archaeological_volume_measurement_assessment.py",
        "tools/validators/domains/archaeology/validate_archaeological_volume_measurement_assessment.py",
    ),
    "candidate_feature.schema.json": (
        "tests/domains/archaeology/test_candidate_not_site.py",
        "tests/domains/archaeology/test_candidate_not_site.py",
    ),
    "three_d_documentation.schema.json": (
        "tests/validators/domains/archaeology/test_validate_three_d_documentation.py",
        "tools/validators/domains/archaeology/validate_three_d_documentation.py",
    ),
    "three_d_visibility_assumption_disclosure.schema.json": (
        "tests/validators/domains/archaeology/test_validate_three_d_visibility_assumption_disclosure.py",
        "tools/validators/domains/archaeology/validate_three_d_visibility_assumption_disclosure.py",
    ),
}


def schemas_with_fields(root: Path) -> list[str]:
    """Return schemas under root that define properties beyond the generic trio."""
    found = []
    for path in sorted(root.rglob("*.schema.json")):
        schema = json.loads(path.read_text(encoding="utf-8"))
        if set(schema.get("properties", {})) - GENERIC_FIELDS:
            found.append(path.relative_to(root).as_posix())
    return found


class ArchaeologySchemaValidationTests(unittest.TestCase):
    def test_every_archaeology_schema_is_valid_draft_2020_12(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            status = validate_schemas([])
        self.assertEqual(status, 0, output.getvalue())
        checked = output.getvalue().count("\nOK ") + output.getvalue().startswith("OK ")
        self.assertEqual(checked, len(list(SCHEMA_ROOT.rglob("*.schema.json"))))

    def test_every_schema_with_fields_has_a_validating_test(self) -> None:
        untested = sorted(set(schemas_with_fields(SCHEMA_ROOT)) - set(TESTED_SCHEMAS))
        self.assertEqual(
            untested,
            [],
            "SCHEMA_VALIDATION_NOT_IMPLEMENTED: these Archaeology schemas define fields but no test "
            "accepts valid and rejects invalid fixtures for them. Add that test and list it in "
            "TESTED_SCHEMAS.",
        )

    def test_listed_schema_tests_exist_and_load_their_schema(self) -> None:
        stale = sorted(set(TESTED_SCHEMAS) - set(schemas_with_fields(SCHEMA_ROOT)))
        self.assertEqual(stale, [], "TESTED_SCHEMAS lists schemas that no longer define fields.")
        for schema, (test, loader) in TESTED_SCHEMAS.items():
            self.assertTrue((REPO_ROOT / test).is_file(), f"{schema}: covering test {test} is missing")
            self.assertTrue(
                Path(schema).name in (REPO_ROOT / loader).read_text(encoding="utf-8"),
                f"{schema}: {loader} no longer loads this schema",
            )


if __name__ == "__main__":
    unittest.main()
