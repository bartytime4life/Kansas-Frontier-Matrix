from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators import validate_admin_boundary_change as validator

ROOT = Path(__file__).resolve().parents[2]


class AdminBoundaryChangeTests(unittest.TestCase):
    def test_schema_is_closed_valid_and_pins_inactive_profile(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual("AdminBoundaryChange", schema["properties"]["object_type"]["const"])
        self.assertEqual(
            "kfm.admin-boundary-change.fixture.v1",
            schema["properties"]["profile"]["const"],
        )

    def test_exact_fixture_matrix(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_positive_cases_cover_event_cardinality_and_crosswalk_postures(self) -> None:
        manifest = validator.load_fixtures()
        passing = [
            validator.materialize_case(manifest, case)
            for case in manifest["cases"]
            if case["expected_outcome"] == "PASS"
        ]
        self.assertEqual(
            {"BOUNDARY_REVISION", "SPLIT", "MERGER", "CREATION", "DISSOLUTION", "RENAME"},
            {item["change"]["change_type"] for item in passing},
        )
        self.assertEqual(
            {"NOT_APPLICABLE", "UNRESOLVED", "REFERENCED_NOT_RESOLVED"},
            {item["lineage"]["crosswalk_state"] for item in passing},
        )
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"PASS": 6, "DENY": 20}, outcomes)

    def test_creation_and_dissolution_have_explicit_empty_sides(self) -> None:
        manifest = validator.load_fixtures()
        cases = {case["case_id"]: case for case in manifest["cases"]}
        creation = validator.materialize_case(manifest, cases["valid-creation"])
        dissolution = validator.materialize_case(manifest, cases["valid-dissolution"])
        self.assertEqual([], creation["lineage"]["source_geography_version_refs"])
        self.assertEqual([], creation["lineage"]["predecessor_feature_refs"])
        self.assertEqual([], dissolution["lineage"]["target_geography_version_refs"])
        self.assertEqual([], dissolution["lineage"]["successor_feature_refs"])
        self.assertEqual("NOT_APPLICABLE", creation["lineage"]["crosswalk_state"])
        self.assertEqual("NOT_APPLICABLE", dissolution["lineage"]["crosswalk_state"])

    def test_fixture_has_no_geometry_names_observations_or_crosswalk_rows(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        keys: set[str] = set()

        def collect(value: object) -> None:
            if isinstance(value, dict):
                keys.update(value)
                for child in value.values():
                    collect(child)
            elif isinstance(value, list):
                for child in value:
                    collect(child)

        collect(document)
        forbidden = {"geometry", "coordinates", "name", "population", "observation", "mappings", "weight_millionths", "source_payload"}
        self.assertTrue(forbidden.isdisjoint(keys))
        governance = dict(document["governance"])
        self.assertEqual("FIXTURE_ONLY", governance.pop("execution_mode"))
        self.assertTrue(all(value is False for value in governance.values()))

    def test_identity_is_content_addressed_and_replay_stable(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        first = validator.canonical_identity(document)
        second = validator.canonical_identity(json.loads(json.dumps(document)))
        self.assertEqual(first, second)
        changed = json.loads(json.dumps(document))
        changed["change"]["effective_date"] = "1910-01-02"
        self.assertNotEqual(first, validator.canonical_identity(changed))

    def test_validation_does_not_open_network(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        with mock.patch("socket.socket", side_effect=AssertionError("network denied")):
            result = validator.validate_payload(document)
        self.assertEqual("PASS", result.outcome)
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "socket."):
            self.assertNotIn(token, source)

    def test_bounded_reader_rejects_duplicate_nonfinite_symlink_and_oversize(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            target = root / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = root / "link.json"
            link.symlink_to(target)
            oversized = root / "oversized.json"
            oversized.write_bytes(b" " * (validator.MAX_BYTES + 1))
            for path, code in (
                (duplicate, "ADMIN_BOUNDARY_JSON_DUPLICATE_KEY"),
                (nonfinite, "ADMIN_BOUNDARY_JSON_NONFINITE_NUMBER"),
                (link, "ADMIN_BOUNDARY_INPUT_SYMLINK_DENIED"),
                (oversized, "ADMIN_BOUNDARY_INPUT_TOO_LARGE"),
            ):
                with self.subTest(path=path.name):
                    value, findings = validator._read(path)
                    self.assertIsNone(value)
                    self.assertEqual(code, findings[0].code)

    def test_cli_fixture_replay_is_deterministic(self) -> None:
        command = [sys.executable, str(Path(validator.__file__)), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn('"cases":26', first.stdout)
        self.assertIn('"suite_match":true', first.stdout)

    def test_serialization_disclaims_authority_and_does_not_reflect_payload(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        sentinel = "do-not-echo-admin-boundary-value"
        document["change"]["jurisdiction_code"] = sentinel
        rendered = validator.serialize(Path("candidate.json"), validator.validate_payload(document))
        self.assertNotIn(sentinel, rendered)
        payload = json.loads(rendered)
        self.assertEqual("NONE", payload["authority"])
        self.assertIn("no_public_use_or_publication", payload["non_effects"])


if __name__ == "__main__":
    unittest.main()
