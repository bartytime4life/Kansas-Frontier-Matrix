#!/usr/bin/env python3
"""Build a deterministic, no-network KFM documentation graph QA projection.

This entrypoint maps scoped Markdown navigation, bounded KFM metadata
relationships, backlinks, entrypoint reachability, generated Maps of Content,
and optional machine document-registry parity. It does not decide doctrine,
evidence, source admissibility, policy, review, release, publication, or
Directory Rules exceptions.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

MODULE_DIR = Path(__file__).resolve().parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

from document_graph_build import _error_result, build_document_graph
from document_graph_core import DocumentGraphError, Finding, _ratchet_findings
from document_graph_parse import extract_links


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build deterministic KFM documentation graph QA."
    )
    parser.add_argument(
        "inputs", nargs="+", help="Explicit Markdown files or directories."
    )
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument(
        "--entrypoint", action="append", default=[], help="Repeatable Markdown entrypoint."
    )
    parser.add_argument("--registry", help="Optional machine document-registry path.")
    parser.add_argument("--git-diff", help="Ratchet findings to <base-sha>...HEAD.")
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Promote current warnings to failures.",
    )
    parser.add_argument(
        "--format", choices=("text", "json", "markdown"), default="text"
    )
    parser.add_argument("--output", help="Explicit output file; stdout when omitted.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = build_document_graph(
            repo_root=Path(args.repo_root),
            inputs=args.inputs,
            entrypoints=args.entrypoint,
            registry_path=args.registry,
            git_diff=args.git_diff,
            warnings_as_errors=args.warnings_as_errors,
        )
    except DocumentGraphError:
        result = _error_result()
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
