#!/usr/bin/env python3
"""Validate proposed PlaceNameAuthorityGraphPacket records without network access.

A pass proves only bounded schema and semantic invariants. It grants no feature,
geometry, legal-status, ownership, source, evidence, policy, review, search,
promotion, release, deployment, publication, or public-use authority.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schemas/contracts/v1/domains/settlements-infrastructure/place_name_authority_graph.schema.json"
PROFILE = ROOT / "fixtures/contracts/v1/domains/settlements-infrastructure/place_name_authority_graph/fixture_profile.json"
SCOPE = "place-name-assertion-alias-binding-and-reconciliation-only"
MAX_BYTES = 1_048_576


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


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
    def error(self) -> bool:
        return any(
            finding.code.startswith(("FILE_", "JSON_", "INPUT_", "SCHEMA_UNAVAILABLE"))
            for finding in self.findings
        )


def _object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _constant(_: str) -> None:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_object,
            parse_constant=_constant,
            parse_float=_float,
        )
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("JSON_ROOT_INVALID", "/")]
    return value, []


def _arr(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _obj(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo else None


def _canonical(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def _hash(candidate: Mapping[str, Any]) -> str:
    value = dict(candidate)
    value.pop("spec_hash", None)
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = sorted(
            validator.iter_errors(candidate),
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )[:100]
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors]


def _ids(values: list[Any], key: str, field: str, code: str) -> tuple[list[str], list[Finding]]:
    found = [item.get(key) for item in values if isinstance(item, dict)]
    return (
        [item for item in found if isinstance(item, str)],
        [] if _canonical(found) else [Finding(code, field)],
    )


def _cycle(edges: list[tuple[str, str]]) -> bool:
    graph: dict[str, set[str]] = {}
    for left, right in edges:
        graph.setdefault(left, set()).add(right)
        graph.setdefault(right, set())
    active: set[str] = set()
    done: set[str] = set()

    def visit(node: str) -> bool:
        if node in active:
            return True
        if node in done:
            return False
        active.add(node)
        if any(visit(next_node) for next_node in sorted(graph.get(node, ()))):
            return True
        active.remove(node)
        done.add(node)
        return False

    return any(visit(node) for node in sorted(graph))


def _semantic(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    assertions = _arr(candidate.get("place_name_assertions"))
    edges = _arr(candidate.get("alias_edges"))
    bindings = _arr(candidate.get("feature_bindings"))
    decisions = _arr(candidate.get("authority_decisions"))
    provenance = _obj(candidate.get("provenance"))
    governance = _obj(candidate.get("governance"))

    supplied = candidate.get("spec_hash")
    if isinstance(supplied, str) and supplied != _hash(candidate):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    assertion_ids, added = _ids(assertions, "assertion_id", "/place_name_assertions", "ASSERTIONS_NOT_CANONICAL")
    findings += added
    edge_ids, added = _ids(edges, "edge_id", "/alias_edges", "ALIAS_EDGES_NOT_CANONICAL")
    findings += added
    binding_ids, added = _ids(bindings, "binding_id", "/feature_bindings", "BINDINGS_NOT_CANONICAL")
    findings += added
    decision_ids, added = _ids(decisions, "decision_id", "/authority_decisions", "DECISIONS_NOT_CANONICAL")
    findings += added
    assertion_set, binding_set, decision_set = set(assertion_ids), set(binding_ids), set(decision_ids)

    arrays: list[tuple[str, list[Any]]] = [("/provenance/input_refs", _arr(provenance.get("input_refs")))]
    for group_name, values in (
        ("place_name_assertions", assertions),
        ("alias_edges", edges),
        ("feature_bindings", bindings),
    ):
        for index, item in enumerate(values):
            if isinstance(item, dict):
                arrays.append((f"/{group_name}/{index}/evidence_refs", _arr(item.get("evidence_refs"))))
    for index, item in enumerate(decisions):
        if isinstance(item, dict):
            for key in ("assertion_refs", "binding_refs", "reason_codes", "evidence_refs"):
                arrays.append((f"/authority_decisions/{index}/{key}", _arr(item.get(key))))
    for field, values in arrays:
        if not _canonical(values):
            findings.append(Finding("REFS_OR_REASONS_NOT_CANONICAL", field))

    assertion_by_id = {
        item["assertion_id"]: item
        for item in assertions
        if isinstance(item, dict) and isinstance(item.get("assertion_id"), str)
    }
    binding_by_id = {
        item["binding_id"]: item
        for item in bindings
        if isinstance(item, dict) and isinstance(item.get("binding_id"), str)
    }

    directed: list[tuple[str, str]] = []
    disputes: list[frozenset[str]] = []
    supersessions: list[tuple[int, dict[str, Any]]] = []
    for index, edge in enumerate(edges):
        if not isinstance(edge, dict):
            continue
        left, right = edge.get("from_assertion_ref"), edge.get("to_assertion_ref")
        relation = edge.get("relation_type")
        if left not in assertion_set or right not in assertion_set:
            findings.append(Finding("ALIAS_ENDPOINT_UNKNOWN", f"/alias_edges/{index}"))
            continue
        if left == right:
            findings.append(Finding("ALIAS_SELF_REFERENCE", f"/alias_edges/{index}"))
        if edge.get("active") is True and relation not in {"DISPUTES", "UNRESOLVED"}:
            directed.append((left, right))
        if relation == "DISPUTES":
            disputes.append(frozenset((left, right)))
        if relation == "SUPERSEDES":
            supersessions.append((index, edge))
    if _cycle(directed):
        findings.append(Finding("ALIAS_CYCLE", "/alias_edges"))

    recorded_at = _time(provenance.get("recorded_at"))
    for index, assertion in enumerate(assertions):
        if not isinstance(assertion, dict):
            continue
        start, end = _time(assertion.get("valid_from")), _time(assertion.get("valid_to"))
        issued = _time(assertion.get("issued_at"))
        if start and end and start > end:
            findings.append(Finding("TIME_ORDER_INVALID", f"/place_name_assertions/{index}"))
        if issued and recorded_at and issued > recorded_at:
            findings.append(Finding("TIME_ORDER_INVALID", f"/place_name_assertions/{index}/issued_at"))

    unresolved: set[str] = set()
    normalized_features: dict[str, set[str]] = {}
    for index, binding in enumerate(bindings):
        if not isinstance(binding, dict):
            continue
        assertion_ref = binding.get("assertion_ref")
        feature_ref = binding.get("feature_ref")
        if assertion_ref not in assertion_set:
            findings.append(Finding("BINDING_ASSERTION_UNKNOWN", f"/feature_bindings/{index}/assertion_ref"))
            continue
        if binding.get("binding_type") == "UNBOUND":
            if feature_ref is not None or binding.get("confidence_class") != "UNRESOLVED":
                findings.append(Finding("UNBOUND_BINDING_INCONSISTENT", f"/feature_bindings/{index}"))
            unresolved.add(assertion_ref)
        elif feature_ref is None:
            findings.append(Finding("BOUND_BINDING_MISSING_FEATURE", f"/feature_bindings/{index}/feature_ref"))
        elif isinstance(feature_ref, str):
            key = assertion_by_id[assertion_ref].get("normalized_name_key")
            if isinstance(key, str):
                normalized_features.setdefault(key, set()).add(feature_ref)
        start, end = _time(binding.get("valid_from")), _time(binding.get("valid_to"))
        if start and end and start > end:
            findings.append(Finding("TIME_ORDER_INVALID", f"/feature_bindings/{index}"))

    reviewed_homonyms: set[str] = set()
    preserved_disputes: set[frozenset[str]] = set()
    for index, decision in enumerate(decisions):
        if not isinstance(decision, dict):
            continue
        assertion_refs = _arr(decision.get("assertion_refs"))
        binding_refs = _arr(decision.get("binding_refs"))
        if any(ref not in assertion_set for ref in assertion_refs) or any(ref not in binding_set for ref in binding_refs):
            findings.append(Finding("AUTHORITY_DECISION_REF_UNKNOWN", f"/authority_decisions/{index}"))
        supersedes = decision.get("supersedes_decision_ref")
        if supersedes is not None and supersedes not in decision_set:
            findings.append(Finding("AUTHORITY_DECISION_REF_UNKNOWN", f"/authority_decisions/{index}/supersedes_decision_ref"))

        outcome = decision.get("outcome")
        reasons = set(_arr(decision.get("reason_codes")))
        if outcome == "ACCEPT_FOR_USE":
            if any(ref in unresolved for ref in assertion_refs):
                findings.append(Finding("ACCEPTED_NAME_UNRESOLVED", f"/authority_decisions/{index}"))
            for ref in binding_refs:
                binding = binding_by_id.get(ref, {})
                if binding.get("binding_type") in {"UNBOUND", "DISPUTED"} or binding.get("confidence_class") in {"DISPUTED", "UNRESOLVED"}:
                    findings.append(Finding("ACCEPTED_NAME_UNRESOLVED", f"/authority_decisions/{index}"))
                    break
        if "HOMONYM_COLLISION_REVIEWED" in reasons and outcome in {"PROVISIONAL", "HOLD", "ABSTAIN"}:
            for ref in assertion_refs:
                key = assertion_by_id.get(ref, {}).get("normalized_name_key")
                if isinstance(key, str):
                    reviewed_homonyms.add(key)
        if "DISPUTED_NAME_PRESERVED" in reasons and outcome in {"PROVISIONAL", "HOLD", "ABSTAIN"}:
            for pair in disputes:
                if pair.issubset(set(assertion_refs)):
                    preserved_disputes.add(pair)

    for key, features in normalized_features.items():
        if len(features) > 1 and key not in reviewed_homonyms:
            findings.append(Finding("HOMONYM_COLLISION_UNREVIEWED", "/feature_bindings"))
    for pair in disputes:
        if pair not in preserved_disputes:
            findings.append(Finding("DISPUTE_NOT_PRESERVED", "/authority_decisions"))

    for index, edge in supersessions:
        old = assertion_by_id.get(edge.get("from_assertion_ref"), {})
        new = assertion_by_id.get(edge.get("to_assertion_ref"), {})
        effective = _time(edge.get("effective_at"))
        old_end, new_start = _time(old.get("valid_to")), _time(new.get("valid_from"))
        if not effective or not old_end or not new_start or old_end > effective or new_start > effective:
            findings.append(Finding("SUPERSESSION_INCOMPLETE", f"/alias_edges/{index}"))

    flags = (
        "source_admitted", "policy_evaluated", "feature_identity_created",
        "geometry_authority_created", "legal_status_created",
        "ownership_authority_created", "promotion_authorized",
        "release_authorized", "publication_authorized", "public_search_authorized",
    )
    if any(governance.get(field) is not False for field in flags) or governance.get("release_ref") is not None:
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return findings


def validate_candidate(candidate: Mapping[str, Any]) -> Result:
    return Result(tuple(sorted(set(_schema_findings(candidate) + _semantic(candidate)))))


def validate_record(path: Path) -> Result:
    candidate, findings = _read(path)
    return Result(tuple(sorted(set(findings)))) if candidate is None else validate_candidate(candidate)


def _apply_patch(base: Mapping[str, Any], operations: list[Any], recompute_hash: bool = True) -> dict[str, Any]:
    value = copy.deepcopy(dict(base))
    for operation in operations:
        if not isinstance(operation, dict) or operation.get("op") not in {"add", "replace"}:
            raise ValueError("unsupported fixture patch")
        parts = operation.get("path", "").split("/")[1:]
        target: Any = value
        for raw in parts[:-1]:
            token = raw.replace("~1", "/").replace("~0", "~")
            target = target[int(token)] if isinstance(target, list) else target[token]
        token = parts[-1].replace("~1", "/").replace("~0", "~")
        if isinstance(target, list):
            if token == "-":
                target.append(copy.deepcopy(operation.get("value")))
            else:
                target[int(token)] = copy.deepcopy(operation.get("value"))
        else:
            target[token] = copy.deepcopy(operation.get("value"))
    if recompute_hash:
        value["spec_hash"] = _hash(value)
    return value


def _load_profile() -> dict[str, Any]:
    profile, findings = _read(PROFILE)
    if profile is None or findings:
        raise ValueError("fixture profile unavailable")
    return profile


def materialize_fixture(case: Mapping[str, Any], profile: Mapping[str, Any] | None = None) -> dict[str, Any]:
    source = profile or _load_profile()
    base = _obj(source.get("bases")).get(case.get("base"))
    if not isinstance(base, dict):
        raise ValueError("fixture base unavailable")
    return _apply_patch(base, _arr(case.get("patch")), case.get("recompute_hash") is not False)


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _report(path: Path, result: Result) -> str:
    return json.dumps(
        {
            "file": _display(path),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixtures() -> int:
    try:
        profile = _load_profile()
        valid, invalid = _obj(profile.get("valid")), _obj(profile.get("invalid"))
    except ValueError:
        return 1
    passed = bool(valid and invalid)
    for name, case in sorted(valid.items()):
        result = validate_candidate(materialize_fixture(case, profile))
        print(_report(PROFILE.parent / "valid" / name, result))
        passed = passed and result.ok
    for name, case in sorted(invalid.items()):
        candidate = materialize_fixture(case, profile)
        result = validate_candidate(candidate)
        expected = sorted(item for item in _arr(case.get("expected_findings")) if isinstance(item, str))
        actual = sorted({finding.code for finding in result.findings})
        print(_report(PROFILE.parent / "invalid" / name, result))
        if result.ok or not expected or actual != expected:
            passed = False
            print(json.dumps({"file": name, "expected": expected, "actual": actual, "outcome": "FIXTURE_POLARITY_ERROR"}, sort_keys=True), file=sys.stderr)
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return 2 if args.files else run_fixtures()
    if not args.files:
        return 2
    exit_code = 0
    for path in args.files:
        result = validate_record(path)
        print(_report(path, result))
        exit_code = max(exit_code, 0 if result.ok else (2 if result.error else 1))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
