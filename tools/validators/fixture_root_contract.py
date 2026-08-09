"""Deterministic fixture-root documentation and projection contract checks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from tools.validators._fixture_root_contract_io import (
    MAX_TEXT_BYTES,
    REQUIRED_H2,
    REQUIRED_META,
    direct_child_snapshot,
    fixtures_target_lines,
    headings,
    metadata,
    read_json,
    read_text,
    tree_entries,
)

README_PATH = Path("fixtures/README.md")
ROOT_REGISTRY_PATH = Path("control_plane/root_registry.yaml")
MAKEFILE_PATH = Path("Makefile")
VALIDATOR_REGISTRY_PATH = Path("tools/validators/validator_registry.json")
SCOPE = "fixtures-root-contract-only"
EXPECTED_FIXTURES_TARGET = '\t@echo "TODO: regenerate deterministic fixtures"'
EXPECTED_FULL_PROFILE_COUNT = 8
EXPECTED_ROOT = {
    "root_id": "root.fixtures",
    "path": "fixtures/",
    "class": "canonical",
    "status": "ACTIVE",
    "responsibility": (
        "Reusable synthetic, valid, invalid, and golden test inputs and expected outputs"
    ),
    "exposure": "public",
    "mutation": "versioned",
    "retention": "repository_lifetime",
    "allowed_artifact_kinds": ["test_fixture"],
    "prohibited_artifact_kinds": ["data_instance", "release_decision"],
    "validation_profiles": ["synthetic_public_safe_only"],
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    direct_child_directories: int = 0
    aggregate_validators: int = 0

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def outcome(self) -> str:
        if not self.findings:
            return "PASS"
        if any(
            finding.code.startswith(("INPUT_", "JSON_", "REPO_ROOT_"))
            for finding in self.findings
        ):
            return "ERROR_VALIDATOR"
        return "FAIL_INVARIANT"


def _error(code: str | None, field: str) -> list[Finding]:
    return [] if code is None else [Finding(code, field)]


def _resolve_root_entry(registry: Mapping[str, Any]) -> Mapping[str, Any] | None:
    entry_defaults = registry.get("entry_defaults")
    class_defaults = registry.get("class_defaults")
    if not isinstance(entry_defaults, Mapping):
        entry_defaults = {}
    if not isinstance(class_defaults, Mapping):
        class_defaults = {}
    roots = registry.get("roots")
    if not isinstance(roots, list):
        return None
    for raw in roots:
        if not isinstance(raw, Mapping) or raw.get("path") != "fixtures/":
            continue
        merged: dict[str, Any] = dict(entry_defaults)
        class_profile = class_defaults.get(raw.get("class"), {})
        if isinstance(class_profile, Mapping):
            merged.update(class_profile)
        merged.update(raw)
        return merged
    return None


def _root_findings(registry: Mapping[str, Any]) -> list[Finding]:
    entry = _resolve_root_entry(registry)
    if entry is None:
        return [Finding("ROOT_REGISTRY_ENTRY_MISSING", "/root_registry/fixtures")]
    return [
        Finding("ROOT_REGISTRY_FIELD_MISMATCH", f"/root_registry/fixtures/{key}")
        for key, expected in EXPECTED_ROOT.items()
        if entry.get(key) != expected
    ]


def _fixture_inventory(repo_root: Path) -> tuple[set[str], int, list[Finding]]:
    fixture_root = repo_root / "fixtures"
    try:
        if fixture_root.is_symlink():
            return set(), 0, [Finding("INPUT_SYMLINK_DENIED", "fixtures")]
        if not fixture_root.is_dir():
            return set(), 0, [Finding("INPUT_NOT_DIRECTORY", "fixtures")]
        entries = sorted(fixture_root.iterdir(), key=lambda path: path.name)
    except OSError:
        return set(), 0, [Finding("INPUT_READ_ERROR", "fixtures")]
    files = [path.name for path in entries if path.is_file()]
    dirs = [path.name for path in entries if path.is_dir()]
    findings: list[Finding] = []
    if files != ["README.md"]:
        findings.append(Finding("DIRECT_CHILD_FILE_SET_INVALID", "/fixtures/files"))
    if any(not path.is_file() and not path.is_dir() for path in entries):
        findings.append(Finding("DIRECT_CHILD_TYPE_INVALID", "/fixtures/entries"))
    return {"README.md", *dirs}, len(dirs), findings


def _aggregate_findings(
    registry: Mapping[str, Any], repo_root: Path
) -> tuple[int, list[Finding]]:
    profiles = registry.get("profiles")
    validators = registry.get("validators")
    if not isinstance(profiles, Mapping) or not isinstance(validators, list):
        return 0, [Finding("VALIDATOR_REGISTRY_SHAPE_INVALID", "/validator_registry")]
    full = profiles.get("full")
    if not isinstance(full, list) or not all(isinstance(item, str) for item in full):
        return 0, [Finding("AGGREGATE_PROFILE_INVALID", "/validator_registry/profiles/full")]
    findings: list[Finding] = []
    if len(full) != EXPECTED_FULL_PROFILE_COUNT:
        findings.append(Finding("AGGREGATE_PROFILE_COUNT_MISMATCH", "/validator_registry/profiles/full"))
    if len(full) != len(set(ful)):
        findings.append(Finding("AGGREGATE_PROFILE_DUPLICATE", "/validator_registry/profiles/full"))
    by_id = {
        item.get("id"): item
        for item in validators
        if isinstance(item, Mapping) and isinstance(item.get("id"), str)
    }
    for index, validator_id in enumerate(full):
        entry = by_id.get(validator_id)
        field = f"/validator_registry/profiles/full/{index}"
        if entry is None:
            findings.append(Finding("AGGREGATE_VALIDATOR_MISSING", field))
            continue
        args = entry.get("args")
        if not isinstance(args, list) or "--fixtures" not in args:
            findings.append(Finding("FIXTURE_MODE_ARGUMENT_MISSING", field))
        script = entry.get("script")
        if not isinstance(script, str) or not (repo_root / script).is_file():
            findings.append(Finding("AGGREGATE_VALIDATOR_SCRIPT_MISSING", field))
    return len(full), findings


def validate_repository(repo_root: Path) -> ValidationResult:
    if repo_root.is_symlink():
        return ValidationResult((Finding("REPO_ROOT_SYMLINK_DENIED", "/repo_root"),))
    try:
        root = repo_root.resolve(strict=True)
    except OSError:
        return ValidationResult((Finding("REPO_ROOT_UNAVAILABLE", "/repo_root"),))
    if not root.is_dir():
        return ValidationResult((Finding("REPO_ROOT_INVALID", "/repo_root"),))

    findings: list[Finding] = []
    readme, error = read_text(root / README_PATH, limit=MAX_TEXT_BYTES, field=README_PATH.as_posix())
    findings.extend(_error(error, README_PATH.as_posix()))
    root_registry, error = read_json(root / ROOT_REGISTRY_PATH, field=ROOT_REGISTRY_PATH.as_posix())
    findings.extend(_error(error, ROOT_REGISTRY_PATH.as_posix()))
    validator_registry, error = read_json(root / VALIDATOR_REGISTRY_PATH, field=VALIDATOR_REGISTRY_PATH.as_posix())
    findings.extend(_error(error, VALIDATOR_REGISTRY_PATH.as_posix()))
    makefile, error = read_text(root / MAKEFILE_PATH, limit=MAX_TEXT_BYTES, field=MAKEFILE_PATH.as_posix())
    findings.extend(_error(error, MAKEFILE_PATH.as_posix()))
    children, directory_count, inventory_findings = _fixture_inventory(root)
    findings.extend(inventory_findings)

    aggregate_count = 0
    if readme is not None:
        meta, error = metadata(readme)
        findings.extend(_error(error, "/metadata"))
        findings.extend(
            Finding("META_FIELD_MISMATCH", f"/metadata/{key}")
            for key, expected in REQUIRED_META.items()
            if meta.get(key) != expected
        )
        h1, h2 = headings(readme)
        if len(h1) != 1:
            findings.append(Finding("H1_COUNT_INVALID", "/headings/h1"))
        if tuple(h2[: len(REQUIRED_H2)]) != REQUIRED_H2:
            findings.append(Finding("ROOT_FULL_HEADING_ORDER", "/headings/h2"))
        snapshot = direct_child_snapshot(readme)
        if snapshot is None:
            findings.append(Finding("DIRECT_CHILD_SNAPSHOT_MISSING", "/direct_child_snapshot"))
        elif snapshot != directory_count:
            findings.append(Finding("DIRECT_CHILD_COUNT_MISMATCH", "/direct_child_snapshot"))
        documented, error = tree_entries(readme)
        findings.extend(_error(error, "/direct_child_map"))
        if documented is not None and documented != children:
            findings.append(Finding("DIRECT_CHILD_MAP_MISMATCH", "/direct_child_map"))

    if root_registry is not None:
        findings.extend(_root_findings(root_registry))
    if validator_registry is not None:
        aggregate_count, aggregate_findings = _aggregate_findings(validator_registry, root)
        findings.extend(aggregate_findings)
    if makefile is not None and fixtures_target_lines(makefile) != [EXPECTED_FIXTURES_TARGET]:
        findings.append(Finding("FIXTURES_TARGET_SEMANTICS_CHANGED", "/Makefile/fixtures"))

    return ValidationResult(
        tuple(sorted(set(findings))),
        direct_child_directories=directory_count,
        aggregate_validators=aggregate_count,
    )
