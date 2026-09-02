"""Deterministically validate inactive PublicMapMisuseReviewCandidate fixtures.

The result classifies one declaration only. It does not inspect or mutate a map,
resolve references, decide evidence or policy, review, release, or publish.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONTRACT = REPO_ROOT / "contracts/data/public_map_misuse_review.md"
DEFAULT_SCHEMA = REPO_ROOT / "schemas/contracts/v1/data/public_map_misuse_review.schema.json"
DEFAULT_FIXTURES = REPO_ROOT / "fixtures/contracts/v1/data/public_map_misuse_review/cases.json"
MAX_JSON_BYTES = 2 * 1024 * 1024
REQUIRED_DIMENSIONS = {"SELECTIVITY", "FRAMING", "SCALE_PRECISION", "SYMBOLOGY", "OMISSION"}
OUTCOME_RANK = {"PASS": 0, "ABSTAIN": 1, "DENY": 2, "ERROR": 3}


class DuplicateKeyError(ValueError):
    pass


def _pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError("non-finite JSON number")
    return parsed


def load_json(path: Path) -> Any:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"unsafe JSON input: {path}")
    if path.stat().st_size > MAX_JSON_BYTES:
        raise ValueError(f"JSON input exceeds {MAX_JSON_BYTES} bytes: {path}")
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_pairs,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)),
        parse_float=_finite,
    )


def _pointer(path: object) -> str:
    parts = [str(item).replace("~", "~0").replace("/", "~1") for item in path]
    return "/" + "/".join(parts) if parts else "/"


def _utc(value: str) -> bool:
    try:
        return value.endswith("Z") and datetime.fromisoformat(value.replace("Z", "+00:00")).utcoffset().total_seconds() == 0
    except (AttributeError, TypeError, ValueError):
        return False


def _finding(code: str, outcome: str, path: str) -> dict[str, str]:
    return {"code": code, "outcome": outcome, "path": path}


def validate_candidate(candidate: Mapping[str, Any], schema: Mapping[str, Any], contract_bytes: bytes) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(validator.iter_errors(candidate), key=lambda item: (_pointer(item.absolute_path), str(item.validator))):
        findings.append(_finding("SCHEMA_INVALID", "ERROR", _pointer(error.absolute_path)))
    if findings:
        return {"outcome": "ERROR", "findings": findings}

    expected_hash = hashlib.sha256(contract_bytes).hexdigest()
    if candidate["profile_spec_hash"] != expected_hash:
        findings.append(_finding("PROFILE_SPEC_HASH_MISMATCH", "ERROR", "/profile_spec_hash"))
    if not _utc(candidate["observed_at"]):
        findings.append(_finding("OBSERVED_AT_NOT_UTC", "ERROR", "/observed_at"))

    map_candidate = candidate["map_candidate"]
    dependencies = candidate["dependency_refs"]
    unresolved = [
        map_candidate["purpose"]["resolution"],
        map_candidate["evidence_scope"]["resolution"],
        *(value["resolution"] for value in dependencies.values()),
    ]
    if "UNRESOLVED" in unresolved:
        findings.append(_finding("PREREQUISITE_UNRESOLVED", "ABSTAIN", "/dependency_refs"))

    checks = candidate["checks"]
    if [check["check_id"] for check in checks] != sorted(check["check_id"] for check in checks):
        findings.append(_finding("CHECK_ORDER_NONCANONICAL", "DENY", "/checks"))
    dimensions = [check["dimension"] for check in checks]
    if set(dimensions) != REQUIRED_DIMENSIONS or len(dimensions) != len(set(dimensions)):
        findings.append(_finding("REVIEW_DIMENSION_COVERAGE_INCOMPLETE", "DENY", "/checks"))

    has_unknown = False
    has_concern = False
    for index, check in enumerate(checks):
        base = f"/checks/{index}"
        for field in ("evidence_refs", "review_refs"):
            values = check[field]
            if values != sorted(values):
                findings.append(_finding("REFERENCE_ORDER_NONCANONICAL", "DENY", f"{base}/{field}"))
        if check["state"] == "UNKNOWN" or check["materiality"] == "UNKNOWN":
            has_unknown = True
        if check["state"] == "CLEAR" and check["finding_code"] != "NONE":
            findings.append(_finding("CLEAR_CHECK_HAS_FINDING", "DENY", base))
        if check["state"] == "CONCERN":
            has_concern = True
            findings.append(_finding("MAP_COMMUNICATION_CONCERN", "DENY", base))
            if check["finding_code"] == "NONE":
                findings.append(_finding("CONCERN_WITHOUT_FINDING", "DENY", base))
            if check["materiality"] == "MATERIAL":
                if check["disclosure_surface"] == "NONE":
                    findings.append(_finding("MATERIAL_CONCERN_UNDISCLOSED", "DENY", f"{base}/disclosure_surface"))
                if check["remediation_ref"] is None:
                    findings.append(_finding("MATERIAL_CONCERN_WITHOUT_REMEDIATION", "DENY", f"{base}/remediation_ref"))
                if not check["review_refs"]:
                    findings.append(_finding("MATERIAL_CONCERN_WITHOUT_REVIEW", "DENY", f"{base}/review_refs"))
        if map_candidate["consequence_tier"] == "HIGH" and not check["review_refs"]:
            findings.append(_finding("HIGH_CONSEQUENCE_REVIEW_REF_MISSING", "DENY", f"{base}/review_refs"))

    conclusion = candidate["conclusion"]
    incomplete = conclusion["completeness"] != "COMPLETE"
    if has_unknown or incomplete:
        findings.append(_finding("REVIEW_INCOMPLETE", "ABSTAIN", "/conclusion"))

    preliminary = max((item["outcome"] for item in findings), key=lambda value: OUTCOME_RANK[value], default="PASS")
    expected_declared = "DENY" if has_concern or preliminary == "DENY" else "HOLD" if preliminary == "ABSTAIN" else "READY_FOR_REVIEW"
    if conclusion["declared_outcome"] != expected_declared:
        findings.append(_finding("DECLARED_OUTCOME_INCOHERENT", "DENY", "/conclusion/declared_outcome"))

    outcome = max((item["outcome"] for item in findings), key=lambda value: OUTCOME_RANK[value], default="PASS")
    return {"outcome": outcome, "findings": sorted(findings, key=lambda item: (item["path"], item["code"]))}


def _set_pointer(document: Any, pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.strip("/").split("/") if part]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    last = parts[-1]
    if isinstance(target, list):
        target[int(last)] = value
    else:
        target[last] = value


def _delete_pointer(document: Any, pointer: str) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.strip("/").split("/") if part]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    last = parts[-1]
    if isinstance(target, list):
        del target[int(last)]
    else:
        del target[last]


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(manifest["base_candidate"])
    for pointer, value in case.get("set", {}).items():
        _set_pointer(candidate, pointer, value)
    for pointer in case.get("delete", []):
        _delete_pointer(candidate, pointer)
    return candidate


def validate_fixture_manifest(manifest: Mapping[str, Any], schema: Mapping[str, Any], contract_bytes: bytes) -> list[dict[str, Any]]:
    results = []
    for case in manifest["cases"]:
        result = validate_candidate(materialize_case(manifest, case), schema, contract_bytes)
        result.update({"case_id": case["case_id"], "expected_outcome": case["expected_outcome"]})
        results.append(result)
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--fixtures", nargs="?", const=DEFAULT_FIXTURES, type=Path)
    parser.add_argument("--candidate", type=Path)
    args = parser.parse_args(argv)
    if bool(args.fixtures) == bool(args.candidate):
        parser.error("select exactly one of --fixtures or --candidate")
    contract_bytes = args.contract.read_bytes()
    schema = load_json(args.schema)
    if args.fixtures:
        manifest = load_json(args.fixtures)
        results = validate_fixture_manifest(manifest, schema, contract_bytes)
        mismatches = [item for item in results if item["outcome"] != item["expected_outcome"]]
        print(json.dumps({"profile": manifest["profile"], "case_count": len(results), "mismatch_count": len(mismatches), "results": results}, sort_keys=True))
        return 1 if mismatches else 0
    result = validate_candidate(load_json(args.candidate), schema, contract_bytes)
    print(json.dumps(result, sort_keys=True))
    return 0 if result["outcome"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
