#!/usr/bin/env python3
"""Validate the bounded KFM E2E readiness hold without running live systems.

This standard-library checker confirms that the implemented Explorer Web
baseline and its separate build/test workflow remain present while the
repository-wide browser/API E2E suite remains deliberately unimplemented.  It
does not start services, install dependencies, make network requests, validate
claims, or grant evidence, policy, release, deployment, or publication status.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
from typing import Mapping, Sequence


MAX_TEXT_BYTES = 2 * 1024 * 1024

EXPECTED_ROOT_HOLDS = {
    "lint": (
        "node -e \"console.error('WORKFLOW_HOLD: root workspace lint "
        "is not implemented.'); process.exit(1)\""
    ),
    "test": (
        "node -e \"console.error('WORKFLOW_HOLD: root workspace tests "
        "are not implemented.'); process.exit(1)\""
    ),
    "build": (
        "node -e \"console.error('WORKFLOW_HOLD: root workspace build "
        "is not implemented.'); process.exit(1)\""
    ),
}

EXPECTED_EXPLORER_SCRIPTS = {
    "dev": "vite",
    "build": "tsc --noEmit -p tsconfig.json && vite build",
    "test": "pnpm run test:unit && pnpm run test:browser",
    "test:unit": "vitest run tests/*.test.ts",
    "test:browser": "playwright test --config=playwright.config.ts",
}

LOCKED_EXPLORER_BROWSER_BASELINE = {
    "apps/explorer-web/playwright.config.ts",
    "apps/explorer-web/tests/browser/evidence-drawer.fixture.ts",
    "apps/explorer-web/tests/browser/evidence-drawer.html",
    "apps/explorer-web/tests/browser/evidence-drawer.spec.ts",
}

EXPECTED_E2E_INVENTORY = {
    "tests/e2e/README.md",
    "tests/e2e/__init__.py",
    "tests/e2e/agriculture/.gitkeep",
    "tests/e2e/agriculture/README.md",
    "tests/e2e/test_hydrology_proof_slice.py",
}

REQUIRED_TEXT_PATHS = {
    ".github/workflows/api-test.yml",
    ".github/workflows/e2e-smoke.yml",
    ".github/workflows/ui-build.yml",
    "Makefile",
    "apps/explorer-web/README.md",
    "apps/explorer-web/index.html",
    "apps/explorer-web/playwright.config.ts",
    "apps/explorer-web/src/features/shell/index.tsx",
    "apps/explorer-web/src/main.ts",
    *LOCKED_EXPLORER_BROWSER_BASELINE,
    "apps/explorer-web/tests/shell-baseline.test.ts",
    "apps/governed-api/README.md",
    "package.json",
    "pnpm-lock.yaml",
    "pnpm-workspace.yaml",
    *EXPECTED_E2E_INVENTORY,
}

IGNORED_SCAN_DIRECTORIES = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".vite",
    "__pycache__",
    "coverage",
    "dist",
    "node_modules",
}


@dataclass(frozen=True, order=True)
class ReadinessFinding:
    """One deterministic, non-content-bearing readiness finding."""

    code: str
    path: str
    detail: str


@dataclass(frozen=True)
class ReadinessReport:
    """Bounded result for the current E2E readiness surface."""

    findings: tuple[ReadinessFinding, ...]
    inspected_files: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _display(path: Path, repository_root: Path) -> str:
    try:
        return path.relative_to(repository_root).as_posix() or "."
    except ValueError:
        return path.as_posix()


def _read_text(
    path: Path,
    *,
    repository_root: Path,
    findings: list[ReadinessFinding],
    inspected: set[str],
) -> str | None:
    display = _display(path, repository_root)
    inspected.add(display)
    try:
        if path.is_symlink():
            findings.append(
                ReadinessFinding(
                    "INPUT_SYMLINK_DENIED",
                    display,
                    "readiness inputs must be regular repository files",
                )
            )
            return None
        if not path.is_file():
            findings.append(
                ReadinessFinding(
                    "REQUIRED_PATH_MISSING",
                    display,
                    "required readiness input is not a regular file",
                )
            )
            return None
        if path.stat().st_size > MAX_TEXT_BYTES:
            findings.append(
                ReadinessFinding(
                    "INPUT_TOO_LARGE",
                    display,
                    "readiness text input exceeds 2 MiB",
                )
            )
            return None
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        findings.append(
            ReadinessFinding(
                "INPUT_UNREADABLE",
                display,
                "readiness input could not be read as UTF-8",
            )
        )
        return None


def _read_json_object(
    path: Path,
    *,
    repository_root: Path,
    findings: list[ReadinessFinding],
    inspected: set[str],
) -> Mapping[str, object] | None:
    text = _read_text(
        path,
        repository_root=repository_root,
        findings=findings,
        inspected=inspected,
    )
    if text is None:
        return None
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        findings.append(
            ReadinessFinding(
                "JSON_INVALID",
                _display(path, repository_root),
                "manifest is not valid JSON",
            )
        )
        return None
    if not isinstance(value, dict):
        findings.append(
            ReadinessFinding(
                "JSON_ROOT_INVALID",
                _display(path, repository_root),
                "manifest root must be an object",
            )
        )
        return None
    return value


def _script_mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, dict) else {}


def _check_manifests(
    repository_root: Path,
    findings: list[ReadinessFinding],
    inspected: set[str],
) -> None:
    root_path = repository_root / "package.json"
    explorer_path = repository_root / "apps/explorer-web/package.json"
    root = _read_json_object(
        root_path,
        repository_root=repository_root,
        findings=findings,
        inspected=inspected,
    )
    explorer = _read_json_object(
        explorer_path,
        repository_root=repository_root,
        findings=findings,
        inspected=inspected,
    )

    if root is not None:
        root_scripts = _script_mapping(root.get("scripts"))
        surfaced = sorted(name for name in root_scripts if "e2e" in name.lower())
        if surfaced:
            findings.append(
                ReadinessFinding(
                    "E2E_SCRIPT_SURFACED",
                    "package.json",
                    "review and wire surfaced E2E scripts: " + ", ".join(surfaced),
                )
            )
        changed = sorted(
            name
            for name, expected in EXPECTED_ROOT_HOLDS.items()
            if root_scripts.get(name) != expected
        )
        if changed:
            findings.append(
                ReadinessFinding(
                    "ROOT_HOLD_SCRIPTS_CHANGED",
                    "package.json",
                    "expected fail-closed root scripts changed: " + ", ".join(changed),
                )
            )
        if root.get("packageManager") != "pnpm@11.17.0":
            findings.append(
                ReadinessFinding(
                    "PACKAGE_MANAGER_PIN_CHANGED",
                    "package.json",
                    "expected exact pnpm@11.17.0 package-manager pin",
                )
            )
        engines = _script_mapping(root.get("engines"))
        if engines.get("node") != ">=22.13 <23":
            findings.append(
                ReadinessFinding(
                    "NODE_ENGINE_CHANGED",
                    "package.json",
                    "expected Node engine >=22.13 <23",
                )
            )

    if explorer is not None:
        scripts = _script_mapping(explorer.get("scripts"))
        surfaced = sorted(name for name in scripts if "e2e" in name.lower())
        if surfaced:
            findings.append(
                ReadinessFinding(
                    "E2E_SCRIPT_SURFACED",
                    "apps/explorer-web/package.json",
                    "review and wire surfaced E2E scripts: " + ", ".join(surfaced),
                )
            )
        if dict(scripts) != EXPECTED_EXPLORER_SCRIPTS:
            changed = sorted(
                name
                for name in set(scripts) | set(EXPECTED_EXPLORER_SCRIPTS)
                if scripts.get(name) != EXPECTED_EXPLORER_SCRIPTS.get(name)
            )
            findings.append(
                ReadinessFinding(
                    "EXPLORER_SCRIPT_MAPPING_CHANGED",
                    "apps/explorer-web/package.json",
                    "expected locked Explorer baseline scripts changed: "
                    + ", ".join(changed),
                )
            )
        engines = _script_mapping(explorer.get("engines"))
        if engines.get("node") != ">=22.13 <23":
            findings.append(
                ReadinessFinding(
                    "EXPLORER_NODE_ENGINE_CHANGED",
                    "apps/explorer-web/package.json",
                    "expected Explorer Node engine >=22.13 <23",
                )
            )


def _check_text_markers(
    repository_root: Path,
    findings: list[ReadinessFinding],
    inspected: set[str],
) -> None:
    checks = {
        "pnpm-workspace.yaml": (
            '- "apps/*"',
            '- "packages/*"',
        ),
        ".github/workflows/ui-build.yml": (
            "UI_MANIFEST: apps/explorer-web/package.json",
            "UI_WORKSPACE: explorer-web",
            'run: pnpm --filter "${UI_WORKSPACE}" build',
            'run: pnpm --filter "${UI_WORKSPACE}" test',
        ),
        ".github/workflows/api-test.yml": ("run: make governed-api-smoke",),
        ".github/workflows/e2e-smoke.yml": (
            "python tools/validators/e2e_readiness.py",
        ),
    }
    for relative, markers in checks.items():
        text = _read_text(
            repository_root / relative,
            repository_root=repository_root,
            findings=findings,
            inspected=inspected,
        )
        if text is None:
            continue
        missing = [marker for marker in markers if marker not in text]
        if missing:
            findings.append(
                ReadinessFinding(
                    "REQUIRED_MARKER_MISSING",
                    relative,
                    f"{len(missing)} required readiness marker(s) are absent",
                )
            )

    makefile = _read_text(
        repository_root / "Makefile",
        repository_root=repository_root,
        findings=findings,
        inspected=inspected,
    )
    if makefile is not None and re.search(
        r"^(?:e2e|e2e-smoke|test-e2e):", makefile, re.MULTILINE
    ):
        findings.append(
            ReadinessFinding(
                "E2E_MAKE_TARGET_SURFACED",
                "Makefile",
                "review and wire the surfaced repository E2E target",
            )
        )


def _check_e2e_inventory(
    repository_root: Path,
    findings: list[ReadinessFinding],
    inspected: set[str],
) -> None:
    root = repository_root / "tests/e2e"
    if not root.is_dir() or root.is_symlink():
        findings.append(
            ReadinessFinding(
                "E2E_ROOT_INVALID",
                "tests/e2e",
                "expected a regular tests/e2e directory",
            )
        )
        return

    observed: set[str] = set()
    try:
        for path in sorted(root.rglob("*")):
            if path.is_file():
                rel = path.relative_to(root)
                if any(part in IGNORED_SCAN_DIRECTORIES for part in rel.parts[:-1]):
                    continue
                relative = _display(path, repository_root)
                observed.add(relative)
                inspected.add(relative)
    except OSError:
        findings.append(
            ReadinessFinding(
                "E2E_INVENTORY_UNREADABLE",
                "tests/e2e",
                "bounded E2E inventory could not be inspected",
            )
        )
        return

    additions = sorted(observed - EXPECTED_E2E_INVENTORY)
    removals = sorted(EXPECTED_E2E_INVENTORY - observed)
    if additions or removals:
        detail = []
        if additions:
            detail.append("added=" + ",".join(additions))
        if removals:
            detail.append("removed=" + ",".join(removals))
        findings.append(
            ReadinessFinding(
                "E2E_INVENTORY_CHANGED",
                "tests/e2e",
                "; ".join(detail),
            )
        )

    init_text = _read_text(
        repository_root / "tests/e2e/__init__.py",
        repository_root=repository_root,
        findings=findings,
        inspected=inspected,
    )
    if init_text is not None and init_text.strip():
        findings.append(
            ReadinessFinding(
                "E2E_INIT_CHANGED",
                "tests/e2e/__init__.py",
                "inspect the surfaced parent harness before wiring E2E",
            )
        )

    placeholder_path = repository_root / "tests/e2e/test_hydrology_proof_slice.py"
    placeholder_text = _read_text(
        placeholder_path,
        repository_root=repository_root,
        findings=findings,
        inspected=inspected,
    )
    if placeholder_text is not None:
        try:
            observed_tree = ast.parse(placeholder_text, filename=str(placeholder_path))
        except SyntaxError:
            findings.append(
                ReadinessFinding(
                    "E2E_PLACEHOLDER_SYNTAX_INVALID",
                    "tests/e2e/test_hydrology_proof_slice.py",
                    "placeholder module is not valid Python",
                )
            )
        else:
            expected_tree = ast.parse(
                "def test_proof_slice_placeholder():\n    assert True\n"
            )
            if ast.dump(observed_tree, include_attributes=False) != ast.dump(
                expected_tree, include_attributes=False
            ):
                findings.append(
                    ReadinessFinding(
                        "E2E_PLACEHOLDER_CHANGED",
                        "tests/e2e/test_hydrology_proof_slice.py",
                        "inspect surfaced Hydrology E2E behavior before wiring CI",
                    )
                )


def _check_surfaced_e2e_files(
    repository_root: Path,
    findings: list[ReadinessFinding],
    inspected: set[str],
) -> None:
    surfaced: list[str] = []
    for relative_root in ("apps/explorer-web", "apps/governed-api", "packages"):
        root = repository_root / relative_root
        if not root.is_dir() or root.is_symlink():
            continue
        for directory, names, files in os.walk(root, followlinks=False):
            names[:] = sorted(
                name for name in names if name not in IGNORED_SCAN_DIRECTORIES
            )
            for name in sorted(files):
                path = Path(directory) / name
                relative = _display(path, repository_root)
                parts = [part.lower() for part in Path(relative).parts]
                lower_name = name.lower()
                if (
                    "e2e" in parts
                    or "e2e" in lower_name
                    or (
                        lower_name.startswith("playwright.config.")
                        and relative not in LOCKED_EXPLORER_BROWSER_BASELINE
                    )
                ):
                    surfaced.append(relative)
                    inspected.add(relative)
    if surfaced:
        findings.append(
            ReadinessFinding(
                "E2E_IMPLEMENTATION_SURFACED",
                "apps/explorer-web|apps/governed-api|packages",
                "review and wire surfaced files: " + ",".join(sorted(surfaced)),
            )
        )


def inspect_readiness(repository_root: Path) -> ReadinessReport:
    """Inspect one repository root without executing repository code."""

    root = Path(os.path.abspath(repository_root))
    findings: list[ReadinessFinding] = []
    inspected: set[str] = set()
    if root.is_symlink() or not root.is_dir():
        return ReadinessReport(
            (
                ReadinessFinding(
                    "REPOSITORY_ROOT_INVALID",
                    root.as_posix(),
                    "repository root must be a regular directory",
                ),
            ),
            (),
        )

    for relative in sorted(REQUIRED_TEXT_PATHS - {"package.json"}):
        _read_text(
            root / relative,
            repository_root=root,
            findings=findings,
            inspected=inspected,
        )

    _check_manifests(root, findings, inspected)
    _check_text_markers(root, findings, inspected)
    _check_e2e_inventory(root, findings, inspected)
    _check_surfaced_e2e_files(root, findings, inspected)
    return ReadinessReport(
        tuple(sorted(set(findings))),
        tuple(sorted(inspected)),
    )


def render_report(report: ReadinessReport) -> tuple[str, ...]:
    """Render bounded output that never echoes manifest or source contents."""

    if report.ok:
        return (
            "E2E_READINESS_CONFIRMED "
            "explorer_baseline=implemented e2e_suite=not-established "
            f"inspected_files={len(report.inspected_files)}",
            "WORKFLOW_SKIPPED_EXPLICIT: run-e2e-smoke",
            "WORKFLOW_HOLD: no accepted Explorer Web plus Governed API E2E "
            "command or deterministic fixture suite",
        )
    lines = tuple(
        "E2E_READINESS_INVALID "
        f"code={finding.code} path={finding.path} detail={finding.detail}"
        for finding in report.findings
    )
    return lines + (
        "WORKFLOW_HOLD: E2E readiness boundary changed; inspect before wiring "
        "a composed suite",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate the no-network KFM E2E readiness hold without starting "
            "services or executing discovered application code."
        )
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root to inspect (default: current directory).",
    )
    arguments = parser.parse_args(argv)
    report = inspect_readiness(Path(arguments.repo_root))
    for line in render_report(report):
        print(line)
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
