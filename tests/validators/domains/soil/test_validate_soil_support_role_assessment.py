from __future__ import annotations

import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.validators.domains.soil import validate_soil_support_role_assessment as target


class SoilSupportRoleAssessmentTests(unittest.TestCase):
    def test_schema_is_draft_2020_12_and_valid(self) -> None:
        schema = json.loads(target.SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        target.Draft202012Validator.check_schema(schema)

    def test_fixture_polarity_is_exact(self) -> None:
        outcomes: list[str] = []
        for definition, candidate in target.load_fixture_cases():
            result = target.validate_payload(candidate)
            expected = tuple(
                target.Finding(item["code"], item["path"])
                for item in definition["expected_findings"]
            )
            self.assertEqual(result.outcome, definition["expected_outcome"], definition["name"])
            self.assertEqual(result.findings, expected, definition["name"])
            outcomes.append(result.outcome)
        self.assertEqual(outcomes.count("PASS"), 4)
        self.assertEqual(outcomes.count("ABSTAIN"), 1)
        self.assertEqual(outcomes.count("DENY"), 11)
        self.assertEqual(outcomes.count("ERROR"), 1)

    def test_identity_is_deterministic(self) -> None:
        _, candidate = target.load_fixture_cases()[0]
        self.assertEqual(candidate, target.assign_identity(candidate))
        self.assertTrue(candidate["assessment_id"].startswith("soil-support-role:"))
        self.assertEqual(target.validate_payload(candidate).outcome, "PASS")

    def test_identity_subject_excludes_only_identity_fields(self) -> None:
        _, candidate = target.load_fixture_cases()[0]
        subject = target.identity_subject(candidate)
        self.assertEqual(set(candidate) - set(subject), {"assessment_id", "spec_hash"})

    def test_pass_output_retains_zero_authority(self) -> None:
        _, candidate = target.load_fixture_cases()[0]
        payload = json.loads(target._serialize(target.validate_payload(candidate)))
        self.assertTrue(all(value is False for value in payload["authority"].values()))

    def test_no_network_is_required(self) -> None:
        def deny(*_args, **_kwargs):
            raise AssertionError("network access attempted")
        with mock.patch.object(socket, "socket", side_effect=deny), mock.patch.object(
            socket, "create_connection", side_effect=deny
        ), mock.patch.object(socket, "getaddrinfo", side_effect=deny):
            self.assertEqual(target.replay_fixtures(), 0)

    def test_duplicate_json_key_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"profile":"x","profile":"y"}', encoding="utf-8")
            result = target.validate_file(path)
        self.assertEqual(result.findings, (target.Finding("JSON_DUPLICATE_KEY", "/"),))

    def test_non_object_json_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "array.json"
            path.write_text("[]", encoding="utf-8")
            result = target.validate_file(path)
        self.assertEqual(result.findings, (target.Finding("ROOT_NOT_OBJECT", "/"),))

    def test_symlink_is_denied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            real = root / "real.json"
            link = root / "link.json"
            real.write_text("{}", encoding="utf-8")
            try:
                link.symlink_to(real)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            result = target.validate_file(link)
        self.assertEqual(result.findings, (target.Finding("INPUT_SYMLINK_DENIED", "/"),))

    def test_cli_contract(self) -> None:
        self.assertEqual(target.main([]), 2)
        self.assertEqual(target.main(["--fixtures", str(target.CASES)]), 2)
        self.assertEqual(target.main(["--fixtures"]), 0)

    def test_diagnostics_do_not_echo_candidate_values(self) -> None:
        for _definition, candidate in target.load_fixture_cases():
            for finding in target.validate_payload(candidate).findings:
                self.assertNotIn(candidate["source_descriptor_ref"], finding.code)

    def test_source_concepts_are_bound(self) -> None:
        document = json.loads(target.CASES.read_text(encoding="utf-8"))
        self.assertEqual(
            document["source_concept_ids"],
            [
                "SOIL-SUPPORT-TYPE-SEPARATION",
                "SSURGO-SDA-STATIC",
                "KANSAS-MESONET-STATION",
                "SMAP-SATELLITE-GRID",
            ],
        )


if __name__ == "__main__":
    unittest.main()
