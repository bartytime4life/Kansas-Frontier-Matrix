#!/usr/bin/env python3
"""Validate the projection-only KFM Domain Lane Register without network access."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from yaml.events import AliasEvent
from yaml.resolver import BaseResolver

ROOT = Path(__file__).resolve().parents[3]
REGISTER = ROOT / "control_plane/domain_lane_register.yaml"
SCHEMA = ROOT / "schemas/contracts/v1/governance/domain_lane_register.schema.json"
DOCTRINE_SHA = "44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e"
LANES = (
    "agriculture",
    "archaeology",
    "atmosphere",
    "fauna",
    "flora",
    "geology",
    "habitat",
    "hazards",
    "hydrology",
    "people-dna-land",
    "roads-rail-trade",
    "settlements-infrastructure",
    "soil",
)
CROSS = ("matrix", "scene", "spatial")
ALIASES = {
    "air": "atmosphere",
    "settlement": "settlements-infrastructure",
    "transport": "roads-rail-trade",
}
MAX_BYTES = 4 * 1024 * 1024
MAX_NODES = 8_192
MAX_DEPTH = 64


class DuplicateKey(ValueError):
    """Raised when a YAML mapping repeats a key."""


class AliasDenied(ValueError):
    """Raised when a YAML alias is present in a governance projection."""


class StrictLoader(yaml.SafeLoader):
    """Safe YAML loader with duplicate-key, alias, and timestamp controls."""

    yaml_implicit_resolvers = copy.deepcopy(yaml.SafeLoader.yaml_implicit_resolvers)

    def compose_node(self, parent: object, index: object) -> yaml.Node:
        if self.check_event(AliasEvent):
            raise AliasDenied
        return super().compose_node(parent, index)


for first_character, resolvers in list(StrictLoader.yaml_implicit_resolvers.items()):
    StrictLoader.yaml_implicit_resolvers[first_character] = [
        (tag, regexp)
        for tag, regexp in resolvers
        if tag != "tag:yaml.org,2002:timestamp"
    ]


def _construct_mapping(
    loader: StrictLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
    loader.flatten_mapping(node)
    value: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in value
        except TypeError as exc:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "found an unhashable mapping key",
                key_node.start_mark,
            ) from exc
        if duplicate:
            raise DuplicateKey
        value[key] = loader.construct_object(value_node, deep=deep)
    return value


StrictLoader.add_constructor(BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class Result:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def outcome(self) -> str:
        codes = {finding.code for finding in self.findings}
        if not codes:
            return "PASS"
        if any(
            code.startswith(("INPUT_", "YAML_", "SCHEMA_", "REPO_ROOT_"))
            for code in codes
        ):
            return "ERROR_VALIDATOR"
        if codes & {
            "AUTHORITY_BINDING_MISSING",
            "DECISION_EVIDENCE_MISSING",
            "DOMAIN_DOCUMENTATION_MISSING",
        }:
            return "HOLD_UNRESOLVED"
        if codes & {
            "CANONICAL_LANE_MISSING",
            "UNEXPECTED_DOMAIN_LANE",
            "DOMAIN_ROOT_PRESENT",
        }:
            return "FAIL_NEW_DRIFT"
        return "FAIL_INVARIANT"


def _bounded(value: object) -> bool:
    pending = [(value, 0)]
    visited = 0
    while pending:
        current, depth = pending.pop()
        visited += 1
        if visited > MAX_NODES or depth > MAX_DEPTH:
            return False
        if isinstance(current, float) and not math.isfinite(current):
            return False
        if isinstance(current, Mapping):
            pending.extend((child, depth + 1) for child in current.values())
        elif isinstance(current, list):
            pending.extend((child, depth + 1) for child in current)
    return True


def load(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = yaml.load(path.read_text(encoding="utf-8"), Loader=StrictLoader)
    except DuplicateKey:
        return None, [Finding("YAML_DUPLICATE_KEY", "/")]
    except AliasDenied:
        return None, [Finding("YAML_ALIAS_DENIED", "/")]
    except yaml.YAMLError:
        return None, [Finding("YAML_INVALID", "/")]
    except (OSError, UnicodeError):
        return None, [Finding("INPUT_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    if not _bounded(value):
        return None, [Finding("YAML_COMPLEXITY_OR_NUMBER_LIMIT", "/")]
    return value, []


def ptr(parts: Iterable[Any]) -> str:
    bits = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(bits) if bits else "/"


def schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema,
                    format_checker=FormatChecker(),
                ).iter_errors(value),
                101,
            )
        )
    except Exception:
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", ptr(error.absolute_path))
        for error in sorted(
            errors[:100],
            key=lambda error: (ptr(error.absolute_path), str(error.validator)),
        )
    ]
    if len(errors) > 100:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def bindings(value: Mapping[str, Any], root: Path) -> list[Finding]:
    findings: list[Finding] = []
    checks = [
        (
            value.get("doctrine"),
            "sha256",
            lambda path: "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest(),
            "/doctrine",
        ),
        (value.get("narrative_register"), "git_blob", blob, "/narrative_register"),
        (value.get("root_registry"), "git_blob", blob, "/root_registry"),
    ]
    for item, key, digest_function, field in checks:
        if not isinstance(item, Mapping):
            continue
        path = root / str(item.get("path", ""))
        if not path.is_file():
            findings.append(Finding("AUTHORITY_BINDING_MISSING", field + "/path"))
            continue
        try:
            observed = digest_function(path)
        except OSError:
            findings.append(Finding("AUTHORITY_BINDING_MISSING", field + "/path"))
            continue
        if observed != item.get(key):
            findings.append(Finding("AUTHORITY_DIGEST_MISMATCH", field + "/" + key))
    if not (
        root / "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
    ).is_file():
        findings.append(Finding("DECISION_EVIDENCE_MISSING", "/doctrine/decision_ref"))
    return findings


def semantic(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    doctrine = value.get("doctrine", {})
    root_registry = value.get("root_registry", {})
    meta = value.get("meta", {})
    if isinstance(doctrine, Mapping):
        if doctrine.get("sha256") != "sha256:" + DOCTRINE_SHA:
            findings.append(Finding("DOCTRINE_DIGEST_MISMATCH", "/doctrine/sha256"))
        if doctrine.get("decision_ref") != "ADR-0029":
            findings.append(
                Finding("DECISION_EVIDENCE_MISSING", "/doctrine/decision_ref")
            )
    if isinstance(root_registry, Mapping) and root_registry.get("base_ref") != value.get(
        "base_ref"
    ):
        findings.append(Finding("BASE_REF_MISMATCH", "/root_registry/base_ref"))
    if isinstance(meta, Mapping):
        if meta.get("last_reviewed") != value.get("updated_at"):
            findings.append(Finding("REVIEW_DATE_MISMATCH", "/meta/last_reviewed"))
        if tuple(meta.get("related_doctrine", [])) != (
            "docs/doctrine/directory-rules.md",
            "docs/registers/DOMAIN_LANE.md",
        ):
            findings.append(
                Finding("RELATED_DOCTRINE_MISMATCH", "/meta/related_doctrine")
            )
    if tuple(value.get("cross_cutting_exclusions", [])) != CROSS:
        findings.append(
            Finding("CROSS_CUTTING_SET_MISMATCH", "/cross_cutting_exclusions")
        )
    if value.get("unresolved_aliases") != ALIASES:
        findings.append(Finding("ALIAS_SET_MISMATCH", "/unresolved_aliases"))
    defaults = value.get("lane_defaults", {})
    if isinstance(defaults, Mapping) and defaults.get("owner_identity") is not None:
        findings.append(
            Finding("OWNER_IDENTITY_OVERCLAIM", "/lane_defaults/owner_identity")
        )
    entries = [entry for entry in value.get("entries", []) if isinstance(entry, Mapping)]
    ids = [entry.get("lane_id") for entry in entries]
    if ids != sorted(ids):
        findings.append(Finding("LANES_NOT_CANONICAL", "/entries"))
    if len(ids) != len(set(ids)):
        findings.append(Finding("LANE_ID_DUPLICATE", "/entries"))
    seen = {lane_id for lane_id in ids if isinstance(lane_id, str)}
    for lane_id in sorted(set(LANES) - seen):
        findings.append(Finding("CANONICAL_LANE_MISSING", "/entries/" + lane_id))
    for lane_id in sorted(seen - set(LANES)):
        findings.append(Finding("UNEXPECTED_DOMAIN_LANE", "/entries/" + lane_id))
    paths: list[object] = []
    aliases: list[object] = []
    for index, entry in enumerate(entries):
        base = f"/entries/{index}"
        lane_id = entry.get("lane_id")
        path = entry.get("documentation_path")
        alias = entry.get("code_alias")
        paths.append(path)
        aliases.append(alias)
        if isinstance(lane_id, str):
            if path != f"docs/domains/{lane_id}/":
                findings.append(
                    Finding("DOCUMENTATION_PATH_MISMATCH", base + "/documentation_path")
                )
            if alias != lane_id.replace("-", "_"):
                findings.append(Finding("CODE_ALIAS_MISMATCH", base + "/code_alias"))
    for values, code in (
        (paths, "DOCUMENTATION_PATH_DUPLICATE"),
        (aliases, "CODE_ALIAS_DUPLICATE"),
    ):
        strings = [value for value in values if isinstance(value, str)]
        if len(strings) != len(set(strings)):
            findings.append(Finding(code, "/entries"))
    return findings


def repository(value: Mapping[str, Any], root: Path) -> list[Finding]:
    try:
        resolved_root = root.resolve(strict=True)
    except OSError:
        return [Finding("REPO_ROOT_UNAVAILABLE", "/repo_root")]
    findings: list[Finding] = []
    for index, entry in enumerate(value.get("entries", [])):
        if not isinstance(entry, Mapping) or not isinstance(entry.get("lane_id"), str):
            continue
        lane_id = entry["lane_id"]
        if not (resolved_root / f"docs/domains/{lane_id}").is_dir():
            findings.append(
                Finding(
                    "DOMAIN_DOCUMENTATION_MISSING",
                    f"/entries/{index}/documentation_path",
                )
            )
        if (resolved_root / lane_id).exists():
            findings.append(Finding("DOMAIN_ROOT_PRESENT", "/repo_roots/" + lane_id))
    return findings


def validate(
    path: Path,
    *,
    repo_root: Path = ROOT,
    check_repository: bool = True,
    check_bindings: bool = True,
) -> Result:
    value, findings = load(path)
    if value is None:
        return Result(tuple(sorted(set(findings))))
    findings += schema_findings(value)
    if not findings:
        findings += semantic(value)
        if check_bindings:
            findings += bindings(value, repo_root)
        if check_repository:
            findings += repository(value, repo_root)
    return Result(tuple(sorted(set(findings))))


def serialize(path: Path, result: Result) -> str:
    try:
        name = path.resolve().relative_to(ROOT.resolve()).as_posix()
    except Exception:
        name = path.name
    return json.dumps(
        {
            "file": name,
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": result.outcome,
            "scope": "domain-lane-register-projection-only",
            "authority": {
                "creates_domain": False,
                "assigns_steward": False,
                "activates_source": False,
                "writes_lifecycle_state": False,
                "authorizes_release": False,
                "deploys": False,
                "promotes": False,
                "publishes": False,
            },
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path, default=REGISTER)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--no-repository-checks", action="store_true")
    parser.add_argument("--no-binding-checks", action="store_true")
    arguments = parser.parse_args(argv)
    result = validate(
        arguments.path,
        repo_root=arguments.repo_root,
        check_repository=not arguments.no_repository_checks,
        check_bindings=not arguments.no_binding_checks,
    )
    print(serialize(arguments.path, result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
