from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/evidence-resolver/src"
sys.path.insert(0, str(PACKAGE_SRC))

from evidence_resolver.core import evaluate_resolution_candidate  # noqa: E402


SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/evidence/runtime_evidence_resolution.schema.json"
)
CONTRACT_FIXTURES = (
    REPO_ROOT
    / "fixtures/contracts/v1/evidence/runtime_evidence_resolution"
)
RESOLVER_FIXTURES = REPO_ROOT / "fixtures/packages/evidence_resolver/v1alpha1"


class RuntimeEvidenceResolutionSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema)

    def _errors(self, payload: object) -> list[str]:
        return [
            error.message
            for error in sorted(
                self.validator.iter_errors(payload), key=lambda item: list(item.path)
            )
        ]

    def test_static_valid_fixtures_conform(self) -> None:
        paths = sorted((CONTRACT_FIXTURES / "valid").glob("*.json"))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual([], self._errors(payload))

    def test_static_invalid_fixtures_fail_closed(self) -> None:
        paths = sorted((CONTRACT_FIXTURES / "invalid").glob("*.json"))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertTrue(self._errors(payload))

    def test_every_checked_in_resolver_result_conforms(self) -> None:
        paths = sorted(RESOLVER_FIXTURES.rglob("*.json"))
        self.assertTrue(paths)
        statuses: set[str] = set()
        for path in paths:
            with self.subTest(path=path.relative_to(RESOLVER_FIXTURES).as_posix()):
                case = json.loads(path.read_text(encoding="utf-8"))
                payload = evaluate_resolution_candidate(case["request"]).as_dict()
                statuses.add(str(payload["status"]))
                self.assertEqual([], self._errors(payload))
        self.assertEqual({"RESOLVED", "UNRESOLVED", "DENIED", "ERROR"}, statuses)

    def test_nonresolved_results_never_expose_bundle_identity(self) -> None:
        for path in sorted(RESOLVER_FIXTURES.rglob("*.json")):
            case = json.loads(path.read_text(encoding="utf-8"))
            payload = evaluate_resolution_candidate(case["request"]).as_dict()
            if payload["status"] != "RESOLVED":
                with self.subTest(path=path.name, status=payload["status"]):
                    self.assertIsNone(payload["bundle_id"])
                    self.assertTrue(payload["issues"])

    def test_authority_guard_is_literal_false(self) -> None:
        for path in sorted((CONTRACT_FIXTURES / "valid").glob("*.json")):
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertIs(payload["authoritative"], False)


if __name__ == "__main__":
    unittest.main()
