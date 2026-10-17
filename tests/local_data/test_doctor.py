"""Local-source prerequisite checks remain bounded and read-only."""

from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
from pathlib import Path

import pytest

from tools.local_data import doctor


@pytest.fixture
def source(tmp_path: Path) -> Path:
    for relative in doctor.REQUIRED_FILES:
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture source file\n", encoding="utf-8")
    return tmp_path


def test_zip_source_does_not_require_git_or_optional_tools(source: Path) -> None:
    report = doctor.inspect(source, python_version=(3, 11, 0), locate=lambda _: None)
    assert report["outcome"] == "PASS"
    assert report["source_kind"] == "SOURCE_DIRECTORY"
    assert all(item["availability"] == "MISSING" for item in report["optional_tools"])
    assert "application-integration" in report["not_checked"]


@pytest.mark.parametrize("git_marker", ["directory", "worktree-file"])
def test_git_metadata_marker_is_only_an_observation(source: Path, git_marker: str) -> None:
    marker = source / ".git"
    if git_marker == "directory":
        marker.mkdir()
    else:
        marker.write_text("gitdir: /not-inspected\n", encoding="utf-8")
    report = doctor.inspect(source, python_version=(3, 12, 1), locate=lambda _: None)
    assert report["outcome"] == "PASS"
    assert report["source_kind"] == "GIT_METADATA_PRESENT"
    assert "git-history-and-update-status" in report["not_checked"]


@pytest.mark.parametrize("version", [(3, 9, 20), (3, 10, 15)])
def test_unsupported_python_fails_without_optional_tool_dependency(source: Path, version) -> None:
    report = doctor.inspect(source, python_version=version, locate=lambda _: "/available")
    assert report["outcome"] == "FAIL"
    assert report["local_data_prerequisites"] == "NOT_READY"
    assert report["checks"][0]["status"] == "FAIL"


@pytest.mark.parametrize("relative", doctor.REQUIRED_FILES)
def test_incomplete_source_fails(source: Path, relative: str) -> None:
    (source / relative).unlink()
    report = doctor.inspect(source, python_version=(3, 11, 0), locate=lambda _: None)
    assert report["outcome"] == "FAIL"
    failures = [check for check in report["checks"] if check["status"] == "FAIL"]
    assert failures == [{
        "id": "source_file", "path": relative,
        "status": "FAIL", "reason": "MISSING_OR_NOT_FILE",
    }]


def test_directory_cannot_substitute_for_required_source(source: Path) -> None:
    path = source / "tools/local_data/manage.py"
    path.unlink()
    path.mkdir()
    assert doctor.inspect(source, locate=lambda _: None)["outcome"] == "FAIL"


def test_optional_tool_location_does_not_claim_version_compatibility(source: Path) -> None:
    report = doctor.inspect(source, locate=lambda _: "/private/tool/location")
    assert all(item["version"] == "NOT_CHECKED" for item in report["optional_tools"])
    assert "/private/tool/location" not in json.dumps(report)


def test_inspection_is_deterministic_no_network_no_subprocess_no_writes(source: Path, monkeypatch) -> None:
    def forbidden(*args, **kwargs):
        raise AssertionError("unexpected side effect")

    before = {str(path.relative_to(source)): path.read_bytes() for path in source.rglob("*") if path.is_file()}
    monkeypatch.setattr(socket, "socket", forbidden)
    monkeypatch.setattr(subprocess, "Popen", forbidden)
    monkeypatch.setattr(Path, "write_text", forbidden)
    monkeypatch.setattr(Path, "write_bytes", forbidden)
    first = doctor.inspect(source, python_version=(3, 12, 1), locate=lambda _: None)
    second = doctor.inspect(source, python_version=(3, 12, 1), locate=lambda _: None)
    after = {str(path.relative_to(source)): path.read_bytes() for path in source.rglob("*") if path.is_file()}
    assert first == second
    assert before == after
    assert first["side_effects"] == {
        "files_written": False, "commands_executed": False,
        "network_requests": False, "services_started": False,
    }


def test_cli_machine_json_and_failure_status(source: Path, capsys) -> None:
    assert doctor.main(["--repo-root", str(source)]) == 0
    assert json.loads(capsys.readouterr().out)["outcome"] == "PASS"
    (source / "pyproject.toml").unlink()
    assert doctor.main(["--repo-root", str(source)]) == 1
    assert json.loads(capsys.readouterr().out)["outcome"] == "FAIL"


def test_water_runtime_rejects_repository_namespace_directories(source: Path, tmp_path: Path) -> None:
    for name in ("catalog", "release"):
        (tmp_path / name).mkdir()
    env = {**os.environ, "PYTHONPATH": str(tmp_path)}
    env.pop("KFM_RELEASE_STORE", None)
    result = subprocess.run(
        [sys.executable, "-S", str(Path(doctor.__file__).resolve()),
         "--repo-root", str(source), "--water-runtime"],
        cwd=tmp_path, env=env, capture_output=True, text=True, check=False,
    )
    assert result.returncode == 1, result.stderr
    report = json.loads(result.stdout)
    checks = {item["name"]: item for item in report["water_runtime"]["dependencies"]}
    assert checks["catalog"]["status"] == "FAIL"
    assert checks["release"]["status"] == "FAIL"
    assert checks["catalog"]["module"] == "catalog.core"
    assert checks["release"]["module"] == "release.local_store"
    assert report["water_runtime"]["dependency_compatibility"] == "NOT_CHECKED"
    assert report["water_runtime"]["release_store"] == "NOT_CONFIGURED"


def test_module_discovery_does_not_execute_package_or_module(tmp_path: Path, monkeypatch) -> None:
    package = tmp_path / "doctor_probe_fixture"
    package.mkdir()
    (package / "__init__.py").write_text("raise AssertionError('package executed')\n")
    (package / "runtime.py").write_text("raise AssertionError('module executed')\n")
    monkeypatch.syspath_prepend(str(tmp_path))

    def forbidden(*args, **kwargs):
        raise AssertionError("unexpected side effect")

    monkeypatch.setattr(socket, "socket", forbidden)
    monkeypatch.setattr(subprocess, "Popen", forbidden)
    monkeypatch.setattr(Path, "write_text", forbidden)
    monkeypatch.setattr(Path, "write_bytes", forbidden)
    assert doctor.module_present("doctor_probe_fixture.runtime") is True
    assert doctor.module_present("doctor_probe_fixture.missing") is False
    assert doctor.module_present("doctor_probe_fixture.runtime.child") is False
    assert "doctor_probe_fixture" not in sys.modules
    assert "doctor_probe_fixture.runtime" not in sys.modules


def test_namespace_cannot_substitute_for_implementation_module(tmp_path: Path, monkeypatch) -> None:
    (tmp_path / "doctor_namespace_fixture" / "runtime").mkdir(parents=True)
    monkeypatch.syspath_prepend(str(tmp_path))
    assert doctor.module_present("doctor_namespace_fixture.runtime") is False


@pytest.mark.parametrize("error", [ImportError, KeyError, OSError, ValueError])
def test_module_discovery_fails_closed_on_lookup_error(monkeypatch, error) -> None:
    def unavailable(*args, **kwargs):
        raise error("unavailable")

    monkeypatch.setattr(doctor, "find_spec", unavailable)
    assert doctor.module_present("doctor_probe_fixture.runtime") is False
