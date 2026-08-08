#!/usr/bin/env python3
"""Validate fixture-only gate override record candidates without network access."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from collections.abc import Sequence
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.governance.gate_override_record_core import (
    Finding,
    JsonInputError,
    ValidationResult,
    load_json_file,
    refresh_identity,
    validate_document,
)

FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/gate_override_record/cases.json"
SCOPE = "governance.gate_override_record_candidate"
NON_EFFECTS = (
    "no_gate_bypass",
    "no_production_signature",
    "no_policy_or_authenticated_review",
    "no_repository_setting_change",
    "no_promotion_release_deployment_or_publication",
)


def validate_file(path: Path) -> ValidationResult:
    try:
        return validate_document(load_json_file(path))
    except JsonInputError:
        return ValidationResult(
            "ERROR", (Finding("OVERRIDE_INPUT_READ_ERROR", "/", "ERROR"),)
        )


def _replace(document: object, pointer: str, value: object) -> None:
    if not pointer.startswith("/"):
        raise ValueError("mutation path must be a JSON Pointer")
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer[1:].split("/")
    ]
    if not parts:
        raise ValueError("root replacement is denied")
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    elif isinstance(target, dict) and final in target:
        target[final] = copy.deepcopy(value)
    else:
        raise ValueError("mutation path does not resolve")


def _mutate(document: object, mutations: object) -> None:
    if not isinstance(mutations, list):
        raise ValueError("mutations must be an array")
    for mutation in mutations:
        if not isinstance(mutation, dict) or mutation.get("op") != "replace":
            raise ValueError("only replace mutations are admitted")
        _replace(document, mutation["path"], mutation["value"])


def load_fixture_cases() -> tuple[list[dict[str, object]], list[str]]:
    try:
        manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        base, definitions = manifest["base_document"], manifest["cases"]
        if not isinstance(base, dict) or not isinstance(definitions, list):
            raise ValueError("invalid fixture manifest")
        cases = []
        for definition in definitions:
            document = copy.deepcopy(base)
            _mutate(document, definition.get("mutations", []))
            if definition.get("refresh_identity", True):
                refresh_identity(document)
            _mutate(document, definition.get("post_identity_mutations", []))
            cases.append(
                {
                    "case_id": definition["case_id"],
                    "expected_outcome": definition["expected_outcome"],
                    "expected_findings": definition["expected_findings"],
                    "document": document,
                }
            )
        return cases, []
    except (
        OSError,
        UnicodeError,
        json.JSONDecodeError,
        KeyError,
        IndexError,
        TypeError,
        ValueError,
    ):
        return [], ["fixture manifest could not be materialized safely"]


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    cases, findings = load_fixture_cases()
    counts = {name: 0 for name in ("PASS", "HOLD", "DENY", "ERROR")}
    mismatches = []
    for case in cases:
        result = validate_document(case["document"])
        counts[result.outcome] += 1
        actual = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        if (
            result.outcome != case["expected_outcome"]
            or actual != case["expected_findings"]
        ):
            mismatches.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    ok = bool(cases) and not findings and not mismatches
    return ok, {
        "authority": "NONE",
        "cases": len(cases),
        "counts": counts,
        "execution_mode": "FIXTURE_ONLY",
        "findings": findings,
        "mismatches": mismatches,
        "non_effects": NON_EFFECTS,
        "outcome": "PASS" if ok else "ERROR",
        "scope": SCOPE,
    }


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix(),
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": NON_EFFECTS,
            "outcome": result.outcome,
            "override_id": result.override_id,
            "scope": SCOPE,
            "spec_hash": result.spec_hash,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 2
    if not args.files:
        parser.error("provide at least one JSON file or --fixtures")
    rank = {"PASS": 0, "HOLD": 1, "DENY": 2, "ERROR": 3}
    exit_code = {"PASS": 0, "DENY": 1, "ERROR": 2, "HOLD": 3}
    highest = "PASS"
    for path in args.files:
        result = validate_file(path)
        print(_serialize(path, result))
        if rank[result.outcome] > rank[highest]:
            highest = result.outcome
    return exit_code[highest]


if __name__ == "__main__":
    raise SystemExit(main())
