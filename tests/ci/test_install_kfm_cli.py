from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/ci/install_kfm_cli.py"
SPEC = importlib.util.spec_from_file_location("kfm_install_cli", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class InstallKfmCliTests(unittest.TestCase):
    def test_committed_lock_pins_cli_dependencies(self) -> None:
        text = module.LOCKFILE.read_text(encoding="utf-8").lower()
        for name in ("hydra-core", "omegaconf", "rich", "typer"):
            self.assertIn(f"{name}==", text)
        module.validate_lockfile()

    def test_commands_use_hash_lock_and_fixed_local_package(self) -> None:
        dependency, local = module.build_commands(executable="python")
        self.assertEqual("python", dependency[0])
        self.assertIn("--require-hashes", dependency)
        self.assertEqual(str(module.LOCKFILE), dependency[-1])
        self.assertIn("--no-deps", local)
        self.assertIn("--no-build-isolation", local)
        self.assertEqual("--editable", local[-2])
        self.assertEqual(module.LOCAL_SPEC, local[-1])

    def test_lock_validation_rejects_unhashed_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "unsafe.lock"
            path.write_text("typer==0.27.2\n", encoding="utf-8")
            with self.assertRaises(module.CliInstallConfigurationError):
                module.validate_lockfile(path)

    def test_lock_validation_rejects_network_source_override(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "unsafe.lock"
            path.write_text(
                "--extra-index-url https://packages.example.invalid/simple\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                module.CliInstallConfigurationError,
                "CLI_LOCKFILE_SOURCE_UNSAFE",
            ):
                module.validate_lockfile(path)

    def test_lock_validation_binds_hashes_to_each_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "unsafe.lock"
            path.write_text(
                "typer==0.27.2 \\\n"
                f"    --hash=sha256:{'a' * 64} \\\n"
                f"    --hash=sha256:{'b' * 64}\n"
                "rich==15.0.0 \\\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                module.CliInstallConfigurationError,
                "CLI_LOCKFILE_HASH_COVERAGE_INVALID",
            ):
                module.validate_lockfile(path)

    def test_local_package_validation_rejects_outside_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)
            with self.assertRaisesRegex(
                module.CliInstallConfigurationError,
                "CLI_LOCAL_PACKAGE_OUTSIDE_REPOSITORY",
            ):
                module.validate_local_package(path)

    def test_install_executes_argument_vectors_without_a_shell(self) -> None:
        with mock.patch.object(module.subprocess, "run") as run:
            module.install()
        self.assertEqual(2, run.call_count)
        for call in run.call_args_list:
            self.assertIsInstance(call.args[0], tuple)
            self.assertIs(call.kwargs["shell"], False)
            self.assertIs(call.kwargs["check"], True)
            self.assertEqual(REPO_ROOT, call.kwargs["cwd"])

    def test_main_rejects_arguments(self) -> None:
        with self.assertRaises(module.CliInstallConfigurationError):
            module.main(["anything"])


if __name__ == "__main__":
    unittest.main()
