#!/usr/bin/env python3
"""Validate deterministic fixture-only GateOutcomeMapping records."""
from __future__ import annotations

import argparse
import copy
import hmac
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
sys.path.insert(0, str(HASHING_SRC))

from hashing import compute_spec_hash

SCHEMA = REPO_ROOT / "schemas/contracts/v1/governance/gate_outcome_mapping.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/governance/gate_outcome_mapping/cases.json"


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]


def _json_pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("mapping_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_mapping_id(spec_hash: str) -> str:
    return f"kfm:gate-outcome-mapping:{spec_hash.removeprefix('sha256:')[:24]}"


def _expected_mapping(target_surface: str, gate_state: str) -> dict[str, Any]:
    if gate_state == "PASS":
        if target_surface == "PROMOTION":
            return {
                "destination_contract": "PromotionDecision",
                "outcome": "APPROVE",
                "reason_codes": ["GATE_PASS_APPROVE"],
            }
        return {
            "destination_contract": "DecisionEnvelope",
            "outcome": "ANSWER",
            "reason_codes": ["GATE_PASS_ANSWER"],
        }
    if gate_state == "FAIL":
        return {
            "destination_contract": (
                "PromotionDecision" if target_surface == "PROMOTION" else "DecisionEnvelope"
            ),
            "outcome": "DENY",
            "reason_codes": ["GATE_FAILURE_DENY"],
        }
    if gate_state == "INSUFFICIENT_EVIDENCE":
        return {
            "destination_contract": (
                "PromotionDecision" if target_surface == "PROMOTION" else "DecisionEnvelope"
            ),
            "outcome": "ABSTAIN",
            "reason_codes": ["GATE_EVIDENCE_INSUFFICIENT"],
        }
    return {
        "destination_contract": "DecisionEnvelope",
        "outcome": "ERROR",
        "reason_codes": ["GATE_EXECUTION_ERROR"],
    }


def _terminal_result(gate_state: str) -> ValidationResult:
    if gate_state == "PASS":
        return ValidationResult("PASS", ())
    if gate_state == "FAIL":
        return ValidationResult("DENY", (Finding("GATE_FAILURE_DENY", "/mapped/outcome"),))
    if gate_state == "INSUFFICIENT_EVIDENCE":
        return ValidationResult(
            "ABSTAIN",
            (Finding("GATE_EVIDENCE_INSUFFICIENT", "/mapped/outcome"),),
        )
    return ValidationResult("ERROR", (Finding("GATE_EXECUTION_ERROR", "/mapped/outcome"),))


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _evidence_finding(document: Mapping[str, Any]) -> Finding | None:
    gate = document["gate"]
    state = gate["state"]
    evidence_state = gate["evidence_state"]
    evidence_ref = gate["evidence_bundle_ref"]

    if state in {"PASS", "FAIL"}:
        if evidence_state != "RESOLVED":
            return Finding("GATE_EVIDENCE_STATE_INCONSISTENT", "/gate/evidence_state")
        if evidence_ref is None:
            return Finding("GATE_EVIDENCE_REF_REQUIRED", "/gate/evidence_bundle_ref")
        return None

    expected_state = "UNRESOLVED" if state == "INSUFFICIENT_EVIDENCE" else "ERROR"
    if evidence_state != expected_state:
        return Finding("GATE_EVIDENCE_STATE_INCONSISTENT", "/gate/evidence_state")
    if evidence_ref is not None:
        return Finding("GATE_EVIDENCE_REF_FORBIDDEN", "/gate/evidence_bundle_ref")
    return None


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_json_pointer(error.absolute_path), str(error.validator)),
    )
    if errors:
        return ValidationResult(
            "DENY",
            (Finding("GATE_MAPPING_SCHEMA_INVALID", _json_pointer(errors[0].absolute_path)),),
        )

    evidence_finding = _evidence_finding(document)
    if evidence_finding is not None:
        return ValidationResult("DENY", (evidence_finding,))

    expected = _expected_mapping(document["target_surface"], document["gate"]["state"])
    if document["mapped"] != expected:
        return ValidationResult(
            "DENY",
            (Finding("GATE_MAPPING_RESULT_MISMATCH", "/mapped"),),
        )

    actual_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], actual_hash):
        return ValidationResult(
            "DENY",
            (Finding("GATE_MAPPING_SPEC_HASH_MISMATCH", "/spec_hash"),),
        )

    actual_id = expected_mapping_id(actual_hash)
    if not hmac.compare_digest(document["mapping_id"], actual_id):
        return ValidationResult(
            "DENY",
            (Finding("GATE_MAPPING_ID_MISMATCH", "/mapping_id"),),
        )

    return _terminal_result(document["gate"]["state"])


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    if not pointer.startswith("/"):
        raise ValueError("fixture mutation path must be an absolute JSON pointer")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[part]
    cursor[parts[-1]] = value


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])

    document["mapped"] = _expected_mapping(document["target_surface"], document["gate"]["state"])
    if "mapped_override" in case:
        document["mapped"] = copy.deepcopy(case["mapped_override"])

    document["spec_hash"] = expected_spec_hash(document)
    document["mapping_id"] = expected_mapping_id(document["spec_hash"])

    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "mapping_id_override" in case:
        document["mapping_id"] = case["mapping_id_override"]
    return document


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual_findings = [{"code": finding.code, "path": finding.path} for finding in result.findings]
        if result.outcome != case["expected_outcome"] or actual_findings != case["expected_findings"]:
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual_findings,
                }
            )
    print(
        json.dumps(
            {
                "cases": len(manifest["cases"]),
                "failures": failures,
                "suite_match": not failures,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def _load_document(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("mapping root must be a JSON object")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.path is None:
        raise SystemExit("path is required unless --fixtures is used")
    result = validate_payload(_load_document(args.path))
    print(
        json.dumps(
            {
                "outcome": result.outcome,
                "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
