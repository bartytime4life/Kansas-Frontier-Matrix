#!/usr/bin/env python3
"""Validate pnpm audit readiness and classify Node audit JSON results.

The repository check is deliberately no-network. The audit classifier consumes
only a report produced by a separate Node package-manager audit process so
registry or command failures cannot be mistaken for a clean dependency result.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Sequence

EXIT_PASS = 0
EXIT_REGRESSION = 1
EXIT_ERROR = 2

LOCKFILE_VERSION = "9.0"
NODE_ENGINE = ">=22.13 <23"
PACKAGE_MANAGER = "pnpm@11.17.0"
PNPM_VERSION = "11.17.0"
SEVERITIES = ("info", "low", "moderate", "high", "critical")
SEVERITY_INDEX = {severity: index for index, severity in enumerate(SEVERITIES)}
AUDIT_LEVELS = ("low", "moderate", "high", "critical")
AUDIT_MANAGERS = ("npm", "pnpm")
MAX_THRESHOLD_VULNERABILITIES = 50
MAX_ADVISORY_IDS_PER_VULNERABILITY = 10
MAX_AUDIT_TEXT_LENGTH = 256
COMPETING_LOCKFILES = (
    "package-lock.json",
    "npm-shrinkwrap.json",
    "yarn.lock",
    "bun.lock",
    "bun.lockb",
)
WORKSPACE_PATTERN_RE = re.compile(r"^[A-Za-z0-9._-]+/\*$")
EXCEPTION_REGISTER = "dependency_audit_exceptions"
EXCEPTION_KEYS = frozenset(
    {
        "advisory",
        "package",
        "version",
        "patch_path",
        "patch_sha256",
        "upstream_fix",
        "reason",
        "recorded_on",
        "expires_on",
        "human_review",
    }
)
MAX_EXCEPTIONS = 10
MAX_EXCEPTION_DAYS = 184
GHSA_RE = re.compile(r"GHSA(?:-[23456789cfghjmpqrvwx]{4}){3}")
PACKAGE_NAME_RE = re.compile(r"(?:@[a-z0-9._-]+/)?[a-z0-9._-]+")
EXACT_VERSION_RE = re.compile(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?")
SHA256_RE = re.compile(r"[0-9a-f]{64}")
LOCKFILE_IMPORTER_RE = re.compile(r"^  (?P<key>[^ \t:#][^:]*):(?:\s.*)?$")


def _finding(code: str, message: str) -> dict[str, str]:
    return {"code": code, "message": message}


def _finalize_report(
    report_type: str,
    outcome: str,
    findings: Iterable[dict[str, str]],
    **details: Any,
) -> dict[str, Any]:
    ordered_findings = sorted(
        findings, key=lambda item: (item["code"], item["message"])
    )
    return {
        "report_type": report_type,
        "outcome": outcome,
        "reason_codes": sorted({item["code"] for item in ordered_findings}),
        "findings": ordered_findings,
        **details,
    }


def render_report(report: dict[str, Any]) -> str:
    """Return a stable one-line JSON representation."""

    return json.dumps(report, sort_keys=True, separators=(",", ":"))


def _read_text_file(
    path: Path,
    *,
    missing_code: str,
    unsafe_code: str,
    invalid_code: str,
    findings: list[dict[str, str]],
) -> str | None:
    if path.is_symlink():
        findings.append(_finding(unsafe_code, f"{path.name} must not be a symlink"))
        return None
    if not path.exists():
        findings.append(_finding(missing_code, f"{path.name} is missing"))
        return None
    if not path.is_file():
        findings.append(
            _finding(unsafe_code, f"{path.name} must be a regular file")
        )
        return None
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        findings.append(
            _finding(invalid_code, f"{path.name} could not be read as UTF-8: {exc}")
        )
        return None


def _load_json_object(
    text: str | None,
    *,
    label: str,
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
                f"{label} is not valid JSON: line {exc.lineno} column {exc.colno}",
            )
        )
        return None
    if not isinstance(value, dict):
        findings.append(_finding(invalid_code, f"{label} must be a JSON object"))
        return None
    return value


def _strip_yaml_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def _parse_workspace_patterns(
    text: str | None, findings: list[dict[str, str]]
) -> list[str] | None:
    if text is None:
        return None

    patterns: list[str] = []
    in_packages = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line == "packages:":
            in_packages = True
            continue
        if in_packages and not line[0].isspace():
            break
        if not in_packages:
            continue
        match = re.fullmatch(r"  -\s+(.+)", line)
        if match is None:
            findings.append(
                _finding(
                    "PNPM_WORKSPACE_INVALID",
                    f"unsupported packages entry at pnpm-workspace.yaml:{line_number}",
                )
            )
            continue
        patterns.append(_strip_yaml_scalar(match.group(1)))

    if not in_packages:
        findings.append(
            _finding("PNPM_WORKSPACE_INVALID", "packages key is missing")
        )
        return None
    if not patterns:
        findings.append(
            _finding("PNPM_WORKSPACE_INVALID", "packages list must not be empty")
        )
        return None
    if len(patterns) != len(set(patterns)):
        findings.append(
            _finding("PNPM_WORKSPACE_INVALID", "packages list contains duplicates")
        )
    return patterns


def _parse_lockfile_importers(
    text: str | None, findings: list[dict[str, str]]
) -> tuple[str | None, list[str]]:
    if text is None:
        return None, []

    version: str | None = None
    importers: list[str] = []
    importer_block_seen = False
    in_importers = False

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.startswith("lockfileVersion:"):
            version = _strip_yaml_scalar(line.split(":", 1)[1])
        if line == "importers:":
            importer_block_seen = True
            in_importers = True
            continue
        if not in_importers:
            continue
        if line and not line[0].isspace():
            break
        match = LOCKFILE_IMPORTER_RE.fullmatch(line)
        if match is None:
            continue
        importer = _strip_yaml_scalar(match.group("key"))
        if importer.startswith("/") or ".." in Path(importer).parts:
            findings.append(
                _finding(
                    "LOCKFILE_IMPORTER_PATH_UNSAFE",
                    f"unsafe importer at pnpm-lock.yaml:{line_number}: {importer}",
                )
            )
            continue
        importers.append(importer)

    if version is None:
        findings.append(
            _finding("LOCKFILE_VERSION_MISSING", "lockfileVersion is missing")
        )
    elif version != LOCKFILE_VERSION:
        findings.append(
            _finding(
                "LOCKFILE_VERSION_UNSUPPORTED",
                f"lockfileVersion must be {LOCKFILE_VERSION}, found {version}",
            )
        )
    if not importer_block_seen:
        findings.append(
            _finding("LOCKFILE_IMPORTERS_MISSING", "importers block is missing")
        )
    elif not importers:
        findings.append(
            _finding("LOCKFILE_IMPORTERS_MISSING", "importers block is empty")
        )
    if len(importers) != len(set(importers)):
        findings.append(
            _finding("LOCKFILE_IMPORTERS_DUPLICATE", "importer keys must be unique")
        )
    return version, sorted(set(importers))


def _manifest_workspace_patterns(
    manifest: dict[str, Any] | None, findings: list[dict[str, str]]
) -> list[str] | None:
    if manifest is None:
        return None
    raw = manifest.get("workspaces")
    if (
        not isinstance(raw, list)
        or not raw
        or any(not isinstance(item, str) or not item for item in raw)
    ):
        findings.append(
            _finding(
                "PACKAGE_WORKSPACES_INVALID",
                "package.json workspaces must be a nonempty string array",
            )
        )
        return None
    if len(raw) != len(set(raw)):
        findings.append(
            _finding("PACKAGE_WORKSPACES_INVALID", "workspaces contains duplicates")
        )
    return list(raw)


def _discover_expected_importers(
    root: Path,
    patterns: list[str] | None,
    findings: list[dict[str, str]],
) -> list[str]:
    expected = {"."}
    if patterns is None:
        return sorted(expected)

    for pattern in patterns:
        if WORKSPACE_PATTERN_RE.fullmatch(pattern) is None:
            findings.append(
                _finding(
                    "WORKSPACE_PATTERN_UNSUPPORTED",
                    f"only immediate child patterns are supported: {pattern}",
                )
            )
            continue
        workspace_root = root / pattern.removesuffix("/*")
        if workspace_root.is_symlink():
            findings.append(
                _finding(
                    "WORKSPACE_PATH_UNSAFE",
                    f"workspace root must not be a symlink: {pattern}",
                )
            )
            continue
        if not workspace_root.is_dir():
            findings.append(
                _finding(
                    "WORKSPACE_ROOT_MISSING",
                    f"workspace root is missing: {pattern}",
                )
            )
            continue

        for child in sorted(workspace_root.iterdir(), key=lambda path: path.name):
            if child.is_symlink():
                findings.append(
                    _finding(
                        "WORKSPACE_PATH_UNSAFE",
                        "workspace child must not be a symlink: "
                        f"{child.relative_to(root)}",
                    )
                )
                continue
            if not child.is_dir():
                continue
            child_manifest_path = child / "package.json"
            if not (
                child_manifest_path.exists() or child_manifest_path.is_symlink()
            ):
                continue
            child_text = _read_text_file(
                child_manifest_path,
                missing_code="WORKSPACE_MANIFEST_MISSING",
                unsafe_code="WORKSPACE_MANIFEST_UNSAFE",
                invalid_code="WORKSPACE_MANIFEST_INVALID",
                findings=findings,
            )
            child_manifest = _load_json_object(
                child_text,
                label=str(child_manifest_path.relative_to(root)),
                invalid_code="WORKSPACE_MANIFEST_INVALID",
                findings=findings,
            )
            if child_manifest is not None:
                expected.add(child.relative_to(root).as_posix())
    return sorted(expected)


def validate_repository(repository_root: Path | str) -> dict[str, Any]:
    """Return a deterministic no-network readiness report."""

    findings: list[dict[str, str]] = []
    supplied_root = Path(repository_root)
    if supplied_root.is_symlink():
        return _finalize_report(
            "pnpm_audit_readiness",
            "ERROR",
            [
                _finding(
                    "REPOSITORY_ROOT_UNSAFE",
                    "repository root must not be a symlink",
                )
            ],
            package_manager=None,
            pnpm_version=None,
            node_engine=None,
            workspace_patterns=[],
            expected_importers=[],
            lockfile_importers=[],
        )
    try:
        root = supplied_root.resolve(strict=True)
    except OSError as exc:
        return _finalize_report(
            "pnpm_audit_readiness",
            "ERROR",
            [
                _finding(
                    "REPOSITORY_ROOT_INVALID",
                    f"repository root is unavailable: {exc}",
                )
            ],
            package_manager=None,
            pnpm_version=None,
            node_engine=None,
            workspace_patterns=[],
            expected_importers=[],
            lockfile_importers=[],
        )
    if not root.is_dir():
        return _finalize_report(
            "pnpm_audit_readiness",
            "ERROR",
            [
                _finding(
                    "REPOSITORY_ROOT_INVALID",
                    "repository root must be a directory",
                )
            ],
            package_manager=None,
            pnpm_version=None,
            node_engine=None,
            workspace_patterns=[],
            expected_importers=[],
            lockfile_importers=[],
        )

    manifest_text = _read_text_file(
        root / "package.json",
        missing_code="PACKAGE_MANIFEST_MISSING",
        unsafe_code="PACKAGE_MANIFEST_UNSAFE",
        invalid_code="PACKAGE_MANIFEST_INVALID",
        findings=findings,
    )
    manifest = _load_json_object(
        manifest_text,
        label="package.json",
        invalid_code="PACKAGE_MANIFEST_INVALID",
        findings=findings,
    )

    package_manager: str | None = None
    pnpm_version: str | None = None
    node_engine: str | None = None
    if manifest is not None:
        raw_manager = manifest.get("packageManager")
        if isinstance(raw_manager, str):
            package_manager = raw_manager
            if raw_manager == PACKAGE_MANAGER:
                pnpm_version = PNPM_VERSION
            else:
                findings.append(
                    _finding(
                        "PACKAGE_MANAGER_INVALID",
                        f"packageManager must be exactly {PACKAGE_MANAGER}",
                    )
                )
        else:
            findings.append(
                _finding(
                    "PACKAGE_MANAGER_INVALID",
                    f"packageManager must be exactly {PACKAGE_MANAGER}",
                )
            )

        engines = manifest.get("engines")
        if isinstance(engines, dict) and isinstance(engines.get("node"), str):
            node_engine = engines["node"]
        if node_engine != NODE_ENGINE:
            findings.append(
                _finding(
                    "NODE_ENGINE_MISMATCH",
                    f"engines.node must be {NODE_ENGINE}",
                )
            )

    manifest_patterns = _manifest_workspace_patterns(manifest, findings)
    workspace_text = _read_text_file(
        root / "pnpm-workspace.yaml",
        missing_code="PNPM_WORKSPACE_MISSING",
        unsafe_code="PNPM_WORKSPACE_UNSAFE",
        invalid_code="PNPM_WORKSPACE_INVALID",
        findings=findings,
    )
    pnpm_patterns = _parse_workspace_patterns(workspace_text, findings)
    if (
        manifest_patterns is not None
        and pnpm_patterns is not None
        and manifest_patterns != pnpm_patterns
    ):
        findings.append(
            _finding(
                "WORKSPACE_DEFINITION_MISMATCH",
                "package.json workspaces and pnpm-workspace.yaml packages differ",
            )
        )

    expected_importers = _discover_expected_importers(
        root, pnpm_patterns or manifest_patterns, findings
    )

    lockfile_text = _read_text_file(
        root / "pnpm-lock.yaml",
        missing_code="PNPM_LOCKFILE_MISSING",
        unsafe_code="PNPM_LOCKFILE_UNSAFE",
        invalid_code="PNPM_LOCKFILE_INVALID",
        findings=findings,
    )
    _lockfile_version, lockfile_importers = _parse_lockfile_importers(
        lockfile_text, findings
    )
    if set(expected_importers) != set(lockfile_importers):
        missing = sorted(set(expected_importers) - set(lockfile_importers))
        extra = sorted(set(lockfile_importers) - set(expected_importers))
        findings.append(
            _finding(
                "LOCKFILE_IMPORTER_MISMATCH",
                f"missing={missing}; extra={extra}",
            )
        )

    for lockfile_name in COMPETING_LOCKFILES:
        path = root / lockfile_name
        if path.exists() or path.is_symlink():
            findings.append(
                _finding(
                    "COMPETING_LOCKFILE_PRESENT",
                    f"competing root lockfile is present: {lockfile_name}",
                )
            )

    return _finalize_report(
        "pnpm_audit_readiness",
        "PASS" if not findings else "ERROR",
        findings,
        package_manager=package_manager,
        pnpm_version=pnpm_version,
        node_engine=node_engine,
        workspace_patterns=pnpm_patterns or manifest_patterns or [],
        expected_importers=expected_importers,
        lockfile_importers=lockfile_importers,
    )


def _vulnerability_counts(
    report: dict[str, Any], findings: list[dict[str, str]]
) -> dict[str, int] | None:
    metadata = report.get("metadata")
    raw_counts = metadata.get("vulnerabilities") if isinstance(metadata, dict) else None
    if not isinstance(raw_counts, dict):
        findings.append(
            _finding(
                "AUDIT_REPORT_INVALID",
                "metadata.vulnerabilities must be an object",
            )
        )
        return None

    counts: dict[str, int] = {}
    for severity in SEVERITIES:
        value = raw_counts.get(severity)
        if (
            not isinstance(value, int)
            or isinstance(value, bool)
            or value < 0
        ):
            findings.append(
                _finding(
                    "AUDIT_REPORT_INVALID",
                    f"metadata.vulnerabilities.{severity} must be a "
                    "nonnegative integer",
                )
            )
            continue
        counts[severity] = value
    return counts if len(counts) == len(SEVERITIES) else None


def _bounded_audit_text(value: Any) -> str | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        value = str(value)
    if not isinstance(value, str) or not value or len(value) > MAX_AUDIT_TEXT_LENGTH:
        return None
    return value


def _threshold_vulnerability_projection(
    report: dict[str, Any], audit_level: str
) -> dict[str, Any]:
    """Return bounded package/advisory identity without echoing raw audit data."""

    raw_vulnerabilities = report.get("vulnerabilities")
    if raw_vulnerabilities is None:
        return _legacy_threshold_advisory_projection(report, audit_level)
    if not isinstance(raw_vulnerabilities, dict):
        return {
            "status": "INVALID",
            "source_format": "modern_vulnerabilities",
            "total": 0,
            "truncated": False,
            "invalid_records": 1,
            "items": [],
        }

    threshold_index = SEVERITY_INDEX.get(audit_level)
    if threshold_index is None:
        return {
            "status": "INVALID",
            "source_format": "modern_vulnerabilities",
            "total": 0,
            "truncated": False,
            "invalid_records": len(raw_vulnerabilities),
            "items": [],
        }

    items: list[dict[str, Any]] = []
    invalid_records = 0
    for package_key, raw_entry in raw_vulnerabilities.items():
        package = _bounded_audit_text(package_key)
        if package is None or not isinstance(raw_entry, dict):
            invalid_records += 1
            continue

        declared_name = _bounded_audit_text(raw_entry.get("name"))
        if declared_name is not None:
            package = declared_name
        severity = raw_entry.get("severity")
        if severity not in SEVERITIES:
            invalid_records += 1
            continue
        if SEVERITY_INDEX[severity] < threshold_index:
            continue

        raw_via = raw_entry.get("via", [])
        if not isinstance(raw_via, list):
            invalid_records += 1
            raw_via = []
        advisory_ids: set[str] = set()
        for via_item in raw_via:
            if isinstance(via_item, dict):
                advisory_id = _bounded_audit_text(via_item.get("source"))
                if advisory_id is not None:
                    advisory_ids.add(advisory_id)

        ordered_ids = sorted(advisory_ids)
        raw_fix = raw_entry.get("fixAvailable")
        fix_available: bool | None = None
        fix_version: str | None = None
        if isinstance(raw_fix, bool):
            fix_available = raw_fix
        elif isinstance(raw_fix, dict):
            fix_available = True
            fix_version = _bounded_audit_text(raw_fix.get("version"))

        items.append(
            {
                "package": package,
                "severity": severity,
                "advisory_ids": ordered_ids[
                    :MAX_ADVISORY_IDS_PER_VULNERABILITY
                ],
                "advisory_ids_truncated": (
                    len(ordered_ids) > MAX_ADVISORY_IDS_PER_VULNERABILITY
                ),
                "fix_available": fix_available,
                "fix_version": fix_version,
            }
        )

    ordered_items = sorted(
        items,
        key=lambda item: (-SEVERITY_INDEX[item["severity"]], item["package"]),
    )
    return {
        "status": "PRESENT" if invalid_records == 0 else "PARTIAL_INVALID",
        "source_format": "modern_vulnerabilities",
        "total": len(ordered_items),
        "truncated": len(ordered_items) > MAX_THRESHOLD_VULNERABILITIES,
        "invalid_records": invalid_records,
        "items": ordered_items[:MAX_THRESHOLD_VULNERABILITIES],
    }


def _legacy_threshold_advisory_projection(
    report: dict[str, Any], audit_level: str
) -> dict[str, Any]:
    raw_advisories = report.get("advisories")
    if raw_advisories is None or raw_advisories == {}:
        return {
            "status": "NOT_PROVIDED",
            "source_format": None,
            "total": 0,
            "truncated": False,
            "invalid_records": 0,
            "items": [],
        }
    if not isinstance(raw_advisories, dict):
        return {
            "status": "INVALID",
            "source_format": "legacy_advisories",
            "total": 0,
            "truncated": False,
            "invalid_records": 1,
            "items": [],
        }

    threshold_index = SEVERITY_INDEX.get(audit_level)
    if threshold_index is None:
        return {
            "status": "INVALID",
            "source_format": "legacy_advisories",
            "total": 0,
            "truncated": False,
            "invalid_records": len(raw_advisories),
            "items": [],
        }

    items: list[dict[str, Any]] = []
    invalid_records = 0
    for advisory_key, raw_entry in raw_advisories.items():
        advisory_id = _bounded_audit_text(advisory_key)
        if advisory_id is None or not isinstance(raw_entry, dict):
            invalid_records += 1
            continue
        package = _bounded_audit_text(raw_entry.get("module_name"))
        severity = raw_entry.get("severity")
        if package is None or severity not in SEVERITIES:
            invalid_records += 1
            continue
        if SEVERITY_INDEX[severity] < threshold_index:
            continue

        advisory_ids = {advisory_id}
        github_advisory_id = _bounded_audit_text(
            raw_entry.get("github_advisory_id")
        )
        if github_advisory_id is not None:
            advisory_ids.add(github_advisory_id)
        ordered_ids = sorted(advisory_ids)
        items.append(
            {
                "package": package,
                "severity": severity,
                "advisory_ids": ordered_ids[
                    :MAX_ADVISORY_IDS_PER_VULNERABILITY
                ],
                "advisory_ids_truncated": (
                    len(ordered_ids) > MAX_ADVISORY_IDS_PER_VULNERABILITY
                ),
                "fix_available": None,
                "fix_version": None,
            }
        )

    ordered_items = sorted(
        items,
        key=lambda item: (
            -SEVERITY_INDEX[item["severity"]],
            item["package"],
            item["advisory_ids"],
        ),
    )
    return {
        "status": "PRESENT" if invalid_records == 0 else "PARTIAL_INVALID",
        "source_format": "legacy_advisories",
        "total": len(ordered_items),
        "truncated": len(ordered_items) > MAX_THRESHOLD_VULNERABILITIES,
        "invalid_records": invalid_records,
        "items": ordered_items[:MAX_THRESHOLD_VULNERABILITIES],
    }


def _parse_iso_day(value: Any) -> datetime.date | None:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return None
    try:
        return datetime.date.fromisoformat(value)
    except ValueError:
        return None


def _lockfile_package_versions(lockfile_text: str, package: str) -> set[str]:
    """Exact versions of ``package`` keyed in the lockfile packages/snapshots maps."""

    pattern = re.compile(
        rf"^  '?{re.escape(package)}@(?P<version>[^:(\s']+)", re.MULTILINE
    )
    return {match.group("version") for match in pattern.finditer(lockfile_text)}


def load_audit_exceptions(
    register_path: Path | str,
    repository_root: Path | str,
    *,
    today: datetime.date | None = None,
    findings: list[dict[str, str]],
) -> list[dict[str, str]] | None:
    """Load reviewed exceptions bound to an in-tree patch; invalid registers fail closed.

    An exception names one advisory for one exact locked package version. It is
    accepted only while unexpired, while its patch file hashes to the recorded
    digest, while ``pnpm-lock.yaml`` applies that patch hash to that version,
    and while no other version of the package is locked.
    """

    root = Path(repository_root)
    today = today or datetime.datetime.now(datetime.timezone.utc).date()
    register_text = _read_text_file(
        Path(register_path),
        missing_code="AUDIT_EXCEPTIONS_MISSING",
        unsafe_code="AUDIT_EXCEPTIONS_UNSAFE",
        invalid_code="AUDIT_EXCEPTIONS_INVALID",
        findings=findings,
    )
    register = _load_json_object(
        register_text,
        label="audit exception register",
        invalid_code="AUDIT_EXCEPTIONS_INVALID",
        findings=findings,
    )
    lockfile_text = _read_text_file(
        root / "pnpm-lock.yaml",
        missing_code="AUDIT_EXCEPTIONS_LOCKFILE_MISSING",
        unsafe_code="AUDIT_EXCEPTIONS_LOCKFILE_UNSAFE",
        invalid_code="AUDIT_EXCEPTIONS_LOCKFILE_INVALID",
        findings=findings,
    )
    if register is None or lockfile_text is None:
        return None

    def invalid(message: str) -> None:
        findings.append(_finding("AUDIT_EXCEPTIONS_INVALID", message))

    entries = register.get("exceptions")
    if register.get("register") != EXCEPTION_REGISTER or register.get("version") != "v1":
        invalid("register identity must be dependency_audit_exceptions v1")
        return None
    if not isinstance(entries, list) or len(entries) > MAX_EXCEPTIONS:
        invalid(f"exceptions must be a list of at most {MAX_EXCEPTIONS} entries")
        return None

    accepted: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    before = len(findings)
    for index, entry in enumerate(entries):
        label = f"exception {index}"
        if not isinstance(entry, dict) or set(entry) != EXCEPTION_KEYS:
            invalid(f"{label} must contain exactly the documented keys")
            continue
        advisory, package, version = entry["advisory"], entry["package"], entry["version"]
        patch_path, patch_sha256 = entry["patch_path"], entry["patch_sha256"]
        if not isinstance(advisory, str) or not GHSA_RE.fullmatch(advisory):
            invalid(f"{label} advisory must be one GHSA identifier")
            continue
        if not isinstance(package, str) or not PACKAGE_NAME_RE.fullmatch(package):
            invalid(f"{label} package name is invalid")
            continue
        if not isinstance(version, str) or not EXACT_VERSION_RE.fullmatch(version):
            invalid(f"{label} version must be one exact version")
            continue
        if (advisory, package) in seen:
            invalid(f"{label} duplicates an earlier advisory/package pair")
            continue
        seen.add((advisory, package))
        for text_key in ("upstream_fix", "reason", "human_review"):
            if _bounded_audit_text(entry[text_key]) is None:
                invalid(f"{label} {text_key} must be bounded non-empty text")
        if not str(entry["upstream_fix"]).startswith("https://"):
            invalid(f"{label} upstream_fix must be an https reference")
        recorded_on = _parse_iso_day(entry["recorded_on"])
        expires_on = _parse_iso_day(entry["expires_on"])
        if recorded_on is None or expires_on is None:
            invalid(f"{label} dates must be ISO calendar days")
            continue
        if not recorded_on <= expires_on or (expires_on - recorded_on).days > MAX_EXCEPTION_DAYS:
            invalid(f"{label} must expire within {MAX_EXCEPTION_DAYS} days of being recorded")
            continue
        if today > expires_on:
            findings.append(
                _finding("AUDIT_EXCEPTION_EXPIRED", f"{label} for {advisory} expired on {expires_on}")
            )
            continue
        if not isinstance(patch_sha256, str) or not SHA256_RE.fullmatch(patch_sha256):
            invalid(f"{label} patch_sha256 must be a lowercase SHA-256 digest")
            continue
        relative = PurePosixPath(patch_path) if isinstance(patch_path, str) else None
        if (
            relative is None
            or relative.is_absolute()
            or ".." in relative.parts
            or str(relative) != patch_path
            or not patch_path.endswith(".patch")
        ):
            invalid(f"{label} patch_path must be a repository-relative .patch file")
            continue
        patch_file = root.joinpath(*relative.parts)
        if any(part.is_symlink() for part in (patch_file, *patch_file.parents)) or not patch_file.is_file():
            invalid(f"{label} patch file is missing or unsafe")
            continue
        if hashlib.sha256(patch_file.read_bytes()).hexdigest() != patch_sha256:
            invalid(f"{label} patch file does not match patch_sha256")
            continue
        applied = re.search(
            rf"^patchedDependencies:\n(?:  .*\n)*?  '?{re.escape(package)}@{re.escape(version)}'?: {patch_sha256}$",
            lockfile_text,
            re.MULTILINE,
        )
        if applied is None:
            invalid(f"{label} lockfile does not apply this patch hash to {package}@{version}")
            continue
        locked = _lockfile_package_versions(lockfile_text, package)
        if locked != {version}:
            invalid(f"{label} lockfile must lock only {package}@{version}")
            continue
        accepted.append(
            {
                "advisory": advisory,
                "package": package,
                "version": version,
                "expires_on": expires_on.isoformat(),
            }
        )
    if len(findings) != before:
        return None
    return accepted


def _legacy_threshold_records(
    report: dict[str, Any], audit_level: str
) -> list[dict[str, Any]] | None:
    """Legacy advisories at or above threshold with their locked finding versions."""

    raw_advisories = report.get("advisories")
    threshold_index = SEVERITY_INDEX.get(audit_level)
    if not isinstance(raw_advisories, dict) or threshold_index is None:
        return None
    records: list[dict[str, Any]] = []
    for advisory_key, raw_entry in raw_advisories.items():
        if not isinstance(raw_entry, dict) or raw_entry.get("severity") not in SEVERITIES:
            return None
        if SEVERITY_INDEX[raw_entry["severity"]] < threshold_index:
            continue
        raw_findings = raw_entry.get("findings")
        versions = (
            {item.get("version") for item in raw_findings if isinstance(item, dict)}
            if isinstance(raw_findings, list)
            else set()
        )
        records.append(
            {
                "package": raw_entry.get("module_name"),
                "advisory_ids": {str(advisory_key), str(raw_entry.get("github_advisory_id"))},
                "versions": versions,
            }
        )
    return records


def classify_audit(
    report_path: Path | str,
    *,
    command_exit_code: int,
    audit_level: str,
    manager: str = "pnpm",
    exceptions: list[dict[str, str]] | None = None,
) -> dict[str, Any]:
    """Classify an npm-compatible JSON audit as PASS, REGRESSION, or ERROR.

    ``exceptions`` come from :func:`load_audit_exceptions`. A threshold finding
    is excepted only when its package, advisory and every locked finding
    version match one exception exactly; any other finding keeps its polarity.
    """

    findings: list[dict[str, str]] = []
    excepted: list[dict[str, str]] = []
    if manager not in AUDIT_MANAGERS:
        findings.append(
            _finding("AUDIT_MANAGER_INVALID", f"unsupported audit manager: {manager}")
        )
    if audit_level not in AUDIT_LEVELS:
        findings.append(
            _finding("AUDIT_LEVEL_INVALID", f"unsupported audit level: {audit_level}")
        )
    if command_exit_code < 0 or command_exit_code > 255:
        findings.append(
            _finding(
                "AUDIT_EXIT_CODE_INVALID",
                "command exit code must be between 0 and 255",
            )
        )

    report_text = _read_text_file(
        Path(report_path),
        missing_code="AUDIT_REPORT_MISSING",
        unsafe_code="AUDIT_REPORT_UNSAFE",
        invalid_code="AUDIT_REPORT_INVALID",
        findings=findings,
    )
    raw_report = _load_json_object(
        report_text,
        label=f"{manager} audit report",
        invalid_code="AUDIT_REPORT_INVALID",
        findings=findings,
    )
    counts = (
        _vulnerability_counts(raw_report, findings)
        if raw_report is not None
        else None
    )
    threshold_vulnerabilities = (
        _threshold_vulnerability_projection(raw_report, audit_level)
        if raw_report is not None
        else {
            "status": "NOT_PROVIDED",
            "source_format": None,
            "total": 0,
            "truncated": False,
            "invalid_records": 0,
            "items": [],
        }
    )

    threshold_count: int | None = None
    outcome = "ERROR"
    if (
        counts is not None
        and manager in AUDIT_MANAGERS
        and audit_level in AUDIT_LEVELS
        and 0 <= command_exit_code <= 255
    ):
        threshold_index = SEVERITY_INDEX[audit_level]
        threshold_count = sum(
            count
            for severity, count in counts.items()
            if SEVERITY_INDEX[severity] >= threshold_index
        )
        if (
            threshold_vulnerabilities["status"] == "PRESENT"
            and threshold_vulnerabilities["total"] != threshold_count
        ):
            threshold_vulnerabilities["status"] = "COUNT_MISMATCH"
        if exceptions and command_exit_code == 1 and threshold_count > 0:
            records = _legacy_threshold_records(raw_report, audit_level)
            attributable = (
                records is not None
                and len(records) == threshold_count
                and threshold_vulnerabilities["status"] == "PRESENT"
                and not threshold_vulnerabilities["truncated"]
            )
            if attributable:
                for record in records:
                    match = next(
                        (
                            exception
                            for exception in exceptions
                            if record["package"] == exception["package"]
                            and exception["advisory"] in record["advisory_ids"]
                            and record["versions"] == {exception["version"]}
                        ),
                        None,
                    )
                    if match is not None:
                        excepted.append(match)
            if attributable and len(excepted) == threshold_count:
                outcome = "PASS"
            elif excepted:
                findings.append(
                    _finding(
                        "VULNERABILITY_THRESHOLD_EXCEEDED",
                        f"{threshold_count - len(excepted)} vulnerabilities at or above {audit_level} "
                        f"after {len(excepted)} reviewed exceptions",
                    )
                )
                outcome = "REGRESSION"
        if outcome == "ERROR":
            if command_exit_code == 0 and threshold_count == 0:
                outcome = "PASS"
            elif command_exit_code == 1 and threshold_count > 0:
                outcome = "REGRESSION"
                findings.append(
                    _finding(
                        "VULNERABILITY_THRESHOLD_EXCEEDED",
                        f"{threshold_count} vulnerabilities at or above {audit_level}",
                    )
                )
            elif command_exit_code == 0:
                findings.append(
                    _finding(
                        "AUDIT_EXIT_CODE_INCONSISTENT",
                        "audit command succeeded despite threshold findings",
                    )
                )
            else:
                findings.append(
                    _finding(
                        "AUDIT_COMMAND_FAILED",
                        "audit command failed without threshold vulnerability findings",
                    )
                )

    return _finalize_report(
        (
            f"{manager}_audit_result"
            if manager in AUDIT_MANAGERS
            else "node_audit_result"
        ),
        outcome,
        findings,
        manager=manager,
        audit_level=audit_level,
        command_exit_code=command_exit_code,
        threshold_count=threshold_count,
        threshold_vulnerabilities=threshold_vulnerabilities,
        vulnerability_counts=counts,
        **({"excepted_vulnerabilities": sorted(excepted, key=lambda item: item["advisory"])}
           if exceptions is not None else {}),
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate locked Node audit readiness and result polarity."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    readiness = subparsers.add_parser(
        "validate-repository",
        help="validate the no-network package-manager and lockfile preconditions",
    )
    readiness.add_argument("--repository-root", default=".")

    classify = subparsers.add_parser(
        "classify-audit",
        help="classify an npm-compatible audit JSON report without querying the network",
    )
    classify.add_argument("--report", required=True)
    classify.add_argument("--command-exit-code", required=True, type=int)
    classify.add_argument("--audit-level", default="high", choices=AUDIT_LEVELS)
    classify.add_argument("--manager", default="pnpm", choices=AUDIT_MANAGERS)
    classify.add_argument(
        "--exceptions",
        help="reviewed exception register bound to in-tree dependency patches",
    )
    classify.add_argument(
        "--repository-root",
        default=".",
        help="repository root used to verify exception patch and lockfile bindings",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "validate-repository":
        report = validate_repository(args.repository_root)
    else:
        exceptions = None
        if args.exceptions is not None:
            exception_findings: list[dict[str, str]] = []
            exceptions = load_audit_exceptions(
                args.exceptions, args.repository_root, findings=exception_findings
            )
            if exceptions is None:
                report = _finalize_report(
                    f"{args.manager}_audit_result",
                    "ERROR",
                    exception_findings,
                    manager=args.manager,
                    audit_level=args.audit_level,
                    command_exit_code=args.command_exit_code,
                )
                print(render_report(report))
                return EXIT_ERROR
        report = classify_audit(
            args.report,
            command_exit_code=args.command_exit_code,
            audit_level=args.audit_level,
            manager=args.manager,
            exceptions=exceptions,
        )
    print(render_report(report))
    if report["outcome"] == "PASS":
        return EXIT_PASS
    if report["outcome"] == "REGRESSION":
        return EXIT_REGRESSION
    return EXIT_ERROR


if __name__ == "__main__":
    raise SystemExit(main())
