#!/usr/bin/env python3
"""Prepare a virtual environment for repository-wide Python test collection.

Compose the existing fixed, hash-locked installers without accepting dependency
names, URLs, paths or shell fragments. This installs test dependencies only;
collection, execution, source admission and release remain separate checks.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform
import subprocess
import sys
from typing import Sequence

MODULE_DIR = Path(__file__).resolve().parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import install_kfm_cli
import install_python_ci

REPO_ROOT = MODULE_DIR.parents[1]
PROFILES = (
    "all-local-test",
    "water-pilot",
    "geo-transforms",
    "nwm-netcdf",
    "geoparquet-pyarrow-25",
)


class FullLocalTestConfigurationError(ValueError):
    """The fixed bundle cannot be installed in this environment."""


def require_supported_environment() -> None:
    # The complete bundle includes an experiment pinned to a CPython 3.12 wheel.
    # Do not broaden that lock or its producer identity to make setup succeed.
    if (sys.version_info[:2] != (3, 12)
            or platform.python_implementation() != "CPython"):
        raise FullLocalTestConfigurationError("FULL_TEST_PYTHON_UNSUPPORTED")
    if sys.platform != "linux" or platform.machine().lower() != "x86_64":
        raise FullLocalTestConfigurationError("FULL_TEST_PLATFORM_UNSUPPORTED")
    if sys.prefix == sys.base_prefix:
        raise FullLocalTestConfigurationError("FULL_TEST_VIRTUALENV_REQUIRED")


def build_plan() -> dict[str, object]:
    """Validate every input before returning the non-mutating install plan."""
    for profile in PROFILES:
        install_python_ci.build_commands(profile)
    install_kfm_cli.build_commands()
    return {
        "environment": "Linux x86_64, CPython 3.12, active virtual environment",
        "profiles": list(PROFILES),
        "commands": [
            [sys.executable, str(MODULE_DIR / "install_python_ci.py"), profile]
            for profile in PROFILES
        ] + [[sys.executable, str(MODULE_DIR / "install_kfm_cli.py")]],
        "post_install_check": [sys.executable, "-I", "-m", "pip", "check"],
        "scope": "Dependency setup only; does not collect or run tests or start services.",
    }


def install() -> None:
    require_supported_environment()
    build_plan()  # Fail before any install if even the last lock/package is invalid.
    for profile in PROFILES:
        install_python_ci.install(profile)
    install_kfm_cli.install()
    subprocess.run(
        [sys.executable, "-I", "-m", "pip", "check"],
        check=True,
        cwd=REPO_ROOT,
        shell=False,
        stdin=subprocess.DEVNULL,
        timeout=300,
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true", help="Validate inputs and print the plan without installing")
    args = parser.parse_args(argv)
    try:
        if args.plan:
            print(json.dumps(build_plan(), indent=2))
        else:
            install()
            print("FULL_LOCAL_TEST_SETUP_COMPLETE: dependencies checked; tests not run")
    except (FullLocalTestConfigurationError,
            install_python_ci.InstallConfigurationError,
            install_kfm_cli.CliInstallConfigurationError) as error:
        print(str(error), file=sys.stderr)
        return 2
    except (subprocess.SubprocessError, OSError):
        print("FULL_LOCAL_TEST_INSTALL_FAILED: setup stopped; environment may be partial", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
