#!/usr/bin/env python3
"""Validate fixture-only GeographyCrosswalk records."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/crosswalks/geography_crosswalk.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/crosswalks/geography_crosswalk/cases.json"
PREFIX = "kfm:geography-crosswalk:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
REQUIRED_LIMITS = {
    "NO_IDENTITY_EQUIVALENCE_INFERENCE",
    "NO_PUBLICATION_AUTHORITY",
    "NO_REVERSE_JOIN_INFERENCE",
    "SOURCE_ROLE_PRESERVED",
    "WEIGHTS_ARE_DECLARATIONS_NOT_MEASUREMENTS",
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
            return None, (Finding("CROSSWALK_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("CROSSWALK_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("CROSSWALK_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("CROSSWALK_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("CROSSWALK_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("CROSSWALK_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("CROSSWALK_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema() -> Mapping[str, Any]:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    validator = Draft202012Validator(_schema(), format_checker=FormatChecker())
    findings = {
        Finding("CROSSWALK_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in islice(validator.iter_errors(value), MAX_FINDINGS)
    }
    return tuple(sorted(findings))


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = dict(value)
    subject.pop("crosswalk_id", None)
    subject.pop("spec_hash", None)
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.removeprefix("sha256:")[:24]


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    scope = value["scope"]
    mappings = value["mappings"]
    support = value["support"]
    disclosure = value["disclosure"]

    if scope["source_geography_version_ref"] == scope["target_geography_version_ref"]:
        findings.add(
            Finding("CROSSWALK_VERSION_PAIR_INVALID", "/scope/target_geography_version_ref")
        )
    valid_from = date.fromisoformat(scope["valid_from"])
    valid_to = date.fromisoformat(scope["valid_to"]) if scope["valid_to"] else None
    if valid_to is not None and valid_to < valid_from:
        findings.add(Finding("CROSSWALK_VALID_INTERVAL_INVALID", "/scope/valid_to"))

    source_digests = [row["source_feature_id_digest"] for row in mappings]
    if source_digests != sorted(source_digests):
        findings.add(Finding("CROSSWALK_ROW_ORDER_INVALID", "/mappings"))
    if len(source_digests) != len(set(source_digests)):
        findings.add(Finding("CROSSWALK_SOURCE_DUPLICATE", "/mappings"))

    target_rows: dict[str, set[int]] = defaultdict(set)
    for index, row in enumerate(mappings):
        path = f"/mappings/{index}"
        targets = row["targets"]
        target_digests = [item["target_feature_id_digest"] for item in targets]
        if target_digests != sorted(target_digests):
            findings.add(Finding("CROSSWALK_TARGET_ORDER_INVALID", f"{path}/targets"))
        if len(target_digests) != len(set(target_digests)):
            findings.add(Finding("CROSSWALK_TARGET_DUPLICATE", f"{path}/targets"))
        for target_digest in target_digests:
            target_rows[target_digest].add(index)

        relation = row["relation"]
        total = sum(item["weight_millionths"] for item in targets)
        reason = row["reason_code"]
        if relation == "EXACT" and not (len(targets) == 1 and total == 1000000):
            findings.add(Finding("CROSSWALK_EXACT_SHAPE_INVALID", path))
        elif relation == "SPLIT":
            if len(targets) < 2:
                findings.add(Finding("CROSSWALK_SPLIT_SHAPE_INVALID", path))
            elif total != 1000000:
                findings.add(Finding("CROSSWALK_SPLIT_WEIGHT_INVALID", f"{path}/targets"))
        elif relation == "MERGE" and not (len(targets) == 1 and total == 1000000):
            findings.add(Finding("CROSSWALK_MERGE_SHAPE_INVALID", path))
        elif relation == "PARTIAL_OVERLAP" and not (targets and 0 < total < 1000000):
            findings.add(Finding("CROSSWALK_PARTIAL_WEIGHT_INVALID", f"{path}/targets"))
        elif relation == "UNMAPPED" and not (
            not targets and reason == "NO_SUPPORTED_TARGET"
        ):
            findings.add(Finding("CROSSWALK_UNMAPPED_SHAPE_INVALID", path))
        if relation != "UNMAPPED" and reason is not None:
            findings.add(Finding("CROSSWALK_REASON_UNEXPECTED", f"{path}/reason_code"))

    merge_rows: set[int] = set()
    for indexes in target_rows.values():
        if len(indexes) > 1:
            merge_rows.update(indexes)
            if all(mappings[index]["relation"] == "MERGE" for index in indexes):
                pass
            else:
                findings.add(Finding("CROSSWALK_TARGET_COLLISION_INVALID", "/mappings"))
    if any(
        row["relation"] == "MERGE" and index not in merge_rows
        for index, row in enumerate(mappings)
    ):
        findings.add(Finding("CROSSWALK_MERGE_GROUP_INVALID", "/mappings"))

    evidence_refs = support["evidence_refs"]
    if evidence_refs != sorted(evidence_refs):
        findings.add(Finding("CROSSWALK_EVIDENCE_ORDER_INVALID", "/support/evidence_refs"))
    limits = disclosure["interpretation_limits"]
    if limits != sorted(limits):
        findings.add(
            Finding("CROSSWALK_LIMIT_ORDER_INVALID", "/disclosure/interpretation_limits")
        )
    if not REQUIRED_LIMITS.issubset(set(limits)):
        findings.add(
            Finding("CROSSWALK_REQUIRED_LIMIT_MISSING", "/disclosure/interpretation_limits")
        )

    try:
        digest, identifier = canonical_identity(value)
    except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
        findings.add(Finding("CROSSWALK_IDENTITY_ERROR", "/spec_hash"))
    else:
        if value["spec_hash"] != digest:
            findings.add(Finding("CROSSWALK_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["crosswalk_id"] != identifier:
            findings.add(Finding("CROSSWALK_ID_MISMATCH", "/crosswalk_id"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    return Result("DENY", semantic_findings) if semantic_findings else Result("PASS", ())


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
    document["crosswalk_id"] = case.get("crosswalk_id_override", identifier)
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
                "no_geography_resolution",
                "no_mapping_execution",
                "no_identity_equivalence",
                "no_evidence_resolution",
                "no_policy_or_review_approval",
                "no_promotion_or_release",
                "no_public_use_or_publication",
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
