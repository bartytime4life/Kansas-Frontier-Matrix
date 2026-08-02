from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path

from tools.validators.validate_generated_receipt import (
    MAX_SCHEMA_FINDINGS,
    REPO_ROOT,
    Finding,
    main,
    validate_receipt,
)


class GeneratedReceiptValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.artifact = self.root / "artifact.txt"
        self.artifact.write_text("synthetic artifact\n", encoding="utf-8")
        self.receipt_path = self.root / "receipt.json"
        self._write_receipt()

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _digest(self, path: Path | None = None) -> str:
        target = path or self.artifact
        return f"sha256:{hashlib.sha256(target.read_bytes()).hexdigest()}"

    def _receipt(self) -> dict[str, object]:
        return {
            "receipt_id": "genrec-test-valid-0001",
            "contract_version": "3.0.0",
            "artifact_paths": ["artifact.txt"],
            "artifact_hashes": {"artifact.txt": self._digest()},
            "model_identity": {
                "provider": "openai",
                "model": "gpt-5",
                "version": "test",
            },
            "prompt_or_contract": "sha256:" + ("1" * 64),
            "parameters": {},
            "inputs": {},
            "truth_labels": {"artifact.txt": "PROPOSED"},
            "validation_gates": [],
            "policy_decisions": [],
            "citations": [],
            "human_review": {
                "reviewer_ids": [],
                "state": "pending",
                "timestamp": None,
            },
            "override_record": None,
            "created_at": "2026-08-02T12:00:00Z",
            "emitter": "test-suite",
        }

    def _write_receipt(self, mutate=None) -> None:
        receipt = self._receipt()
        if mutate is not None:
            mutate(receipt)
        self.receipt_path.write_text(
            json.dumps(receipt, indent=2) + "\n",
            encoding="utf-8",
        )

    def _validate(self, **overrides):
        options = {"repo_root": self.root}
        options.update(overrides)
        return validate_receipt(self.receipt_path, **options)

    def assertFinding(self, result, code: str) -> None:  # noqa: N802
        self.assertIn(code, {finding.code for finding in result.findings})

    def test_pending_receipt_can_be_integrity_valid_without_review_claim(self) -> None:
        result = self._validate()

        self.assertTrue(result.ok, result.findings)
        self.assertTrue(result.integrity_checked)
        self.assertFalse(result.review_claim_present)
        self.assertEqual(result.artifact_count, 1)

    def test_require_review_claim_rejects_pending_review(self) -> None:
        result = self._validate(require_review_claim=True)

        self.assertFinding(result, "REVIEW_CLAIM_MISSING")

    def test_approved_review_satisfies_declared_review_gate(self) -> None:
        self._write_receipt(
            lambda value: value["human_review"].update(  # type: ignore[union-attr]
                state="approved",
                reviewer_ids=["reviewer-1"],
                timestamp="2026-08-02T12:01:00Z",
            )
        )

        result = self._validate(require_review_claim=True)

        self.assertTrue(result.ok)
        self.assertTrue(result.review_claim_present)

    def test_override_satisfies_declared_review_gate(self) -> None:
        self._write_receipt(
            lambda value: value.update(
                override_record={
                    "reason": "synthetic exception",
                    "approver": "reviewer-1",
                    "scope": "test fixture",
                    "expires_at": None,
                }
            )
        )

        result = self._validate(require_review_claim=True)

        self.assertTrue(result.ok)
        self.assertTrue(result.review_claim_present)

    def test_hash_mismatch_fails_closed(self) -> None:
        self.artifact.write_text("changed bytes\n", encoding="utf-8")

        self.assertFinding(self._validate(), "ARTIFACT_DIGEST_MISMATCH")

    def test_sha256_prefix_allowed_by_contract_is_verified(self) -> None:
        prefix = self._digest().removeprefix("sha256:")[:32]
        self._write_receipt(
            lambda value: value["artifact_hashes"].update(  # type: ignore[union-attr]
                {"artifact.txt": f"sha256:{prefix}"}
            )
        )

        self.assertTrue(self._validate().ok)

    def test_artifact_key_sets_must_match(self) -> None:
        def mutate(value) -> None:
            value["artifact_hashes"] = {"other.txt": "sha256:" + ("2" * 64)}
            value["truth_labels"] = {"other.txt": "PROPOSED"}

        self._write_receipt(mutate)
        result = self._validate()

        self.assertFinding(result, "ARTIFACT_HASH_KEYS_MISMATCH")
        self.assertFinding(result, "TRUTH_LABEL_KEYS_MISMATCH")

    def test_noncanonical_path_is_denied(self) -> None:
        def mutate(value) -> None:
            value["artifact_paths"] = ["../artifact.txt"]
            value["artifact_hashes"] = {"../artifact.txt": self._digest()}
            value["truth_labels"] = {"../artifact.txt": "PROPOSED"}

        self._write_receipt(mutate)

        self.assertFinding(self._validate(), "ARTIFACT_PATH_INVALID")

    def test_missing_artifact_fails_closed(self) -> None:
        self.artifact.unlink()

        self.assertFinding(self._validate(), "ARTIFACT_NOT_FILE")

    @unittest.skipUnless(hasattr(os, "symlink"), "symbolic links are unavailable")
    def test_symlink_artifact_is_denied(self) -> None:
        target = self.root / "target.txt"
        target.write_text("synthetic artifact\n", encoding="utf-8")
        self.artifact.unlink()
        self.artifact.symlink_to(target)

        self.assertFinding(self._validate(), "ARTIFACT_SYMLINK_DENIED")

    def test_receipt_cannot_bind_itself(self) -> None:
        def mutate(value) -> None:
            value["artifact_paths"] = ["receipt.json"]
            value["artifact_hashes"] = {"receipt.json": "sha256:" + ("3" * 64)}
            value["truth_labels"] = {"receipt.json": "PROPOSED"}

        self._write_receipt(mutate)

        self.assertFinding(self._validate(), "RECEIPT_SELF_REFERENCE_DENIED")

    def test_governed_root_requires_policy_decision_reference(self) -> None:
        policy_artifact = self.root / "policy" / "rule.rego"
        policy_artifact.parent.mkdir()
        policy_artifact.write_text("package synthetic\n", encoding="utf-8")

        def mutate(value) -> None:
            value["artifact_paths"] = ["policy/rule.rego"]
            value["artifact_hashes"] = {"policy/rule.rego": self._digest(policy_artifact)}
            value["truth_labels"] = {"policy/rule.rego": "PROPOSED"}

        self._write_receipt(mutate)
        result = self._validate()

        self.assertFinding(result, "POLICY_DECISION_REQUIRED")

    def test_documentation_artifact_requires_citation_record(self) -> None:
        document = self.root / "docs" / "guide.md"
        document.parent.mkdir()
        document.write_text("# Synthetic behavior\n", encoding="utf-8")

        def mutate(value) -> None:
            value["artifact_paths"] = ["docs/guide.md"]
            value["artifact_hashes"] = {"docs/guide.md": self._digest(document)}
            value["truth_labels"] = {"docs/guide.md": "PROPOSED"}

        self._write_receipt(mutate)
        self.assertFinding(self._validate(), "DOCUMENT_CITATIONS_REQUIRED")

        def mutate_with_citation(value) -> None:
            mutate(value)
            value["citations"] = [{"id": "repo:synthetic", "validated": True}]

        self._write_receipt(mutate_with_citation)
        self.assertTrue(self._validate().ok)

    def test_blake3_fails_closed_without_an_admitted_dependency(self) -> None:
        self._write_receipt(
            lambda value: value["artifact_hashes"].update(  # type: ignore[union-attr]
                {"artifact.txt": "blake3:" + ("4" * 64)}
            )
        )

        self.assertFinding(self._validate(), "ARTIFACT_DIGEST_UNSUPPORTED")

    def test_contract_version_is_pinned(self) -> None:
        self._write_receipt(lambda value: value.update(contract_version="2.0.0"))

        self.assertFinding(self._validate(), "CONTRACT_VERSION_UNSUPPORTED")

    def test_malformed_and_non_object_json_are_rejected(self) -> None:
        self.receipt_path.write_text("{", encoding="utf-8")
        self.assertFinding(self._validate(), "JSON_INVALID")

        self.receipt_path.write_text("[]\n", encoding="utf-8")
        self.assertFinding(self._validate(), "JSON_ROOT_INVALID")

    def test_nested_duplicate_json_member_is_rejected_without_echoing_name(self) -> None:
        duplicate_name = "reviewer_ids"
        text = self.receipt_path.read_text(encoding="utf-8").replace(
            '"reviewer_ids": [],',
            '"reviewer_ids": ["first"],\n      "reviewer_ids": [],',
            1,
        )
        self.receipt_path.write_text(text, encoding="utf-8")

        result = self._validate()

        self.assertFinding(result, "JSON_DUPLICATE_KEY")
        self.assertNotIn(duplicate_name, " ".join(item.detail for item in result.findings))

    def test_nonfinite_json_number_is_rejected(self) -> None:
        text = self.receipt_path.read_text(encoding="utf-8").replace(
            '"parameters": {},',
            '"parameters": {"temperature": NaN},',
            1,
        )
        self.receipt_path.write_text(text, encoding="utf-8")

        self.assertFinding(self._validate(), "JSON_NONFINITE_NUMBER")

    def test_overflowed_json_number_is_rejected_as_nonfinite(self) -> None:
        text = self.receipt_path.read_text(encoding="utf-8").replace(
            '"parameters": {},',
            '"parameters": {"custom": 1e1000000},',
            1,
        )
        self.receipt_path.write_text(text, encoding="utf-8")

        self.assertFinding(self._validate(), "JSON_NONFINITE_NUMBER")

    def test_parser_complexity_failures_are_deterministic(self) -> None:
        self.receipt_path.write_text(
            '{"value":' * 20_000 + "0" + "}" * 20_000,
            encoding="utf-8",
        )
        nested = self._validate()

        self.receipt_path.write_text(
            '{"value":' + ("9" * 10_000) + "}",
            encoding="utf-8",
        )
        oversized_integer = self._validate()

        self.assertEqual(
            nested.findings,
            (
                Finding(
                    "JSON_COMPLEXITY_LIMIT",
                    "/receipt",
                    "JSON input exceeds parser complexity limits",
                ),
            ),
        )
        self.assertEqual(oversized_integer.findings, nested.findings)

    def test_schema_findings_are_bounded_and_report_truncation(self) -> None:
        self._write_receipt(
            lambda value: value.update(
                validation_gates=[{} for _ in range(MAX_SCHEMA_FINDINGS)]
            )
        )

        result = self._validate()

        self.assertFinding(result, "SCHEMA_FINDINGS_TRUNCATED")
        self.assertLessEqual(len(result.findings), MAX_SCHEMA_FINDINGS + 1)

    def test_cli_output_is_deterministic_and_does_not_echo_artifact_content(self) -> None:
        marker = "DO_NOT_ECHO_RECEIPT_PAYLOAD"
        self.artifact.write_text(marker, encoding="utf-8")
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            first = main([str(self.receipt_path), "--repo-root", str(self.root)])
        first_output = output.getvalue()
        output.seek(0)
        output.truncate(0)
        with contextlib.redirect_stdout(output):
            second = main([str(self.receipt_path), "--repo-root", str(self.root)])

        self.assertEqual(first, 1)
        self.assertEqual(second, 1)
        self.assertEqual(first_output, output.getvalue())
        self.assertNotIn(marker, first_output)
        self.assertIn("ARTIFACT_DIGEST_MISMATCH", first_output)

    def test_repository_fixture_polarity_is_executable(self) -> None:
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            result = main(["--fixtures"])

        self.assertEqual(result, 0, output.getvalue())
        self.assertIn("GENERATED_RECEIPT_FIXTURES_VALID", output.getvalue())

    def test_negative_fixture_pins_exact_expected_failure(self) -> None:
        path = (
            REPO_ROOT
            / "fixtures/generated_receipt/invalid/missing_contract_version.json"
        )

        result = validate_receipt(path)

        self.assertEqual(
            result.findings,
            (Finding("SCHEMA_INVALID", "/", "schema constraint failed: required"),),
        )


if __name__ == "__main__":
    unittest.main()
