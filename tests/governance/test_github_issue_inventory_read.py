import importlib.util
import json
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools/probes/github_issue_inventory_read.py"
FIXTURE = ROOT / "fixtures/contracts/v1/governance/github_issue_inventory_read/api_fixture.json"
SCHEMA = ROOT / "schemas/contracts/v1/governance/github_issue_inventory_read.schema.json"
spec = importlib.util.spec_from_file_location("github_issue_inventory_read", TOOL)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class GitHubIssueInventoryReadTests(unittest.TestCase):
    def setUp(self):
        self.fixture = json.loads(FIXTURE.read_text())
        self.now = datetime(2026, 8, 8, 2, 30, tzinfo=timezone.utc)

    def build(self, **overrides):
        params = dict(repository="bartytime4life/Kansas-Frontier-Matrix", repo_payload=self.fixture["repository"], ref_payload=self.fixture["ref"], issue_payloads=self.fixture["issues"], headers=self.fixture["headers"], requested_issue_ids=[1647, 1675], retrieved_at=self.now)
        params.update(overrides)
        return mod.build_record(**params)

    def test_fresh_record_is_closed_and_non_authoritative(self):
        record = self.build()
        self.assertEqual(record["outcome"], "FRESH")
        for field in ("repository_mutation_allowed", "authority_created", "evidence_created", "release_authorized", "publication_authorized", "public_use_allowed"):
            self.assertFalse(record[field])
        schema = json.loads(SCHEMA.read_text())
        Draft202012Validator(schema, format_checker=FormatChecker()).validate(record)

    def test_ref_binding_mismatch_fails_closed(self):
        broken = json.loads(json.dumps(self.fixture["ref"]))
        broken["ref"] = "refs/heads/not-main"
        with self.assertRaises(ValueError):
            self.build(ref_payload=broken)

    def test_pull_request_object_is_rejected(self):
        rows = json.loads(json.dumps(self.fixture["issues"]))
        rows[0]["pull_request"] = {"url": "https://example.invalid"}
        with self.assertRaises(ValueError):
            self.build(issue_payloads=rows)

    def test_rate_limit_zero_holds(self):
        headers = dict(self.fixture["headers"])
        headers["x-ratelimit-remaining"] = "0"
        self.assertEqual(self.build(headers=headers)["outcome"], "HOLD_RATE_LIMIT")

    def test_stale_state_is_explicit(self):
        record = self.build()
        self.assertEqual(mod.freshness(record, self.now + timedelta(seconds=301)), "STALE")

    def test_identity_is_deterministic(self):
        first = self.build()
        second = self.build()
        self.assertEqual(first["receipt_id"], second["receipt_id"])
        self.assertEqual(first["response_digest"], second["response_digest"])


if __name__ == "__main__":
    unittest.main()
