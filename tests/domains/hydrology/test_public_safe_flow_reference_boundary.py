#!/usr/bin/env python3
"""Regression proof for public-safe Hydrology fixture reference boundaries."""

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


class HydrologyPublicSafeReferenceBoundaryTests(unittest.TestCase):
    def test_fixture_reference_profile_accepts_only_synthetic_hydrology_refs(self) -> None:
        candidate = _candidate()
        self.assertEqual(validate_candidate(candidate), [])

        cases = (
            (
                "source_descriptor_ref",
                "https://example.invalid/live-source",
                Finding("SOURCE_DESCRIPTOR_REF_NOT_FIXTURE", "$.source_descriptor_ref"),
            ),
            (
                "gauge_site_ref",
                "fixture://hydrology/gauge/exact/06800000",
                Finding(
                    "GAUGE_SITE_REF_NOT_GENERALIZED_FIXTURE",
                    "$.gauge_site_ref",
                ),
            ),
        )
        for field, value, expected in cases:
            mutated = copy.deepcopy(candidate)
            mutated[field] = value
            self.assertIn(expected, validate_candidate(mutated))

        mutated = copy.deepcopy(candidate)
        mutated["evidence_refs"] = ["https://example.invalid/live-evidence"]
        self.assertIn(
            Finding("EVIDENCE_REF_NOT_FIXTURE", "$.evidence_refs"),
            validate_candidate(mutated),
        )

    def test_missing_references_keep_existing_missing_findings(self) -> None:
        candidate = _candidate()
        candidate["source_descriptor_ref"] = ""
        candidate["gauge_site_ref"] = ""
        candidate["evidence_refs"] = []
        findings = validate_candidate(candidate)
        self.assertIn(
            Finding("SOURCE_DESCRIPTOR_REF_MISSING", "$.source_descriptor_ref"),
            findings,
        )
        self.assertIn(Finding("GAUGE_SITE_REF_MISSING", "$.gauge_site_ref"), findings)
        self.assertIn(Finding("EVIDENCE_REF_MISSING", "$.evidence_refs"), findings)
        self.assertNotIn(
            Finding("SOURCE_DESCRIPTOR_REF_NOT_FIXTURE", "$.source_descriptor_ref"),
            findings,
        )
        self.assertNotIn(
            Finding(
                "GAUGE_SITE_REF_NOT_GENERALIZED_FIXTURE",
                "$.gauge_site_ref",
            ),
            findings,
        )
        self.assertNotIn(Finding("EVIDENCE_REF_NOT_FIXTURE", "$.evidence_refs"), findings)


if __name__ == "__main__":
    unittest.main()
