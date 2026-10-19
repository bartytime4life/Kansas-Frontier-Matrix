import importlib.util
from pathlib import Path
import unittest
import tempfile
from types import SimpleNamespace
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[2] / "scripts/retire_vercel_deployments.py"
spec = importlib.util.spec_from_file_location("retirement", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def record(identity=1, actor="vercel[bot]", environment="Preview – kfm", **changes):
    return {"id": identity, "creator": {"login": actor}, "environment": environment,
            "sha": "a" * 40, "ref": "main", **changes}


class FakeAPI:
    def __init__(self, replies):
        self.replies = list(replies)
        self.calls = []

    def call(self, method, path, body=None):
        self.calls.append((method, path, body))
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        return reply


class RetirementTests(unittest.TestCase):
    def test_existing_cli_auth_uses_fixed_host_and_no_shell_or_token_argument(self):
        reply = SimpleNamespace(returncode=0, stdout=b"HTTP/2.0 200 OK\r\nContent-Type: application/json\r\n\r\n[]", stderr=b"")
        with mock.patch.object(module.subprocess, "run", return_value=reply) as run:
            self.assertEqual(module.GitHubCLI().call("GET", module.PREFIX + "?per_page=100&page=1"), [])
        command = run.call_args.args[0]
        self.assertEqual(command[:4], ["gh", "api", "--hostname", "github.com"])
        self.assertNotIn("shell", run.call_args.kwargs)
        self.assertNotIn("Authorization", " ".join(command))

    def test_cli_http_error_is_bounded_and_does_not_echo_private_output(self):
        reply = SimpleNamespace(returncode=1, stdout=b"HTTP/2.0 422 Error\n\n{}", stderr=b"private diagnostic")
        with mock.patch.object(module.subprocess, "run", return_value=reply), mock.patch.object(module.time, "sleep"):
            with self.assertRaises(module.APIError) as caught:
                module.GitHubCLI().call("DELETE", module.PREFIX + "/1")
        self.assertEqual(caught.exception.status, 422)
        self.assertNotIn("private diagnostic", str(caught.exception))

    def test_cli_refuses_other_api_resources_before_execution(self):
        with mock.patch.object(module.subprocess, "run") as run:
            with self.assertRaises(module.Stop):
                module.GitHubCLI().call("DELETE", "/repos/another/project/deployments/1")
            run.assert_not_called()

    def test_cli_timeout_stops_with_unverified_outcome(self):
        with mock.patch.object(module.subprocess, "run", side_effect=module.subprocess.TimeoutExpired("gh", 40)):
            with self.assertRaisesRegex(module.Stop, "outcome is unverified"):
                module.GitHubCLI().call("GET", module.PREFIX)

    def test_cli_defaults_to_inventory_and_retains_fingerprint(self):
        api = FakeAPI([[record()]])
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(module, "GitHub", return_value=api):
            output = Path(directory) / "inventory"
            self.assertEqual(module.main(["--output", str(output)]), 0)
            self.assertEqual(len((output / "sha256.txt").read_text().strip()), 64)
            self.assertFalse((output / "journal.jsonl").exists())
        self.assertTrue(all(x[0] == "GET" for x in api.calls))

    def test_existing_output_is_preserved_without_api_calls(self):
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(module, "GitHub") as client:
            with self.assertRaises(module.Stop):
                module.main(["--output", directory])
            client.assert_not_called()

    def test_bad_page_shape_is_rejected(self):
        for page in [{}, None, "not a list"]:
            with self.subTest(page=page), self.assertRaises(module.Stop):
                module.inventory(FakeAPI([page]))

    def test_inventory_only_reads_and_excludes_other_providers_and_environments(self):
        api = FakeAPI([[record(), record(2, actor="github-actions[bot]"),
                        record(3, environment="stage"), record(4, environment="copilot")]])
        snapshot, ignored = module.inventory(api)
        self.assertEqual([x["id"] for x in snapshot["deployments"]], [1])
        self.assertEqual(ignored, 3)
        self.assertTrue(all(x[0] == "GET" for x in api.calls))

    def test_pagination_including_exactly_full_page(self):
        api = FakeAPI([[record(i) for i in range(1, 101)], []])
        snapshot, _ = module.inventory(api)
        self.assertEqual(len(snapshot["deployments"]), 100)
        self.assertTrue(api.calls[-1][1].endswith("page=2"))

    def test_duplicate_ids_abort_before_any_mutation(self):
        with self.assertRaises(module.Stop):
            module.inventory(FakeAPI([[record(), record()]]))

    def test_malformed_records_fail_closed(self):
        for row in [None, record(id=True), record(sha="A" * 40), record(ref=""),
                    record(creator=None), record(environment=None)]:
            with self.subTest(row=row), self.assertRaises(module.Stop):
                module.inventory(FakeAPI([[row]]))

    def test_fingerprint_is_order_independent_and_omits_payload(self):
        snapshot, _ = module.inventory(FakeAPI([[record(2, payload={"secret": "excluded"}), record()]]))
        other, _ = module.inventory(FakeAPI([[record(), record(2)]]))
        self.assertEqual(module.fingerprint(snapshot), module.fingerprint(other))
        self.assertNotIn("payload", str(snapshot))

    def test_wrong_or_missing_fingerprint_never_mutates(self):
        snapshot, _ = module.inventory(FakeAPI([[record()]]))
        for digest in ["", "0" * 64, "A" * 64]:
            api = FakeAPI([])
            with self.subTest(digest=digest), self.assertRaises(module.Stop):
                module.retire(api, snapshot, digest, lambda row: None)
            self.assertEqual(api.calls, [])

    def test_deletes_only_pinned_records_and_journals_completion(self):
        snapshot, _ = module.inventory(FakeAPI([[record(7)]]))
        api, journal = FakeAPI([None]), []
        module.retire(api, snapshot, module.fingerprint(snapshot), journal.append)
        self.assertEqual(api.calls, [("DELETE", module.PREFIX + "/7", None)])
        self.assertEqual(journal[-1], {"id": 7, "action": "deleted"})

    def test_active_record_gets_one_scoped_inactive_transition(self):
        snapshot, _ = module.inventory(FakeAPI([[record()]]))
        api = FakeAPI([module.APIError(422), [{"state": "success"}], {}, None])
        module.retire(api, snapshot, module.fingerprint(snapshot), lambda row: None)
        self.assertEqual([x[0] for x in api.calls], ["DELETE", "GET", "POST", "DELETE"])
        self.assertEqual(api.calls[2][2]["auto_inactive"], False)

    def test_inactive_or_malformed_status_does_not_retry(self):
        snapshot, _ = module.inventory(FakeAPI([[record()]]))
        for statuses in [[], {}, [None], [{"state": "inactive"}], [{"state": "unknown"}]]:
            api = FakeAPI([module.APIError(422), statuses])
            with self.subTest(statuses=statuses), self.assertRaises(module.Stop):
                module.retire(api, snapshot, module.fingerprint(snapshot), lambda row: None)
            self.assertEqual([x[0] for x in api.calls], ["DELETE", "GET"])

    def test_rate_or_permission_failure_stops_and_keeps_partial_journal(self):
        snapshot, _ = module.inventory(FakeAPI([[record(), record(2), record(3)]]))
        api, journal = FakeAPI([None, module.APIError(403)]), []
        with self.assertRaises(module.Stop):
            module.retire(api, snapshot, module.fingerprint(snapshot), journal.append)
        self.assertEqual(len(api.calls), 2)
        self.assertEqual(journal[-1], {"id": 2, "action": "delete_attempt"})

    def test_redirects_are_not_followed(self):
        self.assertIsNone(module.NoRedirect().redirect_request(None, None, 302, "", {}, "https://other.test"))


if __name__ == "__main__":
    unittest.main()
