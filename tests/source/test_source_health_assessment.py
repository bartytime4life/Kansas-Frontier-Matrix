from __future__ import annotations

import importlib.util
import json
import os
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools/validators/source/validate_source_health_assessment.py"
SCHEMA = ROOT / "schemas/contracts/v1/source/source_health_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/source/source_health_assessment"
SPEC = importlib.util.spec_from_file_location("validate_source_health_assessment", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _load(relative: str) -> dict[str, Any]:
    return json.loads((FIXTURES / relative).read_text(encoding="utf-8"))


class SourceHealthAssessmentTests(unittest.TestCase):
    VALID_CASES = {
        "valid/healthy_not_modified.json": ("PASS", []),
        "valid/stale_not_modified.json": ("PASS", []),
        "valid/unavailable_timeout.json": ("PASS", []),
        "valid/unknown_not_probed.json": (
            "ABSTAIN",
            [
                {
                    "code": "SOURCE_HEALTH_UNKNOWN_REQUIRES_REVIEW",
                    "path": "/health_outcome",
                }
            ],
        ),
    }
    INVALID_CASES = {
        "invalid/timeout_marked_healthy.json": [
            {
                "code": "SOURCE_HEALTH_FAILED_AS_HEALTHY",
                "path": "/health_outcome",
            },
            {
                "code": "SOURCE_HEALTH_FRESH_REASON_REQUIRED",
                "path": "/reasons",
            },
        ],
        "invalid/expired_marked_healthy.json": [
            {
                "code": "SOURCE_HEALTH_EXPIRED_AS_HEALTHY",
                "path": "/health_outcome",
            }
        ],
        "invalid/unavailable_without_failure.json": [
            {
                "code": "SOURCE_HEALTH_UNAVAILABLE_WITHOUT_FAILURE",
                "path": "/result_class",
            }
        ],
        "invalid/material_change_without_reason.json": [
            {
                "code": "SOURCE_HEALTH_MATERIAL_REASON_REQUIRED",
                "path": "/reasons",
            }
        ],
        "invalid/empty_marked_healthy.json": [
            {
                "code": "SOURCE_HEALTH_EMPTY_AS_HEALTHY",
                "path": "/health_outcome",
            }
        ],
        "invalid/last_success_after_probe.json": [
            {
                "code": "SOURCE_HEALTH_LAST_SUCCESS_AFTER_PROBE",
                "path": "/last_success_at",
            }
        ],
    }

    @staticmethod
    def _findings(result: Any) -> list[dict[str, str]]:
        return [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]

    def test_schema_is_draft_2020_12_valid(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA.read_text(encoding="utf-8")))

    def test_valid_fixtures_have_exact_outcomes(self) -> None:
        for relative, (outcome, findings) in self.VALID_CASES.items():
            with self.subTest(relative=relative):
                result = MODULE.validate_payload(_load(relative))
                self.assertEqual(result.outcome, outcome)
                self.assertEqual(self._findings(result), findings)

    def test_invalid_fixtures_have_exact_finite_findings(self) -> None:
        for relative, findings in self.INVALID_CASES.items():
            with self.subTest(relative=relative):
                result = MODULE.validate_payload(_load(relative))
                self.assertEqual(result.outcome, "DENY")
                self.assertEqual(self._findings(result), findings)

    def test_optional_headers_remain_optional(self) -> None:
        result = MODULE.validate_payload(_load("valid/unknown_not_probed.json"))
        self.assertEqual(result.outcome, "ABSTAIN")
        self.assertNotIn("etag", _load("valid/unknown_not_probed.json"))
        self.assertNotIn("last_modified", _load("valid/unknown_not_probed.json"))

    def test_compatibility_wrapper_returns_finite_denial_codes(self) -> None:
        codes = MODULE.validate_doc(_load("invalid/material_change_without_reason.json"))
        self.assertEqual(codes, ["SOURCE_HEALTH_MATERIAL_REASON_REQUIRED"])

    def test_duplicate_keys_are_rejected_before_schema_validation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"source_id":"first","source_id":"second"}', encoding="utf-8")
            result = MODULE.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings[0].code, "SOURCE_HEALTH_JSON_DUPLICATE_KEY")

    def test_nonfinite_numbers_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":1e9999}', encoding="utf-8")
            result = MODULE.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings[0].code, "SOURCE_HEALTH_JSON_NONFINITE_NUMBER")

    def test_non_object_root_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "array.json"
            path.write_text("[]", encoding="utf-8")
            result = MODULE.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings[0].code, "SOURCE_HEALTH_ROOT_NOT_OBJECT")

    def test_oversized_input_is_rejected_without_parsing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "large.json"
            path.write_bytes(b" " * (MODULE.MAX_BYTES + 1))
            result = MODULE.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings[0].code, "SOURCE_HEALTH_INPUT_TOO_LARGE")

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks are not supported")
    def test_symlink_input_is_denied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_text(json.dumps(_load("valid/healthy_not_modified.json")), encoding="utf-8")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            result = MODULE.validate_file(link)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings[0].code, "SOURCE_HEALTH_INPUT_SYMLINK_DENIED")

    def test_findings_do_not_echo_document_values(self) -> None:
        value = _load("invalid/material_change_without_reason.json")
        value["source_id"] = "source:private-value"
        result = MODULE.validate_payload(value)
        serialized = MODULE._serialize(None, result)
        self.assertIn("SOURCE_HEALTH_MATERIAL_REASON_REQUIRED", serialized)
        self.assertNotIn("private-value", serialized)

    def test_validation_uses_no_network(self) -> None:
        original = socket.socket

        def denied(*_args: Any, **_kwargs: Any) -> Any:
            raise AssertionError("network denied")

        socket.socket = denied
        try:
            for relative in (*self.VALID_CASES, *self.INVALID_CASES):
                MODULE.validate_payload(_load(relative))
        finally:
            socket.socket = original

    def test_cli_emits_deterministic_json_without_credentials(self) -> None:
        fixture = FIXTURES / "valid/healthy_not_modified.json"
        env = os.environ.copy()
        env["KFM_NO_NETWORK"] = "1"
        env.pop("GITHUB_TOKEN", None)
        env.pop("KFM_GITHUB_READ_TOKEN", None)
        completed = subprocess.run(
            [sys.executable, str(TOOL), str(fixture)],
            cwd=ROOT,
            env=env,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["authority"], "NONE")
        self.assertEqual(payload["execution_mode"], "OFFLINE_VALIDATION")
        self.assertEqual(completed.stdout.strip(), MODULE._compact(payload))


if __name__ == "__main__":
    unittest.main()
