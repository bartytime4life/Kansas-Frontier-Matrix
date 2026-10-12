#!/usr/bin/env python3
"""Validate fixture-only FeatureSetManifest records."""
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

SCHEMA = ROOT / "schemas/contracts/v1/evidence/feature_set_manifest.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/feature_set_manifest/cases.json"
PREFIX = "kfm:feature-set-manifest:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100

ANALYTIC_ROLES = {"DERIVED", "INTERPRETIVE", "MODELED"}
RESTRICTED_CLASSES = {"RESTRICTED", "HIGHLY_RESTRICTED"}
REQUIRED_LIMITS = {
    "NO_MODEL_VALIDITY_CLAIM",
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
            return None, (Finding("FEATURE_SET_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("FEATURE_SET_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("FEATURE_SET_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("FEATURE_SET_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("FEATURE_SET_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("FEATURE_SET_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("FEATURE_SET_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema() -> Mapping[str, Any]:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    validator = Draft202012Validator(_schema())
    findings = {
        Finding("FEATURE_SET_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in islice(validator.iter_errors(value), MAX_FINDINGS)
    }
    return tuple(sorted(findings))


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = dict(value)
    subject.pop("manifest_id", None)
    subject.pop("spec_hash", None)
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.removeprefix("sha256:")[:24]


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    context = value["model_context"]
    features = value["features"]
    lineage = value["lineage"]
    disclosure = value["disclosure"]

    feature_keys = [item["feature_key"] for item in features]
    if feature_keys != sorted(feature_keys):
        findings.add(Finding("FEATURE_SET_FEATURE_ORDER_INVALID", "/features"))
    if len(feature_keys) != len(set(feature_keys)):
        findings.add(Finding("FEATURE_SET_FEATURE_DUPLICATE", "/features"))

    semantic_refs = {item["semantic_ref"] for item in features}
    if context["target_ref"] in semantic_refs:
        findings.add(Finding("FEATURE_SET_TARGET_LEAKAGE", "/model_context/target_ref"))

    for index, feature in enumerate(features):
        derivation_ref = feature["derivation_ref"]
        if feature["source_role"] in ANALYTIC_ROLES:
            if derivation_ref is None:
                findings.add(Finding("FEATURE_SET_DERIVATION_REQUIRED", f"/features/{index}/derivation_ref"))
        elif derivation_ref is not None:
            findings.add(Finding("FEATURE_SET_DERIVATION_UNEXPECTED", f"/features/{index}/derivation_ref"))

        imputation_ref = feature["imputation_method_ref"]
        if feature["missing_data_policy"] == "IMPUTE_WITH_METHOD_REF":
            if imputation_ref is None:
                findings.add(Finding("FEATURE_SET_IMPUTATION_METHOD_REQUIRED", f"/features/{index}/imputation_method_ref"))
        elif imputation_ref is not None:
            findings.add(Finding("FEATURE_SET_IMPUTATION_METHOD_UNEXPECTED", f"/features/{index}/imputation_method_ref"))

        policy_ref = feature["policy_profile_ref"]
        if feature["sensitivity_class"] in RESTRICTED_CLASSES:
            if policy_ref is None:
                findings.add(Finding("FEATURE_SET_POLICY_PROFILE_REQUIRED", f"/features/{index}/policy_profile_ref"))
        elif policy_ref is not None:
            findings.add(Finding("FEATURE_SET_POLICY_PROFILE_UNEXPECTED", f"/features/{index}/policy_profile_ref"))

    source_refs = lineage["source_descriptor_refs"]
    if source_refs != sorted(source_refs):
        findings.add(Finding("FEATURE_SET_SOURCE_ORDER_INVALID", "/lineage/source_descriptor_refs"))
    if len(source_refs) != len(set(source_refs)):
        findings.add(Finding("FEATURE_SET_SOURCE_DUPLICATE", "/lineage/source_descriptor_refs"))

    evidence_refs = lineage["evidence_bundle_refs"]
    if evidence_refs != sorted(evidence_refs):
        findings.add(Finding("FEATURE_SET_EVIDENCE_ORDER_INVALID", "/lineage/evidence_bundle_refs"))
    if len(evidence_refs) != len(set(evidence_refs)):
        findings.add(Finding("FEATURE_SET_EVIDENCE_DUPLICATE", "/lineage/evidence_bundle_refs"))

    training_ref = lineage["training_dataset_ref"]
    if context["use_phase"] in {"TRAINING", "BOTH"}:
        if training_ref is None:
            findings.add(Finding("FEATURE_SET_TRAINING_DATASET_REQUIRED", "/lineage/training_dataset_ref"))
    elif training_ref is not None:
        findings.add(Finding("FEATURE_SET_TRAINING_DATASET_UNEXPECTED", "/lineage/training_dataset_ref"))

    limits = disclosure["interpretation_limits"]
    if limits != sorted(limits):
        findings.add(Finding("FEATURE_SET_LIMIT_ORDER_INVALID", "/disclosure/interpretation_limits"))
    if not REQUIRED_LIMITS.issubset(set(limits)):
        findings.add(Finding("FEATURE_SET_REQUIRED_LIMIT_MISSING", "/disclosure/interpretation_limits"))

    try:
        digest, identifier = canonical_identity(value)
    except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
        findings.add(Finding("FEATURE_SET_IDENTITY_ERROR", "/spec_hash"))
    else:
        if value["spec_hash"] != digest:
            findings.add(Finding("FEATURE_SET_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["manifest_id"] != identifier:
            findings.add(Finding("FEATURE_SET_MANIFEST_ID_MISMATCH", "/manifest_id"))
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
    document["manifest_id"] = case.get("manifest_id_override", identifier)
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
                "no_feature_extraction",
                "no_model_execution",
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
