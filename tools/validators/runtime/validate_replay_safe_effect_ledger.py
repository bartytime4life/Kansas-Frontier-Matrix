"""Validate synthetic replay-safe event/effect ledger candidates; PASS grants no authority."""
from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.runtime.replay_safe_effect_ledger_core import (
    FIXTURE_ROOT,
    MANIFEST_PATH,
    SCOPE,
    Finding,
    ValidationResult,
    load_candidate,
    schema_findings,
)
from tools.validators.runtime.replay_safe_effect_ledger_fixture_expectations import (
    evaluate_fixture_expectation,
)
from tools.validators.runtime.replay_safe_effect_ledger_semantics import semantic_findings


@dataclass(frozen=True)
class StagedValidationResult:
    """A validation result plus the furthest validation stage safely reached."""

    result: ValidationResult
    validation_stage: str


def validate_file_staged(path: Path) -> StagedValidationResult:
    candidate, findings = load_candidate(path)
    if candidate is None:
        return StagedValidationResult(
            ValidationResult("ERROR", tuple(sorted(findings))),
            "PARSE",
        )
    try:
        shape = schema_findings(candidate)
    except (OSError, json.JSONDecodeError, ValueError):
        return StagedValidationResult(
            ValidationResult("ERROR", (Finding("SCHEMA_LOAD_ERROR", "/"),)),
            "SCHEMA",
        )
    if shape:
        return StagedValidationResult(
            ValidationResult("ERROR", tuple(sorted(shape))),
            "SCHEMA",
        )
    semantic = tuple(sorted(semantic_findings(candidate)))
    return StagedValidationResult(
        ValidationResult(
            "DENY" if semantic else "PASS",
            semantic,
            str(candidate.get("ledger_id")),
        ),
        "SEMANTIC",
    )


def validate_file(path: Path) -> ValidationResult:
    """Backward-compatible result-only validation entry point."""

    return validate_file_staged(path).result


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False, {"outcome": "ERROR", "reason": "MANIFEST_UNREADABLE"}
    mismatches: list[dict[str, object]] = []
    stage_counts = {stage: 0 for stage in ("PARSE", "SCHEMA", "SEMANTIC")}
    for case in manifest.get("cases", []):
        staged = validate_file_staged(FIXTURE_ROOT / case["file"])
        result = staged.result
        stage_counts[staged.validation_stage] += 1
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        case_mismatches = evaluate_fixture_expectation(
            case,
            validation_stage=staged.validation_stage,
            outcome=result.outcome,
            findings=actual,
        )
        if case_mismatches:
            mismatches.append(
                {
                    "case_id": case.get("case_id"),
                    "validation_stage": staged.validation_stage,
                    "outcome": result.outcome,
                    "findings": actual,
                    "mismatches": [item.as_dict() for item in case_mismatches],
                }
            )
    payload = {
        "outcome": "PASS" if not mismatches else "DENY",
        "scope": SCOPE,
        "cases": len(manifest.get("cases", [])),
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "network_access": "NONE",
        "stage_counts": stage_counts,
        "mismatches": mismatches,
    }
    return not mismatches, payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True))
        return 0 if ok else 1
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    staged = validate_file_staged(args.path)
    result = staged.result
    print(
        json.dumps(
            {
                "outcome": result.outcome,
                "validation_stage": staged.validation_stage,
                "scope": SCOPE,
                "ledger_id": result.ledger_id,
                "authority": "NONE",
                "findings": [
                    {"code": item.code, "path": item.path}
                    for item in result.findings
                ],
            },
            sort_keys=True,
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
