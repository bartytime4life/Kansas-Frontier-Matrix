from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.validators.dependencies.pnpm_audit_readiness import (
    EXIT_ERROR,
    EXIT_PASS,
    EXIT_REGRESSION,
    classify_audit,
    main,
    render_report,
    validate_repository,
)


WORKSPACES = ["apps/*", "packages/*"]
IMPORTERS = [
    ".",
    "apps/explorer-web",
    "apps/review-console",
    "packages/maplibre",
    "packages/ui",
]


def _write_repository(
    root: Path,
    *,
    manager: str = "pnpm@11.17.0",
    manifest_workspaces: list[str] | None = None,
    pnpm_workspaces: list[str] | None = None,
    importers: list[str] | None = None,
) -> None:
    manifest_workspaces = manifest_workspaces or WORKSPACES
    pnpm_workspaces = pnpm_workspaces or WORKSPACES
    importers = importers or IMPORTERS

    (root / "package.json").write_text(
        json.dumps(
            {
                "name": "fixture",
                "private": True,
                "packageManager": manager,
                "engines": {"node": ">=22.13 <23"},
                "workspaces": manifest_workspaces,
            }
        ),
        encoding="utf-8",
    )
    (root / "pnpm-workspace.yaml").write_text(
        "packages:\n"
        + "".join(f'  - "{pattern}"\n' for pattern in pnpm_workspaces),
        encoding="utf-8",
    )
    for importer in IMPORTERS[1:]:
        package_dir = root / importer
        package_dir.mkdir(parents=True)
        (package_dir / "package.json").write_text(
            json.dumps({"name": importer.replace("/", "-"), "private": True}),
            encoding="utf-8",
        )
    (root / "pnpm-lock.yaml").write_text(
        "lockfileVersion: '9.0'\n\n"
        "settings:\n"
        "  autoInstallPeers: true\n\n"
        "importers:\n\n"
        + "".join(f"  {importer}: {{}}\n" for importer in importers)
        + "\npackages: {}\n",
        encoding="utf-8",
    )


def _write_audit_report(path: Path, **counts: int) -> None:
    vulnerabilities = {
        "info": 0,
        "low": 0,
        "moderate": 0,
        "high": 0,
        "critical": 0,
        **counts,
    }
    path.write_text(
        json.dumps(
            {
                "actions": [],
                "advisories": {},
                "metadata": {
                    "vulnerabilities": vulnerabilities,
                    "dependencies": 5,
                },
            }
        ),
        encoding="utf-8",
    )


def test_current_contract_is_ready_and_report_is_deterministic(tmp_path: Path) -> None:
    _write_repository(tmp_path)

    first = validate_repository(tmp_path)
    second = validate_repository(tmp_path)

    assert first["outcome"] == "PASS"
    assert first["package_manager"] == "pnpm@11.17.0"
    assert first["pnpm_version"] == "11.17.0"
    assert first["expected_importers"] == IMPORTERS
    assert first["lockfile_importers"] == IMPORTERS
    assert render_report(first) == render_report(second)


@pytest.mark.parametrize(
    ("mutation", "reason_code"),
    [
        ("manager", "PACKAGE_MANAGER_INVALID"),
        ("engine", "NODE_ENGINE_MISMATCH"),
        ("workspace", "WORKSPACE_DEFINITION_MISMATCH"),
        ("missing_lock", "PNPM_LOCKFILE_MISSING"),
        ("competing_lock", "COMPETING_LOCKFILE_PRESENT"),
    ],
)
def test_repository_contract_failures_are_explicit(
    tmp_path: Path, mutation: str, reason_code: str
) -> None:
    _write_repository(tmp_path)
    if mutation == "manager":
        manifest = json.loads((tmp_path / "package.json").read_text(encoding="utf-8"))
        manifest["packageManager"] = "pnpm@latest"
        (tmp_path / "package.json").write_text(json.dumps(manifest), encoding="utf-8")
    elif mutation == "engine":
        manifest = json.loads((tmp_path / "package.json").read_text(encoding="utf-8"))
        manifest["engines"]["node"] = ">=24"
        (tmp_path / "package.json").write_text(json.dumps(manifest), encoding="utf-8")
    elif mutation == "workspace":
        (tmp_path / "pnpm-workspace.yaml").write_text(
            'packages:\n  - "apps/*"\n', encoding="utf-8"
        )
    elif mutation == "missing_lock":
        (tmp_path / "pnpm-lock.yaml").unlink()
    else:
        (tmp_path / "package-lock.json").write_text("{}\n", encoding="utf-8")

    report = validate_repository(tmp_path)

    assert report["outcome"] == "ERROR"
    assert reason_code in report["reason_codes"]


@pytest.mark.parametrize(
    ("importers", "expected_missing", "expected_extra"),
    [
        (IMPORTERS[:-1], ["packages/ui"], []),
        (IMPORTERS + ["packages/ghost"], [], ["packages/ghost"]),
    ],
)
def test_lockfile_importer_drift_fails_closed(
    tmp_path: Path,
    importers: list[str],
    expected_missing: list[str],
    expected_extra: list[str],
) -> None:
    _write_repository(tmp_path, importers=importers)

    report = validate_repository(tmp_path)

    assert report["outcome"] == "ERROR"
    assert "LOCKFILE_IMPORTER_MISMATCH" in report["reason_codes"]
    finding = next(
        item
        for item in report["findings"]
        if item["code"] == "LOCKFILE_IMPORTER_MISMATCH"
    )
    assert f"missing={expected_missing}" in finding["message"]
    assert f"extra={expected_extra}" in finding["message"]


def test_malformed_workspace_manifest_is_an_error(tmp_path: Path) -> None:
    _write_repository(tmp_path)
    (tmp_path / "apps/explorer-web/package.json").write_text(
        "{not json", encoding="utf-8"
    )

    report = validate_repository(tmp_path)

    assert report["outcome"] == "ERROR"
    assert "WORKSPACE_MANIFEST_INVALID" in report["reason_codes"]
    assert "apps/explorer-web" not in report["expected_importers"]


def test_symlinked_lockfile_is_rejected(tmp_path: Path) -> None:
    _write_repository(tmp_path)
    real_lock = tmp_path / "real-lock.yaml"
    (tmp_path / "pnpm-lock.yaml").replace(real_lock)
    try:
        (tmp_path / "pnpm-lock.yaml").symlink_to(real_lock)
    except OSError:
        pytest.skip("symlinks are unavailable on this platform")

    report = validate_repository(tmp_path)

    assert report["outcome"] == "ERROR"
    assert "PNPM_LOCKFILE_UNSAFE" in report["reason_codes"]


def test_clean_audit_is_pass(tmp_path: Path) -> None:
    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path, moderate=2)

    report = classify_audit(
        report_path, command_exit_code=0, audit_level="high"
    )

    assert report["outcome"] == "PASS"
    assert report["threshold_count"] == 0
    assert report["reason_codes"] == []


@pytest.mark.parametrize(
    ("counts", "expected_count"),
    [
        ({"high": 1}, 1),
        ({"high": 2, "critical": 1}, 3),
    ],
)
def test_threshold_vulnerability_is_regression(
    tmp_path: Path, counts: dict[str, int], expected_count: int
) -> None:
    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path, **counts)

    report = classify_audit(
        report_path, command_exit_code=1, audit_level="high"
    )

    assert report["outcome"] == "REGRESSION"
    assert report["threshold_count"] == expected_count
    assert report["reason_codes"] == ["VULNERABILITY_THRESHOLD_EXCEEDED"]


@pytest.mark.parametrize("report_body", ["", "not json", "{}"])
def test_unusable_audit_report_is_error(
    tmp_path: Path, report_body: str
) -> None:
    report_path = tmp_path / "audit.json"
    report_path.write_text(report_body, encoding="utf-8")

    report = classify_audit(
        report_path, command_exit_code=1, audit_level="high"
    )

    assert report["outcome"] == "ERROR"
    assert "AUDIT_REPORT_INVALID" in report["reason_codes"]


def test_nonzero_command_without_threshold_findings_is_error(tmp_path: Path) -> None:
    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path)

    report = classify_audit(
        report_path, command_exit_code=1, audit_level="high"
    )

    assert report["outcome"] == "ERROR"
    assert report["reason_codes"] == ["AUDIT_COMMAND_FAILED"]


def test_success_exit_with_threshold_findings_is_error(tmp_path: Path) -> None:
    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path, critical=1)

    report = classify_audit(
        report_path, command_exit_code=0, audit_level="high"
    )

    assert report["outcome"] == "ERROR"
    assert report["reason_codes"] == ["AUDIT_EXIT_CODE_INCONSISTENT"]


def test_nonfinding_exit_code_is_not_relabelled_as_regression(
    tmp_path: Path,
) -> None:
    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path, high=1)

    report = classify_audit(
        report_path, command_exit_code=2, audit_level="high"
    )

    assert report["outcome"] == "ERROR"
    assert report["reason_codes"] == ["AUDIT_COMMAND_FAILED"]


def test_unsupported_audit_level_is_error(tmp_path: Path) -> None:
    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path)

    report = classify_audit(
        report_path, command_exit_code=0, audit_level="info"
    )

    assert report["outcome"] == "ERROR"
    assert report["reason_codes"] == ["AUDIT_LEVEL_INVALID"]


def test_cli_exit_polarity_and_json_output(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _write_repository(tmp_path)
    assert (
        main(["validate-repository", "--repository-root", str(tmp_path)])
        == EXIT_PASS
    )
    readiness = json.loads(capsys.readouterr().out)
    assert readiness["outcome"] == "PASS"

    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path, high=1)
    assert (
        main(
            [
                "classify-audit",
                "--report",
                str(report_path),
                "--command-exit-code",
                "1",
                "--audit-level",
                "high",
            ]
        )
        == EXIT_REGRESSION
    )
    regression = json.loads(capsys.readouterr().out)
    assert regression["outcome"] == "REGRESSION"

    report_path.write_text("{}", encoding="utf-8")
    assert (
        main(
            [
                "classify-audit",
                "--report",
                str(report_path),
                "--command-exit-code",
                "1",
            ]
        )
        == EXIT_ERROR
    )
    error = json.loads(capsys.readouterr().out)
    assert error["outcome"] == "ERROR"
