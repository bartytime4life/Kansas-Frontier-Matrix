"""No-network tests for water-planning region and geometry authority checks."""

from __future__ import annotations

import copy
import io
import json
import socket
import unittest
import urllib.request
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from tools.validators.domains.water_planning.validate_geometry_authority import (
    EXPECTED_REGION_IDS,
    EXPECTED_REGION_NAMES,
    authority_record_digest,
    identity_record_digest,
    main,
    validate_document,
    validate_file,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = (
    REPO_ROOT / "fixtures" / "domains" / "water_planning" / "geometry_authority"
)
VALID_FIXTURE = FIXTURE_ROOT / "valid" / "valid_1.json"
INVALID_FIXTURE = FIXTURE_ROOT / "invalid" / "invalid_1.json"


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("Geometry-authority validation attempted network access")


def _load_valid():
    return json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))


def _redigest(document):
    for record in document["geometry_authorities"]:
        record["record_digest"] = authority_record_digest(record)
    for record in document["county_crosswalk_authorities"]:
        record["record_digest"] = authority_record_digest(record)
    document["identity_authority"]["record_digest"] = identity_record_digest(
        document["identity_authority"], document["regions"]
    )


def _finding_pairs(document):
    return {(finding.code, finding.path) for finding in validate_document(document)}


class WaterPlanningGeometryAuthorityTests(unittest.TestCase):
    def setUp(self):
        patchers = (
            patch.object(socket.socket, "connect", _unexpected_network),
            patch.object(socket, "create_connection", _unexpected_network),
            patch.object(urllib.request, "urlopen", _unexpected_network),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_valid_fixture_passes_and_is_non_vacuous(self):
        document = _load_valid()
        self.assertEqual(validate_file(VALID_FIXTURE), ())
        self.assertEqual(
            tuple(region["region_id"] for region in document["regions"]),
            EXPECTED_REGION_IDS,
        )
        self.assertEqual(
            tuple(region["name"] for region in document["regions"]),
            EXPECTED_REGION_NAMES,
        )
        self.assertEqual(
            tuple(region["rac_number"] for region in document["regions"]),
            tuple(range(1, 15)),
        )
        self.assertEqual(len(document["projects"]), 2)
        self.assertFalse(document["identity_authority"]["source_native_numeric_ids"])

    def test_invalid_fixture_has_exact_stable_findings(self):
        expected = (
            (
                "SOURCE_ACTIVATION_BEHAVIOR_FORBIDDEN",
                "$.blocked_behaviors.source_activation",
            ),
            (
                "IDENTITY_AUTHORITY_DIGEST_MISMATCH",
                "$.identity_authority.record_digest",
            ),
            (
                "INLINE_GEOMETRY_OR_INFERENCE_FORBIDDEN",
                "$.projects[0].address",
            ),
            ("UNEXPECTED_FIELD", "$.projects[0].address"),
            ("PROJECT_GEOMETRY_REFERENCE_REQUIRED", "$.projects[0].location_ref"),
            (
                "PROJECT_REGION_NAMESPACE_FOREIGN",
                "$.projects[0].planning_region_ref",
            ),
            (
                "PROJECT_REGION_AUTHORITY_UNRESOLVED",
                "$.projects[1].planning_region_ref",
            ),
            ("REGION_ID_NUMBER_MISMATCH", "$.regions[0].region_id"),
            ("REGION_ID_OUT_OF_RANGE", "$.regions[0].region_id"),
            ("REGION_NAME_NOT_SOURCE_GROUNDED", "$.regions[1].name"),
            ("REGION_ID_NUMBER_MISMATCH", "$.regions[1].region_id"),
            ("REGION_ID_NUMBER_MISMATCH", "$.regions[3].region_id"),
            ("REGION_NAMESPACE_FOREIGN", "$.regions[3].region_id"),
            ("RAC_NUMBER_OUT_OF_RANGE", "$.regions[4].rac_number"),
            ("REGION_ID_OUT_OF_RANGE", "$.regions[4].region_id"),
            ("RAC_NUMBER_MISSING", "$.regions[5]"),
            ("REGION_ID_NUMBER_MISMATCH", "$.regions[5].region_id"),
            ("REGION_ID_OUT_OF_RANGE", "$.regions[5].region_id"),
            ("REGION_GEOMETRY_REFERENCE_REQUIRED", "$.regions[6].geometry_ref"),
            (
                "COUNTY_CROSSWALK_REFERENCE_REQUIRED",
                "$.regions[7].county_crosswalk_ref",
            ),
            ("REGION_NAME_NOT_SOURCE_GROUNDED", "$.regions[8].name"),
            ("REGION_ID_MISSING", "$.regions[kwo-rac-01]"),
            ("REGION_ID_MISSING", "$.regions[kwo-rac-02]"),
            ("REGION_ID_DUPLICATE", "$.regions[kwo-rac-03]"),
            ("REGION_ID_MISSING", "$.regions[kwo-rac-04]"),
            ("REGION_ID_MISSING", "$.regions[kwo-rac-05]"),
            ("REGION_ID_MISSING", "$.regions[kwo-rac-06]"),
        )
        actual = tuple(
            (finding.code, finding.path) for finding in validate_file(INVALID_FIXTURE)
        )
        self.assertEqual(actual, expected)
        self.assertEqual(validate_file(INVALID_FIXTURE), validate_file(INVALID_FIXTURE))

    def test_id_boundaries_duplicates_gaps_mismatches_and_gmd_fail(self):
        for bad_id in ("kwo-rac-00", "kwo-rac-15", "kwo-rac-99"):
            with self.subTest(bad_id=bad_id):
                document = _load_valid()
                document["regions"][0]["region_id"] = bad_id
                _redigest(document)
                findings = _finding_pairs(document)
                self.assertIn(
                    ("REGION_ID_OUT_OF_RANGE", "$.regions[0].region_id"),
                    findings,
                )
                self.assertIn(
                    ("REGION_ID_NUMBER_MISMATCH", "$.regions[0].region_id"),
                    findings,
                )
                self.assertIn(
                    ("REGION_ID_MISSING", "$.regions[kwo-rac-01]"),
                    findings,
                )

        document = _load_valid()
        document["regions"][1]["region_id"] = "kwo-rac-01"
        _redigest(document)
        findings = _finding_pairs(document)
        self.assertIn(("REGION_ID_DUPLICATE", "$.regions[kwo-rac-01]"), findings)
        self.assertIn(("REGION_ID_MISSING", "$.regions[kwo-rac-02]"), findings)

        document = _load_valid()
        document["regions"].pop()
        _redigest(document)
        findings = _finding_pairs(document)
        self.assertIn(("REGION_COUNT_NOT_14", "$.regions"), findings)
        self.assertIn(("REGION_ID_MISSING", "$.regions[kwo-rac-14]"), findings)
        self.assertIn(("RAC_NUMBER_MISSING", "$.regions[14]"), findings)

        document = _load_valid()
        document["regions"][0]["rac_number"] = 2
        _redigest(document)
        findings = _finding_pairs(document)
        self.assertIn(
            ("REGION_ID_NUMBER_MISMATCH", "$.regions[0].region_id"), findings
        )
        self.assertIn(("RAC_NUMBER_DUPLICATE", "$.regions[2]"), findings)
        self.assertIn(("RAC_NUMBER_MISSING", "$.regions[1]"), findings)

        document = _load_valid()
        document["regions"][0]["region_id"] = "kwo-gmd-01"
        _redigest(document)
        findings = _finding_pairs(document)
        self.assertIn(("REGION_NAMESPACE_FOREIGN", "$.regions[0].region_id"), findings)

    def test_source_grounding_digest_and_correction_lineage_fail_closed(self):
        document = _load_valid()
        document["regions"][0]["name"] = "Invented Region"
        _redigest(document)
        self.assertIn(
            ("REGION_NAME_NOT_SOURCE_GROUNDED", "$.regions[0].name"),
            _finding_pairs(document),
        )

        document = _load_valid()
        document["identity_authority"]["record_digest"] = "sha256:" + ("0" * 64)
        self.assertIn(
            (
                "IDENTITY_AUTHORITY_DIGEST_MISMATCH",
                "$.identity_authority.record_digest",
            ),
            _finding_pairs(document),
        )

        document = _load_valid()
        document["identity_authority"]["correction_status"] = "corrected"
        _redigest(document)
        self.assertIn(
            (
                "CORRECTION_LINEAGE_REQUIRED",
                "$.identity_authority.supersedes_ref",
            ),
            _finding_pairs(document),
        )

    def test_region_geometry_and_county_crosswalk_are_reference_only(self):
        document = _load_valid()
        region = document["regions"][0]
        region["geometry_confidence"] = "approximate"
        region["geometry_ref"] = "synthetic:geometry:rac-region:v1"
        self.assertEqual(validate_document(document), ())

        document = _load_valid()
        document["regions"][0]["geometry_confidence"] = "confirmed"
        self.assertIn(
            ("REGION_GEOMETRY_REFERENCE_REQUIRED", "$.regions[0].geometry_ref"),
            _finding_pairs(document),
        )

        document = _load_valid()
        document["regions"][0]["geometry_confidence"] = "approximate"
        document["regions"][0]["geometry_ref"] = "synthetic:geometry:missing:v1"
        self.assertIn(
            (
                "REGION_GEOMETRY_AUTHORITY_UNRESOLVED",
                "$.regions[0].geometry_ref",
            ),
            _finding_pairs(document),
        )

        document = _load_valid()
        region = document["regions"][0]
        region["county_crosswalk_resolution_status"] = "resolved"
        region["county_crosswalk_ref"] = "synthetic:crosswalk:rac-county:v1"
        self.assertEqual(validate_document(document), ())

        document = _load_valid()
        document["regions"][0]["county_crosswalk_resolution_status"] = "resolved"
        self.assertIn(
            (
                "COUNTY_CROSSWALK_REFERENCE_REQUIRED",
                "$.regions[0].county_crosswalk_ref",
            ),
            _finding_pairs(document),
        )

    def test_project_region_membership_and_location_geometry_are_separate(self):
        document = _load_valid()
        project = document["projects"][0]
        project["planning_region_resolution_status"] = "resolved"
        project["planning_region_ref"] = "kwo-rac-01"
        self.assertEqual(validate_document(document), ())

        document = _load_valid()
        project = document["projects"][0]
        project["geometry_confidence"] = "approximate"
        project["location_ref"] = "synthetic:geometry:project-location:v1"
        self.assertEqual(validate_document(document), ())

        document = _load_valid()
        project = document["projects"][0]
        project["planning_region_resolution_status"] = "resolved"
        project["planning_region_ref"] = "kwo-gmd-01"
        self.assertIn(
            (
                "PROJECT_REGION_NAMESPACE_FOREIGN",
                "$.projects[0].planning_region_ref",
            ),
            _finding_pairs(document),
        )

        document = _load_valid()
        project = document["projects"][0]
        project["geometry_confidence"] = "confirmed"
        self.assertIn(
            ("PROJECT_GEOMETRY_REFERENCE_REQUIRED", "$.projects[0].location_ref"),
            _finding_pairs(document),
        )

        document = _load_valid()
        project = document["projects"][0]
        project["geometry_confidence"] = "approximate"
        project["location_ref"] = "synthetic:geometry:missing:v1"
        self.assertIn(
            (
                "PROJECT_GEOMETRY_AUTHORITY_UNRESOLVED",
                "$.projects[0].location_ref",
            ),
            _finding_pairs(document),
        )

    def test_inline_geometry_and_address_inference_are_rejected_without_echo(self):
        document = _load_valid()
        document["projects"][0]["address"] = "Protected Example Address"
        document["projects"][0]["coordinates"] = [1, 2]
        findings = _finding_pairs(document)
        self.assertIn(
            (
                "INLINE_GEOMETRY_OR_INFERENCE_FORBIDDEN",
                "$.projects[0].address",
            ),
            findings,
        )
        self.assertIn(
            (
                "INLINE_GEOMETRY_OR_INFERENCE_FORBIDDEN",
                "$.projects[0].coordinates",
            ),
            findings,
        )

        output = io.StringIO()
        with redirect_stdout(output):
            return_code = main([str(INVALID_FIXTURE)])
        rendered = output.getvalue()
        self.assertEqual(return_code, 1)
        self.assertNotIn("Protected Example Address", rendered)
        self.assertNotIn("Invented Region Name", rendered)

    def test_cli_exit_contract_is_deterministic(self):
        valid_output = io.StringIO()
        with redirect_stdout(valid_output):
            valid_code = main([str(VALID_FIXTURE)])
        self.assertEqual(valid_code, 0)
        self.assertEqual(
            valid_output.getvalue(),
            '{"files":1,"outcome":"VALIDATOR_PASS"}\n',
        )

        first = io.StringIO()
        second = io.StringIO()
        with redirect_stdout(first):
            first_code = main([str(INVALID_FIXTURE)])
        with redirect_stdout(second):
            second_code = main([str(INVALID_FIXTURE)])
        self.assertEqual(first_code, 1)
        self.assertEqual(second_code, 1)
        self.assertEqual(first.getvalue(), second.getvalue())
        parsed = json.loads(first.getvalue())
        self.assertEqual(parsed["outcome"], "VALIDATOR_FAIL")
        self.assertGreater(len(parsed["findings"]), 0)

    def test_missing_input_has_finite_non_echoing_finding(self):
        findings = validate_file(FIXTURE_ROOT / "missing-protected-value.json")
        self.assertEqual(
            tuple((finding.code, finding.path) for finding in findings),
            (("INPUT_NOT_FOUND", "$"),),
        )


if __name__ == "__main__":
    unittest.main()
