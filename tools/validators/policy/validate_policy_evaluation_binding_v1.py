#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/policy/policy_evaluation_binding_v1.schema.json"
INPUT_SCHEMA = ROOT / "schemas/contracts/v1/policy/policy_input_bundle_profile_v1.schema.json"
DECISION_SCHEMA = ROOT / "schemas/contracts/v1/policy/policy_decision.schema.json"


def _load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _inside(path_text: str) -> Path:
    candidate = (ROOT / path_text).resolve()
    candidate.relative_to(ROOT.resolve())
    if candidate.is_symlink() or not candidate.is_file():
        raise ValueError("bound path must be an existing non-symlink file")
    return candidate


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(binding: dict) -> dict:
    findings: list[dict[str, str]] = []
    schema = _load(SCHEMA)
    for error in sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(binding), key=lambda e: list(e.absolute_path)):
        findings.append({"code": "BINDING_SCHEMA_INVALID", "path": "/" + "/".join(map(str, error.absolute_path))})
    if findings:
        return _result("ERROR", findings)

    try:
        input_path = _inside(binding["input"]["path"])
        decision_path = _inside(binding["decision"]["path"])
        input_value = _load(input_path)
        decision_value = _load(decision_path)
    except (OSError, ValueError, json.JSONDecodeError):
        return _result("ERROR", [{"code": "BOUND_FILE_UNAVAILABLE", "path": "/"}])

    if _sha(input_path) != binding["input"]["sha256"]:
        findings.append({"code": "INPUT_DIGEST_MISMATCH", "path": "/input/sha256"})
    if _sha(decision_path) != binding["decision"]["sha256"]:
        findings.append({"code": "DECISION_DIGEST_MISMATCH", "path": "/decision/sha256"})

    for error in Draft202012Validator(_load(INPUT_SCHEMA), format_checker=FormatChecker()).iter_errors(input_value):
        findings.append({"code": "INPUT_PROFILE_INVALID", "path": "/input"})
        break
    for error in Draft202012Validator(_load(DECISION_SCHEMA), format_checker=FormatChecker()).iter_errors(decision_value):
        findings.append({"code": "DECISION_SCHEMA_INVALID", "path": "/decision"})
        break

    declared = input_value.get("evaluator", {}) if isinstance(input_value, dict) else {}
    evaluator = binding["evaluator"]
    if declared.get("bundle_ref") != evaluator["bundle_ref"] or declared.get("bundle_version") != evaluator["bundle_version"]:
        findings.append({"code": "EVALUATOR_DECLARATION_MISMATCH", "path": "/evaluator"})
    if isinstance(input_value, dict) and input_value.get("governance", {}).get("policy_evaluated") is not False:
        findings.append({"code": "INPUT_AUTHORITY_OVERCLAIM", "path": "/input"})

    return _result("DENY" if findings else "PASS", findings)


def _result(status: str, findings: list[dict[str, str]]) -> dict:
    return {
        "status": status,
        "findings": findings,
        "authority": {
            "policy_evaluated": False,
            "decision_authenticated": False,
            "promotion_authorized": False,
            "release_authorized": False,
            "publication_authorized": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("binding", type=Path)
    args = parser.parse_args()
    try:
        binding = _load(args.binding)
    except (OSError, json.JSONDecodeError):
        result = _result("ERROR", [{"code": "BINDING_UNAVAILABLE", "path": "/"}])
    else:
        result = validate(binding) if isinstance(binding, dict) else _result("ERROR", [{"code": "BINDING_ROOT_INVALID", "path": "/"}])
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["status"] == "PASS" else 2 if result["status"] == "ERROR" else 1


if __name__ == "__main__":
    raise SystemExit(main())
