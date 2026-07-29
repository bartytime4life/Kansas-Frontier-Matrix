"""Deterministic no-network semantic anti-collapse tests for water planning."""

from __future__ import annotations

import io
import json
import socket
import unittest
import urllib.request
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from tools.validators.domains.water_planning.validate_status_collapse import (
    main,
    validate_file,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "fixtures" / "domains" / "water_planning" / "status_collapse"
VALID_FIXTURE = FIXTURE_ROOT / "valid" / "valid_1.json"
INVALID_FIXTURES = {
    FIXTURE_ROOT / "invalid" / "meeting_is_approval.json": {
        ("MEETING_IS_NOT_APPROVAL", "$.status_collapse_claims.meeting_is_approval"),
    },
    FIXTURE_ROOT / "invalid" / "application_is_recommendation.json": {
        (
            "APPLICATION_IS_NOT_RECOMMENDATION",
            "$.status_collapse_claims.application_is_recommendation",
        ),
    },
    FIXTURE_ROOT / "invalid" / "application_is_award.json": {
        ("APPLICATION_IS_NOT_AWARD", "$.status_collapse_claims.application_is_award"),
    },
    FIXTURE_ROOT / "invalid" / "recommendation_is_award.json": {
        (
            "RECOMMENDATION_IS_NOT_AWARD",
            "$.status_collapse_claims.recommendation_is_award",
        ),
    },
    FIXTURE_ROOT / "invalid" / "award_is_payment.json": {
        ("AWARD_IS_NOT_PAYMENT", "$.status_collapse_claims.award_is_payment"),
    },
    FIXTURE_ROOT / "invalid" / "payment_is_construction.json": {
        (
            "PAYMENT_IS_NOT_CONSTRUCTION",
            "$.status_collapse_claims.payment_is_construction",
        ),
    },
    FIXTURE_ROOT / "invalid" / "construction_is_completion.json": {
        (
            "CONSTRUCTION_IS_NOT_COMPLETION",
            "$.status_collapse_claims.construction_is_completion",
        ),
    },
    FIXTURE_ROOT / "invalid" / "scoring_matrix_is_project_outcome.json": {
        (
            "SCORING_MATRIX_IS_NOT_PROJECT_OUTCOME",
            "$.status_collapse_claims.scoring_matrix_is_project_outcome",
        ),
    },
    FIXTURE_ROOT / "invalid" / "program_version_is_project_outcome.json": {
        (
            "PROGRAM_VERSION_IS_NOT_PROJECT_OUTCOME",
            "$.status_collapse_claims.program_version_is_project_outcome",
        ),
    },
    FIXTURE_ROOT / "invalid" / "guessed_resolution_states.json": {
        (
            "APPLICANT_IDENTITY_GUESS_FORBIDDEN",
            "$.resolution_state.applicant_identity",
        ),
        (
            "RECIPIENT_IDENTITY_GUESS_FORBIDDEN",
            "$.resolution_state.recipient_identity",
        ),
        ("PROJECT_GEOMETRY_GUESS_FORBIDDEN", "$.resolution_state.project_geometry"),
        (
            "REGIONAL_GEOMETRY_GUESS_FORBIDDEN",
            "$.resolution_state.regional_geometry",
        ),
    },
    FIXTURE_ROOT / "invalid" / "collapsed_amount_facts.json": {
        ("COLLAPSED_AMOUNT_FIELD_FORBIDDEN", "$.amount_facts.amount"),
    },
    FIXTURE_ROOT / "invalid" / "lineage_erased.json": {
        ("LINEAGE_FIELD_MISSING", "$.lineage.correction_or_withdrawal_ref"),
        ("LINEAGE_FIELD_MISSING", "$.lineage.supersedes_ref"),
        ("LINEAGE_FIELD_MISSING", "$.lineage.superseded_by_ref"),
    },
    FIXTURE_ROOT / "invalid" / "blocked_behaviors.json": {
        (
            "AUTHENTICATED_PORTAL_BEHAVIOR_FORBIDDEN",
            "$.blocked_behaviors.authenticated_portal",
        ),
        ("PERSONAL_DATA_BEHAVIOR_FORBIDDEN", "$.blocked_behaviors.personal_data"),
        ("REAL_APPLICANT_BEHAVIOR_FORBIDDEN", "$.blocked_behaviors.real_applicant"),
        ("REAL_PROJECT_BEHAVIOR_FORBIDDEN", "$.blocked_behaviors.real_project"),
        ("CONNECTOR_BEHAVIOR_FORBIDDEN", "$.blocked_behaviors.connector"),
        ("PROOF_BEHAVIOR_FORBIDDEN", "$.blocked_behaviors.proof"),
        ("RELEASE_BEHAVIOR_FORBIDDEN", "$.blocked_behaviors.release"),
        ("PUBLICATION_BEHAVIOR_FORBIDDEN", "$.blocked_behaviors.publication"),
    },
}


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("Water-planning status-collapse validation attempted network access")


class WaterPlanningStatusCollapseTests(unittest.TestCase):
    def setUp(self):
        patchers = (
            patch.object(socket.socket, "connect", _unexpected_network),
            patch.object(socket, "create_connection", _unexpected_network),
            patch.object(urllib.request, "urlopen", _unexpected_network),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_valid_fixture_passes(self):
        self.assertEqual(validate_file(VALID_FIXTURE), ())

    def test_invalid_fixtures_produce_stable_expected_findings(self):
        for fixture_path, expected_findings in INVALID_FIXTURES.items():
            with self.subTest(fixture=fixture_path.name):
                findings = validate_file(fixture_path)
                actual_findings = {
                    (finding.code, finding.path) for finding in findings
                }
                self.assertEqual(actual_findings, expected_findings)

    def test_invalid_input_does_not_echo_protected_values(self):
        fixture_path = FIXTURE_ROOT / "invalid" / "blocked_behaviors.json"
        output = io.StringIO()
        with redirect_stdout(output):
            return_code = main([str(fixture_path)])
        rendered = output.getvalue()
        self.assertEqual(return_code, 1)
        self.assertNotIn("Jane Example", rendered)
        self.assertNotIn("Project Red River", rendered)
        self.assertNotIn("123 Main Street", rendered)


if __name__ == "__main__":
    unittest.main()
