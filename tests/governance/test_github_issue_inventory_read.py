import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timedelta, timezone
from email.message import Message
from pathlib import Path
from unittest.mock import patch
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


class GitHubIssueInventoryReadInputTests(unittest.TestCase):
    """Untrusted API or fixture JSON of the wrong shape must fail closed as an exception the CLI reports, never a traceback."""

    def setUp(self):
        self.fixture = json.loads(FIXTURE.read_text())
        self.now = datetime.fromisoformat("2026-08-08T02:30:00+00:00")

    def build(self, **overrides):
        params = {"repository": "bartytime4life/Kansas-Frontier-Matrix", "repo_payload": self.fixture["repository"], "ref_payload": self.fixture["ref"],
                  "issue_payloads": self.fixture["issues"], "headers": self.fixture["headers"], "requested_issue_ids": [1647, 1675], "retrieved_at": self.now}
        params.update(overrides)
        return mod.build_record(**params)

    def issues_with(self, **change):
        rows = json.loads(json.dumps(self.fixture["issues"]))
        rows[0].update(change)
        return rows

    def test_malformed_payloads_fail_closed(self):
        cases = {
            "repository not an object": {"repo_payload": []},
            "ref not an object": {"ref_payload": None},
            "ref object not an object": {"ref_payload": {**self.fixture["ref"], "object": "sha"}},
            "headers not an object": {"headers": []},
            "issues not an array": {"issue_payloads": {"1647": self.fixture["issues"][0]}},
            "issue not an object": {"issue_payloads": ["1647", self.fixture["issues"][1]]},
            "state not a string": {"issue_payloads": self.issues_with(state=None)},
            "updated_at not a string": {"issue_payloads": self.issues_with(updated_at=1)},
            "number a string": {"issue_payloads": self.issues_with(number="1647")},
            "repository id a boolean": {"repo_payload": {**self.fixture["repository"], "id": True}},
            "rate limit not an integer": {"headers": {**self.fixture["headers"], "x-ratelimit-remaining": "many"}},
        }
        for name, overrides in cases.items():
            with self.subTest(name), self.assertRaises((TypeError, ValueError)):
                self.build(**overrides)

    def test_boolean_issue_number_does_not_match_issue_one(self):
        rows = json.loads(json.dumps(self.fixture["issues"][:1]))
        rows[0]["number"] = True
        with self.assertRaises(TypeError):
            self.build(issue_payloads=rows, requested_issue_ids=[1])

    def test_requested_ids_and_bindings(self):
        for ids in ([1675, 1647], [1647, 1647], [], [0], [True]):
            with self.subTest(ids=ids), self.assertRaises(ValueError):
                self.build(requested_issue_ids=ids)
        with self.assertRaises(ValueError):
            self.build(repository="someone/else")
        with self.assertRaises(ValueError):
            self.build(issue_payloads=self.fixture["issues"][:1])
        short_sha = {**self.fixture["ref"], "object": {"sha": "abc"}}
        with self.assertRaises(ValueError):
            self.build(ref_payload=short_sha)

    def test_rate_limit_reset_and_staleness(self):
        record = self.build(headers={**self.fixture["headers"], "x-ratelimit-reset": "1786156200"})
        self.assertEqual(record["rate_limit_reset_at"], "2026-08-08T02:30:00Z")
        self.assertEqual(mod.freshness(record, self.now + timedelta(seconds=300)), "FRESH")
        self.assertEqual(mod.freshness(record, self.now + timedelta(seconds=301)), "STALE")

    def test_timestamps_need_an_offset_and_accept_lowercase(self):
        self.assertEqual(mod._parse("2026-08-08t02:30:00z"), self.now)
        self.assertEqual(mod._parse("2026-08-07T21:30:00-05:00"), self.now)
        for value in ("2026-08-08T02:30:00", "yesterday", None):
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                mod._parse(value)

    def run_cli(self, *argv, fixture=None):
        err, out = io.StringIO(), io.StringIO()
        args = ["--repository", "bartytime4life/Kansas-Frontier-Matrix", "--issue", "1647", "--issue", "1675", *argv]
        if fixture is not None:
            args += ["--fixture", str(fixture)]
        with redirect_stdout(out), redirect_stderr(err):
            code = mod.main(args)
        return code, out.getvalue(), err.getvalue()

    def test_cli_reports_errors_as_one_json_line(self):
        code, out, _ = self.run_cli("--now", "2026-08-08T02:30:00Z", fixture=FIXTURE)
        self.assertEqual((code, json.loads(out)["outcome"]), (0, "FRESH"))
        with tempfile.TemporaryDirectory() as temp:
            broken = Path(temp) / "fixture.json"
            for content in ("[]", json.dumps({**self.fixture, "issues": ["x"]}), "{"):
                broken.write_text(content)
                with self.subTest(content=content[:20]):
                    code, out, err = self.run_cli("--now", "2026-08-08T02:30:00Z", fixture=broken)
                    self.assertEqual((code, out), (1, ""))
                    self.assertEqual(json.loads(err)["outcome"], "ERROR")
            for now in ("yesterday", "2026-08-08T02:30:00"):
                with self.subTest(now=now):
                    code, _, err = self.run_cli("--now", now, fixture=FIXTURE)
                    self.assertEqual((code, json.loads(err)["outcome"]), (1, "ERROR"))
            limited = Path(temp) / "limited.json"
            limited.write_text(json.dumps({**self.fixture, "headers": {**self.fixture["headers"], "x-ratelimit-remaining": "0"}}))
            code, out, _ = self.run_cli("--now", "2026-08-08T02:30:00Z", fixture=limited)
            self.assertEqual((code, json.loads(out)["outcome"]), (2, "HOLD_RATE_LIMIT"))

    def test_live_mode_without_a_token_holds(self):
        with patch.dict("os.environ", {}, clear=True):
            code, out, err = self.run_cli()
        self.assertEqual((code, out), (2, ""))
        self.assertEqual(json.loads(err), {"outcome": "HOLD_AUTH", "repository_mutation_allowed": False})


if __name__ == "__main__":
    unittest.main()
