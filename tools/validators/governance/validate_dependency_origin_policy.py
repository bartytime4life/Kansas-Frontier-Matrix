"""Validate the proposed KFM static dependency-origin policy."""

from __future__ import annotations

import argparse
import json
import re
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import urlparse

import yaml
from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/dependency_origin_policy.schema.json"
)
POLICY_PATH = REPO_ROOT / "policy/supply_chain/dependency_origin_policy.v1.json"
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/dependency_origin_policy/cases.json"
)
SCOPE = "governance.dependency_origin_policy"

DEPENDENCY_FIELDS = (
    "dependencies",
    "devDependencies",
    "optionalDependencies",
    "peerDependencies",
)
DIRECT_REFERENCE_PATTERN = re.compile(
    r"(?:\s@\s*(?P<pep508>(?:git\+|https?:|file:)[^\s]+)|"
    r"^(?P<prefix>(?:git\+|git:|github:|gitlab:|bitbucket:|https?:|file:)))",
    re.IGNORECASE,
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]


class InputError(ValueError):
    """Raised when a bounded policy or repository input is unreadable."""


def _load_json(path: Path) -> Any:
    try:
        if path.is_symlink() or not path.is_file():
            raise InputError("input is not a regular file")
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError) as exc:
        raise InputError("JSON input could not be read") from exc


_SCHEMA = _load_json(SCHEMA_PATH)
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())


def _schema_findings(policy: object) -> list[Finding]:
    errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(policy),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    findings: list[Finding] = []
    for error in errors:
        path = "$"
        for part in error.absolute_path:
            path += f"[{part}]" if isinstance(part, int) else f".{part}"
        findings.append(Finding("POLICY_SCHEMA_INVALID", path))
    return findings


def _is_sorted_unique(values: object) -> bool:
    return (
        isinstance(values, list)
        and values == sorted(values)
        and len(values) == len(set(values))
    )


def validate_policy(policy: object) -> ValidationResult:
    findings = set(_schema_findings(policy))
    if findings or not isinstance(policy, dict):
        return ValidationResult("DENY", tuple(sorted(findings)))

    ordered_paths = (
        ("$.forbidden_lockfiles", policy["forbidden_lockfiles"]),
        ("$.npm.allowed_registry_hosts", policy["npm"]["allowed_registry_hosts"]),
        ("$.npm.internal_scopes", policy["npm"]["internal_scopes"]),
        (
            "$.npm.internal_specifier_prefixes",
            policy["npm"]["internal_specifier_prefixes"],
        ),
        (
            "$.npm.forbidden_direct_specifier_prefixes",
            policy["npm"]["forbidden_direct_specifier_prefixes"],
        ),
        (
            "$.python.forbidden_direct_reference_schemes",
            policy["python"]["forbidden_direct_reference_schemes"],
        ),
    )
    for path, values in ordered_paths:
        if not _is_sorted_unique(values):
            findings.add(Finding("POLICY_COLLECTION_NOT_SORTED_UNIQUE", path))

    return ValidationResult("DENY" if findings else "PASS", tuple(sorted(findings)))


def _starts_with_any(value: str, prefixes: Sequence[str]) -> bool:
    lowered = value.strip().lower()
    return any(lowered.startswith(prefix.lower()) for prefix in prefixes)


def evaluate_snapshot(
    policy: Mapping[str, Any], snapshot: Mapping[str, Any]
) -> ValidationResult:
    findings: set[Finding] = set()

    scan_errors = snapshot.get("scan_errors", [])
    if not isinstance(scan_errors, list):
        findings.add(Finding("REPOSITORY_SCAN_ERROR", "$.scan_errors"))
    elif scan_errors:
        findings.add(Finding("REPOSITORY_SCAN_ERROR", "$.scan_errors"))

    if snapshot.get("package_manager") != policy["expected_package_manager"]:
        findings.add(Finding("PACKAGE_MANAGER_PIN_MISMATCH", "$.package_manager"))

    if snapshot.get("required_lockfile_present") is not True:
        findings.add(Finding("LOCKFILE_MISSING", "$.required_lockfile_present"))

    surfaced = snapshot.get("forbidden_lockfiles_present", [])
    if isinstance(surfaced, list) and surfaced:
        findings.add(
            Finding("ALTERNATIVE_LOCKFILE_PRESENT", "$.forbidden_lockfiles_present")
        )
    elif not isinstance(surfaced, list):
        findings.add(Finding("REPOSITORY_SCAN_ERROR", "$.forbidden_lockfiles_present"))

    internal_scopes = tuple(policy["npm"]["internal_scopes"])
    internal_prefixes = tuple(policy["npm"]["internal_specifier_prefixes"])
    forbidden_npm = tuple(policy["npm"]["forbidden_direct_specifier_prefixes"])

    npm_dependencies = snapshot.get("npm_dependencies", [])
    if not isinstance(npm_dependencies, list):
        findings.add(Finding("REPOSITORY_SCAN_ERROR", "$.npm_dependencies"))
    else:
        for index, dependency in enumerate(npm_dependencies):
            if not isinstance(dependency, dict):
                findings.add(
                    Finding("REPOSITORY_SCAN_ERROR", f"$.npm_dependencies[{index}]")
                )
                continue
            package = str(dependency.get("package", ""))
            specifier = str(dependency.get("specifier", ""))
            if any(package.startswith(scope) for scope in internal_scopes):
                if not _starts_with_any(specifier, internal_prefixes):
                    findings.add(
                        Finding(
                            "INTERNAL_PACKAGE_NOT_WORKSPACE_BOUND",
                            f"$.npm_dependencies[{index}].specifier",
                        )
                    )
            elif _starts_with_any(specifier, forbidden_npm):
                findings.add(
                    Finding(
                        "DIRECT_DEPENDENCY_SOURCE_FORBIDDEN",
                        f"$.npm_dependencies[{index}].specifier",
                    )
                )

    allowed_hosts = set(policy["npm"]["allowed_registry_hosts"])
    lock_packages = snapshot.get("lock_packages", [])
    if not isinstance(lock_packages, list):
        findings.add(Finding("REPOSITORY_SCAN_ERROR", "$.lock_packages"))
    else:
        for index, package in enumerate(lock_packages):
            if not isinstance(package, dict):
                findings.add(
                    Finding("REPOSITORY_SCAN_ERROR", f"$.lock_packages[{index}]")
                )
                continue
            if policy["npm"]["require_integrity"] and not package.get("integrity"):
                findings.add(
                    Finding(
                        "LOCK_INTEGRITY_MISSING",
                        f"$.lock_packages[{index}].integrity",
                    )
                )
            tarball_url = package.get("tarball_url")
            if isinstance(tarball_url, str) and tarball_url:
                hostname = (urlparse(tarball_url).hostname or "").lower()
                if hostname not in allowed_hosts:
                    findings.add(
                        Finding(
                            "REGISTRY_HOST_NOT_ALLOWED",
                            f"$.lock_packages[{index}].tarball_url",
                        )
                    )

    python_schemes = tuple(policy["python"]["forbidden_direct_reference_schemes"])
    python_dependencies = snapshot.get("python_dependencies", [])
    if not isinstance(python_dependencies, list):
        findings.add(Finding("REPOSITORY_SCAN_ERROR", "$.python_dependencies"))
    else:
        for index, dependency in enumerate(python_dependencies):
            if not isinstance(dependency, dict):
                findings.add(
                    Finding("REPOSITORY_SCAN_ERROR", f"$.python_dependencies[{index}]")
                )
                continue
            requirement = str(dependency.get("requirement", "")).strip()
            direct_match = DIRECT_REFERENCE_PATTERN.search(requirement)
            direct_value = ""
            if direct_match:
                direct_value = (
                    direct_match.group("pep508")
                    or direct_match.group("prefix")
                    or ""
                )
            if direct_value and _starts_with_any(direct_value, python_schemes):
                findings.add(
                    Finding(
                        "PYTHON_DIRECT_REFERENCE_FORBIDDEN",
                        f"$.python_dependencies[{index}].requirement",
                    )
                )

    outcome = "ERROR" if any(
        finding.code == "REPOSITORY_SCAN_ERROR" for finding in findings
    ) else ("DENY" if findings else "PASS")
    return ValidationResult(outcome, tuple(sorted(findings)))


def _manifest_paths(root: Path) -> list[Path]:
    paths = [root / "package.json"]
    for parent in (root / "apps", root / "packages"):
        if parent.is_dir():
            paths.extend(sorted(parent.glob("*/package.json")))
    return paths


def _npm_dependencies(root: Path, errors: list[str]) -> list[dict[str, str]]:
    dependencies: list[dict[str, str]] = []
    for path in _manifest_paths(root):
        if not path.exists():
            if path == root / "package.json":
                errors.append("package.json:MISSING")
            continue
        try:
            manifest = _load_json(path)
        except InputError:
            errors.append(f"{path.relative_to(root)}:JSON_UNREADABLE")
            continue
        if not isinstance(manifest, dict):
            errors.append(f"{path.relative_to(root)}:ROOT_NOT_OBJECT")
            continue
        for field in DEPENDENCY_FIELDS:
            values = manifest.get(field, {})
            if values is None:
                continue
            if not isinstance(values, dict):
                errors.append(f"{path.relative_to(root)}:{field}_NOT_OBJECT")
                continue
            for package, specifier in values.items():
                if not isinstance(package, str) or not isinstance(specifier, str):
                    errors.append(f"{path.relative_to(root)}:{field}_ENTRY_INVALID")
                    continue
                dependencies.append(
                    {
                        "manifest": path.relative_to(root).as_posix(),
                        "package": package,
                        "specifier": specifier,
                    }
                )
    return sorted(
        dependencies,
        key=lambda item: (item["manifest"], item["package"], item["specifier"]),
    )


def _lock_packages(
    root: Path, policy: Mapping[str, Any], errors: list[str]
) -> list[dict[str, object]]:
    path = root / str(policy["required_lockfile"])
    if not path.is_file() or path.is_symlink():
        return []
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError, RecursionError):
        errors.append(f"{path.name}:YAML_UNREADABLE")
        return []
    if not isinstance(value, dict):
        errors.append(f"{path.name}:ROOT_NOT_OBJECT")
        return []
    if str(value.get("lockfileVersion")) != str(policy["npm"]["lockfile_version"]):
        errors.append(f"{path.name}:LOCKFILE_VERSION_MISMATCH")
    packages = value.get("packages", {})
    if not isinstance(packages, dict):
        errors.append(f"{path.name}:PACKAGES_NOT_OBJECT")
        return []
    records: list[dict[str, object]] = []
    for package_name, metadata in sorted(
        packages.items(), key=lambda item: str(item[0])
    ):
        if not isinstance(metadata, dict):
            errors.append(f"{path.name}:{package_name}:METADATA_INVALID")
            continue
        resolution = metadata.get("resolution")
        if not isinstance(resolution, dict):
            # Link/workspace and metadata-only entries are outside this static remote check.
            continue
        tarball = resolution.get("tarball")
        if tarball is None:
            tarball = resolution.get("url")
        records.append(
            {
                "package": str(package_name),
                "integrity": resolution.get("integrity"),
                "tarball_url": tarball if isinstance(tarball, str) else None,
            }
        )
    return records


def _python_dependencies(root: Path, errors: list[str]) -> list[dict[str, str]]:
    path = root / "pyproject.toml"
    if not path.is_file() or path.is_symlink():
        errors.append("pyproject.toml:MISSING")
        return []
    try:
        value = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError, RecursionError):
        errors.append("pyproject.toml:TOML_UNREADABLE")
        return []
    project = value.get("project", {})
    if not isinstance(project, dict):
        errors.append("pyproject.toml:PROJECT_NOT_OBJECT")
        return []
    requirements: list[str] = []
    dependencies = project.get("dependencies", [])
    if isinstance(dependencies, list):
        requirements.extend(str(item) for item in dependencies)
    else:
        errors.append("pyproject.toml:DEPENDENCIES_NOT_ARRAY")
    optional = project.get("optional-dependencies", {})
    if isinstance(optional, dict):
        for group, values in optional.items():
            if isinstance(values, list):
                requirements.extend(str(item) for item in values)
            else:
                errors.append(
                    f"pyproject.toml:OPTIONAL_DEPENDENCIES_{group}_NOT_ARRAY"
                )
    elif optional is not None:
        errors.append("pyproject.toml:OPTIONAL_DEPENDENCIES_NOT_OBJECT")
    return [
        {"manifest": "pyproject.toml", "requirement": requirement}
        for requirement in sorted(requirements)
    ]


def scan_repository(root: Path, policy: Mapping[str, Any]) -> Mapping[str, Any]:
    errors: list[str] = []
    package_path = root / "package.json"
    package_manager: object = None
    if package_path.is_file() and not package_path.is_symlink():
        try:
            package = _load_json(package_path)
            package_manager = (
                package.get("packageManager") if isinstance(package, dict) else None
            )
        except InputError:
            errors.append("package.json:JSON_UNREADABLE")
    else:
        errors.append("package.json:MISSING")

    return {
        "package_manager": package_manager,
        "required_lockfile_present": (
            (root / str(policy["required_lockfile"])).is_file()
            and not (root / str(policy["required_lockfile"])).is_symlink()
        ),
        "forbidden_lockfiles_present": sorted(
            path
            for path in policy["forbidden_lockfiles"]
            if (root / str(path)).exists()
        ),
        "npm_dependencies": _npm_dependencies(root, errors),
        "lock_packages": _lock_packages(root, policy, errors),
        "python_dependencies": _python_dependencies(root, errors),
        "scan_errors": sorted(set(errors)),
    }


def validate_repository(root: Path, policy: object) -> ValidationResult:
    policy_result = validate_policy(policy)
    if policy_result.outcome != "PASS" or not isinstance(policy, dict):
        return policy_result
    try:
        resolved = root.resolve(strict=True)
    except OSError:
        return ValidationResult(
            "ERROR", (Finding("REPOSITORY_SCAN_ERROR", "$.scan_root"),)
        )
    if not resolved.is_dir():
        return ValidationResult(
            "ERROR", (Finding("REPOSITORY_SCAN_ERROR", "$.scan_root"),)
        )
    return evaluate_snapshot(policy, scan_repository(resolved, policy))


def run_fixture_suite(
    policy: object | None = None,
) -> tuple[bool, dict[str, object]]:
    try:
        active_policy = _load_json(POLICY_PATH) if policy is None else policy
        suite = _load_json(FIXTURE_PATH)
    except InputError:
        return False, {"cases": [], "ok": False, "scope": SCOPE}
    policy_result = validate_policy(active_policy)
    if (
        policy_result.outcome != "PASS"
        or not isinstance(active_policy, dict)
        or not isinstance(suite, dict)
    ):
        return False, {"cases": [], "ok": False, "scope": SCOPE}
    entries = suite.get("cases", [])
    if not isinstance(entries, list):
        return False, {"cases": [], "ok": False, "scope": SCOPE}

    cases: list[dict[str, object]] = []
    ok = True
    for case in entries:
        if not isinstance(case, dict) or not isinstance(case.get("snapshot"), dict):
            ok = False
            continue
        result = evaluate_snapshot(active_policy, case["snapshot"])
        actual_codes = sorted({finding.code for finding in result.findings})
        expected = case.get("expected", {})
        case_ok = (
            isinstance(expected, dict)
            and result.outcome == expected.get("outcome")
            and actual_codes == expected.get("finding_codes")
        )
        ok = ok and case_ok
        cases.append(
            {
                "actual_findings": actual_codes,
                "actual_outcome": result.outcome,
                "case_id": case.get("case_id"),
                "expected_findings": (
                    expected.get("finding_codes")
                    if isinstance(expected, dict)
                    else None
                ),
                "expected_outcome": (
                    expected.get("outcome") if isinstance(expected, dict) else None
                ),
                "ok": case_ok,
            }
        )
    return ok, {"cases": cases, "ok": ok, "scope": SCOPE}


def _serialize(result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate KFM's proposed static dependency-origin policy."
    )
    parser.add_argument("--policy", type=Path, default=POLICY_PATH)
    parser.add_argument("--scan-root", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures == (args.scan_root is not None):
        parser.error("select exactly one of --fixtures or --scan-root")
    try:
        policy = _load_json(args.policy)
    except InputError:
        result = ValidationResult(
            "ERROR", (Finding("POLICY_INPUT_INVALID", "$"),)
        )
        print(_serialize(result))
        return 1
    if args.fixtures:
        ok, report = run_fixture_suite(policy)
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    assert args.scan_root is not None
    result = validate_repository(args.scan_root, policy)
    print(_serialize(result))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
