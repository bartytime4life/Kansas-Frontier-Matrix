#!/usr/bin/env python3
"""Validate non-authoritative VerificationBacklogItem fixture records.

READY means only that a closed record is internally consistent. HOLD preserves an
unresolved item visibly. ERROR means the record is malformed or contradicts its
own declared state. No result creates evidence, activates a source, makes a
steward or governance decision, mutates repository state, promotes, releases, or
publishes.
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

from tools.validators.governance._verification_backlog_item_fixtures import (
    FIXTURE_CASE_FILES,
    load_fixture_cases,
    run_fixture_suite,
)
from tools.validators.governance._verification_backlog_item_io import (
    Evaluation,
    Finding,
    expected_item_id,
    expected_spec_hash,
)
from tools.validators.governance._verification_backlog_item_model import (
    evaluate_document,
    evaluate_path,
)

EXIT_READY = 0
EXIT_ERROR = 2
EXIT_HOLD = 3
EXIT = {"READY": EXIT_READY, "ERROR": EXIT_ERROR, "HOLD": EXIT_HOLD}

def evaluate_paths(paths: Sequence[Path]) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    rank = {"READY": 0, "HOLD": 1, "ERROR": 2}
    overall = "READY"
    seen: set[str] = set()
    for path in paths:
        document, evaluation = evaluate_path(path)
        record_id = document.get("item_id") if isinstance(document, dict) else None
        if isinstance(record_id, str) and record_id in seen:
            evaluation = Evaluation(
                "ERROR",
                tuple(sorted(set(evaluation.findings + (Finding("DUPLICATE_ITEM_ID", "$.item_id"),)))),
            )
        if isinstance(record_id, str):
            seen.add(record_id)
        if rank[evaluation.outcome] > rank[overall]:
            overall = evaluation.outcome
        rows.append(
            {
                "path": path.as_posix(),
                "item_id": record_id,
                "outcome": evaluation.outcome,
                "findings": [
                    {"code": finding.code, "field": finding.field}
                    for finding in evaluation.findings
                ],
            }
        )
    rows.sort(key=lambda row: (str(row.get("item_id") or ""), str(row["path"])))
    return {"authority": "NONE", "outcome": overall, "items": rows}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("items", nargs="*", type=Path)
    parser.add_argument("--cases", action="store_true")
    args = parser.parse_args(argv)
    if args.cases:
        if args.items:
            parser.error("--cases cannot be combined with item paths")
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if ok else EXIT_ERROR
    if not args.items:
        parser.error("provide at least one item or use --cases")
    payload = evaluate_paths(args.items)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return EXIT[str(payload["outcome"])]


if __name__ == "__main__":
    raise SystemExit(main())
