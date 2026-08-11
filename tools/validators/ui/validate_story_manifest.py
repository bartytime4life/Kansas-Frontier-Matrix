#!/usr/bin/env python3
"""Validate the closed, fixture-only StoryManifest composite profile."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/ui/story_manifest.schema.json"
FIXTURES = ROOT / "fixtures/ui/story_manifest/cases.json"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
PREFIX = "kfm:story-manifest:"

STATE_RANK = {
    "READY": 0,
    "PARTIAL": 1,
    "ABSTAINED": 2,
    "SUPERSEDED": 3,
    "BLOCKED": 4,
    "ERROR": 5,
}
OUTCOME_FOR_STATE = {
    "READY": "ANSWER",
    "PARTIAL": "ABSTAIN",
    "ABSTAINED": "ABSTAIN",
    "SUPERSEDED": "ABSTAIN",
    "BLOCKED": "DENY",
    "ERROR": "ERROR",
}
TRUST_ORDER = {
    "rights": ["CLEARED", "GENERALIZED", "WITHHELD", "UNRESOLVED"],
    "sensitivity": ["PUBLIC", "GENERALIZED", "RESTRICTED", "UNKNOWN"],
    "policy": ["ALLOW", "ABSTAIN", "DENY", "ERROR"],
    "review": ["REVIEWED", "NOT_APPLICABLE", "PENDING"],
    "release": ["RELEASED", "UNRELEASED", "WITHDRAWN"],
    "freshness": ["CURRENT", "STALE", "UNKNOWN"],
    "correction": ["NONE", "CURRENT", "CORRECTED", "SUPERSEDED"],
}
READY_SUPPORT = {
    "evidence_bundle_refs",
    "citation_validation_refs",
    "policy_decision_refs",
    "release_refs",
    "review_refs",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
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
            return None, (Finding("STORY_MANIFEST_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("STORY_MANIFEST_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("STORY_MANIFEST_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("STORY_MANIFEST_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("STORY_MANIFEST_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("STORY_MANIFEST_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("STORY_MANIFEST_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema() -> Mapping[str, Any]:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    validator = Draft202012Validator(_schema())
    findings = {
        Finding("STORY_MANIFEST_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in islice(validator.iter_errors(value), MAX_FINDINGS)
    }
    return tuple(sorted(findings))


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = copy.deepcopy(dict(value))
    subject.pop("id", None)
    subject.pop("spec_hash", None)
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.removeprefix("sha256:")[:24]


def _trust_required_state(trust: Mapping[str, str]) -> str:
    if trust["policy"] == "ERROR":
        return "ERROR"
    if trust["correction"] == "SUPERSEDED" and trust["release"] == "WITHDRAWN":
        return "SUPERSEDED"
    if (
        trust["policy"] == "DENY"
        or trust["rights"] in {"WITHHELD", "UNRESOLVED"}
        or trust["sensitivity"] in {"RESTRICTED", "UNKNOWN"}
        or trust["release"] == "WITHDRAWN"
    ):
        return "BLOCKED"
    if (
        trust["policy"] == "ABSTAIN"
        or trust["rights"] == "GENERALIZED"
        or trust["sensitivity"] == "GENERALIZED"
        or trust["review"] == "PENDING"
        or trust["release"] == "UNRELEASED"
        or trust["freshness"] in {"STALE", "UNKNOWN"}
    ):
        return "PARTIAL"
    return "READY"


def _effective_state(node: Mapping[str, Any]) -> str:
    required = _trust_required_state(node["trust_state"])
    return max((node["state"], required), key=STATE_RANK.__getitem__)


def _composite_trust(nodes: Sequence[Mapping[str, Any]]) -> dict[str, str]:
    result: dict[str, str] = {}
    for dimension, order in TRUST_ORDER.items():
        rank = {value: index for index, value in enumerate(order)}
        result[dimension] = max(
            (node["trust_state"][dimension] for node in nodes),
            key=rank.__getitem__,
        )
    return result


def _sorted_unique(values: Sequence[str]) -> bool:
    return list(values) == sorted(set(values))


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    nodes = value["constituents"]

    order = [node["order_index"] for node in nodes]
    refs = [node["node_ref"] for node in nodes]
    if order != sorted(order) or len(order) != len(set(order)):
        findings.add(Finding("STORY_MANIFEST_CONSTITUENT_ORDER_INVALID", "/constituents"))
    if len(refs) != len(set(refs)):
        findings.add(Finding("STORY_MANIFEST_CONSTITUENT_REF_DUPLICATE", "/constituents"))

    effective: list[str] = []
    for index, node in enumerate(nodes):
        required = _trust_required_state(node["trust_state"])
        current = _effective_state(node)
        effective.append(current)
        if STATE_RANK[node["state"]] < STATE_RANK[required]:
            findings.add(
                Finding(
                    "STORY_MANIFEST_CONSTITUENT_TOO_PERMISSIVE",
                    f"/constituents/{index}/state",
                )
            )
        if node["outcome"] != OUTCOME_FOR_STATE[node["state"]]:
            findings.add(
                Finding(
                    "STORY_MANIFEST_CONSTITUENT_OUTCOME_MISMATCH",
                    f"/constituents/{index}/outcome",
                )
            )

    worst = max(effective, key=STATE_RANK.__getitem__)
    worst_rank = STATE_RANK[worst]
    limiting = sorted(
        node["node_ref"]
        for node, state in zip(nodes, effective)
        if STATE_RANK[state] == worst_rank
    )
    reasons = (
        ["SUPPORTED"]
        if worst == "READY"
        else sorted(
            {
                node["reason_code"]
                for node, state in zip(nodes, effective)
                if STATE_RANK[state] == worst_rank
            }
        )
    )
    if value["state"] != worst:
        findings.add(Finding("STORY_MANIFEST_STATE_MISMATCH", "/state"))
    if value["outcome"] != OUTCOME_FOR_STATE[worst]:
        findings.add(Finding("STORY_MANIFEST_OUTCOME_MISMATCH", "/outcome"))
    if value["limiting_node_refs"] != ([] if worst == "READY" else limiting):
        findings.add(Finding("STORY_MANIFEST_LIMITING_REFS_MISMATCH", "/limiting_node_refs"))
    if value["reason_codes"] != reasons:
        findings.add(Finding("STORY_MANIFEST_REASON_CODES_MISMATCH", "/reason_codes"))

    expected_trust = _composite_trust(nodes)
    for dimension, expected in expected_trust.items():
        if value["trust_state"][dimension] != expected:
            findings.add(
                Finding(
                    "STORY_MANIFEST_TRUST_REDUCTION_MISMATCH",
                    f"/trust_state/{dimension}",
                )
            )

    support = value["support"]
    for field, refs_for_field in support.items():
        if isinstance(refs_for_field, list) and not _sorted_unique(refs_for_field):
            findings.add(Finding("STORY_MANIFEST_SUPPORT_REFS_UNSORTED", f"/support/{field}"))
    if not _sorted_unique(value["caveats"]):
        findings.add(Finding("STORY_MANIFEST_CAVEATS_UNSORTED", "/caveats"))
    if not _sorted_unique(value["reason_codes"]):
        findings.add(Finding("STORY_MANIFEST_REASON_CODES_UNSORTED", "/reason_codes"))
    if not _sorted_unique(value["limiting_node_refs"]):
        findings.add(Finding("STORY_MANIFEST_LIMITING_REFS_UNSORTED", "/limiting_node_refs"))

    if value["state"] == "READY":
        for field in sorted(READY_SUPPORT):
            if not support[field]:
                findings.add(Finding("STORY_MANIFEST_READY_SUPPORT_REQUIRED", f"/support/{field}"))

    correction_state = value["trust_state"]["correction"]
    release_state = value["trust_state"]["release"]
    needs_correction = correction_state in {"CORRECTED", "SUPERSEDED"} or release_state == "WITHDRAWN"
    if needs_correction and not support["correction_refs"]:
        findings.add(Finding("STORY_MANIFEST_CORRECTION_REFS_REQUIRED", "/support/correction_refs"))
    needs_supersession = value["state"] == "SUPERSEDED" or release_state == "WITHDRAWN"
    supersession = value.get("supersession")
    if needs_supersession and supersession is None:
        findings.add(Finding("STORY_MANIFEST_SUPERSESSION_REQUIRED", "/supersession"))
    if not needs_supersession and supersession is not None:
        findings.add(Finding("STORY_MANIFEST_SUPERSESSION_DENIED", "/supersession"))
    if supersession is not None and supersession["replacement_manifest_ref"] == value["id"]:
        findings.add(Finding("STORY_MANIFEST_SUPERSESSION_SELF_REFERENCE", "/supersession/replacement_manifest_ref"))

    try:
        expected_hash, expected_id = canonical_identity(value)
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("STORY_MANIFEST_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["id"] != expected_id:
            findings.add(Finding("STORY_MANIFEST_ID_MISMATCH", "/id"))
    except CanonicalizationFailure:
        findings.add(Finding("STORY_MANIFEST_CANONICALIZATION_FAILED", "/"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    findings = _semantic_findings(value)
    return Result("PASS" if not findings else "DENY", findings)


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def _apply(document: Any, mutation: Mapping[str, Any]) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in mutation["path"].split("/")[1:]]
    target = document
    for raw in parts[:-1]:
        target = target[int(raw)] if isinstance(target, list) else target[raw]
    key = parts[-1]
    if mutation.get("remove"):
        if isinstance(target, list):
            del target[int(key)]
        else:
            target.pop(key, None)
    elif isinstance(target, list):
        target[int(key)] = copy.deepcopy(mutation["value"])
    else:
        target[key] = copy.deepcopy(mutation["value"])


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for name in case.get("variants", []):
        for mutation in manifest["variants"][name]:
            _apply(document, mutation)
    for mutation in case.get("mutations", []):
        _apply(document, mutation)
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = digest
    document["id"] = identifier
    for mutation in case.get("post_identity_mutations", []):
        _apply(document, mutation)
    return document


def run_fixtures() -> tuple[bool, list[dict[str, Any]]]:
    manifest = load_fixtures()
    rows: list[dict[str, Any]] = []
    suite_match = True
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        match = result.outcome == case["expected_outcome"] and actual == case["expected_findings"]
        suite_match = suite_match and match
        rows.append({"case_id": case["case_id"], "outcome": result.outcome, "findings": actual, "match": match})
    return suite_match, rows


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "input": None if path is None else str(path),
            "outcome": result.outcome,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": [
                "no_ref_resolution",
                "no_truth_determination",
                "no_policy_execution",
                "no_review_or_release_approval",
                "no_publication",
            ],
        },
        indent=2,
        sort_keys=True,
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        suite_match, rows = run_fixtures()
        print(json.dumps({"authority": "NONE", "cases": len(rows), "execution_mode": "FIXTURE_ONLY", "rows": rows, "suite_match": suite_match}, indent=2, sort_keys=True))
        return 0 if suite_match else 1
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    value, read_findings = _read(args.path)
    result = Result("DENY", read_findings) if value is None else validate_payload(value)
    print(serialize(args.path, result))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
