#!/usr/bin/env python3
"""
Assert a Rego decision value for a JSON fixture.

This helper runs `opa eval` against a policy bundle/file and verifies that a
decision expression resolves to the expected value.

Example:
  python tools/validators/ecology/assert_rego_decision.py \
    --policy policy/ecology \
    --input tests/fixtures/ecology/policy/publication_allow_timeslice_pass.json \
    --query data.ecology.publication.decision \
    --expected allow
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


def run_opa_eval(policy: Path, input_file: Path, query: str) -> Any:
    opa = shutil.which("opa")
    if opa is None:
        raise RuntimeError("opa executable not found on PATH")

    cmd = [
        opa,
        "eval",
        "--format",
        "json",
        "--data",
        str(policy),
        "--input",
        str(input_file),
        query,
    ]

    proc = subprocess.run(
        cmd,
        check=False,
        capture_output=True,
        text=True,
    )

    if proc.returncode != 0:
        raise RuntimeError(
            "opa eval failed\n"
            f"command: {' '.join(cmd)}\n"
            f"stdout:\n{proc.stdout}\n"
            f"stderr:\n{proc.stderr}"
        )

    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"opa eval returned invalid JSON: {exc}") from exc

    results = payload.get("result", [])
    if not results:
        raise RuntimeError(f"opa eval returned no result for query: {query}")

    expressions = results[0].get("expressions", [])
    if not expressions:
        raise RuntimeError(f"opa eval returned no expressions for query: {query}")

    return expressions[0].get("value")


def normalize_expected(value: str) -> Any:
    """
    Allow simple scalar expectations while preserving JSON-capable assertions.

    Examples:
      --expected allow
      --expected '"allow"'
      --expected true
      --expected '["qa_rejected"]'
    """
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Assert expected Rego decision for a JSON fixture."
    )
    parser.add_argument("--policy", required=True, type=Path)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--query", required=True)
    parser.add_argument("--expected", required=True)
    parser.add_argument(
        "--out",
        type=Path,
        help="Optional path to write assertion result JSON.",
    )
    args = parser.parse_args()

    expected = normalize_expected(args.expected)

    try:
        actual = run_opa_eval(args.policy, args.input, args.query)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    result = {
        "input": str(args.input),
        "policy": str(args.policy),
        "query": args.query,
        "expected": expected,
        "actual": actual,
        "status": "PASS" if actual == expected else "FAIL",
    }

    if actual != expected:
        print(
            "ERROR: Rego decision mismatch\n"
            f"  input:    {args.input}\n"
            f"  policy:   {args.policy}\n"
            f"  query:    {args.query}\n"
            f"  expected: {expected}\n"
            f"  actual:   {actual}",
            file=sys.stderr,
        )

        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(
                json.dumps(result, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )

        return 1

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
