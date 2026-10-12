from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.validate_friday_natural_systems_pulse import (
    EXPECTED_DOMAINS,
    FIXTURE_ROOT,
    MATERIAL_SCHEMA_PATH,
    REPO_ROOT,
    SCHEMA_PATH,
    _material_semantic_findings,
    _schema_findings,
    _spec_hash,
    validate_pulse,
)


class FridayNaturalSystemsPulseValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_upstream_assessments_match_shared_shape_and_consumer_semantics(self) -> None:
        files = sorted((FIXTURE_ROOT / "upstream").glob("assessment_*.json"))
        self.assertEqual(8, len(files))
        for path in files:
            with self.subTest(path=path.name):
                candidate = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(
                    [],
                    _schema_findings(
                        candidate,
                        MATERIAL_SCHEMA_PATH,
                        "MATERIAL_SCHEMA_UNAVAILABLE",
                    ),
                )
                self.assertEqual([], _material_semantic_findings(candidate))

    def test_valid_fixtures_pass(self) -> None:
        files = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        self.assertEqual(4, len(files))
        for path in files:
            with self.subTest(path=path.name):
                self.assertTrue(validate_pulse(path).ok)

    def test_valid_fixtures_cover_finite_outcome_precedence(self) -> None:
        expected = {
            "valid_no_event.json": ("NO_EVENT", False),
            "valid_pulse_candidate.json": ("PULSE_CANDIDATE", True),
            "valid_hold.json": ("HOLD", False),
            "valid_error.json": ("ERROR", False),
        }
        for name, (outcome, emit) in expected.items():
            with self.subTest(path=name):
                candidate = json.loads(
                    (FIXTURE_ROOT / "valid" / name).read_text(encoding="utf-8")
                )
                self.assertEqual(outcome, candidate["summary"]["outcome"])
                self.assertIs(emit, candidate["summary"]["emit_candidate"])
                self.assertEqual(list(EXPECTED_DOMAINS), [e["domain"] for e in candidate["entries"]])

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        lane = FIXTURE_ROOT / "invalid"
        manifest = json.loads(
            (lane / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(11, len(manifest))
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = validate_pulse(lane / name)
                self.assertFalse(result.ok)
                self.assertEqual(
                    sorted(set(expected)),
                    sorted({item.code for item in result.findings}),
                )

    def test_fixture_cli_profile_passes_without_echoing_assessment_values(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "tools/validators/validate_friday_natural_systems_pulse.py",
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)
        self.assertNotIn("synthetic_domain_change_fraction", result.stdout)
        self.assertNotIn("kfm://source/synthetic", result.stdout)

    def test_identity_replays_from_canonical_candidate_projection(self) -> None:
        for path in sorted((FIXTURE_ROOT / "valid").glob("valid_*.json")):
            with self.subTest(path=path.name):
                candidate = json.loads(path.read_text(encoding="utf-8"))
                expected_hash = _spec_hash(candidate)
                self.assertEqual(expected_hash, candidate["spec_hash"])
                expected_id = (
                    f"natural-systems-pulse:{candidate['window']['end'][:10]}:"
                    f"{expected_hash.split(':', 1)[1][:24]}"
                )
                self.assertEqual(expected_id, candidate["pulse_id"])

    def test_duplicate_keys_fail_closed_without_echo(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"FridayNaturalSystemsPulseCandidate",'
                '"object_type":"do-not-echo"}',
                encoding="utf-8",
            )
            result = validate_pulse(path)
        self.assertEqual(
            ["JSON_DUPLICATE_KEY"],
            sorted({item.code for item in result.findings}),
        )
        self.assertNotIn("do-not-echo", repr(result.findings))

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_pulse(path)
        self.assertEqual(
            ["JSON_NONFINITE_NUMBER"],
            sorted({item.code for item in result.findings}),
        )

    def test_symlink_input_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = root / "link.json"
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlink creation is unavailable")
            result = validate_pulse(link)
        self.assertEqual(
            ["FILE_SYMLINK_DENIED"],
            sorted({item.code for item in result.findings}),
        )

    def test_validator_has_no_network_or_repository_mutation_surface(self) -> None:
        source = (
            REPO_ROOT
            / "tools/validators/validate_friday_natural_systems_pulse.py"
        ).read_text(encoding="utf-8")
        forbidden = (
            "import requests",
            "import httpx",
            "import urllib.request",
            "import socket",
            "import subprocess",
            "create_pull_request",
            "git push",
            "data/published",
        )
        for token in forbidden:
            with self.subTest(token=token):
                self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
