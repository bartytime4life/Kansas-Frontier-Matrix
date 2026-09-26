"""Route a checkout-local diff command to the existing comparison tools."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path


def main(argv: Sequence[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    parser = argparse.ArgumentParser(
        prog="kfm diff", description="Compare local JSON; no release or policy decision."
    )
    parser.add_argument("kind", choices=("json", "release"))
    if argv and argv[0] in ("json", "release"):
        kind, rest = argv[0], argv[1:]
    else:
        parser.parse_args(argv)
        return 2

    # The CLI is checkout-local: the comparators live at the repo tooling root.
    root = Path(__file__).resolve().parents[5]
    if not (root / "tools" / "diff" / "stable_diff.py").is_file():
        parser.error("comparison tools are unavailable in this checkout")
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    if kind == "json":
        from tools.diff import stable_diff

        return stable_diff.main(rest)

    from tools.diff import release_diff

    return release_diff.main(rest)
