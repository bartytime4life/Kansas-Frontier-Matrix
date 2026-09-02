from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

from tools.validators.policy.validate_policy_obligation_set import (
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
        if key not in {"spec_hash", "obligation_set_id"}
    }
    digest = compute_spec_hash(projection)
    value["spec_hash"] = digest
    value["obligation_set_id"] = (
        "kfm://policy/obligation-set/" + digest.split(":", 1)[1][:24]
    )


class PolicyObligationSetTests(unittest.TestCase):
    def test_schema_is_closed_and_valid(self) -> None:
        schema = json.loads(
            (
                ROOT
                / "schemas/contracts/v1/policy/policy_obligation_set.schema.json"
            ).read_text(encoding="utf-8")
        )
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["$defs"]["obligation"]["additionalProperties"])

    def test_repository_valid_fixture_passes(self) -> None:
        result = validate(FIXTURES / "valid/valid_obligation_set.json")
        self.assertEqual(result.outcome, "PASS")
        self.assertEqual(result.findings, ())

    def test_fixture_manifest_polarity(self) -> None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["cases"]), 6)
        for case in manifest["cases"]:
            result = validate(FIXTURES / case["input"])
            self.assertEqual(result.outcome, case["expected_outcome"], case["case_id"])
            self.assertEqual(
                sorted({finding.code for finding in result.findings}),
                case["expected_findings"],
                case["case_id"],
            )

    def test_policy_refs_must_equal_obligation_union(self) -> None:
        value = _load("valid/valid_obligation_set.json")
        value["policy_decision_refs"] = list(value["policy_decision_refs"][:-1])
        _rehash(value)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(value), encoding="utf-8")
            codes = {finding.code for finding in validate(path).findings}
        self.assertEqual(codes, {"POLICY_REFS_MISMATCH"})

    def test_kind_parameters_are_exclusive(self) -> None:
        result = validate(FIXTURES / "semantic_invalid/parameter_mismatch.json")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"PARAMETERS_INVALID"},
        )

    def test_authority_flags_fail_closed(self) -> None:
        result = validate(FIXTURES / "semantic_invalid/authority_overreach.json")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"AUTHORITY_OVERREACH"},
        )

    def test_cli_is_deterministic_and_no_network(self) -> None:
        command = [
            sys.executable,
            "tools/validators/policy/validate_policy_obligation_set.py",
            "fixtures/contracts/v1/policy/policy_obligation_set/valid/valid_obligation_set.json",
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
        self.assertNotIn("http", first.stdout.lower())


if __name__ == "__main__":
    unittest.main()
