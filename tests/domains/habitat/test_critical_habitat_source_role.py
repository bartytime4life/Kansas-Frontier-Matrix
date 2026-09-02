"""Tests for the fixture-only Habitat critical-habitat role validator."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest import mock

from tools.validators.domains.habitat import (
    validate_critical_habitat_source_role as validator,
)


ROOT = Path(__file__).resolve().parents[3]


def candidate(
    feature_kind: str = "REGULATORY_CRITICAL_HABITAT",
) -> dict[str, object]:
    source_role, claim_kind = validator.EXPECTED_PAIRINGS[feature_kind]
    return {
        "candidate_id": "habitat-role-fixture:critical-habitat-001",
        "claim_kind": claim_kind,
        "evidence_refs": ["fixture://habitat/evidence/critical-habitat-001"],
        "feature_kind": feature_kind,
        "governance": {
            "authority_created": False,
            "evidence_closure_claimed": False,
            "policy_evaluated": False,
            "promotion_authorized": False,
            "publication_authorized": False,
            "release_authorized": False,
            "release_ref": None,
        },
        "profile": validator.PROFILE,
        "public_use_requested": False,
        "source_descriptor_ref": (
            "fixture://habitat/source/critical-habitat-001"
        ),
        "source_role": source_role,
        "status": "PROPOSED_INACTIVE",
    }


class CriticalHabitatSourceRoleTests(unittest.TestCase):
    def test_regulatory_and_modeled_lanes_pass_separately(self) -> None:
        for feature_kind in validator.EXPECTED_PAIRINGS:
            with self.subTest(feature_kind=feature_kind):
                result = validator.validate_payload(candidate(feature_kind))
                self.assertEqual("PASS", result.outcome)

    def test_modeled_candidate_cannot_claim_regulatory_critical_habitat(self) -> None:
        value = candidate()
        value["source_role"] = "MODELED"
        result = validator.validate_payload(value)
        self.assertEqual("DENY", result.outcome)
        self.assertIn(
            "MODELED_AS_CRITICAL_DENIED",
            {item.code for item in result.findings},
        )

    def test_regulatory_candidate_cannot_be_recast_as_modeled(self) -> None:
        value = candidate("MODELED_HABITAT")
        value["source_role"] = "REGULATORY"
        result = validator.validate_payload(value)
        self.assertEqual("DENY", result.outcome)
        self.assertIn(
            "REGULATORY_AS_MODELED_DENIED",
            {item.code for item in result.findings},
        )

    def test_designation_cannot_claim_species_presence(self) -> None:
        value = candidate()
        value["claim_kind"] = "SPECIES_PRESENCE"
        result = validator.validate_payload(value)
        self.assertIn(
            "CRITICAL_HABITAT_PRESENCE_CLAIM_DENIED",
            {item.code for item in result.findings},
        )

    def test_fixture_pass_cannot_grant_publication_or_release(self) -> None:
        fields = (
            "authority_created",
            "evidence_closure_claimed",
            "policy_evaluated",
            "promotion_authorized",
            "publication_authorized",
            "release_authorized",
        )
        for field in fields:
            value = candidate()
            governance = value["governance"]
            assert isinstance(governance, dict)
            governance[field] = True
            with self.subTest(field=field):
                result = validator.validate_payload(value)
                self.assertIn(
                    "HABITAT_ROLE_AUTHORITY_GRANT_DENIED",
                    {item.code for item in result.findings},
                )

    def test_validation_is_deterministic_no_network_and_does_not_echo(self) -> None:
        value = candidate()
        value["candidate_id"] = "do-not-echo-sensitive-clue"
        with mock.patch(
            "socket.socket",
            side_effect=AssertionError("network denied"),
        ):
            first = validator.validate_payload(value)
            second = validator.validate_payload(deepcopy(value))
        self.assertEqual(first, second)
        rendered = validator.serialize(Path("candidate.json"), first)
        self.assertNotIn("do-not-echo-sensitive-clue", rendered)

    def test_cli_and_strict_json_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            valid = root / "valid.json"
            valid.write_text(json.dumps(candidate()), encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(valid)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn('"outcome":"PASS"', completed.stdout)

            invalid = root / "invalid.json"
            invalid.write_text('{"a":1,"a":2}', encoding="utf-8")
            failed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(invalid)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(2, failed.returncode)
            self.assertIn("HABITAT_ROLE_JSON_DUPLICATE_KEY", failed.stdout)
            self.assertIn('"outcome":"ERROR"', failed.stdout)


if __name__ == "__main__":
    unittest.main()
