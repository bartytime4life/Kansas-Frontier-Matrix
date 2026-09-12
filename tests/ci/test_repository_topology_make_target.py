"""Exercise the real Make target with an argv-recording Python substitute.

This proves orchestration, not topology conformance. No validator, baseline,
GitHub API, package installer, or network service is run by this module. The
substitute fails on every unexpected invocation rather than simulating success.
"""
from __future__ import annotations

import itertools
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
EXPECTED_ARGV = [
    ["-m", "unittest", "discover", "--start-directory", "tests/ci", "--pattern",
     "test_repository_topology_make_target.py", "--verbose"],
    ["-m", "unittest", "discover", "--start-directory",
     "tests/validators/directory_governance", "--pattern",
     "test_validate_*topology*.py", "--verbose"],
    ["tools/validators/directory_governance/render_repository_topology_diagnostics.py"],
]
EXPECTED_ENV = {
    "KFM_NO_NETWORK": "1", "PYTHONHASHSEED": "0",
    "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUNBUFFERED": "1", "TZ": "UTC",
}
RECORDER = r'''import json, os, sys
from pathlib import Path
args = sys.argv[1:]
allowed = json.loads(os.environ["KFM_TEST_ARGV"])
with Path(os.environ["KFM_TEST_CALLS"]).open("a", encoding="utf-8") as stream:
    stream.write(json.dumps({"argv": args, "env": {
        name: os.environ.get(name) for name in json.loads(os.environ["KFM_TEST_ENV_KEYS"])
    }}, sort_keys=True) + "\n")
if args not in allowed:
    print("unexpected test invocation", file=sys.stderr)
    sys.exit(99)
index = allowed.index(args)
print("test-substitute lane=" + str(index), flush=True)
print("test-substitute stderr=" + str(index), file=sys.stderr, flush=True)
sys.exit(json.loads(os.environ["KFM_TEST_STATUSES"])[index])
'''


class RepositoryTopologyMakeTargetTests(unittest.TestCase):
    """Each failure remains fatal even when a later command succeeds."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.make = shutil.which("make")
        if cls.make is None:
            raise RuntimeError("make is required; this contract must not silently skip")
        cls.makefile = (REPO_ROOT / "Makefile").read_bytes()

    def run_target(
        self, statuses: tuple[int, int, int], *, shell: str = "/bin/sh",
        shell_flags: str = "-c", makefile: bytes | None = None,
        missing_contract: bool = False,
    ) -> tuple[subprocess.CompletedProcess[str], list[dict[str, object]]]:
        with tempfile.TemporaryDirectory(prefix="kfm-topology-make-") as temporary:
            root = Path(temporary)
            (root / "Makefile").write_bytes(self.makefile if makefile is None else makefile)
            if not missing_contract:
                contract = root / "tests/ci/test_repository_topology_make_target.py"
                contract.parent.mkdir(parents=True)
                contract.write_text("# Presence fixture; the recorder handles execution.\n")
            binary = root / "bin"
            binary.mkdir()
            interpreter = binary / "python"
            interpreter.write_text("#!" + sys.executable + "\n" + RECORDER, encoding="utf-8")
            interpreter.chmod(0o700)
            calls = root / "calls.jsonl"
            environment = os.environ.copy()
            for name in ("MAKEFLAGS", "MFLAGS", "GNUMAKEFLAGS", "MAKEFILES"):
                environment.pop(name, None)
            environment.update({
                "PATH": str(binary) + os.pathsep + os.defpath,
                "KFM_TEST_CALLS": str(calls),
                "KFM_TEST_ARGV": json.dumps(EXPECTED_ARGV),
                "KFM_TEST_ENV_KEYS": json.dumps(list(EXPECTED_ENV)),
                "KFM_TEST_STATUSES": json.dumps(statuses),
            })
            # Start with hostile-but-finite values; the target must set all five.
            environment.update({name: "incorrect" for name in EXPECTED_ENV})
            result = subprocess.run(
                [self.make, "--no-print-directory", "-rR", "-f", "Makefile",
                 "SHELL=" + shell, ".SHELLFLAGS=" + shell_flags, "repository-topology"],
                cwd=root, env=environment, capture_output=True, text=True,
                check=False, timeout=15,
            )
            records = [json.loads(line) for line in calls.read_text().splitlines()] if calls.exists() else []
            return result, records

    def assert_contract(
        self, statuses: tuple[int, int, int], **options: object,
    ) -> None:
        result, calls = self.run_target(statuses, **options)
        self.assertEqual(EXPECTED_ARGV, [call["argv"] for call in calls])
        for call in calls:
            self.assertEqual(EXPECTED_ENV, call["env"])
        self.assertEqual(0 if statuses == (0, 0, 0) else 2, result.returncode,
                         result.stdout + result.stderr)
        self.assertIn("repository-topology statuses: contract=%d tests=%d diagnostics=%d" % statuses,
                      result.stdout)
        for index in range(3):
            self.assertIn("test-substitute lane=" + str(index), result.stdout)
            self.assertIn("test-substitute stderr=" + str(index), result.stderr)

    def test_all_eight_pass_failure_combinations(self) -> None:
        for statuses in itertools.product((0, 1), repeat=3):
            with self.subTest(statuses=statuses):
                self.assert_contract(statuses)

    def test_nonstandard_failure_codes_are_not_accepted(self) -> None:
        for index, status in itertools.product(range(3), (2, 7, 126, 127, 130, 143)):
            statuses = tuple(status if lane == index else 0 for lane in range(3))
            with self.subTest(statuses=statuses):
                self.assert_contract(statuses)

    def test_errexit_does_not_prevent_independent_collection(self) -> None:
        for statuses in ((1, 0, 0), (0, 1, 0), (1, 1, 1)):
            with self.subTest(statuses=statuses):
                self.assert_contract(statuses, shell_flags="-ec")

    def test_bash_has_the_same_failure_boundary(self) -> None:
        bash = shutil.which("bash")
        self.assertIsNotNone(bash, "Bash is required by the hosted CI contract")
        for statuses in ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)):
            with self.subTest(statuses=statuses):
                self.assert_contract(statuses, shell=bash, shell_flags="-euc")

    def test_missing_contract_module_is_failure_not_empty_success(self) -> None:
        result, calls = self.run_target((0, 0, 0), missing_contract=True)
        self.assertEqual(2, result.returncode)
        self.assertEqual(EXPECTED_ARGV[1:], [call["argv"] for call in calls])
        self.assertIn("contract=1 tests=0 diagnostics=0", result.stdout)

    def test_original_fail_fast_target_is_discriminated(self) -> None:
        prefix = " ".join(name + "=" + value for name, value in EXPECTED_ENV.items()).encode()
        original = b"repository-topology:\n\t" + prefix + b" python " + b" ".join(
            argument.encode() if "*" not in argument else ("'" + argument + "'").encode()
            for argument in EXPECTED_ARGV[1]
        ) + b"\n\t" + prefix + b" python " + EXPECTED_ARGV[2][0].encode() + b"\n"
        result, calls = self.run_target((0, 1, 0), makefile=original)
        self.assertEqual(2, result.returncode)
        self.assertEqual([EXPECTED_ARGV[1]], [call["argv"] for call in calls])
        self.assertNotIn("test-substitute lane=2", result.stdout)


if __name__ == "__main__":
    unittest.main()
