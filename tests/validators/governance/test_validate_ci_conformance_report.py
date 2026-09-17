from __future__ import annotations

import copy
import io
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.validators.governance import validate_ci_conformance_report as module


class CIConformanceReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report, findings, cls.raw = module._read_json(module.REPORT_PATH)
        if findings or cls.report is None or cls.raw is None:
            raise AssertionError(findings)

    def codes(self, value: dict[str, object]) -> set[str]:
        digest = module.report_digest(value)
        value["report_digest"] = digest
        value["sha256"] = digest
        return {
            item.code
            for item in module.validate_report(value, check_canonical=False)
        }

    def test_canonical_report_validates(self) -> None:
        self.assertEqual(
            module.validate_report(self.report, raw=self.raw),
            (),
        )

    def test_report_digest_is_reproducible(self) -> None:
        first = module.report_digest(self.report)
        second = module.report_digest(copy.deepcopy(self.report))
        self.assertEqual(first, second)
        self.assertEqual(first, self.report["report_digest"])
        self.assertEqual(first, self.report["sha256"])

    def test_canonical_serialization_is_reproducible(self) -> None:
        self.assertEqual(module.canonical_bytes(self.report), self.raw)
        self.assertEqual(
            module.canonical_bytes(copy.deepcopy(self.report)),
            module.canonical_bytes(self.report),
        )

    def test_check_not_run_cannot_claim_pass(self) -> None:
        candidate = copy.deepcopy(self.report)
        candidate["checks"][3]["outcome"] = "PASS"
        self.assertIn("CHECK_OUTCOME_INVALID", self.codes(candidate))

    def test_skipped_cannot_claim_pass(self) -> None:
        candidate = copy.deepcopy(self.report)
        candidate["checks"][1]["outcome"] = "PASS"
        self.assertIn("CHECK_OUTCOME_INVALID", self.codes(candidate))

    def test_blocked_closure_binds_observed_final_head_without_fabricated_approval(self) -> None:
        closure = self.report["closure"]
        self.assertEqual(closure["state"], "BLOCKED")
        self.assertEqual(
            closure["target_sha"],
            "c653d573c1641503215844c5c4fc85bc15060ced",
        )
        self.assertEqual(
            self.report["repository"]["final_sha"],
            closure["target_sha"],
        )
        self.assertEqual(closure["hosted_runs"], [])
        self.assertEqual(closure["human_review"]["state"], "PENDING")
        self.assertIsNone(closure["closer"])
        self.assertIsNone(closure["closed_at"])

    def test_ready_closure_requires_exact_evidence(self) -> None:
        candidate = copy.deepcopy(self.report)
        candidate["closure"]["state"] = "READY"
        codes = self.codes(candidate)
        self.assertNotIn("CLOSURE_FINAL_SHA_MISSING", codes)
        self.assertIn("CLOSURE_CRITERIA_INCOMPLETE", codes)
        self.assertIn("CLOSURE_HOSTED_EVIDENCE_MISSING", codes)
        self.assertIn("CLOSURE_REVIEW_MISSING", codes)
        self.assertIn("CLOSURE_UNRESOLVED", codes)
        self.assertIn("CLOSURE_REQUIRED_CHECKS", codes)

    def test_report_never_creates_effect_authority(self) -> None:
        controls = self.report["controls"]
        self.assertTrue(controls)
        self.assertEqual(set(controls.values()), {False})
        candidate = copy.deepcopy(self.report)
        candidate["controls"]["release_authorized"] = True
        self.assertIn("AUTHORITY_EFFECT_DENIED", self.codes(candidate))

    def test_inherited_and_introduced_failures_are_distinct(self) -> None:
        failures = self.report["failures"]
        counts = {item["code"]: item["count"] for item in failures["inherited"]}
        self.assertEqual(
            counts,
            {
                "BASELINED_WARNINGS": 125,
                "NEW_DRIFT_CATEGORIES": 9,
                "STALE_BASELINE_FINGERPRINTS": 13,
            },
        )
        self.assertEqual(failures["introduced"], [])

    def test_all_declared_refs_replay(self) -> None:
        self.assertFalse(module._ref_findings(self.report))

    def test_negative_fixture_matrix_has_exact_polarity(self) -> None:
        self.assertEqual(module.validate_fixtures(self.report), ())

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"schema_version":"x","schema_version":"y"}\n', encoding="utf-8")
            value, findings, _raw = module._read_json(path)
        self.assertIsNone(value)
        self.assertEqual([item.code for item in findings], ["JSON_DUPLICATE_KEY"])

    def test_oversized_report_read_stops_at_the_byte_limit(self) -> None:
        class CountingStream(io.BytesIO):
            consumed = 0

            def read(self, size=-1):
                result = super().read(size)
                self.consumed += len(result)
                return result

        stream = CountingStream(b" " * (module.MAX_JSON_BYTES * 2))
        with mock.patch.object(Path, "open", return_value=stream):
            value, findings, raw = module._read_json(module.REPORT_PATH)
        self.assertIsNone(value)
        self.assertIsNone(raw)
        self.assertEqual([item.code for item in findings], ["INPUT_TOO_LARGE"])
        self.assertLessEqual(stream.consumed, module.MAX_JSON_BYTES + 1)

    def test_report_at_exact_byte_limit_remains_readable(self) -> None:
        raw = b'{"padding":"' + b"x" * (module.MAX_JSON_BYTES - 14) + b'"}'
        self.assertEqual(len(raw), module.MAX_JSON_BYTES)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "limit.json"
            path.write_bytes(raw)
            value, findings, observed = module._read_json(path)
        self.assertIsNotNone(value)
        self.assertEqual(findings, [])
        self.assertEqual(observed, raw)

    def test_malformed_report_cli_returns_finite_failure_without_echoing_input(self) -> None:
        marker = "PRIVATE_INPUT_SENTINEL"
        cases = [
            ("/closure", None),
            ("/closure", [marker]),
            ("/closure/state", {marker: True}),
            ("/status", {marker: True}),
            ("/status", marker),
            ("/checks/0/id", {marker: True}),
            ("/checks/0/id", [marker]),
            ("/checks/0/id", None),
            ("/checks/0/id", 1),
            ("/checks/0/execution_state", {marker: True}),
            ("/checks/0/outcome", [marker]),
            ("/failures/introduced", [{"code": "invalid", "count": marker}]),
            ("/failures/introduced", [{"code": "invalid", "count": {marker: True}}]),
            ("/authority_refs/0/id", {marker: True}),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            for pointer, bad in cases:
                with self.subTest(pointer=pointer, bad_type=type(bad).__name__):
                    candidate = copy.deepcopy(self.report)
                    module.apply_mutations(candidate, [{"op": "set", "path": pointer, "value": bad}])
                    digest = module.report_digest(candidate)
                    candidate["report_digest"] = candidate["sha256"] = digest
                    path.write_bytes(module.canonical_bytes(candidate))
                    result = subprocess.run(
                        [module.sys.executable, str(Path(module.__file__)), str(path), "--format", "json"],
                        cwd=module.REPO_ROOT, capture_output=True, text=True, timeout=30,
                    )
                    self.assertEqual(result.returncode, 1, result.stderr + result.stdout)
                    self.assertEqual(result.stderr, "")
                    payload = json.loads(result.stdout)
                    self.assertEqual(payload["validation"], "FAIL")
                    self.assertFalse(payload["authority_created"])
                    self.assertIn("SCHEMA_MISMATCH", {finding["code"] for finding in payload["findings"]})
                    self.assertNotIn(marker, result.stdout)
                    self.assertIn(payload["status"], [None, "CONFORMANT", "NONCONFORMANT", "BLOCKED"])
                    self.assertIn(payload["closure"], [None, "BLOCKED", "READY", "CLOSED"])

    def test_cli_rejects_invalid_git_arguments_and_unicode_without_tracebacks(self) -> None:
        cases = [
            ("/repository/base_sha", "private\x00ref", "BASE_SHA_UNRESOLVED"),
            ("/authority_refs/0/path", "private\x00path", "REF_UNAVAILABLE"),
            ("/repository/base_sha", "\ud800", "JSON_INVALID"),
            ("/authority_refs/0/path", "\udfff", "JSON_INVALID"),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            for pointer, bad, code in cases:
                with self.subTest(pointer=pointer, code=code):
                    candidate = copy.deepcopy(self.report)
                    module.apply_mutations(candidate, [{"op": "set", "path": pointer, "value": bad}])
                    # Escaped JSON can decode to strings unsuitable for Git argv
                    # or UTF-8 canonicalization; do not pre-canonicalize the case.
                    path.write_text(json.dumps(candidate), encoding="utf-8")
                    result = subprocess.run(
                        [module.sys.executable, str(Path(module.__file__)), str(path), "--format", "json"],
                        cwd=module.REPO_ROOT, capture_output=True, text=True, timeout=30,
                    )
                    self.assertEqual(result.returncode, 1)
                    self.assertEqual(result.stderr, "")
                    payload = json.loads(result.stdout)
                    self.assertEqual(payload["validation"], "FAIL")
                    self.assertFalse(payload["authority_created"])
                    self.assertIn(code, {finding["code"] for finding in payload["findings"]})
                    self.assertNotIn("private", result.stdout)

    def test_noncanonical_serialization_is_rejected(self) -> None:
        raw = json.dumps(self.report, separators=(",", ":")).encode("utf-8")
        codes = {
            item.code
            for item in module.validate_report(self.report, raw=raw)
        }
        self.assertIn("SERIALIZATION_NOT_CANONICAL", codes)

    def test_cli_json_is_finite_and_non_authorizing(self) -> None:
        result = subprocess.run(
            [
                module.sys.executable,
                str(module.Path(module.__file__)),
                "--format",
                "json",
            ],
            cwd=module.REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["validation"], "PASS")
        self.assertEqual(payload["status"], "BLOCKED")
        self.assertFalse(payload["authority_created"])

    def test_cli_render_matches_committed_bytes(self) -> None:
        result = subprocess.run(
            [module.sys.executable, str(module.Path(module.__file__)), "--render"],
            cwd=module.REPO_ROOT,
            check=False,
            capture_output=True,
            timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8"))
        self.assertEqual(result.stdout, self.raw)


if __name__ == "__main__":
    unittest.main()
