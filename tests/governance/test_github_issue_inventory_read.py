import importlib.util
import io
import json
import unittest
from datetime import datetime, timedelta, timezone
from email.message import Message
from pathlib import Path
from urllib.error import URLError
from urllib.request import BaseHandler, build_opener
from urllib.response import addinfourl

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


class GitHubIssueInventoryReadRedirectTests(unittest.TestCase):
    """The live probe must never follow a redirect with its bearer token."""

    def install_transport(self, *, code, target):
        requests = []

        class SyntheticTransport(BaseHandler):
            handler_order = 100

            def https_open(self, request):
                requests.append(request)
                headers = Message()
                if code != 200:
                    headers["Location"] = target
                response = addinfourl(io.BytesIO(b"{}"), headers, request.full_url, code)
                response.msg = "synthetic response"
                return response

            http_open = https_open

        return requests, SyntheticTransport()

    def test_get_json_denies_redirect_before_second_request(self):
        requests, transport = self.install_transport(
            code=302, target="https://redirect.invalid/repos/bartytime4life/Kansas-Frontier-Matrix"
        )

        def opener(request, *, timeout):
            return build_opener(transport, mod._RejectRedirects()).open(request, timeout=timeout)

        with self.assertRaises(URLError):
            mod._get_json("/repos/bartytime4life/Kansas-Frontier-Matrix", "synthetic-credential-not-secret", opener)

        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].get_header("Authorization"), "Bearer synthetic-credential-not-secret")

    def test_read_live_denies_redirect_and_does_not_call_build_record(self):
        requests, transport = self.install_transport(
            code=301, target="https://redirect.invalid/repos/bartytime4life/Kansas-Frontier-Matrix"
        )

        def opener(request, *, timeout):
            return build_opener(transport, mod._RejectRedirects()).open(request, timeout=timeout)

        now = datetime(2026, 8, 8, tzinfo=timezone.utc)
        with self.assertRaises(URLError):
            mod.read_live("bartytime4life/Kansas-Frontier-Matrix", [1647], "synthetic-credential-not-secret", now, opener)

        self.assertEqual(len(requests), 1)


if __name__ == "__main__":
    unittest.main()
