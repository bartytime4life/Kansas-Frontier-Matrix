#!/usr/bin/env python3
"""Validate KFM's deterministic pnpm supply-chain policy without network access.

This validator owns repository-local conformance only. It does not query a
registry, install packages, evaluate vulnerability advisories, grant dependency
admission, or authorize release, deployment, promotion, or publication.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

EXIT_PASS = 0
EXIT_ERROR = 2

DEFAULT_POLICY_PATH = "policy/supply_chain/pnpm_dependency_policy.json"
PACKAGE_MANAGER = "pnpm@11.17.0"
NODE_ENGINE = ">=22.13 <23"
LOCKFILE_VERSION = "9.0"
INTERNAL_SCOPE = "@kfm"
DEFAULT_REGISTRY = "https://registry.npmjs.org/"
INTERNAL_DENY_REGISTRY = "https://registry.invalid/"

DEPENDENCY_FIELDS = (
    "dependencies",
    "devDependencies",
    "optionalDependencies",
    "peerDependencies",
)
COMPETING_LOCKFILES = (
    "package-lock.json",
    "npm-shrinkwrap.json",
    "yarn.lock",
    "bun.lock",
    "bun.lockb",
)
REQUIRED_POLICY_ID = "kfm://policy/supply-chain/pnpm-dependency/v1"
REQUIRED_SOURCE_IDEAS = (
    "KFM-P8-PROG-0007",
    "KFM-P8-PROG-0008",
    "KFM-P8-PROG-0009",
    "KFM-P8-PROG-0016",
)
REQUIRED_NPMRC = {
    "registry": DEFAULT_REGISTRY,
    "@kfm:registry": INTERNAL_DENY_REGISTRY,
    "ignore-scripts": "true",
    "save-exact": "true",
    "strict-peer-dependencies": "true",
    "verify-store-integrity": "true",
}
REQUIRED_WORKFLOW_ENV = {
    "NPM_CONFIG_IGNORE_SCRIPTS": "true",
    "PNPM_CONFIG_IGNORE_SCRIPTS": "true",
}
EXACT_SEMVER_RE = re.compile(
    r"^(?:0|[1-9][0-9]*)\."
    r"(?:0|[1-9][0-9]*)\."
    r"(?:0|[1-9][0-9]*)"
    r"(?:-[0-9A-Za-z.-]+)?"
    r"(?:\+[0-9A-Za-z.-]+)?$"
)
INTERNAL_PACKAGE_RE = re.compile(r"^@kfm/[a-z0-9][a-z0-9._-]*$")
SHA256_RE = re.compile(r"^sha256:[a-f0-9]{64}$")
WORKSPACE_PATTERN_RE = re.compile(r"^[A-Za-z0-9._-]+/\*$")
LOCKFILE_PACKAGE_RE = re.compile(r"^  (?P<key>.+):$")
WORKFLOW_ENV_RE_TEMPLATE = r"(?m)^\s*{name}:\s*[\"']?{value}[\"']?\s*(?:#.*)?$"
INSTALL_COMMAND_RE = re.compile(
    r"(?:^|[;&|]\s*)(?:(?:command|env|sudo)\s+)*"
    r"(?P<manager>pnpm|npm|yarn|bun)\s+"
    r"(?P<verb>install|i|ci)\b(?P<args>[^\n]*)",
    flags=re.MULTILINE,
)


class PolicyShapeError(ValueError):
    """Raised internally when the policy cannot be normalized safely."""


def _finding(code: str, path: str, message: str) -> dict[str, str]:
    return {"code": code, "path": path, "message": message}


def _finalize_report(
    outcome: str,
    findings: Iterable[dict[str, str]],
    **details: Any,
) -> dict[str, Any]:
    ordered = sorted(
        findings,
        key=lambda item: (item["path"], item["code"], item["message"]),
    )
    return {
        "report_type": "pnpm_supply_chain_policy",
        "outcome": outcome,
        "reason_codes": sorted({item["code"] for item in ordered}),
        "findings": ordered,
        **details,
        "authority": {
            "network_access": False,
            "package_install": False,
            "registry_mutation": False,
            "dependency_admission": False,
            "policy_approval": False,
            "promotion": False,
            "release": False,
            "deployment": False,
            "publication": False,
        },
    }


def render_report(report: Mapping[str, Any]) -> str:
    """Return a stable, one-line JSON representation."""

    return json.dumps(report, sort_keys=True, separators=(",", ":"))


def _safe_root(value: Path | str) -> tuple[Path | None, list[dict[str, str]]]:
    supplied = Path(value)
    if supplied.is_symlink():
        return None, [
            _finding(
                "REPOSITORY_ROOT_UNSAFE",
                "/",
                "repository root must not be a symlink",
            )
        ]
    try:
        root = supplied.resolve(strict=True)
    except OSError as exc:
        return None, [
            _finding(
                "REPOSITORY_ROOT_INVALID",
                "/",
                f"repository root is unavailable: {exc}",
            )
        ]
    if not root.is_dir():
        return None, [
            _finding(
                "REPOSITORY_ROOT_INVALID",
                "/",
                "repository root must be a directory",
            )
        ]
    return root, []


def _safe_relative_path(root: Path, relative: str, *, field: str) -> Path:
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise PolicyShapeError(f"{field} must be a repository-relative path")
    resolved = (root / candidate).resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise PolicyShapeError(f"{field} escapes the repository root") from exc
    return resolved


def _read_regular_bytes(
    path: Path,
    *,
    display_path: str,
    missing_code: str,
    unsafe_code: str,
    invalid_code: str,
    findings: list[dict[str, str]],
) -> bytes | None:
    if path.is_symlink():
        findings.append(
            _finding(unsafe_code, display_path, "path must not be a symlink")
        )
        return None
    if not path.exists():
        findings.append(_finding(missing_code, display_path, "file is missing"))
        return None
    if not path.is_file():
        findings.append(
            _finding(unsafe_code, display_path, "path must be a regular file")
        )
        return None
    try:
        return path.read_bytes()
    except OSError as exc:
        findings.append(
            _finding(invalid_code, display_path, f"file could not be read: {exc}")
        )
        return None


def _decode_utf8(
    payload: bytes | None,
    *,
    display_path: str,
    invalid_code: str,
    findings: list[dict[str, str]],
) -> str | None:
    if payload is None:
        return None
    try:
        return payload.decode("utf-8")
    except UnicodeError as exc:
        findings.append(
            _finding(invalid_code, display_path, f"file is not valid UTF-8: {exc}")
        )
        return None


def _load_json_object(
    text: str | None,
    *,
    display_path: str,
    invalid_code: str,
    findings: list[dict[str, str]],
) -> dict[str, Any] | None:
    if text is None:
        return None
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        findings.append(
            _finding(
                invalid_code,
                display_path,
                f"invalid JSON at line {exc.lineno} column {exc.colno}",
            )
        )
        return None
    if not isinstance(value, dict):
        findings.append(
            _finding(invalid_code, display_path, "JSON root must be an object")
        )
        return None
    return value


def _require_exact_keys(
    value: Mapping[str, Any],
    expected: set[str],
    *,
    field: str,
) -> None:
    actual = set(value)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise PolicyShapeError(f"{field} keys mismatch: missing={missing}; extra={extra}")


def _require_string(value: Any, *, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise PolicyShapeError(f"{field} must be a nonempty string")
    return value


def _require_bool(value: Any, *, field: str) -> bool:
    if not isinstance(value, bool):
        raise PolicyShapeError(f"{field} must be a boolean")
    return value


def _normalize_policy(raw: Mapping[str, Any]) -> dict[str, Any]:
    _require_exact_keys(
        raw,
        {
            "policy_id",
            "version",
            "status",
            "source_idea_ids",
            "package_manager",
            "node_engine",
            "registries",
            "requirements",
            "npmrc",
            "lockfile",
            "version_range_exceptions",
            "workflows",
            "non_effects",
        },
        field="policy",
    )

    policy_id = _require_string(raw["policy_id"], field="policy.policy_id")
    if policy_id != REQUIRED_POLICY_ID:
        raise PolicyShapeError(f"policy.policy_id must be {REQUIRED_POLICY_ID}")
    version = _require_string(raw["version"], field="policy.version")
    if version != "v1":
        raise PolicyShapeError("policy.version must be v1")
    status = _require_string(raw["status"], field="policy.status")
    if status not in {"PROPOSED", "ACTIVE"}:
        raise PolicyShapeError("policy.status must be PROPOSED or ACTIVE")

    source_ids = raw["source_idea_ids"]
    if not isinstance(source_ids, list) or any(
        not isinstance(item, str) for item in source_ids
    ):
        raise PolicyShapeError("policy.source_idea_ids must be a string array")
    if tuple(source_ids) != REQUIRED_SOURCE_IDEAS:
        raise PolicyShapeError(
            "policy.source_idea_ids must preserve the ordered Pass 8 source set"
        )

    package_manager = _require_string(
        raw["package_manager"], field="policy.package_manager"
    )
    if package_manager != PACKAGE_MANAGER:
        raise PolicyShapeError(f"policy.package_manager must be {PACKAGE_MANAGER}")
    node_engine = _require_string(raw["node_engine"], field="policy.node_engine")
    if node_engine != NODE_ENGINE:
        raise PolicyShapeError(f"policy.node_engine must be {NODE_ENGINE}")

    registries = raw["registries"]
    if not isinstance(registries, dict):
        raise PolicyShapeError("policy.registries must be an object")
    _require_exact_keys(
        registries,
        {
            "default",
            "allowed",
            "internal_scope",
            "internal_scope_registry",
            "internal_resolution",
            "deny_sink",
        },
        field="policy.registries",
    )
    if registries["default"] != DEFAULT_REGISTRY:
        raise PolicyShapeError(
            f"policy.registries.default must be {DEFAULT_REGISTRY}"
        )
    if registries["allowed"] != [DEFAULT_REGISTRY]:
        raise PolicyShapeError(
            "policy.registries.allowed must contain only the explicit public registry"
        )
    if registries["internal_scope"] != INTERNAL_SCOPE:
        raise PolicyShapeError(
            f"policy.registries.internal_scope must be {INTERNAL_SCOPE}"
        )
    if registries["internal_scope_registry"] != INTERNAL_DENY_REGISTRY:
        raise PolicyShapeError(
            "policy.registries.internal_scope_registry must remain the reserved deny sink"
        )
    if registries["internal_resolution"] != "workspace_only":
        raise PolicyShapeError(
            "policy.registries.internal_resolution must be workspace_only"
        )
    if _require_bool(registries["deny_sink"], field="policy.registries.deny_sink") is not True:
        raise PolicyShapeError("policy.registries.deny_sink must be true")

    requirements = raw["requirements"]
    if not isinstance(requirements, dict):
        raise PolicyShapeError("policy.requirements must be an object")
    required_requirement_keys = {
        "private_workspaces",
        "exact_versions",
        "lockfile_integrity",
        "lifecycle_scripts_disabled",
        "frozen_lockfile",
    }
    _require_exact_keys(
        requirements,
        required_requirement_keys,
        field="policy.requirements",
    )
    for key in sorted(required_requirement_keys):
        if _require_bool(requirements[key], field=f"policy.requirements.{key}") is not True:
            raise PolicyShapeError(f"policy.requirements.{key} must be true")

    npmrc = raw["npmrc"]
    if not isinstance(npmrc, dict):
        raise PolicyShapeError("policy.npmrc must be an object")
    if npmrc != REQUIRED_NPMRC:
        raise PolicyShapeError(
            "policy.npmrc must match the fail-closed v1 package-manager settings"
        )

    lockfile = raw["lockfile"]
    if not isinstance(lockfile, dict):
        raise PolicyShapeError("policy.lockfile must be an object")
    _require_exact_keys(lockfile, {"path", "sha256"}, field="policy.lockfile")
    lockfile_path = _require_string(lockfile["path"], field="policy.lockfile.path")
    if lockfile_path != "pnpm-lock.yaml":
        raise PolicyShapeError("policy.lockfile.path must be pnpm-lock.yaml")
    lockfile_sha256 = _require_string(
        lockfile["sha256"], field="policy.lockfile.sha256"
    )
    if SHA256_RE.fullmatch(lockfile_sha256) is None:
        raise PolicyShapeError(
            "policy.lockfile.sha256 must be sha256 followed by 64 lowercase hex characters"
        )

    exceptions_raw = raw["version_range_exceptions"]
    if not isinstance(exceptions_raw, list):
        raise PolicyShapeError("policy.version_range_exceptions must be an array")
    exceptions: dict[tuple[str, str, str], dict[str, Any]] = {}
    for index, item in enumerate(exceptions_raw):
        field = f"policy.version_range_exceptions[{index}]"
        if not isinstance(item, dict):
            raise PolicyShapeError(f"{field} must be an object")
        _require_exact_keys(
            item,
            {
                "manifest",
                "field",
                "name",
                "specifier",
                "reason",
                "expires_on_change",
            },
            field=field,
        )
        manifest = _require_string(item["manifest"], field=f"{field}.manifest")
        dependency_field = _require_string(item["field"], field=f"{field}.field")
        if dependency_field not in DEPENDENCY_FIELDS:
            raise PolicyShapeError(f"{field}.field is not a dependency field")
        name = _require_string(item["name"], field=f"{field}.name")
        if name.startswith(f"{INTERNAL_SCOPE}/"):
            raise PolicyShapeError(f"{field} cannot exempt an internal package")
        specifier = _require_string(item["specifier"], field=f"{field}.specifier")
        if EXACT_SEMVER_RE.fullmatch(specifier):
            raise PolicyShapeError(f"{field} is unnecessary because the specifier is exact")
        _require_string(item["reason"], field=f"{field}.reason")
        if _require_bool(
            item["expires_on_change"], field=f"{field}.expires_on_change"
        ) is not True:
            raise PolicyShapeError(f"{field}.expires_on_change must be true")
        key = (manifest, dependency_field, name)
        if key in exceptions:
            raise PolicyShapeError(f"duplicate version exception for {key}")
        exceptions[key] = dict(item)

    workflows = raw["workflows"]
    if not isinstance(workflows, dict):
        raise PolicyShapeError("policy.workflows must be an object")
    _require_exact_keys(
        workflows,
        {
            "root",
            "allowed_package_manager",
            "required_pnpm_install_flags",
            "required_env",
        },
        field="policy.workflows",
    )
    if workflows["root"] != ".github/workflows":
        raise PolicyShapeError("policy.workflows.root must be .github/workflows")
    if workflows["allowed_package_manager"] != "pnpm":
        raise PolicyShapeError("policy.workflows.allowed_package_manager must be pnpm")
    if workflows["required_pnpm_install_flags"] != [
        "--frozen-lockfile",
        "--ignore-scripts",
    ]:
        raise PolicyShapeError(
            "policy.workflows.required_pnpm_install_flags must preserve v1 ordering"
        )
    if workflows["required_env"] != REQUIRED_WORKFLOW_ENV:
        raise PolicyShapeError(
            "policy.workflows.required_env must require both npm and pnpm ignore-scripts variables"
        )

    non_effects = raw["non_effects"]
    if not isinstance(non_effects, list) or not non_effects or any(
        not isinstance(item, str) or not item for item in non_effects
    ):
        raise PolicyShapeError("policy.non_effects must be a nonempty string array")

    return {
        **dict(raw),
        "version_range_exceptions_by_key": exceptions,
    }


def _load_policy(
    root: Path,
    policy_relative_path: str,
    findings: list[dict[str, str]],
) -> dict[str, Any] | None:
    try:
        policy_path = _safe_relative_path(
            root, policy_relative_path, field="policy path"
        )
    except PolicyShapeError as exc:
        findings.append(
            _finding("SUPPLY_CHAIN_POLICY_PATH_INVALID", policy_relative_path, str(exc))
        )
        return None
    payload = _read_regular_bytes(
        policy_path,
        display_path=policy_relative_path,
        missing_code="SUPPLY_CHAIN_POLICY_MISSING",
        unsafe_code="SUPPLY_CHAIN_POLICY_UNSAFE",
        invalid_code="SUPPLY_CHAIN_POLICY_INVALID",
        findings=findings,
    )
    text = _decode_utf8(
        payload,
        display_path=policy_relative_path,
        invalid_code="SUPPLY_CHAIN_POLICY_INVALID",
        findings=findings,
    )
    raw = _load_json_object(
        text,
        display_path=policy_relative_path,
        invalid_code="SUPPLY_CHAIN_POLICY_INVALID",
        findings=findings,
    )
    if raw is None:
        return None
    try:
        return _normalize_policy(raw)
    except PolicyShapeError as exc:
        findings.append(
            _finding(
                "SUPPLY_CHAIN_POLICY_INVALID",
                policy_relative_path,
                str(exc),
            )
        )
        return None


def _parse_npmrc(
    text: str | None,
    findings: list[dict[str, str]],
) -> dict[str, str]:
    values: dict[str, str] = {}
    if text is None:
        return values
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith(("#", ";")):
            continue
        if "=" not in line:
            findings.append(
                _finding(
                    "NPMRC_INVALID",
                    f".npmrc:{line_number}",
                    "configuration line must use key=value syntax",
                )
            )
            continue
        key, value = (part.strip() for part in line.split("=", 1))
        if not key or not value:
            findings.append(
                _finding(
                    "NPMRC_INVALID",
                    f".npmrc:{line_number}",
                    "configuration key and value must be nonempty",
                )
            )
            continue
        if key in values:
            findings.append(
                _finding(
                    "NPMRC_DUPLICATE_KEY",
                    f".npmrc:{line_number}",
                    f"duplicate configuration key: {key}",
                )
            )
            continue
        values[key] = value
    return values


def _validate_npmrc(
    root: Path,
    policy: Mapping[str, Any],
    findings: list[dict[str, str]],
) -> dict[str, str]:
    path = root / ".npmrc"
    payload = _read_regular_bytes(
        path,
        display_path=".npmrc",
        missing_code="NPMRC_MISSING",
        unsafe_code="NPMRC_UNSAFE",
        invalid_code="NPMRC_INVALID",
        findings=findings,
    )
    text = _decode_utf8(
        payload,
        display_path=".npmrc",
        invalid_code="NPMRC_INVALID",
        findings=findings,
    )
    actual = _parse_npmrc(text, findings)
    expected = policy["npmrc"]
    for key in sorted(expected):
        if actual.get(key) != expected[key]:
            findings.append(
                _finding(
                    "NPMRC_SETTING_MISMATCH",
                    ".npmrc",
                    f"{key} must be {expected[key]!r}, found {actual.get(key)!r}",
                )
            )
    unexpected = sorted(set(actual) - set(expected))
    for key in unexpected:
        findings.append(
            _finding(
                "NPMRC_UNAPPROVED_SETTING",
                ".npmrc",
                f"unapproved root package-manager setting: {key}",
            )
        )
    return actual


def _load_manifest(
    root: Path,
    relative_path: str,
    findings: list[dict[str, str]],
) -> dict[str, Any] | None:
    path = root / relative_path
    payload = _read_regular_bytes(
        path,
        display_path=relative_path,
        missing_code="PACKAGE_MANIFEST_MISSING",
        unsafe_code="PACKAGE_MANIFEST_UNSAFE",
        invalid_code="PACKAGE_MANIFEST_INVALID",
        findings=findings,
    )
    text = _decode_utf8(
        payload,
        display_path=relative_path,
        invalid_code="PACKAGE_MANIFEST_INVALID",
        findings=findings,
    )
    return _load_json_object(
        text,
        display_path=relative_path,
        invalid_code="PACKAGE_MANIFEST_INVALID",
        findings=findings,
    )


def _workspace_manifest_paths(
    root: Path,
    root_manifest: Mapping[str, Any] | None,
    findings: list[dict[str, str]],
) -> list[str]:
    paths: list[str] = ["package.json"]
    if root_manifest is None:
        return paths
    patterns = root_manifest.get("workspaces")
    if not isinstance(patterns, list) or not patterns or any(
        not isinstance(item, str) or not item for item in patterns
    ):
        findings.append(
            _finding(
                "PACKAGE_WORKSPACES_INVALID",
                "package.json#/workspaces",
                "workspaces must be a nonempty string array",
            )
        )
        return paths
    for pattern in patterns:
        if WORKSPACE_PATTERN_RE.fullmatch(pattern) is None:
            findings.append(
                _finding(
                    "WORKSPACE_PATTERN_UNSUPPORTED",
                    "package.json#/workspaces",
                    f"only immediate child patterns are supported: {pattern}",
                )
            )
            continue
        parent = root / pattern.removesuffix("/*")
        if parent.is_symlink():
            findings.append(
                _finding(
                    "WORKSPACE_PATH_UNSAFE",
                    pattern,
                    "workspace root must not be a symlink",
                )
            )
            continue
        if not parent.is_dir():
            findings.append(
                _finding(
                    "WORKSPACE_ROOT_MISSING",
                    pattern,
                    "workspace root is missing",
                )
            )
            continue
        for child in sorted(parent.iterdir(), key=lambda item: item.name):
            if child.is_symlink():
                findings.append(
                    _finding(
                        "WORKSPACE_PATH_UNSAFE",
                        child.relative_to(root).as_posix(),
                        "workspace path must not be a symlink",
                    )
                )
                continue
            manifest = child / "package.json"
            if child.is_dir() and (manifest.exists() or manifest.is_symlink()):
                paths.append(manifest.relative_to(root).as_posix())
    return sorted(set(paths))


def _validate_manifests(
    root: Path,
    policy: Mapping[str, Any],
    findings: list[dict[str, str]],
) -> tuple[list[str], list[dict[str, str]]]:
    root_manifest = _load_manifest(root, "package.json", findings)
    manifest_paths = _workspace_manifest_paths(root, root_manifest, findings)
    manifests: dict[str, dict[str, Any]] = {}
    if root_manifest is not None:
        manifests["package.json"] = root_manifest
    for relative_path in manifest_paths:
        if relative_path == "package.json":
            continue
        manifest = _load_manifest(root, relative_path, findings)
        if manifest is not None:
            manifests[relative_path] = manifest

    exceptions: Mapping[tuple[str, str, str], Mapping[str, Any]] = policy[
        "version_range_exceptions_by_key"
    ]
    used_exceptions: set[tuple[str, str, str]] = set()
    declarations: list[dict[str, str]] = []

    for relative_path in sorted(manifests):
        manifest = manifests[relative_path]
        if manifest.get("private") is not True:
            findings.append(
                _finding(
                    "WORKSPACE_NOT_PRIVATE",
                    f"{relative_path}#/private",
                    "root and workspace package manifests must set private=true",
                )
            )

        manager = manifest.get("packageManager")
        if relative_path == "package.json" and manager != policy["package_manager"]:
            findings.append(
                _finding(
                    "PACKAGE_MANAGER_POLICY_MISMATCH",
                    "package.json#/packageManager",
                    f"packageManager must be {policy['package_manager']}",
                )
            )
        if relative_path == "package.json":
            engines = manifest.get("engines")
            node_value = engines.get("node") if isinstance(engines, dict) else None
            if node_value != policy["node_engine"]:
                findings.append(
                    _finding(
                        "NODE_ENGINE_POLICY_MISMATCH",
                        "package.json#/engines/node",
                        f"engines.node must be {policy['node_engine']}",
                    )
                )

        if relative_path.startswith("packages/"):
            name = manifest.get("name")
            if not isinstance(name, str) or INTERNAL_PACKAGE_RE.fullmatch(name) is None:
                findings.append(
                    _finding(
                        "INTERNAL_PACKAGE_NAMESPACE_REQUIRED",
                        f"{relative_path}#/name",
                        "reusable packages under packages/ must use an @kfm/* name",
                    )
                )

        for dependency_field in DEPENDENCY_FIELDS:
            raw_dependencies = manifest.get(dependency_field, {})
            if raw_dependencies is None:
                continue
            if not isinstance(raw_dependencies, dict):
                findings.append(
                    _finding(
                        "DEPENDENCY_FIELD_INVALID",
                        f"{relative_path}#/{dependency_field}",
                        "dependency field must be an object",
                    )
                )
                continue
            for name in sorted(raw_dependencies):
                specifier = raw_dependencies[name]
                pointer = f"{relative_path}#/{dependency_field}/{name}"
                if not isinstance(name, str) or not name:
                    findings.append(
                        _finding(
                            "DEPENDENCY_NAME_INVALID",
                            pointer,
                            "dependency name must be a nonempty string",
                        )
                    )
                    continue
                if not isinstance(specifier, str) or not specifier:
                    findings.append(
                        _finding(
                            "DEPENDENCY_SPECIFIER_INVALID",
                            pointer,
                            "dependency specifier must be a nonempty string",
                        )
                    )
                    continue
                declarations.append(
                    {
                        "manifest": relative_path,
                        "field": dependency_field,
                        "name": name,
                        "specifier": specifier,
                    }
                )
                exception_key = (relative_path, dependency_field, name)
                exception = exceptions.get(exception_key)
                if exception is not None and exception["specifier"] == specifier:
                    used_exceptions.add(exception_key)
                    continue

                if name.startswith(f"{INTERNAL_SCOPE}/"):
                    workspace_spec = specifier.removeprefix("workspace:")
                    if not specifier.startswith("workspace:") or EXACT_SEMVER_RE.fullmatch(
                        workspace_spec
                    ) is None:
                        findings.append(
                            _finding(
                                "INTERNAL_DEPENDENCY_NOT_WORKSPACE_EXACT",
                                pointer,
                                "@kfm dependencies must use workspace:<exact-semver>",
                            )
                        )
                    continue

                if EXACT_SEMVER_RE.fullmatch(specifier) is None:
                    findings.append(
                        _finding(
                            "DEPENDENCY_SPECIFIER_NOT_EXACT",
                            pointer,
                            "third-party dependencies must use an exact semver unless the exact declaration is in the bounded exception list",
                        )
                    )

    for key, exception in sorted(exceptions.items()):
        if key not in used_exceptions:
            manifest, dependency_field, name = key
            findings.append(
                _finding(
                    "VERSION_RANGE_EXCEPTION_STALE",
                    f"{manifest}#/{dependency_field}/{name}",
                    f"exception no longer matches {exception['specifier']!r}",
                )
            )

    return sorted(manifest_paths), declarations


def _strip_yaml_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _parse_lockfile_version(text: str, findings: list[dict[str, str]]) -> None:
    version: str | None = None
    for line in text.splitlines():
        if line.startswith("lockfileVersion:"):
            version = _strip_yaml_scalar(line.split(":", 1)[1])
            break
    if version is None:
        findings.append(
            _finding(
                "LOCKFILE_VERSION_MISSING",
                "pnpm-lock.yaml",
                "lockfileVersion is missing",
            )
        )
    elif version != LOCKFILE_VERSION:
        findings.append(
            _finding(
                "LOCKFILE_VERSION_UNSUPPORTED",
                "pnpm-lock.yaml#/lockfileVersion",
                f"lockfileVersion must be {LOCKFILE_VERSION}, found {version}",
            )
        )


def _parse_lockfile_packages(
    text: str,
    findings: list[dict[str, str]],
) -> int:
    lines = text.splitlines()
    try:
        start = lines.index("packages:") + 1
    except ValueError:
        findings.append(
            _finding(
                "LOCKFILE_PACKAGES_MISSING",
                "pnpm-lock.yaml",
                "packages block is missing",
            )
        )
        return 0

    entries: list[tuple[str, list[tuple[int, str]]]] = []
    current_key: str | None = None
    current_lines: list[tuple[int, str]] = []
    for index in range(start, len(lines)):
        line = lines[index]
        if line and not line[0].isspace():
            break
        match = LOCKFILE_PACKAGE_RE.fullmatch(line)
        if match is not None:
            if current_key is not None:
                entries.append((current_key, current_lines))
            current_key = _strip_yaml_scalar(match.group("key"))
            current_lines = []
            continue
        if current_key is not None:
            current_lines.append((index + 1, line))
    if current_key is not None:
        entries.append((current_key, current_lines))

    if not entries:
        findings.append(
            _finding(
                "LOCKFILE_PACKAGES_MISSING",
                "pnpm-lock.yaml#/packages",
                "packages block is empty",
            )
        )
        return 0

    for key, entry_lines in entries:
        path = f"pnpm-lock.yaml#/packages/{key}"
        body = "\n".join(line for _line_number, line in entry_lines)
        if key.startswith(f"{INTERNAL_SCOPE}/") or key.startswith(
            f"'{INTERNAL_SCOPE}/"
        ):
            findings.append(
                _finding(
                    "INTERNAL_PACKAGE_RESOLVED_EXTERNALLY",
                    path,
                    "@kfm packages must remain workspace-only and absent from external package resolutions",
                )
            )
        if "resolution:" not in body:
            findings.append(
                _finding(
                    "LOCKFILE_RESOLUTION_MISSING",
                    path,
                    "external package entry has no resolution",
                )
            )
            continue
        if re.search(r"\bintegrity:\s*sha512-[A-Za-z0-9+/=]+", body) is None:
            findings.append(
                _finding(
                    "LOCKFILE_INTEGRITY_MISSING",
                    path,
                    "external package resolution must carry sha512 integrity",
                )
            )
        lowered = body.lower()
        if (
            "tarball:" in lowered
            or "http://" in lowered
            or "https://" in lowered
            or "file:" in lowered
            or "link:" in lowered
        ):
            findings.append(
                _finding(
                    "LOCKFILE_UNAPPROVED_RESOLUTION",
                    path,
                    "URL, tarball, file, and link resolutions are not allowed in the external package block",
                )
            )
    return len(entries)


def _validate_lockfile(
    root: Path,
    policy: Mapping[str, Any],
    findings: list[dict[str, str]],
) -> tuple[str | None, int]:
    relative_path = policy["lockfile"]["path"]
    try:
        path = _safe_relative_path(root, relative_path, field="policy.lockfile.path")
    except PolicyShapeError as exc:
        findings.append(
            _finding("LOCKFILE_PATH_INVALID", relative_path, str(exc))
        )
        return None, 0
    payload = _read_regular_bytes(
        path,
        display_path=relative_path,
        missing_code="PNPM_LOCKFILE_MISSING",
        unsafe_code="PNPM_LOCKFILE_UNSAFE",
        invalid_code="PNPM_LOCKFILE_INVALID",
        findings=findings,
    )
    if payload is None:
        return None, 0
    actual_sha256 = "sha256:" + hashlib.sha256(payload).hexdigest()
    expected_sha256 = policy["lockfile"]["sha256"]
    if actual_sha256 != expected_sha256:
        findings.append(
            _finding(
                "LOCKFILE_SHA256_MISMATCH",
                relative_path,
                f"expected={expected_sha256}; actual={actual_sha256}",
            )
        )
    text = _decode_utf8(
        payload,
        display_path=relative_path,
        invalid_code="PNPM_LOCKFILE_INVALID",
        findings=findings,
    )
    if text is None:
        return actual_sha256, 0
    _parse_lockfile_version(text, findings)
    package_count = _parse_lockfile_packages(text, findings)
    return actual_sha256, package_count


def _logical_shell_text(run_text: str) -> str:
    lines: list[str] = []
    pending = ""
    for raw_line in run_text.splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if pending:
            stripped = pending + " " + stripped
            pending = ""
        if stripped.endswith("\\"):
            pending = stripped[:-1].rstrip()
            continue
        lines.append(stripped)
    if pending:
        lines.append(pending)
    return "\n".join(lines)


def _extract_run_blocks(text: str) -> list[tuple[int, str]]:
    lines = text.splitlines()
    blocks: list[tuple[int, str]] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        match = re.match(r"^(?P<indent>\s*)run:\s*(?P<value>.*)$", line)
        if match is None:
            index += 1
            continue
        line_number = index + 1
        indent = len(match.group("indent"))
        value = match.group("value").strip()
        if value and not re.fullmatch(r"[>|][+-]?", value):
            blocks.append((line_number, value))
            index += 1
            continue
        collected: list[str] = []
        index += 1
        while index < len(lines):
            next_line = lines[index]
            if next_line.strip() and len(next_line) - len(next_line.lstrip()) <= indent:
                break
            collected.append(next_line)
            index += 1
        blocks.append((line_number, "\n".join(collected)))
    return blocks


def _workflow_has_env(text: str, name: str, value: str) -> bool:
    pattern = WORKFLOW_ENV_RE_TEMPLATE.format(
        name=re.escape(name), value=re.escape(value)
    )
    return re.search(pattern, text) is not None


def _validate_workflows(
    root: Path,
    policy: Mapping[str, Any],
    findings: list[dict[str, str]],
) -> tuple[int, int]:
    workflow_root = root / policy["workflows"]["root"]
    if workflow_root.is_symlink():
        findings.append(
            _finding(
                "WORKFLOW_ROOT_UNSAFE",
                policy["workflows"]["root"],
                "workflow root must not be a symlink",
            )
        )
        return 0, 0
    if not workflow_root.is_dir():
        findings.append(
            _finding(
                "WORKFLOW_ROOT_MISSING",
                policy["workflows"]["root"],
                "workflow root is missing",
            )
        )
        return 0, 0

    workflow_paths = sorted(
        {
            *workflow_root.glob("*.yml"),
            *workflow_root.glob("*.yaml"),
        },
        key=lambda item: item.name,
    )
    install_count = 0
    for path in workflow_paths:
        relative_path = path.relative_to(root).as_posix()
        payload = _read_regular_bytes(
            path,
            display_path=relative_path,
            missing_code="WORKFLOW_MISSING",
            unsafe_code="WORKFLOW_UNSAFE",
            invalid_code="WORKFLOW_INVALID",
            findings=findings,
        )
        text = _decode_utf8(
            payload,
            display_path=relative_path,
            invalid_code="WORKFLOW_INVALID",
            findings=findings,
        )
        if text is None:
            continue
        workflow_installs: list[tuple[int, re.Match[str]]] = []
        for line_number, run_block in _extract_run_blocks(text):
            logical = _logical_shell_text(run_block)
            for match in INSTALL_COMMAND_RE.finditer(logical):
                workflow_installs.append((line_number, match))
        if not workflow_installs:
            continue
        install_count += len(workflow_installs)

        for env_name, env_value in policy["workflows"]["required_env"].items():
            if not _workflow_has_env(text, env_name, env_value):
                findings.append(
                    _finding(
                        "WORKFLOW_IGNORE_SCRIPTS_ENV_MISSING",
                        relative_path,
                        f"workflow with package installation must set {env_name}: {env_value!r}",
                    )
                )

        for line_number, match in workflow_installs:
            manager = match.group("manager")
            verb = match.group("verb")
            args = match.group("args")
            path_label = f"{relative_path}:{line_number}"
            if manager != policy["workflows"]["allowed_package_manager"]:
                findings.append(
                    _finding(
                        "WORKFLOW_PACKAGE_MANAGER_INSTALL_DENIED",
                        path_label,
                        f"{manager} {verb} is denied; install lanes must use pnpm",
                    )
                )
                continue
            if verb not in {"install", "i"}:
                findings.append(
                    _finding(
                        "WORKFLOW_PACKAGE_MANAGER_INSTALL_DENIED",
                        path_label,
                        f"pnpm {verb} is not an approved install form",
                    )
                )
                continue
            for required_flag in policy["workflows"][
                "required_pnpm_install_flags"
            ]:
                if required_flag not in args.split():
                    findings.append(
                        _finding(
                            "WORKFLOW_INSTALL_FLAG_MISSING",
                            path_label,
                            f"pnpm install must include {required_flag}",
                        )
                    )
    return len(workflow_paths), install_count


def validate_repository(
    repository_root: Path | str,
    *,
    policy_path: str = DEFAULT_POLICY_PATH,
) -> dict[str, Any]:
    """Return a deterministic, no-network supply-chain policy report."""

    root, root_findings = _safe_root(repository_root)
    if root is None:
        return _finalize_report(
            "ERROR",
            root_findings,
            policy_id=None,
            policy_version=None,
            policy_status=None,
            manifest_paths=[],
            dependency_declarations=[],
            npmrc_settings={},
            lockfile_sha256=None,
            lockfile_package_count=0,
            checked_workflow_count=0,
            install_command_count=0,
        )

    findings: list[dict[str, str]] = []
    policy = _load_policy(root, policy_path, findings)
    if policy is None:
        return _finalize_report(
            "ERROR",
            findings,
            policy_id=None,
            policy_version=None,
            policy_status=None,
            manifest_paths=[],
            dependency_declarations=[],
            npmrc_settings={},
            lockfile_sha256=None,
            lockfile_package_count=0,
            checked_workflow_count=0,
            install_command_count=0,
        )

    npmrc_settings = _validate_npmrc(root, policy, findings)
    manifest_paths, dependency_declarations = _validate_manifests(
        root, policy, findings
    )
    lockfile_sha256, lockfile_package_count = _validate_lockfile(
        root, policy, findings
    )
    checked_workflow_count, install_command_count = _validate_workflows(
        root, policy, findings
    )

    for lockfile_name in COMPETING_LOCKFILES:
        path = root / lockfile_name
        if path.exists() or path.is_symlink():
            findings.append(
                _finding(
                    "COMPETING_LOCKFILE_PRESENT",
                    lockfile_name,
                    "accepted pnpm authority is ambiguous while a competing root lockfile exists",
                )
            )

    return _finalize_report(
        "PASS" if not findings else "ERROR",
        findings,
        policy_id=policy["policy_id"],
        policy_version=policy["version"],
        policy_status=policy["status"],
        manifest_paths=manifest_paths,
        dependency_declarations=dependency_declarations,
        npmrc_settings=npmrc_settings,
        lockfile_sha256=lockfile_sha256,
        lockfile_package_count=lockfile_package_count,
        checked_workflow_count=checked_workflow_count,
        install_command_count=install_command_count,
        version_range_exception_count=len(
            policy["version_range_exceptions_by_key"]
        ),
        registry_boundary={
            "default": policy["registries"]["default"],
            "internal_scope": policy["registries"]["internal_scope"],
            "internal_scope_registry": policy["registries"][
                "internal_scope_registry"
            ],
            "internal_resolution": policy["registries"]["internal_resolution"],
        },
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate deterministic pnpm registry, manifest, lockfile, and "
            "lifecycle-script policy without network access."
        )
    )
    parser.add_argument("--repository-root", default=".")
    parser.add_argument("--policy", default=DEFAULT_POLICY_PATH)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    report = validate_repository(
        args.repository_root,
        policy_path=args.policy,
    )
    print(render_report(report))
    return EXIT_PASS if report["outcome"] == "PASS" else EXIT_ERROR


if __name__ == "__main__":
    raise SystemExit(main())
