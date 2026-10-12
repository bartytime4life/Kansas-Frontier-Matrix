#!/usr/bin/env python3
"""Validate fixture-only IndicatorDefinition records."""
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

SCHEMA = ROOT / "schemas/contracts/v1/evidence/indicator_definition.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/indicator_definition/cases.json"
PREFIX = "kfm:indicator-definition:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100

RATE_KINDS = {"RATE", "RATIO", "PERCENT"}
NO_DENOMINATOR_KINDS = {"COUNT", "INDEX", "CATEGORY"}
REQUIRED_LIMITS = {
    "NO_CAUSAL_CLAIM",
    "NO_PUBLICATION_AUTHORITY",
    "NOT_OBSERVATION",
    "NOT_ROOT_TRUTH",
    "SCOPE_BOUND",
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
            return None, (Finding("INDICATOR_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("INDICATOR_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("INDICATOR_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("INDICATOR_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("INDICATOR_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("INDICATOR_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("INDICATOR_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema() -> Mapping[str, Any]:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    validator = Draft202012Validator(_schema())
    findings = {
        Finding("INDICATOR_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in islice(validator.iter_errors(value), MAX_FINDINGS)
    }
    return tuple(sorted(findings))


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = dict(value)
    subject.pop("definition_id", None)
    subject.pop("spec_hash", None)
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.removeprefix("sha256:")[:24]


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    indicator = value["indicator"]
    components = value["components"]
    method = value["method"]
    support = value["support"]
    disclosure = value["disclosure"]
    kind = indicator["value_kind"]

    if method["aggregation"] != kind:
        findings.add(Finding("INDICATOR_AGGREGATION_MISMATCH", "/method/aggregation"))

    component_refs = [item["component_ref"] for item in components]
    if component_refs != sorted(component_refs):
        findings.add(Finding("INDICATOR_COMPONENT_ORDER_INVALID", "/components"))
    if len(component_refs) != len(set(component_refs)):
        findings.add(Finding("INDICATOR_COMPONENT_DUPLICATE", "/components"))
    for index, component in enumerate(components):
        roles = component["allowed_source_roles"]
        if roles != sorted(roles):
            findings.add(Finding("INDICATOR_ROLE_ORDER_INVALID", f"/components/{index}/allowed_source_roles"))

    numerator_count = sum(item["role"] == "NUMERATOR" for item in components)
    denominator_count = sum(item["role"] == "DENOMINATOR" for item in components)
    if kind in RATE_KINDS:
        if method["denominator_policy"] != "REQUIRED":
            findings.add(Finding("INDICATOR_DENOMINATOR_POLICY_MISMATCH", "/method/denominator_policy"))
        if numerator_count < 1:
            findings.add(Finding("INDICATOR_NUMERATOR_REQUIRED", "/components"))
        if denominator_count != 1:
            findings.add(Finding("INDICATOR_DENOMINATOR_REQUIRED", "/components"))
    elif kind in NO_DENOMINATOR_KINDS:
        if method["denominator_policy"] != "NOT_APPLICABLE":
            findings.add(Finding("INDICATOR_DENOMINATOR_POLICY_MISMATCH", "/method/denominator_policy"))
        if denominator_count:
            findings.add(Finding("INDICATOR_DENOMINATOR_UNEXPECTED", "/components"))

    if kind == "INDEX" and method["normalization"] == "NONE":
        findings.add(Finding("INDICATOR_NORMALIZATION_REQUIRED", "/method/normalization"))

    percentile = method["percentile_method"]
    if method["normalization"] == "PERCENTILE_RANK":
        if percentile is None:
            findings.add(Finding("INDICATOR_PERCENTILE_METHOD_REQUIRED", "/method/percentile_method"))
    elif percentile is not None:
        findings.add(Finding("INDICATOR_PERCENTILE_METHOD_UNEXPECTED", "/method/percentile_method"))

    threshold_ref = method["threshold_policy_ref"]
    if kind == "CATEGORY":
        if threshold_ref is None:
            findings.add(Finding("INDICATOR_THRESHOLD_POLICY_REQUIRED", "/method/threshold_policy_ref"))
    elif threshold_ref is not None:
        findings.add(Finding("INDICATOR_THRESHOLD_POLICY_UNEXPECTED", "/method/threshold_policy_ref"))

    duration = support["window_duration"]
    if support["temporal_support_kind"] == "ROLLING_WINDOW":
        if duration is None:
            findings.add(Finding("INDICATOR_WINDOW_DURATION_REQUIRED", "/support/window_duration"))
    elif duration is not None:
        findings.add(Finding("INDICATOR_WINDOW_DURATION_UNEXPECTED", "/support/window_duration"))

    limits = disclosure["interpretation_limits"]
    if limits != sorted(limits):
        findings.add(Finding("INDICATOR_LIMIT_ORDER_INVALID", "/disclosure/interpretation_limits"))
    if not REQUIRED_LIMITS.issubset(set(limits)):
        findings.add(Finding("INDICATOR_REQUIRED_LIMIT_MISSING", "/disclosure/interpretation_limits"))

    try:
        digest, identifier = canonical_identity(value)
    except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
        findings.add(Finding("INDICATOR_IDENTITY_ERROR", "/spec_hash"))
    else:
        if value["spec_hash"] != digest:
            findings.add(Finding("INDICATOR_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["definition_id"] != identifier:
            findings.add(Finding("INDICATOR_DEFINITION_ID_MISMATCH", "/definition_id"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    return Result("PASS", ())


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(replacement)
    else:
        target[key] = copy.deepcopy(replacement)


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in manifest["variants"][case["base"]]:
        _replace(document, mutation["path"], mutation.get("value"))
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["definition_id"] = case.get("definition_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(
        json.dumps(
            {"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures},
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": [
                "no_network",
                "no_formula_execution",
                "no_indicator_computation",
                "no_evidence_resolution",
                "no_policy_evaluation",
                "no_review_approval",
                "no_promotion",
                "no_release",
                "no_public_use",
                "no_publication",
            ],
            "outcome": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = Result("ERROR", findings) if value is None else validate_payload(value)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
