"""Finite dependency composition and failure behavior; no package downloads."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
from unittest import mock

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "kfm_full_local_test", ROOT / "tools/ci/install_full_local_test.py"
)
assert SPEC and SPEC.loader
TOOL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TOOL)


def test_plan_uses_existing_validated_profiles_and_cli_installer() -> None:
    plan = TOOL.build_plan()
    assert plan["profiles"] == [
        "all-local-test", "water-pilot", "geo-transforms", "nwm-netcdf",
        "geoparquet-pyarrow-25",
    ]
    assert plan["commands"] == [
        [TOOL.sys.executable, str(TOOL.MODULE_DIR / "install_python_ci.py"), profile]
        for profile in TOOL.PROFILES
    ] + [[TOOL.sys.executable, str(TOOL.MODULE_DIR / "install_kfm_cli.py")]]
    assert plan["post_install_check"] == [TOOL.sys.executable, "-I", "-m", "pip", "check"]


def test_plan_never_installs_or_starts_subprocesses(capsys) -> None:
    with mock.patch.object(TOOL, "install") as install, mock.patch.object(TOOL.subprocess, "run") as run:
        assert TOOL.main(["--plan"]) == 0
    install.assert_not_called()
    run.assert_not_called()
    assert json.loads(capsys.readouterr().out)["profiles"] == list(TOOL.PROFILES)


@pytest.mark.parametrize("version,system,machine,prefix,code", [
    ((3, 10), "linux", "x86_64", "venv", "FULL_TEST_PYTHON_UNSUPPORTED"),
    ((3, 11), "linux", "x86_64", "venv", "FULL_TEST_PYTHON_UNSUPPORTED"),
    ((3, 13), "linux", "x86_64", "venv", "FULL_TEST_PYTHON_UNSUPPORTED"),
    ((3, 12), "darwin", "x86_64", "venv", "FULL_TEST_PLATFORM_UNSUPPORTED"),
    ((3, 12), "linux", "aarch64", "venv", "FULL_TEST_PLATFORM_UNSUPPORTED"),
    ((3, 12), "linux", "x86_64", "base", "FULL_TEST_VIRTUALENV_REQUIRED"),
])
def test_unsupported_environment_stops_before_installs(version, system, machine, prefix, code) -> None:
    with (mock.patch.object(TOOL.sys, "version_info", version),
          mock.patch.object(TOOL.sys, "platform", system),
          mock.patch.object(TOOL.platform, "machine", return_value=machine),
          mock.patch.object(TOOL.sys, "prefix", prefix),
          mock.patch.object(TOOL.sys, "base_prefix", "base"),
          mock.patch.object(TOOL.install_python_ci, "install") as install):
        with pytest.raises(TOOL.FullLocalTestConfigurationError, match=code):
            TOOL.install()
    install.assert_not_called()


def test_declared_linux_virtualenv_is_supported() -> None:
    with (mock.patch.object(TOOL.sys, "version_info", (3, 12)),
          mock.patch.object(TOOL.sys, "platform", "linux"),
          mock.patch.object(TOOL.platform, "machine", return_value="x86_64"),
          mock.patch.object(TOOL.sys, "prefix", "venv"),
          mock.patch.object(TOOL.sys, "base_prefix", "base")):
        TOOL.require_supported_environment()


def test_alternative_python_implementation_stops_before_installing() -> None:
    with (mock.patch.object(TOOL.sys, "version_info", (3, 12)),
          mock.patch.object(TOOL.platform, "python_implementation", return_value="PyPy"),
          mock.patch.object(TOOL.install_python_ci, "install") as install):
        with pytest.raises(TOOL.FullLocalTestConfigurationError, match="FULL_TEST_PYTHON_UNSUPPORTED"):
            TOOL.install()
    install.assert_not_called()


def test_invalid_last_input_prevents_every_install() -> None:
    with (mock.patch.object(TOOL, "require_supported_environment"),
          mock.patch.object(TOOL.install_kfm_cli, "build_commands",
                            side_effect=TOOL.install_kfm_cli.CliInstallConfigurationError("CLI_LOCKFILE_HASH_INVALID")),
          mock.patch.object(TOOL.install_python_ci, "install") as install,
          mock.patch.object(TOOL.install_kfm_cli, "install") as cli):
        with pytest.raises(TOOL.install_kfm_cli.CliInstallConfigurationError):
            TOOL.install()
    install.assert_not_called()
    cli.assert_not_called()


def test_failed_install_does_not_continue_to_later_profiles_or_cli(capsys) -> None:
    with (mock.patch.object(TOOL, "require_supported_environment"),
          mock.patch.object(TOOL.install_python_ci, "install",
                            side_effect=subprocess.CalledProcessError(1, ["python"])) as install,
          mock.patch.object(TOOL.install_kfm_cli, "install") as cli,
          mock.patch.object(TOOL.subprocess, "run") as run):
        assert TOOL.main([]) == 1
    install.assert_called_once_with("all-local-test")
    cli.assert_not_called()
    run.assert_not_called()
    assert "environment may be partial" in capsys.readouterr().err


def test_success_delegates_in_order_and_checks_dependency_consistency() -> None:
    calls = mock.Mock()
    with (mock.patch.object(TOOL, "require_supported_environment"),
          mock.patch.object(TOOL.install_python_ci, "install", calls.profile),
          mock.patch.object(TOOL.install_kfm_cli, "install", calls.cli),
          mock.patch.object(TOOL.subprocess, "run", calls.run)):
        TOOL.install()
    assert calls.mock_calls == [mock.call.profile(profile) for profile in TOOL.PROFILES] + [
        mock.call.cli(),
        mock.call.run([TOOL.sys.executable, "-I", "-m", "pip", "check"],
                      check=True, cwd=TOOL.REPO_ROOT, shell=False,
                      stdin=subprocess.DEVNULL, timeout=300),
    ]


def test_unknown_dependency_argument_is_rejected_without_installing() -> None:
    with mock.patch.object(TOOL, "install") as install:
        with pytest.raises(SystemExit) as error:
            TOOL.main(["--profile", "unreviewed"])
    assert error.value.code == 2
    install.assert_not_called()
