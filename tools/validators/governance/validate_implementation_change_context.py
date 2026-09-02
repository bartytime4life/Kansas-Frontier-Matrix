#!/usr/bin/env python3
"""Build and validate non-authoritative ImplementationChangeContext records.

The profile reads local Git metadata only. It records paths, statuses, line counts,
and deterministic review-attention signals; it never emits raw diff hunks or file
contents. READY means only that the context is internally complete for reviewer use.
HOLD and ERROR fail closed. No result creates evidence, policy, review approval,
repository mutation, promotion, release, deployment, publication, or public-use
authority.
"""
from __future__ import annotations

import argparse
import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.governance.implementation_change_context_git import build_from_git
from tools.validators.governance.implementation_change_context_model import (
    CASES,
    EXIT,
    EXIT_ERROR,
    Evaluation,
    Finding,
    GitContextError,
    evaluate_document,
    evaluate_path,
    expected_context_id,
    expected_summary,
    identity_projection,
    load_json,
    signal_codes,
    signal_score,
)

def _pointer_parts(pointer: object) -> list[str | int]:
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise ValueError("fixture pointer must be an absolute JSON Pointer")
    parts: list[str | int] = []
    for raw_part in pointer[1:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        parts.append(int(part) if part.isdigit() else part)
    return parts


def _fixture_set(document: object, pointer: object, value: object) -> None:
    parts = _pointer_parts(pointer)
    if not parts:
        raise ValueError("fixture root replacement is denied")
    parent = document
    for part in parts[:-1]:
        if isinstance(part, int):
            if not isinstance(parent, list) or part >= len(parent):
                raise ValueError("fixture pointer does not resolve")
            parent = parent[part]
        else:
            if not isinstance(parent, dict) or part not in parent:
                raise ValueError("fixture pointer does not resolve")
            parent = parent[part]
    final = parts[-1]
    if isinstance(final, int):
        if not isinstance(parent, list) or final >= len(parent):
            raise ValueError("fixture pointer does not resolve")
        parent[final] = copy.deepcopy(value)
    else:
        if not isinstance(parent, dict):
            raise ValueError("fixture pointer parent is not an object")
        parent[final] = copy.deepcopy(value)


def _materialize_fixture_case(template: Mapping[str, object], case: Mapping[str, object]) -> dict[str, object]:
    document = copy.deepcopy(dict(template))
    operations = case.get("operations")
    if not isinstance(operations, list):
        raise ValueError("fixture operations must be an array")
    for operation in operations:
        if not isinstance(operation, dict):
            raise ValueError("fixture operation must be an object")
        op = operation.get("op")
        if op == "set":
            _fixture_set(document, operation.get("path"), operation.get("value"))
        elif op == "swap":
            parts = _pointer_parts(operation.get("path"))
            target: object = document
            for part in parts:
                target = target[part] if isinstance(part, int) else target[part]  # type: ignore[index]
            indexes = operation.get("indexes")
            if (
                not isinstance(target, list)
                or not isinstance(indexes, list)
                or len(indexes) != 2
                or not all(isinstance(index, int) and 0 <= index < len(target) for index in indexes)
            ):
                raise ValueError("fixture swap is invalid")
            left, right = indexes
            target[left], target[right] = target[right], target[left]
        elif op == "recompute":
            target = operation.get("target")
            if target == "summary":
                files = document.get("files")
                if not isinstance(files, list) or not all(isinstance(item, dict) for item in files):
                    raise ValueError("fixture files are invalid")
                document["summary"] = expected_summary(files)
            elif target == "context_id":
                document["context_id"] = expected_context_id(document)
            else:
                raise ValueError("fixture recompute target is invalid")
        else:
            raise ValueError("fixture operation is unsupported")
    return document


def load_fixture_cases() -> list[dict[str, object]]:
    manifest = load_json(CASES)
    template = manifest.get("template")
    cases = manifest.get("cases")
    if not isinstance(template, dict) or not isinstance(cases, list):
        raise ValueError("fixture manifest is invalid")
    materialized: list[dict[str, object]] = []
    seen: set[str] = set()
    for case in cases:
        if (
            not isinstance(case, dict)
            or not isinstance(case.get("name"), str)
            or case.get("expected_outcome") not in {"READY", "HOLD", "ERROR"}
        ):
            raise ValueError("fixture case is invalid")
        name = str(case["name"])
        if name in seen:
            raise ValueError("fixture case names must be unique")
        seen.add(name)
        materialized.append(
            {
                "name": name,
                "expected_outcome": case["expected_outcome"],
                "document": _materialize_fixture_case(template, case),
            }
        )
    return materialized


def run_cases() -> tuple[bool, dict[str, object]]:
    try:
        cases = load_fixture_cases()
    except Exception:
        return False, {"outcome": "ERROR", "cases": 0, "mismatches": ["FIXTURE_INPUT_INVALID"]}
    mismatches: list[dict[str, object]] = []
    for case in cases:
        actual = evaluate_document(case["document"]).outcome  # type: ignore[arg-type]
        if actual != case.get("expected_outcome"):
            mismatches.append(
                {
                    "case": case.get("name"),
                    "expected": case.get("expected_outcome"),
                    "actual": actual,
                }
            )
    return not mismatches, {
        "authority": "NONE",
        "outcome": "PASS" if not mismatches else "FAIL",
        "cases": len(cases),
        "mismatches": mismatches,
    }


run_fixture_suite = run_cases


def _evaluation_payload(document: Mapping[str, object] | None, evaluation: Evaluation) -> dict[str, object]:
    summary = document.get("summary") if isinstance(document, dict) else None
    return {
        "authority": "NONE",
        "context_id": document.get("context_id") if isinstance(document, dict) else None,
        "outcome": evaluation.outcome,
        "decision_capture_recommended": summary.get("decision_capture_recommended") if isinstance(summary, dict) else None,
        "findings": [
            {"code": finding.code, "field": finding.field}
            for finding in evaluation.findings
        ],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("context", nargs="?", type=Path)
    parser.add_argument("--cases", action="store_true")
    parser.add_argument("--build-from-git", action="store_true")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--repository")
    parser.add_argument("--base")
    parser.add_argument("--head")
    parser.add_argument("--status", choices=("DRAFT", "READY_FOR_REVIEW"), default="DRAFT")
    parser.add_argument("--decision-ref", action="append", default=[])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    selected = int(args.cases) + int(args.build_from_git) + int(args.context is not None)
    if selected != 1:
        parser.error("choose exactly one of a context file, --cases, or --build-from-git")

    if args.cases:
        ok, payload = run_cases()
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if ok else EXIT_ERROR

    if args.build_from_git:
        if not all((args.repository, args.base, args.head)):
            parser.error("--build-from-git requires --repository, --base, and --head")
        try:
            document = build_from_git(
                args.repo_root,
                repository=args.repository,
                base_ref=args.base,
                head_ref=args.head,
                status=args.status,
                implementation_decision_refs=args.decision_ref,
            )
            evaluation = evaluate_document(document)
        except (GitContextError, OSError, subprocess.SubprocessError):
            payload = {
                "authority": "NONE",
                "outcome": "ERROR",
                "findings": [{"code": "GIT_CONTEXT_INVALID", "field": "$"}],
            }
            print(json.dumps(payload, indent=2, sort_keys=True))
            return EXIT_ERROR
        rendered = json.dumps(document, indent=2, sort_keys=True) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
            print(json.dumps(_evaluation_payload(document, evaluation), indent=2, sort_keys=True))
        else:
            print(rendered, end="")
        return EXIT[evaluation.outcome]

    document, evaluation = evaluate_path(args.context)
    print(json.dumps(_evaluation_payload(document, evaluation), indent=2, sort_keys=True))
    return EXIT[evaluation.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
