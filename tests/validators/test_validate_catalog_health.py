from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/catalog/validate_catalog_health.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/catalog_health_report.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/data/catalog_health"

SPEC = importlib.util.spec_from_file_location("catalog_health_under_test", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CatalogHealthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.report_validator = Draft202012Validator(cls.schema)

    def test_schema_is_strict_proposed_draft_2020_12(self) -> None:
        self.assertFalse(self.schema["additionalProperties"])
        self.assertEqual(self.schema["x-kfm"]["status"], "PROPOSED")
        self.assertEqual(self.schema["x-kfm"]["network_default"], "DENY")
        self.assertFalse(self.schema["x-kfm"]["authority_created"])

    def test_fixtures_match_exact_outcomes_findings_and_report_schema(self) -> None:
        expected_outcomes = json.loads(
            (FIXTURE_ROOT / "expected_outcomes.json").read_text(encoding="utf-8")
        )
        expected_findings = json.loads(
            (FIXTURE_ROOT / "expected_findings.json").read_text(encoding="utf-8")
        )
        paths = sorted(
            list((FIXTURE_ROOT / "valid").glob("valid_*.json"))
            + list((FIXTURE_ROOT / "hold").glob("hold_*.json"))
            + list((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
        )
        self.assertEqual(len(paths), 7)
        self.assertEqual(set(expected_outcomes), {path.name for path in paths})
        self.assertEqual(set(expected_findings), {path.name for path in paths})

        for path in paths:
            with self.subTest(path=path.name):
                result = MODULE.validate_record(path, asset_root=FIXTURE_ROOT)
                self.report_validator.validate(result.report)
                self.assertEqual(result.outcome, expected_outcomes[path.name])
                self.assertEqual(
                    sorted({finding.code for finding in result.findings}),
                    sorted(expected_findings[path.name]),
                )
                self.assertFalse(result.report["authority_created"])

    def test_fixture_cli_replays_profile_without_network(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
            env={**os.environ, "KFM_NO_NETWORK": "1"},
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertNotIn("FIXTURE_POLARITY_ERROR", completed.stdout + completed.stderr)
        self.assertEqual(completed.stdout.count('"outcome":"PASS"'), 2)
        self.assertEqual(completed.stdout.count('"outcome":"HOLD"'), 1)
        self.assertEqual(completed.stdout.count('"outcome":"FAIL"'), 4)

    def test_local_asset_bytes_are_verified(self) -> None:
        result = MODULE.validate_record(
            FIXTURE_ROOT / "valid/valid_local_item.json",
            asset_root=FIXTURE_ROOT,
        )
        self.assertEqual(result.outcome, "PASS")
        self.assertEqual(result.report["summary"]["assets_local_verified"], 1)

    def test_remote_head_requires_exact_allowlist_and_can_pass(self) -> None:
        calls: list[tuple[str, float]] = []

        def probe(url: str, timeout: float) -> MODULE.HeadResult:
            calls.append((url, timeout))
            return MODULE.HeadResult(200, {"content-length": "27"})

        with patch.dict(os.environ, {"KFM_NO_NETWORK": ""}):
            result = MODULE.validate_record(
                FIXTURE_ROOT / "hold/hold_remote_unverified.json",
                asset_root=FIXTURE_ROOT,
                network_mode="HEAD",
                allowed_hosts=["catalog.example.invalid"],
                head_probe=probe,
            )
        self.report_validator.validate(result.report)
        self.assertEqual(result.outcome, "PASS")
        self.assertEqual(len(calls), 1)
        self.assertEqual(result.report["network"], {"mode": "HEAD", "attempted": 1, "succeeded": 1})
        self.assertEqual(result.report["summary"]["assets_remote_reachable"], 1)

    def test_remote_head_size_mismatch_fails(self) -> None:
        def probe(_url: str, _timeout: float) -> MODULE.HeadResult:
            return MODULE.HeadResult(200, {"content-length": "26"})

        with patch.dict(os.environ, {"KFM_NO_NETWORK": ""}):
            result = MODULE.validate_record(
                FIXTURE_ROOT / "hold/hold_remote_unverified.json",
                asset_root=FIXTURE_ROOT,
                network_mode="HEAD",
                allowed_hosts=["catalog.example.invalid"],
                head_probe=probe,
            )
        self.assertEqual(result.outcome, "FAIL")
        self.assertIn("CAT_ASSET_SIZE_MISMATCH", {item.code for item in result.findings})

    def test_remote_head_without_allowlist_holds_without_calling_probe(self) -> None:
        called = False

        def probe(_url: str, _timeout: float) -> MODULE.HeadResult:
            nonlocal called
            called = True
            return MODULE.HeadResult(200, {})

        with patch.dict(os.environ, {"KFM_NO_NETWORK": ""}):
            result = MODULE.validate_record(
                FIXTURE_ROOT / "hold/hold_remote_unverified.json",
                asset_root=FIXTURE_ROOT,
                network_mode="HEAD",
                allowed_hosts=[],
                head_probe=probe,
            )
        self.assertFalse(called)
        self.assertEqual(result.outcome, "HOLD")
        self.assertEqual(
            {item.code for item in result.findings},
            {"CAT_ASSET_HOST_NOT_ALLOWLISTED"},
        )

    def test_programmatic_network_mode_honors_environment_kill_switch(self) -> None:
        with patch.dict(os.environ, {"KFM_NO_NETWORK": "1"}):
            result = MODULE.validate_record(
                FIXTURE_ROOT / "hold/hold_remote_unverified.json",
                asset_root=FIXTURE_ROOT,
                network_mode="HEAD",
                allowed_hosts=["catalog.example.invalid"],
            )
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            {item.code for item in result.findings},
            {"CAT_NETWORK_KILL_SWITCH"},
        )

    def test_network_cli_is_denied_by_environment_kill_switch(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                "--network-head",
                "--allow-host",
                "catalog.example.invalid",
                str(FIXTURE_ROOT / "hold/hold_remote_unverified.json"),
            ],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
            env={**os.environ, "KFM_NO_NETWORK": "1"},
        )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("network probes denied", completed.stderr)

    def test_duplicate_keys_fail_closed_without_echo(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"id":"SECRET_CANARY","id":"other"}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual({item.code for item in result.findings}, {"CAT_JSON_DUPLICATE_KEY"})
        self.assertNotIn("SECRET_CANARY", MODULE._serialize(result))

    def test_untrusted_values_are_not_echoed_in_diagnostics(self) -> None:
        candidate = json.loads(
            (FIXTURE_ROOT / "valid/valid_local_item.json").read_text(encoding="utf-8")
        )
        candidate["assets"]["data"]["href"] = "../../SECRET_CANARY"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            result = MODULE.validate_record(path, asset_root=FIXTURE_ROOT)
        report = MODULE._serialize(result)
        self.assertNotIn("SECRET_CANARY", report)
        self.assertIn("CAT_ASSET_PATH_ESCAPE", report)

    def test_replay_is_byte_deterministic(self) -> None:
        path = FIXTURE_ROOT / "valid/valid_local_item.json"
        first = MODULE._serialize(MODULE.validate_record(path, asset_root=FIXTURE_ROOT))
        second = MODULE._serialize(MODULE.validate_record(path, asset_root=FIXTURE_ROOT))
        self.assertEqual(first, second)

    def test_report_schema_rejects_authority_overclaim(self) -> None:
        result = MODULE.validate_record(
            FIXTURE_ROOT / "valid/valid_local_item.json",
            asset_root=FIXTURE_ROOT,
        )
        overclaim = dict(result.report)
        overclaim["authority_created"] = True
        self.assertTrue(list(self.report_validator.iter_errors(overclaim)))


if __name__ == "__main__":
    unittest.main()
