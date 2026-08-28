#!/usr/bin/env python3
"""Inventory browser-renderer acquisition surfaces without admitting a renderer.

This assessment is intentionally non-authoritative. It inventories bounded executable,
package, test, example, runtime, and public-web roots for renderer acquisition mechanisms
so ADR-0006/0007 can be enforced with structural evidence. PASS means the scan completed
with no renderer acquisition. HOLD means acquisition is confined to the accepted package
seam while runtime admission remains unresolved. FAIL means raw renderer acquisition
escaped that seam or parallel active MapLibre package homes surfaced. ERROR means the
bounded scan could not complete safely.

Imports of the KFM-owned ``@kfm/maplibre`` facade are consumer use of the accepted
MapRuntimePort boundary, not raw renderer acquisition. Only ``packages/maplibre/`` is an
approved candidate seam for a future raw renderer dependency or import.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Sequence

PROFILE = "kfm-maplibre-acquisition-inventory-v3"
TEXT_SUFFIXES = frozenset({".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".html"})
MAX_FILES = 5000
SCAN_ROOTS = ("apps", "packages", "runtime", "scripts", "tests", "examples", "public")
RENDERER_PACKAGES = ("maplibre-gl", "mapbox-gl", "cesium", "leaflet", "ol", "openlayers")
KFM_RENDERER_FACADES = ("@kfm/maplibre",)

PATTERNS = {
    "STATIC_IMPORT": re.compile(r"(?:^|\n)\s*import(?:\s+type)?(?:[\s\S]{0,160}?from\s*)?['\"]([^'\"]+)['\"]"),
    "DYNAMIC_IMPORT": re.compile(r"\bimport\s*\(\s*['\"]([^'\"]+)['\"]\s*\)"),
    "REQUIRE": re.compile(r"\brequire\s*\(\s*['\"]([^'\"]+)['\"]\s*\)"),
    "RE_EXPORT": re.compile(
        r"(?:^|\n)\s*export(?:\s+type)?(?:\s*\*(?:\s+as\s+[A-Za-z_$][\w$]*)?"
        r"|\s*\{[\s\S]{0,160}?\})"
        r"\s*from\s*['\"]([^'\"]+)['\"]"
    ),
    "IMPORT_META_RESOLVE": re.compile(
        r"\bimport\s*\.\s*meta\s*\.\s*resolve\s*\(\s*['\"]([^'\"]+)['\"]\s*\)"
    ),
    "REQUIRE_RESOLVE": re.compile(
        r"\brequire\s*\.\s*resolve\s*\(\s*['\"]([^'\"]+)['\"]\s*\)"
    ),
    "CDN_URL": re.compile(
        r"https?://(?:"
        r"(?:unpkg\.com|cdn\.jsdelivr\.net|cdnjs\.cloudflare\.com|esm\.sh)/"
        r"[^\s'\"<>`{}]*(?:maplibre|mapbox|cesium|leaflet|openlayers)[^\s'\"<>`{}]*"
        r"|[^\s'\"<>`{}]*(?:maplibre|mapbox|cesium|leaflet|openlayers)"
        r"[^\s'\"<>`{}]*\.(?:m?js|css)(?:[?#][^\s'\"<>`{}]*)?"
        r")",
        re.I,
    ),
    "GLOBAL_RUNTIME": re.compile(
        r"\b(?:maplibregl|mapboxgl|Cesium)\b(?=\s*(?:[.([;,)}\]]|$))"
    ),
    "PROTOCOL_REGISTRATION": re.compile(r"\baddProtocol\s*\("),
    "WORKER_ACQUISITION": re.compile(r"\bnew\s+Worker\s*\("),
}


class Outcome(StrEnum):
    PASS = "PASS"
    HOLD = "HOLD"
    FAIL = "FAIL"
    ERROR = "ERROR"


@dataclass(frozen=True)
class Finding:
    kind: str
    path: str
    subject: str
    candidate_seam: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "candidate_seam": self.candidate_seam,
            "kind": self.kind,
            "path": self.path,
            "subject": self.subject,
        }


@dataclass(frozen=True)
class Result:
    outcome: Outcome
    reasons: tuple[str, ...]
    findings: tuple[Finding, ...]
    scanned_files: int
    truncated: bool

    def to_dict(self) -> dict[str, object]:
        counts: dict[str, int] = {}
        for finding in self.findings:
            counts[finding.kind] = counts.get(finding.kind, 0) + 1
        return {
            "authority_created": False,
            "dependency_admitted": False,
            "findings": [finding.to_dict() for finding in self.findings],
            "finding_counts": dict(sorted(counts.items())),
            "outcome": self.outcome,
            "profile": PROFILE,
            "reasons": list(self.reasons),
            "renderer_selected": False,
            "scanned_files": self.scanned_files,
            "truncated": self.truncated,
        }


def _candidate_seam(path: str) -> bool:
    return path.startswith("packages/maplibre/")


def _is_kfm_renderer_facade(value: str) -> bool:
    lowered = value.lower()
    return any(
        lowered == facade or lowered.startswith(facade + "/")
        for facade in KFM_RENDERER_FACADES
    )


def _renderer_package_subject(value: str) -> str | None:
    lowered = value.lower()
    if _is_kfm_renderer_facade(lowered):
        return None
    for package in RENDERER_PACKAGES:
        if lowered == package or lowered.startswith(package + "/"):
            return package
    return None


def _renderer_subject(value: str) -> str | None:
    package = _renderer_package_subject(value)
    if package:
        return package
    lowered = value.lower()
    for marker in ("maplibre", "mapbox", "cesium", "leaflet", "openlayers"):
        if marker in lowered:
            return marker
    return None


def _renderer_import_subject(value: str) -> str | None:
    """Classify package or remote imports, not KFM-local filenames and aliases."""
    lowered = value.lower()
    if lowered.startswith(("http://", "https://")):
        return _renderer_subject(lowered)
    return _renderer_package_subject(lowered)


def _iter_files(root: Path) -> tuple[list[Path], bool]:
    files: list[Path] = []
    ignored_parts = {".git", "node_modules", "dist", "build", ".next", "coverage"}
    root_manifest = root / "package.json"
    if root_manifest.is_file():
        files.append(root_manifest)
    for root_name in SCAN_ROOTS:
        base = root / root_name
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file() or any(part in ignored_parts for part in path.parts):
                continue
            if path.name == "package.json" or path.suffix.lower() in TEXT_SUFFIXES:
                files.append(path)
                if len(files) > MAX_FILES:
                    return files[:MAX_FILES], True
    return files, False


def _scan_manifest(root: Path, path: Path) -> list[Finding]:
    rel = path.relative_to(root).as_posix()
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return [Finding("MANIFEST_UNREADABLE", rel, "package.json", False)]
    if not isinstance(value, dict):
        return [Finding("MANIFEST_UNREADABLE", rel, "package.json", False)]
    findings: list[Finding] = []
    for section in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
        deps = value.get(section)
        if not isinstance(deps, dict):
            continue
        for name in sorted(deps):
            subject = _renderer_package_subject(str(name))
            if subject:
                findings.append(Finding("MANIFEST_DEPENDENCY", rel, subject, _candidate_seam(rel)))
    return findings


def _scan_text(root: Path, path: Path) -> list[Finding]:
    rel = path.relative_to(root).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return [Finding("TEXT_UNREADABLE", rel, path.name, False)]
    findings: list[Finding] = []
    for kind in (
        "STATIC_IMPORT",
        "DYNAMIC_IMPORT",
        "REQUIRE",
        "RE_EXPORT",
        "IMPORT_META_RESOLVE",
        "REQUIRE_RESOLVE",
    ):
        for match in PATTERNS[kind].finditer(text):
            subject = _renderer_import_subject(match.group(1))
            if subject:
                findings.append(Finding(kind, rel, subject, _candidate_seam(rel)))
    for kind in ("CDN_URL", "GLOBAL_RUNTIME"):
        for match in PATTERNS[kind].finditer(text):
            subject = _renderer_subject(match.group(0))
            if subject:
                findings.append(Finding(kind, rel, subject, _candidate_seam(rel)))
    lower = text.lower()
    if "maplibre" in lower or "mapbox" in lower:
        if PATTERNS["PROTOCOL_REGISTRATION"].search(text):
            findings.append(Finding("PROTOCOL_REGISTRATION", rel, "renderer-protocol", _candidate_seam(rel)))
        if PATTERNS["WORKER_ACQUISITION"].search(text):
            findings.append(Finding("WORKER_ACQUISITION", rel, "renderer-worker", _candidate_seam(rel)))
    return findings


def scan(root: Path) -> Result:
    if not root.is_dir():
        return Result(Outcome.ERROR, ("ROOT_NOT_DIRECTORY",), (), 0, False)
    files, truncated = _iter_files(root)
    findings: list[Finding] = []
    for path in files:
        findings.extend(_scan_manifest(root, path) if path.name == "package.json" else _scan_text(root, path))

    unique = tuple(sorted(set(findings), key=lambda item: (item.path, item.kind, item.subject, item.candidate_seam)))
    reasons: set[str] = set()
    package_homes = {
        finding.path.rsplit("/", 1)[0]
        for finding in unique
        if finding.kind == "MANIFEST_DEPENDENCY" and finding.subject == "maplibre-gl"
    }
    active_package_homes = {home for home in package_homes if home.startswith("packages/")}
    if len(active_package_homes) > 1:
        reasons.add("PARALLEL_MAPLIBRE_PACKAGE_HOMES")
    if any(finding.kind in {"MANIFEST_UNREADABLE", "TEXT_UNREADABLE"} for finding in unique):
        reasons.add("SCAN_INPUT_UNREADABLE")
    if truncated:
        reasons.add("SCAN_TRUNCATED")
    if any(not finding.candidate_seam for finding in unique):
        reasons.add("ACQUISITION_OUTSIDE_CANDIDATE_SEAM")
    if unique:
        reasons.add("RENDERER_ACQUISITION_PRESENT")

    if "SCAN_INPUT_UNREADABLE" in reasons or "SCAN_TRUNCATED" in reasons:
        outcome = Outcome.ERROR
    elif "PARALLEL_MAPLIBRE_PACKAGE_HOMES" in reasons or "ACQUISITION_OUTSIDE_CANDIDATE_SEAM" in reasons:
        outcome = Outcome.FAIL
    elif reasons:
        outcome = Outcome.HOLD
    else:
        outcome = Outcome.PASS
    return Result(outcome, tuple(sorted(reasons)), unique, len(files), truncated)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--summary", action="store_true", help="omit individual findings")
    args = parser.parse_args(argv)
    result = scan(args.repo_root.resolve())
    payload = result.to_dict()
    if args.summary:
        payload["findings"] = []
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    return {Outcome.PASS: 0, Outcome.HOLD: 3, Outcome.FAIL: 1, Outcome.ERROR: 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
