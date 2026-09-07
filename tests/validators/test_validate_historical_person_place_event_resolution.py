#!/usr/bin/env python3
"""Tests for the fixture-only historical person-place-event resolver."""
from __future__ import annotations

import copy
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_historical_person_place_event_resolution.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution.schema.json"

spec = importlib.util.spec_from_file_location("historical_resolution_validator", VALIDATOR_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("validator module could not be loaded")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class HistoricalResolutionTests(unittest.TestCase):
    def load(self, relative: str) -> dict:
        return json.loads((FIXTURE_ROOT / relative).read_text(encoding="utf-8"))

    def codes(self, candidate: dict) -> set[str]:
        return {finding.code for finding in module.validate_candidate(candidate)}

    def test_schema_is_draft_2020_12_and_closed(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])
        self.assertIn("spec_hash", schema["required"])
        self.assertIn("negative_evidence", schema["required"])

    def test_valid_fixture_polarity(self) -> None:
        expected = {
            "high_anchor.json": (7, "high", "candidate_review"),
            "conflict_hold.json": (4, "medium", "hold_for_review"),
            "weak_abstain.json": (0, "low", "abstain"),
        }
        for name, result in expected.items():
            with self.subTest(name=name):
                candidate = self.load(f"valid/{name}")
                self.assertEqual(module.validate_candidate(candidate), [])
                self.assertEqual((candidate["score"], candidate["confidence"], candidate["disposition"]), result)
                self.assertEqual(candidate["spec_hash"], module.candidate_spec_hash(candidate))

    def test_invalid_fixture_expected_codes(self) -> None:
        for path in sorted((FIXTURE_ROOT / "invalid").glob("*.json")):
            with self.subTest(path=path.name):
                candidate = json.loads(path.read_text(encoding="utf-8"))
                expected = path.with_suffix(".expected_error.txt").read_text(encoding="utf-8").strip()
                self.assertIn(expected, self.codes(candidate))

    def test_confidence_and_disposition_are_derived(self) -> None:
        candidate = self.load("valid/high_anchor.json")
        candidate["confidence"] = "medium"
        candidate["disposition"] = "hold_for_review"
        candidate["governance"]["review_state"] = "hold_for_review"
        candidate["spec_hash"] = module.candidate_spec_hash(candidate)
        codes = self.codes(candidate)
        self.assertIn("CONFIDENCE_MISMATCH", codes)
        self.assertIn("DISPOSITION_MISMATCH", codes)

    def test_snac_alone_is_corroborative_not_primary_score(self) -> None:
        candidate = self.load("valid/weak_abstain.json")
        self.assertEqual(module.authority_points(candidate), 0)
        self.assertEqual(candidate["person"]["primary_authority"], "local")

    def test_private_and_dna_fields_fail_closed(self) -> None:
        candidate = self.load("valid/high_anchor.json")
        candidate["person"]["raw_genotype"] = "denied"
        candidate["person"]["parcel_id"] = "denied"
        candidate["spec_hash"] = module.candidate_spec_hash(candidate)
        codes = self.codes(candidate)
        self.assertIn("RAW_DNA_FIELD_DENIED", codes)
        self.assertIn("PRIVATE_OR_PRECISE_FIELD_DENIED", codes)

    def test_explicit_candidate_below_symlinked_directory_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target"
            target.mkdir()
            candidate = target / "candidate.json"
            candidate.write_bytes((FIXTURE_ROOT / "valid/high_anchor.json").read_bytes())
            linked = root / "linked"
            linked.symlink_to(target, target_is_directory=True)

            value, findings = module.load_candidate(linked / candidate.name)

        self.assertIsNone(value)
        self.assertEqual({finding.code for finding in findings}, {"INPUT_NOT_REGULAR_FILE"})

    def test_parent_traversal_is_rejected_before_open(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = root / "parent"
            child = parent / "child"
            child.mkdir(parents=True)
            candidate = parent / "candidate.json"
            candidate.write_bytes((FIXTURE_ROOT / "valid/high_anchor.json").read_bytes())
            traversing_candidate = child / ".." / candidate.name

            with mock.patch.object(
                module.os,
                "open",
                side_effect=AssertionError("parent traversal reached os.open"),
            ):
                value, findings = module.load_candidate(traversing_candidate)

        self.assertIsNone(value)
        self.assertEqual({finding.code for finding in findings}, {"INPUT_NOT_REGULAR_FILE"})

    @unittest.skipUnless(os.open in os.supports_dir_fd, "requires directory-relative open")
    def test_parent_swap_cannot_redirect_open_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = root / "parent"
            parent.mkdir()
            candidate = parent / "candidate.json"
            expected = self.load("valid/high_anchor.json")
            candidate.write_text(json.dumps(expected), encoding="utf-8")
            attacker = root / "attacker"
            attacker.mkdir()
            (attacker / candidate.name).write_text("not-json", encoding="utf-8")
            moved_parent = root / "held-parent"
            real_open = os.open
            swapped = False

            def swapping_open(path, flags, mode=0o600, *, dir_fd=None):
                nonlocal swapped
                del mode
                if path == candidate.name and dir_fd is not None and not swapped:
                    parent.rename(moved_parent)
                    parent.symlink_to(attacker, target_is_directory=True)
                    swapped = True
                if dir_fd is None:
                    return real_open(path, flags)
                return real_open(path, flags, dir_fd=dir_fd)

            with mock.patch.object(module.os, "open", side_effect=swapping_open):
                value, findings = module.load_candidate(candidate)

        self.assertTrue(swapped)
        self.assertEqual(findings, [])
        self.assertEqual(value, expected)

    def test_explicit_candidate_oversize_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / "oversized.json"
            candidate.write_bytes(b" " * (module.MAX_JSON_BYTES + 1))

            value, findings = module.load_candidate(candidate)

        self.assertIsNone(value)
        self.assertEqual({finding.code for finding in findings}, {"INPUT_TOO_LARGE"})

    @unittest.skipUnless(hasattr(os, "mkfifo"), "requires POSIX named pipes")
    def test_explicit_candidate_nonregular_file_fails_without_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / "candidate.json"
            os.mkfifo(candidate)

            value, findings = module.load_candidate(candidate)

        self.assertIsNone(value)
        self.assertEqual({finding.code for finding in findings}, {"INPUT_NOT_REGULAR_FILE"})

    def test_fixture_runner_rejects_symlinked_lanes_before_filtering(self) -> None:
        with self.subTest("synthetic symlinked fixture inventory"):
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / "valid").symlink_to(FIXTURE_ROOT / "valid", target_is_directory=True)
                (root / "invalid").symlink_to(FIXTURE_ROOT / "invalid", target_is_directory=True)
                self.assertEqual(module.run_fixtures(root), 2)

    def test_cli_rejects_abbreviated_fixture_options(self) -> None:
        option = "--fixtures"
        for stop in range(3, len(option)):
            abbreviated = option[:stop]
            with self.subTest(option=abbreviated):
                result = subprocess.run(
                    [sys.executable, str(VALIDATOR_PATH), abbreviated],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(2, result.returncode)
                self.assertNotIn("HISTORICAL_RESOLUTION_FIXTURES_VALID", result.stdout)

    def test_fixture_runner(self) -> None:
        self.assertEqual(module.run_fixtures(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
