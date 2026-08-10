#!/usr/bin/env python3
"""Validate the bounded lifecycle/API overlay in contracts/OBJECT_MAP.md.

PASS proves only marker integrity, selected-family coverage, local path
resolution, and parity with the governed API's finite stub registry. It does
not establish ontology completeness, semantic correctness, lifecycle state,
policy, release, deployment, publication, or public API authority.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Callable, Mapping

REPO_ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = REPO_ROOT / "contracts/OBJECT_MAP.md"
API_SOURCE = Path("apps/governed-api/src")
START_MARKER = "<!-- KFM_RESOURCE_LIFECYCLE_OVERLAY_V1:START -->"
END_MARKER = "<!-- KFM_RESOURCE_LIFECYCLE_OVERLAY_V1:END -->"
ROUTE_HEADING = "### Current executable route registry"
RESOURCE_HEADING = "### Resource relationship map"
MAX_FILE_BYTES = 2 * 1024 * 1024
SCOPE = "contract-object-map-lifecycle-navigation-and-stub-parity-only"

REQUIRED_RESOURCES = frozenset(
    {
        "AIReceipt",
        "CatalogMatrix",
        "ClaimEnvelope",
        "CorrectionNotice",
        "DecisionEnvelope",
        "EvidenceBundle",
        "EvidenceDrawerPayload",
        "LayerManifest",
        "PolicyDecision",
        "ReleaseManifest",
        "ReviewRecord",
        "RollbackCard",
        "RuntimeResponseEnvelope",
        "SourceArtifact",
        "SourceDescriptor",
        "SourceIntakeRecord",
        "TileArtifactManifest",
    }
)

PATH_PATTERN = re.compile(
    r"`((?:apps|contracts|control_plane|docs|schemas|tests|tools)/[^`\n]+)`"
)
ROUTE_PATTERN = re.compile(r"^\| `(/[^`]+)` \|", re.MULTILINE)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _read_text(path: Path) -> tuple[str | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        return path.read_text(encoding="utf-8"), []
    except UnicodeDecodeError:
        return None, [Finding("INPUT_NOT_UTF8", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]


def _bounded_section(text: str) -> tuple[str | None, list[Finding]]:
    if text.count(START_MARKER) != 1 or text.count(END_MARKER) != 1:
        return None, [Finding("SECTION_MARKER_INVALID", "/overlay")]
    start = text.index(START_MARKER) + len(START_MARKER)
    end = text.index(END_MARKER)
    if start >= end:
        return None, [Finding("SECTION_MARKER_INVALID", "/overlay")]
    return text[start:end], []


def _canonical_path(value: str) -> PurePosixPath | None:
    if not value or value.startswith("/") or "\\" in value:
        return None
    path = PurePosixPath(value)
    if str(path) != value or any(part in {"", ".", ".."} for part in path.parts):
        return None
    return path


def _path_findings(section: str, repo_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        root = repo_root.resolve(strict=True)
    except OSError:
        return [Finding("REPO_ROOT_INVALID", "/repo_root")]
    for value in sorted(set(PATH_PATTERN.findall(section))):
        relative = _canonical_path(value)
        if relative is None:
            findings.append(Finding("PATH_INVALID", value))
            continue
        candidate = root.joinpath(*relative.parts)
        try:
            candidate.resolve(strict=True).relative_to(root)
        except (OSError, ValueError):
            findings.append(Finding("PATH_NOT_FOUND", value))
    return findings


def _load_routes(repo_root: Path) -> tuple[Mapping[str, Callable[[], object]] | None, list[Finding]]:
    api_source = repo_root / API_SOURCE
    original_path = list(sys.path)
    try:
        sys.path.insert(0, str(api_source))
        from governed_api.routes.registry import ROUTES
    except (ImportError, OSError, ValueError):
        return None, [Finding("ROUTE_REGISTRY_UNAVAILABLE", "apps/governed-api")]
    finally:
        sys.path[:] = original_path
    if not isinstance(ROUTES, Mapping):
        return None, [Finding("ROUTE_REGISTRY_INVALID", "apps/governed-api")]
    return ROUTES, []


def _route_findings(
    section: str,
    routes: Mapping[str, Callable[[], object]],
) -> list[Finding]:
    findings: list[Finding] = []
    if section.count(ROUTE_HEADING) != 1 or section.count(RESOURCE_HEADING) != 1:
        return [Finding("ROUTE_TABLE_INVALID", "/overlay/routes")]
    start = section.index(ROUTE_HEADING) + len(ROUTE_HEADING)
    end = section.index(RESOURCE_HEADING)
    if start >= end:
        return [Finding("ROUTE_TABLE_INVALID", "/overlay/routes")]
    documented = set(ROUTE_PATTERN.findall(section[start:end]))
    registered = set(routes)
    if documented != registered:
        findings.append(Finding("ROUTE_INVENTORY_MISMATCH", "/overlay/routes"))
    for route in sorted(registered):
        handler = routes[route]
        try:
            payload = handler()
        except Exception:  # bounded fail-closed adapter around registry handlers
            findings.append(Finding("ROUTE_HANDLER_FAILED", route))
            continue
        if not isinstance(payload, Mapping) or payload.get("decision") != "ABSTAIN" or payload.get("outcome") != "ABSTAIN":
            findings.append(Finding("ROUTE_NOT_ABSTAIN", route))
    return findings


def validate_object_map(
    path: Path = MAP_PATH,
    *,
    repo_root: Path = REPO_ROOT,
    routes: Mapping[str, Callable[[], object]] | None = None,
) -> ValidationResult:
    text, findings = _read_text(path)
    if text is None:
        return ValidationResult(tuple(sorted(set(findings))))
    section, section_findings = _bounded_section(text)
    findings.extend(section_findings)
    if section is None:
        return ValidationResult(tuple(sorted(set(findings))))

    for resource in sorted(REQUIRED_RESOURCES):
        if f"`{resource}`" not in section:
            findings.append(Finding("RESOURCE_FAMILY_MISSING", resource))
    findings.extend(_path_findings(section, repo_root))

    active_routes = routes
    if active_routes is None:
        active_routes, route_load_findings = _load_routes(repo_root)
        findings.extend(route_load_findings)
    if active_routes is not None:
        findings.extend(_route_findings(section, active_routes))
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def serialize(path: Path, result: ValidationResult, *, repo_root: Path = REPO_ROOT) -> str:
    return json.dumps(
        {
            "file": _display(path, repo_root),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=str(MAP_PATH))
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    args = parser.parse_args(argv)
    repo_root = Path(args.repo_root)
    path = Path(args.path)
    result = validate_object_map(path, repo_root=repo_root)
    print(serialize(path, result, repo_root=repo_root))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
