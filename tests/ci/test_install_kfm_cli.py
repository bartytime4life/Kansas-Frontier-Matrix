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
        self.assertEqual("-I", dependency[1])
        self.assertEqual("-I", local[1])
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

    def test_lock_validation_rejects_conditional_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "conditional.lock"
            path.write_text(
                "typer==0.27.2; python_version >= '3.11' \\\n"
                f"    --hash=sha256:{'0' * 64}\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                module.CliInstallConfigurationError,
                "^CLI_LOCKFILE_REQUIREMENT_UNSAFE$",
            ):
                module.validate_lockfile(path)

    def test_install_executes_argument_vectors_without_a_shell(self) -> None:
        with (
            mock.patch.object(module.time, "monotonic", side_effect=(100.0, 100.0, 150.0)),
            mock.patch.object(module.subprocess, "run") as run,
        ):
            module.install()
        self.assertEqual(2, run.call_count)
        for call in run.call_args_list:
            self.assertIsInstance(call.args[0], tuple)
            self.assertIs(call.kwargs["shell"], False)
            self.assertIs(call.kwargs["check"], True)
            self.assertEqual(REPO_ROOT, call.kwargs["cwd"])
            self.assertIs(module.subprocess.DEVNULL, call.kwargs["stdin"])
        self.assertEqual(
            [300.0, 250.0],
            [call.kwargs["timeout"] for call in run.call_args_list],
        )

    def test_install_timeout_fails_closed_before_second_command(self) -> None:
        expired = module.subprocess.TimeoutExpired(
            cmd=("python", "-m", "pip"),
            timeout=module.INSTALL_TIMEOUT_SECONDS,
        )
        with (
            mock.patch.object(module.time, "monotonic", side_effect=(100.0, 100.0)),
            mock.patch.object(module.subprocess, "run", side_effect=expired) as run,
        ):
            with self.assertRaisesRegex(
                module.CliInstallConfigurationError,
                "^CLI_INSTALL_TIMEOUT$",
            ):
                module.install()
        self.assertEqual(1, run.call_count)

    def test_install_uses_one_deadline_across_both_commands(self) -> None:
        with (
            mock.patch.object(module.time, "monotonic", side_effect=(100.0, 100.0, 401.0)),
            mock.patch.object(module.subprocess, "run") as run,
        ):
            with self.assertRaisesRegex(
                module.CliInstallConfigurationError,
                "^CLI_INSTALL_TIMEOUT$",
            ):
                module.install()
        self.assertEqual(1, run.call_count)

    def test_install_command_failure_uses_finite_error_and_stops(self) -> None:
        failed = module.subprocess.CalledProcessError(
            returncode=1,
            cmd=("python", "-m", "pip"),
        )
        with (
            mock.patch.object(module.time, "monotonic", side_effect=(100.0, 100.0)),
            mock.patch.object(module.subprocess, "run", side_effect=failed) as run,
        ):
            with self.assertRaisesRegex(
                module.CliInstallConfigurationError,
                "^CLI_INSTALL_COMMAND_FAILED$",
            ):
                module.install()
        self.assertEqual(1, run.call_count)

    def test_install_execution_failure_uses_finite_error_and_stops(self) -> None:
        failed = OSError("synthetic launch failure")
        with (
            mock.patch.object(module.time, "monotonic", side_effect=(100.0, 100.0)),
            mock.patch.object(module.subprocess, "run", side_effect=failed) as run,
        ):
            with self.assertRaisesRegex(
                module.CliInstallConfigurationError,
                "^CLI_INSTALL_EXECUTION_FAILED$",
            ):
                module.install()
        self.assertEqual(1, run.call_count)

    def test_install_closes_ambient_process_controls(self) -> None:
        inherited = {
            "PIP_CONSTRAINT": "/outside/constraint.txt",
            "PIP_INDEX_URL": "https://packages.invalid/simple",
            "PIP_REQUIREMENT": "/outside/requirements.txt",
            "PIP_TARGET": "/outside/target",
            "PYTHONHOME": "/outside/python-home",
            "pythonpath": "/outside/imports",
            "PyThOnUsErBaSe": "/outside/user-base",
            "UNRELATED_STATE": "preserved",
        }
        with (
            mock.patch.dict(module.os.environ, inherited, clear=False),
            mock.patch.object(module.time, "monotonic", side_effect=(100.0, 100.0, 150.0)),
            mock.patch.object(module.subprocess, "run") as run,
        ):
            module.install()
        self.assertEqual(2, run.call_count)
        for call in run.call_args_list:
            environment = call.kwargs["env"]
            self.assertFalse(any(key.upper().startswith("PIP_") for key in environment if key not in {
                "PIP_CONFIG_FILE",
                "PIP_DISABLE_PIP_VERSION_CHECK",
                "PIP_NO_INPUT",
            }))
            self.assertEqual(module.os.devnull, environment["PIP_CONFIG_FILE"])
            self.assertEqual("1", environment["PIP_DISABLE_PIP_VERSION_CHECK"])
            self.assertEqual("1", environment["PIP_NO_INPUT"])
            self.assertFalse(
                any(
                    key.upper() in module.UNSAFE_PYTHON_ENVIRONMENT
                    for key in environment
                )
            )
            self.assertEqual("1", environment["PYTHONNOUSERSITE"])
            self.assertEqual("preserved", environment["UNRELATED_STATE"])

    def test_main_rejects_arguments(self) -> None:
        with self.assertRaises(module.CliInstallConfigurationError):
            module.main(["anything"])


if __name__ == "__main__":
    unittest.main()
