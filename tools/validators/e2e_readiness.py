#!/usr/bin/env python3
"""Check the explicit composed-E2E hold after the legacy UI retirement."""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

RETIRED_APPS = (
    "apps/explorer-web",
    "apps/kansas-frontier-matrix-explorer",
)
EXPECTED_E2E_FILES = frozenset(
    {
        "README.md",
        "__init__.py",
        "agriculture/.gitkeep",
        "agriculture/README.md",
        "test_hydrology_proof_slice.py",
    }
)
PROOF_SLICE_TEST = "test_hydrology_proof_slice.py"
PROOF_SLICE_LANE_MARKERS = ("tools/readiness/run_lane.py", "proof-slice")
SUBPROCESS_LAUNCHERS = frozenset({"call", "check_call", "check_output", "Popen", "run"})
NESTED_SCOPES = (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)


@dataclass(frozen=True)
class ReadinessReport:
    findings: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _is_vacuous_test(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    body = [
        stmt
        for stmt in node.body
        if not (isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant))
    ]
    return all(
        isinstance(stmt, ast.Pass)
        or (isinstance(stmt, ast.Assert) and isinstance(stmt.test, ast.Constant))
        for stmt in body
    )


def _proof_slice_test_findings(path: Path) -> list[str]:
    """The Hydrology proof-slice E2E must run the accepted lane, not a placeholder."""

    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (OSError, SyntaxError, UnicodeError):
        return ["E2E_PROOF_SLICE_TEST_INVALID"]
    tests = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test")
    ]
    if not tests or any(_is_vacuous_test(node) for node in tests):
        return ["E2E_PROOF_SLICE_TEST_VACUOUS"]
    if not any(_invokes_proof_slice_lane(node) for node in tests):
        return ["E2E_PROOF_SLICE_LANE_NOT_INVOKED"]
    return []


def _invokes_proof_slice_lane(test: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    """True when the test starts the lane as a subprocess.

    The call must be ``subprocess.<launcher>(...)`` whose command list or tuple
    names ``tools/readiness/run_lane.py`` immediately followed by
    ``proof-slice``. Comments, docstrings, other calls that merely carry those
    strings, and calls inside nested functions or lambdas (which may never
    run) do not count.
    """

    for node in _walk_executed_scope(test):
        if not isinstance(node, ast.Call) or not _is_subprocess_launcher(node.func):
            continue
        command = node.args[0] if node.args else next(
            (keyword.value for keyword in node.keywords if keyword.arg == "args"), None
        )
        if not isinstance(command, (ast.List, ast.Tuple)):
            continue
        elements = [
            element.value if isinstance(element, ast.Constant) else None
            for element in command.elts
        ]
        pairs = zip(elements, elements[1:])
        if PROOF_SLICE_LANE_MARKERS in pairs:
            return True
    return False


def _walk_executed_scope(test: ast.FunctionDef | ast.AsyncFunctionDef):
    """Yield nodes in the test body without entering nested function scopes."""

    pending: list[ast.AST] = [node for node in test.body if not isinstance(node, NESTED_SCOPES)]
    while pending:
        node = pending.pop()
        yield node
        for child in ast.iter_child_nodes(node):
            if not isinstance(child, NESTED_SCOPES):
                pending.append(child)


def _is_subprocess_launcher(func: ast.expr) -> bool:
    return (
        isinstance(func, ast.Attribute)
        and func.attr in SUBPROCESS_LAUNCHERS
        and isinstance(func.value, ast.Name)
        and func.value.id == "subprocess"
    )


def inspect_readiness(repository_root: Path) -> ReadinessReport:
    root = repository_root.resolve()
    findings: list[str] = []
    if not root.is_dir():
        return ReadinessReport(("REPOSITORY_ROOT_INVALID",))

    for relative in RETIRED_APPS:
        if (root / relative).exists():
            findings.append(f"RETIRED_APP_RESURFACED:{relative}")

    for relative in ("package.json", "Makefile", "apps/governed-api/README.md"):
        if not (root / relative).is_file():
            findings.append(f"REQUIRED_BOUNDARY_MISSING:{relative}")

    e2e_root = root / "tests/e2e"
    if not e2e_root.is_dir():
        findings.append("E2E_ROOT_MISSING")
    else:
        observed = {
            path.relative_to(e2e_root).as_posix()
            for path in e2e_root.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        for relative in sorted(EXPECTED_E2E_FILES - observed):
            findings.append(f"E2E_BOUNDARY_MISSING:{relative}")
        for relative in sorted(observed - EXPECTED_E2E_FILES):
            findings.append(f"E2E_IMPLEMENTATION_SURFACED:{relative}")
        proof_slice_test = e2e_root / PROOF_SLICE_TEST
        if proof_slice_test.is_file():
            findings.extend(_proof_slice_test_findings(proof_slice_test))

    return ReadinessReport(tuple(sorted(set(findings))))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args(argv)
    report = inspect_readiness(Path(args.repo_root))
    if report.ok:
        print("E2E_READINESS_CONFIRMED legacy_apps=retired e2e_suite=not-established")
        print("WORKFLOW_SKIPPED_EXPLICIT: run-e2e-smoke")
        print("WORKFLOW_HOLD: no accepted composed Site plus Governed API E2E suite")
        return 0
    for finding in report.findings:
        print(f"E2E_READINESS_INVALID code={finding}")
    print("WORKFLOW_HOLD: E2E readiness boundary changed")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
