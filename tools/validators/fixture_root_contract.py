"""Deterministic fixture-root documentation and projection contract checks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from tools.validators._fixture_root_contract_checks import (
    EXPECTED_ROOT,
    EXPECTED_TARGET,
    aggregate,
    inventory,
    root_entry,
)
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

README = Path("fixtures/README.md")
ROOT_REGISTRY = Path("control_plane/root_registry.yaml")
VALIDATOR_REGISTRY = Path("tools/validators/validator_registry.json")
MAKEFILE = Path("Makefile")
SCOPE = "fixtures-root-contract-only"


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
        if self.ok:
            return "PASS"
        operational = ("INPUT_", "JSON_", "REPO_ROOT_")
        return "ERROR_VALIDATOR" if any(f.code.startswith(operational) for f in self.findings) else "FAIL_INVARIANT"


def _error(code: str | None, field: str) -> list[Finding]:
    return [] if code is None else [Finding(code, field)]


def _pairs(items: list[tuple[str, str]]) -> list[Finding]:
    return [Finding(code, field) for code, field in items]


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
    readme, error = read_text(root / README, limit=MAX_TEXT_BYTES, field=README.as_posix())
    findings.extend(_error(error, README.as_posix()))
    root_registry, error = read_json(root / ROOT_REGISTRY, field=ROOT_REGISTRY.as_posix())
    findings.extend(_error(error, ROOT_REGISTRY.as_posix()))
    validator_registry, error = read_json(root / VALIDATOR_REGISTRY, field=VALIDATOR_REGISTRY.as_posix())
    findings.extend(_error(error, VALIDATOR_REGISTRY.as_posix()))
    makefile, error = read_text(root / MAKEFILE, limit=MAX_TEXT_BYTES, field=MAKEFILE.as_posix())
    findings.extend(_error(error, MAKEFILE.as_posix()))
    children, child_count, child_findings = inventory(root)
    findings.extend(_pairs(child_findings))

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
        elif snapshot != child_count:
            findings.append(Finding("DIRECT_CHILD_COUNT_MISMATCH", "/direct_child_snapshot"))
        documented, error = tree_entries(readme)
        findings.extend(_error(error, "/direct_child_map"))
        if documented is not None and documented != children:
            findings.append(Finding("DIRECT_CHILD_MAP_MISMATCH", "/direct_child_map"))

    if root_registry is not None:
        entry = root_entry(root_registry)
        if entry is None:
            findings.append(Finding("ROOT_REGISTRY_ENTRY_MISSING", "/root_registry/fixtures"))
        else:
            findings.extend(
                Finding("ROOT_REGISTRY_FIELD_MISMATCH", f"/root_registry/fixtures/{key}")
                for key, expected in EXPECTED_ROOT.items()
                if entry.get(key) != expected
            )

    aggregate_count = 0
    if validator_registry is not None:
        aggregate_count, aggregate_findings = aggregate(validator_registry, root)
        findings.extend(_pairs(aggregate_findings))
    if makefile is not None and fixtures_target_lines(makefile) != [EXPECTED_TARGET]:
        findings.append(Finding("FIXTURES_TARGET_SEMANTICS_CHANGED", "/Makefile/fixtures"))

    return ValidationResult(
        tuple(sorted(set(findings))),
        direct_child_directories=child_count,
        aggregate_validators=aggregate_count,
    )
