#!/usr/bin/env python3
"""CLI for bounded, no-network promotion verification execution."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from tools.validators.promotion_gate.execution.common import Finding, canonical_hash, read_json
from tools.validators.promotion_gate.execution.engine import execute as _execute, result_payload

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/promotion_verification_execution.schema.json"
PROMOTION_VALIDATOR = REPO_ROOT / "tools/validators/promotion_gate/validate_promotion_gate.py"
COSIGN_PLAN_VALIDATOR = REPO_ROOT / "tools/validators/release/validate_cosign_attestation_verification_plan.py"


def execute(
    plan: dict[str, object],
    *,
    repo_root: Path,
    cosign_bin: Path,
    conftest_bin: Path,
    promotion_validator: Path,
    cosign_plan_validator: Path,
) -> dict[str, object]:
    """Execute using the repository-owned schema selected by this entry point."""

    return _execute(
        plan,
        repo_root=repo_root,
        schema_path=SCHEMA_PATH,
        cosign_bin=cosign_bin,
        conftest_bin=conftest_bin,
        promotion_validator=promotion_validator,
        cosign_plan_validator=cosign_plan_validator,
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Execute bounded promotion verification without promoting anything.")
    parser.add_argument("execution_plan", type=Path)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--cosign-bin", type=Path, required=True)
    parser.add_argument("--conftest-bin", type=Path, required=True)
    parser.add_argument("--promotion-validator", type=Path, default=PROMOTION_VALIDATOR)
    parser.add_argument("--cosign-plan-validator", type=Path, default=COSIGN_PLAN_VALIDATOR)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    value, findings = read_json(args.execution_plan)
    if findings or not isinstance(value, dict):
        result = result_payload({}, findings or [Finding("EXECUTION_PLAN_INVALID", "/", "ERROR")])
    else:
        result = execute(
            value,
            repo_root=args.repo_root,
            cosign_bin=args.cosign_bin.resolve(),
            conftest_bin=args.conftest_bin.resolve(),
            promotion_validator=args.promotion_validator.resolve(),
            cosign_plan_validator=args.cosign_plan_validator.resolve(),
        )
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["status"] == "PASS" else 2 if result["status"] == "ERROR" else 1


if __name__ == "__main__":
    raise SystemExit(main())

__all__ = ["canonical_hash", "execute", "Finding", "main", "result_payload"]
