"""Every Flora schema is valid Draft 2020-12, and every schema with fields is tested.

Planned intent (docs/domains/flora/MISSING_OR_PLANNED_FILES.md): All Flora object-family schemas accept valid / reject invalid fixtures.

Most Flora schemas are PROPOSED scaffolds with no domain fields, or only the
generic id / spec_hash / version trio. The seven schemas that define real
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

from tools.validators.domains.flora.validate_schema import SCHEMA_ROOT, main as validate_schemas

REPO_ROOT = Path(__file__).resolve().parents[3]
GENERIC_FIELDS = {"id", "spec_hash", "version"}

# schema (relative to SCHEMA_ROOT) -> (test that exercises it, file that loads the schema)
TESTED_SCHEMAS = {
    "flora_occurrence_candidate.schema.json": (
        "tests/packages/domains/flora/normalizers/test_dwc_occurrence.py",
        "tests/packages/domains/flora/normalizers/test_dwc_occurrence.py",
    ),
    "flora_occurrence_intake_decision.schema.json": (
        "tests/packages/domains/flora/normalizers/test_intake_governance.py",
        "tests/packages/domains/flora/normalizers/test_intake_governance.py",
    ),
    "inaturalist_ingest_candidate.schema.json": (
        "tests/pipelines/domains/flora/test_inaturalist_ingest.py",
        "pipelines/domains/flora/inaturalist_ingest.py",
    ),
    "specimen_record.schema.json": (
        "tests/domains/flora/test_specimen_record.py",
        "tools/validators/domains/flora/validate_specimen_record.py",
    ),
    "usda_plants_distribution_snapshot.schema.json": (
        "tests/domains/flora/test_usda_plants_distribution_snapshot.py",
        "tools/validators/domains/flora/validate_usda_plants_distribution_snapshot.py",
    ),
    "source_readiness/materiality_candidate.schema.json": (
        "tests/validators/domains/flora/test_source_readiness_materiality.py",
        "tools/validators/domains/flora/validate_source_readiness_materiality.py",
    ),
    "source_readiness/materiality_profile.schema.json": (
        "tests/validators/domains/flora/test_source_readiness_materiality.py",
        "tools/validators/domains/flora/validate_source_readiness_materiality.py",
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


class FloraSchemaValidationTests(unittest.TestCase):
    def test_every_flora_schema_is_valid_draft_2020_12(self) -> None:
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
            "SCHEMA_VALIDATION_NOT_IMPLEMENTED: these Flora schemas define fields but no test "
            "accepts valid and rejects invalid fixtures for them. Add that test and list it in "
            "TESTED_SCHEMAS.",
        )

    def test_listed_schema_tests_exist_and_load_their_schema(self) -> None:
        stale = sorted(set(TESTED_SCHEMAS) - set(schemas_with_fields(SCHEMA_ROOT)))
        self.assertEqual(stale, [], "TESTED_SCHEMAS lists schemas that no longer define fields.")
        for schema, (test, loader) in TESTED_SCHEMAS.items():
            self.assertTrue((REPO_ROOT / test).is_file(), f"{schema}: covering test {test} is missing")
            self.assertIn(
                Path(schema).name,
                (REPO_ROOT / loader).read_text(encoding="utf-8"),
                f"{schema}: {loader} no longer loads this schema",
            )


if __name__ == "__main__":
    unittest.main()
