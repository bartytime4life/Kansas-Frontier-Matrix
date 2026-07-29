#!/usr/bin/env python3
"""Fail-closed classification of placeholder-only CI readiness lanes.

This checker is deliberately narrow.  It does not execute discovered Python,
import domain code, validate domain semantics, or grant release authority.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
import os
from pathlib import Path
import stat
from typing import Sequence, Union


MAX_REPORTED_FINDINGS = 50
MAX_RENDERED_FIELD = 240
MAX_LABEL_LENGTH = 120
PLACEHOLDER_DOCUMENT_NAMES = {".gitkeep", "LICENSE", "NOTICE", "README"}
PLACEHOLDER_DOCUMENT_SUFFIXES = {".md", ".markdown", ".rst", ".txt"}

PathInput = Union[str, os.PathLike[str]]


@dataclass(frozen=True)
class SourceClassification:
    """Classification of one Python source file."""

    placeholder: bool
    reason: str
    detail: str


@dataclass(frozen=True)
class ReadinessFinding:
    """One deterministic, repository-relative readiness finding."""

    category: str
    path: str
    reason: str
    detail: str


@dataclass(frozen=True)
class ReadinessReport:
    """Result of inspecting the requested test and validator roots."""

    label: str
    test_files: tuple[str, ...]
    validator_files: tuple[str, ...]
    findings: tuple[ReadinessFinding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings and bool(self.test_files) and bool(
            self.validator_files
        )


def _syntax_failure(error: SyntaxError) -> SourceClassification:
    line = error.lineno or 1
    column = error.offset or 1
    return SourceClassification(
        False,
        "syntax_error",
        f"Python syntax error at line {line}, column {column}",
    )


def _module_body_without_docstring(tree: ast.Module) -> list[ast.stmt]:
    body = list(tree.body)
    if body and isinstance(body[0], ast.Expr):
        value = body[0].value
        if isinstance(value, ast.Constant) and isinstance(value.value, str):
            body.pop(0)
    return body


def _has_empty_signature(function: ast.FunctionDef) -> bool:
    arguments = function.args
    return not any(
        (
            arguments.posonlyargs,
            arguments.args,
            arguments.kwonlyargs,
            arguments.defaults,
            [item for item in arguments.kw_defaults if item is not None],
            [arguments.vararg] if arguments.vararg else [],
            [arguments.kwarg] if arguments.kwarg else [],
            [function.returns] if function.returns else [],
            [function.type_comment] if function.type_comment else [],
            list(getattr(function, "type_params", ())),
        )
    )


def _is_exact_test_placeholder(function: ast.stmt) -> bool:
    if not isinstance(function, ast.FunctionDef):
        return False
    if function.name != "test_placeholder" or function.decorator_list:
        return False
    if not _has_empty_signature(function) or len(function.body) != 1:
        return False
    statement = function.body[0]
    return (
        isinstance(statement, ast.Assert)
        and isinstance(statement.test, ast.Constant)
        and statement.test.value is True
        and statement.msg is None
    )


def _is_not_implemented_raise(statement: ast.stmt) -> bool:
    if not isinstance(statement, ast.Raise) or statement.cause is not None:
        return False
    exception = statement.exc
    if isinstance(exception, ast.Name):
        return exception.id == "NotImplementedError"
    return (
        isinstance(exception, ast.Call)
        and isinstance(exception.func, ast.Name)
        and exception.func.id == "NotImplementedError"
        and not exception.keywords
        and len(exception.args) == 1
        and isinstance(exception.args[0], ast.Constant)
        and isinstance(exception.args[0].value, str)
    )


def _is_exact_validator_placeholder(function: ast.stmt) -> bool:
    return (
        isinstance(function, ast.FunctionDef)
        and function.name == "main"
        and not function.decorator_list
        and _has_empty_signature(function)
        and len(function.body) == 1
        and _is_not_implemented_raise(function.body[0])
    )


def classify_test_source(source: str) -> SourceClassification:
    """Recognize only comment/docstring-only modules or one exact test stub."""

    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        return _syntax_failure(error)
    body = _module_body_without_docstring(tree)
    if not body:
        return SourceClassification(True, "placeholder", "documentation-only module")
    if len(body) == 1 and _is_exact_test_placeholder(body[0]):
        return SourceClassification(True, "placeholder", "exact test placeholder")
    return SourceClassification(
        False,
        "substantive_test_module",
        "expected only a module docstring/comments or exact test_placeholder assert True",
    )


def classify_validator_source(source: str) -> SourceClassification:
    """Recognize only comment/docstring-only modules or one exact main stub."""

    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        return _syntax_failure(error)
    body = _module_body_without_docstring(tree)
    if not body:
        return SourceClassification(True, "placeholder", "documentation-only module")
    if len(body) == 1 and _is_exact_validator_placeholder(body[0]):
        return SourceClassification(True, "placeholder", "exact validator placeholder")
    return SourceClassification(
        False,
        "substantive_validator_module",
        "expected only a module docstring/comments or exact main NotImplementedError stub",
    )


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _display_path(path: Path, repository_root: Path) -> str:
    try:
        return path.relative_to(repository_root).as_posix() or "."
    except ValueError:
        return path.as_posix()


def _finding_key(finding: ReadinessFinding) -> tuple[int, str, str, str]:
    category_rank = {
        "repository": 0,
        "test_root": 1,
        "test": 2,
        "validator_root": 3,
        "validator": 4,
    }
    return (
        category_rank.get(finding.category, 99),
        finding.path,
        finding.reason,
        finding.detail,
    )


def _root_finding(
    category: str,
    path: Path,
    repository_root: Path,
    reason: str,
    detail: str,
) -> ReadinessFinding:
    return ReadinessFinding(
        category,
        _display_path(path, repository_root),
        reason,
        detail,
    )


def _symlink_component(path: Path, repository_root: Path) -> Path | None:
    """Return the first symlink between repository_root and path, if any."""

    try:
        relative = path.relative_to(repository_root)
    except ValueError:
        return None
    current = repository_root
    for part in relative.parts:
        current = current / part
        try:
            if current.is_symlink():
                return current
        except OSError:
            return current
    return None


def _walk_python_files(
    root: Path,
    *,
    repository_root: Path,
    category: str,
) -> tuple[list[Path], list[ReadinessFinding]]:
    files: list[Path] = []
    findings: list[ReadinessFinding] = []

    def visit(directory: Path) -> None:
        try:
            with os.scandir(directory) as iterator:
                entries = sorted(iterator, key=lambda item: item.name)
        except OSError as error:
            findings.append(
                _root_finding(
                    f"{category}_root",
                    directory,
                    repository_root,
                    "unreadable_directory",
                    error.__class__.__name__,
                )
            )
            return

        for entry in entries:
            entry_path = Path(entry.path)
            try:
                if entry.is_symlink():
                    findings.append(
                        _root_finding(
                            category,
                            entry_path,
                            repository_root,
                            "symlink_not_allowed",
                            "readiness roots must not contain symlinks",
                        )
                    )
                elif entry.is_dir(follow_symlinks=False):
                    visit(entry_path)
                elif entry.is_file(follow_symlinks=False):
                    if entry_path.suffix == ".py":
                        files.append(entry_path)
                    elif not (
                        entry_path.name in PLACEHOLDER_DOCUMENT_NAMES
                        or entry_path.suffix.lower() in PLACEHOLDER_DOCUMENT_SUFFIXES
                    ):
                        if not entry_path.suffix:
                            try:
                                if not entry_path.read_text(encoding="utf-8").strip():
                                    continue
                            except (OSError, UnicodeError):
                                pass
                        findings.append(
                            _root_finding(
                                category,
                                entry_path,
                                repository_root,
                                f"unexpected_{category}_source",
                                f"{category} roots allow only Python placeholders, documentation, .gitkeep, or empty extensionless files",
                            )
                        )
                else:
                    findings.append(
                        _root_finding(
                            category,
                            entry_path,
                            repository_root,
                            "unsupported_path_type",
                            "only regular files and directories are inspectable",
                        )
                    )
            except OSError as error:
                findings.append(
                    _root_finding(
                        category,
                        entry_path,
                        repository_root,
                        "unreadable_path",
                        error.__class__.__name__,
                    )
                )

    visit(root)
    return files, findings


def _inspect_roots(
    roots: Sequence[PathInput],
    *,
    repository_root: Path,
    repository_root_resolved: Path,
    category: str,
) -> tuple[set[str], list[ReadinessFinding]]:
    discovered: set[str] = set()
    inspected: set[Path] = set()
    findings: list[ReadinessFinding] = []
    classifier = (
        classify_test_source if category == "test" else classify_validator_source
    )

    for raw_root in sorted({os.fspath(root) for root in roots}):
        supplied = Path(raw_root)
        candidate = supplied if supplied.is_absolute() else repository_root / supplied
        candidate = Path(os.path.abspath(candidate))
        root_category = f"{category}_root"

        if not _is_relative_to(candidate, repository_root):
            findings.append(
                _root_finding(
                    root_category,
                    candidate,
                    repository_root,
                    "path_escape",
                    "root is outside the repository",
                )
            )
            continue
        try:
            metadata = candidate.lstat()
        except FileNotFoundError:
            findings.append(
                _root_finding(
                    root_category,
                    candidate,
                    repository_root,
                    "missing_root",
                    "required readiness root does not exist",
                )
            )
            continue
        except OSError as error:
            findings.append(
                _root_finding(
                    root_category,
                    candidate,
                    repository_root,
                    "unreadable_root",
                    error.__class__.__name__,
                )
            )
            continue

        if stat.S_ISLNK(metadata.st_mode):
            findings.append(
                _root_finding(
                    root_category,
                    candidate,
                    repository_root,
                    "symlink_not_allowed",
                    "readiness roots must not be symlinks",
                )
            )
            continue
        if not stat.S_ISDIR(metadata.st_mode):
            findings.append(
                _root_finding(
                    root_category,
                    candidate,
                    repository_root,
                    "root_not_directory",
                    "required readiness root is not a directory",
                )
            )
            continue

        symlink = _symlink_component(candidate, repository_root)
        if symlink is not None:
            findings.append(
                _root_finding(
                    root_category,
                    symlink,
                    repository_root,
                    "symlink_not_allowed",
                    "root traversal crosses a symlink",
                )
            )
            continue
        try:
            resolved = candidate.resolve(strict=True)
        except OSError as error:
            findings.append(
                _root_finding(
                    root_category,
                    candidate,
                    repository_root,
                    "unreadable_root",
                    error.__class__.__name__,
                )
            )
            continue
        if not _is_relative_to(resolved, repository_root_resolved):
            findings.append(
                _root_finding(
                    root_category,
                    candidate,
                    repository_root,
                    "path_escape",
                    "resolved root is outside the repository",
                )
            )
            continue
        if resolved in inspected:
            continue
        inspected.add(resolved)

        files, root_findings = _walk_python_files(
            resolved,
            repository_root=repository_root_resolved,
            category=category,
        )
        findings.extend(root_findings)
        for file_path in files:
            display = _display_path(file_path, repository_root_resolved)
            discovered.add(display)
            try:
                resolved_file = file_path.resolve(strict=True)
            except OSError as error:
                findings.append(
                    ReadinessFinding(
                        category,
                        display,
                        "unreadable_python",
                        error.__class__.__name__,
                    )
                )
                continue
            if not _is_relative_to(resolved_file, resolved) or not _is_relative_to(
                resolved_file, repository_root_resolved
            ):
                findings.append(
                    ReadinessFinding(
                        category,
                        display,
                        "path_escape",
                        "resolved Python file is outside its readiness root",
                    )
                )
                continue
            try:
                source = file_path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as error:
                findings.append(
                    ReadinessFinding(
                        category,
                        display,
                        "unreadable_python",
                        error.__class__.__name__,
                    )
                )
                continue
            classification = classifier(source)
            if not classification.placeholder:
                findings.append(
                    ReadinessFinding(
                        category,
                        display,
                        classification.reason,
                        classification.detail,
                    )
                )

    return discovered, findings


def inspect_readiness(
    *,
    label: str,
    test_roots: Sequence[PathInput],
    validator_roots: Sequence[PathInput],
    repository_root: PathInput | None = None,
) -> ReadinessReport:
    """Inspect roots without executing or importing their Python files."""

    repository = Path(repository_root) if repository_root is not None else Path.cwd()
    repository = Path(os.path.abspath(repository))
    findings: list[ReadinessFinding] = []
    try:
        metadata = repository.lstat()
        if not stat.S_ISDIR(metadata.st_mode):
            raise NotADirectoryError(repository)
        repository_resolved = repository.resolve(strict=True)
    except (OSError, ValueError) as error:
        return ReadinessReport(
            label,
            (),
            (),
            (
                ReadinessFinding(
                    "repository",
                    repository.as_posix(),
                    "invalid_repository_root",
                    error.__class__.__name__,
                ),
            ),
        )

    if not test_roots:
        findings.append(
            ReadinessFinding(
                "test_root",
                "<none>",
                "missing_root_argument",
                "at least one test root is required",
            )
        )
    if not validator_roots:
        findings.append(
            ReadinessFinding(
                "validator_root",
                "<none>",
                "missing_root_argument",
                "at least one validator root is required",
            )
        )
    test_files, test_findings = _inspect_roots(
        test_roots,
        repository_root=repository,
        repository_root_resolved=repository_resolved,
        category="test",
    )
    validator_files, validator_findings = _inspect_roots(
        validator_roots,
        repository_root=repository,
        repository_root_resolved=repository_resolved,
        category="validator",
    )
    findings.extend(test_findings)
    findings.extend(validator_findings)
    if test_roots and not test_files and not test_findings:
        findings.append(
            ReadinessFinding(
                "test_root",
                "<test-root-set>",
                "no_python_files",
                "test roots contain no Python files",
            )
        )
    if validator_roots and not validator_files and not validator_findings:
        findings.append(
            ReadinessFinding(
                "validator_root",
                "<validator-root-set>",
                "no_python_files",
                "validator roots contain no Python files",
            )
        )
    ordered_findings = tuple(sorted(set(findings), key=_finding_key))
    return ReadinessReport(
        label,
        tuple(sorted(test_files)),
        tuple(sorted(validator_files)),
        ordered_findings,
    )


def _bounded_field(value: str, limit: int = MAX_RENDERED_FIELD) -> str:
    normalized = " ".join(value.split())
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 3] + "..."


def render_report(report: ReadinessReport) -> tuple[str, ...]:
    """Render bounded, deterministic, line-oriented CLI output."""

    label = _bounded_field(report.label, MAX_LABEL_LENGTH)
    if report.ok:
        return (
            f"WORKFLOW_SKIPPED_EXPLICIT: {label}",
            "WORKFLOW_HOLD: "
            f"{label} readiness is placeholder-only; "
            f"tests={len(report.test_files)}; validators={len(report.validator_files)}",
        )

    lines = [f"CI_READINESS_FAIL: {label}; findings={len(report.findings)}"]
    for finding in report.findings[:MAX_REPORTED_FINDINGS]:
        lines.append(
            "CI_READINESS_REASON: "
            f"{_bounded_field(finding.reason)}: "
            f"{_bounded_field(finding.path)}: "
            f"{_bounded_field(finding.detail)}"
        )
    omitted = len(report.findings) - MAX_REPORTED_FINDINGS
    if omitted > 0:
        lines.append(f"CI_READINESS_OMITTED: {omitted}")
    lines.append(
        "WORKFLOW_HOLD: "
        f"{label} readiness check failed; tests={len(report.test_files)}; "
        f"validators={len(report.validator_files)}"
    )
    return tuple(lines)


def _label_argument(value: str) -> str:
    if not value.strip():
        raise argparse.ArgumentTypeError("label must not be empty")
    if len(value) > MAX_LABEL_LENGTH:
        raise argparse.ArgumentTypeError(
            f"label must be at most {MAX_LABEL_LENGTH} characters"
        )
    if any(ord(character) < 32 or ord(character) == 127 for character in value):
        raise argparse.ArgumentTypeError("label must not contain control characters")
    return value.strip()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Classify test and validator roots as placeholder-only or substantive."
    )
    parser.add_argument("--label", required=True, type=_label_argument)
    parser.add_argument("--test-root", action="append", required=True)
    parser.add_argument("--validator-root", action="append", required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    arguments = build_parser().parse_args(argv)
    report = inspect_readiness(
        label=arguments.label,
        test_roots=arguments.test_root,
        validator_roots=arguments.validator_root,
    )
    for line in render_report(report):
        print(line)
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
