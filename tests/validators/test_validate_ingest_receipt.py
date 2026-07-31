from __future__ import annotations

import contextlib
import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from tools.validators.validate_ingest_receipt import (
    ArtifactBinding,
    main,
    validate_receipt,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_TEMPLATE = (
    REPO_ROOT
    / "fixtures/contracts/v1/source/source_descriptor/valid/valid_1.json"
)


class IngestReceiptValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.carrier = self.root / "carrier.html"
        self.document = self.root / "guidance.pdf"
        self.carrier.write_bytes(b"synthetic KWO carrier fixture\n")
        self.document.write_bytes(b"synthetic KWO document fixture\n")

        self.carrier_digest = hashlib.sha256(self.carrier.read_bytes()).hexdigest()
        self.document_digest = hashlib.sha256(self.document.read_bytes()).hexdigest()
        self.receipt_path = self.root / "receipt.json"
        self.descriptor_path = self.root / "source.json"
        self._write_receipt()
        self._write_descriptor()

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _receipt(self) -> dict[str, object]:
        return {
            "id": "ingest:kwo-synthetic:run-1",
            "source_id": "src:kwo-synthetic",
            "run_id": "run-1",
            "started_at": "2026-07-31T12:00:00Z",
            "finished_at": "2026-07-31T12:00:01Z",
            "outcome": "SUCCESS",
            "bytes_in": self.carrier.stat().st_size + self.document.stat().st_size,
            "digests": {
                "source_head": f"sha256:{self.carrier_digest}",
                "guidance": f"sha256:{self.document_digest}",
            },
        }

    def _write_receipt(self, mutate=None) -> None:
        receipt = self._receipt()
        if mutate is not None:
            mutate(receipt)
        self.receipt_path.write_text(
            json.dumps(receipt, indent=2) + "\n",
            encoding="utf-8",
        )

    def _write_descriptor(self, mutate=None) -> None:
        descriptor = json.loads(SOURCE_TEMPLATE.read_text(encoding="utf-8"))
        descriptor["source_id"] = "src:kwo-synthetic"
        descriptor["source_head"] = {
            "observed_at": "2026-07-31T12:00:00Z",
            "method": "file_checksum",
            "content_identity": {
                "content_sha256": self.carrier_digest,
                "source_head_uri": "https://www.kwo.ks.gov/synthetic-public-fixture",
            },
        }
        if mutate is not None:
            mutate(descriptor)
        self.descriptor_path.write_text(
            json.dumps(descriptor, indent=2) + "\n",
            encoding="utf-8",
        )

    def _bindings(self) -> tuple[ArtifactBinding, ...]:
        return (
            ArtifactBinding("source_head", self.carrier),
            ArtifactBinding("guidance", self.document),
        )

    def _validate(self, **overrides):
        options = {
            "source_descriptor_path": self.descriptor_path,
            "artifacts": self._bindings(),
            "require_success": True,
        }
        options.update(overrides)
        return validate_receipt(self.receipt_path, **options)

    def assertFinding(self, result, code: str) -> None:  # noqa: N802 - unittest style
        self.assertIn(code, {finding.code for finding in result.findings})

    def test_valid_receipt_binds_source_head_artifacts_and_bytes(self) -> None:
        result = self._validate()

        self.assertTrue(result.ok, result.findings)
        self.assertTrue(result.source_head_bound)
        self.assertEqual(result.artifact_count, 2)

    def test_source_id_mismatch_fails_closed(self) -> None:
        self._write_descriptor(lambda value: value.update(source_id="src:other-source"))

        self.assertFinding(self._validate(), "SOURCE_ID_MISMATCH")

    def test_missing_source_head_digest_fails_closed(self) -> None:
        def remove_digest(value):
            value["source_head"]["content_identity"].pop("content_sha256")
            value["source_head"]["content_identity"]["etag"] = "synthetic-etag"

        self._write_descriptor(remove_digest)

        self.assertFinding(self._validate(), "SOURCE_HEAD_DIGEST_MISSING")

    def test_source_head_digest_mismatch_fails_closed(self) -> None:
        def change_digest(value):
            value["source_head"]["content_identity"]["content_sha256"] = "f" * 64

        self._write_descriptor(change_digest)

        self.assertFinding(self._validate(), "SOURCE_HEAD_DIGEST_MISMATCH")

    def test_changed_artifact_bytes_fail_closed(self) -> None:
        self.document.write_bytes(b"changed synthetic document bytes\n")

        self.assertFinding(self._validate(), "ARTIFACT_DIGEST_MISMATCH")

    def test_wrong_byte_count_fails_closed(self) -> None:
        self._write_receipt(lambda value: value.update(bytes_in=1))

        self.assertFinding(self._validate(), "BYTE_COUNT_MISMATCH")

    def test_all_zero_digest_fails_closed(self) -> None:
        def placeholder(value):
            value["digests"]["guidance"] = "sha256:" + ("0" * 64)

        self._write_receipt(placeholder)

        self.assertFinding(self._validate(), "DIGEST_PLACEHOLDER_DENIED")

    def test_reversed_time_fails_closed(self) -> None:
        self._write_receipt(
            lambda value: value.update(finished_at="2026-07-31T11:59:59Z")
        )

        self.assertFinding(self._validate(), "TIME_ORDER_INVALID")

    def test_partial_and_fail_are_valid_records_but_not_successful_gate_outcomes(self) -> None:
        for outcome in ("PARTIAL", "FAIL"):
            with self.subTest(outcome=outcome):
                self._write_receipt(lambda value, outcome=outcome: value.update(outcome=outcome))
                record_result = self._validate(require_success=False)
                gate_result = self._validate(require_success=True)

                self.assertTrue(record_result.ok, record_result.findings)
                self.assertFinding(gate_result, "OUTCOME_NOT_SUCCESS")

    def test_output_is_deterministic_and_does_not_echo_artifact_content(self) -> None:
        protected_marker = "DO-NOT-ECHO-SYNTHETIC-BODY"
        self.document.write_text(protected_marker, encoding="utf-8")
        arguments = [
            str(self.receipt_path),
            "--source-descriptor",
            str(self.descriptor_path),
            "--artifact",
            f"source_head={self.carrier}",
            "--artifact",
            f"guidance={self.document}",
            "--require-success",
        ]

        outputs = []
        for _ in range(2):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                self.assertEqual(main(arguments), 1)
            outputs.append(stream.getvalue())

        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn(protected_marker, outputs[0])
        self.assertIn("ARTIFACT_DIGEST_MISMATCH", outputs[0])

    def test_fixture_mode_has_nonempty_expected_polarity(self) -> None:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            exit_code = main(["--fixtures"])

        self.assertEqual(exit_code, 0)
        self.assertEqual(
            stream.getvalue(),
            "INGEST_RECEIPT_FIXTURES_VALID valid=2 invalid=3\n",
        )


if __name__ == "__main__":
    unittest.main()
