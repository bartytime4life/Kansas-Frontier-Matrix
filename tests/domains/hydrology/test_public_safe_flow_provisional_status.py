#!/usr/bin/env python3
"""Regression proof for FlowObservation provisional-status preservation."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(REPO_ROOT))

from tools.validators.domains.hydrology.validate_public_safe_flow_fixture import (  # noqa: E402
    Finding,
    validate_candidate,
)


VALID_FIXTURE = (
    REPO_ROOT
    / "fixtures/domains/hydrology/public_safe_flow/valid/public_safe_flow.json"
)


def _candidate() -> dict[str, object]:
    return json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))


class HydrologyPublicSafeProvisionalStatusTests(unittest.TestCase):
    def test_valid_fixture_preserves_provisional_status_separately_from_qualifier(self) -> None:
        candidate = _candidate()
        measurement = candidate["measurement"]
        self.assertEqual(measurement["qualifier"], "synthetic")  # type: ignore[index]
        self.assertEqual(measurement["provisional_status"], "provisional")  # type: ignore[index]
        self.assertEqual(validate_candidate(candidate), [])

    def test_missing_or_blank_provisional_status_fails_closed(self) -> None:
        expected = Finding(
            "PROVISIONAL_STATUS_MISSING",
            "$.measurement.provisional_status",
        )
        for value in ("", "   ", None, 0, False):
            candidate = copy.deepcopy(_candidate())
            candidate["measurement"]["provisional_status"] = value  # type: ignore[index]
            self.assertIn(expected, validate_candidate(candidate))

        candidate = copy.deepcopy(_candidate())
        candidate["measurement"].pop("provisional_status")  # type: ignore[index]
        self.assertIn(expected, validate_candidate(candidate))

    def test_source_status_is_not_inferred_from_fixture_qualifier(self) -> None:
        candidate = copy.deepcopy(_candidate())
        candidate["measurement"]["qualifier"] = "synthetic"  # type: ignore[index]
        candidate["measurement"].pop("provisional_status")  # type: ignore[index]
        findings = validate_candidate(candidate)
        self.assertIn(
            Finding("PROVISIONAL_STATUS_MISSING", "$.measurement.provisional_status"),
            findings,
        )
        self.assertNotIn(Finding("QUALIFIER_INVALID", "$.measurement.qualifier"), findings)


if __name__ == "__main__":
    unittest.main()
