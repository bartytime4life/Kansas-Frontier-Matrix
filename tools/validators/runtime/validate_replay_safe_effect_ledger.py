"""Validate synthetic replay-safe event/effect ledger candidates; PASS grants no authority."""
from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
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
from tools.validators.runtime.replay_safe_effect_ledger_semantics import semantic_findings


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = load_candidate(path)
    if candidate is None:
        return ValidationResult("ERROR", tuple(sorted(findings)))
    try:
        shape = schema_findings(candidate)
    except (OSError, json.JSONDecodeError, ValueError):
        return ValidationResult("ERROR", (Finding("SCHEMA_LOAD_ERROR", "/"),))
    if shape:
        return ValidationResult("ERROR", tuple(sorted(shape)))
    semantic = tuple(sorted(semantic_findings(candidate)))
    return ValidationResult(
        "DENY" if semantic else "PASS",
        semantic,
        str(candidate.get("ledger_id")),
    )


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False, {"outcome": "ERROR", "reason": "MANIFEST_UNREADABLE"}
    mismatches: list[dict[str, object]] = []
    for case in manifest.get("cases", []):
        result = validate_file(FIXTURE_ROOT / case["file"])
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            mismatches.append(
                {
                    "case_id": case["case_id"],
                    "outcome": result.outcome,
                    "findings": actual,
                }
            )
    payload = {
        "outcome": "PASS" if not mismatches else "DENY",
        "scope": SCOPE,
        "cases": len(manifest.get("cases", [])),
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "network_access": "NONE",
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
    result = validate_file(args.path)
    print(
        json.dumps(
            {
                "outcome": result.outcome,
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
