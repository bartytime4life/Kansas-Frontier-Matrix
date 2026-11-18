from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.validators.dependencies.pnpm_audit_readiness import (
    EXIT_ERROR,
    EXIT_PASS,
    EXIT_REGRESSION,
    classify_audit,
    load_audit_exceptions,
    main,
    render_report,
    validate_repository,
)
from tools.validators.validate_all import load_registry, select_validators


REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / "tools/validators/validator_registry.json"
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


def _write_audit_report(
    path: Path,
    *,
    legacy_advisories: dict[str, object] | None = None,
    vulnerability_records: dict[str, object] | None = None,
    **counts: int,
) -> None:
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
                "advisories": legacy_advisories or {},
                **(
                    {"vulnerabilities": vulnerability_records}
                    if vulnerability_records is not None
                    else {}
                ),
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
    "changed_path",
    [
        "package.json",
        "pnpm-workspace.yaml",
        "pnpm-lock.yaml",
        "package-lock.json",
        "apps/kansas-frontier-matrix-explorer/package-lock.json",
        "apps/explorer-web/package.json",
        "packages/maplibre/package.json",
        ".github/workflows/dependency-scan.yml",
        "tools/validators/dependencies/pnpm_audit_readiness.py",
    ],
)
def test_registry_runs_readiness_for_dependency_contract_changes(
    changed_path: str,
) -> None:
    registry = load_registry(REGISTRY_PATH, REPO_ROOT)
    registered = registry.by_id["pnpm-dependency-readiness"]

    assert registered.script == (
        "tools/validators/dependencies/pnpm_audit_readiness.py"
    )
    assert registered.args == (
        "validate-repository",
        "--repository-root",
        ".",
    )
    assert "pnpm-dependency-readiness" in registry.profiles["full"]
    assert "pnpm-dependency-readiness" not in registry.profiles["focused"]
    assert "pnpm-dependency-readiness" not in registry.profiles["release-dry-run"]

    selected, mode = select_validators(
        registry,
        profile="changed-area",
        changed_paths=(changed_path,),
    )

    assert mode == "changed-area"
    assert "pnpm-dependency-readiness" in {
        item.validator_id for item in selected
    }


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


def test_npm_audit_is_classified_as_the_installed_graph(tmp_path: Path) -> None:
    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path, moderate=1)

    report = classify_audit(
        report_path,
        command_exit_code=0,
        audit_level="high",
        manager="npm",
    )

    assert report["outcome"] == "PASS"
    assert report["report_type"] == "npm_audit_result"
    assert report["manager"] == "npm"


def test_unsupported_audit_manager_is_error(tmp_path: Path) -> None:
    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path)

    report = classify_audit(
        report_path,
        command_exit_code=0,
        audit_level="high",
        manager="other",
    )

    assert report["outcome"] == "ERROR"
    assert report["report_type"] == "node_audit_result"
    assert report["reason_codes"] == ["AUDIT_MANAGER_INVALID"]


def test_dependency_workflow_audits_remaining_locked_node_graph() -> None:
    workflow = (REPO_ROOT / ".github/workflows/dependency-scan.yml").read_text(
        encoding="utf-8"
    )

    assert 'pnpm audit \\' in workflow
    assert '--manager "pnpm"' in workflow
    assert "--exceptions configs/dependency-patches/audit-exceptions.json" in workflow
    assert 'apps/kansas-frontier-matrix-explorer' not in workflow


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


def test_threshold_projection_is_actionable_bounded_and_deterministic(
    tmp_path: Path,
) -> None:
    report_path = tmp_path / "audit.json"
    records = {
        f"package-{index:02d}": {
            "name": f"package-{index:02d}",
            "severity": "critical" if index == 59 else "high",
            "via": [
                {"source": 9000 + index},
                {"source": 8000 + index},
                "transitive-package",
            ],
            "fixAvailable": {
                "name": f"package-{index:02d}",
                "version": f"2.0.{index}",
                "isSemVerMajor": False,
            },
        }
        for index in range(60)
    }
    _write_audit_report(
        report_path,
        vulnerability_records=records,
        high=59,
        critical=1,
    )

    first = classify_audit(
        report_path, command_exit_code=1, audit_level="high"
    )
    second = classify_audit(
        report_path, command_exit_code=1, audit_level="high"
    )

    projection = first["threshold_vulnerabilities"]
    assert first["outcome"] == "REGRESSION"
    assert projection["status"] == "PRESENT"
    assert projection["total"] == 60
    assert projection["truncated"] is True
    assert projection["invalid_records"] == 0
    assert len(projection["items"]) == 50
    assert projection["items"][0] == {
        "package": "package-59",
        "severity": "critical",
        "advisory_ids": ["8059", "9059"],
        "advisory_ids_truncated": False,
        "fix_available": True,
        "fix_version": "2.0.59",
    }
    assert render_report(first) == render_report(second)


def test_threshold_projection_marks_missing_and_count_mismatch(
    tmp_path: Path,
) -> None:
    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path, high=1)
    missing = classify_audit(
        report_path, command_exit_code=1, audit_level="high"
    )
    assert missing["threshold_vulnerabilities"]["status"] == "NOT_PROVIDED"

    _write_audit_report(
        report_path,
        vulnerability_records={},
        high=1,
    )
    mismatch = classify_audit(
        report_path, command_exit_code=1, audit_level="high"
    )
    assert mismatch["threshold_vulnerabilities"]["status"] == "COUNT_MISMATCH"


def test_legacy_pnpm_advisories_are_projected_without_raw_text(
    tmp_path: Path,
) -> None:
    report_path = tmp_path / "audit.json"
    _write_audit_report(
        report_path,
        legacy_advisories={
            "1138809": {
                "module_name": "vinext",
                "severity": "high",
                "github_advisory_id": "GHSA-example-2",
                "title": "must not be copied",
                "url": "https://untrusted.example/advisory",
                "recommendation": "must not be copied",
            },
            "1138808": {
                "module_name": "image-size",
                "severity": "high",
                "github_advisory_id": "GHSA-example-1",
                "title": "must not be copied",
            },
            "1138810": {
                "module_name": "below-threshold",
                "severity": "moderate",
            },
        },
        high=2,
        moderate=1,
    )

    report = classify_audit(
        report_path,
        command_exit_code=1,
        audit_level="high",
        manager="pnpm",
    )

    projection = report["threshold_vulnerabilities"]
    assert report["outcome"] == "REGRESSION"
    assert projection["status"] == "PRESENT"
    assert projection["source_format"] == "legacy_advisories"
    assert projection["total"] == 2
    assert projection["items"] == [
        {
            "package": "image-size",
            "severity": "high",
            "advisory_ids": ["1138808", "GHSA-example-1"],
            "advisory_ids_truncated": False,
            "fix_available": None,
            "fix_version": None,
        },
        {
            "package": "vinext",
            "severity": "high",
            "advisory_ids": ["1138809", "GHSA-example-2"],
            "advisory_ids_truncated": False,
            "fix_available": None,
            "fix_version": None,
        },
    ]
    rendered = render_report(report)
    assert "must not be copied" not in rendered
    assert "untrusted.example" not in rendered


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


PICOMATCH_GHSA = "GHSA-fc5q-39xc-vjpf"


def _picomatch_advisory(version: str = "4.0.7", **extra: object) -> dict[str, object]:
    return {
        "1247710": {
            "module_name": "picomatch",
            "severity": "high",
            "github_advisory_id": PICOMATCH_GHSA,
            "findings": [{"version": version, "paths": ["packages__maplibre>vitest>picomatch"]}],
        },
        **extra,
    }


def _exception_repository(
    root: Path,
    *,
    patch_text: str = "diff --git a/lib/parse.js b/lib/parse.js\n",
    lock_hash: str | None = None,
    extra_lock_version: bool = False,
    **entry_changes: object,
) -> Path:
    import hashlib

    patch = root / "configs/dependency-patches/picomatch-4.0.7.patch"
    patch.parent.mkdir(parents=True, exist_ok=True)
    patch.write_text(patch_text, encoding="utf-8")
    digest = hashlib.sha256(patch.read_bytes()).hexdigest()
    lock_hash = lock_hash or digest
    (root / "pnpm-lock.yaml").write_text(
        "lockfileVersion: '9.0'\n\n"
        "patchedDependencies:\n"
        f"  picomatch@4.0.7: {lock_hash}\n\n"
        "packages:\n\n"
        "  picomatch@4.0.7:\n    resolution: {integrity: sha512-x}\n\n"
        + ("  picomatch@2.3.1:\n    resolution: {integrity: sha512-y}\n\n" if extra_lock_version else "")
        + f"snapshots:\n\n  picomatch@4.0.7(patch_hash={lock_hash}): {{}}\n",
        encoding="utf-8",
    )
    entry: dict[str, object] = {
        "advisory": PICOMATCH_GHSA,
        "package": "picomatch",
        "version": "4.0.7",
        "patch_path": "configs/dependency-patches/picomatch-4.0.7.patch",
        "patch_sha256": digest,
        "upstream_fix": "https://github.com/micromatch/picomatch/pull/264",
        "reason": "No fixed release; upstream fix applied in-tree.",
        "recorded_on": "2026-11-18",
        "expires_on": "2027-02-18",
        "human_review": "pending",
        **entry_changes,
    }
    register = root / "configs/dependency-patches/audit-exceptions.json"
    register.write_text(
        json.dumps({"register": "dependency_audit_exceptions", "version": "v1", "exceptions": [entry]}),
        encoding="utf-8",
    )
    return register


def test_repository_picomatch_exception_is_bound_to_the_applied_patch() -> None:
    import datetime

    findings: list[dict[str, str]] = []
    accepted = load_audit_exceptions(
        REPO_ROOT / "configs/dependency-patches/audit-exceptions.json",
        REPO_ROOT,
        today=datetime.date(2026, 11, 18),
        findings=findings,
    )
    assert findings == []
    assert accepted == [
        {"advisory": PICOMATCH_GHSA, "package": "picomatch", "version": "4.0.7", "expires_on": "2027-02-18"}
    ]
    workspace = (REPO_ROOT / "pnpm-workspace.yaml").read_text(encoding="utf-8")
    assert '"picomatch@4.0.7": "configs/dependency-patches/picomatch-4.0.7.patch"' in workspace
    assert "ignoreGhsas" not in workspace, "pnpm ignores keep severity counts and fail the classifier"


def test_bound_exception_passes_only_its_own_finding(tmp_path: Path) -> None:
    import datetime

    register = _exception_repository(tmp_path)
    findings: list[dict[str, str]] = []
    exceptions = load_audit_exceptions(register, tmp_path, today=datetime.date(2026, 11, 18), findings=findings)
    assert findings == [] and exceptions

    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path, legacy_advisories=_picomatch_advisory(), high=1)
    report = classify_audit(report_path, command_exit_code=1, audit_level="high", exceptions=exceptions)
    assert report["outcome"] == "PASS"
    assert report["excepted_vulnerabilities"] == [
        {"advisory": PICOMATCH_GHSA, "package": "picomatch", "version": "4.0.7", "expires_on": "2027-02-18"}
    ]

    other = {"1138809": {"module_name": "vinext", "severity": "high", "github_advisory_id": "GHSA-example-2"}}
    _write_audit_report(report_path, legacy_advisories=_picomatch_advisory(**other), high=2)
    report = classify_audit(report_path, command_exit_code=1, audit_level="high", exceptions=exceptions)
    assert report["outcome"] == "REGRESSION"
    assert report["reason_codes"] == ["VULNERABILITY_THRESHOLD_EXCEEDED"]
    assert "1 vulnerabilities at or above high after 1 reviewed exceptions" in render_report(report)

    _write_audit_report(report_path, legacy_advisories=_picomatch_advisory(version="4.0.8"), high=1)
    report = classify_audit(report_path, command_exit_code=1, audit_level="high", exceptions=exceptions)
    assert report["outcome"] == "REGRESSION", "a different locked version is not excepted"

    _write_audit_report(report_path, legacy_advisories=_picomatch_advisory(), high=2)
    report = classify_audit(report_path, command_exit_code=1, audit_level="high", exceptions=exceptions)
    assert report["outcome"] == "REGRESSION", "unattributable counts are never excepted"


def test_classification_without_exceptions_is_unchanged(tmp_path: Path) -> None:
    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path, legacy_advisories=_picomatch_advisory(), high=1)
    report = classify_audit(report_path, command_exit_code=1, audit_level="high")
    assert report["outcome"] == "REGRESSION"
    assert "excepted_vulnerabilities" not in report


@pytest.mark.parametrize(
    ("changes", "code"),
    [
        ({"expires_on": "2026-11-17", "recorded_on": "2026-11-01"}, "AUDIT_EXCEPTION_EXPIRED"),
        ({"expires_on": "2027-12-31"}, "AUDIT_EXCEPTIONS_INVALID"),
        ({"patch_sha256": "0" * 64}, "AUDIT_EXCEPTIONS_INVALID"),
        ({"lock_hash": "f" * 64}, "AUDIT_EXCEPTIONS_INVALID"),
        ({"extra_lock_version": True}, "AUDIT_EXCEPTIONS_INVALID"),
        ({"advisory": "CVE-2026-112366"}, "AUDIT_EXCEPTIONS_INVALID"),
        ({"patch_path": "../outside.patch"}, "AUDIT_EXCEPTIONS_INVALID"),
        ({"upstream_fix": "http://example.test/fix"}, "AUDIT_EXCEPTIONS_INVALID"),
        ({"unexpected": "key"}, "AUDIT_EXCEPTIONS_INVALID"),
    ],
)
def test_unbound_or_expired_exceptions_fail_closed(tmp_path: Path, changes: dict[str, object], code: str) -> None:
    import datetime

    repository_changes = {key: changes.pop(key) for key in ("lock_hash", "extra_lock_version") if key in changes}
    register = _exception_repository(tmp_path, **repository_changes, **changes)
    findings: list[dict[str, str]] = []
    assert load_audit_exceptions(register, tmp_path, today=datetime.date(2026, 11, 18), findings=findings) is None
    assert code in {finding["code"] for finding in findings}


def test_cli_exception_register_errors_are_reported(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    register = _exception_repository(tmp_path, patch_sha256="0" * 64)
    report_path = tmp_path / "audit.json"
    _write_audit_report(report_path, legacy_advisories=_picomatch_advisory(), high=1)
    exit_code = main([
        "classify-audit", "--report", str(report_path), "--command-exit-code", "1",
        "--exceptions", str(register), "--repository-root", str(tmp_path),
    ])
    output = json.loads(capsys.readouterr().out)
    assert exit_code == EXIT_ERROR
    assert output["outcome"] == "ERROR"
    assert output["reason_codes"] == ["AUDIT_EXCEPTIONS_INVALID"]
