from __future__ import annotations

import json
import os
import stat
import sys
from pathlib import Path

from tools.validate_all import (
    EXIT_ERROR,
    EXIT_OK,
    EXIT_VALIDATION,
    ValidatorSpec,
    main,
    run_validators,
    serialize_report,
)


def _script(path: Path, body: str) -> Path:
    path.write_text("#!/usr/bin/env python3\n" + body, encoding="utf-8")
    path.chmod(path.stat().st_mode | stat.S_IXUSR)
    return path


def test_registry_order_and_deterministic_json(tmp_path: Path) -> None:
    first = _script(tmp_path / "first.py", "print('first')\n")
    second = _script(tmp_path / "second.py", "print('second')\n")
    specs = (
        ValidatorSpec("first", first, ()),
        ValidatorSpec("second", second, ()),
    )

    report, exit_code = run_validators(specs, repo_root=tmp_path)
    assert exit_code == EXIT_OK
    assert [item["name"] for item in report["results"]] == ["first", "second"]
    assert serialize_report(report, "json") == serialize_report(report, "json")


def test_finite_exit_mapping(tmp_path: Path) -> None:
    passed = _script(tmp_path / "pass.py", "raise SystemExit(0)\n")
    failed = _script(tmp_path / "fail.py", "raise SystemExit(1)\n")
    errored = _script(tmp_path / "error.py", "raise SystemExit(2)\n")

    report, exit_code = run_validators(
        (
            ValidatorSpec("pass", passed, ()),
            ValidatorSpec("fail", failed, ()),
        ),
        repo_root=tmp_path,
    )
    assert exit_code == EXIT_VALIDATION
    assert report["outcome"] == "FAIL"

    report, exit_code = run_validators(
        (ValidatorSpec("error", errored, ()),),
        repo_root=tmp_path,
    )
    assert exit_code == EXIT_ERROR
    assert report["outcome"] == "ERROR"


def test_warning_policy_is_explicit(tmp_path: Path) -> None:
    warning = _script(tmp_path / "warning.py", "print('WARNING fixture warning')\n")
    specs = (ValidatorSpec("warning", warning, ()),)

    report, exit_code = run_validators(specs, repo_root=tmp_path)
    assert exit_code == EXIT_OK
    assert report["outcome"] == "WARNING"

    report, exit_code = run_validators(
        specs,
        repo_root=tmp_path,
        fail_on_warning=True,
    )
    assert exit_code == EXIT_VALIDATION
    assert report["outcome"] == "FAIL"


def test_child_environment_is_deterministic_and_no_network(tmp_path: Path) -> None:
    probe = _script(
        tmp_path / "probe.py",
        (
            "import os\n"
            "assert os.environ['KFM_NO_NETWORK'] == '1'\n"
            "assert os.environ['PYTHONHASHSEED'] == '0'\n"
            "assert os.environ['TZ'] == 'UTC'\n"
        ),
    )
    report, exit_code = run_validators(
        (ValidatorSpec("probe", probe, ()),),
        repo_root=tmp_path,
    )
    assert exit_code == EXIT_OK
    assert report["outcome"] == "PASS"


def test_missing_validator_is_system_error(tmp_path: Path) -> None:
    report, exit_code = run_validators(
        (ValidatorSpec("missing", tmp_path / "missing.py", ()),),
        repo_root=tmp_path,
    )
    assert exit_code == EXIT_ERROR
    assert report["results"][0]["diagnostics"] == ["validator file is missing"]


def test_selection_list_and_unknown_name(
    tmp_path: Path,
    capsys,
) -> None:
    passed = _script(tmp_path / "pass.py", "raise SystemExit(0)\n")
    registry = (ValidatorSpec("fixture-pass", passed, ()),)

    assert main(["--list"], registry=registry, repo_root=tmp_path) == EXIT_OK
    assert capsys.readouterr().out == "fixture-pass\n"

    assert (
        main(
            ["--only", "fixture-pass", "--format", "json"],
            registry=registry,
            repo_root=tmp_path,
        )
        == EXIT_OK
    )
    payload = json.loads(capsys.readouterr().out)
    assert payload["results"][0]["name"] == "fixture-pass"

    assert (
        main(
            ["--only", "unknown", "--format", "json"],
            registry=registry,
            repo_root=tmp_path,
        )
        == EXIT_ERROR
    )
    error = json.loads(capsys.readouterr().out)
    assert error["error"]["code"] == "ORCHESTRATOR_CONFIGURATION_ERROR"


def test_junit_and_atomic_report(tmp_path: Path, capsys) -> None:
    passed = _script(tmp_path / "pass.py", "print('ok')\n")
    report_path = tmp_path / "reports" / "validation.xml"
    registry = (ValidatorSpec("fixture-pass", passed, ()),)

    exit_code = main(
        [
            "--only",
            "fixture-pass",
            "--format",
            "junit",
            "--report",
            str(report_path),
        ],
        registry=registry,
        repo_root=tmp_path,
    )
    assert exit_code == EXIT_OK
    stdout = capsys.readouterr().out
    assert stdout == report_path.read_text(encoding="utf-8")
    assert '<testcase classname="kfm-validate-all" name="fixture-pass"' in stdout
