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
EXPECTED_PLACEHOLDER = "def test_proof_slice_placeholder():\n    assert True"


@dataclass(frozen=True)
class ReadinessReport:
    findings: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


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
        placeholder = e2e_root / "test_hydrology_proof_slice.py"
        if placeholder.is_file():
            try:
                tree = ast.parse(placeholder.read_text(encoding="utf-8"))
                expected = ast.parse(EXPECTED_PLACEHOLDER)
                if ast.dump(tree, include_attributes=False) != ast.dump(expected, include_attributes=False):
                    findings.append("E2E_PLACEHOLDER_CHANGED")
            except (OSError, SyntaxError, UnicodeError):
                findings.append("E2E_PLACEHOLDER_INVALID")

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
