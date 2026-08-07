#!/usr/bin/env python3
"""Run bounded, deterministic KFM documentation freshness QA."""

from __future__ import annotations

import argparse
import os
import sys
from datetime import date
from pathlib import Path
from typing import Sequence

MODULE_DIR = Path(__file__).resolve().parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

from stale_scan_build import parse_type_windows, scan_stale_docs
from stale_scan_core import StaleScanError, error_result


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Scan explicitly scoped KFM Markdown for bounded freshness signals."
    )
    parser.add_argument("inputs", nargs="+", help="Markdown files or directories.")
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument(
        "--as-of",
        default=os.environ.get("KFM_DOCS_AS_OF"),
        help="Required ISO date (or KFM_DOCS_AS_OF) used for deterministic age checks.",
    )
    parser.add_argument(
        "--profile",
        choices=("advisory", "bounded-required"),
        default="advisory",
    )
    parser.add_argument("--review-window-days", type=int, default=365)
    parser.add_argument("--placeholder-grace-days", type=int, default=90)
    parser.add_argument(
        "--type-window",
        action="append",
        default=[],
        metavar="TYPE=DAYS",
        help="Repeatable type-specific review window.",
    )
    parser.add_argument("--git-diff", help="Ratchet findings to <base>...HEAD.")
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Promote current warnings only; historical debt remains warning-only.",
    )
    parser.add_argument(
        "--format", choices=("text", "json", "markdown"), default="text"
    )
    parser.add_argument("--output", help="Explicit output file; stdout when omitted.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    fallback_as_of = args.as_of or "1970-01-01"
    try:
        if not args.as_of:
            raise StaleScanError("--as-of or KFM_DOCS_AS_OF is required")
        as_of = date.fromisoformat(args.as_of)
        type_windows = parse_type_windows(args.type_window)
        result = scan_stale_docs(
            repo_root=Path(args.repo_root),
            inputs=args.inputs,
            as_of=as_of,
            profile=args.profile,
            review_window_days=args.review_window_days,
            placeholder_grace_days=args.placeholder_grace_days,
            type_windows=type_windows,
            git_diff=args.git_diff,
            warnings_as_errors=args.warnings_as_errors,
        )
    except (StaleScanError, ValueError) as exc:
        result = error_result(
            as_of=fallback_as_of,
            profile=args.profile,
            message=str(exc) or "bounded stale scan failed",
        )

    rendered = (
        result.to_json()
        if args.format == "json"
        else result.to_markdown()
        if args.format == "markdown"
        else result.to_text()
    )
    if args.output:
        output = Path(args.output)
        if output.exists() and output.is_symlink():
            print("ERROR output symbolic link denied", file=sys.stderr)
            return 2
        try:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(
                rendered + ("" if rendered.endswith("\n") else "\n"),
                encoding="utf-8",
            )
        except (OSError, UnicodeError):
            print("ERROR output could not be written safely", file=sys.stderr)
            return 2
    else:
        print(rendered)
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
