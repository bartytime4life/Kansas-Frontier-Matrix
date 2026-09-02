#!/usr/bin/env python3
"""Inventory browser-renderer acquisition surfaces without admitting a renderer.

This assessment is intentionally non-authoritative. It inventories bounded executable,
package, test, example, runtime, and public-web roots for renderer acquisition mechanisms,
including JavaScript and CSS imports, so ADR-0006/0007 can be enforced with structural
evidence. Descriptor reads fail closed
when identity, size, modification time, or change time differs across a bounded read, or
when a second bounded read has a different SHA-256 digest. Both verification passes count
against an explicit aggregate physical-read budget. PASS means the scan completed
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
import hashlib
import json
import os
import re
import stat
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Sequence

PROFILE = "kfm-maplibre-acquisition-inventory-v14"
TEXT_SUFFIXES = frozenset(
    {".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".html", ".css"}
)
MAX_FILES = 5000
MAX_INPUT_BYTES = 1024 * 1024
MAX_TOTAL_INPUT_BYTES = 16 * 1024 * 1024
MAX_TOTAL_PHYSICAL_READ_BYTES = 2 * MAX_TOTAL_INPUT_BYTES
SCAN_ROOTS = ("apps", "packages", "runtime", "scripts", "tests", "examples", "public")
RENDERER_PACKAGES = ("maplibre-gl", "mapbox-gl", "cesium", "leaflet", "ol", "openlayers")
KFM_RENDERER_FACADES = ("@kfm/maplibre",)
DESCRIPTOR_SAFETY_SUPPORTED = (
    hasattr(os, "O_DIRECTORY")
    and hasattr(os, "O_NOFOLLOW")
    and os.open in os.supports_dir_fd
    and os.stat in os.supports_dir_fd
    and os.stat in os.supports_follow_symlinks
)
INPUT_ERROR_KINDS = frozenset(
    {
        "INPUT_TOO_LARGE",
        "INPUT_CONTENT_CHANGED_DURING_VERIFICATION",
        "INPUT_CHANGED_DURING_READ",
        "INPUT_CHANGED_DURING_OPEN",
        "INPUT_DESCRIPTOR_SAFETY_UNAVAILABLE",
        "INPUT_NOT_REGULAR",
        "MANIFEST_UNREADABLE",
        "INPUT_OUTSIDE_ROOT",
        "SYMLINK_INPUT_DENIED",
        "TEXT_UNREADABLE",
        "TOTAL_INPUT_BUDGET_EXCEEDED",
        "TOTAL_PHYSICAL_READ_BUDGET_EXCEEDED",
    }
)

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
    "CSS_IMPORT": re.compile(
        r"(?:^|\n)\s*@import\s+(?:url\(\s*)?['\"]([^'\"]+)['\"]\s*\)?",
        re.I,
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

IDENTIFIER = r"[A-Za-z_$][\w$]*"
NODE_MODULE_SPECIFIER = r"(?:node:)?module"
CREATE_REQUIRE_NAMED_IMPORT = re.compile(
    rf"(?:^|\n)\s*import\s*\{{(?P<bindings>[\s\S]{{0,240}}?)\}}"
    rf"\s*from\s*['\"]{NODE_MODULE_SPECIFIER}['\"]"
)
CREATE_REQUIRE_NAMESPACE_IMPORT = re.compile(
    rf"(?:^|\n)\s*import\s*\*\s*as\s*(?P<name>{IDENTIFIER})"
    rf"\s*from\s*['\"]{NODE_MODULE_SPECIFIER}['\"]"
)
CREATE_REQUIRE_DESTRUCTURE = re.compile(
    rf"\b(?:const|let|var)\s*\{{(?P<bindings>[\s\S]{{0,240}}?)\}}\s*=\s*"
    rf"require\s*\(\s*['\"]{NODE_MODULE_SPECIFIER}['\"]\s*\)"
)
REGEX_PREFIX_KEYWORDS = frozenset(
    {
        "await",
        "case",
        "delete",
        "do",
        "else",
        "in",
        "instanceof",
        "new",
        "of",
        "return",
        "throw",
        "typeof",
        "void",
        "yield",
    }
)


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
    max_total_input_bytes: int
    max_total_physical_read_bytes: int
    scanned_files: int
    scanned_bytes: int
    physical_read_bytes: int
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
            "max_input_bytes": MAX_INPUT_BYTES,
            "max_total_input_bytes": self.max_total_input_bytes,
            "max_total_physical_read_bytes": self.max_total_physical_read_bytes,
            "scanned_bytes": self.scanned_bytes,
            "physical_read_bytes": self.physical_read_bytes,
            "scanned_files": self.scanned_files,
            "truncated": self.truncated,
        }


@dataclass
class ScanBudget:
    scanned_bytes: int = 0
    physical_read_bytes: int = 0


class _DescriptorSafetyUnavailable(Exception):
    pass


class _InputChangedDuringOpen(Exception):
    pass


class _InputChangedDuringRead(Exception):
    pass


class _InputContentChangedDuringVerification(Exception):
    pass


class _InputNotRegular(Exception):
    pass


class _TotalPhysicalReadBudgetExceeded(Exception):
    pass


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


def _create_require_factories(text: str) -> set[str]:
    """Return bounded Node ``createRequire`` factory expressions imported by a file."""
    factories: set[str] = set()
    for match in CREATE_REQUIRE_NAMED_IMPORT.finditer(text):
        for binding in match.group("bindings").split(","):
            parsed = re.fullmatch(
                rf"\s*createRequire(?:\s+as\s+(?P<alias>{IDENTIFIER}))?\s*",
                binding,
            )
            if parsed:
                factories.add(parsed.group("alias") or "createRequire")
    for match in CREATE_REQUIRE_NAMESPACE_IMPORT.finditer(text):
        factories.add(f'{match.group("name")}.createRequire')
    for match in CREATE_REQUIRE_DESTRUCTURE.finditer(text):
        for binding in match.group("bindings").split(","):
            parsed = re.fullmatch(
                rf"\s*createRequire(?:\s*:\s*(?P<alias>{IDENTIFIER}))?\s*",
                binding,
            )
            if parsed:
                factories.add(parsed.group("alias") or "createRequire")
    return factories


def _scan_create_require(text: str) -> list[tuple[str, str]]:
    """Classify literal renderer acquisition through imported ``createRequire`` aliases."""
    factories = _create_require_factories(text)
    if not factories:
        return []
    factory_pattern = (
        "(?:" + "|".join(re.escape(value) for value in sorted(factories)) + ")"
    )
    aliases = {
        match.group("alias")
        for match in re.finditer(
            rf"\b(?:const|let|var)\s+(?P<alias>{IDENTIFIER})\s*=\s*"
            rf"{factory_pattern}\s*\([^)]{{0,240}}\)",
            text,
        )
    }
    findings: list[tuple[str, str]] = []
    targets = [(factory_pattern + r"\s*\([^)]{0,240}\)\s*", True)]
    targets.extend((re.escape(alias), False) for alias in sorted(aliases))
    for target, chained in targets:
        prefix = r"(?<![\w$])" + target
        for kind, suffix in (
            ("CREATE_REQUIRE", ""),
            ("CREATE_REQUIRE_RESOLVE", r"\s*\.\s*resolve"),
        ):
            if chained and kind == "CREATE_REQUIRE_RESOLVE":
                suffix = r"\.\s*resolve"
            pattern = re.compile(
                prefix + suffix + r"\s*\(\s*['\"]([^'\"]+)['\"]\s*\)"
            )
            for match in pattern.finditer(text):
                subject = _renderer_import_subject(match.group(1))
                if subject:
                    findings.append((kind, subject))
    return findings


def _regex_literal_end(text: str, start: int) -> int | None:
    """Return the end of a bounded JavaScript regex literal, or ``None``."""
    index = start + 1
    in_character_class = False
    while index < len(text):
        character = text[index]
        if character in {"\r", "\n"}:
            return None
        if character == "\\":
            index += 2
            continue
        if character == "[":
            in_character_class = True
        elif character == "]":
            in_character_class = False
        elif character == "/" and not in_character_class:
            index += 1
            while index < len(text) and text[index].isalpha():
                index += 1
            return index
        index += 1
    return None


def _mask_comments(text: str) -> str:
    """Blank bounded JS/HTML comments while preserving strings, regexes, and lines."""
    masked = list(text)
    quote: str | None = None
    regex_allowed = True
    index = 0
    while index < len(text):
        character = text[index]
        if quote is not None:
            if character == "\\":
                index += 2
                continue
            if character == quote:
                quote = None
                regex_allowed = False
            index += 1
            continue
        if character in {"'", '"', "`"}:
            quote = character
            index += 1
            continue

        end: int | None = None
        if text.startswith("//", index):
            newline = text.find("\n", index + 2)
            end = len(text) if newline == -1 else newline
        elif text.startswith("/*", index):
            closing = text.find("*/", index + 2)
            end = len(text) if closing == -1 else closing + 2
        elif text.startswith("<!--", index):
            closing = text.find("-->", index + 4)
            end = len(text) if closing == -1 else closing + 3

        if end is None:
            if character == "/":
                regex_end = _regex_literal_end(text, index) if regex_allowed else None
                if regex_end is not None:
                    index = regex_end
                    regex_allowed = False
                    continue
                index += 2 if text.startswith("/=", index) else 1
                regex_allowed = True
                continue
            if character.isspace():
                index += 1
                continue
            if character.isalpha() or character in {"_", "$"}:
                token_end = index + 1
                while token_end < len(text) and (
                    text[token_end].isalnum() or text[token_end] in {"_", "$"}
                ):
                    token_end += 1
                regex_allowed = text[index:token_end] in REGEX_PREFIX_KEYWORDS
                index = token_end
                continue
            if character.isdigit():
                token_end = index + 1
                while token_end < len(text) and (
                    text[token_end].isalnum() or text[token_end] in {"_", "."}
                ):
                    token_end += 1
                regex_allowed = False
                index = token_end
                continue
            if character in ")]}":
                regex_allowed = False
            elif character not in {".", "~"}:
                regex_allowed = True
            index += 1
            continue
        for offset in range(index, end):
            if masked[offset] not in {"\r", "\n"}:
                masked[offset] = " "
        index = end
    return "".join(masked)


def _iter_files(root: Path) -> tuple[list[Path], bool]:
    files: list[Path] = []
    ignored_parts = {".git", "node_modules", "dist", "build", ".next", "coverage"}
    root_manifest = root / "package.json"
    if root_manifest.is_symlink() or root_manifest.is_file():
        files.append(root_manifest)
    for root_name in SCAN_ROOTS:
        base = root / root_name
        if base.is_symlink():
            files.append(base)
            if len(files) > MAX_FILES:
                return files[:MAX_FILES], True
            continue
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if any(part in ignored_parts for part in path.parts):
                continue
            if path.is_symlink():
                files.append(path)
                if len(files) > MAX_FILES:
                    return files[:MAX_FILES], True
                continue
            if not path.is_file():
                continue
            if path.name == "package.json" or path.suffix.lower() in TEXT_SUFFIXES:
                files.append(path)
                if len(files) > MAX_FILES:
                    return files[:MAX_FILES], True
    return files, False


def _same_file_identity(left: os.stat_result, right: os.stat_result) -> bool:
    return (
        left.st_dev,
        left.st_ino,
        stat.S_IFMT(left.st_mode),
    ) == (
        right.st_dev,
        right.st_ino,
        stat.S_IFMT(right.st_mode),
    )


def _same_read_metadata(left: os.stat_result, right: os.stat_result) -> bool:
    return _same_file_identity(left, right) and (
        left.st_size,
        left.st_mtime_ns,
        left.st_ctime_ns,
    ) == (
        right.st_size,
        right.st_mtime_ns,
        right.st_ctime_ns,
    )


def _verified_open_at(
    parent_fd: int, name: str, flags: int, *, require_directory: bool
) -> int:
    snapshot = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    expected_type = stat.S_ISDIR if require_directory else stat.S_ISREG
    if not expected_type(snapshot.st_mode):
        raise _InputNotRegular
    try:
        descriptor = os.open(name, flags, dir_fd=parent_fd)
    except OSError as error:
        try:
            current = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        except OSError:
            raise _InputChangedDuringOpen from error
        if not _same_file_identity(snapshot, current):
            raise _InputChangedDuringOpen from error
        raise
    opened = os.fstat(descriptor)
    if not _same_file_identity(snapshot, opened):
        os.close(descriptor)
        raise _InputChangedDuringOpen
    if not expected_type(opened.st_mode):
        os.close(descriptor)
        raise _InputNotRegular
    return descriptor


def _read_descriptor_bounded(
    root: Path, path: Path, read_limit: int, budget: ScanBudget
) -> bytes:
    if not DESCRIPTOR_SAFETY_SUPPORTED:
        raise _DescriptorSafetyUnavailable

    relative = path.relative_to(root)
    if not relative.parts or any(part in {"", ".", ".."} for part in relative.parts):
        raise _InputChangedDuringOpen

    close_on_exec = getattr(os, "O_CLOEXEC", 0)
    no_follow = os.O_NOFOLLOW
    directory_flags = os.O_RDONLY | os.O_DIRECTORY | no_follow | close_on_exec
    file_flags = (
        os.O_RDONLY
        | no_follow
        | close_on_exec
        | getattr(os, "O_NONBLOCK", 0)
    )
    resolved_root = root.resolve(strict=True)
    root_snapshot = os.stat(resolved_root, follow_symlinks=False)
    if not stat.S_ISDIR(root_snapshot.st_mode):
        raise _InputNotRegular
    root_fd = os.open(resolved_root, directory_flags)
    opened_root = os.fstat(root_fd)
    if not _same_file_identity(root_snapshot, opened_root):
        os.close(root_fd)
        raise _InputChangedDuringOpen

    parent_fd = root_fd
    try:
        for part in relative.parts[:-1]:
            next_fd = _verified_open_at(
                parent_fd, part, directory_flags, require_directory=True
            )
            if parent_fd != root_fd:
                os.close(parent_fd)
            parent_fd = next_fd
        file_fd = _verified_open_at(
            parent_fd, relative.parts[-1], file_flags, require_directory=False
        )
        try:
            def read_once() -> bytes:
                chunks: list[bytes] = []
                remaining = read_limit
                while remaining:
                    chunk = os.read(file_fd, remaining)
                    if not chunk:
                        break
                    chunks.append(chunk)
                    budget.physical_read_bytes += len(chunk)
                    remaining -= len(chunk)
                return b"".join(chunks)

            before_read = os.fstat(file_fd)
            planned_read_bytes = min(before_read.st_size, read_limit)
            physical_read_limit = max(
                MAX_TOTAL_PHYSICAL_READ_BYTES - budget.physical_read_bytes, 0
            )
            if planned_read_bytes * 2 > physical_read_limit:
                raise _TotalPhysicalReadBudgetExceeded
            read_limit = min(read_limit, physical_read_limit // 2)
            raw = read_once()
            after_read = os.fstat(file_fd)
            if not _same_read_metadata(before_read, after_read):
                raise _InputChangedDuringRead
            os.lseek(file_fd, 0, os.SEEK_SET)
            verification = read_once()
            after_verification = os.fstat(file_fd)
            if not _same_read_metadata(after_read, after_verification):
                raise _InputChangedDuringRead
            if hashlib.sha256(raw).digest() != hashlib.sha256(verification).digest():
                raise _InputContentChangedDuringVerification
            return raw
        finally:
            os.close(file_fd)
    finally:
        if parent_fd != root_fd:
            os.close(parent_fd)
        os.close(root_fd)


def _read_bounded_text(
    root: Path, path: Path, budget: ScanBudget, *, unreadable_kind: str
) -> tuple[str | None, Finding | None]:
    rel = path.relative_to(root).as_posix()
    if path.is_symlink():
        return None, Finding("SYMLINK_INPUT_DENIED", rel, "symlink", False)
    try:
        resolved_root = root.resolve(strict=True)
        resolved_path = path.resolve(strict=True)
    except OSError:
        return None, Finding(unreadable_kind, rel, path.name, False)
    if not resolved_path.is_relative_to(resolved_root):
        return None, Finding("INPUT_OUTSIDE_ROOT", rel, "resolved-outside-root", False)
    remaining_bytes = max(MAX_TOTAL_INPUT_BYTES - budget.scanned_bytes, 0)
    read_limit = min(MAX_INPUT_BYTES, remaining_bytes) + 1
    try:
        raw = _read_descriptor_bounded(root, path, read_limit, budget)
    except _TotalPhysicalReadBudgetExceeded:
        return None, Finding(
            "TOTAL_PHYSICAL_READ_BUDGET_EXCEEDED",
            rel,
            f"max-total-physical-read-bytes-{MAX_TOTAL_PHYSICAL_READ_BYTES}",
            False,
        )
    except _DescriptorSafetyUnavailable:
        return None, Finding(
            "INPUT_DESCRIPTOR_SAFETY_UNAVAILABLE",
            rel,
            "descriptor-no-follow-unavailable",
            False,
        )
    except _InputChangedDuringOpen:
        return None, Finding(
            "INPUT_CHANGED_DURING_OPEN", rel, "inode-identity-changed", False
        )
    except _InputChangedDuringRead:
        return None, Finding(
            "INPUT_CHANGED_DURING_READ", rel, "descriptor-metadata-changed", False
        )
    except _InputContentChangedDuringVerification:
        return None, Finding(
            "INPUT_CONTENT_CHANGED_DURING_VERIFICATION",
            rel,
            "descriptor-content-digest-changed",
            False,
        )
    except _InputNotRegular:
        return None, Finding("INPUT_NOT_REGULAR", rel, "not-regular-file", False)
    except OSError:
        return None, Finding(unreadable_kind, rel, path.name, False)
    budget.scanned_bytes += len(raw)
    if len(raw) > MAX_INPUT_BYTES:
        return None, Finding(
            "INPUT_TOO_LARGE", rel, f"max-bytes-{MAX_INPUT_BYTES}", False
        )
    if len(raw) > remaining_bytes:
        return None, Finding(
            "TOTAL_INPUT_BUDGET_EXCEEDED",
            rel,
            f"max-total-bytes-{MAX_TOTAL_INPUT_BYTES}",
            False,
        )
    try:
        return raw.decode("utf-8"), None
    except UnicodeError:
        return None, Finding(unreadable_kind, rel, path.name, False)


def _scan_manifest(root: Path, path: Path, budget: ScanBudget) -> list[Finding]:
    rel = path.relative_to(root).as_posix()
    text, error = _read_bounded_text(
        root, path, budget, unreadable_kind="MANIFEST_UNREADABLE"
    )
    if error:
        return [error]
    assert text is not None
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
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


def _scan_text(root: Path, path: Path, budget: ScanBudget) -> list[Finding]:
    text, error = _read_bounded_text(
        root, path, budget, unreadable_kind="TEXT_UNREADABLE"
    )
    if error:
        return [error]
    assert text is not None
    rel = path.relative_to(root).as_posix()
    scan_text = _mask_comments(text)
    findings: list[Finding] = []
    for kind in (
        "STATIC_IMPORT",
        "DYNAMIC_IMPORT",
        "REQUIRE",
        "RE_EXPORT",
        "IMPORT_META_RESOLVE",
        "REQUIRE_RESOLVE",
        "CSS_IMPORT",
    ):
        for match in PATTERNS[kind].finditer(scan_text):
            subject = _renderer_import_subject(match.group(1))
            if subject:
                findings.append(Finding(kind, rel, subject, _candidate_seam(rel)))
    for kind, subject in _scan_create_require(scan_text):
        findings.append(Finding(kind, rel, subject, _candidate_seam(rel)))
    for kind in ("CDN_URL", "GLOBAL_RUNTIME"):
        for match in PATTERNS[kind].finditer(scan_text):
            subject = _renderer_subject(match.group(0))
            if subject:
                findings.append(Finding(kind, rel, subject, _candidate_seam(rel)))
    lower = scan_text.lower()
    if "maplibre" in lower or "mapbox" in lower:
        if PATTERNS["PROTOCOL_REGISTRATION"].search(scan_text):
            findings.append(Finding("PROTOCOL_REGISTRATION", rel, "renderer-protocol", _candidate_seam(rel)))
        if PATTERNS["WORKER_ACQUISITION"].search(scan_text):
            findings.append(Finding("WORKER_ACQUISITION", rel, "renderer-worker", _candidate_seam(rel)))
    return findings


def scan(root: Path) -> Result:
    if not root.is_dir():
        return Result(
            Outcome.ERROR,
            ("ROOT_NOT_DIRECTORY",),
            (),
            MAX_TOTAL_INPUT_BYTES,
            MAX_TOTAL_PHYSICAL_READ_BYTES,
            0,
            0,
            0,
            False,
        )
    files, truncated = _iter_files(root)
    findings: list[Finding] = []
    budget = ScanBudget()
    scanned_files = 0
    for path in files:
        scanned_files += 1
        path_findings = (
            _scan_manifest(root, path, budget)
            if path.name == "package.json"
            else _scan_text(root, path, budget)
        )
        findings.extend(path_findings)
        if any(
            finding.kind
            in {
                "INPUT_CHANGED_DURING_OPEN",
                "INPUT_CHANGED_DURING_READ",
                "INPUT_CONTENT_CHANGED_DURING_VERIFICATION",
                "INPUT_DESCRIPTOR_SAFETY_UNAVAILABLE",
                "INPUT_NOT_REGULAR",
                "INPUT_OUTSIDE_ROOT",
                "INPUT_TOO_LARGE",
                "SYMLINK_INPUT_DENIED",
                "TOTAL_INPUT_BUDGET_EXCEEDED",
                "TOTAL_PHYSICAL_READ_BUDGET_EXCEEDED",
            }
            for finding in path_findings
        ):
            break

    unique = tuple(sorted(set(findings), key=lambda item: (item.path, item.kind, item.subject, item.candidate_seam)))
    acquisition_findings = tuple(
        finding for finding in unique if finding.kind not in INPUT_ERROR_KINDS
    )
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
    if any(finding.kind == "INPUT_TOO_LARGE" for finding in unique):
        reasons.add("SCAN_INPUT_TOO_LARGE")
    if any(finding.kind == "TOTAL_INPUT_BUDGET_EXCEEDED" for finding in unique):
        reasons.add("SCAN_TOTAL_INPUT_TOO_LARGE")
    if any(
        finding.kind == "TOTAL_PHYSICAL_READ_BUDGET_EXCEEDED"
        for finding in unique
    ):
        reasons.add("SCAN_TOTAL_PHYSICAL_READ_TOO_LARGE")
    if any(finding.kind == "SYMLINK_INPUT_DENIED" for finding in unique):
        reasons.add("SCAN_INPUT_SYMLINK_DENIED")
    if any(finding.kind == "INPUT_OUTSIDE_ROOT" for finding in unique):
        reasons.add("SCAN_INPUT_OUTSIDE_ROOT")
    if any(finding.kind == "INPUT_CHANGED_DURING_OPEN" for finding in unique):
        reasons.add("SCAN_INPUT_CHANGED_DURING_OPEN")
    if any(finding.kind == "INPUT_CHANGED_DURING_READ" for finding in unique):
        reasons.add("SCAN_INPUT_CHANGED_DURING_READ")
    if any(
        finding.kind == "INPUT_CONTENT_CHANGED_DURING_VERIFICATION"
        for finding in unique
    ):
        reasons.add("SCAN_INPUT_CONTENT_CHANGED_DURING_VERIFICATION")
    if any(
        finding.kind == "INPUT_DESCRIPTOR_SAFETY_UNAVAILABLE" for finding in unique
    ):
        reasons.add("SCAN_DESCRIPTOR_SAFETY_UNAVAILABLE")
    if any(finding.kind == "INPUT_NOT_REGULAR" for finding in unique):
        reasons.add("SCAN_INPUT_NOT_REGULAR")
    if truncated:
        reasons.add("SCAN_TRUNCATED")
    if any(not finding.candidate_seam for finding in acquisition_findings):
        reasons.add("ACQUISITION_OUTSIDE_CANDIDATE_SEAM")
    if acquisition_findings:
        reasons.add("RENDERER_ACQUISITION_PRESENT")

    if reasons.intersection(
        {
            "SCAN_DESCRIPTOR_SAFETY_UNAVAILABLE",
            "SCAN_INPUT_CHANGED_DURING_OPEN",
            "SCAN_INPUT_CHANGED_DURING_READ",
            "SCAN_INPUT_CONTENT_CHANGED_DURING_VERIFICATION",
            "SCAN_INPUT_NOT_REGULAR",
            "SCAN_INPUT_TOO_LARGE",
            "SCAN_INPUT_OUTSIDE_ROOT",
            "SCAN_INPUT_SYMLINK_DENIED",
            "SCAN_INPUT_UNREADABLE",
            "SCAN_TOTAL_INPUT_TOO_LARGE",
            "SCAN_TOTAL_PHYSICAL_READ_TOO_LARGE",
            "SCAN_TRUNCATED",
        }
    ):
        outcome = Outcome.ERROR
    elif "PARALLEL_MAPLIBRE_PACKAGE_HOMES" in reasons or "ACQUISITION_OUTSIDE_CANDIDATE_SEAM" in reasons:
        outcome = Outcome.FAIL
    elif reasons:
        outcome = Outcome.HOLD
    else:
        outcome = Outcome.PASS
    return Result(
        outcome,
        tuple(sorted(reasons)),
        unique,
        MAX_TOTAL_INPUT_BYTES,
        MAX_TOTAL_PHYSICAL_READ_BYTES,
        scanned_files,
        budget.scanned_bytes,
        budget.physical_read_bytes,
        truncated,
    )


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
