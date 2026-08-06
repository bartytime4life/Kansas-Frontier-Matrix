#!/usr/bin/env python3
"""Validate bounded KFM documentation metadata blocks without network access.

This entrypoint validates explicitly scoped ``KFM_META_BLOCK_V2`` envelopes and
can emit a deterministic, review-only machine document-registry delta. It never
edits documentation or the registry and never decides doctrine, evidence,
policy, review, release, or publication authority.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

MODULE_DIR = Path(__file__).resolve().parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

from meta_block_build import _error_result, validate_meta_blocks
from meta_block_core import (
    PROFILE_PRESENT, PROFILE_REQUIRED, MetaBlockError, MetaBlockResult,
)

def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate bounded KFM documentation metadata blocks."
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        help="Explicit Markdown files or directories.",
    )
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument(
        "--profile",
        choices=(PROFILE_PRESENT, PROFILE_REQUIRED),
        default=PROFILE_PRESENT,
        help="present validates blocks when found; required also fails on absence.",
    )
    parser.add_argument("--registry", help="Optional machine document-registry path.")
    parser.add_argument("--git-diff", help="Ratchet findings to <base-sha>...HEAD.")
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Promote current warnings to failures.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json", "markdown"),
        default="text",
    )
    parser.add_argument("--output", help="Explicit report output; stdout when omitted.")
    parser.add_argument(
        "--registry-delta-output",
        help="Optional review-only registry-delta JSON output path.",
    )
    return parser


def _write_output(path: Path, content: str) -> None:
    if path.exists() and path.is_symlink():
        raise MetaBlockError("output symbolic link denied")
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            content + ("" if content.endswith("\n") else "\n"),
            encoding="utf-8",
        )
    except (OSError, UnicodeError) as error:
        raise MetaBlockError("output could not be written safely") from error


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = validate_meta_blocks(
            repo_root=Path(args.repo_root),
            inputs=args.inputs,
            profile=args.profile,
            registry_path=args.registry,
            git_diff=args.git_diff,
            warnings_as_errors=args.warnings_as_errors,
        )
        rendered = (
            result.to_json()
            if args.format == "json"
            else result.to_markdown()
            if args.format == "markdown"
            else result.to_text()
        )
        if args.output:
            _write_output(Path(args.output), rendered)
        else:
            print(rendered)
        if args.registry_delta_output:
            _write_output(
                Path(args.registry_delta_output), result.registry_delta_json()
            )
        return result.exit_code
    except MetaBlockError:
        result = _error_result(args.profile)
        print(result.to_text(), file=sys.stderr)
        return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
