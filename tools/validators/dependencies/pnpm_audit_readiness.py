#!/usr/bin/env python3
"""Validate pnpm audit readiness and classify pnpm's JSON audit result.

The repository check is deliberately no-network. The audit classifier consumes
only a report produced by a separate ``pnpm audit --json`` process so registry
or command failures cannot be mistaken for a clean dependency result.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
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
COMPETING_LOCKFILES = (
    "package-lock.json",
    "npm-shrinkwrap.json",
    "yarn.lock",
    "bun.lock",
    "bun.lockb",
)
WORKSPACE_PATTERN_RE = re.compile(r"^[A-Za-z0-9._-]+/\*$")
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


def classify_audit(
    report_path: Path | str,
    *,
    command_exit_code: int,
    audit_level: str,
) -> dict[str, Any]:
    """Classify a pnpm JSON audit as PASS, REGRESSION, or ERROR."""

    findings: list[dict[str, str]] = []
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
        label="pnpm audit report",
        invalid_code="AUDIT_REPORT_INVALID",
        findings=findings,
    )
    counts = (
        _vulnerability_counts(raw_report, findings)
        if raw_report is not None
        else None
    )

    threshold_count: int | None = None
    outcome = "ERROR"
    if (
        counts is not None
        and audit_level in AUDIT_LEVELS
        and 0 <= command_exit_code <= 255
    ):
        threshold_index = SEVERITY_INDEX[audit_level]
        threshold_count = sum(
            count
            for severity, count in counts.items()
            if SEVERITY_INDEX[severity] >= threshold_index
        )
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
        "pnpm_audit_result",
        outcome,
        findings,
        audit_level=audit_level,
        command_exit_code=command_exit_code,
        threshold_count=threshold_count,
        vulnerability_counts=counts,
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate locked pnpm audit readiness and result polarity."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    readiness = subparsers.add_parser(
        "validate-repository",
        help="validate the no-network package-manager and lockfile preconditions",
    )
    readiness.add_argument("--repository-root", default=".")

    classify = subparsers.add_parser(
        "classify-audit",
        help="classify a pnpm audit JSON report without querying the network",
    )
    classify.add_argument("--report", required=True)
    classify.add_argument("--command-exit-code", required=True, type=int)
    classify.add_argument("--audit-level", default="high", choices=AUDIT_LEVELS)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "validate-repository":
        report = validate_repository(args.repository_root)
    else:
        report = classify_audit(
            args.report,
            command_exit_code=args.command_exit_code,
            audit_level=args.audit_level,
        )
    print(render_report(report))
    if report["outcome"] == "PASS":
        return EXIT_PASS
    if report["outcome"] == "REGRESSION":
        return EXIT_REGRESSION
    return EXIT_ERROR


if __name__ == "__main__":
    raise SystemExit(main())
