#!/usr/bin/env python3
"""Validate the KFM path-alias register without network access.

A PASS proves bounded shape, doctrine/root-registry binding, compatibility-class
semantics, dual-read/single-write constraints, identity uniqueness, and (when
enabled) repository-path parity. It does not accept an ADR, authorize an alias,
move bytes, create a tombstone, close consumers, retire a path, or grant release,
deployment, promotion, or publication status.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

_BOOTSTRAP_ROOT = Path(__file__).resolve().parents[3]
if str(_BOOTSTRAP_ROOT) not in sys.path:
    sys.path.insert(0, str(_BOOTSTRAP_ROOT))

from tools.validators.directory_governance.path_alias_fixtures import run_fixture_profile as _run_fixtures
from tools.validators.directory_governance.path_alias_io import load_root_registry, read_object, schema_findings
from tools.validators.directory_governance.path_alias_model import (
    ADOPTED_DECISION,
    ADOPTED_DOCTRINE_SHA256,
    ADR_PATH,
    DOCTRINE_PATH,
    EXPECTED_ROOT_REGISTRY_BASE,
    EXPECTED_ROOT_REGISTRY_SHA256,
    FIXTURE_ROOT,
    REGISTER_PATH,
    REPO_ROOT,
    ROOT_REGISTRY_PATH,
    SCHEMA_PATH,
    SCOPE,
    Finding,
    ValidationResult,
)
from tools.validators.directory_governance.path_alias_repository import repository_findings
from tools.validators.directory_governance.path_alias_semantics import semantic_findings


def validate_register(
    path: Path,
    *,
    repo_root: Path = REPO_ROOT,
    root_registry_path: Path = ROOT_REGISTRY_PATH,
    check_repository: bool = True,
    enforce_projection_binding: bool = True,
) -> ValidationResult:
    candidate, findings = read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    root_registry, root_findings = load_root_registry(root_registry_path)
    findings.extend(root_findings)
    findings.extend(schema_findings(candidate))
    if not findings and root_registry is not None:
        findings.extend(
            semantic_findings(
                candidate,
                root_registry,
                enforce_projection_binding=enforce_projection_binding,
            )
        )
        if check_repository:
            findings.extend(repository_findings(candidate, repo_root))
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display(path),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": result.outcome,
            "scope": SCOPE,
            "authority": {
                "accepts_adr": False,
                "authorizes_alias_writes": False,
                "closes_consumers": False,
                "migrates_or_deletes_paths": False,
                "releases": False,
                "publishes": False,
            },
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    return _run_fixtures(validate_register, _serialize)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the KFM path-alias register projection.")
    parser.add_argument("path", nargs="?", default=str(REGISTER_PATH))
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    parser.add_argument("--root-registry", default=str(ROOT_REGISTRY_PATH))
    parser.add_argument("--skip-repository", action="store_true")
    parser.add_argument("--skip-projection-binding", action="store_true")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        return run_fixture_profile()

    result = validate_register(
        Path(args.path),
        repo_root=Path(args.repo_root),
        root_registry_path=Path(args.root_registry),
        check_repository=not args.skip_repository,
        enforce_projection_binding=not args.skip_projection_binding,
    )
    print(_serialize(Path(args.path), result))
    if result.outcome == "PASS":
        return 0
    if result.outcome == "ERROR_VALIDATOR":
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
