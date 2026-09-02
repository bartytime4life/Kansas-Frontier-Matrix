#!/usr/bin/env python3
"""Validate fixture-only LifecycleGateClosureAssessment records."""
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

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/governance/lifecycle_gate_closure_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/governance/lifecycle_gate_closure_assessment/cases.json"
PREFIX = "kfm:lifecycle-gate-closure:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100


STAGES = {
    "ADMISSION": ("DISCOVERED", "RAW"),
    "NORMALIZATION": ("RAW", "WORK"),
    "VALIDATION": ("WORK", "PROCESSED"),
    "CATALOG_CLOSURE": ("PROCESSED", "CATALOG"),
    "RELEASE": ("CATALOG", "PUBLISHED"),
    "CORRECTION": ("PUBLISHED", "PUBLISHED_SUPERSEDED"),
    "ROLLBACK": ("PUBLISHED", "PRIOR_RELEASE"),
}

BASE_ROLES = {
    "ADMISSION": {"PAYLOAD_IDENTITY", "POLICY_DECISION", "SOURCE_DESCRIPTOR"},
    "NORMALIZATION": {"POLICY_DECISION", "TRANSFORM_RECEIPT", "VALIDATION_REPORT"},
    "VALIDATION": {"POLICY_DECISION", "VALIDATION_REPORT"},
    "CATALOG_CLOSURE": {"CATALOG_MATRIX", "EVIDENCE_BUNDLE", "POLICY_DECISION"},
    "RELEASE": {"CORRECTION_PATH", "POLICY_DECISION", "RELEASE_MANIFEST", "ROLLBACK_TARGET"},
    "CORRECTION": {
        "CORRECTION_NOTICE",
        "INVALIDATION_LIST",
        "POLICY_DECISION",
        "RELEASE_MANIFEST",
        "REVIEW_RECORD",
    },
    "ROLLBACK": {
        "CORRECTION_NOTICE",
        "INVALIDATION_LIST",
        "POLICY_DECISION",
        "RELEASE_MANIFEST",
        "ROLLBACK_CARD",
    },
}

FAILURE_DISPOSITIONS = {
    "ADMISSION": "NOT_ADMITTED",
    "NORMALIZATION": "QUARANTINE",
    "VALIDATION": "STAY_WORK",
    "CATALOG_CLOSURE": "HOLD_PROCESSED",
    "RELEASE": "HOLD_CATALOG",
    "CORRECTION": "STALE_STATE_ANNOUNCEMENT",
    "ROLLBACK": "HOLD_CURRENT_RELEASE",
}

DEPENDENCY_ARTIFACT_ROLES = {
    "source_descriptor": "SOURCE_DESCRIPTOR",
    "evidence_bundle": "EVIDENCE_BUNDLE",
    "model_run_receipt": "MODEL_RUN_RECEIPT",
    "policy_decision": "POLICY_DECISION",
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
            return None, (Finding("GATE_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("GATE_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("GATE_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("GATE_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("GATE_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("GATE_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("GATE_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema() -> Mapping[str, Any]:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    validator = Draft202012Validator(_schema(), format_checker=FormatChecker())
    findings = {
        Finding("GATE_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in islice(validator.iter_errors(value), MAX_FINDINGS)
    }
    return tuple(sorted(findings))


def required_artifact_roles(value: Mapping[str, Any]) -> set[str]:
    gate = value["gate"]
    requirements = value["requirements"]
    roles = set(BASE_ROLES[gate])
    if gate == "VALIDATION" and requirements["sensitivity_transform_required"]:
        roles.add("REDACTION_RECEIPT")
    if gate == "VALIDATION" and requirements["aggregation_required"]:
        roles.add("AGGREGATION_RECEIPT")
    if gate == "CATALOG_CLOSURE" and requirements["graph_projection_required"]:
        roles.add("GRAPH_PROJECTION")
    if requirements["model_run_required"]:
        roles.add("MODEL_RUN_RECEIPT")
    if gate == "RELEASE" and requirements["review_required"]:
        roles.add("REVIEW_RECORD")
    return roles


def required_dependencies(value: Mapping[str, Any]) -> set[str]:
    gate = value["gate"]
    required = {"policy_decision"}
    if gate == "ADMISSION":
        required.add("source_descriptor")
    if gate in {"CATALOG_CLOSURE", "RELEASE", "CORRECTION"}:
        required.add("evidence_bundle")
    if value["requirements"]["model_run_required"]:
        required.add("model_run_receipt")
    return required


def _flag_findings(value: Mapping[str, Any]) -> set[Finding]:
    gate = value["gate"]
    requirements = value["requirements"]
    findings: set[Finding] = set()
    allowed = {
        "sensitivity_transform_required": gate == "VALIDATION",
        "aggregation_required": gate == "VALIDATION",
        "graph_projection_required": gate == "CATALOG_CLOSURE",
        "review_required": gate == "RELEASE",
    }
    for field, applicable in allowed.items():
        if requirements[field] and not applicable:
            findings.add(Finding("GATE_REQUIREMENT_FLAG_NOT_APPLICABLE", f"/requirements/{field}"))
    return findings


def _artifact_map(value: Mapping[str, Any]) -> tuple[dict[str, Mapping[str, Any]], set[Finding]]:
    artifacts = value["artifacts"]
    roles = [artifact["role"] for artifact in artifacts]
    findings: set[Finding] = set()
    if len(roles) != len(set(roles)):
        findings.add(Finding("GATE_ARTIFACT_ROLE_DUPLICATE", "/artifacts"))
    if roles != sorted(roles):
        findings.add(Finding("GATE_ARTIFACT_ORDER_INVALID", "/artifacts"))
    mapping = {artifact["role"]: artifact for artifact in artifacts}
    unexpected = set(mapping) - required_artifact_roles(value)
    if unexpected:
        findings.add(Finding("GATE_ARTIFACT_ROLE_UNEXPECTED", "/artifacts"))
    return mapping, findings


def _decision_reasons(value: Mapping[str, Any]) -> tuple[str, ...]:
    if value["assessment_state"] == "ERROR":
        return ("ASSESSMENT_ERROR",)
    artifacts, _ = _artifact_map(value)
    required_roles = required_artifact_roles(value)
    required_deps = required_dependencies(value)
    reasons: set[str] = set()
    if required_roles - set(artifacts):
        reasons.add("MISSING_REQUIRED_ARTIFACT")
    required_artifacts = [artifacts[role] for role in required_roles if role in artifacts]
    if any(item["resolution_state"] == "INVALID" for item in required_artifacts):
        reasons.add("REQUIRED_ARTIFACT_INVALID")
    if any(item["resolution_state"] == "UNRESOLVED" for item in required_artifacts):
        reasons.add("UNRESOLVED_REQUIRED_ARTIFACT")
    dependencies = value["dependencies"]
    if any(dependencies[name] == "INVALID" for name in required_deps):
        reasons.add("DEPENDENCY_INVALID")
    if any(dependencies[name] == "UNRESOLVED" for name in required_deps):
        reasons.add("UNRESOLVED_REQUIRED_DEPENDENCY")
    return tuple(sorted(reasons)) or ("GATE_CLOSURE_COMPLETE",)


def recompute_decision(value: Mapping[str, Any]) -> dict[str, Any]:
    reasons = _decision_reasons(value)
    if reasons == ("ASSESSMENT_ERROR",):
        outcome = "ERROR"
        disposition = "ASSESSMENT_ERROR"
    elif reasons == ("GATE_CLOSURE_COMPLETE",):
        outcome = "ALLOW"
        disposition = "ADVANCE"
    else:
        invalid = bool({"DEPENDENCY_INVALID", "REQUIRED_ARTIFACT_INVALID"} & set(reasons))
        outcome = "DENY" if invalid or value["gate"] == "VALIDATION" else "HOLD"
        disposition = FAILURE_DISPOSITIONS[value["gate"]]
    return {
        "outcome": outcome,
        "disposition": disposition,
        "reason_codes": list(reasons),
        "prior_state_preservation_required": outcome != "ALLOW",
    }


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = dict(value)
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.removeprefix("sha256:")[:24]


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings = _flag_findings(value)
    expected_prior, expected_target = STAGES[value["gate"]]
    if value["prior_stage"] != expected_prior or value["target_stage"] != expected_target:
        findings.add(Finding("GATE_STAGE_MAPPING_MISMATCH", "/gate"))

    artifacts, artifact_findings = _artifact_map(value)
    findings.update(artifact_findings)
    required_deps = required_dependencies(value)
    dependencies = value["dependencies"]
    for name, state in dependencies.items():
        if name not in required_deps and state != "NOT_REQUIRED":
            findings.add(Finding("GATE_DEPENDENCY_REQUIREMENT_MISMATCH", f"/dependencies/{name}"))
        if name in required_deps and state == "NOT_REQUIRED":
            findings.add(Finding("GATE_DEPENDENCY_REQUIREMENT_MISMATCH", f"/dependencies/{name}"))

    for name in required_deps:
        role = DEPENDENCY_ARTIFACT_ROLES[name]
        artifact = artifacts.get(role)
        if artifact is None:
            continue
        state = dependencies[name]
        if state != artifact["resolution_state"]:
            findings.add(Finding("GATE_DEPENDENCY_ARTIFACT_MISMATCH", f"/dependencies/{name}"))

    if value["decision"] != recompute_decision(value):
        findings.add(Finding("GATE_DECISION_MISMATCH", "/decision"))
    try:
        digest, identifier = canonical_identity(value)
    except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
        findings.add(Finding("GATE_IDENTITY_ERROR", "/spec_hash"))
    else:
        if value["spec_hash"] != digest:
            findings.add(Finding("GATE_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != identifier:
            findings.add(Finding("GATE_ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    outcome = value["decision"]["outcome"]
    if outcome == "ALLOW":
        return Result("ALLOW", ())
    return Result(
        outcome,
        tuple(Finding(code, "/decision/outcome") for code in value["decision"]["reason_codes"]),
    )


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
    document = copy.deepcopy(manifest["bases"][case["base"]])
    remove_roles = set(case.get("remove_roles", []))
    if remove_roles:
        document["artifacts"] = [
            artifact for artifact in document["artifacts"] if artifact["role"] not in remove_roles
        ]
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    document["decision"] = copy.deepcopy(case.get("decision_override", recompute_decision(document)))
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["assessment_id"] = case.get("assessment_id_override", identifier)
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
                "no_reference_resolution",
                "no_policy_evaluation",
                "no_lifecycle_write",
                "no_promotion",
                "no_release",
                "no_correction",
                "no_rollback",
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
    return {"ALLOW": 0, "DENY": 1, "ERROR": 2, "HOLD": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
