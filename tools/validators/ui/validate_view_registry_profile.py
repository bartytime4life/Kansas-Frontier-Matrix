#!/usr/bin/env python3
"""Validate fixture-only contract-first view registry candidates.

A PASS proves bounded local shape and consistency only. It does not resolve any
reference, bind a route, query a store, evaluate policy, activate a layer,
approve review, release an artifact, deploy code, or publish a view.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/ui/view_registry_profile.schema.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:view-registry:"
_DIRECT_STORE_MARKERS = (
    "postgres://",
    "neo4j://",
    "s3://",
    "file://",
    "data/raw",
    "data/work",
    "data/quarantine",
    "raw/",
    "work/",
    "quarantine/",
)
_QUERY_MARKERS = ("match (", "select *", "sparql ", "graph_query", "cypher:")


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("VIEW_REGISTRY_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("VIEW_REGISTRY_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("VIEW_REGISTRY_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("VIEW_REGISTRY_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("VIEW_REGISTRY_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("VIEW_REGISTRY_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("VIEW_REGISTRY_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("VIEW_REGISTRY_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"registry_id", "spec_hash"}}
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("VIEW_REGISTRY_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("VIEW_REGISTRY_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("VIEW_REGISTRY_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _walk_strings(value: Any, path: str = "") -> Iterable[tuple[str, str]]:
    if isinstance(value, str):
        yield path or "/", value
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _walk_strings(item, f"{path}/{index}")
    elif isinstance(value, dict):
        for key in sorted(value):
            escaped = str(key).replace("~", "~0").replace("/", "~1")
            yield from _walk_strings(value[key], f"{path}/{escaped}")


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("VIEW_REGISTRY_CANONICALIZATION_ERROR", "/"))
    else:
        if value.get("spec_hash") != expected_hash:
            findings.add(Finding("VIEW_REGISTRY_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value.get("registry_id") != expected_id:
            findings.add(Finding("VIEW_REGISTRY_ID_MISMATCH", "/registry_id"))

    entries = value["entries"]
    view_ids = [entry["view_id"] for entry in entries]
    routes = [entry["route_path"] for entry in entries]
    if view_ids != sorted(view_ids):
        findings.add(Finding("VIEW_REGISTRY_ENTRY_ORDER_INVALID", "/entries"))
    if len(set(view_ids)) != len(view_ids):
        findings.add(Finding("VIEW_REGISTRY_VIEW_ID_DUPLICATE", "/entries"))
    if len(set(routes)) != len(routes):
        findings.add(Finding("VIEW_REGISTRY_ROUTE_DUPLICATE", "/entries"))

    for index, entry in enumerate(entries):
        layers = entry["layer_manifest_refs"]
        if layers != sorted(layers):
            findings.add(Finding("VIEW_REGISTRY_LAYER_ORDER_INVALID", f"/entries/{index}/layer_manifest_refs"))
        catalog_refs = set(entry["catalog"].values()) - {"READY", "HOLD", "DENY"}
        if entry["release_manifest_ref"] in catalog_refs:
            findings.add(Finding("VIEW_REGISTRY_RELEASE_CATALOG_ROLE_COLLAPSE", f"/entries/{index}/release_manifest_ref"))

    for path, text in _walk_strings(value):
        lowered = text.casefold()
        if any(marker in lowered for marker in _DIRECT_STORE_MARKERS):
            findings.add(Finding("VIEW_REGISTRY_DIRECT_STORE_REFERENCE_DENIED", path))
        if any(marker in lowered for marker in _QUERY_MARKERS):
            findings.add(Finding("VIEW_REGISTRY_EMBEDDED_QUERY_DENIED", path))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema = _schema_findings(value)
    if schema:
        return Result("DENY", schema)
    semantic = _semantic_findings(value)
    if semantic:
        return Result("DENY", semantic)
    closure_states = {entry["catalog"]["closure_state"] for entry in value["entries"]}
    if "DENY" in closure_states:
        return Result("DENY", (Finding("VIEW_REGISTRY_CATALOG_CLOSURE_DENIED", "/entries"),))
    if "HOLD" in closure_states:
        return Result("ABSTAIN", (Finding("VIEW_REGISTRY_CATALOG_CLOSURE_HELD", "/entries"),))
    return Result("PASS", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    return Result("ERROR", findings) if value is None else validate_payload(value)


def _serialize(path: Path, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix(),
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": [
                "no_network",
                "no_route_binding",
                "no_direct_store_or_graph_query",
                "no_layer_activation",
                "no_policy_review_release_deployment_or_publication",
            ],
            "outcome": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args(argv)
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
