"""Repository-shape checks used by the fixture-root contract validator."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

EXPECTED_PROFILE_COUNT = 8
EXPECTED_TARGET = '\t@echo "TODO: regenerate deterministic fixtures"'
EXPECTED_ROOT: dict[str, object] = {
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


def root_entry(registry: Mapping[str, Any]) -> Mapping[str, Any] | None:
    entry_defaults = registry.get("entry_defaults", {})
    class_defaults = registry.get("class_defaults", {})
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
        result: dict[str, Any] = dict(entry_defaults)
        class_profile = class_defaults.get(raw.get("class"), {})
        if isinstance(class_profile, Mapping):
            result.update(class_profile)
        result.update(raw)
        return result
    return None


def inventory(root: Path) -> tuple[set[str], int, list[tuple[str, str]]]:
    directory = root / "fixtures"
    try:
        if directory.is_symlink():
            return set(), 0, [("INPUT_SYMLINK_DENIED", "fixtures")]
        if not directory.is_dir():
            return set(), 0, [("INPUT_NOT_DIRECTORY", "fixtures")]
        entries = sorted(directory.iterdir(), key=lambda item: item.name)
    except OSError:
        return set(), 0, [("INPUT_READ_ERROR", "fixtures")]

    files = [item.name for item in entries if item.is_file()]
    dirs = [item.name for item in entries if item.is_dir()]
    findings: list[tuple[str, str]] = []
    if files != ["README.md"]:
        findings.append(("DIRECT_CHILD_FILE_SET_INVALID", "/fixtures/files"))
    if any(not item.is_file() and not item.is_dir() for item in entries):
        findings.append(("DIRECT_CHILD_TYPE_INVALID", "/fixtures/entries"))
    return {"README.md", *dirs}, len(dirs), findings


def aggregate(
    registry: Mapping[str, Any], root: Path
) -> tuple[int, list[tuple[str, str]]]:
    profiles, validators = registry.get("profiles"), registry.get("validators")
    if not isinstance(profiles, Mapping) or not isinstance(validators, list):
        return 0, [("VALIDATOR_REGISTRY_SHAPE_INVALID", "/validator_registry")]
    full = profiles.get("full")
    if not isinstance(full, list) or not all(isinstance(item, str) for item in full):
        return 0, [("AGGREGATE_PROFILE_INVALID", "/validator_registry/profiles/full")]

    findings: list[tuple[str, str]] = []
    if len(full) != EXPECTED_PROFILE_COUNT:
        findings.append(("AGGREGATE_PROFILE_COUNT_MISMATCH", "/validator_registry/profiles/full"))
    if len(full) != len(set(full)):
        findings.append(("AGGREGATE_PROFILE_DUPLICATE", "/validator_registry/profiles/full"))
    by_id = {
        item.get("id"): item
        for item in validators
        if isinstance(item, Mapping) and isinstance(item.get("id"), str)
    }
    for index, validator_id in enumerate(full):
        field = f"/validator_registry/profiles/full/{index}"
        item = by_id.get(validator_id)
        if item is None:
            findings.append(("AGGREGATE_VALIDATOR_MISSING", field))
            continue
        args, script = item.get("args"), item.get("script")
        if not isinstance(args, list) or "--fixtures" not in args:
            findings.append(("FIXTURE_MODE_ARGUMENT_MISSING", field))
        if not isinstance(script, str) or not (root / script).is_file():
            findings.append(("AGGREGATE_VALIDATOR_SCRIPT_MISSING", field))
    return len(full), findings
