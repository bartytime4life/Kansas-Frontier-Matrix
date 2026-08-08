from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = (
    REPO_ROOT / "tools/validators/dependencies/pnpm_supply_chain_policy.py"
)
SPEC = importlib.util.spec_from_file_location(
    "pnpm_supply_chain_policy", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

EXIT_ERROR = MODULE.EXIT_ERROR
EXIT_PASS = MODULE.EXIT_PASS
main = MODULE.main
render_report = MODULE.render_report
validate_repository = MODULE.validate_repository

POLICY_PATH = Path("policy/supply_chain/pnpm_dependency_policy.json")


def _base_policy(lock_sha256: str) -> dict:
    return {
        "policy_id": "kfm://policy/supply-chain/pnpm-dependency/v1",
        "version": "v1",
        "status": "PROPOSED",
        "source_idea_ids": [
            "KFM-P8-PROG-0007",
            "KFM-P8-PROG-0008",
            "KFM-P8-PROG-0009",
            "KFM-P8-PROG-0016",
        ],
        "package_manager": "pnpm@11.17.0",
        "node_engine": ">=22.13 <23",
        "registries": {
            "default": "https://registry.npmjs.org/",
            "allowed": ["https://registry.npmjs.org/"],
            "internal_scope": "@kfm",
            "internal_scope_registry": "https://registry.invalid/",
            "internal_resolution": "workspace_only",
            "deny_sink": True,
        },
        "requirements": {
            "private_workspaces": True,
            "exact_versions": True,
            "lockfile_integrity": True,
            "lifecycle_scripts_disabled": True,
            "frozen_lockfile": True,
        },
        "npmrc": {
            "registry": "https://registry.npmjs.org/",
            "@kfm:registry": "https://registry.invalid/",
            "ignore-scripts": "true",
            "save-exact": "true",
            "strict-peer-dependencies": "true",
            "verify-store-integrity": "true",
        },
        "lockfile": {
            "path": "pnpm-lock.yaml",
            "sha256": lock_sha256,
        },
        "version_range_exceptions": [],
        "workflows": {
            "root": ".github/workflows",
            "allowed_package_manager": "pnpm",
            "required_pnpm_install_flags": [
                "--frozen-lockfile",
                "--ignore-scripts",
            ],
            "required_env": {
                "NPM_CONFIG_IGNORE_SCRIPTS": "true",
                "PNPM_CONFIG_IGNORE_SCRIPTS": "true",
            },
        },
        "non_effects": [
            "does_not_create_or_activate_a_registry",
            "does_not_install_packages",
            "does_not_authorize_release_or_publication",
        ],
    }


def _lockfile(
    *,
    integrity: bool = True,
    package_key: str = "vite@8.2.0",
    resolution: str | None = None,
) -> str:
    if resolution is None:
        resolution = (
            "{integrity: sha512-QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVo=}"
            if integrity
            else "{}"
        )
    return (
        "lockfileVersion: '9.0'\n\n"
        "settings:\n"
        "  autoInstallPeers: true\n"
        "  excludeLinksFromLockfile: false\n\n"
        "importers:\n\n"
        "  .: {}\n\n"
        "  apps/explorer-web: {}\n\n"
        "  packages/ui: {}\n\n"
        "packages:\n\n"
        f"  '{package_key}':\n"
        f"    resolution: {resolution}\n\n"
        "snapshots: {}\n"
    )


def _guarded_workflow() -> str:
    return '''name: fixture
on: [pull_request]
permissions:
  contents: read
env:
  NPM_CONFIG_IGNORE_SCRIPTS: "true"
  PNPM_CONFIG_IGNORE_SCRIPTS: "true"
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: |
          set -euo pipefail
          pnpm install --frozen-lockfile --ignore-scripts
'''


def _write_repository(
    root: Path,
    *,
    root_dependencies: dict[str, str] | None = None,
    package_name: str = "@kfm/ui",
    package_dependencies: dict[str, str] | None = None,
    npmrc: str | None = None,
    lockfile_text: str | None = None,
    workflow_text: str | None = None,
    exceptions: list[dict] | None = None,
) -> dict:
    (root / "apps/explorer-web").mkdir(parents=True)
    (root / "packages/ui").mkdir(parents=True)
    (root / ".github/workflows").mkdir(parents=True)
    (root / POLICY_PATH.parent).mkdir(parents=True)

    root_manifest = {
        "name": "fixture",
        "private": True,
        "packageManager": "pnpm@11.17.0",
        "engines": {"node": ">=22.13 <23"},
        "workspaces": ["apps/*", "packages/*"],
        "devDependencies": root_dependencies or {"vite": "8.2.0"},
    }
    (root / "package.json").write_text(
        json.dumps(root_manifest, sort_keys=True), encoding="utf-8"
    )
    (root / "apps/explorer-web/package.json").write_text(
        json.dumps(
            {
                "name": "explorer-web",
                "private": True,
                "dependencies": {"vite": "8.2.0"},
            },
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    package_manifest = {
        "name": package_name,
        "private": True,
    }
    if package_dependencies is not None:
        package_manifest["dependencies"] = package_dependencies
    (root / "packages/ui/package.json").write_text(
        json.dumps(package_manifest, sort_keys=True), encoding="utf-8"
    )

    if npmrc is None:
        npmrc = (
            "registry=https://registry.npmjs.org/\n"
            "@kfm:registry=https://registry.invalid/\n"
            "ignore-scripts=true\n"
            "save-exact=true\n"
            "strict-peer-dependencies=true\n"
            "verify-store-integrity=true\n"
        )
    (root / ".npmrc").write_text(npmrc, encoding="utf-8")

    lockfile_text = lockfile_text or _lockfile()
    lock_path = root / "pnpm-lock.yaml"
    lock_path.write_text(lockfile_text, encoding="utf-8")
    lock_sha256 = "sha256:" + hashlib.sha256(lock_path.read_bytes()).hexdigest()

    (root / ".github/workflows/fixture.yml").write_text(
        workflow_text or _guarded_workflow(), encoding="utf-8"
    )

    policy = _base_policy(lock_sha256)
    policy["version_range_exceptions"] = exceptions or []
    (root / POLICY_PATH).write_text(
        json.dumps(policy, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return policy


def _assert_error(root: Path, code: str) -> dict:
    report = validate_repository(root)
    assert report["outcome"] == "ERROR"
    assert code in report["reason_codes"]
    return report


def test_valid_repository_passes_deterministically(tmp_path: Path) -> None:
    _write_repository(tmp_path)
    first = validate_repository(tmp_path)
    second = validate_repository(tmp_path)
    assert first["outcome"] == "PASS"
    assert first["install_command_count"] == 1
    assert first["lockfile_package_count"] == 1
    assert first["registry_boundary"]["internal_resolution"] == "workspace_only"
    assert render_report(first) == render_report(second)
    assert set(first["authority"].values()) == {False}


def test_missing_policy_fails_closed(tmp_path: Path) -> None:
    _write_repository(tmp_path)
    (tmp_path / POLICY_PATH).unlink()
    _assert_error(tmp_path, "SUPPLY_CHAIN_POLICY_MISSING")


def test_malformed_policy_fails_closed(tmp_path: Path) -> None:
    _write_repository(tmp_path)
    (tmp_path / POLICY_PATH).write_text("{not-json", encoding="utf-8")
    _assert_error(tmp_path, "SUPPLY_CHAIN_POLICY_INVALID")


def test_missing_npmrc_fails_closed(tmp_path: Path) -> None:
    _write_repository(tmp_path)
    (tmp_path / ".npmrc").unlink()
    _assert_error(tmp_path, "NPMRC_MISSING")


def test_registry_mismatch_fails_closed(tmp_path: Path) -> None:
    _write_repository(
        tmp_path,
        npmrc=(
            "registry=https://registry.example.invalid/\n"
            "@kfm:registry=https://registry.invalid/\n"
            "ignore-scripts=true\n"
            "save-exact=true\n"
            "strict-peer-dependencies=true\n"
            "verify-store-integrity=true\n"
        ),
    )
    _assert_error(tmp_path, "NPMRC_SETTING_MISMATCH")


def test_duplicate_npmrc_key_is_rejected(tmp_path: Path) -> None:
    _write_repository(
        tmp_path,
        npmrc=(
            "registry=https://registry.npmjs.org/\n"
            "registry=https://registry.npmjs.org/\n"
            "@kfm:registry=https://registry.invalid/\n"
            "ignore-scripts=true\n"
            "save-exact=true\n"
            "strict-peer-dependencies=true\n"
            "verify-store-integrity=true\n"
        ),
    )
    _assert_error(tmp_path, "NPMRC_DUPLICATE_KEY")


def test_missing_ignore_scripts_setting_is_rejected(tmp_path: Path) -> None:
    _write_repository(
        tmp_path,
        npmrc=(
            "registry=https://registry.npmjs.org/\n"
            "@kfm:registry=https://registry.invalid/\n"
            "save-exact=true\n"
            "strict-peer-dependencies=true\n"
            "verify-store-integrity=true\n"
        ),
    )
    _assert_error(tmp_path, "NPMRC_SETTING_MISMATCH")


def test_unapproved_npmrc_setting_is_rejected(tmp_path: Path) -> None:
    _write_repository(tmp_path)
    with (tmp_path / ".npmrc").open("a", encoding="utf-8") as stream:
        stream.write("registry-fallback=true\n")
    _assert_error(tmp_path, "NPMRC_UNAPPROVED_SETTING")


def test_non_exact_dependency_is_rejected(tmp_path: Path) -> None:
    _write_repository(tmp_path, root_dependencies={"vite": "^8.2.0"})
    _assert_error(tmp_path, "DEPENDENCY_SPECIFIER_NOT_EXACT")


def test_bounded_exact_exception_is_accepted(tmp_path: Path) -> None:
    exception = {
        "manifest": "package.json",
        "field": "devDependencies",
        "name": "vite",
        "specifier": "^8.2.0",
        "reason": "pre-existing baseline pending reviewed lockfile update",
        "expires_on_change": True,
    }
    _write_repository(
        tmp_path,
        root_dependencies={"vite": "^8.2.0"},
        exceptions=[exception],
    )
    assert validate_repository(tmp_path)["outcome"] == "PASS"


def test_stale_exception_is_rejected(tmp_path: Path) -> None:
    exception = {
        "manifest": "package.json",
        "field": "devDependencies",
        "name": "vite",
        "specifier": "^8.2.0",
        "reason": "pre-existing baseline pending reviewed lockfile update",
        "expires_on_change": True,
    }
    _write_repository(tmp_path, exceptions=[exception])
    _assert_error(tmp_path, "VERSION_RANGE_EXCEPTION_STALE")


def test_internal_package_namespace_is_required(tmp_path: Path) -> None:
    _write_repository(tmp_path, package_name="ui")
    _assert_error(tmp_path, "INTERNAL_PACKAGE_NAMESPACE_REQUIRED")


def test_internal_dependency_must_be_workspace_exact(tmp_path: Path) -> None:
    _write_repository(
        tmp_path,
        package_dependencies={"@kfm/maplibre": "^0.0.0"},
    )
    _assert_error(tmp_path, "INTERNAL_DEPENDENCY_NOT_WORKSPACE_EXACT")


def test_internal_dependency_workspace_exact_is_accepted(tmp_path: Path) -> None:
    _write_repository(
        tmp_path,
        package_dependencies={"@kfm/maplibre": "workspace:0.0.0"},
    )
    assert validate_repository(tmp_path)["outcome"] == "PASS"


def test_lockfile_integrity_is_required(tmp_path: Path) -> None:
    _write_repository(tmp_path, lockfile_text=_lockfile(integrity=False))
    _assert_error(tmp_path, "LOCKFILE_INTEGRITY_MISSING")


def test_lockfile_sha_mismatch_reports_actual_digest(tmp_path: Path) -> None:
    policy = _write_repository(tmp_path)
    policy["lockfile"]["sha256"] = "sha256:" + ("0" * 64)
    (tmp_path / POLICY_PATH).write_text(
        json.dumps(policy, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    report = _assert_error(tmp_path, "LOCKFILE_SHA256_MISMATCH")
    finding = next(
        item
        for item in report["findings"]
        if item["code"] == "LOCKFILE_SHA256_MISMATCH"
    )
    assert f"actual={report['lockfile_sha256']}" in finding["message"]


def test_internal_package_cannot_resolve_from_lockfile(tmp_path: Path) -> None:
    _write_repository(
        tmp_path,
        lockfile_text=_lockfile(package_key="@kfm/ui@0.0.0"),
    )
    _assert_error(tmp_path, "INTERNAL_PACKAGE_RESOLVED_EXTERNALLY")


def test_tarball_or_url_resolution_is_rejected(tmp_path: Path) -> None:
    _write_repository(
        tmp_path,
        lockfile_text=_lockfile(
            resolution=(
                "{tarball: https://registry.example.invalid/vite.tgz, "
                "integrity: sha512-QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVo=}"
            )
        ),
    )
    _assert_error(tmp_path, "LOCKFILE_UNAPPROVED_RESOLUTION")


@pytest.mark.parametrize(
    ("workflow_text", "reason_code"),
    [
        (
            '''name: x
on: [pull_request]
jobs:
  x:
    runs-on: ubuntu-latest
    steps:
      - run: pnpm install --frozen-lockfile
''',
            "WORKFLOW_INSTALL_FLAG_MISSING",
        ),
        (
            '''name: x
on: [pull_request]
env:
  NPM_CONFIG_IGNORE_SCRIPTS: "true"
  PNPM_CONFIG_IGNORE_SCRIPTS: "true"
jobs:
  x:
    runs-on: ubuntu-latest
    steps:
      - run: npm ci --ignore-scripts
''',
            "WORKFLOW_PACKAGE_MANAGER_INSTALL_DENIED",
        ),
        (
            '''name: x
on: [pull_request]
jobs:
  x:
    runs-on: ubuntu-latest
    steps:
      - run: pnpm install --frozen-lockfile --ignore-scripts
''',
            "WORKFLOW_IGNORE_SCRIPTS_ENV_MISSING",
        ),
    ],
)
def test_workflow_install_policy_fails_closed(
    tmp_path: Path, workflow_text: str, reason_code: str
) -> None:
    _write_repository(tmp_path, workflow_text=workflow_text)
    _assert_error(tmp_path, reason_code)


def test_quoted_prohibited_example_is_not_treated_as_execution(tmp_path: Path) -> None:
    workflow = '''name: x
on: [pull_request]
jobs:
  x:
    runs-on: ubuntu-latest
    steps:
      - run: |
          forbidden=("npm install" "pnpm install")
          printf '%s\\n' "${forbidden[@]}"
'''
    _write_repository(tmp_path, workflow_text=workflow)
    assert validate_repository(tmp_path)["outcome"] == "PASS"


def test_competing_lockfile_is_rejected(tmp_path: Path) -> None:
    _write_repository(tmp_path)
    (tmp_path / "package-lock.json").write_text("{}\n", encoding="utf-8")
    _assert_error(tmp_path, "COMPETING_LOCKFILE_PRESENT")


def test_cli_exit_polarity_and_json_output(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _write_repository(tmp_path)
    assert main(["--repository-root", str(tmp_path)]) == EXIT_PASS
    payload = json.loads(capsys.readouterr().out)
    assert payload["outcome"] == "PASS"

    (tmp_path / ".npmrc").unlink()
    assert main(["--repository-root", str(tmp_path)]) == EXIT_ERROR
    payload = json.loads(capsys.readouterr().out)
    assert payload["outcome"] == "ERROR"
