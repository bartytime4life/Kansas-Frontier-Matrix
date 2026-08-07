"""Closed model, identity, signal, and validation rules for ImplementationChangeContext."""
from __future__ import annotations

import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))
from hashing import compute_spec_hash  # noqa: E402

SCHEMA = REPO_ROOT / "schemas/contracts/v1/governance/implementation_change_context.schema.json"
CASES = REPO_ROOT / "fixtures/contracts/v1/governance/implementation_change_context/cases.json"
MAX_BYTES = 4 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
MAX_FILES = 1_000
EXIT_READY = 0
EXIT_ERROR = 2
EXIT_HOLD = 3
EXIT = {"READY": EXIT_READY, "ERROR": EXIT_ERROR, "HOLD": EXIT_HOLD}
SCHEMA_PATH = SCHEMA
FIXTURE_PATH = CASES

SIGNAL_CODES = (
    "AUTHORITY_SURFACE",
    "BINARY_CONTENT",
    "CROSS_ROOT",
    "DELETION_OR_RENAME",
    "DEPENDENCY_SURFACE",
    "DOCUMENTATION_ONLY",
    "LARGE_CHANGE",
    "PUBLIC_SURFACE",
    "SENSITIVE_PATH_NAME",
    "TEST_OR_FIXTURE_ONLY",
    "WORKFLOW_SURFACE",
)
SIGNAL_WEIGHTS = {
    "AUTHORITY_SURFACE": 2,
    "BINARY_CONTENT": 1,
    "CROSS_ROOT": 1,
    "DELETION_OR_RENAME": 2,
    "DEPENDENCY_SURFACE": 2,
    "DOCUMENTATION_ONLY": 0,
    "LARGE_CHANGE": 1,
    "PUBLIC_SURFACE": 2,
    "SENSITIVE_PATH_NAME": 3,
    "TEST_OR_FIXTURE_ONLY": 0,
    "WORKFLOW_SURFACE": 2,
}
STATUS_MAP = {
    "A": "ADDED",
    "M": "MODIFIED",
    "D": "DELETED",
    "R": "RENAMED",
    "C": "COPIED",
    "T": "TYPE_CHANGED",
}
DOCUMENT_SUFFIXES = frozenset({".md", ".mdx", ".rst", ".adoc", ".txt"})
DEPENDENCY_BASENAMES = frozenset(
    {
        "Cargo.lock",
        "Cargo.toml",
        "Gemfile",
        "Gemfile.lock",
        "Pipfile",
        "Pipfile.lock",
        "go.mod",
        "go.sum",
        "package-lock.json",
        "package.json",
        "pnpm-lock.yaml",
        "poetry.lock",
        "pyproject.toml",
        "uv.lock",
        "yarn.lock",
    }
)
AUTHORITY_PREFIXES = (
    "contracts/",
    "control_plane/",
    "data/proofs/",
    "data/published/",
    "data/receipts/",
    "data/registry/",
    "docs/adr/",
    "docs/doctrine/",
    "policy/",
    "release/",
    "schemas/",
)
PUBLIC_PREFIXES = (
    "apps/",
    "packages/api/",
    "packages/maplibre/",
    "runtime/",
    "ui/",
    "web/",
)
SENSITIVE_COMPONENTS = frozenset({"credentials", "private_keys", "secrets"})


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class Evaluation:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


class GitContextError(ValueError):
    pass


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in items:
        if key in out:
            raise DuplicateKeyError(key)
        out[key] = value
    return out


def _constant(_: str) -> object:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json(path: Path) -> dict[str, object]:
    if path.is_symlink() or not path.is_file():
        raise ValueError("input must be a regular non-symlink file")
    if path.stat().st_size > MAX_BYTES:
        raise ValueError("input exceeds 4 MiB")
    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_pairs,
        parse_constant=_constant,
        parse_float=_float,
    )
    if not isinstance(value, dict):
        raise ValueError("JSON root must be an object")
    return value


def _validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _pointer(parts: Iterable[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _schema_findings(document: Mapping[str, object]) -> list[Finding]:
    errors = list(islice(_validator().iter_errors(document), MAX_SCHEMA_FINDINGS + 1))
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "$"))
    return findings


def _sorted_unique(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(value)
        and len(value) == len(set(value))
    )


def _canonical_path(value: object) -> bool:
    if not isinstance(value, str) or not value or value.startswith("/") or "\\" in value:
        return False
    if any(ord(char) < 32 or ord(char) == 127 for char in value):
        return False
    path = PurePosixPath(value)
    return (
        str(path) == value
        and all(part not in {"", ".", ".."} for part in path.parts)
        and path.parts[0] != ".git"
    )


def _file_sort_key(item: Mapping[str, object]) -> tuple[str, str, str]:
    return (
        str(item.get("path", "")),
        str(item.get("status", "")),
        str(item.get("previous_path") or ""),
    )


def _roots(files: Sequence[Mapping[str, object]]) -> list[str]:
    return sorted({PurePosixPath(str(item["path"])).parts[0] for item in files})


def _is_dependency_path(path: str) -> bool:
    name = PurePosixPath(path).name
    return (
        name in DEPENDENCY_BASENAMES
        or (name.startswith("requirements") and name.endswith(".txt"))
        or name.endswith(".lock")
    )


def _is_sensitive_path(path: str) -> bool:
    parts = [part.lower() for part in PurePosixPath(path).parts]
    name = parts[-1]
    if name == ".env" or (name.startswith(".env.") and name != ".env.example"):
        return True
    return any(part in SENSITIVE_COMPONENTS for part in parts)


def signal_codes(files: Sequence[Mapping[str, object]]) -> list[str]:
    signals: set[str] = set()
    paths = [str(item["path"]) for item in files]
    roots = _roots(files)
    changed_lines = sum(
        int(item.get("additions") or 0) + int(item.get("deletions") or 0)
        for item in files
    )
    if len(roots) > 1:
        signals.add("CROSS_ROOT")
    if len(files) >= 20 or changed_lines >= 500:
        signals.add("LARGE_CHANGE")
    if any(bool(item.get("binary")) for item in files):
        signals.add("BINARY_CONTENT")
    if any(item.get("status") in {"DELETED", "RENAMED"} for item in files):
        signals.add("DELETION_OR_RENAME")
    if any(_is_dependency_path(path) for path in paths):
        signals.add("DEPENDENCY_SURFACE")
    if any(path.startswith(".github/workflows/") for path in paths):
        signals.add("WORKFLOW_SURFACE")
    if any(path.startswith(AUTHORITY_PREFIXES) for path in paths):
        signals.add("AUTHORITY_SURFACE")
    if any(path.startswith(PUBLIC_PREFIXES) for path in paths):
        signals.add("PUBLIC_SURFACE")
    if any(_is_sensitive_path(path) for path in paths):
        signals.add("SENSITIVE_PATH_NAME")
    if all(PurePosixPath(path).suffix.lower() in DOCUMENT_SUFFIXES for path in paths):
        signals.add("DOCUMENTATION_ONLY")
    if set(roots).issubset({"fixtures", "tests"}):
        signals.add("TEST_OR_FIXTURE_ONLY")
    return sorted(signals)


def signal_score(signals: Sequence[str]) -> int:
    return sum(SIGNAL_WEIGHTS[item] for item in signals)


def expected_summary(files: Sequence[Mapping[str, object]]) -> dict[str, object]:
    signals = signal_codes(files)
    score = signal_score(signals)
    return {
        "file_count": len(files),
        "additions": sum(int(item.get("additions") or 0) for item in files),
        "deletions": sum(int(item.get("deletions") or 0) for item in files),
        "binary_file_count": sum(1 for item in files if item.get("binary") is True),
        "top_level_roots": _roots(files),
        "signal_codes": signals,
        "signal_score": score,
        "decision_capture_recommended": score >= 2,
    }


def identity_projection(document: Mapping[str, object]) -> dict[str, object]:
    return {
        "profile": document.get("profile"),
        "repository": document.get("repository"),
        "base_sha": document.get("base_sha"),
        "head_sha": document.get("head_sha"),
        "files": copy.deepcopy(document.get("files")),
    }


def expected_context_id(document: Mapping[str, object]) -> str:
    digest = compute_spec_hash(identity_projection(document)).split(":", 1)[1]
    return f"kfm:implementation-change-context:{digest}"


def _semantic_errors(document: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    files = document.get("files")
    summary = document.get("summary")
    refs = document.get("implementation_decision_refs")
    if document.get("base_sha") == document.get("head_sha"):
        findings.append(Finding("EMPTY_COMMIT_RANGE", "$.head_sha"))
    if not isinstance(files, list):
        return findings

    if len(files) > MAX_FILES:
        findings.append(Finding("FILE_LIMIT_EXCEEDED", "$.files"))
    if files != sorted(files, key=lambda item: _file_sort_key(item) if isinstance(item, dict) else ("", "", "")):
        findings.append(Finding("CANONICAL_FILE_ORDER_REQUIRED", "$.files"))

    destinations: set[str] = set()
    for index, item in enumerate(files):
        if not isinstance(item, dict):
            continue
        path = item.get("path")
        previous = item.get("previous_path")
        status = item.get("status")
        if not _canonical_path(path):
            findings.append(Finding("REPOSITORY_PATH_UNSAFE", f"$.files[{index}].path"))
        elif path in destinations:
            findings.append(Finding("DUPLICATE_DESTINATION_PATH", f"$.files[{index}].path"))
        else:
            destinations.add(path)
        if previous is not None and not _canonical_path(previous):
            findings.append(Finding("REPOSITORY_PATH_UNSAFE", f"$.files[{index}].previous_path"))
        if status in {"RENAMED", "COPIED"}:
            if previous is None:
                findings.append(Finding("PREVIOUS_PATH_REQUIRED", f"$.files[{index}].previous_path"))
            elif previous == path:
                findings.append(Finding("PREVIOUS_PATH_EQUALS_DESTINATION", f"$.files[{index}].previous_path"))
        elif previous is not None:
            findings.append(Finding("PREVIOUS_PATH_NOT_ALLOWED", f"$.files[{index}].previous_path"))
        if item.get("binary") is True:
            if item.get("additions") is not None or item.get("deletions") is not None:
                findings.append(Finding("BINARY_METRICS_MUST_BE_NULL", f"$.files[{index}]"))
        elif not isinstance(item.get("additions"), int) or not isinstance(item.get("deletions"), int):
            findings.append(Finding("TEXT_METRICS_REQUIRED", f"$.files[{index}]"))

    if not _sorted_unique(refs):
        findings.append(Finding("CANONICAL_ORDER_REQUIRED", "$.implementation_decision_refs"))
    if isinstance(summary, dict):
        expected = expected_summary([item for item in files if isinstance(item, dict)])
        for key, value in expected.items():
            if summary.get(key) != value:
                findings.append(Finding("SUMMARY_MISMATCH", f"$.summary.{key}"))
    if document.get("context_id") != expected_context_id(document):
        findings.append(Finding("CONTEXT_ID_MISMATCH", "$.context_id"))
    return findings


def _hold_findings(document: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    if document.get("status") == "DRAFT":
        findings.append(Finding("CONTEXT_DRAFT", "$.status"))
    summary = document.get("summary")
    refs = document.get("implementation_decision_refs")
    if (
        document.get("status") == "READY_FOR_REVIEW"
        and isinstance(summary, dict)
        and summary.get("decision_capture_recommended") is True
        and not refs
    ):
        findings.append(
            Finding(
                "IMPLEMENTATION_DECISION_REFERENCE_RECOMMENDED",
                "$.implementation_decision_refs",
            )
        )
    return findings


def evaluate_document(document: Mapping[str, object]) -> Evaluation:
    schema_errors = tuple(sorted(set(_schema_findings(document))))
    if schema_errors:
        return Evaluation("ERROR", schema_errors)
    errors = tuple(sorted(set(_semantic_errors(document))))
    if errors:
        return Evaluation("ERROR", errors)
    holds = tuple(sorted(set(_hold_findings(document))))
    return Evaluation("HOLD" if holds else "READY", holds)


def evaluate_path(path: Path) -> tuple[dict[str, object] | None, Evaluation]:
    try:
        document = load_json(path)
        return document, evaluate_document(document)
    except (json.JSONDecodeError, DuplicateKeyError, NonFiniteNumberError):
        return None, Evaluation("ERROR", (Finding("INPUT_JSON_INVALID", "$"),))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return None, Evaluation("ERROR", (Finding("INPUT_INVALID", "$"),))
