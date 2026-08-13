from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/ci/install_python_ci.py"
SPEC = importlib.util.spec_from_file_location("kfm_install_python_ci", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class InstallPythonCiTests(unittest.TestCase):
    def test_all_profiles_use_hashes_and_disable_local_resolution(self) -> None:
        self.assertEqual(
            {
                "all-local-test",
                "audit-tool",
                "connectors-core",
                "project-runtime",
                "project-test",
                "project-test-hashing",
                "project-test-hashing-test",
                "project-test-schema-registry-test",
                "project-test-wheel",
                "test-dependencies",
            },
            set(module.PROFILES),
        )
        for name, profile in module.PROFILES.items():
            with self.subTest(profile=name):
                commands = module.build_commands(name, executable="python")
                self.assertIn("--require-hashes", commands[0])
                self.assertIn("--requirement", commands[0])
                if profile.local_specs:
                    self.assertEqual(2, len(commands))
                    self.assertIn("--no-deps", commands[1])
                    self.assertIn("--no-build-isolation", commands[1])
                else:
                    self.assertEqual(1, len(commands))

    def test_committed_locks_pin_direct_dependencies(self) -> None:
        test_lock = (REPO_ROOT / "tools/ci/python-test.lock").read_text(
            encoding="utf-8"
        )
        for name in (
            "editables",
            "hatchling",
            "hypothesis",
            "jsonschema",
            "pyyaml",
            "pytest",
            "referencing",
            "rfc3339-validator",
            "rfc8785",
        ):
            self.assertIn(f"{name}==", test_lock.lower())
        audit_lock = (REPO_ROOT / "tools/ci/python-audit.lock").read_text(
            encoding="utf-8"
        )
        self.assertIn("pip-audit==2.10.1", audit_lock.lower())

    def test_lock_validation_rejects_unhashed_and_remote_sources(self) -> None:
        remote = (
            "thing @ https://example.invalid/thing.whl "
            + "\\\n    --hash=sha256:"
            + "a" * 64
            + "\n"
        )
        for content in ("pytest==9.1.1\n", remote):
            with (
                self.subTest(content=content),
                tempfile.TemporaryDirectory() as temp,
            ):
                path = Path(temp) / "unsafe.lock"
                path.write_text(content, encoding="utf-8")
                with self.assertRaises(module.InstallConfigurationError):
                    module.validate_lockfile(path)

    def test_install_executes_argument_vectors_without_a_shell(self) -> None:
        with mock.patch.object(module.subprocess, "run") as run:
            module.install("project-test")
        self.assertEqual(2, run.call_count)
        for call in run.call_args_list:
            self.assertIsInstance(call.args[0], tuple)
            self.assertIs(call.kwargs["shell"], False)
            self.assertIs(call.kwargs["check"], True)
            self.assertEqual(REPO_ROOT, call.kwargs["cwd"])

    def test_each_migrated_workflow_selects_one_known_profile(self) -> None:
        counts: dict[str, int] = {}
        for workflow in sorted((REPO_ROOT / ".github/workflows").glob("*.yml")):
            for profile in module.profiles_for_workflow(workflow):
                counts[profile] = counts.get(profile, 0) + 1
        self.assertGreaterEqual(sum(counts.values()), 388)
        self.assertEqual(1, counts["audit-tool"])
        self.assertEqual(1, counts["all-local-test"])


if __name__ == "__main__":
    unittest.main()
