from __future__ import annotations

import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.domains.flora.validate_specimen_record import (
    CASES_PATH,
    REPO_ROOT,
    SCHEMA_PATH,
    build_case_candidate,
    canonical_record_id,
    canonical_spec_hash,
    main,
    replay_cases,
    validate_document,
)


class SpecimenRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profile = json.loads(CASES_PATH.read_text(encoding="utf-8"))

    def candidate(self, name: str) -> dict[str, object]:
        case = next(case for case in self.profile["cases"] if case["name"] == name)
        return build_case_candidate(self.profile, case)

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            schema["properties"]["object_type"]["const"],
            "SpecimenRecordCandidate",
        )
        self.assertEqual(
            set(schema["properties"]["governance"]["properties"]),
            {
                "source_activated",
                "evidence_resolved",
                "policy_approved",
                "review_approved",
                "release_authorized",
                "published",
            },
        )

    def test_exact_fixture_polarity_replays(self) -> None:
        self.assertEqual(replay_cases(), [])
        valid = [
            case for case in self.profile["cases"] if not case["expected_codes"]
        ]
        invalid = [
            case for case in self.profile["cases"] if case["expected_codes"]
        ]
        self.assertEqual(len(valid), 4)
        self.assertGreaterEqual(len(invalid), 20)
        for case in self.profile["cases"]:
            with self.subTest(case=case["name"]):
                candidate = build_case_candidate(self.profile, case)
                actual = [
                    finding.code for finding in validate_document(candidate)
                ]
                self.assertEqual(actual, case["expected_codes"])

    def test_identity_and_spec_hash_are_deterministic_and_source_bound(self) -> None:
        candidate = self.candidate(
            "valid-public-safe-historical-voucher-candidate"
        )
        self.assertEqual(candidate["record_id"], canonical_record_id(candidate))
        self.assertEqual(candidate["spec_hash"], canonical_spec_hash(candidate))

        changed = json.loads(json.dumps(candidate))
        changed["source"]["catalog_number"] = "KANU-0002"
        self.assertNotEqual(
            canonical_record_id(changed),
            candidate["record_id"],
        )
        changed["record_id"] = canonical_record_id(changed)
        self.assertNotEqual(canonical_spec_hash(changed), candidate["spec_hash"])

    def test_valid_profiles_preserve_voucher_boundaries(self) -> None:
        public_candidate = self.candidate(
            "valid-public-safe-historical-voucher-candidate"
        )
        event = public_candidate["collection_event"]
        projection = public_candidate["public_projection"]
        governance = public_candidate["governance"]
        self.assertTrue(event["historical_evidence_only"])
        self.assertFalse(event["current_occurrence_claimed"])
        self.assertNotEqual(
            event["restricted_geometry_ref"],
            projection["geometry_ref"],
        )
        self.assertTrue(projection["candidate"])
        self.assertIsNone(projection["release_ref"])
        self.assertTrue(all(value is False for value in governance.values()))

        sensitive = self.candidate("valid-sensitive-specimen-held")
        self.assertEqual(sensitive["sensitivity"]["state"], "restricted")
        self.assertFalse(sensitive["public_projection"]["candidate"])

        unresolved = self.candidate("valid-unresolved-catalog-candidate")
        self.assertEqual(unresolved["source_role"], "candidate")
        self.assertEqual(unresolved["determination"]["status"], "unresolved")

        synthetic = self.candidate("valid-synthetic-reality-boundary")
        self.assertEqual(synthetic["source_role"], "synthetic")
        self.assertEqual(synthetic["record_class"], "synthetic")

    def test_cli_validates_composed_candidate_and_fixture_profile(self) -> None:
        self.assertEqual(main(["--fixtures"]), 0)
        self.assertEqual(main([]), 2)
        candidate = self.candidate(
            "valid-public-safe-historical-voucher-candidate"
        )
        invalid = self.candidate("invalid-current-occurrence-overclaim")
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            valid_path = root / "valid.json"
            invalid_path = root / "invalid.json"
            valid_path.write_text(
                json.dumps(candidate, sort_keys=True),
                encoding="utf-8",
            )
            invalid_path.write_text(
                json.dumps(invalid, sort_keys=True),
                encoding="utf-8",
            )
            self.assertEqual(main([str(valid_path)]), 0)
            self.assertEqual(main([str(invalid_path)]), 1)

    def test_validation_has_no_network_dependency(self) -> None:
        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")

        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            self.assertEqual(replay_cases(), [])

    def test_contract_and_source_map_keep_authority_false(self) -> None:
        contract = (
            REPO_ROOT / "contracts/domains/flora/specimen_record.md"
        ).read_text(encoding="utf-8")
        source_map = (
            REPO_ROOT
            / "docs/intake/exploratory/specimen-record-conformance-source-map.md"
        ).read_text(encoding="utf-8")
        for token in (
            "historical evidence",
            "current occurrence",
            "source activation",
            "release",
        ):
            self.assertIn(token, source_map.lower())
        self.assertIn("schema_version", contract)
        self.assertIn("fixture-only", contract)


if __name__ == "__main__":
    unittest.main()
