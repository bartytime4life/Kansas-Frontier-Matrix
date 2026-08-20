#!/usr/bin/env python3
"""Fail-fast source-boundary checks for the repository CodeQL matrix.

The helper is intentionally small, standard-library-only, read-only, and no-network.
It verifies that each configured CodeQL matrix cell maps to checked-out, tracked
source before CodeQL initialization. Unsupported language/build-mode combinations
fail closed so a future compiled-language lane must add an explicit, reviewed policy
rather than silently relying on automatic detection.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

TROUBLESHOOTING_URL = (
    "https://docs.github.com/en/code-security/reference/code-scanning/"
    "troubleshoot-analysis-errors/no-source-code-seen-during-build"
)

EXIT_NO_SOURCE = 1
EXIT_CONFIGURATION = 2

IGNORED_DIRECTORY_NAMES = frozenset(
    {
        ".git",
        ".mypy_cache",
        ".pytest_cache",
        ".tox",
        ".venv",
        "__pycache__",
        "build",
        "coverage",
        "dist",
        "node_modules",
        "venv",
        "vendor",
    }
)


@dataclass(frozen=True)
class LanguagePolicy:
    """Repository-admitted source selectors for one CodeQL language."""

    build_modes: frozenset[str]
    suffixes: frozenset[str]
    required_prefix: tuple[str, ...] = ()


@dataclass(frozen=True)
class BoundaryReport:
    """Deterministic result for one matrix cell."""

    language: str
    build_mode: str
    source_count: int
    workflow: str


class BoundaryFailure(RuntimeError):
    """A finite, user-actionable source-boundary failure."""

    def __init__(
        self,
        *,
        reason: str,
        message: str,
        exit_code: int,
        language: str | None = None,
        build_mode: str | None = None,
    ) -> None:
        super().__init__(message)
        self.reason = reason
        self.message = message
        self.exit_code = exit_code
        self.language = language
        self.build_mode = build_mode

    def as_record(self) -> dict[str, object]:
        return {
            "build_mode": self.build_mode,
            "docs": TROUBLESHOOTING_URL,
            "language": self.language,
            "message": self.message,
            "outcome": "FAIL",
            "reason": self.reason,
        }


LANGUAGE_POLICIES: dict[str, LanguagePolicy] = {
    "actions": LanguagePolicy(
        build_modes=frozenset({"none"}),
        suffixes=frozenset({".yaml", ".yml"}),
        required_prefix=(".github", "workflows"),
    ),
    "javascript-typescript": LanguagePolicy(
        build_modes=frozenset({"none"}),
        suffixes=frozenset({".cjs", ".js", ".jsx", ".mjs", ".ts", ".tsx"}),
    ),
    "python": LanguagePolicy(
        build_modes=frozenset({"none"}),
        suffixes=frozenset({".py", ".pyw"}),
    ),
}

EXPECTED_MATRIX = frozenset(
    {
        ("actions", "none"),
        ("javascript-typescript", "none"),
        ("python", "none"),
    }
)

_MATRIX_LANGUAGE_RE = re.compile(
    r"^\s*-\s+language:\s*([A-Za-z0-9_-]+)\s*(?:#.*)?$"
)
_MATRIX_BUILD_MODE_RE = re.compile(
    r"^\s*build-mode:\s*([A-Za-z0-9_-]+)\s*(?:#.*)?$"
)
_STEP_NAME_RE_TEMPLATE = r"^\s*-\s+name:\s*{name}\s*$"


def _normalized_relative_path(raw_path: str | Path) -> Path:
    path = Path(str(raw_path).replace("\\", "/"))
    if path.is_absolute() or ".." in path.parts:
        raise BoundaryFailure(
            reason="INVALID_TRACKED_PATH",
            message=f"Tracked path is not repository-relative: {raw_path!r}.",
            exit_code=EXIT_CONFIGURATION,
        )
    return path


def _is_ignored(path: Path) -> bool:
    return any(part in IGNORED_DIRECTORY_NAMES for part in path.parts)


def path_matches_policy(path: str | Path, policy: LanguagePolicy) -> bool:
    """Return whether a repository-relative path is analyzable for a policy."""

    normalized = _normalized_relative_path(path)
    if _is_ignored(normalized):
        return False
    if policy.required_prefix:
        prefix_length = len(policy.required_prefix)
        if normalized.parts[:prefix_length] != policy.required_prefix:
            return False
    return normalized.suffix.lower() in policy.suffixes


def evaluate_paths(
    paths: Iterable[str | Path],
    *,
    language: str,
    build_mode: str,
    workflow: str,
) -> BoundaryReport:
    """Evaluate one matrix cell over a known set of checked-out tracked paths."""

    policy = LANGUAGE_POLICIES.get(language)
    if policy is None:
        raise BoundaryFailure(
            reason="LANGUAGE_POLICY_MISSING",
            message=(
                f"CodeQL language {language!r} has no repository source policy. "
                "Add explicit source selectors and reviewed build handling before "
                "expanding the matrix."
            ),
            exit_code=EXIT_CONFIGURATION,
            language=language,
            build_mode=build_mode,
        )

    if build_mode not in policy.build_modes:
        raise BoundaryFailure(
            reason="BUILD_MODE_NOT_ADMITTED",
            message=(
                f"Build mode {build_mode!r} is not admitted for CodeQL language "
                f"{language!r}; admitted modes: {sorted(policy.build_modes)}."
            ),
            exit_code=EXIT_CONFIGURATION,
            language=language,
            build_mode=build_mode,
        )

    matched = sorted(
        {
            _normalized_relative_path(path).as_posix()
            for path in paths
            if path_matches_policy(path, policy)
        }
    )
    if not matched:
        raise BoundaryFailure(
            reason="NO_TRACKED_SOURCE",
            message=(
                f"No checked-out tracked source matches CodeQL language {language!r}. "
                "Remove the matrix cell or restore analyzable source before analysis."
            ),
            exit_code=EXIT_NO_SOURCE,
            language=language,
            build_mode=build_mode,
        )

    return BoundaryReport(
        language=language,
        build_mode=build_mode,
        source_count=len(matched),
        workflow=workflow,
    )


def tracked_checked_out_files(repo_root: Path) -> tuple[str, ...]:
    """Return checked-out files known to Git, sorted by repository-relative path."""

    try:
        completed = subprocess.run(
            ("git", "-C", str(repo_root), "ls-files", "-z", "--cached"),
            check=True,
            capture_output=True,
            shell=False,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise BoundaryFailure(
            reason="TRACKED_FILE_INVENTORY_ERROR",
            message=f"Unable to enumerate tracked files with git ls-files: {exc}.",
            exit_code=EXIT_CONFIGURATION,
        ) from exc

    decoded = completed.stdout.decode("utf-8", errors="surrogateescape")
    candidates = sorted(filter(None, decoded.split("\0")))
    checked_out: list[str] = []
    for candidate in candidates:
        normalized = _normalized_relative_path(candidate)
        candidate_path = repo_root.joinpath(*normalized.parts)
        if candidate_path.is_file():
            checked_out.append(normalized.as_posix())
    return tuple(checked_out)


def extract_matrix_entries(workflow_text: str) -> tuple[tuple[str, str], ...]:
    """Extract the intentionally simple language/build-mode include matrix."""

    entries: list[tuple[str, str]] = []
    pending_language: str | None = None
    for line in workflow_text.splitlines():
        language_match = _MATRIX_LANGUAGE_RE.match(line)
        if language_match:
            if pending_language is not None:
                raise BoundaryFailure(
                    reason="MATRIX_ENTRY_INCOMPLETE",
                    message=(
                        f"CodeQL matrix language {pending_language!r} has no adjacent "
                        "build-mode entry."
                    ),
                    exit_code=EXIT_CONFIGURATION,
                )
            pending_language = language_match.group(1)
            continue

        if pending_language is not None:
            build_match = _MATRIX_BUILD_MODE_RE.match(line)
            if build_match:
                entries.append((pending_language, build_match.group(1)))
                pending_language = None
                continue
            if line.strip() and not line.lstrip().startswith("#"):
                raise BoundaryFailure(
                    reason="MATRIX_ENTRY_INCOMPLETE",
                    message=(
                        f"CodeQL matrix language {pending_language!r} must be followed "
                        "by its build-mode entry."
                    ),
                    exit_code=EXIT_CONFIGURATION,
                )

    if pending_language is not None:
        raise BoundaryFailure(
            reason="MATRIX_ENTRY_INCOMPLETE",
            message=(
                f"CodeQL matrix language {pending_language!r} has no build-mode entry."
            ),
            exit_code=EXIT_CONFIGURATION,
        )
    if not entries:
        raise BoundaryFailure(
            reason="MATRIX_NOT_FOUND",
            message="No explicit CodeQL language/build-mode matrix entries were found.",
            exit_code=EXIT_CONFIGURATION,
        )
    if len(set(entries)) != len(entries):
        raise BoundaryFailure(
            reason="DUPLICATE_MATRIX_ENTRY",
            message="Duplicate CodeQL language/build-mode matrix entries were found.",
            exit_code=EXIT_CONFIGURATION,
        )
    return tuple(entries)


def _step_index(lines: Sequence[str], name: str) -> int:
    pattern = re.compile(_STEP_NAME_RE_TEMPLATE.format(name=re.escape(name)))
    matches = [index for index, line in enumerate(lines) if pattern.match(line)]
    if len(matches) != 1:
        raise BoundaryFailure(
            reason="WORKFLOW_STEP_CONTRACT_ERROR",
            message=f"Expected exactly one workflow step named {name!r}.",
            exit_code=EXIT_CONFIGURATION,
        )
    return matches[0]


def validate_workflow_contract(
    workflow_text: str,
    *,
    language: str,
    build_mode: str,
) -> tuple[tuple[str, str], ...]:
    """Validate the matrix and preflight placement in the CodeQL workflow."""

    entries = extract_matrix_entries(workflow_text)
    entry = (language, build_mode)
    if entry not in entries:
        raise BoundaryFailure(
            reason="MATRIX_INVOCATION_MISMATCH",
            message=f"Requested matrix cell {entry!r} is not declared in the workflow.",
            exit_code=EXIT_CONFIGURATION,
            language=language,
            build_mode=build_mode,
        )

    lines = workflow_text.splitlines()
    checkout_index = _step_index(lines, "Check out analyzed revision")
    test_index = _step_index(lines, "Test CodeQL source boundary helper")
    boundary_index = _step_index(lines, "Validate CodeQL source boundary")
    init_index = _step_index(lines, "Initialize CodeQL")
    analyze_index = _step_index(lines, "Analyze source")

    if not (
        checkout_index
        < test_index
        < boundary_index
        < init_index
        < analyze_index
    ):
        raise BoundaryFailure(
            reason="WORKFLOW_STEP_ORDER_ERROR",
            message=(
                "CodeQL source-boundary checks must run after checkout and before "
                "CodeQL initialization; analysis must remain after initialization."
            ),
            exit_code=EXIT_CONFIGURATION,
            language=language,
            build_mode=build_mode,
        )

    boundary_block = "\n".join(lines[boundary_index:init_index])
    required_fragments = (
        "tools/ci/validate_codeql_source_boundary.py",
        "${{ matrix.language }}",
        "${{ matrix.build-mode }}",
    )
    missing = [
        fragment for fragment in required_fragments if fragment not in boundary_block
    ]
    if missing:
        raise BoundaryFailure(
            reason="WORKFLOW_INVOCATION_CONTRACT_ERROR",
            message=(
                "The CodeQL boundary step is missing required matrix-bound invocation "
                f"fragments: {missing}."
            ),
            exit_code=EXIT_CONFIGURATION,
            language=language,
            build_mode=build_mode,
        )

    return entries


def _resolve_workflow(repo_root: Path, workflow_arg: str) -> tuple[Path, str]:
    relative = _normalized_relative_path(workflow_arg)
    workflow_path = repo_root.joinpath(*relative.parts)
    if not workflow_path.is_file():
        raise BoundaryFailure(
            reason="WORKFLOW_NOT_FOUND",
            message=f"CodeQL workflow does not exist: {relative.as_posix()}.",
            exit_code=EXIT_CONFIGURATION,
        )
    return workflow_path, relative.as_posix()


def _append_summary(report: BoundaryReport) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    with Path(summary_path).open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(
            "\n".join(
                (
                    f"### CodeQL source boundary — `{report.language}`",
                    "",
                    f"- Build mode: `{report.build_mode}`",
                    f"- Checked-out tracked source files: `{report.source_count}`",
                    f"- Workflow: `{report.workflow}`",
                    f"- Troubleshooting reference: {TROUBLESHOOTING_URL}",
                    "",
                )
            )
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Fail before CodeQL initialization when a configured matrix cell has "
            "no checked-out tracked source or lacks an explicit repository policy."
        )
    )
    parser.add_argument("--repo-root", default=".", help="Repository checkout root.")
    parser.add_argument(
        "--workflow",
        default=".github/workflows/codeql.yml",
        help="Repository-relative CodeQL workflow path.",
    )
    parser.add_argument("--language", required=True, help="CodeQL matrix language.")
    parser.add_argument("--build-mode", required=True, help="CodeQL matrix build mode.")
    return parser


def run(args: argparse.Namespace) -> BoundaryReport:
    repo_root = Path(args.repo_root).resolve()
    if not repo_root.is_dir():
        raise BoundaryFailure(
            reason="REPOSITORY_ROOT_NOT_FOUND",
            message=f"Repository root does not exist: {repo_root}.",
            exit_code=EXIT_CONFIGURATION,
            language=args.language,
            build_mode=args.build_mode,
        )

    workflow_path, workflow_relative = _resolve_workflow(repo_root, args.workflow)
    workflow_text = workflow_path.read_text(encoding="utf-8")
    validate_workflow_contract(
        workflow_text,
        language=args.language,
        build_mode=args.build_mode,
    )

    tracked = tracked_checked_out_files(repo_root)
    if workflow_relative not in tracked:
        raise BoundaryFailure(
            reason="WORKFLOW_NOT_TRACKED",
            message=f"CodeQL workflow is not tracked by Git: {workflow_relative}.",
            exit_code=EXIT_CONFIGURATION,
            language=args.language,
            build_mode=args.build_mode,
        )

    report = evaluate_paths(
        tracked,
        language=args.language,
        build_mode=args.build_mode,
        workflow=workflow_relative,
    )
    _append_summary(report)
    return report


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        report = run(args)
    except BoundaryFailure as failure:
        print(json.dumps(failure.as_record(), sort_keys=True), file=sys.stderr)
        return failure.exit_code

    print(
        json.dumps(
            {
                "build_mode": report.build_mode,
                "docs": TROUBLESHOOTING_URL,
                "language": report.language,
                "outcome": "PASS",
                "source_count": report.source_count,
                "workflow": report.workflow,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
