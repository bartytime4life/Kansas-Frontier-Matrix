#!/usr/bin/env python3
"""Deterministic, no-network KFM repository-control evaluator.

The tracked state is strict JSON stored with a ``.yaml`` extension (valid YAML
1.2). This command verifies the state digest, compares a prepared pull-request
context with one bounded claim, and emits the registered CI outcome vocabulary.
It does not read GitHub, change settings, review, merge, release, or publish.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.repository_control._evaluate import evaluate, make_outcome
from tools.validators.repository_control._model import InputError, compute_state_digest, load_json
from tools.validators.repository_control._state import validate_state_shape

# Re-export the public API used by tests and future adapters.
__all__ = [
    "InputError", "compute_state_digest", "evaluate", "load_json",
    "make_outcome", "validate_state_shape",
]

def _exit(outcome: str) -> int:
    return {"PASS": 0, "NOT_APPLICABLE": 0, "SKIPPED_EXPLICIT": 0, "REGRESSION": 1, "UNKNOWN": 2, "EXPECTED_READINESS_HOLD": 3}[outcome]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("digest", "validate-state"):
        command = commands.add_parser(name)
        command.add_argument("--state", type=Path, required=True)
    command = commands.add_parser("evaluate")
    command.add_argument("--state", type=Path, required=True)
    command.add_argument("--context", type=Path, required=True)
    command.add_argument("--outcome-json", type=Path)
    args = parser.parse_args(argv)
    try:
        state = load_json(args.state)
    except InputError as exc:
        print(f"REGRESSION: STATE_INPUT_INVALID\n{exc}", file=sys.stderr)
        return 1
    if args.command == "digest":
        print(compute_state_digest(state))
        return 0
    invalid = validate_state_shape(state)
    if args.command == "validate-state":
        if invalid:
            for finding in invalid:
                print(f"{finding.code}: {finding.message}", file=sys.stderr)
            return 1
        print("PASS: STATE_VALID")
        return 0
    try:
        context = load_json(args.context)
    except InputError as exc:
        print(f"REGRESSION: CONTEXT_INPUT_INVALID\n{exc}", file=sys.stderr)
        return 1
    evaluation = evaluate(state, context)
    outcome = make_outcome(state, context, evaluation)
    print(f"{evaluation.outcome_class}: {evaluation.reason_code}")
    print(evaluation.summary)
    for finding in evaluation.findings:
        print(f"- {finding.code}: {finding.message}")
    print(json.dumps(outcome, sort_keys=True, separators=(",", ":"), ensure_ascii=False))
    if args.outcome_json:
        args.outcome_json.parent.mkdir(parents=True, exist_ok=True)
        args.outcome_json.write_text(json.dumps(outcome, indent=2) + "\n", encoding="utf-8")
    return _exit(evaluation.outcome_class)


if __name__ == "__main__":
    raise SystemExit(main())
