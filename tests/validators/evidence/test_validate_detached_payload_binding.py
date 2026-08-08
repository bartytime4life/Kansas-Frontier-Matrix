from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

from tools.validators.evidence.validate_detached_payload_binding import (  # noqa: E402
    FIXTURES,
    MANIFEST,
    validate,
)


def _load(relative: str) -> dict[str, object]:
    return json.loads((FIXTURES / relative).read_text(encoding="utf-8"))


def _rehash(value: dict[str, object]) -> None:
    projection = {
        key: item
        for key, item in value.items()
        if key not in {"spec_hash", "binding_id"}
    }
    digest = compute_spec_hash(projection)
    value["spec_hash"] = digest
    value["binding_id"] = (
        "kfm://evidence/detached-payload-binding/"
        + digest.split(":", 1)[1][:24]
    )


class DetachedPayloadBindingTests(unittest.TestCase):
    def test_schema_is_closed_and_valid(self) -> None:
        schema = json.loads(
            (
                ROOT
                / "schemas/contracts/v1/evidence/detached_payload_binding.schema.json"
            ).read_text(encoding="utf-8")
        )
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["$defs"]["location"]["additionalProperties"])
        self.assertFalse(schema["properties"]["payload"]["additionalProperties"])

    def test_valid_fixture_and_detached_bytes_pass(self) -> None:
        result = validate(
            FIXTURES / "valid/valid_binding.json",
            FIXTURES / "payload/synthetic_payload.bin",
        )
        self.assertEqual(result.outcome, "PASS")
        self.assertEqual(result.findings, ())

    def test_valid_metadata_without_bytes_holds(self) -> None:
        result = validate(FIXTURES / "valid/valid_binding.json")
        self.assertEqual(result.outcome, "HOLD")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"PAYLOAD_BYTES_UNVERIFIED"},
        )

    def test_fixture_manifest_polarity(self) -> None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["cases"]), 7)
        for case in manifest["cases"]:
            result = validate(
                FIXTURES / case["input"],
                FIXTURES / case["payload_file"],
            )
            self.assertEqual(result.outcome, case["expected_outcome"], case["case_id"])
            self.assertEqual(
                sorted({finding.code for finding in result.findings}),
                case["expected_findings"],
                case["case_id"],
            )

    def test_private_location_fails_closed_without_network(self) -> None:
        result = validate(
            FIXTURES / "semantic_invalid/unsafe_location.json",
            FIXTURES / "payload/synthetic_payload.bin",
        )
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"UNSAFE_LOCATION"},
        )

    def test_payload_id_must_follow_raw_digest(self) -> None:
        value = _load("valid/valid_binding.json")
        value["payload"]["payload_id"] = (
            "kfm://evidence/detached-payload/" + "0" * 24
        )
        _rehash(value)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(value), encoding="utf-8")
            result = validate(path, FIXTURES / "payload/synthetic_payload.bin")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"PAYLOAD_ID_MISMATCH"},
        )

    def test_payload_bytes_are_verified_not_inferred(self) -> None:
        result = validate(
            FIXTURES / "semantic_invalid/payload_digest_mismatch.json",
            FIXTURES / "payload/synthetic_payload.bin",
        )
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"PAYLOAD_DIGEST_MISMATCH"},
        )

    def test_cli_is_deterministic_and_no_network(self) -> None:
        command = [
            sys.executable,
            "tools/validators/evidence/validate_detached_payload_binding.py",
            "fixtures/contracts/v1/evidence/detached_payload_binding/valid/valid_binding.json",
            "--payload-file",
            "fixtures/contracts/v1/evidence/detached_payload_binding/payload/synthetic_payload.bin",
        ]
        environment = os.environ.copy()
        environment["KFM_NO_NETWORK"] = "1"
        first = subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        second = subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(first.returncode, 0)
        self.assertEqual(first.stdout, second.stdout)
        report = json.loads(first.stdout)
        self.assertFalse(report["network_attempted"])
        self.assertFalse(report["authority_created"])


if __name__ == "__main__":
    unittest.main()
