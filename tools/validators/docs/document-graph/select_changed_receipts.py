#!/usr/bin/env python3
"""Select changed GENERATED_RECEIPT candidates for current-byte validation.

The selector is intentionally narrow: it reads local Git history, returns only
added, copied, modified, or renamed JSON receipt paths under the canonical
generated-receipt lane, and emits NUL-delimited paths for safe shell consumption.
It performs no receipt validation and makes no network request.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Sequence

GENERATED_RECEIPT_ROOT = "data/receipts/generated"
GENERATED_RECEIPT_PATHSPEC = f":(glob){GENERATED_RECEIPT_ROOT}/*.json"


class SelectionError(RuntimeError):
    """Raised when changed-receipt selection cannot complete safely."""


def _run_git(repo_root: Path, arguments: Sequence[str]) -> bytes:
    result = subprocess.run(
        ["git", *arguments],
        cwd=repo_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        command = "git " + " ".join(arguments)
        raise SelectionError(
            f"{command} failed with exit {result.returncode}: {detail or 'no stderr'}"
        )
    return result.stdout


def _validate_ref(repo_root: Path, ref: str, label: str) -> None:
    if not ref or ref.startswith("-") or "\x00" in ref or any(ch.isspace() for ch in ref):
        raise SelectionError(f"{label} is not a safe non-empty Git revision")
    _run_git(
        repo_root,
        ["rev-parse", "--verify", "--quiet", "--end-of-options", f"{ref}^{{commit}}"],
    )


def _validate_prefix(prefix: str) -> str:
    if not prefix or "\x00" in prefix or "\\" in prefix:
        raise SelectionError("prefix must be a non-empty repository-relative POSIX path")
    candidate = PurePosixPath(prefix)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise SelectionError("prefix must not be absolute or escape the repository")
    normalized = candidate.as_posix()
    required_prefix = GENERATED_RECEIPT_ROOT + "/"
    if not normalized.startswith(required_prefix):
        raise SelectionError(
            f"prefix must remain under {GENERATED_RECEIPT_ROOT}/"
        )
    return normalized


def changed_receipt_paths(
    repo_root: Path,
    *,
    base_ref: str,
    head_ref: str,
    mode: str,
    prefix: str,
) -> list[str]:
    """Return current receipt candidates changed between two verified commits."""

    resolved_root = repo_root.resolve()
    if not resolved_root.is_dir():
        raise SelectionError(f"repository root is not a directory: {repo_root}")

    _validate_ref(resolved_root, base_ref, "base_ref")
    _validate_ref(resolved_root, head_ref, "head_ref")
    normalized_prefix = _validate_prefix(prefix)

    if mode == "merge-base":
        revision_range = f"{base_ref}...{head_ref}"
    elif mode == "direct":
        revision_range = f"{base_ref}..{head_ref}"
    else:
        raise SelectionError("mode must be 'merge-base' or 'direct'")

    output = _run_git(
        resolved_root,
        [
            "diff",
            "--name-only",
            "-z",
            "--find-renames",
            "--diff-filter=ACMR",
            revision_range,
            "--",
            GENERATED_RECEIPT_PATHSPEC,
        ],
    )

    selected: set[str] = set()
    for raw_path in output.split(b"\0"):
        if not raw_path:
            continue
        try:
            path_text = raw_path.decode("utf-8", errors="strict")
        except UnicodeDecodeError as exc:
            raise SelectionError("Git returned a non-UTF-8 receipt path") from exc

        path = PurePosixPath(path_text)
        if path.is_absolute() or ".." in path.parts or "\\" in path_text:
            raise SelectionError(f"Git returned an unsafe path: {path_text!r}")

        normalized_path = path.as_posix()
        if not normalized_path.startswith(normalized_prefix):
            continue
        if not normalized_path.endswith(".json"):
            continue

        candidate = resolved_root / normalized_path
        if candidate.is_symlink():
            raise SelectionError(
                f"changed generated receipt must not be a symbolic link: {normalized_path}"
            )
        if not candidate.is_file():
            continue
        selected.add(normalized_path)

    return sorted(selected)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Emit NUL-delimited added/copied/modified/renamed generated-receipt "
            "paths from a bounded local Git range."
        )
    )
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--base", required=True, help="Verified base commit or ref")
    parser.add_argument("--head", default="HEAD", help="Verified head commit or ref")
    parser.add_argument(
        "--mode",
        choices=("direct", "merge-base"),
        default="direct",
        help="Use base..head or base...head Git diff semantics",
    )
    parser.add_argument(
        "--prefix",
        required=True,
        help=(
            "Repository-relative receipt-path prefix under "
            "data/receipts/generated/"
        ),
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        paths = changed_receipt_paths(
            args.repo_root,
            base_ref=args.base,
            head_ref=args.head,
            mode=args.mode,
            prefix=args.prefix,
        )
    except SelectionError as exc:
        print(f"CHANGED_RECEIPT_SELECTION_ERROR detail={exc}", file=sys.stderr)
        return 2

    for path in paths:
        sys.stdout.buffer.write(path.encode("utf-8") + b"\0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
