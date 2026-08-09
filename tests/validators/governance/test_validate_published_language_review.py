from __future__ import annotations

import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.validators.governance import validate_published_language_review as target


class PublishedLanguageReviewTests(unittest.TestCase):
    def test_schema_is_draft_2020_12_and_valid(self) -> None:
        schema = json.loads(target.SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        target.Draft202012Validator.check_schema(schema)

    def test_fixture_polarity_is_exact(self) -> None:
        results = []
        for definition, candidate in target.load_fixture_cases():
            result = target.validate_payload(candidate)
            expected = tuple(
                target.Finding(item["code"], item["path"])
                for item in definition["expected_findings"]
            )
            self.assertEqual(result.outcome, definition["expected_outcome"], definition["name"])
            self.assertEqual(result.findings, expected, definition["name"])
            results.append(result.outcome)
        self.assertEqual(results.count("PASS"), 2)
        self.assertEqual(results.count("DENY"), 9)
        self.assertEqual(results.count("ERROR"), 1)

    def test_valid_identity_is_deterministic(self) -> None:
        definition, candidate = target.load_fixture_cases()[0]
        self.assertEqual(definition["name"], "stable_public_term_candidate")
        self.assertEqual(candidate, target.assign_identity(candidate))
        self.assertEqual(target.validate_payload(candidate).outcome, "PASS")
        self.assertTrue(candidate["review_id"].startswith("published-language-review:"))

    def test_identity_subject_excludes_only_identity_fields(self) -> None:
        _, candidate = target.load_fixture_cases()[0]
        subject = target.identity_subject(candidate)
        self.assertNotIn("review_id", subject)
        self.assertNotIn("spec_hash", subject)
        self.assertEqual(set(candidate) - set(subject), {"review_id", "spec_hash"})

    def test_finite_authority_output(self) -> None:
        _, candidate = target.load_fixture_cases()[0]
        serialized = json.loads(target._serialize(target.validate_payload(candidate)))
        self.assertEqual(serialized["outcome"], "PASS")
        self.assertTrue(all(value is False for value in serialized["authority"].values()))

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
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings, (target.Finding("JSON_DUPLICATE_KEY", "/"),))

    def test_non_object_json_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "array.json"
            path.write_text("[]", encoding="utf-8")
            result = target.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
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
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings, (target.Finding("INPUT_SYMLINK_DENIED", "/"),))

    def test_cli_contract(self) -> None:
        self.assertEqual(target.main([]), 2)
        self.assertEqual(target.main(["--fixtures", str(target.CASES)]), 2)
        self.assertEqual(target.main(["--fixtures"]), 0)

    def test_direct_script_entrypoint(self) -> None:
        script = target.ROOT / "tools/validators/governance/validate_published_language_review.py"
        completed = subprocess.run(
            [sys.executable, str(script), "--fixtures"],
            cwd=target.ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 12)

    def test_findings_are_value_free(self) -> None:
        for _definition, candidate in target.load_fixture_cases():
            result = target.validate_payload(candidate)
            for finding in result.findings:
                self.assertNotIn(candidate["public_term"], finding.code)
                self.assertNotIn(candidate["definition"], finding.code)

    def test_fixture_source_ideas_are_bound(self) -> None:
        document = json.loads(target.CASES.read_text(encoding="utf-8"))
        self.assertEqual(
            document["source_idea_ids"],
            ["KFM-IDX-MOD-005", "KFM-P18-INV-350", "KFM-P18-INV-375"],
        )


if __name__ == "__main__":
    unittest.main()
