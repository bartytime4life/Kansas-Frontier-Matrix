"""Synthetic context/CLI checks; not a scan of the current KFM repository.

The local Git fixture and deliberately tiny validator double isolate diagnostic
binding, log safety and exit propagation. Existing tests own native rule proof.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stdout
from unittest import mock

ROOT = Path(__file__).resolve().parents[3]
REL = Path("tools/validators/directory_governance")
SOURCE = ROOT / REL / "render_repository_topology_diagnostics.py"


def local_git(root: Path, *args: str) -> bytes:
    env = os.environ.copy()
    env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1",
               GIT_TERMINAL_PROMPT="0", GIT_OPTIONAL_LOCKS="0", LC_ALL="C")
    return subprocess.run(["git", *args], cwd=root, env=env, check=True,
                          capture_output=True, timeout=10).stdout


DOUBLE = types.ModuleType("validate_repository_topology")
DOUBLE.DEFAULT_BASELINE = Path("baseline.json")
DOUBLE.TopologyError = ValueError
DOUBLE._git = local_git
DOUBLE.__file__ = "fixture-validator.py"
SPEC = importlib.util.spec_from_file_location("kfm_topology_context_tests", SOURCE)
assert SPEC and SPEC.loader
DIAGNOSTICS = importlib.util.module_from_spec(SPEC)
with mock.patch.dict(sys.modules, {"validate_repository_topology": DOUBLE}):
    SPEC.loader.exec_module(DIAGNOSTICS)


# A process fixture, not a substitute KFM implementation or valid topology data.
VALIDATOR_DOUBLE = '''from pathlib import Path
import os
import subprocess
DEFAULT_BASELINE = Path(__file__).with_name("repository_topology_baseline.json")
TopologyError = ValueError
def _git(root, *args):
    return subprocess.run(["git", *args], cwd=root, capture_output=True,
                          check=True, timeout=10).stdout
def scan(root):
    if os.environ.get("FIXTURE_MUTATE") == "1":
        DEFAULT_BASELINE.write_bytes(b'{"changed": true}')
    if os.environ.get("FIXTURE_CRASH") == "1":
        raise ValueError("PRIVATE_EXCEPTION")
    return [], 1
def _load_baseline_bytes(raw, label):
    return {"expires_on": "2099-01-01"}, {}
def enforce_trusted_baseline(*args):
    pass
def evaluate(*args, **kwargs):
    code = int(os.environ.get("FIXTURE_EXIT", "1"))
    return code, {"outcome": "FIXTURE_RESULT", "tracked_path_count": 1,
        "counts": {"fail_invariant": 0, "fail_new_drift": 0, "baselined_warning": 0},
        "findings": [], "baseline": {"stale_fingerprints": []}}
'''


@unittest.skipUnless(shutil.which("git"), "local Git is required")
class ContextBindingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.lane = self.root / REL
        self.lane.mkdir(parents=True)
        self.validator = self.lane / "validate_repository_topology.py"
        self.renderer = self.lane / SOURCE.name
        self.baseline = self.lane / "repository_topology_baseline.json"
        self.validator.write_text(VALIDATOR_DOUBLE, encoding="utf-8")
        self.renderer.write_bytes(SOURCE.read_bytes())
        self.baseline.write_bytes(b'{}\n')
        local_git(self.root, "init", "-q")
        local_git(self.root, "add", ".")
        local_git(self.root, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                  "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null",
                  "commit", "-qm", "synthetic diagnostic fixture")
        self.addCleanup(mock.patch.stopall)
        mock.patch.object(DOUBLE, "__file__", str(self.validator)).start()
        mock.patch.object(DIAGNOSTICS, "__file__", str(self.renderer)).start()
        mock.patch.dict(os.environ, {
            "GITHUB_RUN_ID": "123", "GITHUB_RUN_ATTEMPT": "2",
            "GITHUB_EVENT_NAME": "pull_request", "KFM_TRUSTED_BASE_REF": "",
        }).start()
        self.args = ["--repo-root", str(self.root), "--baseline", str(self.baseline)]

    def context(self):
        return DIAGNOSTICS.execution_context(self.root, self.baseline)

    def framed(self, code, before=None, after=None):
        output = io.StringIO()
        with mock.patch.object(DIAGNOSTICS, "main", return_value=code) as main:
            with redirect_stdout(output):
                if before is None and after is None:
                    actual = DIAGNOSTICS.run_with_context(self.args)
                else:
                    with mock.patch.object(DIAGNOSTICS, "_context_record", side_effect=[before, after]):
                        actual = DIAGNOSTICS.run_with_context(self.args)
        main.assert_called_once_with(self.args)
        return actual, output.getvalue()

    def test_git_and_file_identities_match_independent_commands(self):
        value = self.context()
        self.assertEqual(local_git(self.root, "rev-parse", "HEAD").decode().strip(), value["checkout_commit"])
        self.assertEqual(local_git(self.root, "rev-parse", "HEAD^{tree}").decode().strip(), value["checkout_tree"])
        index = local_git(self.root, "ls-files", "-s", "-z")
        self.assertEqual(hashlib.sha256(index).hexdigest(), value["index_sha256"])
        for key, path in (("validator_file_sha256", self.validator),
                          ("diagnostic_file_sha256", self.renderer),
                          ("baseline_file_sha256", self.baseline)):
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), value[key])

    def test_replay_is_deterministic_and_read_only(self):
        before = {p: p.read_bytes() for p in self.lane.iterdir()}
        status = local_git(self.root, "status", "--porcelain")
        first = DIAGNOSTICS._context_record(self.root, self.baseline)
        self.assertEqual(first, DIAGNOSTICS._context_record(self.root, self.baseline))
        self.assertEqual(status, local_git(self.root, "status", "--porcelain"))
        self.assertEqual(before, {p: p.read_bytes() for p in self.lane.iterdir()})
        digest, payload = first
        self.assertEqual(hashlib.sha256(payload.encode("ascii")).hexdigest(), digest)

    def test_staged_index_change_is_not_misreported_as_unchanged_head(self):
        first = self.context()
        (self.root / "new.txt").write_bytes(b"staged")
        local_git(self.root, "add", "new.txt")
        second = self.context()
        self.assertEqual(first["checkout_commit"], second["checkout_commit"])
        self.assertNotEqual(first["index_sha256"], second["index_sha256"])

    def test_each_file_digest_detects_working_byte_changes(self):
        for path, key in ((self.validator, "validator_file_sha256"),
                          (self.renderer, "diagnostic_file_sha256"),
                          (self.baseline, "baseline_file_sha256")):
            with self.subTest(path=path.name):
                before = self.context()
                original = path.read_bytes()
                path.write_bytes(original + b"\n")
                self.assertNotEqual(before[key], self.context()[key])
                path.write_bytes(original)

    def test_run_attempt_and_event_change_the_binding(self):
        first = DIAGNOSTICS._context_record(self.root, self.baseline)
        for key, value in (("GITHUB_RUN_ID", "124"), ("GITHUB_RUN_ATTEMPT", "3"),
                           ("GITHUB_EVENT_NAME", "push")):
            with self.subTest(key=key), mock.patch.dict(os.environ, {key: value}):
                self.assertNotEqual(first, DIAGNOSTICS._context_record(self.root, self.baseline))

    def test_local_context_without_github_environment_is_explicit(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            value = self.context()
        self.assertIsNone(value["github_run_id"])
        self.assertIsNone(value["github_run_attempt"])
        self.assertIsNone(value["github_event_name"])

    def test_arbitrary_environment_is_never_projected(self):
        with mock.patch.dict(os.environ, {"TOKEN": "PRIVATE_SECRET", "KFM_TRUSTED_BASE_REF": "PRIVATE_REF"}):
            _, payload = DIAGNOSTICS._context_record(self.root, self.baseline)
        self.assertNotIn("PRIVATE", payload)
        self.assertNotIn(str(self.root), payload)
        self.assertNotIn("expires_on", payload)
        self.assertNotIn("source", payload)

    def test_untrusted_run_metadata_is_unavailable_not_echoed(self):
        for key in ("GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_EVENT_NAME"):
            for value in ("", "0", "::error::PRIVATE\n", "9" * 21, "\u202e"):
                with self.subTest(key=key, value=repr(value)), mock.patch.dict(os.environ, {key: value}):
                    self.assertIsNone(DIAGNOSTICS._context_record(self.root, self.baseline))

    def test_malformed_git_identity_is_not_projected(self):
        for value in (b"bad\n", b"a" * 39, b"a" * 41, b"::error::PRIVATE\n", b"\xff"):
            with self.subTest(value=value), mock.patch.object(DOUBLE, "_git", return_value=value):
                self.assertIsNone(DIAGNOSTICS._context_record(self.root, self.baseline))

    def test_file_budget_is_enforced(self):
        with mock.patch.object(DIAGNOSTICS, "CONTEXT_MAX_BYTES", 2):
            self.assertIsNone(DIAGNOSTICS._context_record(self.root, self.baseline))

    def test_index_budget_is_enforced(self):
        with mock.patch.object(DIAGNOSTICS, "CONTEXT_MAX_INDEX_BYTES", 1):
            self.assertIsNone(DIAGNOSTICS._context_record(self.root, self.baseline))

    def test_outside_file_is_rejected_without_reading(self):
        with tempfile.TemporaryDirectory() as other:
            outside = Path(other) / "secret"
            outside.write_bytes(b"PRIVATE")
            self.assertIsNone(DIAGNOSTICS._context_record(self.root, outside))

    def test_missing_directory_and_symlink_inputs_are_unavailable(self):
        for path in (self.root / "missing", self.lane):
            with self.subTest(path=path.name):
                self.assertIsNone(DIAGNOSTICS._context_record(self.root, path))
        alias = self.root / "alias"
        alias.symlink_to(self.lane, target_is_directory=True)
        self.assertIsNone(DIAGNOSTICS._context_record(self.root, alias / self.baseline.name))
        file_alias = self.root / "file_alias"
        file_alias.symlink_to(self.baseline)
        self.assertIsNone(DIAGNOSTICS._context_record(self.root, file_alias))

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO check requires POSIX")
    def test_fifo_is_rejected_without_blocking(self):
        fifo = self.root / "fifo"
        os.mkfifo(fifo)
        self.assertIsNone(DIAGNOSTICS._context_record(self.root, fifo))

    def test_begin_end_ids_match_and_status_is_preserved(self):
        for code in (0, 1, 2):
            with self.subTest(code=code):
                actual, output = self.framed(code)
                self.assertEqual(code, actual)
                lines = output.splitlines()
                self.assertEqual(2, len(lines))
                identity = lines[0].split(" id=", 1)[1].split(" ", 1)[0]
                self.assertIn(f"status=UNCHANGED id={identity} validator_exit={code}", lines[1])
                self.assertNotIn("::", output)
                self.assertTrue(all(ord(c) < 128 for c in output))

    def test_unavailable_or_changed_context_never_overrides_validator_exit(self):
        for before, after in ((None, ("b", "{}")), (("a", "{}"), None),
                              (("a", "{}"), ("b", "{}"))):
            for code in (0, 1, 2):
                with self.subTest(before=before, after=after, code=code):
                    actual, output = self.framed(code, before, after)
                    self.assertEqual(code, actual)
                    self.assertIn(f"status=NON_COMPARABLE validator_exit={code}", output)

    def test_exception_text_is_not_a_context_field(self):
        for error in (OSError("PRIVATE_PATH"), ValueError("PRIVATE_REF")):
            with self.subTest(error=type(error)), mock.patch.object(DIAGNOSTICS, "execution_context", side_effect=error):
                actual, output = self.framed(1)
                self.assertEqual(1, actual)
                self.assertNotIn("PRIVATE", output)
                self.assertIn("status=NON_COMPARABLE", output)

    def test_unexpected_ratchet_exception_is_not_relabelled_as_a_result(self):
        output = io.StringIO()
        with mock.patch.object(DIAGNOSTICS, "main", side_effect=RuntimeError("test")), redirect_stdout(output):
            with self.assertRaises(RuntimeError):
                DIAGNOSTICS.run_with_context(self.args)
        self.assertIn("validator_exit=UNKNOWN", output.getvalue())

    def test_cli_entrypoint_uses_binding_not_the_unframed_main(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        guard = tree.body[-1]
        self.assertIsInstance(guard, ast.If)
        call = guard.body[0].exc
        self.assertIsInstance(call, ast.Call)
        self.assertEqual("SystemExit", call.func.id)
        self.assertEqual("run_with_context", call.args[0].func.id)

    def test_real_process_fixture_preserves_exit_and_frames_one_run(self):
        for code in (0, 1, 2):
            with self.subTest(code=code):
                env = dict(os.environ, FIXTURE_EXIT=str(code), PYTHONDONTWRITEBYTECODE="1")
                result = subprocess.run([sys.executable, str(self.renderer), *self.args],
                                        cwd=self.root, env=env, capture_output=True,
                                        text=True, timeout=15)
                self.assertEqual(code, result.returncode, result.stderr)
                lines = result.stdout.splitlines()
                self.assertEqual(3, len(lines), result.stdout)
                self.assertTrue(lines[0].startswith("TOPOLOGY_CONTEXT_BEGIN id="))
                self.assertTrue(lines[1].startswith("FIXTURE_RESULT:"))
                self.assertIn(f"status=UNCHANGED", lines[2])
                self.assertIn(f"validator_exit={code}", lines[2])

    def test_real_process_detects_baseline_change_during_scan(self):
        env = dict(os.environ, FIXTURE_MUTATE="1", PYTHONDONTWRITEBYTECODE="1")
        result = subprocess.run([sys.executable, str(self.renderer), *self.args], cwd=self.root,
                                env=env, capture_output=True, text=True, timeout=15)
        self.assertEqual(1, result.returncode, result.stderr)
        self.assertIn("status=NON_COMPARABLE validator_exit=1", result.stdout)

    def test_real_process_scan_error_is_still_error_without_private_text(self):
        env = dict(os.environ, FIXTURE_CRASH="1", PYTHONDONTWRITEBYTECODE="1")
        result = subprocess.run([sys.executable, str(self.renderer), *self.args], cwd=self.root,
                                env=env, capture_output=True, text=True, timeout=15)
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertIn("reason=SCAN_ERROR", result.stdout)
        self.assertNotIn("PRIVATE_EXCEPTION", result.stdout)
        self.assertIn("validator_exit=2", result.stdout)


if __name__ == "__main__":
    unittest.main()
