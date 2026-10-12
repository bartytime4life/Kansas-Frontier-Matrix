from __future__ import annotations

import copy
import importlib.util
import json
import os
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools/validators/source/validate_source_availability_watchlist.py"
FIXTURES = ROOT / "fixtures/contracts/v1/source/source_availability_watchlist/cases.json"
SCHEMA = ROOT / "schemas/contracts/v1/source/source_availability_watchlist.schema.json"
spec = importlib.util.spec_from_file_location("validate_source_availability_watchlist", TOOL)
MODULE = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = MODULE
spec.loader.exec_module(MODULE)

def _decode(value: str) -> str:
    return value.replace("~1", "/").replace("~0", "~")

def _replace(document: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [_decode(part) for part in pointer[1:].split("/")]
    target: Any = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    else:
        target[final] = copy.deepcopy(value)

class SourceAvailabilityWatchlistTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(FIXTURES.read_text(encoding="utf-8"))
        cls.cases = {case["case_id"]: case for case in cls.manifest["cases"]}

    def materialize(self, case_id: str) -> dict[str, Any]:
        case = self.cases[case_id]
        document = copy.deepcopy(self.manifest["bases"][case["base"]])
        for mutation in case.get("mutations", []):
            _replace(document, mutation["path"], mutation.get("value"))
        document["summary"] = MODULE.recompute_summary(document["entries"])
        document["summary"].update(case.get("summary_override", {}))
        spec_hash, watchlist_id = MODULE.canonical_identity(document)
        document["spec_hash"] = case.get("spec_hash_override", spec_hash)
        document["watchlist_id"] = case.get("watchlist_id_override", watchlist_id)
        return document

    def result(self, case_id: str) -> Any:
        return MODULE.validate_payload(self.materialize(case_id))

    def test_schema_is_draft_2020_12_valid(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_fixture_manifest_has_exact_polarity(self) -> None:
        outcomes = [case["expected_outcome"] for case in self.manifest["cases"]]
        self.assertEqual(outcomes.count("PASS"), 3)
        self.assertEqual(outcomes.count("ABSTAIN"), 1)
        self.assertEqual(outcomes.count("ERROR"), 1)
        self.assertEqual(outcomes.count("DENY"), 10)

    def test_all_fixture_cases_match_exactly(self) -> None:
        for case in self.manifest["cases"]:
            with self.subTest(case_id=case["case_id"]):
                result = self.result(case["case_id"])
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(result.outcome, case["expected_outcome"])
                self.assertEqual(actual, case["expected_findings"])

    def test_identity_is_deterministic(self) -> None:
        first = self.materialize("schema-review-pass")
        second = self.materialize("schema-review-pass")
        self.assertEqual(first["spec_hash"], second["spec_hash"])
        self.assertEqual(first["watchlist_id"], second["watchlist_id"])

    def test_candidate_reference_is_review_only(self) -> None:
        document = self.materialize("schema-review-pass")
        self.assertEqual(document["entries"][0]["routing"], "REVIEW_CANDIDATE")
        self.assertTrue(document["entries"][0]["review_required"])
        self.assertFalse(document["governance"]["candidate_work_created"])
        self.assertFalse(document["governance"]["candidate_execution_allowed"])

    def test_no_network_is_used(self) -> None:
        original = socket.socket
        def denied(*_args: Any, **_kwargs: Any) -> Any:
            raise AssertionError("network denied")
        socket.socket = denied
        try:
            for case_id in self.cases:
                self.result(case_id)
        finally:
            socket.socket = original

    def test_findings_are_value_minimized(self) -> None:
        result = self.result("source-ref-mismatch")
        serialized = MODULE._serialize(None, result)
        self.assertIn("WATCHLIST_SOURCE_REF_MISMATCH", serialized)
        self.assertNotIn("wrong.source", serialized)
        self.assertNotIn("usgs.waterdata", serialized)

    def test_cli_validates_fixture_without_credentials(self) -> None:
        document = self.materialize("stable-pass")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "watchlist.json"
            path.write_text(json.dumps(document), encoding="utf-8")
            env = os.environ.copy()
            env["KFM_NO_NETWORK"] = "1"
            env.pop("GITHUB_TOKEN", None)
            env.pop("KFM_GITHUB_READ_TOKEN", None)
            completed = subprocess.run([sys.executable, str(TOOL), str(path)], cwd=ROOT, env=env, check=False, capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn('"outcome":"PASS"', completed.stdout)
        self.assertIn('"authority":"NONE"', completed.stdout)

if __name__ == "__main__":
    unittest.main()
