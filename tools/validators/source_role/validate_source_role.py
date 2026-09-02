#!/usr/bin/env python3
"""Validate source-role preservation and anti-collapse requests without network access."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.source_role.source_role_core import (  # noqa: E402
    BASE_PATH,
    CASES_PATH,
    EXIT_CODES,
    expected_request_id,
    load_json,
)
from tools.validators.source_role.source_role_rules import evaluate_path, evaluate_document  # noqa: E402


def _pointer_parts(value: object) -> list[str]:
    if not isinstance(value, str) or not value.startswith("/"):
        raise ValueError("mutation path must be an absolute JSON pointer")
    if value == "/":
        return []
    return [part.replace("~1", "/").replace("~0", "~") for part in value[1:].split("/")]


def _apply(document: dict[str, Any], mutation: Mapping[str, Any]) -> None:
    parts = _pointer_parts(mutation.get("path"))
    if not parts:
        raise ValueError("root replacement is not supported")
    target: Any = document
    for part in parts[:-1]:
        if not isinstance(target, dict) or part not in target:
            raise ValueError("mutation path does not resolve")
        target = target[part]
    if not isinstance(target, dict):
        raise ValueError("mutation parent must be an object")
    leaf = parts[-1]
    if mutation.get("op") == "set":
        target[leaf] = copy.deepcopy(mutation.get("value"))
    elif mutation.get("op") == "remove":
        del target[leaf]
    else:
        raise ValueError("unsupported mutation operation")


def load_fixture_cases() -> list[dict[str, Any]]:
    base = load_json(BASE_PATH)
    manifest = load_json(CASES_PATH)
    raw_cases = manifest.get("cases")
    if not isinstance(raw_cases, list):
        raise ValueError("fixture manifest requires cases")
    cases: list[dict[str, Any]] = []
    for raw in raw_cases:
        if not isinstance(raw, dict) or not isinstance(raw.get("name"), str):
            raise ValueError("invalid fixture case")
        packet = copy.deepcopy(base)
        for mutation in raw.get("mutations", []):
            if not isinstance(mutation, dict):
                raise ValueError("invalid fixture mutation")
            _apply(packet, mutation)
        if raw.get("recompute_request_id", True):
            packet["use"]["request_id"] = expected_request_id(packet)
        else:
            packet["use"]["request_id"] = raw["request_id_override"]
        cases.append({
            "name": raw["name"],
            "packet": packet,
            "expected_outcome": raw.get("expected_outcome"),
            "expected_findings": sorted(raw.get("expected_findings", [])),
        })
    return cases


def run_fixture_suite() -> tuple[bool, dict[str, Any]]:
    try:
        cases = load_fixture_cases()
    except Exception:
        return False, {"profile": "kfm.source-role-use.fixtures.v1", "outcome": "ERROR", "cases": 0, "mismatches": ["FIXTURE_INPUT_INVALID"]}
    mismatches: list[dict[str, Any]] = []
    for case in cases:
        evaluation = evaluate_document(case["packet"])
        actual_codes = sorted({finding.code for finding in evaluation.findings})
        if evaluation.outcome != case["expected_outcome"] or actual_codes != case["expected_findings"]:
            mismatches.append({
                "case": case["name"],
                "expected": {"outcome": case["expected_outcome"], "findings": case["expected_findings"]},
                "actual": {"outcome": evaluation.outcome, "findings": actual_codes},
            })
    return not mismatches, {
        "profile": "kfm.source-role-use.fixtures.v1",
        "outcome": "PASS" if not mismatches else "FAIL",
        "cases": len(cases),
        "mismatches": mismatches,
        "authority_created": False,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true", help="replay exact synthetic fixture outcomes")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures:
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 2
    if not args.paths:
        _parser().error("provide at least one path or --fixtures")
    evaluations = [evaluate_path(path) for path in args.paths]
    payload: Any = evaluations[0].report if len(evaluations) == 1 else [item.report for item in evaluations]
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    return max(EXIT_CODES[item.outcome] for item in evaluations)


if __name__ == "__main__":
    raise SystemExit(main())
