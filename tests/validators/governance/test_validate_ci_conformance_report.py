from __future__ import annotations

import copy
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

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

    def test_blocked_closure_has_no_fabricated_final_evidence(self) -> None:
        closure = self.report["closure"]
        self.assertEqual(closure["state"], "BLOCKED")
        self.assertIsNone(closure["target_sha"])
        self.assertEqual(closure["hosted_runs"], [])
        self.assertEqual(closure["human_review"]["state"], "PENDING")
        self.assertIsNone(closure["closer"])
        self.assertIsNone(closure["closed_at"])

    def test_ready_closure_requires_exact_evidence(self) -> None:
        candidate = copy.deepcopy(self.report)
        candidate["closure"]["state"] = "READY"
        codes = self.codes(candidate)
        self.assertIn("CLOSURE_FINAL_SHA_MISSING", codes)
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
