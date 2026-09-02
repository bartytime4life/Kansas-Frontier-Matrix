from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.governance import validate_lifecycle_gate_closure_assessment as validator

ROOT = Path(__file__).resolve().parents[3]


class LifecycleGateClosureAssessmentTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_all_seven_gates_have_closed_positive_cases(self) -> None:
        manifest = validator.load_fixtures()
        gates = {
            validator.materialize_case(manifest, case)["gate"]
            for case in manifest["cases"]
            if case["expected_outcome"] == "ALLOW"
        }
        self.assertEqual(set(validator.STAGES), gates)
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"ALLOW", "HOLD", "DENY", "ERROR"}, set(outcomes))
        self.assertGreaterEqual(outcomes["DENY"], 10)

    def test_failure_dispositions_preserve_each_prior_stage(self) -> None:
        manifest = validator.load_fixtures()
        case_ids = {
            "admission_missing_source_descriptor",
            "normalization_transform_unresolved",
            "validation_report_missing",
            "catalog_evidence_unresolved",
            "release_rollback_target_missing",
            "correction_notice_invalid",
            "rollback_card_unresolved",
        }
        seen: dict[str, str] = {}
        for case in manifest["cases"]:
            if case["case_id"] not in case_ids:
                continue
            document = validator.materialize_case(manifest, case)
            seen[document["gate"]] = document["decision"]["disposition"]
            self.assertTrue(document["decision"]["prior_state_preservation_required"])
            self.assertFalse(document["governance"]["state_transition_performed"])
        self.assertEqual(validator.FAILURE_DISPOSITIONS, seen)

    def test_conditional_roles_are_gate_scoped(self) -> None:
        manifest = validator.load_fixtures()
        validation = manifest["bases"]["validation_conditional"]
        self.assertEqual(
            {"AGGREGATION_RECEIPT", "POLICY_DECISION", "REDACTION_RECEIPT", "VALIDATION_REPORT"},
            validator.required_artifact_roles(validation),
        )
        catalog = manifest["bases"]["catalog_model_graph"]
        self.assertEqual(
            {"CATALOG_MATRIX", "EVIDENCE_BUNDLE", "GRAPH_PROJECTION", "MODEL_RUN_RECEIPT", "POLICY_DECISION"},
            validator.required_artifact_roles(catalog),
        )
        release = manifest["bases"]["release_review"]
        self.assertIn("REVIEW_RECORD", validator.required_artifact_roles(release))

    def test_identity_is_content_addressed_and_replay_stable(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        first = validator.canonical_identity(document)
        second = validator.canonical_identity(json.loads(json.dumps(document)))
        self.assertEqual(first, second)
        changed = json.loads(json.dumps(document))
        changed["subject_ref"] = "kfm://candidate/synthetic-gate-subject-v2"
        self.assertNotEqual(first, validator.canonical_identity(changed))

    def test_validation_does_not_open_network(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        with mock.patch("socket.socket", side_effect=AssertionError("network denied")):
            result = validator.validate_payload(document)
        self.assertEqual("ALLOW", result.outcome)
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "socket."):
            self.assertNotIn(token, source)

    def test_serialization_does_not_echo_payload_values(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        sentinel = "do-not-echo-subject-value"
        document["subject_ref"] = f"kfm://candidate/{sentinel}"
        result = validator.validate_payload(document)
        rendered = validator.serialize(Path("candidate.json"), result)
        self.assertNotIn(sentinel, rendered)
        self.assertNotIn("synthetic-gate-subject", rendered)

    def test_cli_fixture_replay_and_parser_error_are_deterministic(self) -> None:
        command = [sys.executable, str(Path(validator.__file__)), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn('"cases":31', first.stdout)
        self.assertIn('"suite_match":true', first.stdout)

        with tempfile.TemporaryDirectory() as directory:
            invalid = Path(directory) / "invalid.json"
            invalid.write_text("{", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(invalid)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(2, completed.returncode)
        self.assertIn('"outcome":"ERROR"', completed.stdout)

    def test_duplicate_nonfinite_symlink_and_oversize_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            target = root / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = root / "link.json"
            link.symlink_to(target)
            oversized = root / "oversized.json"
            oversized.write_bytes(b" " * (validator.MAX_BYTES + 1))

            for path, code in (
                (duplicate, "GATE_JSON_DUPLICATE_KEY"),
                (nonfinite, "GATE_JSON_NONFINITE_NUMBER"),
                (link, "GATE_INPUT_SYMLINK_DENIED"),
                (oversized, "GATE_INPUT_TOO_LARGE"),
            ):
                with self.subTest(path=path.name):
                    value, findings = validator._read(path)
                    self.assertIsNone(value)
                    self.assertEqual(code, findings[0].code)


if __name__ == "__main__":
    unittest.main()
