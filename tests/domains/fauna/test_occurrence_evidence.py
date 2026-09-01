"""Deterministic no-network tests for the draft OccurrenceEvidence profile."""
from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import json
import socket
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = (
    ROOT
    / "tools"
    / "validators"
    / "domains"
    / "fauna"
    / "occurrence"
    / "validate_occurrence_evidence.py"
)
SPEC = importlib.util.spec_from_file_location("kfm_occurrence_evidence_validator", MODULE_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError("occurrence validator module could not be loaded")
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

FIXTURE_ROOT = ROOT / "fixtures" / "domains" / "fauna" / "occurrence_evidence"
SCHEMA_PATH = (
    ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "domains"
    / "fauna"
    / "occurrence_evidence.schema.json"
)


class NetworkDenied(RuntimeError):
    """Raised if the focused suite attempts network access."""


def _deny_network(*_args, **_kwargs):
    raise NetworkDenied("network access is forbidden in occurrence-evidence tests")


def _load(relative_path: str) -> dict:
    return json.loads((FIXTURE_ROOT / relative_path).read_text(encoding="utf-8"))


class OccurrenceEvidenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.network_patches = [
            mock.patch.object(socket, "create_connection", _deny_network),
            mock.patch.object(socket.socket, "connect", _deny_network),
        ]
        for patch in self.network_patches:
            patch.start()
            self.addCleanup(patch.stop)

    def test_schema_is_valid_and_closed(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        for definition_name in (
            "taxon",
            "observation",
            "publicSafeGeometry",
            "geometry",
            "rights",
            "sensitivity",
            "provenance",
            "validation",
        ):
            definition = schema["$defs"][definition_name]
            self.assertFalse(
                definition["additionalProperties"],
                msg=f"{definition_name} must remain closed",
            )
        self.assertFalse(schema["$defs"]["validation"]["properties"]["checks"]["additionalProperties"])

    def test_manifest_replay_matches_exact_findings(self) -> None:
        result = validator.validate_fixture_manifest()
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("PASS", result.outcome)

    def test_valid_profiles_preserve_non_public_states(self) -> None:
        for relative_path in (
            "valid/valid_observed_open.json",
            "valid/valid_modeled_context.json",
            "valid/valid_sensitive_withheld_quarantine.json",
        ):
            with self.subTest(relative_path=relative_path):
                result = validator.validate_file(FIXTURE_ROOT / relative_path)
                self.assertTrue(result.ok, result.findings)

        held = _load("valid/valid_sensitive_withheld_quarantine.json")
        self.assertEqual("quarantine", held["validation"]["validator_result"])
        self.assertEqual("withheld", held["geometry"]["public_safe_geometry"]["geometry_type"])
        self.assertFalse(held["sensitivity"]["exact_location_public_safe"])

    def test_occurrence_identity_is_deterministic(self) -> None:
        candidate = _load("valid/valid_observed_open.json")
        reordered = dict(reversed(list(candidate.items())))
        self.assertEqual(
            candidate["spec_hash"],
            validator.compute_occurrence_spec_hash(reordered),
        )
        self.assertEqual(
            "kfm://occurrence/" + candidate["spec_hash"].split(":", 1)[1],
            candidate["occurrence_evidence_id"],
        )

    def test_source_role_cannot_masquerade_as_observation(self) -> None:
        candidate = _load("valid/valid_observed_open.json")
        candidate["source_role"] = "modeled"
        candidate["spec_hash"] = validator.compute_occurrence_spec_hash(candidate)
        candidate["occurrence_evidence_id"] = (
            "kfm://occurrence/" + candidate["spec_hash"].split(":", 1)[1]
        )
        result = validator.validate_candidate(candidate)
        self.assertIn(
            validator.Finding("obs.source_role_mismatch", "/observation/basis_of_record"),
            result.findings,
        )

    def test_event_time_cannot_contradict_event_date(self) -> None:
        candidate = _load("semantic_invalid/event_time_date_mismatch.json")

        result = validator.validate_candidate(candidate)

        self.assertIn(
            validator.Finding(
                "obs.event_time_date_mismatch",
                "/observation/event_time",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.pass_gate_failed",
                "/validation/validator_result",
            ),
            result.findings,
        )

    def test_public_safe_geometry_type_must_match_precision(self) -> None:
        candidate = _load(
            "semantic_invalid/public_safe_type_precision_mismatch.json"
        )

        result = validator.validate_candidate(candidate)

        self.assertIn(
            validator.Finding(
                "geom.public_safe_type_precision_mismatch",
                "/geometry/public_safe_geometry/precision_class",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.validation_check_mismatch",
                "/validation/checks/geometry_public_safe",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.pass_gate_failed",
                "/validation/validator_result",
            ),
            result.findings,
        )

    def test_exact_public_coordinates_must_match_internal_geometry(self) -> None:
        candidate = _load(
            "semantic_invalid/exact_public_coordinates_mismatch.json"
        )

        result = validator.validate_candidate(candidate)

        self.assertIn(
            validator.Finding(
                "geom.exact_public_coordinates_mismatch",
                "/geometry/public_safe_geometry/coordinates",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.validation_check_mismatch",
                "/validation/checks/geometry_public_safe",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.pass_gate_failed",
                "/validation/validator_result",
            ),
            result.findings,
        )

    def test_exact_public_precision_requires_exact_internal_precision(self) -> None:
        candidate = _load(
            "semantic_invalid/exact_public_internal_precision_mismatch.json"
        )

        result = validator.validate_candidate(candidate)

        self.assertIn(
            validator.Finding(
                "geom.exact_public_internal_precision_mismatch",
                "/geometry/precision_class",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.validation_check_mismatch",
                "/validation/checks/geometry_public_safe",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.pass_gate_failed",
                "/validation/validator_result",
            ),
            result.findings,
        )

    def test_exact_public_geometry_requires_explicit_safety_declaration(self) -> None:
        candidate = _load(
            "semantic_invalid/exact_public_safety_declaration_missing.json"
        )

        result = validator.validate_candidate(candidate)

        self.assertIn(
            validator.Finding(
                "sens.exact_location_public_safe_required",
                "/sensitivity/exact_location_public_safe",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.validation_check_mismatch",
                "/validation/checks/geometry_public_safe",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.pass_gate_failed",
                "/validation/validator_result",
            ),
            result.findings,
        )

    def test_generalized_public_geometry_requires_method(self) -> None:
        candidate = _load(
            "semantic_invalid/public_safe_generalization_method_missing.json"
        )

        result = validator.validate_candidate(candidate)

        self.assertIn(
            validator.Finding(
                "geom.generalization_method_required",
                "/geometry/public_safe_geometry/generalization_method",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.validation_check_mismatch",
                "/validation/checks/geometry_public_safe",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.pass_gate_failed",
                "/validation/validator_result",
            ),
            result.findings,
        )

    def test_required_generalized_point_cannot_reuse_internal_coordinates(self) -> None:
        candidate = _load(
            "semantic_invalid/generalized_public_coordinates_unchanged.json"
        )

        result = validator.validate_candidate(candidate)

        self.assertIn(
            validator.Finding(
                "geom.generalized_public_coordinates_unchanged",
                "/geometry/public_safe_geometry/coordinates",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.validation_check_mismatch",
                "/validation/checks/geometry_public_safe",
            ),
            result.findings,
        )
        self.assertIn(
            validator.Finding(
                "schema.pass_gate_failed",
                "/validation/validator_result",
            ),
            result.findings,
        )

    def test_closed_schema_rejects_undeclared_fields(self) -> None:
        candidate = _load("valid/valid_observed_open.json")
        candidate["runtime_hint"] = "not part of the occurrence evidence contract"
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        errors = list(
            Draft202012Validator(
                schema,
                format_checker=FormatChecker(),
            ).iter_errors(candidate)
        )
        self.assertTrue(errors)
        self.assertTrue(
            any(error.validator == "additionalProperties" for error in errors),
            errors,
        )

    def test_validation_checks_cannot_claim_unresolved_rights_passed(self) -> None:
        candidate = _load("valid/valid_observed_open.json")
        candidate["rights"]["license"] = "UNKNOWN"
        candidate["rights"]["redistribution_allowed"] = None
        candidate["spec_hash"] = validator.compute_occurrence_spec_hash(candidate)
        candidate["occurrence_evidence_id"] = (
            "kfm://occurrence/" + candidate["spec_hash"].split(":", 1)[1]
        )
        result = validator.validate_candidate(candidate)
        self.assertIn(validator.Finding("rights.unresolved", "/rights"), result.findings)
        self.assertIn(
            validator.Finding(
                "schema.validation_check_mismatch",
                "/validation/checks/rights_resolved",
            ),
            result.findings,
        )

    def test_cli_reports_codes_and_paths_without_record_values(self) -> None:
        fixture = FIXTURE_ROOT / "semantic_invalid" / "modeled_as_observed.json"
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exit_code = validator.main([str(fixture)])
        rendered = output.getvalue()
        self.assertEqual(1, exit_code)
        self.assertIn("obs.source_role_mismatch", rendered)
        self.assertNotIn("Specimen fictivus", rendered)
        self.assertNotIn("Synthetic fixture animal", rendered)
        self.assertNotIn('"coordinates"', rendered)


if __name__ == "__main__":
    unittest.main()
