"""Command-line and finite authority output."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from .fixtures import replay_fixtures
from .model import ROOT, SCOPE, ValidationResult
from .rules import validate_file


def _serialize(
    result: ValidationResult,
    *,
    path: Path | None = None,
    case: str | None = None,
) -> str:
    payload: dict[str, Any] = {
        "outcome": result.outcome,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "scope": SCOPE,
        "authority": {
            key: False
            for key in (
                "context_map_change",
                "schema_change",
                "api_change",
                "policy_evaluation",
                "review_approval",
                "adoption",
                "release",
                "publication",
                "public_use",
            )
        },
    }
    if path is not None:
        try:
            payload["file"] = path.resolve().relative_to(ROOT.resolve()).as_posix()
        except (OSError, ValueError):
            payload["file"] = path.name
    if case is not None:
        payload["case"] = case
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate an inactive PublishedLanguageReview candidate."
    )
    parser.add_argument("file", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(list(sys.argv[1:] if argv is None else argv))
    if args.fixtures and args.file is not None:
        print("--fixtures cannot be combined with a file", file=sys.stderr)
        return 2
    if args.fixtures:
        return replay_fixtures()
    if args.file is None:
        print("a fixture file or --fixtures is required", file=sys.stderr)
        return 2
    result = validate_file(args.file)
    print(_serialize(result, path=args.file))
    return 0 if result.ok else 1
